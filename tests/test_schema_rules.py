"""Checks that the schema agrees with the OSCAL release it is pinned to."""

import importlib.util
import re
import xml.etree.ElementTree as ET
from collections import Counter
from functools import lru_cache
from pathlib import Path

import yaml

ROOT = Path(__file__).parent.parent
SCHEMA_DIR = ROOT / "src" / "oscal" / "schema"
SCHEMA = SCHEMA_DIR / "oscal.yaml"
MODULES = sorted(SCHEMA_DIR.glob("oscal*.yaml"))
METASCHEMA = SCHEMA_DIR / "metaschema"
NS = "{http://csrc.nist.gov/ns/oscal/metaschema/1.0}"
ENTITY = re.compile(r'<!ENTITY\s+([\w.-]+)\s+SYSTEM\s+"([^"]+)"\s*>')


def _watch():
    spec = importlib.util.spec_from_file_location(
        "watch", ROOT / "scripts" / "check_upstream_release.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _load(path):
    """A metaschema file with its shared-constraint entities written in.

    The files declare each entity as a SYSTEM file beside them. The text is
    substituted by hand, so the parser resolves no external entity."""
    text = path.read_text(encoding="utf-8")
    entities = {
        m.group(1): (path.parent / m.group(2)).read_text(encoding="utf-8")
        for m in ENTITY.finditer(text)
    }
    text = re.sub(r"<!DOCTYPE[^\[]*\[.*?\]>", "", text, flags=re.S)
    for name, body in entities.items():
        text = text.replace(f"&{name};", re.sub(r"<\?xml[^>]*\?>", "", body))
    return ET.fromstring(text.encode("utf-8"))


@lru_cache(maxsize=1)
def _allowed_values():
    """Every allowed-values list in the copy: its key, whether it admits
    other values, and its values.

    A list is keyed by its id. OSCAL reuses four ids in two definitions each,
    so such a list is keyed id@definition, after the nearest named definition
    around it; one with no id is keyed file#definition path#target. Two lists
    under one key constrain the same node, and metaschema joins their values."""
    found = []
    for path in sorted(METASCHEMA.glob("*_metaschema.xml")):
        root = _load(path)
        parents = {child: parent for parent in root.iter() for child in parent}
        for av in root.iter(f"{NS}allowed-values"):
            names, node = [], parents.get(av)
            while node is not None:
                if node.get("name"):
                    names.append(node.get("name"))
                node = parents.get(node)
            values = [e.get("value") for e in av.findall(f"{NS}enum")]
            found.append(
                (
                    av.get("id"),
                    path.name,
                    names,
                    av.get("target", "."),
                    av.get("allow-other") == "yes",
                    values,
                )
            )
    ids = Counter(id_ for id_, *_ in found if id_)
    lists = {}
    for id_, name, names, target, open_, values in found:
        if id_ and ids[id_] == 1:
            key = id_
        elif id_:
            key = f"{id_}@{names[0]}"
        else:
            key = f"{name}#{'/'.join(reversed(names))}#{target}"
        was_open, was = lists.get(key, (False, []))
        lists[key] = (was_open or open_, was + [v for v in values if v not in was])
    return lists


def _enums():
    """Each enum of every module, by name."""
    enums = {}
    for module in MODULES:
        for name, enum in (
            yaml.safe_load(module.read_text()).get("enums") or {}
        ).items():
            enums[name] = enum or {}
    return enums


def test_header_pins_match_the_watch():
    """The header records the release and commit the upstream watch checks."""
    watch = _watch()
    header = yaml.safe_load(SCHEMA.read_text())
    notes = header["annotations"]
    assert notes["oscal_tag"] == watch.PINNED_TAG == f"v{header['version']}"
    assert notes["oscal_commit"] == watch.PINNED_COMMIT
    assert f"/tree/{watch.PINNED_COMMIT}/{watch.PINNED_PATH}" in header["source"]


def test_modules_carry_the_pinned_version():
    """Every module names the release the umbrella does, and each module's
    source is that release's JSON schema."""
    version = yaml.safe_load(SCHEMA.read_text())["version"]
    for module in MODULES:
        header = yaml.safe_load(module.read_text())
        assert str(header["version"]) == version, module.name
        if module != SCHEMA:
            assert f"/ns/oscal/{version}/" in header["source"], module.name


def test_modules_share_the_oscal_namespace():
    """Every module's id lies under the umbrella's, and every element takes
    the one oscal prefix, which the repository's w3id route covers."""
    umbrella = yaml.safe_load(SCHEMA.read_text())
    namespace = umbrella["prefixes"]["oscal"]
    assert namespace == umbrella["id"] + "/"
    for module in MODULES:
        header = yaml.safe_load(module.read_text())
        assert header["default_prefix"] == "oscal", module.name
        assert header["prefixes"]["oscal"] == namespace, module.name
        if module != SCHEMA:
            assert header["id"] == namespace + header["name"], module.name

def test_every_enum_names_its_lists():
    """Each enum names, in its oscal_allowed_values annotation, the
    metaschema lists it renders, and each name is a list of the copy."""
    lists = _allowed_values()
    for name, enum in _enums().items():
        keys = str(
            (enum.get("annotations") or {}).get("oscal_allowed_values", "")
        ).split()
        assert keys, name
        for key in keys:
            assert key in lists, (name, key)


def test_enums_render_the_pinned_metaschema():
    """An enum holds exactly the values of the lists it names, and admits
    other values (allow_any) exactly when one of them does. OSCAL 1.2.3 lists
    a blank location type marked TBD, which the schema leaves out."""
    lists = _allowed_values()
    for name, enum in _enums().items():
        notes = enum.get("annotations") or {}
        keys = str(notes["oscal_allowed_values"]).split()
        theirs = {v for key in keys for v in lists[key][1] if v.strip()}
        ours = set(enum.get("permissible_values") or {})
        assert ours == theirs, (name, sorted(ours - theirs), sorted(theirs - ours))
        assert bool(notes.get("allow_any")) == any(lists[key][0] for key in keys), name
