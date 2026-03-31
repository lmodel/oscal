# Auto generated from oscal.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-03-31T15:51:55
# Schema: oscal
#
# id: https://w3id.org/lmodel/oscal
# description: OSCAL: Open Security Controls Assessment Language: LinkML Schema
# license: Apache-2.0

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Boolean, Float, String
from linkml_runtime.utils.metamodelcore import Bool

metamodel_version = "1.7.0"
version = "1.2.1"

# Namespaces
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
OSCAL = CurieNamespace('oscal', 'https://w3id.org/lmodel/oscal/')
OSCAL_ASSESSMENT_PLAN = CurieNamespace('oscal_assessment_plan', 'https://w3id.org/lmodel/oscal_assessment_plan/')
OSCAL_ASSESSMENT_RESULTS = CurieNamespace('oscal_assessment_results', 'https://w3id.org/lmodel/oscal_assessment_results/')
OSCAL_CATALOG = CurieNamespace('oscal_catalog', 'https://w3id.org/lmodel/oscal_catalog/')
OSCAL_COMPONENT = CurieNamespace('oscal_component', 'https://w3id.org/lmodel/oscal_component/')
OSCAL_MAPPING = CurieNamespace('oscal_mapping', 'https://w3id.org/lmodel/oscal_mapping/')
OSCAL_POAM = CurieNamespace('oscal_poam', 'https://w3id.org/lmodel/oscal_poam/')
OSCAL_PROFILE = CurieNamespace('oscal_profile', 'https://w3id.org/lmodel/oscal_profile/')
OSCAL_SSP = CurieNamespace('oscal_ssp', 'https://w3id.org/lmodel/oscal_ssp/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = OSCAL


# Types
class UUIDType(str):
    """ A type 4 or type 5 UUID per RFC 4122. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "UUIDType"
    type_model_uri = OSCAL.UUIDType


class URIType(str):
    """ A universal resource identifier formatted according to RFC3986. """
    type_class_uri = XSD["anyURI"]
    type_class_curie = "xsd:anyURI"
    type_name = "URIType"
    type_model_uri = OSCAL.URIType


class URIReferenceType(str):
    """ A URI Reference, either a URI or relative-reference, per RFC3986. """
    type_class_uri = XSD["anyURI"]
    type_class_curie = "xsd:anyURI"
    type_name = "URIReferenceType"
    type_model_uri = OSCAL.URIReferenceType


class DateTimeWithTimezoneType(str):
    """ A string representing a point in time with a required timezone. """
    type_class_uri = XSD["dateTime"]
    type_class_curie = "xsd:dateTime"
    type_name = "DateTimeWithTimezoneType"
    type_model_uri = OSCAL.DateTimeWithTimezoneType


class MarkupLineType(str):
    """ A single line of Markdown content (no newlines). """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "MarkupLineType"
    type_model_uri = OSCAL.MarkupLineType


class MarkupMultilineType(str):
    """ Multiple lines of Markdown content. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "MarkupMultilineType"
    type_model_uri = OSCAL.MarkupMultilineType


class TokenType(str):
    """ A non-colonized XML NCName token. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "TokenType"
    type_model_uri = OSCAL.TokenType


class Base64Type(str):
    """ Binary data encoded using Base64 as defined by RFC4648. """
    type_class_uri = XSD["base64Binary"]
    type_class_curie = "xsd:base64Binary"
    type_name = "Base64Type"
    type_model_uri = OSCAL.Base64Type


class EmailAddressType(str):
    """ An email address string formatted according to RFC 6531. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "EmailAddressType"
    type_model_uri = OSCAL.EmailAddressType


class NonNegativeIntegerType(int):
    """ A non-negative integer value (>= 0), as used for port range boundaries. """
    type_class_uri = XSD["nonNegativeInteger"]
    type_class_curie = "xsd:nonNegativeInteger"
    type_name = "NonNegativeIntegerType"
    type_model_uri = OSCAL.NonNegativeIntegerType


class PositiveIntegerType(int):
    """ A positive integer value (>= 1), as used for task recurrence periods. """
    type_class_uri = XSD["positiveInteger"]
    type_class_curie = "xsd:positiveInteger"
    type_name = "PositiveIntegerType"
    type_model_uri = OSCAL.PositiveIntegerType


# Class references



@dataclass(repr=False)
class HasPropsAndLinks(YAMLRoot):
    """
    Mixin providing the props and links slots that are common to many OSCAL objects.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["HasPropsAndLinks"]
    class_class_curie: ClassVar[str] = "oscal_catalog:HasPropsAndLinks"
    class_name: ClassVar[str] = "HasPropsAndLinks"
    class_model_uri: ClassVar[URIRef] = OSCAL.HasPropsAndLinks

    props: Optional[Union[Union[dict, "Property"], list[Union[dict, "Property"]]]] = empty_list()
    links: Optional[Union[Union[dict, "Link"], list[Union[dict, "Link"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="props", slot_type=Property, key_name="name", keyed=False)

        self._normalize_inlined_as_list(slot_name="links", slot_type=Link, key_name="href", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OscalCommon(YAMLRoot):
    """
    Mixin providing props, links, and remarks slots common to most OSCAL objects. Extends HasPropsAndLinks.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["OscalCommon"]
    class_class_curie: ClassVar[str] = "oscal_catalog:OscalCommon"
    class_name: ClassVar[str] = "OscalCommon"
    class_model_uri: ClassVar[URIRef] = OSCAL.OscalCommon

    remarks: Optional[str] = None
    props: Optional[Union[Union[dict, "Property"], list[Union[dict, "Property"]]]] = empty_list()
    links: Optional[Union[Union[dict, "Link"], list[Union[dict, "Link"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        self._normalize_inlined_as_list(slot_name="props", slot_type=Property, key_name="name", keyed=False)

        self._normalize_inlined_as_list(slot_name="links", slot_type=Link, key_name="href", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HasResponsibleRoles(YAMLRoot):
    """
    Mixin providing the responsible-roles slot for objects that carry role assignments.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["HasResponsibleRoles"]
    class_class_curie: ClassVar[str] = "oscal_catalog:HasResponsibleRoles"
    class_name: ClassVar[str] = "HasResponsibleRoles"
    class_model_uri: ClassVar[URIRef] = OSCAL.HasResponsibleRoles

    responsible_roles: Optional[Union[Union[dict, "ResponsibleRole"], list[Union[dict, "ResponsibleRole"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="responsible_roles", slot_type=ResponsibleRole, key_name="role-id", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HasResponsibleParties(YAMLRoot):
    """
    Mixin providing the responsible-parties slot for objects that carry party assignments.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["HasResponsibleParties"]
    class_class_curie: ClassVar[str] = "oscal_catalog:HasResponsibleParties"
    class_name: ClassVar[str] = "HasResponsibleParties"
    class_model_uri: ClassVar[URIRef] = OSCAL.HasResponsibleParties

    responsible_parties: Optional[Union[Union[dict, "ResponsibleParty"], list[Union[dict, "ResponsibleParty"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="responsible_parties", slot_type=ResponsibleParty, key_name="role-id", keyed=False)

        super().__post_init__(**kwargs)


class OscalDocument(YAMLRoot):
    """
    A root wrapper for an OSCAL document, which may be of any OSCAL document type (e.g. Catalog, Profile, Assessment
    Plan, SSP).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["OscalDocument"]
    class_class_curie: ClassVar[str] = "oscal_catalog:OscalDocument"
    class_name: ClassVar[str] = "OscalDocument"
    class_model_uri: ClassVar[URIRef] = OSCAL.OscalDocument


@dataclass(repr=False)
class CatalogDocument(OscalDocument):
    """
    Root wrapper for an OSCAL Catalog document.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["CatalogDocument"]
    class_class_curie: ClassVar[str] = "oscal_catalog:CatalogDocument"
    class_name: ClassVar[str] = "CatalogDocument"
    class_model_uri: ClassVar[URIRef] = OSCAL.CatalogDocument

    catalog: Union[dict, "Catalog"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.catalog):
            self.MissingRequiredField("catalog")
        if not isinstance(self.catalog, Catalog):
            self.catalog = Catalog(**as_dict(self.catalog))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Catalog(YAMLRoot):
    """
    A structured, organized collection of control information.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["Catalog"]
    class_class_curie: ClassVar[str] = "oscal_catalog:Catalog"
    class_name: ClassVar[str] = "Catalog"
    class_model_uri: ClassVar[URIRef] = OSCAL.Catalog

    uuid: str = None
    metadata: Union[dict, "Metadata"] = None
    back_matter: Optional[Union[dict, "BackMatter"]] = None
    params: Optional[Union[Union[dict, "Parameter"], list[Union[dict, "Parameter"]]]] = empty_list()
    controls: Optional[Union[Union[dict, "Control"], list[Union[dict, "Control"]]]] = empty_list()
    groups: Optional[Union[Union[dict, "Group"], list[Union[dict, "Group"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uuid):
            self.MissingRequiredField("uuid")
        if not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        if self._is_empty(self.metadata):
            self.MissingRequiredField("metadata")
        if not isinstance(self.metadata, Metadata):
            self.metadata = Metadata(**as_dict(self.metadata))

        if self.back_matter is not None and not isinstance(self.back_matter, BackMatter):
            self.back_matter = BackMatter(**as_dict(self.back_matter))

        self._normalize_inlined_as_list(slot_name="params", slot_type=Parameter, key_name="id", keyed=False)

        self._normalize_inlined_as_list(slot_name="controls", slot_type=Control, key_name="id", keyed=False)

        self._normalize_inlined_as_list(slot_name="groups", slot_type=Group, key_name="title", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Group(YAMLRoot):
    """
    A group of controls, or of groups of controls.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["Group"]
    class_class_curie: ClassVar[str] = "oscal_catalog:Group"
    class_name: ClassVar[str] = "Group"
    class_model_uri: ClassVar[URIRef] = OSCAL.Group

    title: str = None
    id: Optional[str] = None
    _class: Optional[str] = None
    params: Optional[Union[Union[dict, "Parameter"], list[Union[dict, "Parameter"]]]] = empty_list()
    parts: Optional[Union[Union[dict, "Part"], list[Union[dict, "Part"]]]] = empty_list()
    groups: Optional[Union[Union[dict, "Group"], list[Union[dict, "Group"]]]] = empty_list()
    controls: Optional[Union[Union[dict, "Control"], list[Union[dict, "Control"]]]] = empty_list()
    props: Optional[Union[Union[dict, "Property"], list[Union[dict, "Property"]]]] = empty_list()
    links: Optional[Union[Union[dict, "Link"], list[Union[dict, "Link"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self.id is not None and not isinstance(self.id, str):
            self.id = str(self.id)

        if self._class is not None and not isinstance(self._class, str):
            self._class = str(self._class)

        self._normalize_inlined_as_list(slot_name="params", slot_type=Parameter, key_name="id", keyed=False)

        self._normalize_inlined_as_list(slot_name="parts", slot_type=Part, key_name="name", keyed=False)

        self._normalize_inlined_as_list(slot_name="groups", slot_type=Group, key_name="title", keyed=False)

        self._normalize_inlined_as_list(slot_name="controls", slot_type=Control, key_name="id", keyed=False)

        self._normalize_inlined_as_list(slot_name="props", slot_type=Property, key_name="name", keyed=False)

        self._normalize_inlined_as_list(slot_name="links", slot_type=Link, key_name="href", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Control(YAMLRoot):
    """
    A structured object representing a requirement or guideline, which when implemented will reduce an aspect of risk
    related to an information system and its information.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["Control"]
    class_class_curie: ClassVar[str] = "oscal_catalog:Control"
    class_name: ClassVar[str] = "Control"
    class_model_uri: ClassVar[URIRef] = OSCAL.Control

    id: str = None
    title: str = None
    _class: Optional[str] = None
    params: Optional[Union[Union[dict, "Parameter"], list[Union[dict, "Parameter"]]]] = empty_list()
    parts: Optional[Union[Union[dict, "Part"], list[Union[dict, "Part"]]]] = empty_list()
    controls: Optional[Union[Union[dict, "Control"], list[Union[dict, "Control"]]]] = empty_list()
    props: Optional[Union[Union[dict, "Property"], list[Union[dict, "Property"]]]] = empty_list()
    links: Optional[Union[Union[dict, "Link"], list[Union[dict, "Link"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self._class is not None and not isinstance(self._class, str):
            self._class = str(self._class)

        self._normalize_inlined_as_list(slot_name="params", slot_type=Parameter, key_name="id", keyed=False)

        self._normalize_inlined_as_list(slot_name="parts", slot_type=Part, key_name="name", keyed=False)

        self._normalize_inlined_as_list(slot_name="controls", slot_type=Control, key_name="id", keyed=False)

        self._normalize_inlined_as_list(slot_name="props", slot_type=Property, key_name="name", keyed=False)

        self._normalize_inlined_as_list(slot_name="links", slot_type=Link, key_name="href", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Metadata(YAMLRoot):
    """
    Provides information about the containing document, and defines concepts shared across the document.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["Metadata"]
    class_class_curie: ClassVar[str] = "oscal_catalog:Metadata"
    class_name: ClassVar[str] = "Metadata"
    class_model_uri: ClassVar[URIRef] = OSCAL.Metadata

    title: str = None
    last_modified: str = None
    version: str = None
    oscal_version: str = None
    published: Optional[str] = None
    document_ids: Optional[Union[Union[dict, "DocumentId"], list[Union[dict, "DocumentId"]]]] = empty_list()
    revisions: Optional[Union[Union[dict, "Revision"], list[Union[dict, "Revision"]]]] = empty_list()
    roles: Optional[Union[Union[dict, "Role"], list[Union[dict, "Role"]]]] = empty_list()
    locations: Optional[Union[Union[dict, "Location"], list[Union[dict, "Location"]]]] = empty_list()
    parties: Optional[Union[Union[dict, "Party"], list[Union[dict, "Party"]]]] = empty_list()
    actions: Optional[Union[Union[dict, "Action"], list[Union[dict, "Action"]]]] = empty_list()
    props: Optional[Union[Union[dict, "MetadataProperty"], list[Union[dict, "MetadataProperty"]]]] = empty_list()
    links: Optional[Union[Union[dict, "Link"], list[Union[dict, "Link"]]]] = empty_list()
    remarks: Optional[str] = None
    responsible_parties: Optional[Union[Union[dict, "ResponsibleParty"], list[Union[dict, "ResponsibleParty"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self._is_empty(self.last_modified):
            self.MissingRequiredField("last_modified")
        if not isinstance(self.last_modified, str):
            self.last_modified = str(self.last_modified)

        if self._is_empty(self.version):
            self.MissingRequiredField("version")
        if not isinstance(self.version, str):
            self.version = str(self.version)

        if self._is_empty(self.oscal_version):
            self.MissingRequiredField("oscal_version")
        if not isinstance(self.oscal_version, str):
            self.oscal_version = str(self.oscal_version)

        if self.published is not None and not isinstance(self.published, str):
            self.published = str(self.published)

        self._normalize_inlined_as_list(slot_name="document_ids", slot_type=DocumentId, key_name="identifier", keyed=False)

        self._normalize_inlined_as_list(slot_name="revisions", slot_type=Revision, key_name="version", keyed=False)

        self._normalize_inlined_as_list(slot_name="roles", slot_type=Role, key_name="id", keyed=False)

        self._normalize_inlined_as_list(slot_name="locations", slot_type=Location, key_name="uuid", keyed=False)

        self._normalize_inlined_as_list(slot_name="parties", slot_type=Party, key_name="uuid", keyed=False)

        self._normalize_inlined_as_list(slot_name="actions", slot_type=Action, key_name="uuid", keyed=False)

        self._normalize_inlined_as_list(slot_name="props", slot_type=MetadataProperty, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="links", slot_type=Link, key_name="href", keyed=False)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        self._normalize_inlined_as_list(slot_name="responsible_parties", slot_type=ResponsibleParty, key_name="role-id", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Revision(YAMLRoot):
    """
    An entry in a sequential list of revisions to the containing document.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["Revision"]
    class_class_curie: ClassVar[str] = "oscal_catalog:Revision"
    class_name: ClassVar[str] = "Revision"
    class_model_uri: ClassVar[URIRef] = OSCAL.Revision

    version: str = None
    title: Optional[str] = None
    published: Optional[str] = None
    last_modified: Optional[str] = None
    oscal_version: Optional[str] = None
    props: Optional[Union[Union[dict, "RevisionProperty"], list[Union[dict, "RevisionProperty"]]]] = empty_list()
    links: Optional[Union[Union[dict, "Link"], list[Union[dict, "Link"]]]] = empty_list()
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.version):
            self.MissingRequiredField("version")
        if not isinstance(self.version, str):
            self.version = str(self.version)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.published is not None and not isinstance(self.published, str):
            self.published = str(self.published)

        if self.last_modified is not None and not isinstance(self.last_modified, str):
            self.last_modified = str(self.last_modified)

        if self.oscal_version is not None and not isinstance(self.oscal_version, str):
            self.oscal_version = str(self.oscal_version)

        self._normalize_inlined_as_list(slot_name="props", slot_type=RevisionProperty, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="links", slot_type=Link, key_name="href", keyed=False)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DocumentId(YAMLRoot):
    """
    A document identifier qualified by an identifier scheme.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["DocumentId"]
    class_class_curie: ClassVar[str] = "oscal_catalog:DocumentId"
    class_name: ClassVar[str] = "DocumentId"
    class_model_uri: ClassVar[URIRef] = OSCAL.DocumentId

    identifier: str = None
    scheme: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.identifier):
            self.MissingRequiredField("identifier")
        if not isinstance(self.identifier, str):
            self.identifier = str(self.identifier)

        if self.scheme is not None and not isinstance(self.scheme, str):
            self.scheme = str(self.scheme)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Role(YAMLRoot):
    """
    Defines a function, which might be assigned to a party in a specific situation.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["Role"]
    class_class_curie: ClassVar[str] = "oscal_catalog:Role"
    class_name: ClassVar[str] = "Role"
    class_model_uri: ClassVar[URIRef] = OSCAL.Role

    id: str = None
    title: str = None
    short_name: Optional[str] = None
    description: Optional[str] = None
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self.short_name is not None and not isinstance(self.short_name, str):
            self.short_name = str(self.short_name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Location(YAMLRoot):
    """
    A physical point of presence, which may be associated with people, organizations, or other concepts within the
    current or linked OSCAL document.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["Location"]
    class_class_curie: ClassVar[str] = "oscal_catalog:Location"
    class_name: ClassVar[str] = "Location"
    class_model_uri: ClassVar[URIRef] = OSCAL.Location

    uuid: str = None
    title: Optional[str] = None
    email_addresses: Optional[Union[str, list[str]]] = empty_list()
    telephone_numbers: Optional[Union[Union[dict, "TelephoneNumber"], list[Union[dict, "TelephoneNumber"]]]] = empty_list()
    address: Optional[Union[dict, "Address"]] = None
    urls: Optional[Union[str, list[str]]] = empty_list()
    props: Optional[Union[Union[dict, "LocationProperty"], list[Union[dict, "LocationProperty"]]]] = empty_list()
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uuid):
            self.MissingRequiredField("uuid")
        if not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.email_addresses, list):
            self.email_addresses = [self.email_addresses] if self.email_addresses is not None else []
        self.email_addresses = [v if isinstance(v, str) else str(v) for v in self.email_addresses]

        self._normalize_inlined_as_list(slot_name="telephone_numbers", slot_type=TelephoneNumber, key_name="number", keyed=False)

        if self.address is not None and not isinstance(self.address, Address):
            self.address = Address(**as_dict(self.address))

        if not isinstance(self.urls, list):
            self.urls = [self.urls] if self.urls is not None else []
        self.urls = [v if isinstance(v, str) else str(v) for v in self.urls]

        self._normalize_inlined_as_list(slot_name="props", slot_type=LocationProperty, key_name="name", keyed=False)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Party(YAMLRoot):
    """
    An organization or person, which may be associated with roles or other concepts within the current or linked OSCAL
    document.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["Party"]
    class_class_curie: ClassVar[str] = "oscal_catalog:Party"
    class_name: ClassVar[str] = "Party"
    class_model_uri: ClassVar[URIRef] = OSCAL.Party

    uuid: str = None
    type: Union[str, "PartyTypeEnum"] = None
    name: Optional[str] = None
    short_name: Optional[str] = None
    email_addresses: Optional[Union[str, list[str]]] = empty_list()
    telephone_numbers: Optional[Union[Union[dict, "TelephoneNumber"], list[Union[dict, "TelephoneNumber"]]]] = empty_list()
    external_ids: Optional[Union[Union[dict, "MetadataPartyExternalId"], list[Union[dict, "MetadataPartyExternalId"]]]] = empty_list()
    addresses: Optional[Union[Union[dict, "Address"], list[Union[dict, "Address"]]]] = empty_list()
    location_uuids: Optional[Union[str, list[str]]] = empty_list()
    member_of_organizations: Optional[Union[str, list[str]]] = empty_list()
    props: Optional[Union[Union[dict, "PartyProperty"], list[Union[dict, "PartyProperty"]]]] = empty_list()
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uuid):
            self.MissingRequiredField("uuid")
        if not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, PartyTypeEnum):
            self.type = PartyTypeEnum(self.type)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.short_name is not None and not isinstance(self.short_name, str):
            self.short_name = str(self.short_name)

        if not isinstance(self.email_addresses, list):
            self.email_addresses = [self.email_addresses] if self.email_addresses is not None else []
        self.email_addresses = [v if isinstance(v, str) else str(v) for v in self.email_addresses]

        self._normalize_inlined_as_list(slot_name="telephone_numbers", slot_type=TelephoneNumber, key_name="number", keyed=False)

        self._normalize_inlined_as_list(slot_name="external_ids", slot_type=MetadataPartyExternalId, key_name="scheme", keyed=False)

        if not isinstance(self.addresses, list):
            self.addresses = [self.addresses] if self.addresses is not None else []
        self.addresses = [v if isinstance(v, Address) else Address(**as_dict(v)) for v in self.addresses]

        if not isinstance(self.location_uuids, list):
            self.location_uuids = [self.location_uuids] if self.location_uuids is not None else []
        self.location_uuids = [v if isinstance(v, str) else str(v) for v in self.location_uuids]

        if not isinstance(self.member_of_organizations, list):
            self.member_of_organizations = [self.member_of_organizations] if self.member_of_organizations is not None else []
        self.member_of_organizations = [v if isinstance(v, str) else str(v) for v in self.member_of_organizations]

        self._normalize_inlined_as_list(slot_name="props", slot_type=PartyProperty, key_name="value", keyed=False)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PartyExternalId(YAMLRoot):
    """
    An identifier for a person or organization using a designated scheme, e.g. an Open Researcher and Contributor ID
    (ORCID).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["PartyExternalId"]
    class_class_curie: ClassVar[str] = "oscal_catalog:PartyExternalId"
    class_name: ClassVar[str] = "PartyExternalId"
    class_model_uri: ClassVar[URIRef] = OSCAL.PartyExternalId

    scheme: str = None
    id: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.scheme):
            self.MissingRequiredField("scheme")
        if not isinstance(self.scheme, str):
            self.scheme = str(self.scheme)

        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ResponsibleParty(YAMLRoot):
    """
    A reference to a set of persons and/or organizations that have responsibility for performing the referenced role
    in the context of the containing object.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["ResponsibleParty"]
    class_class_curie: ClassVar[str] = "oscal_catalog:ResponsibleParty"
    class_name: ClassVar[str] = "ResponsibleParty"
    class_model_uri: ClassVar[URIRef] = OSCAL.ResponsibleParty

    role_id: str = None
    party_uuids: Union[str, list[str]] = None
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.role_id):
            self.MissingRequiredField("role_id")
        if not isinstance(self.role_id, str):
            self.role_id = str(self.role_id)

        if self._is_empty(self.party_uuids):
            self.MissingRequiredField("party_uuids")
        if not isinstance(self.party_uuids, list):
            self.party_uuids = [self.party_uuids] if self.party_uuids is not None else []
        self.party_uuids = [v if isinstance(v, str) else str(v) for v in self.party_uuids]

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ResponsibleRole(YAMLRoot):
    """
    A reference to a role with responsibility for performing a function relative to the containing object, optionally
    associated with a set of persons and/or organizations that perform that role.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["ResponsibleRole"]
    class_class_curie: ClassVar[str] = "oscal_catalog:ResponsibleRole"
    class_name: ClassVar[str] = "ResponsibleRole"
    class_model_uri: ClassVar[URIRef] = OSCAL.ResponsibleRole

    role_id: str = None
    party_uuids: Optional[Union[str, list[str]]] = empty_list()
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.role_id):
            self.MissingRequiredField("role_id")
        if not isinstance(self.role_id, str):
            self.role_id = str(self.role_id)

        if not isinstance(self.party_uuids, list):
            self.party_uuids = [self.party_uuids] if self.party_uuids is not None else []
        self.party_uuids = [v if isinstance(v, str) else str(v) for v in self.party_uuids]

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Action(YAMLRoot):
    """
    An action applied by a role within a given party to the content.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["Action"]
    class_class_curie: ClassVar[str] = "oscal_catalog:Action"
    class_name: ClassVar[str] = "Action"
    class_model_uri: ClassVar[URIRef] = OSCAL.Action

    uuid: str = None
    type: Union[str, "ActionTypeEnum"] = None
    system: str = None
    date: Optional[str] = None
    remarks: Optional[str] = None
    responsible_parties: Optional[Union[Union[dict, ResponsibleParty], list[Union[dict, ResponsibleParty]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uuid):
            self.MissingRequiredField("uuid")
        if not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, ActionTypeEnum):
            self.type = ActionTypeEnum(self.type)

        if self._is_empty(self.system):
            self.MissingRequiredField("system")
        if not isinstance(self.system, str):
            self.system = str(self.system)

        if self.date is not None and not isinstance(self.date, str):
            self.date = str(self.date)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        self._normalize_inlined_as_list(slot_name="responsible_parties", slot_type=ResponsibleParty, key_name="role-id", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TelephoneNumber(YAMLRoot):
    """
    A telephone service number as defined by ITU-T E.164.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["TelephoneNumber"]
    class_class_curie: ClassVar[str] = "oscal_catalog:TelephoneNumber"
    class_name: ClassVar[str] = "TelephoneNumber"
    class_model_uri: ClassVar[URIRef] = OSCAL.TelephoneNumber

    number: str = None
    type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.number):
            self.MissingRequiredField("number")
        if not isinstance(self.number, str):
            self.number = str(self.number)

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Address(YAMLRoot):
    """
    A postal address for the location.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["Address"]
    class_class_curie: ClassVar[str] = "oscal_catalog:Address"
    class_name: ClassVar[str] = "Address"
    class_model_uri: ClassVar[URIRef] = OSCAL.Address

    type: Optional[str] = None
    addr_lines: Optional[Union[str, list[str]]] = empty_list()
    city: Optional[str] = None
    state: Optional[str] = None
    postal_code: Optional[str] = None
    country: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        if not isinstance(self.addr_lines, list):
            self.addr_lines = [self.addr_lines] if self.addr_lines is not None else []
        self.addr_lines = [v if isinstance(v, str) else str(v) for v in self.addr_lines]

        if self.city is not None and not isinstance(self.city, str):
            self.city = str(self.city)

        if self.state is not None and not isinstance(self.state, str):
            self.state = str(self.state)

        if self.postal_code is not None and not isinstance(self.postal_code, str):
            self.postal_code = str(self.postal_code)

        if self.country is not None and not isinstance(self.country, str):
            self.country = str(self.country)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Hash(YAMLRoot):
    """
    A representation of a cryptographic digest generated over a resource using a specified hash algorithm.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["Hash"]
    class_class_curie: ClassVar[str] = "oscal_catalog:Hash"
    class_name: ClassVar[str] = "Hash"
    class_model_uri: ClassVar[URIRef] = OSCAL.Hash

    value: str = None
    algorithm: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, str):
            self.value = str(self.value)

        if self._is_empty(self.algorithm):
            self.MissingRequiredField("algorithm")
        if not isinstance(self.algorithm, str):
            self.algorithm = str(self.algorithm)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Property(YAMLRoot):
    """
    An attribute, characteristic, or quality of the containing object expressed as a namespace qualified name/value
    pair.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["Property"]
    class_class_curie: ClassVar[str] = "oscal_catalog:Property"
    class_name: ClassVar[str] = "Property"
    class_model_uri: ClassVar[URIRef] = OSCAL.Property

    name: str = None
    value: str = None
    uuid: Optional[str] = None
    ns: Optional[str] = None
    _class: Optional[str] = None
    remarks: Optional[str] = None
    group: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, str):
            self.value = str(self.value)

        if self.uuid is not None and not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        if self.ns is not None and not isinstance(self.ns, str):
            self.ns = str(self.ns)

        if self._class is not None and not isinstance(self._class, str):
            self._class = str(self._class)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        if self.group is not None and not isinstance(self.group, str):
            self.group = str(self.group)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MetadataProperty(Property):
    """
    Metadata-scoped OSCAL property.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["MetadataProperty"]
    class_class_curie: ClassVar[str] = "oscal_catalog:MetadataProperty"
    class_name: ClassVar[str] = "MetadataProperty"
    class_model_uri: ClassVar[URIRef] = OSCAL.MetadataProperty

    value: str = None
    name: Union[str, "MetadataPropNameEnum"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, MetadataPropNameEnum):
            self.name = MetadataPropNameEnum(self.name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RevisionProperty(Property):
    """
    Revision-scoped OSCAL property.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["RevisionProperty"]
    class_class_curie: ClassVar[str] = "oscal_catalog:RevisionProperty"
    class_name: ClassVar[str] = "RevisionProperty"
    class_model_uri: ClassVar[URIRef] = OSCAL.RevisionProperty

    value: str = None
    name: Union[str, "RevisionPropNameEnum"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, RevisionPropNameEnum):
            self.name = RevisionPropNameEnum(self.name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LocationProperty(Property):
    """
    Location-scoped OSCAL property.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["LocationProperty"]
    class_class_curie: ClassVar[str] = "oscal_catalog:LocationProperty"
    class_name: ClassVar[str] = "LocationProperty"
    class_model_uri: ClassVar[URIRef] = OSCAL.LocationProperty

    name: Union[str, "LocationPropNameEnum"] = None
    value: str = None
    _class: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, LocationPropNameEnum):
            self.name = LocationPropNameEnum(self.name)

        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, str):
            self.value = str(self.value)

        if self._class is not None and not isinstance(self._class, str):
            self._class = str(self._class)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PartyProperty(Property):
    """
    Party-scoped OSCAL property.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["PartyProperty"]
    class_class_curie: ClassVar[str] = "oscal_catalog:PartyProperty"
    class_name: ClassVar[str] = "PartyProperty"
    class_model_uri: ClassVar[URIRef] = OSCAL.PartyProperty

    value: str = None
    name: Union[str, "PartyPropNameEnum"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, PartyPropNameEnum):
            self.name = PartyPropNameEnum(self.name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ResourceProperty(Property):
    """
    Back-matter resource-scoped OSCAL property.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["ResourceProperty"]
    class_class_curie: ClassVar[str] = "oscal_catalog:ResourceProperty"
    class_name: ClassVar[str] = "ResourceProperty"
    class_model_uri: ClassVar[URIRef] = OSCAL.ResourceProperty

    name: Union[str, "ResourcePropNameEnum"] = None
    value: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, ResourcePropNameEnum):
            self.name = ResourcePropNameEnum(self.name)

        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, str):
            self.value = str(self.value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PartProperty(Property):
    """
    Control-common part-scoped OSCAL property.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["PartProperty"]
    class_class_curie: ClassVar[str] = "oscal_catalog:PartProperty"
    class_name: ClassVar[str] = "PartProperty"
    class_model_uri: ClassVar[URIRef] = OSCAL.PartProperty

    value: str = None
    name: Union[str, "PartPropNameEnum"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, PartPropNameEnum):
            self.name = PartPropNameEnum(self.name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ParameterProperty(Property):
    """
    Control-common parameter-scoped OSCAL property.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["ParameterProperty"]
    class_class_curie: ClassVar[str] = "oscal_catalog:ParameterProperty"
    class_name: ClassVar[str] = "ParameterProperty"
    class_model_uri: ClassVar[URIRef] = OSCAL.ParameterProperty

    value: str = None
    name: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MetadataPartyExternalId(PartyExternalId):
    """
    Metadata-scoped external identifier.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["MetadataPartyExternalId"]
    class_class_curie: ClassVar[str] = "oscal_catalog:MetadataPartyExternalId"
    class_name: ClassVar[str] = "MetadataPartyExternalId"
    class_model_uri: ClassVar[URIRef] = OSCAL.MetadataPartyExternalId

    scheme: str = None
    id: str = None

@dataclass(repr=False)
class Link(YAMLRoot):
    """
    A reference to a local or remote resource, that has a specific relation to the containing object.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["Link"]
    class_class_curie: ClassVar[str] = "oscal_catalog:Link"
    class_name: ClassVar[str] = "Link"
    class_model_uri: ClassVar[URIRef] = OSCAL.Link

    href: str = None
    rel: Optional[str] = None
    resource_fragment: Optional[str] = None
    media_type: Optional[str] = None
    text: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.href):
            self.MissingRequiredField("href")
        if not isinstance(self.href, str):
            self.href = str(self.href)

        if self.rel is not None and not isinstance(self.rel, str):
            self.rel = str(self.rel)

        if self.resource_fragment is not None and not isinstance(self.resource_fragment, str):
            self.resource_fragment = str(self.resource_fragment)

        if self.media_type is not None and not isinstance(self.media_type, str):
            self.media_type = str(self.media_type)

        if self.text is not None and not isinstance(self.text, str):
            self.text = str(self.text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BackMatter(YAMLRoot):
    """
    A collection of resources that may be referenced from within the OSCAL document instance.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["BackMatter"]
    class_class_curie: ClassVar[str] = "oscal_catalog:BackMatter"
    class_name: ClassVar[str] = "BackMatter"
    class_model_uri: ClassVar[URIRef] = OSCAL.BackMatter

    resources: Optional[Union[Union[dict, "Resource"], list[Union[dict, "Resource"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="resources", slot_type=Resource, key_name="uuid", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Resource(YAMLRoot):
    """
    A resource associated with content in the containing document instance. A resource may be directly included in the
    document using base64 encoding or may point to one or more equivalent internet resources.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["Resource"]
    class_class_curie: ClassVar[str] = "oscal_catalog:Resource"
    class_name: ClassVar[str] = "Resource"
    class_model_uri: ClassVar[URIRef] = OSCAL.Resource

    uuid: str = None
    title: Optional[str] = None
    description: Optional[str] = None
    props: Optional[Union[Union[dict, ResourceProperty], list[Union[dict, ResourceProperty]]]] = empty_list()
    document_ids: Optional[Union[Union[dict, DocumentId], list[Union[dict, DocumentId]]]] = empty_list()
    remarks: Optional[str] = None
    citation: Optional[Union[dict, "Citation"]] = None
    rlinks: Optional[Union[Union[dict, "ResourceLink"], list[Union[dict, "ResourceLink"]]]] = empty_list()
    base64: Optional[Union[dict, "Base64Resource"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uuid):
            self.MissingRequiredField("uuid")
        if not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_list(slot_name="props", slot_type=ResourceProperty, key_name="name", keyed=False)

        self._normalize_inlined_as_list(slot_name="document_ids", slot_type=DocumentId, key_name="identifier", keyed=False)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        if self.citation is not None and not isinstance(self.citation, Citation):
            self.citation = Citation(**as_dict(self.citation))

        self._normalize_inlined_as_list(slot_name="rlinks", slot_type=ResourceLink, key_name="href", keyed=False)

        if self.base64 is not None and not isinstance(self.base64, Base64Resource):
            self.base64 = Base64Resource(**as_dict(self.base64))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Citation(YAMLRoot):
    """
    An optional citation consisting of end note text using structured markup.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["Citation"]
    class_class_curie: ClassVar[str] = "oscal_catalog:Citation"
    class_name: ClassVar[str] = "Citation"
    class_model_uri: ClassVar[URIRef] = OSCAL.Citation

    text: str = None
    links: Optional[Union[Union[dict, Link], list[Union[dict, Link]]]] = empty_list()
    props: Optional[Union[Union[dict, Property], list[Union[dict, Property]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.text):
            self.MissingRequiredField("text")
        if not isinstance(self.text, str):
            self.text = str(self.text)

        self._normalize_inlined_as_list(slot_name="links", slot_type=Link, key_name="href", keyed=False)

        self._normalize_inlined_as_list(slot_name="props", slot_type=Property, key_name="name", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ResourceLink(YAMLRoot):
    """
    A URL-based pointer to an external resource with an optional hash for verification and change detection.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["ResourceLink"]
    class_class_curie: ClassVar[str] = "oscal_catalog:ResourceLink"
    class_name: ClassVar[str] = "ResourceLink"
    class_model_uri: ClassVar[URIRef] = OSCAL.ResourceLink

    href: str = None
    media_type: Optional[str] = None
    hashes: Optional[Union[Union[dict, Hash], list[Union[dict, Hash]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.href):
            self.MissingRequiredField("href")
        if not isinstance(self.href, str):
            self.href = str(self.href)

        if self.media_type is not None and not isinstance(self.media_type, str):
            self.media_type = str(self.media_type)

        self._normalize_inlined_as_list(slot_name="hashes", slot_type=Hash, key_name="value", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Base64Resource(YAMLRoot):
    """
    A resource encoded using the Base64 alphabet defined by RFC 2045.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["Base64Resource"]
    class_class_curie: ClassVar[str] = "oscal_catalog:Base64Resource"
    class_name: ClassVar[str] = "Base64Resource"
    class_model_uri: ClassVar[URIRef] = OSCAL.Base64Resource

    value: str = None
    media_type: Optional[str] = None
    filename: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, str):
            self.value = str(self.value)

        if self.media_type is not None and not isinstance(self.media_type, str):
            self.media_type = str(self.media_type)

        if self.filename is not None and not isinstance(self.filename, str):
            self.filename = str(self.filename)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Part(YAMLRoot):
    """
    An annotated, markup-based textual element of a control's or catalog group's definition, or a child of another
    part.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["Part"]
    class_class_curie: ClassVar[str] = "oscal_catalog:Part"
    class_name: ClassVar[str] = "Part"
    class_model_uri: ClassVar[URIRef] = OSCAL.Part

    name: str = None
    id: Optional[str] = None
    ns: Optional[str] = None
    _class: Optional[str] = None
    title: Optional[str] = None
    prose: Optional[str] = None
    parts: Optional[Union[Union[dict, "Part"], list[Union[dict, "Part"]]]] = empty_list()
    props: Optional[Union[Union[dict, PartProperty], list[Union[dict, PartProperty]]]] = empty_list()
    links: Optional[Union[Union[dict, Link], list[Union[dict, Link]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.id is not None and not isinstance(self.id, str):
            self.id = str(self.id)

        if self.ns is not None and not isinstance(self.ns, str):
            self.ns = str(self.ns)

        if self._class is not None and not isinstance(self._class, str):
            self._class = str(self._class)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.prose is not None and not isinstance(self.prose, str):
            self.prose = str(self.prose)

        self._normalize_inlined_as_list(slot_name="parts", slot_type=Part, key_name="name", keyed=False)

        self._normalize_inlined_as_list(slot_name="props", slot_type=PartProperty, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="links", slot_type=Link, key_name="href", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Parameter(YAMLRoot):
    """
    Parameters provide a mechanism for the dynamic assignment of value(s) in a control.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["Parameter"]
    class_class_curie: ClassVar[str] = "oscal_catalog:Parameter"
    class_name: ClassVar[str] = "Parameter"
    class_model_uri: ClassVar[URIRef] = OSCAL.Parameter

    id: str = None
    _class: Optional[str] = None
    depends_on: Optional[str] = None
    label: Optional[str] = None
    usage: Optional[str] = None
    constraints: Optional[Union[Union[dict, "ParameterConstraint"], list[Union[dict, "ParameterConstraint"]]]] = empty_list()
    guidelines: Optional[Union[Union[dict, "ParameterGuideline"], list[Union[dict, "ParameterGuideline"]]]] = empty_list()
    values: Optional[Union[str, list[str]]] = empty_list()
    select: Optional[Union[dict, "ParameterSelection"]] = None
    props: Optional[Union[Union[dict, ParameterProperty], list[Union[dict, ParameterProperty]]]] = empty_list()
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self._class is not None and not isinstance(self._class, str):
            self._class = str(self._class)

        if self.depends_on is not None and not isinstance(self.depends_on, str):
            self.depends_on = str(self.depends_on)

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        if self.usage is not None and not isinstance(self.usage, str):
            self.usage = str(self.usage)

        if not isinstance(self.constraints, list):
            self.constraints = [self.constraints] if self.constraints is not None else []
        self.constraints = [v if isinstance(v, ParameterConstraint) else ParameterConstraint(**as_dict(v)) for v in self.constraints]

        self._normalize_inlined_as_list(slot_name="guidelines", slot_type=ParameterGuideline, key_name="prose", keyed=False)

        if not isinstance(self.values, list):
            self.values = [self.values] if self.values is not None else []
        self.values = [v if isinstance(v, str) else str(v) for v in self.values]

        if self.select is not None and not isinstance(self.select, ParameterSelection):
            self.select = ParameterSelection(**as_dict(self.select))

        self._normalize_inlined_as_list(slot_name="props", slot_type=ParameterProperty, key_name="value", keyed=False)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ParameterConstraint(YAMLRoot):
    """
    A formal or informal expression of a constraint or test.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["ParameterConstraint"]
    class_class_curie: ClassVar[str] = "oscal_catalog:ParameterConstraint"
    class_name: ClassVar[str] = "ParameterConstraint"
    class_model_uri: ClassVar[URIRef] = OSCAL.ParameterConstraint

    description: Optional[str] = None
    tests: Optional[Union[Union[dict, "ConstraintTest"], list[Union[dict, "ConstraintTest"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_list(slot_name="tests", slot_type=ConstraintTest, key_name="expression", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ConstraintTest(YAMLRoot):
    """
    A test expression which is expected to be evaluated by a tool.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["ConstraintTest"]
    class_class_curie: ClassVar[str] = "oscal_catalog:ConstraintTest"
    class_name: ClassVar[str] = "ConstraintTest"
    class_model_uri: ClassVar[URIRef] = OSCAL.ConstraintTest

    expression: str = None
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.expression):
            self.MissingRequiredField("expression")
        if not isinstance(self.expression, str):
            self.expression = str(self.expression)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ParameterGuideline(YAMLRoot):
    """
    A prose statement that provides a recommendation for the use of a parameter.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["ParameterGuideline"]
    class_class_curie: ClassVar[str] = "oscal_catalog:ParameterGuideline"
    class_name: ClassVar[str] = "ParameterGuideline"
    class_model_uri: ClassVar[URIRef] = OSCAL.ParameterGuideline

    prose: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.prose):
            self.MissingRequiredField("prose")
        if not isinstance(self.prose, str):
            self.prose = str(self.prose)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ParameterSelection(YAMLRoot):
    """
    Presenting a choice among alternatives.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["ParameterSelection"]
    class_class_curie: ClassVar[str] = "oscal_catalog:ParameterSelection"
    class_name: ClassVar[str] = "ParameterSelection"
    class_model_uri: ClassVar[URIRef] = OSCAL.ParameterSelection

    how_many: Optional[Union[str, "ParameterCardinalityEnum"]] = None
    choice: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.how_many is not None and not isinstance(self.how_many, ParameterCardinalityEnum):
            self.how_many = ParameterCardinalityEnum(self.how_many)

        if not isinstance(self.choice, list):
            self.choice = [self.choice] if self.choice is not None else []
        self.choice = [v if isinstance(v, str) else str(v) for v in self.choice]

        super().__post_init__(**kwargs)


class IncludeAll(YAMLRoot):
    """
    Include all controls from the imported catalog or profile resources.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["IncludeAll"]
    class_class_curie: ClassVar[str] = "oscal_catalog:IncludeAll"
    class_name: ClassVar[str] = "IncludeAll"
    class_model_uri: ClassVar[URIRef] = OSCAL.IncludeAll


@dataclass(repr=False)
class ControlMatching(YAMLRoot):
    """
    Selecting a set of controls by matching their IDs with a wildcard pattern.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["ControlMatching"]
    class_class_curie: ClassVar[str] = "oscal_catalog:ControlMatching"
    class_name: ClassVar[str] = "ControlMatching"
    class_model_uri: ClassVar[URIRef] = OSCAL.ControlMatching

    remarks: Optional[str] = None
    pattern: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        if self.pattern is not None and not isinstance(self.pattern, str):
            self.pattern = str(self.pattern)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SelectControlById(YAMLRoot):
    """
    Select a control or controls from an imported control set.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["SelectControlById"]
    class_class_curie: ClassVar[str] = "oscal_catalog:SelectControlById"
    class_name: ClassVar[str] = "SelectControlById"
    class_model_uri: ClassVar[URIRef] = OSCAL.SelectControlById

    with_child_controls: Optional[Union[str, "WithChildControlsEnum"]] = None
    with_ids: Optional[Union[str, list[str]]] = empty_list()
    matching: Optional[Union[Union[dict, ControlMatching], list[Union[dict, ControlMatching]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.with_child_controls is not None and not isinstance(self.with_child_controls, WithChildControlsEnum):
            self.with_child_controls = WithChildControlsEnum(self.with_child_controls)

        if not isinstance(self.with_ids, list):
            self.with_ids = [self.with_ids] if self.with_ids is not None else []
        self.with_ids = [v if isinstance(v, str) else str(v) for v in self.with_ids]

        if not isinstance(self.matching, list):
            self.matching = [self.matching] if self.matching is not None else []
        self.matching = [v if isinstance(v, ControlMatching) else ControlMatching(**as_dict(v)) for v in self.matching]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ProfileDocument(OscalDocument):
    """
    Root wrapper for an OSCAL Profile document.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_PROFILE["ProfileDocument"]
    class_class_curie: ClassVar[str] = "oscal_profile:ProfileDocument"
    class_name: ClassVar[str] = "ProfileDocument"
    class_model_uri: ClassVar[URIRef] = OSCAL.ProfileDocument

    profile: Union[dict, "Profile"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.profile):
            self.MissingRequiredField("profile")
        if not isinstance(self.profile, Profile):
            self.profile = Profile(**as_dict(self.profile))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Profile(YAMLRoot):
    """
    An OSCAL Profile that designates a set of controls from one or more catalogs or profiles, optionally restructures
    and modifies them, to describe a basis for a security standard or body of practice.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_PROFILE["Profile"]
    class_class_curie: ClassVar[str] = "oscal_profile:Profile"
    class_name: ClassVar[str] = "Profile"
    class_model_uri: ClassVar[URIRef] = OSCAL.Profile

    uuid: str = None
    metadata: Union[dict, Metadata] = None
    imports: Union[Union[dict, "ProfileImport"], list[Union[dict, "ProfileImport"]]] = None
    merge: Optional[Union[dict, "ProfileMerge"]] = None
    modify: Optional[Union[dict, "ProfileModify"]] = None
    back_matter: Optional[Union[dict, BackMatter]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uuid):
            self.MissingRequiredField("uuid")
        if not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        if self._is_empty(self.metadata):
            self.MissingRequiredField("metadata")
        if not isinstance(self.metadata, Metadata):
            self.metadata = Metadata(**as_dict(self.metadata))

        if self._is_empty(self.imports):
            self.MissingRequiredField("imports")
        self._normalize_inlined_as_list(slot_name="imports", slot_type=ProfileImport, key_name="href", keyed=False)

        if self.merge is not None and not isinstance(self.merge, ProfileMerge):
            self.merge = ProfileMerge(**as_dict(self.merge))

        if self.modify is not None and not isinstance(self.modify, ProfileModify):
            self.modify = ProfileModify(**as_dict(self.modify))

        if self.back_matter is not None and not isinstance(self.back_matter, BackMatter):
            self.back_matter = BackMatter(**as_dict(self.back_matter))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ProfileImport(YAMLRoot):
    """
    Designates a referenced source catalog or profile that provides a source of control information for use in
    creating a new overlay or baseline.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_PROFILE["ProfileImport"]
    class_class_curie: ClassVar[str] = "oscal_profile:ProfileImport"
    class_name: ClassVar[str] = "ProfileImport"
    class_model_uri: ClassVar[URIRef] = OSCAL.ProfileImport

    href: str = None
    include_all: Optional[Union[dict, IncludeAll]] = None
    include_controls: Optional[Union[Union[dict, SelectControlById], list[Union[dict, SelectControlById]]]] = empty_list()
    exclude_controls: Optional[Union[Union[dict, SelectControlById], list[Union[dict, SelectControlById]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.href):
            self.MissingRequiredField("href")
        if not isinstance(self.href, str):
            self.href = str(self.href)

        if self.include_all is not None and not isinstance(self.include_all, IncludeAll):
            self.include_all = IncludeAll()

        if not isinstance(self.include_controls, list):
            self.include_controls = [self.include_controls] if self.include_controls is not None else []
        self.include_controls = [v if isinstance(v, SelectControlById) else SelectControlById(**as_dict(v)) for v in self.include_controls]

        if not isinstance(self.exclude_controls, list):
            self.exclude_controls = [self.exclude_controls] if self.exclude_controls is not None else []
        self.exclude_controls = [v if isinstance(v, SelectControlById) else SelectControlById(**as_dict(v)) for v in self.exclude_controls]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ProfileMerge(YAMLRoot):
    """
    Provides structuring directives that instruct how controls are organized after profile resolution.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_PROFILE["ProfileMerge"]
    class_class_curie: ClassVar[str] = "oscal_profile:ProfileMerge"
    class_name: ClassVar[str] = "ProfileMerge"
    class_model_uri: ClassVar[URIRef] = OSCAL.ProfileMerge

    combine: Optional[Union[dict, "CombinationRule"]] = None
    flat: Optional[Union[dict, "MergeFlat"]] = None
    as_is: Optional[Union[bool, Bool]] = None
    custom: Optional[Union[dict, "MergeCustom"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.combine is not None and not isinstance(self.combine, CombinationRule):
            self.combine = CombinationRule(**as_dict(self.combine))

        if self.flat is not None and not isinstance(self.flat, MergeFlat):
            self.flat = MergeFlat()

        if self.as_is is not None and not isinstance(self.as_is, Bool):
            self.as_is = Bool(self.as_is)

        if self.custom is not None and not isinstance(self.custom, MergeCustom):
            self.custom = MergeCustom(**as_dict(self.custom))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CombinationRule(YAMLRoot):
    """
    Defines how to resolve duplicate instances of the same control (e.g., controls with the same ID) encountered in a
    profile merge.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_PROFILE["CombinationRule"]
    class_class_curie: ClassVar[str] = "oscal_profile:CombinationRule"
    class_name: ClassVar[str] = "CombinationRule"
    class_model_uri: ClassVar[URIRef] = OSCAL.CombinationRule

    method: Optional[Union[str, "CombinationMethodEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.method is not None and not isinstance(self.method, CombinationMethodEnum):
            self.method = CombinationMethodEnum(self.method)

        super().__post_init__(**kwargs)


class MergeFlat(YAMLRoot):
    """
    Directs that controls appear without any grouping structure after profile resolution.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_PROFILE["MergeFlat"]
    class_class_curie: ClassVar[str] = "oscal_profile:MergeFlat"
    class_name: ClassVar[str] = "MergeFlat"
    class_model_uri: ClassVar[URIRef] = OSCAL.MergeFlat


@dataclass(repr=False)
class MergeCustom(YAMLRoot):
    """
    Provides an alternate grouping structure that selected controls will be placed in after profile resolution.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_PROFILE["MergeCustom"]
    class_class_curie: ClassVar[str] = "oscal_profile:MergeCustom"
    class_name: ClassVar[str] = "MergeCustom"
    class_model_uri: ClassVar[URIRef] = OSCAL.MergeCustom

    groups: Optional[Union[Union[dict, "ProfileGroup"], list[Union[dict, "ProfileGroup"]]]] = empty_list()
    insert_controls: Optional[Union[Union[dict, "InsertControls"], list[Union[dict, "InsertControls"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="groups", slot_type=ProfileGroup, key_name="title", keyed=False)

        if not isinstance(self.insert_controls, list):
            self.insert_controls = [self.insert_controls] if self.insert_controls is not None else []
        self.insert_controls = [v if isinstance(v, InsertControls) else InsertControls(**as_dict(v)) for v in self.insert_controls]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ProfileGroup(YAMLRoot):
    """
    A group of (selected) controls or of groups of controls within a profile custom merge structure.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_PROFILE["ProfileGroup"]
    class_class_curie: ClassVar[str] = "oscal_profile:ProfileGroup"
    class_name: ClassVar[str] = "ProfileGroup"
    class_model_uri: ClassVar[URIRef] = OSCAL.ProfileGroup

    title: str = None
    id: Optional[str] = None
    _class: Optional[str] = None
    params: Optional[Union[Union[dict, Parameter], list[Union[dict, Parameter]]]] = empty_list()
    parts: Optional[Union[Union[dict, Part], list[Union[dict, Part]]]] = empty_list()
    groups: Optional[Union[Union[dict, "ProfileGroup"], list[Union[dict, "ProfileGroup"]]]] = empty_list()
    insert_controls: Optional[Union[Union[dict, "InsertControls"], list[Union[dict, "InsertControls"]]]] = empty_list()
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self.id is not None and not isinstance(self.id, str):
            self.id = str(self.id)

        if self._class is not None and not isinstance(self._class, str):
            self._class = str(self._class)

        self._normalize_inlined_as_list(slot_name="params", slot_type=Parameter, key_name="id", keyed=False)

        self._normalize_inlined_as_list(slot_name="parts", slot_type=Part, key_name="name", keyed=False)

        self._normalize_inlined_as_list(slot_name="groups", slot_type=ProfileGroup, key_name="title", keyed=False)

        if not isinstance(self.insert_controls, list):
            self.insert_controls = [self.insert_controls] if self.insert_controls is not None else []
        self.insert_controls = [v if isinstance(v, InsertControls) else InsertControls(**as_dict(v)) for v in self.insert_controls]

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ProfileModify(YAMLRoot):
    """
    Set parameters or amend controls in resolution.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_PROFILE["ProfileModify"]
    class_class_curie: ClassVar[str] = "oscal_profile:ProfileModify"
    class_name: ClassVar[str] = "ProfileModify"
    class_model_uri: ClassVar[URIRef] = OSCAL.ProfileModify

    set_parameters: Optional[Union[Union[dict, "ParameterSetting"], list[Union[dict, "ParameterSetting"]]]] = empty_list()
    alters: Optional[Union[Union[dict, "Alteration"], list[Union[dict, "Alteration"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="set_parameters", slot_type=ParameterSetting, key_name="param-id", keyed=False)

        self._normalize_inlined_as_list(slot_name="alters", slot_type=Alteration, key_name="control-id", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ParameterSetting(YAMLRoot):
    """
    A parameter setting to be propagated to points of insertion in a resolved profile.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_PROFILE["ParameterSetting"]
    class_class_curie: ClassVar[str] = "oscal_profile:ParameterSetting"
    class_name: ClassVar[str] = "ParameterSetting"
    class_model_uri: ClassVar[URIRef] = OSCAL.ParameterSetting

    param_id: str = None
    _class: Optional[str] = None
    depends_on: Optional[str] = None
    label: Optional[str] = None
    usage: Optional[str] = None
    constraints: Optional[Union[Union[dict, ParameterConstraint], list[Union[dict, ParameterConstraint]]]] = empty_list()
    guidelines: Optional[Union[Union[dict, ParameterGuideline], list[Union[dict, ParameterGuideline]]]] = empty_list()
    values: Optional[Union[str, list[str]]] = empty_list()
    select: Optional[Union[dict, ParameterSelection]] = None
    props: Optional[Union[Union[dict, Property], list[Union[dict, Property]]]] = empty_list()
    links: Optional[Union[Union[dict, Link], list[Union[dict, Link]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.param_id):
            self.MissingRequiredField("param_id")
        if not isinstance(self.param_id, str):
            self.param_id = str(self.param_id)

        if self._class is not None and not isinstance(self._class, str):
            self._class = str(self._class)

        if self.depends_on is not None and not isinstance(self.depends_on, str):
            self.depends_on = str(self.depends_on)

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        if self.usage is not None and not isinstance(self.usage, str):
            self.usage = str(self.usage)

        if not isinstance(self.constraints, list):
            self.constraints = [self.constraints] if self.constraints is not None else []
        self.constraints = [v if isinstance(v, ParameterConstraint) else ParameterConstraint(**as_dict(v)) for v in self.constraints]

        self._normalize_inlined_as_list(slot_name="guidelines", slot_type=ParameterGuideline, key_name="prose", keyed=False)

        if not isinstance(self.values, list):
            self.values = [self.values] if self.values is not None else []
        self.values = [v if isinstance(v, str) else str(v) for v in self.values]

        if self.select is not None and not isinstance(self.select, ParameterSelection):
            self.select = ParameterSelection(**as_dict(self.select))

        self._normalize_inlined_as_list(slot_name="props", slot_type=Property, key_name="name", keyed=False)

        self._normalize_inlined_as_list(slot_name="links", slot_type=Link, key_name="href", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Alteration(YAMLRoot):
    """
    Specifies changes to be made to an included control when a profile is resolved.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_PROFILE["Alteration"]
    class_class_curie: ClassVar[str] = "oscal_profile:Alteration"
    class_name: ClassVar[str] = "Alteration"
    class_model_uri: ClassVar[URIRef] = OSCAL.Alteration

    control_id: str = None
    removes: Optional[Union[Union[dict, "Removal"], list[Union[dict, "Removal"]]]] = empty_list()
    adds: Optional[Union[Union[dict, "Addition"], list[Union[dict, "Addition"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.control_id):
            self.MissingRequiredField("control_id")
        if not isinstance(self.control_id, str):
            self.control_id = str(self.control_id)

        if not isinstance(self.removes, list):
            self.removes = [self.removes] if self.removes is not None else []
        self.removes = [v if isinstance(v, Removal) else Removal(**as_dict(v)) for v in self.removes]

        if not isinstance(self.adds, list):
            self.adds = [self.adds] if self.adds is not None else []
        self.adds = [v if isinstance(v, Addition) else Addition(**as_dict(v)) for v in self.adds]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Removal(YAMLRoot):
    """
    Specifies objects to be removed from a control based on aspects of the object that must all match.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_PROFILE["Removal"]
    class_class_curie: ClassVar[str] = "oscal_profile:Removal"
    class_name: ClassVar[str] = "Removal"
    class_model_uri: ClassVar[URIRef] = OSCAL.Removal

    by_name: Optional[str] = None
    by_class: Optional[str] = None
    by_id: Optional[str] = None
    by_item_name: Optional[Union[str, "ByItemNameEnum"]] = None
    by_ns: Optional[str] = None
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.by_name is not None and not isinstance(self.by_name, str):
            self.by_name = str(self.by_name)

        if self.by_class is not None and not isinstance(self.by_class, str):
            self.by_class = str(self.by_class)

        if self.by_id is not None and not isinstance(self.by_id, str):
            self.by_id = str(self.by_id)

        if self.by_item_name is not None and not isinstance(self.by_item_name, ByItemNameEnum):
            self.by_item_name = ByItemNameEnum(self.by_item_name)

        if self.by_ns is not None and not isinstance(self.by_ns, str):
            self.by_ns = str(self.by_ns)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Addition(YAMLRoot):
    """
    Specifies content to be added into controls in resolution.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_PROFILE["Addition"]
    class_class_curie: ClassVar[str] = "oscal_profile:Addition"
    class_name: ClassVar[str] = "Addition"
    class_model_uri: ClassVar[URIRef] = OSCAL.Addition

    position: Optional[Union[str, "AdditionPositionEnum"]] = None
    by_id: Optional[str] = None
    title: Optional[str] = None
    params: Optional[Union[Union[dict, Parameter], list[Union[dict, Parameter]]]] = empty_list()
    props: Optional[Union[Union[dict, "ProfileAlterationProperty"], list[Union[dict, "ProfileAlterationProperty"]]]] = empty_list()
    links: Optional[Union[Union[dict, Link], list[Union[dict, Link]]]] = empty_list()
    parts: Optional[Union[Union[dict, Part], list[Union[dict, Part]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.position is not None and not isinstance(self.position, AdditionPositionEnum):
            self.position = AdditionPositionEnum(self.position)

        if self.by_id is not None and not isinstance(self.by_id, str):
            self.by_id = str(self.by_id)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        self._normalize_inlined_as_list(slot_name="params", slot_type=Parameter, key_name="id", keyed=False)

        self._normalize_inlined_as_list(slot_name="props", slot_type=ProfileAlterationProperty, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="links", slot_type=Link, key_name="href", keyed=False)

        self._normalize_inlined_as_list(slot_name="parts", slot_type=Part, key_name="name", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ProfileAlterationProperty(Property):
    """
    OSCAL property entries allowed in profile modify additions.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_PROFILE["ProfileAlterationProperty"]
    class_class_curie: ClassVar[str] = "oscal_profile:ProfileAlterationProperty"
    class_name: ClassVar[str] = "ProfileAlterationProperty"
    class_model_uri: ClassVar[URIRef] = OSCAL.ProfileAlterationProperty

    value: str = None
    name: Union[str, "AlterationPropNameEnum"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, AlterationPropNameEnum):
            self.name = AlterationPropNameEnum(self.name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InsertControls(YAMLRoot):
    """
    Specifies which controls to use in the containing context (as part of a group or custom merge structure).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_PROFILE["InsertControls"]
    class_class_curie: ClassVar[str] = "oscal_profile:InsertControls"
    class_name: ClassVar[str] = "InsertControls"
    class_model_uri: ClassVar[URIRef] = OSCAL.InsertControls

    order: Optional[Union[str, "InsertOrderEnum"]] = None
    include_all: Optional[Union[dict, IncludeAll]] = None
    include_controls: Optional[Union[Union[dict, SelectControlById], list[Union[dict, SelectControlById]]]] = empty_list()
    exclude_controls: Optional[Union[Union[dict, SelectControlById], list[Union[dict, SelectControlById]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.order is not None and not isinstance(self.order, InsertOrderEnum):
            self.order = InsertOrderEnum(self.order)

        if self.include_all is not None and not isinstance(self.include_all, IncludeAll):
            self.include_all = IncludeAll()

        if not isinstance(self.include_controls, list):
            self.include_controls = [self.include_controls] if self.include_controls is not None else []
        self.include_controls = [v if isinstance(v, SelectControlById) else SelectControlById(**as_dict(v)) for v in self.include_controls]

        if not isinstance(self.exclude_controls, list):
            self.exclude_controls = [self.exclude_controls] if self.exclude_controls is not None else []
        self.exclude_controls = [v if isinstance(v, SelectControlById) else SelectControlById(**as_dict(v)) for v in self.exclude_controls]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SspDocument(OscalDocument):
    """
    Root wrapper for an OSCAL System Security Plan document.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_SSP["SspDocument"]
    class_class_curie: ClassVar[str] = "oscal_ssp:SspDocument"
    class_name: ClassVar[str] = "SspDocument"
    class_model_uri: ClassVar[URIRef] = OSCAL.SspDocument

    system_security_plan: Union[dict, "SystemSecurityPlan"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.system_security_plan):
            self.MissingRequiredField("system_security_plan")
        if not isinstance(self.system_security_plan, SystemSecurityPlan):
            self.system_security_plan = SystemSecurityPlan(**as_dict(self.system_security_plan))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SystemSecurityPlan(YAMLRoot):
    """
    A system security plan, such as those described in NIST SP 800-18.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_SSP["SystemSecurityPlan"]
    class_class_curie: ClassVar[str] = "oscal_ssp:SystemSecurityPlan"
    class_name: ClassVar[str] = "SystemSecurityPlan"
    class_model_uri: ClassVar[URIRef] = OSCAL.SystemSecurityPlan

    uuid: str = None
    metadata: Union[dict, Metadata] = None
    import_profile: Union[dict, "ImportProfile"] = None
    system_characteristics: Union[dict, "SystemCharacteristics"] = None
    system_implementation: Union[dict, "SystemImplementation"] = None
    control_implementation: Union[dict, "SspControlImplementation"] = None
    back_matter: Optional[Union[dict, BackMatter]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uuid):
            self.MissingRequiredField("uuid")
        if not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        if self._is_empty(self.metadata):
            self.MissingRequiredField("metadata")
        if not isinstance(self.metadata, Metadata):
            self.metadata = Metadata(**as_dict(self.metadata))

        if self._is_empty(self.import_profile):
            self.MissingRequiredField("import_profile")
        if not isinstance(self.import_profile, ImportProfile):
            self.import_profile = ImportProfile(**as_dict(self.import_profile))

        if self._is_empty(self.system_characteristics):
            self.MissingRequiredField("system_characteristics")
        if not isinstance(self.system_characteristics, SystemCharacteristics):
            self.system_characteristics = SystemCharacteristics(**as_dict(self.system_characteristics))

        if self._is_empty(self.system_implementation):
            self.MissingRequiredField("system_implementation")
        if not isinstance(self.system_implementation, SystemImplementation):
            self.system_implementation = SystemImplementation(**as_dict(self.system_implementation))

        if self._is_empty(self.control_implementation):
            self.MissingRequiredField("control_implementation")
        if not isinstance(self.control_implementation, SspControlImplementation):
            self.control_implementation = SspControlImplementation(**as_dict(self.control_implementation))

        if self.back_matter is not None and not isinstance(self.back_matter, BackMatter):
            self.back_matter = BackMatter(**as_dict(self.back_matter))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ImportProfile(YAMLRoot):
    """
    Used to import the OSCAL profile representing the system's control baseline.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_SSP["ImportProfile"]
    class_class_curie: ClassVar[str] = "oscal_ssp:ImportProfile"
    class_name: ClassVar[str] = "ImportProfile"
    class_model_uri: ClassVar[URIRef] = OSCAL.ImportProfile

    href: str = None
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.href):
            self.MissingRequiredField("href")
        if not isinstance(self.href, str):
            self.href = str(self.href)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SystemCharacteristics(YAMLRoot):
    """
    Contains the characteristics of the system, such as its name, purpose, and security impact level.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_SSP["SystemCharacteristics"]
    class_class_curie: ClassVar[str] = "oscal_ssp:SystemCharacteristics"
    class_name: ClassVar[str] = "SystemCharacteristics"
    class_model_uri: ClassVar[URIRef] = OSCAL.SystemCharacteristics

    system_ids: Union[Union[dict, "SystemId"], list[Union[dict, "SystemId"]]] = None
    system_name: str = None
    description: str = None
    system_information: Union[dict, "SystemInformation"] = None
    system_status: Union[dict, "SystemStatus"] = None
    authorization_boundary: Union[dict, "AuthorizationBoundary"] = None
    system_name_short: Optional[str] = None
    date_authorized: Optional[str] = None
    security_sensitivity_level: Optional[str] = None
    security_impact_level: Optional[Union[dict, "SecurityImpactLevel"]] = None
    network_architecture: Optional[Union[dict, "NetworkArchitecture"]] = None
    data_flow: Optional[Union[dict, "DataFlow"]] = None
    responsible_parties: Optional[Union[Union[dict, "SspSystemCharacteristicsResponsibleParty"], list[Union[dict, "SspSystemCharacteristicsResponsibleParty"]]]] = empty_list()
    remarks: Optional[str] = None
    props: Optional[Union[Union[dict, "SspSystemCharacteristicsProp"], list[Union[dict, "SspSystemCharacteristicsProp"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.system_ids):
            self.MissingRequiredField("system_ids")
        self._normalize_inlined_as_list(slot_name="system_ids", slot_type=SystemId, key_name="id", keyed=False)

        if self._is_empty(self.system_name):
            self.MissingRequiredField("system_name")
        if not isinstance(self.system_name, str):
            self.system_name = str(self.system_name)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self._is_empty(self.system_information):
            self.MissingRequiredField("system_information")
        if not isinstance(self.system_information, SystemInformation):
            self.system_information = SystemInformation(**as_dict(self.system_information))

        if self._is_empty(self.system_status):
            self.MissingRequiredField("system_status")
        if not isinstance(self.system_status, SystemStatus):
            self.system_status = SystemStatus(**as_dict(self.system_status))

        if self._is_empty(self.authorization_boundary):
            self.MissingRequiredField("authorization_boundary")
        if not isinstance(self.authorization_boundary, AuthorizationBoundary):
            self.authorization_boundary = AuthorizationBoundary(**as_dict(self.authorization_boundary))

        if self.system_name_short is not None and not isinstance(self.system_name_short, str):
            self.system_name_short = str(self.system_name_short)

        if self.date_authorized is not None and not isinstance(self.date_authorized, str):
            self.date_authorized = str(self.date_authorized)

        if self.security_sensitivity_level is not None and not isinstance(self.security_sensitivity_level, str):
            self.security_sensitivity_level = str(self.security_sensitivity_level)

        if self.security_impact_level is not None and not isinstance(self.security_impact_level, SecurityImpactLevel):
            self.security_impact_level = SecurityImpactLevel(**as_dict(self.security_impact_level))

        if self.network_architecture is not None and not isinstance(self.network_architecture, NetworkArchitecture):
            self.network_architecture = NetworkArchitecture(**as_dict(self.network_architecture))

        if self.data_flow is not None and not isinstance(self.data_flow, DataFlow):
            self.data_flow = DataFlow(**as_dict(self.data_flow))

        self._normalize_inlined_as_list(slot_name="responsible_parties", slot_type=SspSystemCharacteristicsResponsibleParty, key_name="party-uuids", keyed=False)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        self._normalize_inlined_as_list(slot_name="props", slot_type=SspSystemCharacteristicsProp, key_name="name", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SystemInformation(YAMLRoot):
    """
    Contains details about all information types that are stored, processed, or transmitted by the system, such as
    privacy information.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_SSP["SystemInformation"]
    class_class_curie: ClassVar[str] = "oscal_ssp:SystemInformation"
    class_name: ClassVar[str] = "SystemInformation"
    class_model_uri: ClassVar[URIRef] = OSCAL.SystemInformation

    information_types: Union[Union[dict, "InformationType"], list[Union[dict, "InformationType"]]] = None
    props: Optional[Union[Union[dict, "SspSystemInformationProp"], list[Union[dict, "SspSystemInformationProp"]]]] = empty_list()
    links: Optional[Union[Union[dict, "SspSystemInformationLink"], list[Union[dict, "SspSystemInformationLink"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.information_types):
            self.MissingRequiredField("information_types")
        self._normalize_inlined_as_list(slot_name="information_types", slot_type=InformationType, key_name="title", keyed=False)

        self._normalize_inlined_as_list(slot_name="props", slot_type=SspSystemInformationProp, key_name="name", keyed=False)

        self._normalize_inlined_as_list(slot_name="links", slot_type=SspSystemInformationLink, key_name="href", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InformationType(YAMLRoot):
    """
    Contains details about one information type that is stored, processed, or transmitted by the system, such as
    privacy information, and its impact level.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_SSP["InformationType"]
    class_class_curie: ClassVar[str] = "oscal_ssp:InformationType"
    class_name: ClassVar[str] = "InformationType"
    class_model_uri: ClassVar[URIRef] = OSCAL.InformationType

    title: str = None
    description: str = None
    uuid: Optional[str] = None
    categorizations: Optional[Union[Union[dict, "InformationTypeCategorization"], list[Union[dict, "InformationTypeCategorization"]]]] = empty_list()
    props: Optional[Union[Union[dict, Property], list[Union[dict, Property]]]] = empty_list()
    links: Optional[Union[Union[dict, Link], list[Union[dict, Link]]]] = empty_list()
    confidentiality_impact: Optional[Union[dict, "ImpactLevel"]] = None
    integrity_impact: Optional[Union[dict, "ImpactLevel"]] = None
    availability_impact: Optional[Union[dict, "ImpactLevel"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self.uuid is not None and not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        self._normalize_inlined_as_list(slot_name="categorizations", slot_type=InformationTypeCategorization, key_name="system", keyed=False)

        self._normalize_inlined_as_list(slot_name="props", slot_type=Property, key_name="name", keyed=False)

        self._normalize_inlined_as_list(slot_name="links", slot_type=Link, key_name="href", keyed=False)

        if self.confidentiality_impact is not None and not isinstance(self.confidentiality_impact, ImpactLevel):
            self.confidentiality_impact = ImpactLevel(**as_dict(self.confidentiality_impact))

        if self.integrity_impact is not None and not isinstance(self.integrity_impact, ImpactLevel):
            self.integrity_impact = ImpactLevel(**as_dict(self.integrity_impact))

        if self.availability_impact is not None and not isinstance(self.availability_impact, ImpactLevel):
            self.availability_impact = ImpactLevel(**as_dict(self.availability_impact))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InformationTypeCategorization(YAMLRoot):
    """
    A set of information type identifiers qualified by the given identification system used.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_SSP["InformationTypeCategorization"]
    class_class_curie: ClassVar[str] = "oscal_ssp:InformationTypeCategorization"
    class_name: ClassVar[str] = "InformationTypeCategorization"
    class_model_uri: ClassVar[URIRef] = OSCAL.InformationTypeCategorization

    system: str = None
    information_type_ids: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.system):
            self.MissingRequiredField("system")
        if not isinstance(self.system, str):
            self.system = str(self.system)

        if not isinstance(self.information_type_ids, list):
            self.information_type_ids = [self.information_type_ids] if self.information_type_ids is not None else []
        self.information_type_ids = [v if isinstance(v, str) else str(v) for v in self.information_type_ids]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ImpactLevel(YAMLRoot):
    """
    The expected level of impact resulting from the described information's confidentiality, integrity, or
    availability affect.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_SSP["ImpactLevel"]
    class_class_curie: ClassVar[str] = "oscal_ssp:ImpactLevel"
    class_name: ClassVar[str] = "ImpactLevel"
    class_model_uri: ClassVar[URIRef] = OSCAL.ImpactLevel

    base: str = None
    props: Optional[Union[Union[dict, Property], list[Union[dict, Property]]]] = empty_list()
    links: Optional[Union[Union[dict, Link], list[Union[dict, Link]]]] = empty_list()
    selected: Optional[str] = None
    adjustment_justification: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.base):
            self.MissingRequiredField("base")
        if not isinstance(self.base, str):
            self.base = str(self.base)

        self._normalize_inlined_as_list(slot_name="props", slot_type=Property, key_name="name", keyed=False)

        self._normalize_inlined_as_list(slot_name="links", slot_type=Link, key_name="href", keyed=False)

        if self.selected is not None and not isinstance(self.selected, str):
            self.selected = str(self.selected)

        if self.adjustment_justification is not None and not isinstance(self.adjustment_justification, str):
            self.adjustment_justification = str(self.adjustment_justification)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SecurityImpactLevel(YAMLRoot):
    """
    The overall level of expected impact resulting from unauthorized disclosure, modification, or loss of access to
    information.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_SSP["SecurityImpactLevel"]
    class_class_curie: ClassVar[str] = "oscal_ssp:SecurityImpactLevel"
    class_name: ClassVar[str] = "SecurityImpactLevel"
    class_model_uri: ClassVar[URIRef] = OSCAL.SecurityImpactLevel

    security_objective_confidentiality: str = None
    security_objective_integrity: str = None
    security_objective_availability: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.security_objective_confidentiality):
            self.MissingRequiredField("security_objective_confidentiality")
        if not isinstance(self.security_objective_confidentiality, str):
            self.security_objective_confidentiality = str(self.security_objective_confidentiality)

        if self._is_empty(self.security_objective_integrity):
            self.MissingRequiredField("security_objective_integrity")
        if not isinstance(self.security_objective_integrity, str):
            self.security_objective_integrity = str(self.security_objective_integrity)

        if self._is_empty(self.security_objective_availability):
            self.MissingRequiredField("security_objective_availability")
        if not isinstance(self.security_objective_availability, str):
            self.security_objective_availability = str(self.security_objective_availability)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SystemStatus(YAMLRoot):
    """
    Describes the operational status of the system.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_SSP["SystemStatus"]
    class_class_curie: ClassVar[str] = "oscal_ssp:SystemStatus"
    class_name: ClassVar[str] = "SystemStatus"
    class_model_uri: ClassVar[URIRef] = OSCAL.SystemStatus

    state: Union[str, "SystemOperatingStatusEnum"] = None
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.state):
            self.MissingRequiredField("state")
        if not isinstance(self.state, SystemOperatingStatusEnum):
            self.state = SystemOperatingStatusEnum(self.state)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AuthorizationBoundary(YAMLRoot):
    """
    A description of this system's authorization boundary, optionally supplemented with diagrams that illustrate the
    authorization boundary.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_SSP["AuthorizationBoundary"]
    class_class_curie: ClassVar[str] = "oscal_ssp:AuthorizationBoundary"
    class_name: ClassVar[str] = "AuthorizationBoundary"
    class_model_uri: ClassVar[URIRef] = OSCAL.AuthorizationBoundary

    description: str = None
    props: Optional[Union[Union[dict, Property], list[Union[dict, Property]]]] = empty_list()
    links: Optional[Union[Union[dict, Link], list[Union[dict, Link]]]] = empty_list()
    diagrams: Optional[Union[Union[dict, "Diagram"], list[Union[dict, "Diagram"]]]] = empty_list()
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_list(slot_name="props", slot_type=Property, key_name="name", keyed=False)

        self._normalize_inlined_as_list(slot_name="links", slot_type=Link, key_name="href", keyed=False)

        self._normalize_inlined_as_list(slot_name="diagrams", slot_type=Diagram, key_name="uuid", keyed=False)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Diagram(YAMLRoot):
    """
    A graphic that provides a visual representation the system, or some aspect of it.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_SSP["Diagram"]
    class_class_curie: ClassVar[str] = "oscal_ssp:Diagram"
    class_name: ClassVar[str] = "Diagram"
    class_model_uri: ClassVar[URIRef] = OSCAL.Diagram

    uuid: str = None
    description: Optional[str] = None
    props: Optional[Union[Union[dict, Property], list[Union[dict, Property]]]] = empty_list()
    links: Optional[Union[Union[dict, "SspDiagramLink"], list[Union[dict, "SspDiagramLink"]]]] = empty_list()
    caption: Optional[str] = None
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uuid):
            self.MissingRequiredField("uuid")
        if not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_list(slot_name="props", slot_type=Property, key_name="name", keyed=False)

        self._normalize_inlined_as_list(slot_name="links", slot_type=SspDiagramLink, key_name="href", keyed=False)

        if self.caption is not None and not isinstance(self.caption, str):
            self.caption = str(self.caption)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NetworkArchitecture(YAMLRoot):
    """
    A description of the system's network architecture, optionally supplemented with diagrams that illustrate the
    network architecture.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_SSP["NetworkArchitecture"]
    class_class_curie: ClassVar[str] = "oscal_ssp:NetworkArchitecture"
    class_name: ClassVar[str] = "NetworkArchitecture"
    class_model_uri: ClassVar[URIRef] = OSCAL.NetworkArchitecture

    description: str = None
    props: Optional[Union[Union[dict, Property], list[Union[dict, Property]]]] = empty_list()
    links: Optional[Union[Union[dict, Link], list[Union[dict, Link]]]] = empty_list()
    diagrams: Optional[Union[Union[dict, Diagram], list[Union[dict, Diagram]]]] = empty_list()
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_list(slot_name="props", slot_type=Property, key_name="name", keyed=False)

        self._normalize_inlined_as_list(slot_name="links", slot_type=Link, key_name="href", keyed=False)

        self._normalize_inlined_as_list(slot_name="diagrams", slot_type=Diagram, key_name="uuid", keyed=False)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataFlow(YAMLRoot):
    """
    A description of the logical flow of information within the system and across its boundaries, optionally
    supplemented with diagrams.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_SSP["DataFlow"]
    class_class_curie: ClassVar[str] = "oscal_ssp:DataFlow"
    class_name: ClassVar[str] = "DataFlow"
    class_model_uri: ClassVar[URIRef] = OSCAL.DataFlow

    description: str = None
    props: Optional[Union[Union[dict, Property], list[Union[dict, Property]]]] = empty_list()
    links: Optional[Union[Union[dict, Link], list[Union[dict, Link]]]] = empty_list()
    diagrams: Optional[Union[Union[dict, Diagram], list[Union[dict, Diagram]]]] = empty_list()
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_list(slot_name="props", slot_type=Property, key_name="name", keyed=False)

        self._normalize_inlined_as_list(slot_name="links", slot_type=Link, key_name="href", keyed=False)

        self._normalize_inlined_as_list(slot_name="diagrams", slot_type=Diagram, key_name="uuid", keyed=False)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SystemImplementation(YAMLRoot):
    """
    Provides information as to how the system is implemented.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_SSP["SystemImplementation"]
    class_class_curie: ClassVar[str] = "oscal_ssp:SystemImplementation"
    class_name: ClassVar[str] = "SystemImplementation"
    class_model_uri: ClassVar[URIRef] = OSCAL.SystemImplementation

    components: Union[Union[dict, "SspSystemComponent"], list[Union[dict, "SspSystemComponent"]]] = None
    props: Optional[Union[Union[dict, Property], list[Union[dict, Property]]]] = empty_list()
    links: Optional[Union[Union[dict, Link], list[Union[dict, Link]]]] = empty_list()
    leveraged_authorizations: Optional[Union[Union[dict, "LeveragedAuthorization"], list[Union[dict, "LeveragedAuthorization"]]]] = empty_list()
    users: Optional[Union[Union[dict, "SystemUser"], list[Union[dict, "SystemUser"]]]] = empty_list()
    inventory_items: Optional[Union[Union[dict, "SspInventoryItem"], list[Union[dict, "SspInventoryItem"]]]] = empty_list()
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.components):
            self.MissingRequiredField("components")
        self._normalize_inlined_as_list(slot_name="components", slot_type=SspSystemComponent, key_name="uuid", keyed=False)

        self._normalize_inlined_as_list(slot_name="props", slot_type=Property, key_name="name", keyed=False)

        self._normalize_inlined_as_list(slot_name="links", slot_type=Link, key_name="href", keyed=False)

        self._normalize_inlined_as_list(slot_name="leveraged_authorizations", slot_type=LeveragedAuthorization, key_name="uuid", keyed=False)

        self._normalize_inlined_as_list(slot_name="users", slot_type=SystemUser, key_name="uuid", keyed=False)

        self._normalize_inlined_as_list(slot_name="inventory_items", slot_type=SspInventoryItem, key_name="uuid", keyed=False)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LeveragedAuthorization(YAMLRoot):
    """
    A description of another authorized system from which this system inherits capabilities that satisfy security
    requirements. Another term for this concept is a common control provider.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_SSP["LeveragedAuthorization"]
    class_class_curie: ClassVar[str] = "oscal_ssp:LeveragedAuthorization"
    class_name: ClassVar[str] = "LeveragedAuthorization"
    class_model_uri: ClassVar[URIRef] = OSCAL.LeveragedAuthorization

    uuid: str = None
    title: str = None
    party_uuid: str = None
    date_authorized: str = None
    props: Optional[Union[Union[dict, Property], list[Union[dict, Property]]]] = empty_list()
    links: Optional[Union[Union[dict, "SspLeveragedAuthorizationLink"], list[Union[dict, "SspLeveragedAuthorizationLink"]]]] = empty_list()
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uuid):
            self.MissingRequiredField("uuid")
        if not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self._is_empty(self.party_uuid):
            self.MissingRequiredField("party_uuid")
        if not isinstance(self.party_uuid, str):
            self.party_uuid = str(self.party_uuid)

        if self._is_empty(self.date_authorized):
            self.MissingRequiredField("date_authorized")
        if not isinstance(self.date_authorized, str):
            self.date_authorized = str(self.date_authorized)

        self._normalize_inlined_as_list(slot_name="props", slot_type=Property, key_name="name", keyed=False)

        self._normalize_inlined_as_list(slot_name="links", slot_type=SspLeveragedAuthorizationLink, key_name="href", keyed=False)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SspControlImplementation(YAMLRoot):
    """
    Describes how the system satisfies a set of controls.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_SSP["SspControlImplementation"]
    class_class_curie: ClassVar[str] = "oscal_ssp:SspControlImplementation"
    class_name: ClassVar[str] = "SspControlImplementation"
    class_model_uri: ClassVar[URIRef] = OSCAL.SspControlImplementation

    description: str = None
    implemented_requirements: Union[Union[dict, "SspImplementedRequirement"], list[Union[dict, "SspImplementedRequirement"]]] = None
    set_parameters: Optional[Union[Union[dict, "SetParameter"], list[Union[dict, "SetParameter"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self._is_empty(self.implemented_requirements):
            self.MissingRequiredField("implemented_requirements")
        self._normalize_inlined_as_list(slot_name="implemented_requirements", slot_type=SspImplementedRequirement, key_name="uuid", keyed=False)

        self._normalize_inlined_as_list(slot_name="set_parameters", slot_type=SetParameter, key_name="param-id", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SspImplementedRequirement(YAMLRoot):
    """
    Describes how the system satisfies an individual control.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_SSP["SspImplementedRequirement"]
    class_class_curie: ClassVar[str] = "oscal_ssp:SspImplementedRequirement"
    class_name: ClassVar[str] = "SspImplementedRequirement"
    class_model_uri: ClassVar[URIRef] = OSCAL.SspImplementedRequirement

    uuid: str = None
    control_id: str = None
    props: Optional[Union[Union[dict, "SspControlOriginationProp"], list[Union[dict, "SspControlOriginationProp"]]]] = empty_list()
    links: Optional[Union[Union[dict, Link], list[Union[dict, Link]]]] = empty_list()
    set_parameters: Optional[Union[Union[dict, "SetParameter"], list[Union[dict, "SetParameter"]]]] = empty_list()
    responsible_roles: Optional[Union[Union[dict, "SspImplementedRequirementResponsibleRole"], list[Union[dict, "SspImplementedRequirementResponsibleRole"]]]] = empty_list()
    statements: Optional[Union[Union[dict, "SspStatement"], list[Union[dict, "SspStatement"]]]] = empty_list()
    by_components: Optional[Union[Union[dict, "ByComponent"], list[Union[dict, "ByComponent"]]]] = empty_list()
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uuid):
            self.MissingRequiredField("uuid")
        if not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        if self._is_empty(self.control_id):
            self.MissingRequiredField("control_id")
        if not isinstance(self.control_id, str):
            self.control_id = str(self.control_id)

        self._normalize_inlined_as_list(slot_name="props", slot_type=SspControlOriginationProp, key_name="name", keyed=False)

        self._normalize_inlined_as_list(slot_name="links", slot_type=Link, key_name="href", keyed=False)

        self._normalize_inlined_as_list(slot_name="set_parameters", slot_type=SetParameter, key_name="param-id", keyed=False)

        self._normalize_inlined_as_list(slot_name="responsible_roles", slot_type=SspImplementedRequirementResponsibleRole, key_name="role-id", keyed=False)

        self._normalize_inlined_as_list(slot_name="statements", slot_type=SspStatement, key_name="statement-id", keyed=False)

        self._normalize_inlined_as_list(slot_name="by_components", slot_type=ByComponent, key_name="component-uuid", keyed=False)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SspStatement(YAMLRoot):
    """
    Identifies which statements within a control are addressed.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_SSP["SspStatement"]
    class_class_curie: ClassVar[str] = "oscal_ssp:SspStatement"
    class_name: ClassVar[str] = "SspStatement"
    class_model_uri: ClassVar[URIRef] = OSCAL.SspStatement

    statement_id: str = None
    uuid: str = None
    props: Optional[Union[Union[dict, "SspControlOriginationProp"], list[Union[dict, "SspControlOriginationProp"]]]] = empty_list()
    links: Optional[Union[Union[dict, Link], list[Union[dict, Link]]]] = empty_list()
    responsible_roles: Optional[Union[Union[dict, "SspImplementedRequirementResponsibleRole"], list[Union[dict, "SspImplementedRequirementResponsibleRole"]]]] = empty_list()
    by_components: Optional[Union[Union[dict, "ByComponent"], list[Union[dict, "ByComponent"]]]] = empty_list()
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.statement_id):
            self.MissingRequiredField("statement_id")
        if not isinstance(self.statement_id, str):
            self.statement_id = str(self.statement_id)

        if self._is_empty(self.uuid):
            self.MissingRequiredField("uuid")
        if not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        self._normalize_inlined_as_list(slot_name="props", slot_type=SspControlOriginationProp, key_name="name", keyed=False)

        self._normalize_inlined_as_list(slot_name="links", slot_type=Link, key_name="href", keyed=False)

        self._normalize_inlined_as_list(slot_name="responsible_roles", slot_type=SspImplementedRequirementResponsibleRole, key_name="role-id", keyed=False)

        self._normalize_inlined_as_list(slot_name="by_components", slot_type=ByComponent, key_name="component-uuid", keyed=False)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ByComponent(YAMLRoot):
    """
    Defines how the referenced component implements a set of controls.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_SSP["ByComponent"]
    class_class_curie: ClassVar[str] = "oscal_ssp:ByComponent"
    class_name: ClassVar[str] = "ByComponent"
    class_model_uri: ClassVar[URIRef] = OSCAL.ByComponent

    component_uuid: str = None
    uuid: str = None
    description: str = None
    props: Optional[Union[Union[dict, "SspControlOriginationProp"], list[Union[dict, "SspControlOriginationProp"]]]] = empty_list()
    links: Optional[Union[Union[dict, "SspByComponentLink"], list[Union[dict, "SspByComponentLink"]]]] = empty_list()
    set_parameters: Optional[Union[Union[dict, "SetParameter"], list[Union[dict, "SetParameter"]]]] = empty_list()
    implementation_status: Optional[Union[dict, "ImplementationStatus"]] = None
    export: Optional[Union[dict, "Export"]] = None
    inherited: Optional[Union[Union[dict, "InheritedControlImplementation"], list[Union[dict, "InheritedControlImplementation"]]]] = empty_list()
    satisfied: Optional[Union[Union[dict, "SatisfiedControlImplementation"], list[Union[dict, "SatisfiedControlImplementation"]]]] = empty_list()
    responsible_roles: Optional[Union[Union[dict, "SspByComponentResponsibleRole"], list[Union[dict, "SspByComponentResponsibleRole"]]]] = empty_list()
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.component_uuid):
            self.MissingRequiredField("component_uuid")
        if not isinstance(self.component_uuid, str):
            self.component_uuid = str(self.component_uuid)

        if self._is_empty(self.uuid):
            self.MissingRequiredField("uuid")
        if not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_list(slot_name="props", slot_type=SspControlOriginationProp, key_name="name", keyed=False)

        self._normalize_inlined_as_list(slot_name="links", slot_type=SspByComponentLink, key_name="href", keyed=False)

        self._normalize_inlined_as_list(slot_name="set_parameters", slot_type=SetParameter, key_name="param-id", keyed=False)

        if self.implementation_status is not None and not isinstance(self.implementation_status, ImplementationStatus):
            self.implementation_status = ImplementationStatus(**as_dict(self.implementation_status))

        if self.export is not None and not isinstance(self.export, Export):
            self.export = Export(**as_dict(self.export))

        self._normalize_inlined_as_list(slot_name="inherited", slot_type=InheritedControlImplementation, key_name="uuid", keyed=False)

        self._normalize_inlined_as_list(slot_name="satisfied", slot_type=SatisfiedControlImplementation, key_name="uuid", keyed=False)

        self._normalize_inlined_as_list(slot_name="responsible_roles", slot_type=SspByComponentResponsibleRole, key_name="role-id", keyed=False)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Export(YAMLRoot):
    """
    Defines a set of control implementations that are provided as reference implementations for use by organizations
    implementing the leveraged system.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_SSP["Export"]
    class_class_curie: ClassVar[str] = "oscal_ssp:Export"
    class_name: ClassVar[str] = "Export"
    class_model_uri: ClassVar[URIRef] = OSCAL.Export

    description: Optional[str] = None
    props: Optional[Union[Union[dict, Property], list[Union[dict, Property]]]] = empty_list()
    links: Optional[Union[Union[dict, Link], list[Union[dict, Link]]]] = empty_list()
    provided: Optional[Union[Union[dict, "ProvidedControlImplementation"], list[Union[dict, "ProvidedControlImplementation"]]]] = empty_list()
    responsibilities: Optional[Union[Union[dict, "ControlResponsibility"], list[Union[dict, "ControlResponsibility"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_list(slot_name="props", slot_type=Property, key_name="name", keyed=False)

        self._normalize_inlined_as_list(slot_name="links", slot_type=Link, key_name="href", keyed=False)

        self._normalize_inlined_as_list(slot_name="provided", slot_type=ProvidedControlImplementation, key_name="uuid", keyed=False)

        self._normalize_inlined_as_list(slot_name="responsibilities", slot_type=ControlResponsibility, key_name="uuid", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ProvidedControlImplementation(YAMLRoot):
    """
    Describes a capability which may be inherited by a leveraging system.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_SSP["ProvidedControlImplementation"]
    class_class_curie: ClassVar[str] = "oscal_ssp:ProvidedControlImplementation"
    class_name: ClassVar[str] = "ProvidedControlImplementation"
    class_model_uri: ClassVar[URIRef] = OSCAL.ProvidedControlImplementation

    uuid: str = None
    description: str = None
    props: Optional[Union[Union[dict, Property], list[Union[dict, Property]]]] = empty_list()
    links: Optional[Union[Union[dict, Link], list[Union[dict, Link]]]] = empty_list()
    responsible_roles: Optional[Union[Union[dict, "SspByComponentResponsibleRole"], list[Union[dict, "SspByComponentResponsibleRole"]]]] = empty_list()
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uuid):
            self.MissingRequiredField("uuid")
        if not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_list(slot_name="props", slot_type=Property, key_name="name", keyed=False)

        self._normalize_inlined_as_list(slot_name="links", slot_type=Link, key_name="href", keyed=False)

        self._normalize_inlined_as_list(slot_name="responsible_roles", slot_type=SspByComponentResponsibleRole, key_name="role-id", keyed=False)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ControlResponsibility(YAMLRoot):
    """
    Describes a control implementation responsibility imposed on a leveraging system.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_SSP["ControlResponsibility"]
    class_class_curie: ClassVar[str] = "oscal_ssp:ControlResponsibility"
    class_name: ClassVar[str] = "ControlResponsibility"
    class_model_uri: ClassVar[URIRef] = OSCAL.ControlResponsibility

    uuid: str = None
    description: str = None
    provided_uuid: Optional[str] = None
    props: Optional[Union[Union[dict, Property], list[Union[dict, Property]]]] = empty_list()
    links: Optional[Union[Union[dict, Link], list[Union[dict, Link]]]] = empty_list()
    responsible_roles: Optional[Union[Union[dict, "SspByComponentResponsibleRole"], list[Union[dict, "SspByComponentResponsibleRole"]]]] = empty_list()
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uuid):
            self.MissingRequiredField("uuid")
        if not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self.provided_uuid is not None and not isinstance(self.provided_uuid, str):
            self.provided_uuid = str(self.provided_uuid)

        self._normalize_inlined_as_list(slot_name="props", slot_type=Property, key_name="name", keyed=False)

        self._normalize_inlined_as_list(slot_name="links", slot_type=Link, key_name="href", keyed=False)

        self._normalize_inlined_as_list(slot_name="responsible_roles", slot_type=SspByComponentResponsibleRole, key_name="role-id", keyed=False)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InheritedControlImplementation(YAMLRoot):
    """
    Describes a control implementation inherited by a leveraging system.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_SSP["InheritedControlImplementation"]
    class_class_curie: ClassVar[str] = "oscal_ssp:InheritedControlImplementation"
    class_name: ClassVar[str] = "InheritedControlImplementation"
    class_model_uri: ClassVar[URIRef] = OSCAL.InheritedControlImplementation

    uuid: str = None
    description: str = None
    provided_uuid: Optional[str] = None
    props: Optional[Union[Union[dict, Property], list[Union[dict, Property]]]] = empty_list()
    links: Optional[Union[Union[dict, Link], list[Union[dict, Link]]]] = empty_list()
    responsible_roles: Optional[Union[Union[dict, "SspByComponentResponsibleRole"], list[Union[dict, "SspByComponentResponsibleRole"]]]] = empty_list()
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uuid):
            self.MissingRequiredField("uuid")
        if not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self.provided_uuid is not None and not isinstance(self.provided_uuid, str):
            self.provided_uuid = str(self.provided_uuid)

        self._normalize_inlined_as_list(slot_name="props", slot_type=Property, key_name="name", keyed=False)

        self._normalize_inlined_as_list(slot_name="links", slot_type=Link, key_name="href", keyed=False)

        self._normalize_inlined_as_list(slot_name="responsible_roles", slot_type=SspByComponentResponsibleRole, key_name="role-id", keyed=False)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SatisfiedControlImplementation(YAMLRoot):
    """
    Describes how this system satisfies a responsibility imposed by a leveraged system.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_SSP["SatisfiedControlImplementation"]
    class_class_curie: ClassVar[str] = "oscal_ssp:SatisfiedControlImplementation"
    class_name: ClassVar[str] = "SatisfiedControlImplementation"
    class_model_uri: ClassVar[URIRef] = OSCAL.SatisfiedControlImplementation

    uuid: str = None
    description: str = None
    responsibility_uuid: Optional[str] = None
    props: Optional[Union[Union[dict, Property], list[Union[dict, Property]]]] = empty_list()
    links: Optional[Union[Union[dict, Link], list[Union[dict, Link]]]] = empty_list()
    responsible_roles: Optional[Union[Union[dict, "SspByComponentResponsibleRole"], list[Union[dict, "SspByComponentResponsibleRole"]]]] = empty_list()
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uuid):
            self.MissingRequiredField("uuid")
        if not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self.responsibility_uuid is not None and not isinstance(self.responsibility_uuid, str):
            self.responsibility_uuid = str(self.responsibility_uuid)

        self._normalize_inlined_as_list(slot_name="props", slot_type=Property, key_name="name", keyed=False)

        self._normalize_inlined_as_list(slot_name="links", slot_type=Link, key_name="href", keyed=False)

        self._normalize_inlined_as_list(slot_name="responsible_roles", slot_type=SspByComponentResponsibleRole, key_name="role-id", keyed=False)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SspSystemCharacteristicsProp(Property):
    """
    SSP-scoped property used in system characteristics.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_SSP["SspSystemCharacteristicsProp"]
    class_class_curie: ClassVar[str] = "oscal_ssp:SspSystemCharacteristicsProp"
    class_name: ClassVar[str] = "SspSystemCharacteristicsProp"
    class_model_uri: ClassVar[URIRef] = OSCAL.SspSystemCharacteristicsProp

    name: Union[str, "SystemCharacteristicsPropNameEnum"] = None
    value: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, SystemCharacteristicsPropNameEnum):
            self.name = SystemCharacteristicsPropNameEnum(self.name)

        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, str):
            self.value = str(self.value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SspSystemInformationProp(Property):
    """
    SSP-scoped property used in system information.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_SSP["SspSystemInformationProp"]
    class_class_curie: ClassVar[str] = "oscal_ssp:SspSystemInformationProp"
    class_name: ClassVar[str] = "SspSystemInformationProp"
    class_model_uri: ClassVar[URIRef] = OSCAL.SspSystemInformationProp

    name: Union[str, "SystemInformationPropNameEnum"] = None
    value: Union[str, "PrivacyDesignationEnum"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, SystemInformationPropNameEnum):
            self.name = SystemInformationPropNameEnum(self.name)

        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, PrivacyDesignationEnum):
            self.value = PrivacyDesignationEnum(self.value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SspControlOriginationProp(Property):
    """
    SSP-scoped property used in implemented requirement and by-component contexts.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_SSP["SspControlOriginationProp"]
    class_class_curie: ClassVar[str] = "oscal_ssp:SspControlOriginationProp"
    class_name: ClassVar[str] = "SspControlOriginationProp"
    class_model_uri: ClassVar[URIRef] = OSCAL.SspControlOriginationProp

    name: Union[str, "ControlOriginationPropNameEnum"] = None
    value: Union[str, "ControlOriginationValueEnum"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, ControlOriginationPropNameEnum):
            self.name = ControlOriginationPropNameEnum(self.name)

        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, ControlOriginationValueEnum):
            self.value = ControlOriginationValueEnum(self.value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SspAllowsAuthenticatedScanProp(Property):
    """
    SSP-scoped property used for component and inventory allows-authenticated-scan.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_SSP["SspAllowsAuthenticatedScanProp"]
    class_class_curie: ClassVar[str] = "oscal_ssp:SspAllowsAuthenticatedScanProp"
    class_name: ClassVar[str] = "SspAllowsAuthenticatedScanProp"
    class_model_uri: ClassVar[URIRef] = OSCAL.SspAllowsAuthenticatedScanProp

    name: str = None
    value: Union[str, "AllowsAuthenticatedScanEnum"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, AllowsAuthenticatedScanEnum):
            self.value = AllowsAuthenticatedScanEnum(self.value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SspSystemInformationLink(Link):
    """
    SSP-scoped link used in system information.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_SSP["SspSystemInformationLink"]
    class_class_curie: ClassVar[str] = "oscal_ssp:SspSystemInformationLink"
    class_name: ClassVar[str] = "SspSystemInformationLink"
    class_model_uri: ClassVar[URIRef] = OSCAL.SspSystemInformationLink

    href: str = None
    rel: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.rel is not None and not isinstance(self.rel, str):
            self.rel = str(self.rel)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SspDiagramLink(Link):
    """
    SSP-scoped link used in diagram objects.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_SSP["SspDiagramLink"]
    class_class_curie: ClassVar[str] = "oscal_ssp:SspDiagramLink"
    class_name: ClassVar[str] = "SspDiagramLink"
    class_model_uri: ClassVar[URIRef] = OSCAL.SspDiagramLink

    href: str = None
    rel: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.rel is not None and not isinstance(self.rel, str):
            self.rel = str(self.rel)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SspLeveragedAuthorizationLink(Link):
    """
    SSP-scoped link used in leveraged authorization objects.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_SSP["SspLeveragedAuthorizationLink"]
    class_class_curie: ClassVar[str] = "oscal_ssp:SspLeveragedAuthorizationLink"
    class_name: ClassVar[str] = "SspLeveragedAuthorizationLink"
    class_model_uri: ClassVar[URIRef] = OSCAL.SspLeveragedAuthorizationLink

    href: str = None
    rel: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.rel is not None and not isinstance(self.rel, str):
            self.rel = str(self.rel)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SspByComponentLink(Link):
    """
    SSP-scoped link used in by-component contexts.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_SSP["SspByComponentLink"]
    class_class_curie: ClassVar[str] = "oscal_ssp:SspByComponentLink"
    class_name: ClassVar[str] = "SspByComponentLink"
    class_model_uri: ClassVar[URIRef] = OSCAL.SspByComponentLink

    href: str = None
    rel: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.rel is not None and not isinstance(self.rel, str):
            self.rel = str(self.rel)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SspSystemCharacteristicsResponsibleParty(ResponsibleParty):
    """
    SSP-scoped responsible party for system characteristics.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_SSP["SspSystemCharacteristicsResponsibleParty"]
    class_class_curie: ClassVar[str] = "oscal_ssp:SspSystemCharacteristicsResponsibleParty"
    class_name: ClassVar[str] = "SspSystemCharacteristicsResponsibleParty"
    class_model_uri: ClassVar[URIRef] = OSCAL.SspSystemCharacteristicsResponsibleParty

    party_uuids: Union[str, list[str]] = None
    role_id: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.role_id):
            self.MissingRequiredField("role_id")
        if not isinstance(self.role_id, str):
            self.role_id = str(self.role_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SspImplementedRequirementResponsibleRole(ResponsibleRole):
    """
    SSP-scoped responsible role used by implemented requirement and statement contexts.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_SSP["SspImplementedRequirementResponsibleRole"]
    class_class_curie: ClassVar[str] = "oscal_ssp:SspImplementedRequirementResponsibleRole"
    class_name: ClassVar[str] = "SspImplementedRequirementResponsibleRole"
    class_model_uri: ClassVar[URIRef] = OSCAL.SspImplementedRequirementResponsibleRole

    role_id: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.role_id):
            self.MissingRequiredField("role_id")
        if not isinstance(self.role_id, str):
            self.role_id = str(self.role_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SspByComponentResponsibleRole(ResponsibleRole):
    """
    SSP-scoped responsible role used by by-component contexts.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_SSP["SspByComponentResponsibleRole"]
    class_class_curie: ClassVar[str] = "oscal_ssp:SspByComponentResponsibleRole"
    class_name: ClassVar[str] = "SspByComponentResponsibleRole"
    class_model_uri: ClassVar[URIRef] = OSCAL.SspByComponentResponsibleRole

    role_id: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.role_id):
            self.MissingRequiredField("role_id")
        if not isinstance(self.role_id, str):
            self.role_id = str(self.role_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AssessmentPlanDocument(OscalDocument):
    """
    Root wrapper for an OSCAL Assessment Plan document.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["AssessmentPlanDocument"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:AssessmentPlanDocument"
    class_name: ClassVar[str] = "AssessmentPlanDocument"
    class_model_uri: ClassVar[URIRef] = OSCAL.AssessmentPlanDocument

    assessment_plan: Union[dict, "AssessmentPlan"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.assessment_plan):
            self.MissingRequiredField("assessment_plan")
        if not isinstance(self.assessment_plan, AssessmentPlan):
            self.assessment_plan = AssessmentPlan(**as_dict(self.assessment_plan))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AssessmentPlan(YAMLRoot):
    """
    An assessment plan, such as those provided by a FedRAMP assessor.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["AssessmentPlan"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:AssessmentPlan"
    class_name: ClassVar[str] = "AssessmentPlan"
    class_model_uri: ClassVar[URIRef] = OSCAL.AssessmentPlan

    uuid: str = None
    metadata: Union[dict, Metadata] = None
    import_ssp: Union[dict, "ImportSSP"] = None
    reviewed_controls: Union[dict, "ReviewedControls"] = None
    local_definitions: Optional[Union[dict, "LocalDefinitions"]] = None
    terms_and_conditions: Optional[Union[dict, "TermsAndConditions"]] = None
    assessment_subjects: Optional[Union[Union[dict, "AssessmentSubject"], list[Union[dict, "AssessmentSubject"]]]] = empty_list()
    assessment_assets: Optional[Union[dict, "AssessmentAssets"]] = None
    tasks: Optional[Union[Union[dict, "Task"], list[Union[dict, "Task"]]]] = empty_list()
    back_matter: Optional[Union[dict, BackMatter]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uuid):
            self.MissingRequiredField("uuid")
        if not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        if self._is_empty(self.metadata):
            self.MissingRequiredField("metadata")
        if not isinstance(self.metadata, Metadata):
            self.metadata = Metadata(**as_dict(self.metadata))

        if self._is_empty(self.import_ssp):
            self.MissingRequiredField("import_ssp")
        if not isinstance(self.import_ssp, ImportSSP):
            self.import_ssp = ImportSSP(**as_dict(self.import_ssp))

        if self._is_empty(self.reviewed_controls):
            self.MissingRequiredField("reviewed_controls")
        if not isinstance(self.reviewed_controls, ReviewedControls):
            self.reviewed_controls = ReviewedControls(**as_dict(self.reviewed_controls))

        if self.local_definitions is not None and not isinstance(self.local_definitions, LocalDefinitions):
            self.local_definitions = LocalDefinitions(**as_dict(self.local_definitions))

        if self.terms_and_conditions is not None and not isinstance(self.terms_and_conditions, TermsAndConditions):
            self.terms_and_conditions = TermsAndConditions(**as_dict(self.terms_and_conditions))

        self._normalize_inlined_as_list(slot_name="assessment_subjects", slot_type=AssessmentSubject, key_name="type", keyed=False)

        if self.assessment_assets is not None and not isinstance(self.assessment_assets, AssessmentAssets):
            self.assessment_assets = AssessmentAssets(**as_dict(self.assessment_assets))

        self._normalize_inlined_as_list(slot_name="tasks", slot_type=Task, key_name="uuid", keyed=False)

        if self.back_matter is not None and not isinstance(self.back_matter, BackMatter):
            self.back_matter = BackMatter(**as_dict(self.back_matter))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ImportSSP(YAMLRoot):
    """
    Used by the assessment plan and POA&M to import information about the system.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["ImportSSP"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:ImportSSP"
    class_name: ClassVar[str] = "ImportSSP"
    class_model_uri: ClassVar[URIRef] = OSCAL.ImportSSP

    href: str = None
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.href):
            self.MissingRequiredField("href")
        if not isinstance(self.href, str):
            self.href = str(self.href)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LocalDefinitions(YAMLRoot):
    """
    Used to define data objects that are used in the assessment plan, that do not appear in the referenced SSP.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["LocalDefinitions"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:LocalDefinitions"
    class_name: ClassVar[str] = "LocalDefinitions"
    class_model_uri: ClassVar[URIRef] = OSCAL.LocalDefinitions

    components: Optional[Union[Union[dict, "SystemComponent"], list[Union[dict, "SystemComponent"]]]] = empty_list()
    inventory_items: Optional[Union[Union[dict, "InventoryItem"], list[Union[dict, "InventoryItem"]]]] = empty_list()
    users: Optional[Union[Union[dict, "SystemUser"], list[Union[dict, "SystemUser"]]]] = empty_list()
    objectives_and_methods: Optional[Union[Union[dict, "LocalObjective"], list[Union[dict, "LocalObjective"]]]] = empty_list()
    activities: Optional[Union[Union[dict, "Activity"], list[Union[dict, "Activity"]]]] = empty_list()
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="components", slot_type=SystemComponent, key_name="uuid", keyed=False)

        self._normalize_inlined_as_list(slot_name="inventory_items", slot_type=InventoryItem, key_name="uuid", keyed=False)

        self._normalize_inlined_as_list(slot_name="users", slot_type=SystemUser, key_name="uuid", keyed=False)

        self._normalize_inlined_as_list(slot_name="objectives_and_methods", slot_type=LocalObjective, key_name="control-id", keyed=False)

        self._normalize_inlined_as_list(slot_name="activities", slot_type=Activity, key_name="uuid", keyed=False)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TermsAndConditions(YAMLRoot):
    """
    Used to define various terms and conditions under which an assessment can be performed.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["TermsAndConditions"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:TermsAndConditions"
    class_name: ClassVar[str] = "TermsAndConditions"
    class_model_uri: ClassVar[URIRef] = OSCAL.TermsAndConditions

    parts: Optional[Union[Union[dict, "TermsAndConditionsPart"], list[Union[dict, "TermsAndConditionsPart"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="parts", slot_type=TermsAndConditionsPart, key_name="name", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ReviewedControls(YAMLRoot):
    """
    Identifies the controls being assessed and their control objectives.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["ReviewedControls"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:ReviewedControls"
    class_name: ClassVar[str] = "ReviewedControls"
    class_model_uri: ClassVar[URIRef] = OSCAL.ReviewedControls

    control_selections: Union[Union[dict, "ControlSelection"], list[Union[dict, "ControlSelection"]]] = None
    description: Optional[str] = None
    control_objective_selections: Optional[Union[Union[dict, "ControlObjectiveSelection"], list[Union[dict, "ControlObjectiveSelection"]]]] = empty_list()
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.control_selections):
            self.MissingRequiredField("control_selections")
        if not isinstance(self.control_selections, list):
            self.control_selections = [self.control_selections] if self.control_selections is not None else []
        self.control_selections = [v if isinstance(v, ControlSelection) else ControlSelection(**as_dict(v)) for v in self.control_selections]

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.control_objective_selections, list):
            self.control_objective_selections = [self.control_objective_selections] if self.control_objective_selections is not None else []
        self.control_objective_selections = [v if isinstance(v, ControlObjectiveSelection) else ControlObjectiveSelection(**as_dict(v)) for v in self.control_objective_selections]

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ControlSelection(YAMLRoot):
    """
    Identifies the controls being assessed.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["ControlSelection"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:ControlSelection"
    class_name: ClassVar[str] = "ControlSelection"
    class_model_uri: ClassVar[URIRef] = OSCAL.ControlSelection

    description: Optional[str] = None
    include_all: Optional[Union[dict, IncludeAll]] = None
    include_controls: Optional[Union[Union[dict, "AssessmentSelectControlById"], list[Union[dict, "AssessmentSelectControlById"]]]] = empty_list()
    exclude_controls: Optional[Union[Union[dict, "AssessmentSelectControlById"], list[Union[dict, "AssessmentSelectControlById"]]]] = empty_list()
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.include_all is not None and not isinstance(self.include_all, IncludeAll):
            self.include_all = IncludeAll()

        self._normalize_inlined_as_list(slot_name="include_controls", slot_type=AssessmentSelectControlById, key_name="control-id", keyed=False)

        self._normalize_inlined_as_list(slot_name="exclude_controls", slot_type=AssessmentSelectControlById, key_name="control-id", keyed=False)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ControlObjectiveSelection(YAMLRoot):
    """
    Identifies the control objectives of the assessment.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["ControlObjectiveSelection"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:ControlObjectiveSelection"
    class_name: ClassVar[str] = "ControlObjectiveSelection"
    class_model_uri: ClassVar[URIRef] = OSCAL.ControlObjectiveSelection

    description: Optional[str] = None
    include_all: Optional[Union[dict, IncludeAll]] = None
    include_objectives: Optional[Union[Union[dict, "SelectObjectiveById"], list[Union[dict, "SelectObjectiveById"]]]] = empty_list()
    exclude_objectives: Optional[Union[Union[dict, "SelectObjectiveById"], list[Union[dict, "SelectObjectiveById"]]]] = empty_list()
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.include_all is not None and not isinstance(self.include_all, IncludeAll):
            self.include_all = IncludeAll()

        self._normalize_inlined_as_list(slot_name="include_objectives", slot_type=SelectObjectiveById, key_name="objective-id", keyed=False)

        self._normalize_inlined_as_list(slot_name="exclude_objectives", slot_type=SelectObjectiveById, key_name="objective-id", keyed=False)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AssessmentSelectControlById(YAMLRoot):
    """
    Select a specific control for inclusion/exclusion in the assessment by literal control ID and optional statement
    IDs.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["AssessmentSelectControlById"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:AssessmentSelectControlById"
    class_name: ClassVar[str] = "AssessmentSelectControlById"
    class_model_uri: ClassVar[URIRef] = OSCAL.AssessmentSelectControlById

    control_id: str = None
    statement_ids: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.control_id):
            self.MissingRequiredField("control_id")
        if not isinstance(self.control_id, str):
            self.control_id = str(self.control_id)

        if not isinstance(self.statement_ids, list):
            self.statement_ids = [self.statement_ids] if self.statement_ids is not None else []
        self.statement_ids = [v if isinstance(v, str) else str(v) for v in self.statement_ids]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SelectObjectiveById(YAMLRoot):
    """
    Used to select a control objective for inclusion/exclusion.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["SelectObjectiveById"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:SelectObjectiveById"
    class_name: ClassVar[str] = "SelectObjectiveById"
    class_model_uri: ClassVar[URIRef] = OSCAL.SelectObjectiveById

    objective_id: str = None
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.objective_id):
            self.MissingRequiredField("objective_id")
        if not isinstance(self.objective_id, str):
            self.objective_id = str(self.objective_id)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AssessmentSubject(YAMLRoot):
    """
    Identifies system elements being assessed, such as components, inventory items, and locations.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["AssessmentSubject"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:AssessmentSubject"
    class_name: ClassVar[str] = "AssessmentSubject"
    class_model_uri: ClassVar[URIRef] = OSCAL.AssessmentSubject

    type: str = None
    description: Optional[str] = None
    include_all: Optional[Union[dict, IncludeAll]] = None
    include_subjects: Optional[Union[Union[dict, "SelectSubjectById"], list[Union[dict, "SelectSubjectById"]]]] = empty_list()
    exclude_subjects: Optional[Union[Union[dict, "SelectSubjectById"], list[Union[dict, "SelectSubjectById"]]]] = empty_list()
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.include_all is not None and not isinstance(self.include_all, IncludeAll):
            self.include_all = IncludeAll()

        self._normalize_inlined_as_list(slot_name="include_subjects", slot_type=SelectSubjectById, key_name="subject-uuid", keyed=False)

        self._normalize_inlined_as_list(slot_name="exclude_subjects", slot_type=SelectSubjectById, key_name="subject-uuid", keyed=False)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SelectSubjectById(YAMLRoot):
    """
    Identifies a set of assessment subjects to include/exclude by UUID.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["SelectSubjectById"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:SelectSubjectById"
    class_name: ClassVar[str] = "SelectSubjectById"
    class_model_uri: ClassVar[URIRef] = OSCAL.SelectSubjectById

    subject_uuid: str = None
    type: str = None
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.subject_uuid):
            self.MissingRequiredField("subject_uuid")
        if not isinstance(self.subject_uuid, str):
            self.subject_uuid = str(self.subject_uuid)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SubjectReference(YAMLRoot):
    """
    A human-oriented identifier reference to a resource. Use type to indicate whether the identified resource is a
    component, inventory item, location, user, or something else.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["SubjectReference"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:SubjectReference"
    class_name: ClassVar[str] = "SubjectReference"
    class_model_uri: ClassVar[URIRef] = OSCAL.SubjectReference

    subject_uuid: str = None
    type: str = None
    title: Optional[str] = None
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.subject_uuid):
            self.MissingRequiredField("subject_uuid")
        if not isinstance(self.subject_uuid, str):
            self.subject_uuid = str(self.subject_uuid)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AssessmentSubjectPlaceholder(YAMLRoot):
    """
    Used when the assessment subjects will be determined as part of one or more other assessment activities.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["AssessmentSubjectPlaceholder"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:AssessmentSubjectPlaceholder"
    class_name: ClassVar[str] = "AssessmentSubjectPlaceholder"
    class_model_uri: ClassVar[URIRef] = OSCAL.AssessmentSubjectPlaceholder

    uuid: str = None
    sources: Union[Union[dict, "AssessmentSubjectSource"], list[Union[dict, "AssessmentSubjectSource"]]] = None
    description: Optional[str] = None
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uuid):
            self.MissingRequiredField("uuid")
        if not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        if self._is_empty(self.sources):
            self.MissingRequiredField("sources")
        self._normalize_inlined_as_list(slot_name="sources", slot_type=AssessmentSubjectSource, key_name="task-uuid", keyed=False)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AssessmentSubjectSource(YAMLRoot):
    """
    Assessment subjects will be identified while conducting the referenced activity.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["AssessmentSubjectSource"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:AssessmentSubjectSource"
    class_name: ClassVar[str] = "AssessmentSubjectSource"
    class_model_uri: ClassVar[URIRef] = OSCAL.AssessmentSubjectSource

    task_uuid: str = None
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.task_uuid):
            self.MissingRequiredField("task_uuid")
        if not isinstance(self.task_uuid, str):
            self.task_uuid = str(self.task_uuid)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AssessmentAssets(YAMLRoot):
    """
    Identifies the assets used to perform this assessment.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["AssessmentAssets"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:AssessmentAssets"
    class_name: ClassVar[str] = "AssessmentAssets"
    class_model_uri: ClassVar[URIRef] = OSCAL.AssessmentAssets

    assessment_platforms: Union[Union[dict, "AssessmentPlatform"], list[Union[dict, "AssessmentPlatform"]]] = None
    components: Optional[Union[Union[dict, "SystemComponent"], list[Union[dict, "SystemComponent"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.assessment_platforms):
            self.MissingRequiredField("assessment_platforms")
        self._normalize_inlined_as_list(slot_name="assessment_platforms", slot_type=AssessmentPlatform, key_name="uuid", keyed=False)

        self._normalize_inlined_as_list(slot_name="components", slot_type=SystemComponent, key_name="uuid", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AssessmentPlatform(YAMLRoot):
    """
    Used to represent the toolset used to perform aspects of the assessment.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["AssessmentPlatform"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:AssessmentPlatform"
    class_name: ClassVar[str] = "AssessmentPlatform"
    class_model_uri: ClassVar[URIRef] = OSCAL.AssessmentPlatform

    uuid: str = None
    title: Optional[str] = None
    uses_components: Optional[Union[Union[dict, "UsesComponent"], list[Union[dict, "UsesComponent"]]]] = empty_list()
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uuid):
            self.MissingRequiredField("uuid")
        if not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        self._normalize_inlined_as_list(slot_name="uses_components", slot_type=UsesComponent, key_name="component-uuid", keyed=False)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class UsesComponent(YAMLRoot):
    """
    The set of components that are used by the assessment platform.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["UsesComponent"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:UsesComponent"
    class_name: ClassVar[str] = "UsesComponent"
    class_model_uri: ClassVar[URIRef] = OSCAL.UsesComponent

    component_uuid: str = None
    remarks: Optional[str] = None
    responsible_parties: Optional[Union[Union[dict, ResponsibleParty], list[Union[dict, ResponsibleParty]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.component_uuid):
            self.MissingRequiredField("component_uuid")
        if not isinstance(self.component_uuid, str):
            self.component_uuid = str(self.component_uuid)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        self._normalize_inlined_as_list(slot_name="responsible_parties", slot_type=ResponsibleParty, key_name="role-id", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LocalObjective(YAMLRoot):
    """
    A local definition of a control objective for this assessment. Uses catalog syntax for control objective and
    assessment actions.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["LocalObjective"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:LocalObjective"
    class_name: ClassVar[str] = "LocalObjective"
    class_model_uri: ClassVar[URIRef] = OSCAL.LocalObjective

    control_id: str = None
    parts: Union[Union[dict, "ControlPart"], list[Union[dict, "ControlPart"]]] = None
    description: Optional[str] = None
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.control_id):
            self.MissingRequiredField("control_id")
        if not isinstance(self.control_id, str):
            self.control_id = str(self.control_id)

        if self._is_empty(self.parts):
            self.MissingRequiredField("parts")
        self._normalize_inlined_as_list(slot_name="parts", slot_type=ControlPart, key_name="name", keyed=False)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AssessmentMethod(YAMLRoot):
    """
    A local definition of a control objective.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["AssessmentMethod"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:AssessmentMethod"
    class_name: ClassVar[str] = "AssessmentMethod"
    class_model_uri: ClassVar[URIRef] = OSCAL.AssessmentMethod

    uuid: str = None
    part: Union[dict, "AssessmentPart"] = None
    description: Optional[str] = None
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uuid):
            self.MissingRequiredField("uuid")
        if not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        if self._is_empty(self.part):
            self.MissingRequiredField("part")
        if not isinstance(self.part, AssessmentPart):
            self.part = AssessmentPart(**as_dict(self.part))

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Activity(YAMLRoot):
    """
    Identifies an assessment or related process that can be performed. In the assessment plan, this is an intended
    activity.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["Activity"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:Activity"
    class_name: ClassVar[str] = "Activity"
    class_model_uri: ClassVar[URIRef] = OSCAL.Activity

    uuid: str = None
    description: str = None
    title: Optional[str] = None
    steps: Optional[Union[Union[dict, "Step"], list[Union[dict, "Step"]]]] = empty_list()
    related_controls: Optional[Union[dict, ReviewedControls]] = None
    remarks: Optional[str] = None
    responsible_roles: Optional[Union[Union[dict, ResponsibleRole], list[Union[dict, ResponsibleRole]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uuid):
            self.MissingRequiredField("uuid")
        if not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        self._normalize_inlined_as_list(slot_name="steps", slot_type=Step, key_name="uuid", keyed=False)

        if self.related_controls is not None and not isinstance(self.related_controls, ReviewedControls):
            self.related_controls = ReviewedControls(**as_dict(self.related_controls))

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        self._normalize_inlined_as_list(slot_name="responsible_roles", slot_type=ResponsibleRole, key_name="role-id", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Step(YAMLRoot):
    """
    Identifies an individual step in a series of steps related to an activity, such as an assessment test or
    examination procedure.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["Step"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:Step"
    class_name: ClassVar[str] = "Step"
    class_model_uri: ClassVar[URIRef] = OSCAL.Step

    uuid: str = None
    description: str = None
    title: Optional[str] = None
    reviewed_controls: Optional[Union[dict, ReviewedControls]] = None
    remarks: Optional[str] = None
    responsible_roles: Optional[Union[Union[dict, ResponsibleRole], list[Union[dict, ResponsibleRole]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uuid):
            self.MissingRequiredField("uuid")
        if not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.reviewed_controls is not None and not isinstance(self.reviewed_controls, ReviewedControls):
            self.reviewed_controls = ReviewedControls(**as_dict(self.reviewed_controls))

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        self._normalize_inlined_as_list(slot_name="responsible_roles", slot_type=ResponsibleRole, key_name="role-id", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Task(YAMLRoot):
    """
    Represents a scheduled event or milestone, which may be associated with a series of assessment actions.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["Task"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:Task"
    class_name: ClassVar[str] = "Task"
    class_model_uri: ClassVar[URIRef] = OSCAL.Task

    uuid: str = None
    type: str = None
    title: str = None
    description: Optional[str] = None
    timing: Optional[Union[dict, "EventTiming"]] = None
    dependencies: Optional[Union[Union[dict, "TaskDependency"], list[Union[dict, "TaskDependency"]]]] = empty_list()
    associated_activities: Optional[Union[Union[dict, "AssociatedActivity"], list[Union[dict, "AssociatedActivity"]]]] = empty_list()
    tasks: Optional[Union[Union[dict, "Task"], list[Union[dict, "Task"]]]] = empty_list()
    subjects: Optional[Union[Union[dict, AssessmentSubject], list[Union[dict, AssessmentSubject]]]] = empty_list()
    remarks: Optional[str] = None
    responsible_roles: Optional[Union[Union[dict, ResponsibleRole], list[Union[dict, ResponsibleRole]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uuid):
            self.MissingRequiredField("uuid")
        if not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.timing is not None and not isinstance(self.timing, EventTiming):
            self.timing = EventTiming(**as_dict(self.timing))

        self._normalize_inlined_as_list(slot_name="dependencies", slot_type=TaskDependency, key_name="task-uuid", keyed=False)

        self._normalize_inlined_as_list(slot_name="associated_activities", slot_type=AssociatedActivity, key_name="activity-uuid", keyed=False)

        self._normalize_inlined_as_list(slot_name="tasks", slot_type=Task, key_name="uuid", keyed=False)

        self._normalize_inlined_as_list(slot_name="subjects", slot_type=AssessmentSubject, key_name="type", keyed=False)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        self._normalize_inlined_as_list(slot_name="responsible_roles", slot_type=ResponsibleRole, key_name="role-id", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EventTiming(YAMLRoot):
    """
    The timing under which the task is intended to occur.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["EventTiming"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:EventTiming"
    class_name: ClassVar[str] = "EventTiming"
    class_model_uri: ClassVar[URIRef] = OSCAL.EventTiming

    on_date: Optional[Union[dict, "OnDateCondition"]] = None
    within_date_range: Optional[Union[dict, "WithinDateRange"]] = None
    at_frequency: Optional[Union[dict, "AtFrequency"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.on_date is not None and not isinstance(self.on_date, OnDateCondition):
            self.on_date = OnDateCondition(**as_dict(self.on_date))

        if self.within_date_range is not None and not isinstance(self.within_date_range, WithinDateRange):
            self.within_date_range = WithinDateRange(**as_dict(self.within_date_range))

        if self.at_frequency is not None and not isinstance(self.at_frequency, AtFrequency):
            self.at_frequency = AtFrequency(**as_dict(self.at_frequency))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OnDateCondition(YAMLRoot):
    """
    The task is intended to occur on the specified date.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["OnDateCondition"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:OnDateCondition"
    class_name: ClassVar[str] = "OnDateCondition"
    class_model_uri: ClassVar[URIRef] = OSCAL.OnDateCondition

    date: str = None
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.date):
            self.MissingRequiredField("date")
        if not isinstance(self.date, str):
            self.date = str(self.date)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class WithinDateRange(YAMLRoot):
    """
    The task is intended to occur within the specified date range.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["WithinDateRange"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:WithinDateRange"
    class_name: ClassVar[str] = "WithinDateRange"
    class_model_uri: ClassVar[URIRef] = OSCAL.WithinDateRange

    start: str = None
    end: str = None
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.start):
            self.MissingRequiredField("start")
        if not isinstance(self.start, str):
            self.start = str(self.start)

        if self._is_empty(self.end):
            self.MissingRequiredField("end")
        if not isinstance(self.end, str):
            self.end = str(self.end)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AtFrequency(YAMLRoot):
    """
    The task is intended to occur at the specified frequency.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["AtFrequency"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:AtFrequency"
    class_name: ClassVar[str] = "AtFrequency"
    class_model_uri: ClassVar[URIRef] = OSCAL.AtFrequency

    period: int = None
    unit: Union[str, "TimingUnitEnum"] = None
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.period):
            self.MissingRequiredField("period")
        if not isinstance(self.period, int):
            self.period = int(self.period)

        if self._is_empty(self.unit):
            self.MissingRequiredField("unit")
        if not isinstance(self.unit, TimingUnitEnum):
            self.unit = TimingUnitEnum(self.unit)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TaskDependency(YAMLRoot):
    """
    Used to indicate that a task is dependent on another task.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["TaskDependency"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:TaskDependency"
    class_name: ClassVar[str] = "TaskDependency"
    class_model_uri: ClassVar[URIRef] = OSCAL.TaskDependency

    task_uuid: str = None
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.task_uuid):
            self.MissingRequiredField("task_uuid")
        if not isinstance(self.task_uuid, str):
            self.task_uuid = str(self.task_uuid)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AssociatedActivity(YAMLRoot):
    """
    Identifies an individual activity to be performed as part of a task.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["AssociatedActivity"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:AssociatedActivity"
    class_name: ClassVar[str] = "AssociatedActivity"
    class_model_uri: ClassVar[URIRef] = OSCAL.AssociatedActivity

    activity_uuid: str = None
    subjects: Union[Union[dict, AssessmentSubject], list[Union[dict, AssessmentSubject]]] = None
    remarks: Optional[str] = None
    responsible_roles: Optional[Union[Union[dict, ResponsibleRole], list[Union[dict, ResponsibleRole]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.activity_uuid):
            self.MissingRequiredField("activity_uuid")
        if not isinstance(self.activity_uuid, str):
            self.activity_uuid = str(self.activity_uuid)

        if self._is_empty(self.subjects):
            self.MissingRequiredField("subjects")
        self._normalize_inlined_as_list(slot_name="subjects", slot_type=AssessmentSubject, key_name="type", keyed=False)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        self._normalize_inlined_as_list(slot_name="responsible_roles", slot_type=ResponsibleRole, key_name="role-id", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AssessmentPart(YAMLRoot):
    """
    A partition of an assessment plan or results or a child of another part.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["AssessmentPart"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:AssessmentPart"
    class_name: ClassVar[str] = "AssessmentPart"
    class_model_uri: ClassVar[URIRef] = OSCAL.AssessmentPart

    name: str = None
    uuid: Optional[str] = None
    ns: Optional[str] = None
    _class: Optional[str] = None
    title: Optional[str] = None
    prose: Optional[str] = None
    parts: Optional[Union[Union[dict, "AssessmentPart"], list[Union[dict, "AssessmentPart"]]]] = empty_list()
    props: Optional[Union[Union[dict, Property], list[Union[dict, Property]]]] = empty_list()
    links: Optional[Union[Union[dict, Link], list[Union[dict, Link]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.uuid is not None and not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        if self.ns is not None and not isinstance(self.ns, str):
            self.ns = str(self.ns)

        if self._class is not None and not isinstance(self._class, str):
            self._class = str(self._class)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.prose is not None and not isinstance(self.prose, str):
            self.prose = str(self.prose)

        self._normalize_inlined_as_list(slot_name="parts", slot_type=AssessmentPart, key_name="name", keyed=False)

        self._normalize_inlined_as_list(slot_name="props", slot_type=Property, key_name="name", keyed=False)

        self._normalize_inlined_as_list(slot_name="links", slot_type=Link, key_name="href", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TermsAndConditionsPart(AssessmentPart):
    """
    A terms-and-conditions scoped assessment part.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["TermsAndConditionsPart"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:TermsAndConditionsPart"
    class_name: ClassVar[str] = "TermsAndConditionsPart"
    class_model_uri: ClassVar[URIRef] = OSCAL.TermsAndConditionsPart

    name: Union[str, "TermsAndConditionsPartNameEnum"] = None
    parts: Optional[Union[Union[dict, "TermsAndConditionsPart"], list[Union[dict, "TermsAndConditionsPart"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, TermsAndConditionsPartNameEnum):
            self.name = TermsAndConditionsPartNameEnum(self.name)

        self._normalize_inlined_as_list(slot_name="parts", slot_type=TermsAndConditionsPart, key_name="name", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ControlPart(YAMLRoot):
    """
    An annotated, markup-based textual element of a control's or catalog group's definition, or a child of another
    part.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["ControlPart"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:ControlPart"
    class_name: ClassVar[str] = "ControlPart"
    class_model_uri: ClassVar[URIRef] = OSCAL.ControlPart

    name: str = None
    id: Optional[str] = None
    ns: Optional[str] = None
    _class: Optional[str] = None
    title: Optional[str] = None
    prose: Optional[str] = None
    parts: Optional[Union[Union[dict, "ControlPart"], list[Union[dict, "ControlPart"]]]] = empty_list()
    props: Optional[Union[Union[dict, Property], list[Union[dict, Property]]]] = empty_list()
    links: Optional[Union[Union[dict, Link], list[Union[dict, Link]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.id is not None and not isinstance(self.id, str):
            self.id = str(self.id)

        if self.ns is not None and not isinstance(self.ns, str):
            self.ns = str(self.ns)

        if self._class is not None and not isinstance(self._class, str):
            self._class = str(self._class)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.prose is not None and not isinstance(self.prose, str):
            self.prose = str(self.prose)

        self._normalize_inlined_as_list(slot_name="parts", slot_type=ControlPart, key_name="name", keyed=False)

        self._normalize_inlined_as_list(slot_name="props", slot_type=Property, key_name="name", keyed=False)

        self._normalize_inlined_as_list(slot_name="links", slot_type=Link, key_name="href", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SetParameter(YAMLRoot):
    """
    Identifies the parameter that will be set by the enclosed value.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["SetParameter"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:SetParameter"
    class_name: ClassVar[str] = "SetParameter"
    class_model_uri: ClassVar[URIRef] = OSCAL.SetParameter

    param_id: str = None
    values: Union[str, list[str]] = None
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.param_id):
            self.MissingRequiredField("param_id")
        if not isinstance(self.param_id, str):
            self.param_id = str(self.param_id)

        if self._is_empty(self.values):
            self.MissingRequiredField("values")
        if not isinstance(self.values, list):
            self.values = [self.values] if self.values is not None else []
        self.values = [v if isinstance(v, str) else str(v) for v in self.values]

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SystemComponent(YAMLRoot):
    """
    A defined component that can be part of an implemented system.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["SystemComponent"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:SystemComponent"
    class_name: ClassVar[str] = "SystemComponent"
    class_model_uri: ClassVar[URIRef] = OSCAL.SystemComponent

    uuid: str = None
    type: str = None
    title: str = None
    description: str = None
    status: Union[dict, "ComponentStatus"] = None
    purpose: Optional[str] = None
    protocols: Optional[Union[Union[dict, "Protocol"], list[Union[dict, "Protocol"]]]] = empty_list()
    props: Optional[Union[Union[dict, "ImplementationCommonProperty"], list[Union[dict, "ImplementationCommonProperty"]]]] = empty_list()
    links: Optional[Union[Union[dict, "ImplementationCommonLink"], list[Union[dict, "ImplementationCommonLink"]]]] = empty_list()
    responsible_roles: Optional[Union[Union[dict, "ImplementationResponsibleRole"], list[Union[dict, "ImplementationResponsibleRole"]]]] = empty_list()
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uuid):
            self.MissingRequiredField("uuid")
        if not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self._is_empty(self.status):
            self.MissingRequiredField("status")
        if not isinstance(self.status, ComponentStatus):
            self.status = ComponentStatus(**as_dict(self.status))

        if self.purpose is not None and not isinstance(self.purpose, str):
            self.purpose = str(self.purpose)

        if not isinstance(self.protocols, list):
            self.protocols = [self.protocols] if self.protocols is not None else []
        self.protocols = [v if isinstance(v, Protocol) else Protocol(**as_dict(v)) for v in self.protocols]

        self._normalize_inlined_as_list(slot_name="props", slot_type=ImplementationCommonProperty, key_name="name", keyed=False)

        self._normalize_inlined_as_list(slot_name="links", slot_type=ImplementationCommonLink, key_name="href", keyed=False)

        self._normalize_inlined_as_list(slot_name="responsible_roles", slot_type=ImplementationResponsibleRole, key_name="role-id", keyed=False)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SspSystemComponent(SystemComponent):
    """
    SSP-scoped system component with allows-authenticated-scan property typing.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_SSP["SspSystemComponent"]
    class_class_curie: ClassVar[str] = "oscal_ssp:SspSystemComponent"
    class_name: ClassVar[str] = "SspSystemComponent"
    class_model_uri: ClassVar[URIRef] = OSCAL.SspSystemComponent

    uuid: str = None
    type: str = None
    title: str = None
    description: str = None
    status: Union[dict, "ComponentStatus"] = None
    props: Optional[Union[Union[dict, SspAllowsAuthenticatedScanProp], list[Union[dict, SspAllowsAuthenticatedScanProp]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="props", slot_type=SspAllowsAuthenticatedScanProp, key_name="name", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ComponentStatus(YAMLRoot):
    """
    Describes the operational status of the system component.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["ComponentStatus"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:ComponentStatus"
    class_name: ClassVar[str] = "ComponentStatus"
    class_model_uri: ClassVar[URIRef] = OSCAL.ComponentStatus

    state: Union[str, "ComponentStateEnum"] = None
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.state):
            self.MissingRequiredField("state")
        if not isinstance(self.state, ComponentStateEnum):
            self.state = ComponentStateEnum(self.state)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Protocol(YAMLRoot):
    """
    Information about the protocol used to provide a service.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["Protocol"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:Protocol"
    class_name: ClassVar[str] = "Protocol"
    class_model_uri: ClassVar[URIRef] = OSCAL.Protocol

    uuid: Optional[str] = None
    name: Optional[str] = None
    title: Optional[str] = None
    port_ranges: Optional[Union[Union[dict, "PortRange"], list[Union[dict, "PortRange"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.uuid is not None and not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.port_ranges, list):
            self.port_ranges = [self.port_ranges] if self.port_ranges is not None else []
        self.port_ranges = [v if isinstance(v, PortRange) else PortRange(**as_dict(v)) for v in self.port_ranges]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PortRange(YAMLRoot):
    """
    Where applicable, the transport layer protocol port range.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["PortRange"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:PortRange"
    class_name: ClassVar[str] = "PortRange"
    class_model_uri: ClassVar[URIRef] = OSCAL.PortRange

    start: Optional[int] = None
    end: Optional[int] = None
    transport: Optional[Union[str, "TransportEnum"]] = None
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.start is not None and not isinstance(self.start, int):
            self.start = int(self.start)

        if self.end is not None and not isinstance(self.end, int):
            self.end = int(self.end)

        if self.transport is not None and not isinstance(self.transport, TransportEnum):
            self.transport = TransportEnum(self.transport)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ImplementationStatus(YAMLRoot):
    """
    Indicates the degree to which a given control is implemented.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["ImplementationStatus"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:ImplementationStatus"
    class_name: ClassVar[str] = "ImplementationStatus"
    class_model_uri: ClassVar[URIRef] = OSCAL.ImplementationStatus

    state: str = None
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.state):
            self.MissingRequiredField("state")
        if not isinstance(self.state, str):
            self.state = str(self.state)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SystemUser(YAMLRoot):
    """
    A type of user that interacts with the system based on an associated role.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["SystemUser"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:SystemUser"
    class_name: ClassVar[str] = "SystemUser"
    class_model_uri: ClassVar[URIRef] = OSCAL.SystemUser

    uuid: str = None
    title: Optional[str] = None
    short_name: Optional[str] = None
    description: Optional[str] = None
    role_ids: Optional[Union[str, list[str]]] = empty_list()
    authorized_privileges: Optional[Union[Union[dict, "AuthorizedPrivilege"], list[Union[dict, "AuthorizedPrivilege"]]]] = empty_list()
    props: Optional[Union[Union[dict, "ImplementationCommonProperty"], list[Union[dict, "ImplementationCommonProperty"]]]] = empty_list()
    links: Optional[Union[Union[dict, "ImplementationCommonLink"], list[Union[dict, "ImplementationCommonLink"]]]] = empty_list()
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uuid):
            self.MissingRequiredField("uuid")
        if not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.short_name is not None and not isinstance(self.short_name, str):
            self.short_name = str(self.short_name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.role_ids, list):
            self.role_ids = [self.role_ids] if self.role_ids is not None else []
        self.role_ids = [v if isinstance(v, str) else str(v) for v in self.role_ids]

        self._normalize_inlined_as_list(slot_name="authorized_privileges", slot_type=AuthorizedPrivilege, key_name="title", keyed=False)

        self._normalize_inlined_as_list(slot_name="props", slot_type=ImplementationCommonProperty, key_name="name", keyed=False)

        self._normalize_inlined_as_list(slot_name="links", slot_type=ImplementationCommonLink, key_name="href", keyed=False)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AuthorizedPrivilege(YAMLRoot):
    """
    Identifies a specific system privilege held by the user, along with an associated description and/or rationale for
    the privilege.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["AuthorizedPrivilege"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:AuthorizedPrivilege"
    class_name: ClassVar[str] = "AuthorizedPrivilege"
    class_model_uri: ClassVar[URIRef] = OSCAL.AuthorizedPrivilege

    title: str = None
    functions_performed: Union[str, list[str]] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self._is_empty(self.functions_performed):
            self.MissingRequiredField("functions_performed")
        if not isinstance(self.functions_performed, list):
            self.functions_performed = [self.functions_performed] if self.functions_performed is not None else []
        self.functions_performed = [v if isinstance(v, str) else str(v) for v in self.functions_performed]

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InventoryItem(YAMLRoot):
    """
    A single managed inventory item within the system.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["InventoryItem"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:InventoryItem"
    class_name: ClassVar[str] = "InventoryItem"
    class_model_uri: ClassVar[URIRef] = OSCAL.InventoryItem

    uuid: str = None
    description: str = None
    implemented_components: Optional[Union[Union[dict, "ImplementedComponent"], list[Union[dict, "ImplementedComponent"]]]] = empty_list()
    props: Optional[Union[Union[dict, "ImplementationCommonProperty"], list[Union[dict, "ImplementationCommonProperty"]]]] = empty_list()
    links: Optional[Union[Union[dict, "ImplementationCommonLink"], list[Union[dict, "ImplementationCommonLink"]]]] = empty_list()
    responsible_parties: Optional[Union[Union[dict, "ImplementationResponsibleParty"], list[Union[dict, "ImplementationResponsibleParty"]]]] = empty_list()
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uuid):
            self.MissingRequiredField("uuid")
        if not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_list(slot_name="implemented_components", slot_type=ImplementedComponent, key_name="component-uuid", keyed=False)

        self._normalize_inlined_as_list(slot_name="props", slot_type=ImplementationCommonProperty, key_name="name", keyed=False)

        self._normalize_inlined_as_list(slot_name="links", slot_type=ImplementationCommonLink, key_name="href", keyed=False)

        self._normalize_inlined_as_list(slot_name="responsible_parties", slot_type=ImplementationResponsibleParty, key_name="party-uuids", keyed=False)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SspInventoryItem(InventoryItem):
    """
    SSP-scoped inventory item with allows-authenticated-scan property typing.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_SSP["SspInventoryItem"]
    class_class_curie: ClassVar[str] = "oscal_ssp:SspInventoryItem"
    class_name: ClassVar[str] = "SspInventoryItem"
    class_model_uri: ClassVar[URIRef] = OSCAL.SspInventoryItem

    uuid: str = None
    description: str = None
    props: Optional[Union[Union[dict, SspAllowsAuthenticatedScanProp], list[Union[dict, SspAllowsAuthenticatedScanProp]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="props", slot_type=SspAllowsAuthenticatedScanProp, key_name="name", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ImplementedComponent(YAMLRoot):
    """
    The set of components that are implemented in a given system inventory item.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["ImplementedComponent"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:ImplementedComponent"
    class_name: ClassVar[str] = "ImplementedComponent"
    class_model_uri: ClassVar[URIRef] = OSCAL.ImplementedComponent

    component_uuid: str = None
    props: Optional[Union[Union[dict, "ImplementationCommonProperty"], list[Union[dict, "ImplementationCommonProperty"]]]] = empty_list()
    links: Optional[Union[Union[dict, "ImplementationCommonLink"], list[Union[dict, "ImplementationCommonLink"]]]] = empty_list()
    responsible_parties: Optional[Union[Union[dict, "ImplementationResponsibleParty"], list[Union[dict, "ImplementationResponsibleParty"]]]] = empty_list()
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.component_uuid):
            self.MissingRequiredField("component_uuid")
        if not isinstance(self.component_uuid, str):
            self.component_uuid = str(self.component_uuid)

        self._normalize_inlined_as_list(slot_name="props", slot_type=ImplementationCommonProperty, key_name="name", keyed=False)

        self._normalize_inlined_as_list(slot_name="links", slot_type=ImplementationCommonLink, key_name="href", keyed=False)

        self._normalize_inlined_as_list(slot_name="responsible_parties", slot_type=ImplementationResponsibleParty, key_name="party-uuids", keyed=False)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SystemId(YAMLRoot):
    """
    A human-oriented, globally unique identifier for a system.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["SystemId"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:SystemId"
    class_name: ClassVar[str] = "SystemId"
    class_model_uri: ClassVar[URIRef] = OSCAL.SystemId

    id: str = None
    identifier_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self.identifier_type is not None and not isinstance(self.identifier_type, str):
            self.identifier_type = str(self.identifier_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ImplementationCommonProperty(Property):
    """
    Implementation-common scoped OSCAL property.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["ImplementationCommonProperty"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:ImplementationCommonProperty"
    class_name: ClassVar[str] = "ImplementationCommonProperty"
    class_model_uri: ClassVar[URIRef] = OSCAL.ImplementationCommonProperty

    name: Union[str, "ImplementationPropNameEnum"] = None
    value: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, ImplementationPropNameEnum):
            self.name = ImplementationPropNameEnum(self.name)

        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, str):
            self.value = str(self.value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ImplementationCommonLink(Link):
    """
    Implementation-common scoped OSCAL link.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["ImplementationCommonLink"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:ImplementationCommonLink"
    class_name: ClassVar[str] = "ImplementationCommonLink"
    class_model_uri: ClassVar[URIRef] = OSCAL.ImplementationCommonLink

    href: str = None
    rel: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.rel is not None and not isinstance(self.rel, str):
            self.rel = str(self.rel)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ImplementationResponsibleRole(ResponsibleRole):
    """
    Implementation-common scoped responsible role.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["ImplementationResponsibleRole"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:ImplementationResponsibleRole"
    class_name: ClassVar[str] = "ImplementationResponsibleRole"
    class_model_uri: ClassVar[URIRef] = OSCAL.ImplementationResponsibleRole

    role_id: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.role_id):
            self.MissingRequiredField("role_id")
        if not isinstance(self.role_id, str):
            self.role_id = str(self.role_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ImplementationResponsibleParty(ResponsibleParty):
    """
    Implementation-common scoped responsible party.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["ImplementationResponsibleParty"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:ImplementationResponsibleParty"
    class_name: ClassVar[str] = "ImplementationResponsibleParty"
    class_model_uri: ClassVar[URIRef] = OSCAL.ImplementationResponsibleParty

    party_uuids: Union[str, list[str]] = None
    role_id: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.role_id):
            self.MissingRequiredField("role_id")
        if not isinstance(self.role_id, str):
            self.role_id = str(self.role_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Origin(YAMLRoot):
    """
    Identifies the source of the finding, such as a tool, interviewed person, or activity.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["Origin"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:Origin"
    class_name: ClassVar[str] = "Origin"
    class_model_uri: ClassVar[URIRef] = OSCAL.Origin

    actors: Union[Union[dict, "OriginActor"], list[Union[dict, "OriginActor"]]] = None
    related_tasks: Optional[Union[Union[dict, "RelatedTask"], list[Union[dict, "RelatedTask"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.actors):
            self.MissingRequiredField("actors")
        self._normalize_inlined_as_list(slot_name="actors", slot_type=OriginActor, key_name="type", keyed=False)

        self._normalize_inlined_as_list(slot_name="related_tasks", slot_type=RelatedTask, key_name="task-uuid", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OriginActor(YAMLRoot):
    """
    The actor that produces an observation, a finding, or a risk.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["OriginActor"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:OriginActor"
    class_name: ClassVar[str] = "OriginActor"
    class_model_uri: ClassVar[URIRef] = OSCAL.OriginActor

    type: Union[str, "OriginActorTypeEnum"] = None
    actor_uuid: str = None
    role_id: Optional[str] = None
    props: Optional[Union[Union[dict, Property], list[Union[dict, Property]]]] = empty_list()
    links: Optional[Union[Union[dict, Link], list[Union[dict, Link]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, OriginActorTypeEnum):
            self.type = OriginActorTypeEnum(self.type)

        if self._is_empty(self.actor_uuid):
            self.MissingRequiredField("actor_uuid")
        if not isinstance(self.actor_uuid, str):
            self.actor_uuid = str(self.actor_uuid)

        if self.role_id is not None and not isinstance(self.role_id, str):
            self.role_id = str(self.role_id)

        self._normalize_inlined_as_list(slot_name="props", slot_type=Property, key_name="name", keyed=False)

        self._normalize_inlined_as_list(slot_name="links", slot_type=Link, key_name="href", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RelatedTask(YAMLRoot):
    """
    Identifies an individual task for which the containing object is a consequence of.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["RelatedTask"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:RelatedTask"
    class_name: ClassVar[str] = "RelatedTask"
    class_model_uri: ClassVar[URIRef] = OSCAL.RelatedTask

    task_uuid: str = None
    subjects: Optional[Union[Union[dict, AssessmentSubject], list[Union[dict, AssessmentSubject]]]] = empty_list()
    identified_subject: Optional[Union[dict, "IdentifiedSubject"]] = None
    remarks: Optional[str] = None
    responsible_parties: Optional[Union[Union[dict, ResponsibleParty], list[Union[dict, ResponsibleParty]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.task_uuid):
            self.MissingRequiredField("task_uuid")
        if not isinstance(self.task_uuid, str):
            self.task_uuid = str(self.task_uuid)

        self._normalize_inlined_as_list(slot_name="subjects", slot_type=AssessmentSubject, key_name="type", keyed=False)

        if self.identified_subject is not None and not isinstance(self.identified_subject, IdentifiedSubject):
            self.identified_subject = IdentifiedSubject(**as_dict(self.identified_subject))

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        self._normalize_inlined_as_list(slot_name="responsible_parties", slot_type=ResponsibleParty, key_name="role-id", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IdentifiedSubject(YAMLRoot):
    """
    Used to detail assessment subjects that were identified by this task.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["IdentifiedSubject"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:IdentifiedSubject"
    class_name: ClassVar[str] = "IdentifiedSubject"
    class_model_uri: ClassVar[URIRef] = OSCAL.IdentifiedSubject

    subject_placeholder_uuid: str = None
    subjects: Union[Union[dict, AssessmentSubject], list[Union[dict, AssessmentSubject]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.subject_placeholder_uuid):
            self.MissingRequiredField("subject_placeholder_uuid")
        if not isinstance(self.subject_placeholder_uuid, str):
            self.subject_placeholder_uuid = str(self.subject_placeholder_uuid)

        if self._is_empty(self.subjects):
            self.MissingRequiredField("subjects")
        self._normalize_inlined_as_list(slot_name="subjects", slot_type=AssessmentSubject, key_name="type", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Observation(YAMLRoot):
    """
    Describes an individual observation.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["Observation"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:Observation"
    class_name: ClassVar[str] = "Observation"
    class_model_uri: ClassVar[URIRef] = OSCAL.Observation

    uuid: str = None
    description: str = None
    methods: Union[str, list[str]] = None
    collected: str = None
    title: Optional[str] = None
    types: Optional[Union[str, list[str]]] = empty_list()
    origins: Optional[Union[Union[dict, Origin], list[Union[dict, Origin]]]] = empty_list()
    subjects: Optional[Union[Union[dict, SubjectReference], list[Union[dict, SubjectReference]]]] = empty_list()
    relevant_evidence: Optional[Union[Union[dict, "RelevantEvidence"], list[Union[dict, "RelevantEvidence"]]]] = empty_list()
    expires: Optional[str] = None
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uuid):
            self.MissingRequiredField("uuid")
        if not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self._is_empty(self.methods):
            self.MissingRequiredField("methods")
        if not isinstance(self.methods, list):
            self.methods = [self.methods] if self.methods is not None else []
        self.methods = [v if isinstance(v, str) else str(v) for v in self.methods]

        if self._is_empty(self.collected):
            self.MissingRequiredField("collected")
        if not isinstance(self.collected, str):
            self.collected = str(self.collected)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.types, list):
            self.types = [self.types] if self.types is not None else []
        self.types = [v if isinstance(v, str) else str(v) for v in self.types]

        if not isinstance(self.origins, list):
            self.origins = [self.origins] if self.origins is not None else []
        self.origins = [v if isinstance(v, Origin) else Origin(**as_dict(v)) for v in self.origins]

        self._normalize_inlined_as_list(slot_name="subjects", slot_type=SubjectReference, key_name="subject-uuid", keyed=False)

        self._normalize_inlined_as_list(slot_name="relevant_evidence", slot_type=RelevantEvidence, key_name="description", keyed=False)

        if self.expires is not None and not isinstance(self.expires, str):
            self.expires = str(self.expires)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RelevantEvidence(YAMLRoot):
    """
    Links this observation to relevant evidence.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["RelevantEvidence"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:RelevantEvidence"
    class_name: ClassVar[str] = "RelevantEvidence"
    class_model_uri: ClassVar[URIRef] = OSCAL.RelevantEvidence

    description: str = None
    href: Optional[str] = None
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self.href is not None and not isinstance(self.href, str):
            self.href = str(self.href)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Finding(YAMLRoot):
    """
    Describes an individual finding.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["Finding"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:Finding"
    class_name: ClassVar[str] = "Finding"
    class_model_uri: ClassVar[URIRef] = OSCAL.Finding

    uuid: str = None
    title: str = None
    description: str = None
    target: Union[dict, "FindingTarget"] = None
    implementation_statement_uuid: Optional[str] = None
    origins: Optional[Union[Union[dict, Origin], list[Union[dict, Origin]]]] = empty_list()
    related_observations: Optional[Union[Union[dict, "RelatedObservation"], list[Union[dict, "RelatedObservation"]]]] = empty_list()
    related_risks: Optional[Union[Union[dict, "AssociatedRisk"], list[Union[dict, "AssociatedRisk"]]]] = empty_list()
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uuid):
            self.MissingRequiredField("uuid")
        if not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self._is_empty(self.target):
            self.MissingRequiredField("target")
        if not isinstance(self.target, FindingTarget):
            self.target = FindingTarget(**as_dict(self.target))

        if self.implementation_statement_uuid is not None and not isinstance(self.implementation_statement_uuid, str):
            self.implementation_statement_uuid = str(self.implementation_statement_uuid)

        if not isinstance(self.origins, list):
            self.origins = [self.origins] if self.origins is not None else []
        self.origins = [v if isinstance(v, Origin) else Origin(**as_dict(v)) for v in self.origins]

        self._normalize_inlined_as_list(slot_name="related_observations", slot_type=RelatedObservation, key_name="observation-uuid", keyed=False)

        self._normalize_inlined_as_list(slot_name="related_risks", slot_type=AssociatedRisk, key_name="risk-uuid", keyed=False)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FindingTarget(YAMLRoot):
    """
    Captures an assessor's conclusions regarding the degree to which an objective is satisfied.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["FindingTarget"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:FindingTarget"
    class_name: ClassVar[str] = "FindingTarget"
    class_model_uri: ClassVar[URIRef] = OSCAL.FindingTarget

    type: Union[str, "FindingTargetTypeEnum"] = None
    target_id: str = None
    status: Union[dict, "ObjectiveStatus"] = None
    title: Optional[str] = None
    description: Optional[str] = None
    implementation_status: Optional[Union[dict, ImplementationStatus]] = None
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, FindingTargetTypeEnum):
            self.type = FindingTargetTypeEnum(self.type)

        if self._is_empty(self.target_id):
            self.MissingRequiredField("target_id")
        if not isinstance(self.target_id, str):
            self.target_id = str(self.target_id)

        if self._is_empty(self.status):
            self.MissingRequiredField("status")
        if not isinstance(self.status, ObjectiveStatus):
            self.status = ObjectiveStatus(**as_dict(self.status))

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.implementation_status is not None and not isinstance(self.implementation_status, ImplementationStatus):
            self.implementation_status = ImplementationStatus(**as_dict(self.implementation_status))

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ObjectiveStatus(YAMLRoot):
    """
    A determination of if the objective is satisfied or not within a given system.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["ObjectiveStatus"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:ObjectiveStatus"
    class_name: ClassVar[str] = "ObjectiveStatus"
    class_model_uri: ClassVar[URIRef] = OSCAL.ObjectiveStatus

    state: Union[str, "ObjectiveStatusStateEnum"] = None
    reason: Optional[str] = None
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.state):
            self.MissingRequiredField("state")
        if not isinstance(self.state, ObjectiveStatusStateEnum):
            self.state = ObjectiveStatusStateEnum(self.state)

        if self.reason is not None and not isinstance(self.reason, str):
            self.reason = str(self.reason)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RelatedObservation(YAMLRoot):
    """
    Relates the identified element to a set of referenced observations.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["RelatedObservation"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:RelatedObservation"
    class_name: ClassVar[str] = "RelatedObservation"
    class_model_uri: ClassVar[URIRef] = OSCAL.RelatedObservation

    observation_uuid: str = None
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.observation_uuid):
            self.MissingRequiredField("observation_uuid")
        if not isinstance(self.observation_uuid, str):
            self.observation_uuid = str(self.observation_uuid)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AssociatedRisk(YAMLRoot):
    """
    Relates the finding to a set of referenced risks.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["AssociatedRisk"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:AssociatedRisk"
    class_name: ClassVar[str] = "AssociatedRisk"
    class_model_uri: ClassVar[URIRef] = OSCAL.AssociatedRisk

    risk_uuid: str = None
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.risk_uuid):
            self.MissingRequiredField("risk_uuid")
        if not isinstance(self.risk_uuid, str):
            self.risk_uuid = str(self.risk_uuid)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Risk(YAMLRoot):
    """
    An identified risk.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["Risk"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:Risk"
    class_name: ClassVar[str] = "Risk"
    class_model_uri: ClassVar[URIRef] = OSCAL.Risk

    uuid: str = None
    title: str = None
    description: str = None
    statement: str = None
    status: str = None
    origins: Optional[Union[Union[dict, Origin], list[Union[dict, Origin]]]] = empty_list()
    threat_ids: Optional[Union[Union[dict, "ThreatId"], list[Union[dict, "ThreatId"]]]] = empty_list()
    characterizations: Optional[Union[Union[dict, "Characterization"], list[Union[dict, "Characterization"]]]] = empty_list()
    mitigating_factors: Optional[Union[Union[dict, "MitigatingFactor"], list[Union[dict, "MitigatingFactor"]]]] = empty_list()
    deadline: Optional[str] = None
    remediations: Optional[Union[Union[dict, "Response"], list[Union[dict, "Response"]]]] = empty_list()
    risk_log: Optional[Union[dict, "RiskLog"]] = None
    related_observations: Optional[Union[Union[dict, RelatedObservation], list[Union[dict, RelatedObservation]]]] = empty_list()
    props: Optional[Union[Union[dict, Property], list[Union[dict, Property]]]] = empty_list()
    links: Optional[Union[Union[dict, Link], list[Union[dict, Link]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uuid):
            self.MissingRequiredField("uuid")
        if not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self._is_empty(self.statement):
            self.MissingRequiredField("statement")
        if not isinstance(self.statement, str):
            self.statement = str(self.statement)

        if self._is_empty(self.status):
            self.MissingRequiredField("status")
        if not isinstance(self.status, str):
            self.status = str(self.status)

        if not isinstance(self.origins, list):
            self.origins = [self.origins] if self.origins is not None else []
        self.origins = [v if isinstance(v, Origin) else Origin(**as_dict(v)) for v in self.origins]

        self._normalize_inlined_as_list(slot_name="threat_ids", slot_type=ThreatId, key_name="system", keyed=False)

        if not isinstance(self.characterizations, list):
            self.characterizations = [self.characterizations] if self.characterizations is not None else []
        self.characterizations = [v if isinstance(v, Characterization) else Characterization(**as_dict(v)) for v in self.characterizations]

        self._normalize_inlined_as_list(slot_name="mitigating_factors", slot_type=MitigatingFactor, key_name="uuid", keyed=False)

        if self.deadline is not None and not isinstance(self.deadline, str):
            self.deadline = str(self.deadline)

        self._normalize_inlined_as_list(slot_name="remediations", slot_type=Response, key_name="uuid", keyed=False)

        if self.risk_log is not None and not isinstance(self.risk_log, RiskLog):
            self.risk_log = RiskLog(**as_dict(self.risk_log))

        self._normalize_inlined_as_list(slot_name="related_observations", slot_type=RelatedObservation, key_name="observation-uuid", keyed=False)

        self._normalize_inlined_as_list(slot_name="props", slot_type=Property, key_name="name", keyed=False)

        self._normalize_inlined_as_list(slot_name="links", slot_type=Link, key_name="href", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ThreatId(YAMLRoot):
    """
    A pointer, by ID, to an externally-defined threat.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["ThreatId"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:ThreatId"
    class_name: ClassVar[str] = "ThreatId"
    class_model_uri: ClassVar[URIRef] = OSCAL.ThreatId

    system: str = None
    id: str = None
    href: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.system):
            self.MissingRequiredField("system")
        if not isinstance(self.system, str):
            self.system = str(self.system)

        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self.href is not None and not isinstance(self.href, str):
            self.href = str(self.href)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Characterization(YAMLRoot):
    """
    A collection of descriptive data about the containing object from a specific origin.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["Characterization"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:Characterization"
    class_name: ClassVar[str] = "Characterization"
    class_model_uri: ClassVar[URIRef] = OSCAL.Characterization

    origin: Union[dict, Origin] = None
    facets: Union[Union[dict, "Facet"], list[Union[dict, "Facet"]]] = None
    props: Optional[Union[Union[dict, Property], list[Union[dict, Property]]]] = empty_list()
    links: Optional[Union[Union[dict, Link], list[Union[dict, Link]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.origin):
            self.MissingRequiredField("origin")
        if not isinstance(self.origin, Origin):
            self.origin = Origin(**as_dict(self.origin))

        if self._is_empty(self.facets):
            self.MissingRequiredField("facets")
        self._normalize_inlined_as_list(slot_name="facets", slot_type=Facet, key_name="name", keyed=False)

        self._normalize_inlined_as_list(slot_name="props", slot_type=Property, key_name="name", keyed=False)

        self._normalize_inlined_as_list(slot_name="links", slot_type=Link, key_name="href", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Facet(YAMLRoot):
    """
    An individual characteristic that is part of a larger set produced by the same actor.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["Facet"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:Facet"
    class_name: ClassVar[str] = "Facet"
    class_model_uri: ClassVar[URIRef] = OSCAL.Facet

    name: str = None
    value: str = None
    system: str = None
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, str):
            self.value = str(self.value)

        if self._is_empty(self.system):
            self.MissingRequiredField("system")
        if not isinstance(self.system, str):
            self.system = str(self.system)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MitigatingFactor(YAMLRoot):
    """
    Describes an existing mitigating factor that may affect the overall determination of the risk.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["MitigatingFactor"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:MitigatingFactor"
    class_name: ClassVar[str] = "MitigatingFactor"
    class_model_uri: ClassVar[URIRef] = OSCAL.MitigatingFactor

    uuid: str = None
    description: str = None
    implementation_uuid: Optional[str] = None
    subjects: Optional[Union[Union[dict, SubjectReference], list[Union[dict, SubjectReference]]]] = empty_list()
    props: Optional[Union[Union[dict, Property], list[Union[dict, Property]]]] = empty_list()
    links: Optional[Union[Union[dict, Link], list[Union[dict, Link]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uuid):
            self.MissingRequiredField("uuid")
        if not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self.implementation_uuid is not None and not isinstance(self.implementation_uuid, str):
            self.implementation_uuid = str(self.implementation_uuid)

        self._normalize_inlined_as_list(slot_name="subjects", slot_type=SubjectReference, key_name="subject-uuid", keyed=False)

        self._normalize_inlined_as_list(slot_name="props", slot_type=Property, key_name="name", keyed=False)

        self._normalize_inlined_as_list(slot_name="links", slot_type=Link, key_name="href", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Response(YAMLRoot):
    """
    Describes either recommended or an actual plan for addressing the risk.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["Response"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:Response"
    class_name: ClassVar[str] = "Response"
    class_model_uri: ClassVar[URIRef] = OSCAL.Response

    uuid: str = None
    title: str = None
    description: str = None
    lifecycle: str = None
    origins: Optional[Union[Union[dict, Origin], list[Union[dict, Origin]]]] = empty_list()
    required_assets: Optional[Union[Union[dict, "RequiredAsset"], list[Union[dict, "RequiredAsset"]]]] = empty_list()
    tasks: Optional[Union[Union[dict, Task], list[Union[dict, Task]]]] = empty_list()
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uuid):
            self.MissingRequiredField("uuid")
        if not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self._is_empty(self.lifecycle):
            self.MissingRequiredField("lifecycle")
        if not isinstance(self.lifecycle, str):
            self.lifecycle = str(self.lifecycle)

        if not isinstance(self.origins, list):
            self.origins = [self.origins] if self.origins is not None else []
        self.origins = [v if isinstance(v, Origin) else Origin(**as_dict(v)) for v in self.origins]

        self._normalize_inlined_as_list(slot_name="required_assets", slot_type=RequiredAsset, key_name="uuid", keyed=False)

        self._normalize_inlined_as_list(slot_name="tasks", slot_type=Task, key_name="uuid", keyed=False)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RequiredAsset(YAMLRoot):
    """
    Identifies an asset required to achieve remediation.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["RequiredAsset"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:RequiredAsset"
    class_name: ClassVar[str] = "RequiredAsset"
    class_model_uri: ClassVar[URIRef] = OSCAL.RequiredAsset

    uuid: str = None
    description: str = None
    title: Optional[str] = None
    subjects: Optional[Union[Union[dict, SubjectReference], list[Union[dict, SubjectReference]]]] = empty_list()
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uuid):
            self.MissingRequiredField("uuid")
        if not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        self._normalize_inlined_as_list(slot_name="subjects", slot_type=SubjectReference, key_name="subject-uuid", keyed=False)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RiskLog(YAMLRoot):
    """
    A log of all risk-related tasks taken.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["RiskLog"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:RiskLog"
    class_name: ClassVar[str] = "RiskLog"
    class_model_uri: ClassVar[URIRef] = OSCAL.RiskLog

    entries: Union[Union[dict, "RiskLogEntry"], list[Union[dict, "RiskLogEntry"]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.entries):
            self.MissingRequiredField("entries")
        self._normalize_inlined_as_list(slot_name="entries", slot_type=RiskLogEntry, key_name="uuid", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RiskLogEntry(YAMLRoot):
    """
    Identifies an individual risk response that occurred as part of managing an identified risk.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["RiskLogEntry"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:RiskLogEntry"
    class_name: ClassVar[str] = "RiskLogEntry"
    class_model_uri: ClassVar[URIRef] = OSCAL.RiskLogEntry

    uuid: str = None
    start: str = None
    title: Optional[str] = None
    description: Optional[str] = None
    end: Optional[str] = None
    logged_by: Optional[Union[Union[dict, "LoggedBy"], list[Union[dict, "LoggedBy"]]]] = empty_list()
    status_change: Optional[str] = None
    related_responses: Optional[Union[Union[dict, "RiskResponseReference"], list[Union[dict, "RiskResponseReference"]]]] = empty_list()
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uuid):
            self.MissingRequiredField("uuid")
        if not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        if self._is_empty(self.start):
            self.MissingRequiredField("start")
        if not isinstance(self.start, str):
            self.start = str(self.start)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.end is not None and not isinstance(self.end, str):
            self.end = str(self.end)

        self._normalize_inlined_as_list(slot_name="logged_by", slot_type=LoggedBy, key_name="party-uuid", keyed=False)

        if self.status_change is not None and not isinstance(self.status_change, str):
            self.status_change = str(self.status_change)

        self._normalize_inlined_as_list(slot_name="related_responses", slot_type=RiskResponseReference, key_name="response-uuid", keyed=False)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LoggedBy(YAMLRoot):
    """
    Used to indicate who created a log entry in what role.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["LoggedBy"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:LoggedBy"
    class_name: ClassVar[str] = "LoggedBy"
    class_model_uri: ClassVar[URIRef] = OSCAL.LoggedBy

    party_uuid: str = None
    role_id: Optional[str] = None
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.party_uuid):
            self.MissingRequiredField("party_uuid")
        if not isinstance(self.party_uuid, str):
            self.party_uuid = str(self.party_uuid)

        if self.role_id is not None and not isinstance(self.role_id, str):
            self.role_id = str(self.role_id)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RiskResponseReference(YAMLRoot):
    """
    Identifies an individual risk response that this log entry is for.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["RiskResponseReference"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:RiskResponseReference"
    class_name: ClassVar[str] = "RiskResponseReference"
    class_model_uri: ClassVar[URIRef] = OSCAL.RiskResponseReference

    response_uuid: str = None
    related_tasks: Optional[Union[Union[dict, RelatedTask], list[Union[dict, RelatedTask]]]] = empty_list()
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.response_uuid):
            self.MissingRequiredField("response_uuid")
        if not isinstance(self.response_uuid, str):
            self.response_uuid = str(self.response_uuid)

        self._normalize_inlined_as_list(slot_name="related_tasks", slot_type=RelatedTask, key_name="task-uuid", keyed=False)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AssessmentResultsDocument(OscalDocument):
    """
    Root wrapper for an OSCAL Assessment Results document.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_RESULTS["AssessmentResultsDocument"]
    class_class_curie: ClassVar[str] = "oscal_assessment_results:AssessmentResultsDocument"
    class_name: ClassVar[str] = "AssessmentResultsDocument"
    class_model_uri: ClassVar[URIRef] = OSCAL.AssessmentResultsDocument

    assessment_results: Union[dict, "AssessmentResults"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.assessment_results):
            self.MissingRequiredField("assessment_results")
        if not isinstance(self.assessment_results, AssessmentResults):
            self.assessment_results = AssessmentResults(**as_dict(self.assessment_results))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AssessmentResults(YAMLRoot):
    """
    Security assessment results, such as those provided by a FedRAMP assessor in a security assessment report.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_RESULTS["AssessmentResults"]
    class_class_curie: ClassVar[str] = "oscal_assessment_results:AssessmentResults"
    class_name: ClassVar[str] = "AssessmentResults"
    class_model_uri: ClassVar[URIRef] = OSCAL.AssessmentResults

    uuid: str = None
    metadata: Union[dict, Metadata] = None
    import_ap: Union[dict, "ImportAssessmentPlan"] = None
    results: Union[Union[dict, "Result"], list[Union[dict, "Result"]]] = None
    local_definitions: Optional[Union[dict, "AssessmentResultsLocalDefinitions"]] = None
    back_matter: Optional[Union[dict, BackMatter]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uuid):
            self.MissingRequiredField("uuid")
        if not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        if self._is_empty(self.metadata):
            self.MissingRequiredField("metadata")
        if not isinstance(self.metadata, Metadata):
            self.metadata = Metadata(**as_dict(self.metadata))

        if self._is_empty(self.import_ap):
            self.MissingRequiredField("import_ap")
        if not isinstance(self.import_ap, ImportAssessmentPlan):
            self.import_ap = ImportAssessmentPlan(**as_dict(self.import_ap))

        if self._is_empty(self.results):
            self.MissingRequiredField("results")
        self._normalize_inlined_as_list(slot_name="results", slot_type=Result, key_name="uuid", keyed=False)

        if self.local_definitions is not None and not isinstance(self.local_definitions, AssessmentResultsLocalDefinitions):
            self.local_definitions = AssessmentResultsLocalDefinitions(**as_dict(self.local_definitions))

        if self.back_matter is not None and not isinstance(self.back_matter, BackMatter):
            self.back_matter = BackMatter(**as_dict(self.back_matter))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ImportAssessmentPlan(YAMLRoot):
    """
    Used by assessment-results to import information about the original plan for assessing the system.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_RESULTS["ImportAssessmentPlan"]
    class_class_curie: ClassVar[str] = "oscal_assessment_results:ImportAssessmentPlan"
    class_name: ClassVar[str] = "ImportAssessmentPlan"
    class_model_uri: ClassVar[URIRef] = OSCAL.ImportAssessmentPlan

    href: str = None
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.href):
            self.MissingRequiredField("href")
        if not isinstance(self.href, str):
            self.href = str(self.href)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AssessmentResultsLocalDefinitions(YAMLRoot):
    """
    Used to define data objects that are referenced by the assessment results but do not appear in the imported
    assessment plan.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_RESULTS["AssessmentResultsLocalDefinitions"]
    class_class_curie: ClassVar[str] = "oscal_assessment_results:AssessmentResultsLocalDefinitions"
    class_name: ClassVar[str] = "AssessmentResultsLocalDefinitions"
    class_model_uri: ClassVar[URIRef] = OSCAL.AssessmentResultsLocalDefinitions

    objectives_and_methods: Optional[Union[Union[dict, LocalObjective], list[Union[dict, LocalObjective]]]] = empty_list()
    activities: Optional[Union[Union[dict, Activity], list[Union[dict, Activity]]]] = empty_list()
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="objectives_and_methods", slot_type=LocalObjective, key_name="control-id", keyed=False)

        self._normalize_inlined_as_list(slot_name="activities", slot_type=Activity, key_name="uuid", keyed=False)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Result(YAMLRoot):
    """
    Identifies all of the assessment observations and findings, initial and residual risks, deviations, and
    disposition for a particular execution of the assessment.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_RESULTS["Result"]
    class_class_curie: ClassVar[str] = "oscal_assessment_results:Result"
    class_name: ClassVar[str] = "Result"
    class_model_uri: ClassVar[URIRef] = OSCAL.Result

    uuid: str = None
    title: str = None
    description: str = None
    start: str = None
    reviewed_controls: Union[dict, ReviewedControls] = None
    end: Optional[str] = None
    local_definitions: Optional[Union[dict, "ResultLocalDefinitions"]] = None
    attestations: Optional[Union[Union[dict, "Attestation"], list[Union[dict, "Attestation"]]]] = empty_list()
    assessment_log: Optional[Union[dict, "AssessmentLog"]] = None
    observations: Optional[Union[Union[dict, Observation], list[Union[dict, Observation]]]] = empty_list()
    risks: Optional[Union[Union[dict, Risk], list[Union[dict, Risk]]]] = empty_list()
    findings: Optional[Union[Union[dict, Finding], list[Union[dict, Finding]]]] = empty_list()
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uuid):
            self.MissingRequiredField("uuid")
        if not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self._is_empty(self.start):
            self.MissingRequiredField("start")
        if not isinstance(self.start, str):
            self.start = str(self.start)

        if self._is_empty(self.reviewed_controls):
            self.MissingRequiredField("reviewed_controls")
        if not isinstance(self.reviewed_controls, ReviewedControls):
            self.reviewed_controls = ReviewedControls(**as_dict(self.reviewed_controls))

        if self.end is not None and not isinstance(self.end, str):
            self.end = str(self.end)

        if self.local_definitions is not None and not isinstance(self.local_definitions, ResultLocalDefinitions):
            self.local_definitions = ResultLocalDefinitions(**as_dict(self.local_definitions))

        if not isinstance(self.attestations, list):
            self.attestations = [self.attestations] if self.attestations is not None else []
        self.attestations = [v if isinstance(v, Attestation) else Attestation(**as_dict(v)) for v in self.attestations]

        if self.assessment_log is not None and not isinstance(self.assessment_log, AssessmentLog):
            self.assessment_log = AssessmentLog(**as_dict(self.assessment_log))

        self._normalize_inlined_as_list(slot_name="observations", slot_type=Observation, key_name="uuid", keyed=False)

        self._normalize_inlined_as_list(slot_name="risks", slot_type=Risk, key_name="uuid", keyed=False)

        self._normalize_inlined_as_list(slot_name="findings", slot_type=Finding, key_name="uuid", keyed=False)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ResultLocalDefinitions(YAMLRoot):
    """
    Used to define local implementation and assessment assets referenced by a result that do not appear in the
    imported system security plan.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_RESULTS["ResultLocalDefinitions"]
    class_class_curie: ClassVar[str] = "oscal_assessment_results:ResultLocalDefinitions"
    class_name: ClassVar[str] = "ResultLocalDefinitions"
    class_model_uri: ClassVar[URIRef] = OSCAL.ResultLocalDefinitions

    components: Optional[Union[Union[dict, SystemComponent], list[Union[dict, SystemComponent]]]] = empty_list()
    inventory_items: Optional[Union[Union[dict, InventoryItem], list[Union[dict, InventoryItem]]]] = empty_list()
    users: Optional[Union[Union[dict, SystemUser], list[Union[dict, SystemUser]]]] = empty_list()
    assessment_assets: Optional[Union[dict, AssessmentAssets]] = None
    tasks: Optional[Union[Union[dict, Task], list[Union[dict, Task]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="components", slot_type=SystemComponent, key_name="uuid", keyed=False)

        self._normalize_inlined_as_list(slot_name="inventory_items", slot_type=InventoryItem, key_name="uuid", keyed=False)

        self._normalize_inlined_as_list(slot_name="users", slot_type=SystemUser, key_name="uuid", keyed=False)

        if self.assessment_assets is not None and not isinstance(self.assessment_assets, AssessmentAssets):
            self.assessment_assets = AssessmentAssets(**as_dict(self.assessment_assets))

        self._normalize_inlined_as_list(slot_name="tasks", slot_type=Task, key_name="uuid", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Attestation(YAMLRoot):
    """
    A set of textual attestation statements, typically written by the assessor.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_RESULTS["Attestation"]
    class_class_curie: ClassVar[str] = "oscal_assessment_results:Attestation"
    class_name: ClassVar[str] = "Attestation"
    class_model_uri: ClassVar[URIRef] = OSCAL.Attestation

    parts: Union[Union[dict, AssessmentPart], list[Union[dict, AssessmentPart]]] = None
    responsible_parties: Optional[Union[Union[dict, ResponsibleParty], list[Union[dict, ResponsibleParty]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.parts):
            self.MissingRequiredField("parts")
        self._normalize_inlined_as_list(slot_name="parts", slot_type=AssessmentPart, key_name="name", keyed=False)

        self._normalize_inlined_as_list(slot_name="responsible_parties", slot_type=ResponsibleParty, key_name="role-id", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AssessmentLog(YAMLRoot):
    """
    A log of all assessment-related actions taken.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_RESULTS["AssessmentLog"]
    class_class_curie: ClassVar[str] = "oscal_assessment_results:AssessmentLog"
    class_name: ClassVar[str] = "AssessmentLog"
    class_model_uri: ClassVar[URIRef] = OSCAL.AssessmentLog

    entries: Union[Union[dict, "AssessmentLogEntry"], list[Union[dict, "AssessmentLogEntry"]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.entries):
            self.MissingRequiredField("entries")
        self._normalize_inlined_as_list(slot_name="entries", slot_type=AssessmentLogEntry, key_name="uuid", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AssessmentLogEntry(YAMLRoot):
    """
    Identifies the result of an action and/or task that occurred as part of executing an assessment plan or assessment
    event.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_RESULTS["AssessmentLogEntry"]
    class_class_curie: ClassVar[str] = "oscal_assessment_results:AssessmentLogEntry"
    class_name: ClassVar[str] = "AssessmentLogEntry"
    class_model_uri: ClassVar[URIRef] = OSCAL.AssessmentLogEntry

    uuid: str = None
    start: str = None
    title: Optional[str] = None
    description: Optional[str] = None
    end: Optional[str] = None
    logged_by: Optional[Union[Union[dict, LoggedBy], list[Union[dict, LoggedBy]]]] = empty_list()
    related_tasks: Optional[Union[Union[dict, RelatedTask], list[Union[dict, RelatedTask]]]] = empty_list()
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uuid):
            self.MissingRequiredField("uuid")
        if not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        if self._is_empty(self.start):
            self.MissingRequiredField("start")
        if not isinstance(self.start, str):
            self.start = str(self.start)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.end is not None and not isinstance(self.end, str):
            self.end = str(self.end)

        self._normalize_inlined_as_list(slot_name="logged_by", slot_type=LoggedBy, key_name="party-uuid", keyed=False)

        self._normalize_inlined_as_list(slot_name="related_tasks", slot_type=RelatedTask, key_name="task-uuid", keyed=False)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ComponentDefinitionDocument(OscalDocument):
    """
    Root wrapper for an OSCAL Component Definition document.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_COMPONENT["ComponentDefinitionDocument"]
    class_class_curie: ClassVar[str] = "oscal_component:ComponentDefinitionDocument"
    class_name: ClassVar[str] = "ComponentDefinitionDocument"
    class_model_uri: ClassVar[URIRef] = OSCAL.ComponentDefinitionDocument

    component_definition: Union[dict, "ComponentDefinition"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.component_definition):
            self.MissingRequiredField("component_definition")
        if not isinstance(self.component_definition, ComponentDefinition):
            self.component_definition = ComponentDefinition(**as_dict(self.component_definition))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ComponentDefinition(YAMLRoot):
    """
    A collection of component descriptions, which may optionally be grouped by capability.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_COMPONENT["ComponentDefinition"]
    class_class_curie: ClassVar[str] = "oscal_component:ComponentDefinition"
    class_name: ClassVar[str] = "ComponentDefinition"
    class_model_uri: ClassVar[URIRef] = OSCAL.ComponentDefinition

    uuid: str = None
    metadata: Union[dict, Metadata] = None
    import_component_definitions: Optional[Union[Union[dict, "ImportComponentDefinition"], list[Union[dict, "ImportComponentDefinition"]]]] = empty_list()
    components: Optional[Union[Union[dict, "DefinedComponent"], list[Union[dict, "DefinedComponent"]]]] = empty_list()
    capabilities: Optional[Union[Union[dict, "Capability"], list[Union[dict, "Capability"]]]] = empty_list()
    back_matter: Optional[Union[dict, BackMatter]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uuid):
            self.MissingRequiredField("uuid")
        if not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        if self._is_empty(self.metadata):
            self.MissingRequiredField("metadata")
        if not isinstance(self.metadata, Metadata):
            self.metadata = Metadata(**as_dict(self.metadata))

        self._normalize_inlined_as_list(slot_name="import_component_definitions", slot_type=ImportComponentDefinition, key_name="href", keyed=False)

        self._normalize_inlined_as_list(slot_name="components", slot_type=DefinedComponent, key_name="uuid", keyed=False)

        self._normalize_inlined_as_list(slot_name="capabilities", slot_type=Capability, key_name="uuid", keyed=False)

        if self.back_matter is not None and not isinstance(self.back_matter, BackMatter):
            self.back_matter = BackMatter(**as_dict(self.back_matter))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ImportComponentDefinition(YAMLRoot):
    """
    Loads a component definition from another resource.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_COMPONENT["ImportComponentDefinition"]
    class_class_curie: ClassVar[str] = "oscal_component:ImportComponentDefinition"
    class_name: ClassVar[str] = "ImportComponentDefinition"
    class_model_uri: ClassVar[URIRef] = OSCAL.ImportComponentDefinition

    href: str = None
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.href):
            self.MissingRequiredField("href")
        if not isinstance(self.href, str):
            self.href = str(self.href)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DefinedComponent(YAMLRoot):
    """
    A defined component that can be part of an implemented system.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_COMPONENT["DefinedComponent"]
    class_class_curie: ClassVar[str] = "oscal_component:DefinedComponent"
    class_name: ClassVar[str] = "DefinedComponent"
    class_model_uri: ClassVar[URIRef] = OSCAL.DefinedComponent

    uuid: str = None
    type: str = None
    title: str = None
    description: str = None
    purpose: Optional[str] = None
    protocols: Optional[Union[Union[dict, Protocol], list[Union[dict, Protocol]]]] = empty_list()
    control_implementations: Optional[Union[Union[dict, "ControlImplementationSet"], list[Union[dict, "ControlImplementationSet"]]]] = empty_list()
    remarks: Optional[str] = None
    responsible_roles: Optional[Union[Union[dict, ResponsibleRole], list[Union[dict, ResponsibleRole]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uuid):
            self.MissingRequiredField("uuid")
        if not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self.purpose is not None and not isinstance(self.purpose, str):
            self.purpose = str(self.purpose)

        if not isinstance(self.protocols, list):
            self.protocols = [self.protocols] if self.protocols is not None else []
        self.protocols = [v if isinstance(v, Protocol) else Protocol(**as_dict(v)) for v in self.protocols]

        self._normalize_inlined_as_list(slot_name="control_implementations", slot_type=ControlImplementationSet, key_name="uuid", keyed=False)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        self._normalize_inlined_as_list(slot_name="responsible_roles", slot_type=ResponsibleRole, key_name="role-id", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Capability(YAMLRoot):
    """
    A grouping of other components and/or capabilities.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_COMPONENT["Capability"]
    class_class_curie: ClassVar[str] = "oscal_component:Capability"
    class_name: ClassVar[str] = "Capability"
    class_model_uri: ClassVar[URIRef] = OSCAL.Capability

    uuid: str = None
    name: str = None
    description: str = None
    incorporates_components: Optional[Union[Union[dict, "IncorporatesComponent"], list[Union[dict, "IncorporatesComponent"]]]] = empty_list()
    control_implementations: Optional[Union[Union[dict, "ControlImplementationSet"], list[Union[dict, "ControlImplementationSet"]]]] = empty_list()
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uuid):
            self.MissingRequiredField("uuid")
        if not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_list(slot_name="incorporates_components", slot_type=IncorporatesComponent, key_name="component-uuid", keyed=False)

        self._normalize_inlined_as_list(slot_name="control_implementations", slot_type=ControlImplementationSet, key_name="uuid", keyed=False)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IncorporatesComponent(YAMLRoot):
    """
    The collection of components comprising a capability.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_COMPONENT["IncorporatesComponent"]
    class_class_curie: ClassVar[str] = "oscal_component:IncorporatesComponent"
    class_name: ClassVar[str] = "IncorporatesComponent"
    class_model_uri: ClassVar[URIRef] = OSCAL.IncorporatesComponent

    component_uuid: str = None
    description: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.component_uuid):
            self.MissingRequiredField("component_uuid")
        if not isinstance(self.component_uuid, str):
            self.component_uuid = str(self.component_uuid)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ControlImplementationSet(YAMLRoot):
    """
    Defines how the component or capability supports a set of controls.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_COMPONENT["ControlImplementationSet"]
    class_class_curie: ClassVar[str] = "oscal_component:ControlImplementationSet"
    class_name: ClassVar[str] = "ControlImplementationSet"
    class_model_uri: ClassVar[URIRef] = OSCAL.ControlImplementationSet

    uuid: str = None
    source: str = None
    description: str = None
    implemented_requirements: Union[Union[dict, "ImplementedRequirement"], list[Union[dict, "ImplementedRequirement"]]] = None
    set_parameters: Optional[Union[Union[dict, SetParameter], list[Union[dict, SetParameter]]]] = empty_list()
    props: Optional[Union[Union[dict, Property], list[Union[dict, Property]]]] = empty_list()
    links: Optional[Union[Union[dict, Link], list[Union[dict, Link]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uuid):
            self.MissingRequiredField("uuid")
        if not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        if self._is_empty(self.source):
            self.MissingRequiredField("source")
        if not isinstance(self.source, str):
            self.source = str(self.source)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self._is_empty(self.implemented_requirements):
            self.MissingRequiredField("implemented_requirements")
        self._normalize_inlined_as_list(slot_name="implemented_requirements", slot_type=ImplementedRequirement, key_name="uuid", keyed=False)

        self._normalize_inlined_as_list(slot_name="set_parameters", slot_type=SetParameter, key_name="param-id", keyed=False)

        self._normalize_inlined_as_list(slot_name="props", slot_type=Property, key_name="name", keyed=False)

        self._normalize_inlined_as_list(slot_name="links", slot_type=Link, key_name="href", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ImplementedRequirement(YAMLRoot):
    """
    Describes how the containing component or capability implements an individual control.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_COMPONENT["ImplementedRequirement"]
    class_class_curie: ClassVar[str] = "oscal_component:ImplementedRequirement"
    class_name: ClassVar[str] = "ImplementedRequirement"
    class_model_uri: ClassVar[URIRef] = OSCAL.ImplementedRequirement

    uuid: str = None
    control_id: str = None
    description: str = None
    set_parameters: Optional[Union[Union[dict, SetParameter], list[Union[dict, SetParameter]]]] = empty_list()
    statements: Optional[Union[Union[dict, "ImplementedControlStatement"], list[Union[dict, "ImplementedControlStatement"]]]] = empty_list()
    remarks: Optional[str] = None
    props: Optional[Union[Union[dict, Property], list[Union[dict, Property]]]] = empty_list()
    links: Optional[Union[Union[dict, Link], list[Union[dict, Link]]]] = empty_list()
    responsible_roles: Optional[Union[Union[dict, ResponsibleRole], list[Union[dict, ResponsibleRole]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uuid):
            self.MissingRequiredField("uuid")
        if not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        if self._is_empty(self.control_id):
            self.MissingRequiredField("control_id")
        if not isinstance(self.control_id, str):
            self.control_id = str(self.control_id)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_list(slot_name="set_parameters", slot_type=SetParameter, key_name="param-id", keyed=False)

        self._normalize_inlined_as_list(slot_name="statements", slot_type=ImplementedControlStatement, key_name="statement-id", keyed=False)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        self._normalize_inlined_as_list(slot_name="props", slot_type=Property, key_name="name", keyed=False)

        self._normalize_inlined_as_list(slot_name="links", slot_type=Link, key_name="href", keyed=False)

        self._normalize_inlined_as_list(slot_name="responsible_roles", slot_type=ResponsibleRole, key_name="role-id", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ImplementedControlStatement(YAMLRoot):
    """
    Identifies which statements within a control are addressed.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_COMPONENT["ImplementedControlStatement"]
    class_class_curie: ClassVar[str] = "oscal_component:ImplementedControlStatement"
    class_name: ClassVar[str] = "ImplementedControlStatement"
    class_model_uri: ClassVar[URIRef] = OSCAL.ImplementedControlStatement

    statement_id: str = None
    uuid: str = None
    description: str = None
    remarks: Optional[str] = None
    props: Optional[Union[Union[dict, Property], list[Union[dict, Property]]]] = empty_list()
    links: Optional[Union[Union[dict, Link], list[Union[dict, Link]]]] = empty_list()
    responsible_roles: Optional[Union[Union[dict, ResponsibleRole], list[Union[dict, ResponsibleRole]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.statement_id):
            self.MissingRequiredField("statement_id")
        if not isinstance(self.statement_id, str):
            self.statement_id = str(self.statement_id)

        if self._is_empty(self.uuid):
            self.MissingRequiredField("uuid")
        if not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        self._normalize_inlined_as_list(slot_name="props", slot_type=Property, key_name="name", keyed=False)

        self._normalize_inlined_as_list(slot_name="links", slot_type=Link, key_name="href", keyed=False)

        self._normalize_inlined_as_list(slot_name="responsible_roles", slot_type=ResponsibleRole, key_name="role-id", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MappingCollectionDocument(OscalDocument):
    """
    Root wrapper for an OSCAL Mapping Collection document.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_MAPPING["MappingCollectionDocument"]
    class_class_curie: ClassVar[str] = "oscal_mapping:MappingCollectionDocument"
    class_name: ClassVar[str] = "MappingCollectionDocument"
    class_model_uri: ClassVar[URIRef] = OSCAL.MappingCollectionDocument

    mapping_collection: Union[dict, "MappingCollection"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.mapping_collection):
            self.MissingRequiredField("mapping_collection")
        if not isinstance(self.mapping_collection, MappingCollection):
            self.mapping_collection = MappingCollection(**as_dict(self.mapping_collection))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MappingCollection(YAMLRoot):
    """
    A collection of control mappings between source and target resources.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_MAPPING["MappingCollection"]
    class_class_curie: ClassVar[str] = "oscal_mapping:MappingCollection"
    class_name: ClassVar[str] = "MappingCollection"
    class_model_uri: ClassVar[URIRef] = OSCAL.MappingCollection

    uuid: str = None
    metadata: Union[dict, Metadata] = None
    provenance: Union[dict, "MappingProvenance"] = None
    mappings: Union[Union[dict, "Mapping"], list[Union[dict, "Mapping"]]] = None
    back_matter: Optional[Union[dict, BackMatter]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uuid):
            self.MissingRequiredField("uuid")
        if not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        if self._is_empty(self.metadata):
            self.MissingRequiredField("metadata")
        if not isinstance(self.metadata, Metadata):
            self.metadata = Metadata(**as_dict(self.metadata))

        if self._is_empty(self.provenance):
            self.MissingRequiredField("provenance")
        if not isinstance(self.provenance, MappingProvenance):
            self.provenance = MappingProvenance(**as_dict(self.provenance))

        if self._is_empty(self.mappings):
            self.MissingRequiredField("mappings")
        self._normalize_inlined_as_list(slot_name="mappings", slot_type=Mapping, key_name="uuid", keyed=False)

        if self.back_matter is not None and not isinstance(self.back_matter, BackMatter):
            self.back_matter = BackMatter(**as_dict(self.back_matter))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MappingProvenance(YAMLRoot):
    """
    Mapping-level provenance details and mapping defaults.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_MAPPING["MappingProvenance"]
    class_class_curie: ClassVar[str] = "oscal_mapping:MappingProvenance"
    class_name: ClassVar[str] = "MappingProvenance"
    class_model_uri: ClassVar[URIRef] = OSCAL.MappingProvenance

    method: Union[str, "MappingMethodEnum"] = None
    matching_rationale: Union[str, "MatchingRationaleEnum"] = None
    status: Union[str, "MappingStatusEnum"] = None
    mapping_description: str = None
    confidence_score: Optional[Union[dict, "ConfidenceScore"]] = None
    coverage: Optional[Union[dict, "Coverage"]] = None
    remarks: Optional[str] = None
    responsible_parties: Optional[Union[Union[dict, ResponsibleParty], list[Union[dict, ResponsibleParty]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.method):
            self.MissingRequiredField("method")
        if not isinstance(self.method, MappingMethodEnum):
            self.method = MappingMethodEnum(self.method)

        if self._is_empty(self.matching_rationale):
            self.MissingRequiredField("matching_rationale")
        if not isinstance(self.matching_rationale, MatchingRationaleEnum):
            self.matching_rationale = MatchingRationaleEnum(self.matching_rationale)

        if self._is_empty(self.status):
            self.MissingRequiredField("status")
        if not isinstance(self.status, MappingStatusEnum):
            self.status = MappingStatusEnum(self.status)

        if self._is_empty(self.mapping_description):
            self.MissingRequiredField("mapping_description")
        if not isinstance(self.mapping_description, str):
            self.mapping_description = str(self.mapping_description)

        if self.confidence_score is not None and not isinstance(self.confidence_score, ConfidenceScore):
            self.confidence_score = ConfidenceScore(**as_dict(self.confidence_score))

        if self.coverage is not None and not isinstance(self.coverage, Coverage):
            self.coverage = Coverage(**as_dict(self.coverage))

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        self._normalize_inlined_as_list(slot_name="responsible_parties", slot_type=ResponsibleParty, key_name="role-id", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Mapping(YAMLRoot):
    """
    A mapping between two mapped resources.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_MAPPING["Mapping"]
    class_class_curie: ClassVar[str] = "oscal_mapping:Mapping"
    class_name: ClassVar[str] = "Mapping"
    class_model_uri: ClassVar[URIRef] = OSCAL.Mapping

    uuid: str = None
    source_resource: Union[dict, "MappingResourceReference"] = None
    target_resource: Union[dict, "MappingResourceReference"] = None
    maps: Union[Union[dict, "Map"], list[Union[dict, "Map"]]] = None
    method: Optional[Union[str, "MappingMethodEnum"]] = None
    matching_rationale: Optional[Union[str, "MatchingRationaleEnum"]] = None
    status: Optional[Union[str, "MappingStatusEnum"]] = None
    mapping_description: Optional[str] = None
    source_gap_summary: Optional[Union[dict, "GapSummary"]] = None
    target_gap_summary: Optional[Union[dict, "GapSummary"]] = None
    confidence_score: Optional[Union[dict, "ConfidenceScore"]] = None
    coverage: Optional[Union[dict, "Coverage"]] = None
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uuid):
            self.MissingRequiredField("uuid")
        if not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        if self._is_empty(self.source_resource):
            self.MissingRequiredField("source_resource")
        if not isinstance(self.source_resource, MappingResourceReference):
            self.source_resource = MappingResourceReference(**as_dict(self.source_resource))

        if self._is_empty(self.target_resource):
            self.MissingRequiredField("target_resource")
        if not isinstance(self.target_resource, MappingResourceReference):
            self.target_resource = MappingResourceReference(**as_dict(self.target_resource))

        if self._is_empty(self.maps):
            self.MissingRequiredField("maps")
        self._normalize_inlined_as_list(slot_name="maps", slot_type=Map, key_name="uuid", keyed=False)

        if self.method is not None and not isinstance(self.method, MappingMethodEnum):
            self.method = MappingMethodEnum(self.method)

        if self.matching_rationale is not None and not isinstance(self.matching_rationale, MatchingRationaleEnum):
            self.matching_rationale = MatchingRationaleEnum(self.matching_rationale)

        if self.status is not None and not isinstance(self.status, MappingStatusEnum):
            self.status = MappingStatusEnum(self.status)

        if self.mapping_description is not None and not isinstance(self.mapping_description, str):
            self.mapping_description = str(self.mapping_description)

        if self.source_gap_summary is not None and not isinstance(self.source_gap_summary, GapSummary):
            self.source_gap_summary = GapSummary(**as_dict(self.source_gap_summary))

        if self.target_gap_summary is not None and not isinstance(self.target_gap_summary, GapSummary):
            self.target_gap_summary = GapSummary(**as_dict(self.target_gap_summary))

        if self.confidence_score is not None and not isinstance(self.confidence_score, ConfidenceScore):
            self.confidence_score = ConfidenceScore(**as_dict(self.confidence_score))

        if self.coverage is not None and not isinstance(self.coverage, Coverage):
            self.coverage = Coverage(**as_dict(self.coverage))

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Map(YAMLRoot):
    """
    A relationship-based mapping entry between source and target sets.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_MAPPING["Map"]
    class_class_curie: ClassVar[str] = "oscal_mapping:Map"
    class_name: ClassVar[str] = "Map"
    class_model_uri: ClassVar[URIRef] = OSCAL.Map

    uuid: str = None
    relationship: str = None
    sources: Union[Union[dict, "MappingItem"], list[Union[dict, "MappingItem"]]] = None
    targets: Union[Union[dict, "MappingItem"], list[Union[dict, "MappingItem"]]] = None
    ns: Optional[str] = None
    matching_rationale: Optional[Union[str, "MatchingRationaleEnum"]] = None
    qualifiers: Optional[Union[Union[dict, "QualifierItem"], list[Union[dict, "QualifierItem"]]]] = empty_list()
    confidence_score: Optional[Union[dict, "ConfidenceScore"]] = None
    coverage: Optional[Union[dict, "Coverage"]] = None
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uuid):
            self.MissingRequiredField("uuid")
        if not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        if self._is_empty(self.relationship):
            self.MissingRequiredField("relationship")
        if not isinstance(self.relationship, str):
            self.relationship = str(self.relationship)

        if self._is_empty(self.sources):
            self.MissingRequiredField("sources")
        self._normalize_inlined_as_list(slot_name="sources", slot_type=MappingItem, key_name="type", keyed=False)

        if self._is_empty(self.targets):
            self.MissingRequiredField("targets")
        self._normalize_inlined_as_list(slot_name="targets", slot_type=MappingItem, key_name="type", keyed=False)

        if self.ns is not None and not isinstance(self.ns, str):
            self.ns = str(self.ns)

        if self.matching_rationale is not None and not isinstance(self.matching_rationale, MatchingRationaleEnum):
            self.matching_rationale = MatchingRationaleEnum(self.matching_rationale)

        self._normalize_inlined_as_list(slot_name="qualifiers", slot_type=QualifierItem, key_name="subject", keyed=False)

        if self.confidence_score is not None and not isinstance(self.confidence_score, ConfidenceScore):
            self.confidence_score = ConfidenceScore(**as_dict(self.confidence_score))

        if self.coverage is not None and not isinstance(self.coverage, Coverage):
            self.coverage = Coverage(**as_dict(self.coverage))

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MappingItem(YAMLRoot):
    """
    A source or target item participating in a mapping entry.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_MAPPING["MappingItem"]
    class_class_curie: ClassVar[str] = "oscal_mapping:MappingItem"
    class_name: ClassVar[str] = "MappingItem"
    class_model_uri: ClassVar[URIRef] = OSCAL.MappingItem

    type: Union[str, "MappingSubjectTypeEnum"] = None
    id_ref: str = None
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, MappingSubjectTypeEnum):
            self.type = MappingSubjectTypeEnum(self.type)

        if self._is_empty(self.id_ref):
            self.MissingRequiredField("id_ref")
        if not isinstance(self.id_ref, str):
            self.id_ref = str(self.id_ref)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MappingResourceReference(YAMLRoot):
    """
    A reference to the source or target resource for a mapping.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_MAPPING["MappingResourceReference"]
    class_class_curie: ClassVar[str] = "oscal_mapping:MappingResourceReference"
    class_name: ClassVar[str] = "MappingResourceReference"
    class_model_uri: ClassVar[URIRef] = OSCAL.MappingResourceReference

    type: str = None
    href: str = None
    ns: Optional[str] = None
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.href):
            self.MissingRequiredField("href")
        if not isinstance(self.href, str):
            self.href = str(self.href)

        if self.ns is not None and not isinstance(self.ns, str):
            self.ns = str(self.ns)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class QualifierItem(YAMLRoot):
    """
    A qualifier describing requirements or incompatibilities.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_MAPPING["QualifierItem"]
    class_class_curie: ClassVar[str] = "oscal_mapping:QualifierItem"
    class_name: ClassVar[str] = "QualifierItem"
    class_model_uri: ClassVar[URIRef] = OSCAL.QualifierItem

    subject: Union[str, "QualifierSubjectEnum"] = None
    predicate: Union[str, "QualifierPredicateEnum"] = None
    category: Union[str, "QualifierCategoryEnum"] = None
    description: str = None
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, QualifierSubjectEnum):
            self.subject = QualifierSubjectEnum(self.subject)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, QualifierPredicateEnum):
            self.predicate = QualifierPredicateEnum(self.predicate)

        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, QualifierCategoryEnum):
            self.category = QualifierCategoryEnum(self.category)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GapSummary(YAMLRoot):
    """
    A summary of controls that were not mapped.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_MAPPING["GapSummary"]
    class_class_curie: ClassVar[str] = "oscal_mapping:GapSummary"
    class_name: ClassVar[str] = "GapSummary"
    class_model_uri: ClassVar[URIRef] = OSCAL.GapSummary

    uuid: str = None
    unmapped_controls: Union[Union[dict, SelectControlById], list[Union[dict, SelectControlById]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uuid):
            self.MissingRequiredField("uuid")
        if not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        if self._is_empty(self.unmapped_controls):
            self.MissingRequiredField("unmapped_controls")
        if not isinstance(self.unmapped_controls, list):
            self.unmapped_controls = [self.unmapped_controls] if self.unmapped_controls is not None else []
        self.unmapped_controls = [v if isinstance(v, SelectControlById) else SelectControlById(**as_dict(v)) for v in self.unmapped_controls]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ConfidenceScore(YAMLRoot):
    """
    Confidence represented as a category and/or percentage value.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_MAPPING["ConfidenceScore"]
    class_class_curie: ClassVar[str] = "oscal_mapping:ConfidenceScore"
    class_name: ClassVar[str] = "ConfidenceScore"
    class_model_uri: ClassVar[URIRef] = OSCAL.ConfidenceScore

    category: Optional[str] = None
    percentage: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.category is not None and not isinstance(self.category, str):
            self.category = str(self.category)

        if self.percentage is not None and not isinstance(self.percentage, float):
            self.percentage = float(self.percentage)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Coverage(YAMLRoot):
    """
    A percentage representing target coverage by source mappings.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_MAPPING["Coverage"]
    class_class_curie: ClassVar[str] = "oscal_mapping:Coverage"
    class_name: ClassVar[str] = "Coverage"
    class_model_uri: ClassVar[URIRef] = OSCAL.Coverage

    target_coverage: float = None
    generation_method: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.target_coverage):
            self.MissingRequiredField("target_coverage")
        if not isinstance(self.target_coverage, float):
            self.target_coverage = float(self.target_coverage)

        if self.generation_method is not None and not isinstance(self.generation_method, str):
            self.generation_method = str(self.generation_method)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PoamDocument(OscalDocument):
    """
    Root wrapper for an OSCAL Plan of Action and Milestones document.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_POAM["PoamDocument"]
    class_class_curie: ClassVar[str] = "oscal_poam:PoamDocument"
    class_name: ClassVar[str] = "PoamDocument"
    class_model_uri: ClassVar[URIRef] = OSCAL.PoamDocument

    plan_of_action_and_milestones: Union[dict, "PlanOfActionAndMilestones"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.plan_of_action_and_milestones):
            self.MissingRequiredField("plan_of_action_and_milestones")
        if not isinstance(self.plan_of_action_and_milestones, PlanOfActionAndMilestones):
            self.plan_of_action_and_milestones = PlanOfActionAndMilestones(**as_dict(self.plan_of_action_and_milestones))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PlanOfActionAndMilestones(YAMLRoot):
    """
    A plan of action and milestones that identifies initial and residual risks, deviations, and disposition.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_POAM["PlanOfActionAndMilestones"]
    class_class_curie: ClassVar[str] = "oscal_poam:PlanOfActionAndMilestones"
    class_name: ClassVar[str] = "PlanOfActionAndMilestones"
    class_model_uri: ClassVar[URIRef] = OSCAL.PlanOfActionAndMilestones

    uuid: str = None
    metadata: Union[dict, Metadata] = None
    poam_items: Union[Union[dict, "PoamItem"], list[Union[dict, "PoamItem"]]] = None
    import_ssp: Optional[Union[dict, ImportSSP]] = None
    system_id: Optional[Union[dict, SystemId]] = None
    local_definitions: Optional[Union[dict, "PoamLocalDefinitions"]] = None
    observations: Optional[Union[Union[dict, Observation], list[Union[dict, Observation]]]] = empty_list()
    risks: Optional[Union[Union[dict, Risk], list[Union[dict, Risk]]]] = empty_list()
    findings: Optional[Union[Union[dict, Finding], list[Union[dict, Finding]]]] = empty_list()
    back_matter: Optional[Union[dict, BackMatter]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uuid):
            self.MissingRequiredField("uuid")
        if not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        if self._is_empty(self.metadata):
            self.MissingRequiredField("metadata")
        if not isinstance(self.metadata, Metadata):
            self.metadata = Metadata(**as_dict(self.metadata))

        if self._is_empty(self.poam_items):
            self.MissingRequiredField("poam_items")
        self._normalize_inlined_as_list(slot_name="poam_items", slot_type=PoamItem, key_name="title", keyed=False)

        if self.import_ssp is not None and not isinstance(self.import_ssp, ImportSSP):
            self.import_ssp = ImportSSP(**as_dict(self.import_ssp))

        if self.system_id is not None and not isinstance(self.system_id, SystemId):
            self.system_id = SystemId(**as_dict(self.system_id))

        if self.local_definitions is not None and not isinstance(self.local_definitions, PoamLocalDefinitions):
            self.local_definitions = PoamLocalDefinitions(**as_dict(self.local_definitions))

        self._normalize_inlined_as_list(slot_name="observations", slot_type=Observation, key_name="uuid", keyed=False)

        self._normalize_inlined_as_list(slot_name="risks", slot_type=Risk, key_name="uuid", keyed=False)

        self._normalize_inlined_as_list(slot_name="findings", slot_type=Finding, key_name="uuid", keyed=False)

        if self.back_matter is not None and not isinstance(self.back_matter, BackMatter):
            self.back_matter = BackMatter(**as_dict(self.back_matter))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PoamLocalDefinitions(YAMLRoot):
    """
    Allows components and inventory items to be defined within the POA&M for cases where no OSCAL SSP is available
    with the POA&M.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_POAM["PoamLocalDefinitions"]
    class_class_curie: ClassVar[str] = "oscal_poam:PoamLocalDefinitions"
    class_name: ClassVar[str] = "PoamLocalDefinitions"
    class_model_uri: ClassVar[URIRef] = OSCAL.PoamLocalDefinitions

    components: Optional[Union[Union[dict, SystemComponent], list[Union[dict, SystemComponent]]]] = empty_list()
    inventory_items: Optional[Union[Union[dict, InventoryItem], list[Union[dict, InventoryItem]]]] = empty_list()
    assessment_assets: Optional[Union[dict, AssessmentAssets]] = None
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="components", slot_type=SystemComponent, key_name="uuid", keyed=False)

        self._normalize_inlined_as_list(slot_name="inventory_items", slot_type=InventoryItem, key_name="uuid", keyed=False)

        if self.assessment_assets is not None and not isinstance(self.assessment_assets, AssessmentAssets):
            self.assessment_assets = AssessmentAssets(**as_dict(self.assessment_assets))

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PoamItem(YAMLRoot):
    """
    Describes an individual POA&M item.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_POAM["PoamItem"]
    class_class_curie: ClassVar[str] = "oscal_poam:PoamItem"
    class_name: ClassVar[str] = "PoamItem"
    class_model_uri: ClassVar[URIRef] = OSCAL.PoamItem

    title: str = None
    description: str = None
    uuid: Optional[str] = None
    origins: Optional[Union[Union[dict, Origin], list[Union[dict, Origin]]]] = empty_list()
    related_findings: Optional[Union[Union[dict, "RelatedFinding"], list[Union[dict, "RelatedFinding"]]]] = empty_list()
    related_observations: Optional[Union[Union[dict, RelatedObservation], list[Union[dict, RelatedObservation]]]] = empty_list()
    related_risks: Optional[Union[Union[dict, AssociatedRisk], list[Union[dict, AssociatedRisk]]]] = empty_list()
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self.uuid is not None and not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        if not isinstance(self.origins, list):
            self.origins = [self.origins] if self.origins is not None else []
        self.origins = [v if isinstance(v, Origin) else Origin(**as_dict(v)) for v in self.origins]

        self._normalize_inlined_as_list(slot_name="related_findings", slot_type=RelatedFinding, key_name="finding-uuid", keyed=False)

        self._normalize_inlined_as_list(slot_name="related_observations", slot_type=RelatedObservation, key_name="observation-uuid", keyed=False)

        self._normalize_inlined_as_list(slot_name="related_risks", slot_type=AssociatedRisk, key_name="risk-uuid", keyed=False)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RelatedFinding(YAMLRoot):
    """
    Relates a POA&M item to a referenced finding.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_POAM["RelatedFinding"]
    class_class_curie: ClassVar[str] = "oscal_poam:RelatedFinding"
    class_name: ClassVar[str] = "RelatedFinding"
    class_model_uri: ClassVar[URIRef] = OSCAL.RelatedFinding

    finding_uuid: str = None
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.finding_uuid):
            self.MissingRequiredField("finding_uuid")
        if not isinstance(self.finding_uuid, str):
            self.finding_uuid = str(self.finding_uuid)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


# Enumerations
class PartyTypeEnum(EnumDefinitionImpl):

    person = PermissibleValue(text="person")
    organization = PermissibleValue(text="organization")

    _defn = EnumDefinition(
        name="PartyTypeEnum",
    )

class HashAlgorithmEnum(EnumDefinitionImpl):
    """
    Curated hash algorithm values. Other values are permitted (OSCAL allow-other="yes").
    """
    _defn = EnumDefinition(
        name="HashAlgorithmEnum",
        description="""Curated hash algorithm values. Other values are permitted (OSCAL allow-other=\"yes\").""",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "SHA-224",
            PermissibleValue(text="SHA-224"))
        setattr(cls, "SHA-256",
            PermissibleValue(text="SHA-256"))
        setattr(cls, "SHA-384",
            PermissibleValue(text="SHA-384"))
        setattr(cls, "SHA-512",
            PermissibleValue(text="SHA-512"))
        setattr(cls, "SHA3-224",
            PermissibleValue(text="SHA3-224"))
        setattr(cls, "SHA3-256",
            PermissibleValue(text="SHA3-256"))
        setattr(cls, "SHA3-384",
            PermissibleValue(text="SHA3-384"))
        setattr(cls, "SHA3-512",
            PermissibleValue(text="SHA3-512"))

class PhoneTypeEnum(EnumDefinitionImpl):
    """
    Curated telephone number type values. Other values are permitted (OSCAL allow-other="yes").
    """
    home = PermissibleValue(text="home")
    office = PermissibleValue(text="office")
    mobile = PermissibleValue(text="mobile")

    _defn = EnumDefinition(
        name="PhoneTypeEnum",
        description="""Curated telephone number type values. Other values are permitted (OSCAL allow-other=\"yes\").""",
    )

class AddressTypeEnum(EnumDefinitionImpl):
    """
    Curated address type values. Other values are permitted (OSCAL allow-other="yes").
    """
    home = PermissibleValue(text="home")
    work = PermissibleValue(text="work")

    _defn = EnumDefinition(
        name="AddressTypeEnum",
        description="""Curated address type values. Other values are permitted (OSCAL allow-other=\"yes\").""",
    )

class MetadataLinkRelEnum(EnumDefinitionImpl):
    """
    Curated metadata link relation values. Other values are permitted (OSCAL allow-other="yes").
    """
    canonical = PermissibleValue(text="canonical")
    alternate = PermissibleValue(text="alternate")
    reference = PermissibleValue(text="reference")

    _defn = EnumDefinition(
        name="MetadataLinkRelEnum",
        description="""Curated metadata link relation values. Other values are permitted (OSCAL allow-other=\"yes\").""",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "latest-version",
            PermissibleValue(text="latest-version"))
        setattr(cls, "predecessor-version",
            PermissibleValue(text="predecessor-version"))
        setattr(cls, "successor-version",
            PermissibleValue(text="successor-version"))
        setattr(cls, "version-history",
            PermissibleValue(text="version-history"))
        setattr(cls, "source-profile",
            PermissibleValue(text="source-profile"))
        setattr(cls, "source-profile-uuid",
            PermissibleValue(text="source-profile-uuid"))

class LocationPropNameEnum(EnumDefinitionImpl):
    """
    Allowed OSCAL property names for metadata locations.
    """
    type = PermissibleValue(text="type")

    _defn = EnumDefinition(
        name="LocationPropNameEnum",
        description="Allowed OSCAL property names for metadata locations.",
    )

class LocationPropTypeEnum(EnumDefinitionImpl):
    """
    Curated OSCAL location type property values. Other values are permitted (OSCAL allow-other="yes").
    """
    _defn = EnumDefinition(
        name="LocationPropTypeEnum",
        description="""Curated OSCAL location type property values. Other values are permitted (OSCAL allow-other=\"yes\").""",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "data-center",
            PermissibleValue(text="data-center"))

class LocationDataCenterClassEnum(EnumDefinitionImpl):
    """
    Curated OSCAL location class values for data-center type. Other values are permitted (OSCAL allow-other="yes").
    """
    primary = PermissibleValue(text="primary")
    alternate = PermissibleValue(text="alternate")

    _defn = EnumDefinition(
        name="LocationDataCenterClassEnum",
        description="""Curated OSCAL location class values for data-center type. Other values are permitted (OSCAL allow-other=\"yes\").""",
    )

class PartyExternalIdSchemeEnum(EnumDefinitionImpl):
    """
    Curated external identifier scheme values for metadata parties. Other values are permitted (OSCAL
    allow-other="yes").
    """
    _defn = EnumDefinition(
        name="PartyExternalIdSchemeEnum",
        description="""Curated external identifier scheme values for metadata parties. Other values are permitted (OSCAL allow-other=\"yes\").""",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "http://orcid.org/",
            PermissibleValue(text="http://orcid.org/"))

class PartyPropNameEnum(EnumDefinitionImpl):
    """
    Allowed OSCAL property names for metadata parties.
    """
    office = PermissibleValue(text="office")

    _defn = EnumDefinition(
        name="PartyPropNameEnum",
        description="Allowed OSCAL property names for metadata parties.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "mail-stop",
            PermissibleValue(text="mail-stop"))
        setattr(cls, "job-title",
            PermissibleValue(text="job-title"))

class MetadataResponsiblePartyRoleIdEnum(EnumDefinitionImpl):
    """
    Curated metadata responsible-party role identifiers. Other values are permitted (OSCAL allow-other="yes").
    """
    creator = PermissibleValue(text="creator")
    contact = PermissibleValue(text="contact")

    _defn = EnumDefinition(
        name="MetadataResponsiblePartyRoleIdEnum",
        description="""Curated metadata responsible-party role identifiers. Other values are permitted (OSCAL allow-other=\"yes\").""",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "prepared-by",
            PermissibleValue(text="prepared-by"))
        setattr(cls, "prepared-for",
            PermissibleValue(text="prepared-for"))
        setattr(cls, "content-approver",
            PermissibleValue(text="content-approver"))

class MetadataPropNameEnum(EnumDefinitionImpl):
    """
    Allowed OSCAL property names for metadata.
    """
    keywords = PermissibleValue(text="keywords")

    _defn = EnumDefinition(
        name="MetadataPropNameEnum",
        description="Allowed OSCAL property names for metadata.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "resolution-tool",
            PermissibleValue(text="resolution-tool"))
        setattr(cls, "source-profile-uuid",
            PermissibleValue(text="source-profile-uuid"))

class RevisionPropNameEnum(EnumDefinitionImpl):
    """
    Allowed OSCAL property names for metadata revisions.
    """
    marking = PermissibleValue(text="marking")

    _defn = EnumDefinition(
        name="RevisionPropNameEnum",
        description="Allowed OSCAL property names for metadata revisions.",
    )

class ResourcePropNameEnum(EnumDefinitionImpl):
    """
    Allowed OSCAL property names for back-matter resources.
    """
    type = PermissibleValue(text="type")
    version = PermissibleValue(text="version")
    published = PermissibleValue(text="published")

    _defn = EnumDefinition(
        name="ResourcePropNameEnum",
        description="Allowed OSCAL property names for back-matter resources.",
    )

class ResourcePropTypeEnum(EnumDefinitionImpl):
    """
    Allowed OSCAL back-matter resource type property values.
    """
    logo = PermissibleValue(text="logo")
    image = PermissibleValue(text="image")
    law = PermissibleValue(text="law")
    regulation = PermissibleValue(text="regulation")
    standard = PermissibleValue(text="standard")
    acronyms = PermissibleValue(text="acronyms")
    citation = PermissibleValue(text="citation")
    policy = PermissibleValue(text="policy")
    procedure = PermissibleValue(text="procedure")
    plan = PermissibleValue(text="plan")
    artifact = PermissibleValue(text="artifact")
    evidence = PermissibleValue(text="evidence")
    questionnaire = PermissibleValue(text="questionnaire")
    report = PermissibleValue(text="report")
    agreement = PermissibleValue(text="agreement")

    _defn = EnumDefinition(
        name="ResourcePropTypeEnum",
        description="Allowed OSCAL back-matter resource type property values.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "screen-shot",
            PermissibleValue(text="screen-shot"))
        setattr(cls, "external-guidance",
            PermissibleValue(text="external-guidance"))
        setattr(cls, "system-guide",
            PermissibleValue(text="system-guide"))
        setattr(cls, "users-guide",
            PermissibleValue(text="users-guide"))
        setattr(cls, "administrators-guide",
            PermissibleValue(text="administrators-guide"))
        setattr(cls, "rules-of-behavior",
            PermissibleValue(text="rules-of-behavior"))
        setattr(cls, "tool-output",
            PermissibleValue(text="tool-output"))
        setattr(cls, "raw-data",
            PermissibleValue(text="raw-data"))
        setattr(cls, "interview-notes",
            PermissibleValue(text="interview-notes"))

class ActionSystemEnum(EnumDefinitionImpl):
    """
    Curated OSCAL action system values. Other values are permitted (OSCAL allow-other="yes").
    """
    _defn = EnumDefinition(
        name="ActionSystemEnum",
        description="""Curated OSCAL action system values. Other values are permitted (OSCAL allow-other=\"yes\").""",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "http://csrc.nist.gov/ns/oscal",
            PermissibleValue(text="http://csrc.nist.gov/ns/oscal"))

class ActionTypeEnum(EnumDefinitionImpl):
    """
    Allowed OSCAL action type values.
    """
    approval = PermissibleValue(text="approval")

    _defn = EnumDefinition(
        name="ActionTypeEnum",
        description="Allowed OSCAL action type values.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "request-changes",
            PermissibleValue(text="request-changes"))

class DocumentIdSchemeEnum(EnumDefinitionImpl):
    """
    Curated document identifier scheme values. Other values are permitted (OSCAL allow-other="yes").
    """
    _defn = EnumDefinition(
        name="DocumentIdSchemeEnum",
        description="""Curated document identifier scheme values. Other values are permitted (OSCAL allow-other=\"yes\").""",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "http://www.doi.org/",
            PermissibleValue(text="http://www.doi.org/"))

class ParameterCardinalityEnum(EnumDefinitionImpl):

    one = PermissibleValue(text="one")

    _defn = EnumDefinition(
        name="ParameterCardinalityEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "one-or-more",
            PermissibleValue(text="one-or-more"))

class PartPropNameEnum(EnumDefinitionImpl):
    """
    Allowed OSCAL property names for control-common parts.
    """
    label = PermissibleValue(text="label")

    _defn = EnumDefinition(
        name="PartPropNameEnum",
        description="Allowed OSCAL property names for control-common parts.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "sort-id",
            PermissibleValue(text="sort-id"))
        setattr(cls, "alt-identifier",
            PermissibleValue(text="alt-identifier"))

class ParameterPropNameEnum(EnumDefinitionImpl):
    """
    Allowed OSCAL property names for control-common parameters.
    """
    label = PermissibleValue(text="label")

    _defn = EnumDefinition(
        name="ParameterPropNameEnum",
        description="Allowed OSCAL property names for control-common parameters.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "sort-id",
            PermissibleValue(text="sort-id"))
        setattr(cls, "alt-identifier",
            PermissibleValue(text="alt-identifier"))
        setattr(cls, "alt-label",
            PermissibleValue(text="alt-label"))

class RmfParameterPropNameEnum(EnumDefinitionImpl):
    """
    Allowed OSCAL RMF parameter property names.
    """
    aggregates = PermissibleValue(text="aggregates")

    _defn = EnumDefinition(
        name="RmfParameterPropNameEnum",
        description="Allowed OSCAL RMF parameter property names.",
    )

class GroupPartNameEnum(EnumDefinitionImpl):
    """
    Allowed OSCAL part names for catalog groups.
    """
    overview = PermissibleValue(text="overview")
    instruction = PermissibleValue(text="instruction")

    _defn = EnumDefinition(
        name="GroupPartNameEnum",
        description="Allowed OSCAL part names for catalog groups.",
    )

class ControlPropNameEnum(EnumDefinitionImpl):
    """
    Allowed OSCAL property names for catalog controls.
    """
    label = PermissibleValue(text="label")
    status = PermissibleValue(text="status")

    _defn = EnumDefinition(
        name="ControlPropNameEnum",
        description="Allowed OSCAL property names for catalog controls.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "sort-id",
            PermissibleValue(text="sort-id"))
        setattr(cls, "alt-identifier",
            PermissibleValue(text="alt-identifier"))

class ControlPropStatusValueEnum(EnumDefinitionImpl):
    """
    Allowed OSCAL status property values for catalog controls.
    """
    withdrawn = PermissibleValue(text="withdrawn")
    Withdrawn = PermissibleValue(text="Withdrawn")

    _defn = EnumDefinition(
        name="ControlPropStatusValueEnum",
        description="Allowed OSCAL status property values for catalog controls.",
    )

class ControlLinkRelEnum(EnumDefinitionImpl):
    """
    Curated OSCAL link relation values for catalog controls. Other values are permitted (OSCAL allow-other="yes").
    """
    reference = PermissibleValue(text="reference")
    related = PermissibleValue(text="related")
    required = PermissibleValue(text="required")

    _defn = EnumDefinition(
        name="ControlLinkRelEnum",
        description="""Curated OSCAL link relation values for catalog controls. Other values are permitted (OSCAL allow-other=\"yes\").""",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "incorporated-into",
            PermissibleValue(text="incorporated-into"))
        setattr(cls, "moved-to",
            PermissibleValue(text="moved-to"))

class ControlPartNameEnum(EnumDefinitionImpl):
    """
    Allowed top-level OSCAL part names for catalog controls.
    """
    overview = PermissibleValue(text="overview")
    statement = PermissibleValue(text="statement")
    guidance = PermissibleValue(text="guidance")
    example = PermissibleValue(text="example")
    assessment = PermissibleValue(text="assessment")

    _defn = EnumDefinition(
        name="ControlPartNameEnum",
        description="Allowed top-level OSCAL part names for catalog controls.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "assessment-method",
            PermissibleValue(text="assessment-method"))

class ControlStatementPartSubpartNameEnum(EnumDefinitionImpl):
    """
    Allowed OSCAL subpart names for control statement parts.
    """
    item = PermissibleValue(text="item")

    _defn = EnumDefinition(
        name="ControlStatementPartSubpartNameEnum",
        description="Allowed OSCAL subpart names for control statement parts.",
    )

class ControlStatementPartNameEnum(EnumDefinitionImpl):
    """
    Allowed OSCAL part names for control statement parts.
    """
    objective = PermissibleValue(text="objective")

    _defn = EnumDefinition(
        name="ControlStatementPartNameEnum",
        description="Allowed OSCAL part names for control statement parts.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "assessment-objective",
            PermissibleValue(text="assessment-objective"))

class ControlObjectivePartSubpartNameEnum(EnumDefinitionImpl):
    """
    Allowed OSCAL subpart names for control objective parts.
    """
    objects = PermissibleValue(text="objects")

    _defn = EnumDefinition(
        name="ControlObjectivePartSubpartNameEnum",
        description="Allowed OSCAL subpart names for control objective parts.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "assessment-objects",
            PermissibleValue(text="assessment-objects"))

class ControlStatementPartPropNameEnum(EnumDefinitionImpl):
    """
    Allowed OSCAL property names for control statement parts.
    """
    method = PermissibleValue(text="method")

    _defn = EnumDefinition(
        name="ControlStatementPartPropNameEnum",
        description="Allowed OSCAL property names for control statement parts.",
    )

class ControlStatementPartRmfPropNameEnum(EnumDefinitionImpl):
    """
    Allowed OSCAL RMF property names for control statement parts.
    """
    method = PermissibleValue(text="method")

    _defn = EnumDefinition(
        name="ControlStatementPartRmfPropNameEnum",
        description="Allowed OSCAL RMF property names for control statement parts.",
    )

class ControlObjectivePartMethodPropValueEnum(EnumDefinitionImpl):
    """
    Allowed OSCAL method property values for control objectives.
    """
    INTERVIEW = PermissibleValue(text="INTERVIEW")
    EXAMINE = PermissibleValue(text="EXAMINE")
    TEST = PermissibleValue(text="TEST")

    _defn = EnumDefinition(
        name="ControlObjectivePartMethodPropValueEnum",
        description="Allowed OSCAL method property values for control objectives.",
    )

class WithChildControlsEnum(EnumDefinitionImpl):

    yes = PermissibleValue(text="yes")
    no = PermissibleValue(text="no")

    _defn = EnumDefinition(
        name="WithChildControlsEnum",
    )

class InsertOrderEnum(EnumDefinitionImpl):
    """
    Ordering options for a selection of controls.
    """
    keep = PermissibleValue(text="keep")
    ascending = PermissibleValue(text="ascending")
    descending = PermissibleValue(text="descending")

    _defn = EnumDefinition(
        name="InsertOrderEnum",
        description="Ordering options for a selection of controls.",
    )

class AdditionPositionEnum(EnumDefinitionImpl):
    """
    Where new content is added relative to the targeted element.
    """
    before = PermissibleValue(text="before")
    after = PermissibleValue(text="after")
    starting = PermissibleValue(text="starting")
    ending = PermissibleValue(text="ending")

    _defn = EnumDefinition(
        name="AdditionPositionEnum",
        description="Where new content is added relative to the targeted element.",
    )

class ByItemNameEnum(EnumDefinitionImpl):
    """
    Identifies content to remove by the item's object type name.
    """
    param = PermissibleValue(text="param")
    prop = PermissibleValue(text="prop")
    link = PermissibleValue(text="link")
    part = PermissibleValue(text="part")
    mapping = PermissibleValue(text="mapping")
    map = PermissibleValue(text="map")

    _defn = EnumDefinition(
        name="ByItemNameEnum",
        description="Identifies content to remove by the item's object type name.",
    )

class CombinationMethodEnum(EnumDefinitionImpl):
    """
    Methods for resolving duplicate control instances during merge.
    """
    merge = PermissibleValue(text="merge")
    keep = PermissibleValue(text="keep")

    _defn = EnumDefinition(
        name="CombinationMethodEnum",
        description="Methods for resolving duplicate control instances during merge.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "use-first",
            PermissibleValue(text="use-first"))

class AlterationPropNameEnum(EnumDefinitionImpl):
    """
    Allowed OSCAL property names for profile modification additions.
    """
    label = PermissibleValue(text="label")

    _defn = EnumDefinition(
        name="AlterationPropNameEnum",
        description="Allowed OSCAL property names for profile modification additions.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "sort-id",
            PermissibleValue(text="sort-id"))
        setattr(cls, "alt-identifier",
            PermissibleValue(text="alt-identifier"))

class SystemOperatingStatusEnum(EnumDefinitionImpl):
    """
    Allowable operational states for an OSCAL-described system.
    """
    operational = PermissibleValue(
        text="operational",
        description="The system is currently operating in production.")
    disposition = PermissibleValue(
        text="disposition",
        description="The system is no longer operational.")
    other = PermissibleValue(
        text="other",
        description="Some other state.")

    _defn = EnumDefinition(
        name="SystemOperatingStatusEnum",
        description="Allowable operational states for an OSCAL-described system.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "under-development",
            PermissibleValue(
                text="under-development",
                description="The system is being designed, developed, or implemented."))
        setattr(cls, "under-major-modification",
            PermissibleValue(
                text="under-major-modification",
                description="The system is undergoing a major change, development, or transition."))

class SystemCharacteristicsPropNameEnum(EnumDefinitionImpl):
    """
    OSCAL-defined property names used within system characteristics.
    """
    _defn = EnumDefinition(
        name="SystemCharacteristicsPropNameEnum",
        description="OSCAL-defined property names used within system characteristics.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "identity-assurance-level",
            PermissibleValue(text="identity-assurance-level"))
        setattr(cls, "authenticator-assurance-level",
            PermissibleValue(text="authenticator-assurance-level"))
        setattr(cls, "federation-assurance-level",
            PermissibleValue(text="federation-assurance-level"))
        setattr(cls, "cloud-deployment-model",
            PermissibleValue(text="cloud-deployment-model"))
        setattr(cls, "cloud-service-model",
            PermissibleValue(text="cloud-service-model"))

class AssuranceLevelValueEnum(EnumDefinitionImpl):
    """
    NIST SP 800-63 assurance level values.
    """
    _defn = EnumDefinition(
        name="AssuranceLevelValueEnum",
        description="NIST SP 800-63 assurance level values.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "1",
            PermissibleValue(text="1"))
        setattr(cls, "2",
            PermissibleValue(text="2"))
        setattr(cls, "3",
            PermissibleValue(text="3"))

class CloudDeploymentModelEnum(EnumDefinitionImpl):
    """
    Cloud deployment model values used by OSCAL SSP properties.
    """
    other = PermissibleValue(text="other")

    _defn = EnumDefinition(
        name="CloudDeploymentModelEnum",
        description="Cloud deployment model values used by OSCAL SSP properties.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "public-cloud",
            PermissibleValue(text="public-cloud"))
        setattr(cls, "private-cloud",
            PermissibleValue(text="private-cloud"))
        setattr(cls, "community-cloud",
            PermissibleValue(text="community-cloud"))
        setattr(cls, "hybrid-cloud",
            PermissibleValue(text="hybrid-cloud"))
        setattr(cls, "government-only-cloud",
            PermissibleValue(text="government-only-cloud"))

class CloudServiceModelEnum(EnumDefinitionImpl):
    """
    Cloud service model values used by OSCAL SSP properties.
    """
    saas = PermissibleValue(text="saas")
    paas = PermissibleValue(text="paas")
    iaas = PermissibleValue(text="iaas")
    other = PermissibleValue(text="other")

    _defn = EnumDefinition(
        name="CloudServiceModelEnum",
        description="Cloud service model values used by OSCAL SSP properties.",
    )

class SystemCharacteristicsResponsibleRoleIdEnum(EnumDefinitionImpl):
    """
    Curated role identifiers for system characteristics responsible parties. Other values are permitted (OSCAL
    allow-other="yes").
    """
    _defn = EnumDefinition(
        name="SystemCharacteristicsResponsibleRoleIdEnum",
        description="""Curated role identifiers for system characteristics responsible parties. Other values are permitted (OSCAL allow-other=\"yes\").""",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "authorizing-official",
            PermissibleValue(text="authorizing-official"))
        setattr(cls, "authorizing-official-poc",
            PermissibleValue(text="authorizing-official-poc"))
        setattr(cls, "system-owner",
            PermissibleValue(text="system-owner"))
        setattr(cls, "system-poc-management",
            PermissibleValue(text="system-poc-management"))
        setattr(cls, "system-poc-technical",
            PermissibleValue(text="system-poc-technical"))
        setattr(cls, "system-poc-other",
            PermissibleValue(text="system-poc-other"))
        setattr(cls, "information-system-security-officer",
            PermissibleValue(text="information-system-security-officer"))
        setattr(cls, "privacy-poc",
            PermissibleValue(text="privacy-poc"))

class InformationTypeCategorizationSystemEnum(EnumDefinitionImpl):
    """
    Curated information type categorization system URIs. Other values are permitted (OSCAL allow-other="yes").
    """
    _defn = EnumDefinition(
        name="InformationTypeCategorizationSystemEnum",
        description="""Curated information type categorization system URIs. Other values are permitted (OSCAL allow-other=\"yes\").""",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "http://doi.org/10.6028/NIST.SP.800-60v2r1",
            PermissibleValue(text="http://doi.org/10.6028/NIST.SP.800-60v2r1"))

class SystemInformationPropNameEnum(EnumDefinitionImpl):
    """
    OSCAL-defined property names used within system information.
    """
    _defn = EnumDefinition(
        name="SystemInformationPropNameEnum",
        description="OSCAL-defined property names used within system information.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "privacy-designation",
            PermissibleValue(text="privacy-designation"))

class PrivacyDesignationEnum(EnumDefinitionImpl):
    """
    Privacy designation property values.
    """
    yes = PermissibleValue(text="yes")
    no = PermissibleValue(text="no")

    _defn = EnumDefinition(
        name="PrivacyDesignationEnum",
        description="Privacy designation property values.",
    )

class SystemInformationLinkRelEnum(EnumDefinitionImpl):
    """
    Curated relation values for links in system information. Other values are permitted (OSCAL allow-other="yes").
    """
    _defn = EnumDefinition(
        name="SystemInformationLinkRelEnum",
        description="""Curated relation values for links in system information. Other values are permitted (OSCAL allow-other=\"yes\").""",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "privacy-impact-assessment",
            PermissibleValue(text="privacy-impact-assessment"))

class Fips199ImpactLevelEnum(EnumDefinitionImpl):
    """
    Curated FIPS 199 impact level values. Other values are permitted (OSCAL allow-other="yes").
    """
    _defn = EnumDefinition(
        name="Fips199ImpactLevelEnum",
        description="Curated FIPS 199 impact level values. Other values are permitted (OSCAL allow-other=\"yes\").",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "fips-199-low",
            PermissibleValue(text="fips-199-low"))
        setattr(cls, "fips-199-moderate",
            PermissibleValue(text="fips-199-moderate"))
        setattr(cls, "fips-199-high",
            PermissibleValue(text="fips-199-high"))

class DiagramLinkRelEnum(EnumDefinitionImpl):
    """
    Curated relation values for links in diagram objects. Other values are permitted (OSCAL allow-other="yes").
    """
    diagram = PermissibleValue(text="diagram")

    _defn = EnumDefinition(
        name="DiagramLinkRelEnum",
        description="""Curated relation values for links in diagram objects. Other values are permitted (OSCAL allow-other=\"yes\").""",
    )

class LeveragedAuthorizationLinkRelEnum(EnumDefinitionImpl):
    """
    Curated relation values for links in leveraged authorization objects. Other values are permitted (OSCAL
    allow-other="yes").
    """
    _defn = EnumDefinition(
        name="LeveragedAuthorizationLinkRelEnum",
        description="""Curated relation values for links in leveraged authorization objects. Other values are permitted (OSCAL allow-other=\"yes\").""",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "system-security-plan",
            PermissibleValue(text="system-security-plan"))

class AllowsAuthenticatedScanEnum(EnumDefinitionImpl):
    """
    Values for allows-authenticated-scan property in SSP component and inventory contexts.
    """
    yes = PermissibleValue(text="yes")
    no = PermissibleValue(text="no")

    _defn = EnumDefinition(
        name="AllowsAuthenticatedScanEnum",
        description="Values for allows-authenticated-scan property in SSP component and inventory contexts.",
    )

class ControlOriginationPropNameEnum(EnumDefinitionImpl):
    """
    OSCAL-defined property names used in implementation statements.
    """
    _defn = EnumDefinition(
        name="ControlOriginationPropNameEnum",
        description="OSCAL-defined property names used in implementation statements.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "control-origination",
            PermissibleValue(text="control-origination"))

class ControlOriginationValueEnum(EnumDefinitionImpl):
    """
    Control origination values.
    """
    organization = PermissibleValue(text="organization")
    inherited = PermissibleValue(text="inherited")

    _defn = EnumDefinition(
        name="ControlOriginationValueEnum",
        description="Control origination values.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "system-specific",
            PermissibleValue(text="system-specific"))
        setattr(cls, "customer-configured",
            PermissibleValue(text="customer-configured"))
        setattr(cls, "customer-provided",
            PermissibleValue(text="customer-provided"))

class ImplementedRequirementResponsibleRoleIdEnum(EnumDefinitionImpl):
    """
    Curated role identifiers for implemented requirement and statement responsible roles. Other values are permitted
    (OSCAL allow-other="yes").
    """
    _defn = EnumDefinition(
        name="ImplementedRequirementResponsibleRoleIdEnum",
        description="""Curated role identifiers for implemented requirement and statement responsible roles. Other values are permitted (OSCAL allow-other=\"yes\").""",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "asset-owner",
            PermissibleValue(text="asset-owner"))
        setattr(cls, "asset-administrator",
            PermissibleValue(text="asset-administrator"))
        setattr(cls, "security-operations",
            PermissibleValue(text="security-operations"))
        setattr(cls, "network-operations",
            PermissibleValue(text="network-operations"))
        setattr(cls, "incident-response",
            PermissibleValue(text="incident-response"))
        setattr(cls, "help-desk",
            PermissibleValue(text="help-desk"))
        setattr(cls, "configuration-management",
            PermissibleValue(text="configuration-management"))

class ByComponentLinkRelEnum(EnumDefinitionImpl):
    """
    Curated relation values for links in by-component objects. Other values are permitted (OSCAL allow-other="yes").
    """
    _defn = EnumDefinition(
        name="ByComponentLinkRelEnum",
        description="""Curated relation values for links in by-component objects. Other values are permitted (OSCAL allow-other=\"yes\").""",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "imported-from",
            PermissibleValue(text="imported-from"))
        setattr(cls, "provided-by",
            PermissibleValue(text="provided-by"))

class ByComponentResponsibleRoleIdEnum(EnumDefinitionImpl):
    """
    Curated role identifiers for by-component responsible roles. Other values are permitted (OSCAL allow-other="yes").
    """
    maintainer = PermissibleValue(text="maintainer")
    provider = PermissibleValue(text="provider")

    _defn = EnumDefinition(
        name="ByComponentResponsibleRoleIdEnum",
        description="""Curated role identifiers for by-component responsible roles. Other values are permitted (OSCAL allow-other=\"yes\").""",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "asset-owner",
            PermissibleValue(text="asset-owner"))
        setattr(cls, "asset-administrator",
            PermissibleValue(text="asset-administrator"))
        setattr(cls, "security-operations",
            PermissibleValue(text="security-operations"))
        setattr(cls, "network-operations",
            PermissibleValue(text="network-operations"))
        setattr(cls, "incident-response",
            PermissibleValue(text="incident-response"))
        setattr(cls, "help-desk",
            PermissibleValue(text="help-desk"))
        setattr(cls, "configuration-management",
            PermissibleValue(text="configuration-management"))

class TaskTypeEnum(EnumDefinitionImpl):
    """
    Curated task type values. Other values are permitted (OSCAL allow-other="yes").
    """
    milestone = PermissibleValue(text="milestone")
    action = PermissibleValue(text="action")

    _defn = EnumDefinition(
        name="TaskTypeEnum",
        description="""Curated task type values. Other values are permitted (OSCAL allow-other=\"yes\").""",
    )

class TimingUnitEnum(EnumDefinitionImpl):

    seconds = PermissibleValue(text="seconds")
    minutes = PermissibleValue(text="minutes")
    hours = PermissibleValue(text="hours")
    days = PermissibleValue(text="days")
    months = PermissibleValue(text="months")
    years = PermissibleValue(text="years")

    _defn = EnumDefinition(
        name="TimingUnitEnum",
    )

class AssessmentSubjectTypeEnum(EnumDefinitionImpl):
    """
    Curated assessment subject type values. Other values are permitted (OSCAL allow-other="yes").
    """
    component = PermissibleValue(text="component")
    location = PermissibleValue(text="location")
    party = PermissibleValue(text="party")
    user = PermissibleValue(text="user")

    _defn = EnumDefinition(
        name="AssessmentSubjectTypeEnum",
        description="""Curated assessment subject type values. Other values are permitted (OSCAL allow-other=\"yes\").""",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "inventory-item",
            PermissibleValue(text="inventory-item"))

class SelectSubjectTypeEnum(EnumDefinitionImpl):
    """
    Curated subject type values for subject selection. Other values are permitted (OSCAL allow-other="yes").
    """
    component = PermissibleValue(text="component")
    location = PermissibleValue(text="location")
    party = PermissibleValue(text="party")
    user = PermissibleValue(text="user")
    resource = PermissibleValue(text="resource")

    _defn = EnumDefinition(
        name="SelectSubjectTypeEnum",
        description="""Curated subject type values for subject selection. Other values are permitted (OSCAL allow-other=\"yes\").""",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "inventory-item",
            PermissibleValue(text="inventory-item"))

class OriginActorTypeEnum(EnumDefinitionImpl):

    tool = PermissibleValue(text="tool")
    party = PermissibleValue(text="party")

    _defn = EnumDefinition(
        name="OriginActorTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "assessment-platform",
            PermissibleValue(text="assessment-platform"))

class ObservationMethodEnum(EnumDefinitionImpl):
    """
    Curated observation method values. Other values are permitted (OSCAL allow-other="yes").
    """
    EXAMINE = PermissibleValue(text="EXAMINE")
    INTERVIEW = PermissibleValue(text="INTERVIEW")
    TEST = PermissibleValue(text="TEST")
    UNKNOWN = PermissibleValue(text="UNKNOWN")

    _defn = EnumDefinition(
        name="ObservationMethodEnum",
        description="""Curated observation method values. Other values are permitted (OSCAL allow-other=\"yes\").""",
    )

class ObservationTypeEnum(EnumDefinitionImpl):
    """
    Curated observation type values. Other values are permitted (OSCAL allow-other="yes").
    """
    mitigation = PermissibleValue(text="mitigation")
    finding = PermissibleValue(text="finding")
    discovery = PermissibleValue(text="discovery")
    historic = PermissibleValue(text="historic")

    _defn = EnumDefinition(
        name="ObservationTypeEnum",
        description="""Curated observation type values. Other values are permitted (OSCAL allow-other=\"yes\").""",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "ssp-statement-issue",
            PermissibleValue(text="ssp-statement-issue"))
        setattr(cls, "control-objective",
            PermissibleValue(text="control-objective"))

class RiskStatusEnum(EnumDefinitionImpl):
    """
    Curated risk status values. Other values are permitted (OSCAL allow-other="yes").
    """
    open = PermissibleValue(text="open")
    investigating = PermissibleValue(text="investigating")
    remediating = PermissibleValue(text="remediating")
    closed = PermissibleValue(text="closed")

    _defn = EnumDefinition(
        name="RiskStatusEnum",
        description="""Curated risk status values. Other values are permitted (OSCAL allow-other=\"yes\").""",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "deviation-requested",
            PermissibleValue(text="deviation-requested"))
        setattr(cls, "deviation-approved",
            PermissibleValue(text="deviation-approved"))

class FindingTargetTypeEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="FindingTargetTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "statement-id",
            PermissibleValue(text="statement-id"))
        setattr(cls, "objective-id",
            PermissibleValue(text="objective-id"))

class ObjectiveStatusStateEnum(EnumDefinitionImpl):

    satisfied = PermissibleValue(text="satisfied")

    _defn = EnumDefinition(
        name="ObjectiveStatusStateEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "not-satisfied",
            PermissibleValue(text="not-satisfied"))

class ObjectiveStatusReasonEnum(EnumDefinitionImpl):
    """
    Curated objective status reason values. Other values are permitted (OSCAL allow-other="yes").
    """
    fail = PermissibleValue(text="fail")
    other = PermissibleValue(text="other")

    _defn = EnumDefinition(
        name="ObjectiveStatusReasonEnum",
        description="""Curated objective status reason values. Other values are permitted (OSCAL allow-other=\"yes\").""",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "pass",
            PermissibleValue(text="pass"))

class ImplementationStatusStateEnum(EnumDefinitionImpl):
    """
    Curated implementation status state values. Other values are permitted (OSCAL allow-other="yes").
    """
    implemented = PermissibleValue(text="implemented")
    partial = PermissibleValue(text="partial")
    planned = PermissibleValue(text="planned")
    alternative = PermissibleValue(text="alternative")

    _defn = EnumDefinition(
        name="ImplementationStatusStateEnum",
        description="""Curated implementation status state values. Other values are permitted (OSCAL allow-other=\"yes\").""",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "not-applicable",
            PermissibleValue(text="not-applicable"))

class ComponentTypeEnum(EnumDefinitionImpl):
    """
    Curated component type values. Other values are permitted (OSCAL allow-other="yes").
    """
    system = PermissibleValue(text="system")
    interconnection = PermissibleValue(text="interconnection")
    software = PermissibleValue(text="software")
    hardware = PermissibleValue(text="hardware")
    service = PermissibleValue(text="service")
    policy = PermissibleValue(text="policy")
    physical = PermissibleValue(text="physical")
    plan = PermissibleValue(text="plan")
    guidance = PermissibleValue(text="guidance")
    standard = PermissibleValue(text="standard")
    validation = PermissibleValue(text="validation")
    network = PermissibleValue(text="network")

    _defn = EnumDefinition(
        name="ComponentTypeEnum",
        description="""Curated component type values. Other values are permitted (OSCAL allow-other=\"yes\").""",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "this-system",
            PermissibleValue(text="this-system"))
        setattr(cls, "process-procedure",
            PermissibleValue(text="process-procedure"))

class ComponentStateEnum(EnumDefinitionImpl):

    operational = PermissibleValue(text="operational")
    disposition = PermissibleValue(text="disposition")
    other = PermissibleValue(text="other")

    _defn = EnumDefinition(
        name="ComponentStateEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "under-development",
            PermissibleValue(text="under-development"))

class TransportEnum(EnumDefinitionImpl):

    TCP = PermissibleValue(text="TCP")
    UDP = PermissibleValue(text="UDP")

    _defn = EnumDefinition(
        name="TransportEnum",
    )

class ImplementationPropNameEnum(EnumDefinitionImpl):
    """
    Allowed OSCAL implementation-common property names.
    """
    public = PermissibleValue(text="public")
    virtual = PermissibleValue(text="virtual")
    label = PermissibleValue(text="label")
    function = PermissibleValue(text="function")
    model = PermissibleValue(text="model")
    version = PermissibleValue(text="version")
    direction = PermissibleValue(text="direction")
    uri = PermissibleValue(text="uri")
    fqdn = PermissibleValue(text="fqdn")
    type = PermissibleValue(text="type")

    _defn = EnumDefinition(
        name="ImplementationPropNameEnum",
        description="Allowed OSCAL implementation-common property names.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "implementation-point",
            PermissibleValue(text="implementation-point"))
        setattr(cls, "leveraged-authorization-uuid",
            PermissibleValue(text="leveraged-authorization-uuid"))
        setattr(cls, "inherited-uuid",
            PermissibleValue(text="inherited-uuid"))
        setattr(cls, "asset-type",
            PermissibleValue(text="asset-type"))
        setattr(cls, "asset-id",
            PermissibleValue(text="asset-id"))
        setattr(cls, "asset-tag",
            PermissibleValue(text="asset-tag"))
        setattr(cls, "vlan-id",
            PermissibleValue(text="vlan-id"))
        setattr(cls, "network-id",
            PermissibleValue(text="network-id"))
        setattr(cls, "sort-id",
            PermissibleValue(text="sort-id"))
        setattr(cls, "baseline-configuration-name",
            PermissibleValue(text="baseline-configuration-name"))
        setattr(cls, "allows-authenticated-scan",
            PermissibleValue(text="allows-authenticated-scan"))
        setattr(cls, "hardware-model",
            PermissibleValue(text="hardware-model"))
        setattr(cls, "os-name",
            PermissibleValue(text="os-name"))
        setattr(cls, "os-version",
            PermissibleValue(text="os-version"))
        setattr(cls, "software-name",
            PermissibleValue(text="software-name"))
        setattr(cls, "software-version",
            PermissibleValue(text="software-version"))
        setattr(cls, "software-patch-level",
            PermissibleValue(text="software-patch-level"))
        setattr(cls, "patch-level",
            PermissibleValue(text="patch-level"))
        setattr(cls, "release-date",
            PermissibleValue(text="release-date"))
        setattr(cls, "validation-type",
            PermissibleValue(text="validation-type"))
        setattr(cls, "validation-reference",
            PermissibleValue(text="validation-reference"))
        setattr(cls, "vendor-name",
            PermissibleValue(text="vendor-name"))
        setattr(cls, "software-identifier",
            PermissibleValue(text="software-identifier"))
        setattr(cls, "isa-title",
            PermissibleValue(text="isa-title"))
        setattr(cls, "isa-date",
            PermissibleValue(text="isa-date"))
        setattr(cls, "isa-remote-system-name",
            PermissibleValue(text="isa-remote-system-name"))
        setattr(cls, "ipv4-address",
            PermissibleValue(text="ipv4-address"))
        setattr(cls, "ipv6-address",
            PermissibleValue(text="ipv6-address"))
        setattr(cls, "serial-number",
            PermissibleValue(text="serial-number"))
        setattr(cls, "netbios-name",
            PermissibleValue(text="netbios-name"))
        setattr(cls, "mac-address",
            PermissibleValue(text="mac-address"))
        setattr(cls, "physical-location",
            PermissibleValue(text="physical-location"))
        setattr(cls, "is-scanned",
            PermissibleValue(text="is-scanned"))
        setattr(cls, "privilege-level",
            PermissibleValue(text="privilege-level"))

class ImplementationLinkRelEnum(EnumDefinitionImpl):
    """
    Curated implementation-common link relation values. Other values are permitted (OSCAL allow-other="yes").
    """
    validation = PermissibleValue(text="validation")

    _defn = EnumDefinition(
        name="ImplementationLinkRelEnum",
        description="""Curated implementation-common link relation values. Other values are permitted (OSCAL allow-other=\"yes\").""",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "depends-on",
            PermissibleValue(text="depends-on"))
        setattr(cls, "proof-of-compliance",
            PermissibleValue(text="proof-of-compliance"))
        setattr(cls, "baseline-template",
            PermissibleValue(text="baseline-template"))
        setattr(cls, "uses-service",
            PermissibleValue(text="uses-service"))
        setattr(cls, "system-security-plan",
            PermissibleValue(text="system-security-plan"))
        setattr(cls, "uses-network",
            PermissibleValue(text="uses-network"))
        setattr(cls, "imported-from",
            PermissibleValue(text="imported-from"))
        setattr(cls, "validation-details",
            PermissibleValue(text="validation-details"))
        setattr(cls, "provided-by",
            PermissibleValue(text="provided-by"))
        setattr(cls, "used-by",
            PermissibleValue(text="used-by"))
        setattr(cls, "isa-agreement",
            PermissibleValue(text="isa-agreement"))

class ImplementationAssetTypeEnum(EnumDefinitionImpl):
    """
    Curated implementation asset type values. Other values are permitted (OSCAL allow-other="yes").
    """
    database = PermissibleValue(text="database")
    pbx = PermissibleValue(text="pbx")
    firewall = PermissibleValue(text="firewall")
    router = PermissibleValue(text="router")
    switch = PermissibleValue(text="switch")
    appliance = PermissibleValue(text="appliance")

    _defn = EnumDefinition(
        name="ImplementationAssetTypeEnum",
        description="Curated implementation asset type values. Other values are permitted (OSCAL allow-other=\"yes\").",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "operating-system",
            PermissibleValue(text="operating-system"))
        setattr(cls, "web-server",
            PermissibleValue(text="web-server"))
        setattr(cls, "dns-server",
            PermissibleValue(text="dns-server"))
        setattr(cls, "email-server",
            PermissibleValue(text="email-server"))
        setattr(cls, "directory-server",
            PermissibleValue(text="directory-server"))
        setattr(cls, "storage-array",
            PermissibleValue(text="storage-array"))

class ImplementationPointEnum(EnumDefinitionImpl):

    internal = PermissibleValue(text="internal")
    external = PermissibleValue(text="external")

    _defn = EnumDefinition(
        name="ImplementationPointEnum",
    )

class ImplementationIpAddressClassEnum(EnumDefinitionImpl):

    local = PermissibleValue(text="local")
    remote = PermissibleValue(text="remote")

    _defn = EnumDefinition(
        name="ImplementationIpAddressClassEnum",
    )

class ImplementationDirectionEnum(EnumDefinitionImpl):

    incoming = PermissibleValue(text="incoming")
    outgoing = PermissibleValue(text="outgoing")

    _defn = EnumDefinition(
        name="ImplementationDirectionEnum",
    )

class UserTypeEnum(EnumDefinitionImpl):

    internal = PermissibleValue(text="internal")
    external = PermissibleValue(text="external")

    _defn = EnumDefinition(
        name="UserTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "general-public",
            PermissibleValue(text="general-public"))

class UserPrivilegeLevelEnum(EnumDefinitionImpl):

    privileged = PermissibleValue(text="privileged")

    _defn = EnumDefinition(
        name="UserPrivilegeLevelEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "non-privileged",
            PermissibleValue(text="non-privileged"))
        setattr(cls, "no-logical-access",
            PermissibleValue(text="no-logical-access"))

class InterconnectionResponsibleRoleIdEnum(EnumDefinitionImpl):
    """
    Curated interconnection responsible-role identifiers. Other values are permitted (OSCAL allow-other="yes").
    """
    _defn = EnumDefinition(
        name="InterconnectionResponsibleRoleIdEnum",
        description="""Curated interconnection responsible-role identifiers. Other values are permitted (OSCAL allow-other=\"yes\").""",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "isa-poc-local",
            PermissibleValue(text="isa-poc-local"))
        setattr(cls, "isa-poc-remote",
            PermissibleValue(text="isa-poc-remote"))
        setattr(cls, "isa-authorizing-official-local",
            PermissibleValue(text="isa-authorizing-official-local"))
        setattr(cls, "isa-authorizing-official-remote",
            PermissibleValue(text="isa-authorizing-official-remote"))

class ImplementationResponsibleRoleIdEnum(EnumDefinitionImpl):
    """
    Curated implementation-common role identifiers used in responsible role and responsible party contexts. Other
    values are permitted (OSCAL allow-other="yes").
    """
    maintainer = PermissibleValue(text="maintainer")
    provider = PermissibleValue(text="provider")

    _defn = EnumDefinition(
        name="ImplementationResponsibleRoleIdEnum",
        description="""Curated implementation-common role identifiers used in responsible role and responsible party contexts. Other values are permitted (OSCAL allow-other=\"yes\").""",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "asset-owner",
            PermissibleValue(text="asset-owner"))
        setattr(cls, "asset-administrator",
            PermissibleValue(text="asset-administrator"))
        setattr(cls, "security-operations",
            PermissibleValue(text="security-operations"))
        setattr(cls, "network-operations",
            PermissibleValue(text="network-operations"))
        setattr(cls, "incident-response",
            PermissibleValue(text="incident-response"))
        setattr(cls, "help-desk",
            PermissibleValue(text="help-desk"))
        setattr(cls, "configuration-management",
            PermissibleValue(text="configuration-management"))

class ImplementationYesNoEnum(EnumDefinitionImpl):
    """
    Implementation-common yes/no value set used by several properties.
    """
    yes = PermissibleValue(text="yes")
    no = PermissibleValue(text="no")

    _defn = EnumDefinition(
        name="ImplementationYesNoEnum",
        description="Implementation-common yes/no value set used by several properties.",
    )

class SystemIdentifierTypeEnum(EnumDefinitionImpl):
    """
    Curated system identifier type URIs. Other values are permitted (OSCAL allow-other="yes").
    """
    _defn = EnumDefinition(
        name="SystemIdentifierTypeEnum",
        description="Curated system identifier type URIs. Other values are permitted (OSCAL allow-other=\"yes\").",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "http://fedramp.gov",
            PermissibleValue(text="http://fedramp.gov"))
        setattr(cls, "http://fedramp.gov/ns/oscal",
            PermissibleValue(text="http://fedramp.gov/ns/oscal"))
        setattr(cls, "https://ietf.org/rfc/rfc4122",
            PermissibleValue(text="https://ietf.org/rfc/rfc4122"))
        setattr(cls, "http://ietf.org/rfc/rfc4122",
            PermissibleValue(text="http://ietf.org/rfc/rfc4122"))
        setattr(cls, "http://datatracker.ietf.org/doc/html/rfc4122",
            PermissibleValue(text="http://datatracker.ietf.org/doc/html/rfc4122"))

class AssessmentPartNameEnum(EnumDefinitionImpl):
    """
    Curated assessment part name values. Other values are permitted (OSCAL allow-other="yes").
    """
    asset = PermissibleValue(text="asset")
    method = PermissibleValue(text="method")
    objective = PermissibleValue(text="objective")

    _defn = EnumDefinition(
        name="AssessmentPartNameEnum",
        description="""Curated assessment part name values. Other values are permitted (OSCAL allow-other=\"yes\").""",
    )

class TermsAndConditionsPartNameEnum(EnumDefinitionImpl):
    """
    Allowed part names in assessment plan terms-and-conditions.
    """
    disclosures = PermissibleValue(text="disclosures")
    assumptions = PermissibleValue(text="assumptions")
    methodology = PermissibleValue(text="methodology")

    _defn = EnumDefinition(
        name="TermsAndConditionsPartNameEnum",
        description="Allowed part names in assessment plan terms-and-conditions.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "rules-of-engagement",
            PermissibleValue(text="rules-of-engagement"))
        setattr(cls, "assessment-inclusions",
            PermissibleValue(text="assessment-inclusions"))
        setattr(cls, "assessment-exclusions",
            PermissibleValue(text="assessment-exclusions"))
        setattr(cls, "results-delivery",
            PermissibleValue(text="results-delivery"))

class OscalAssessmentObjectiveTypesEnum(EnumDefinitionImpl):
    """
    Values from assessment-common set oscal-assessment-objective-types.
    """
    objective = PermissibleValue(text="objective")
    assessment = PermissibleValue(text="assessment")

    _defn = EnumDefinition(
        name="OscalAssessmentObjectiveTypesEnum",
        description="Values from assessment-common set oscal-assessment-objective-types.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "assessment-objective",
            PermissibleValue(text="assessment-objective"))
        setattr(cls, "assessment-method",
            PermissibleValue(text="assessment-method"))

class OscalRiskPropTypeValuesEnum(EnumDefinitionImpl):
    """
    Values from assessment-common set oscal-risk-prop-type-values.
    """
    mitigation = PermissibleValue(text="mitigation")
    remediated = PermissibleValue(text="remediated")
    closed = PermissibleValue(text="closed")

    _defn = EnumDefinition(
        name="OscalRiskPropTypeValuesEnum",
        description="Values from assessment-common set oscal-risk-prop-type-values.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "vendor-check-in",
            PermissibleValue(text="vendor-check-in"))
        setattr(cls, "status-update",
            PermissibleValue(text="status-update"))
        setattr(cls, "milestone-complete",
            PermissibleValue(text="milestone-complete"))
        setattr(cls, "dr-submission",
            PermissibleValue(text="dr-submission"))
        setattr(cls, "dr-updated",
            PermissibleValue(text="dr-updated"))
        setattr(cls, "dr-approved",
            PermissibleValue(text="dr-approved"))
        setattr(cls, "dr-rejected",
            PermissibleValue(text="dr-rejected"))

class OscalRiskPropNameValuesEnum(EnumDefinitionImpl):
    """
    Values from assessment-common set oscal-risk-prop-name-values.
    """
    accepted = PermissibleValue(text="accepted")
    priority = PermissibleValue(text="priority")

    _defn = EnumDefinition(
        name="OscalRiskPropNameValuesEnum",
        description="Values from assessment-common set oscal-risk-prop-name-values.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "false-positive",
            PermissibleValue(text="false-positive"))
        setattr(cls, "risk-adjusted",
            PermissibleValue(text="risk-adjusted"))

class OscalCharacterizationFacetNameSystemValuesEnum(EnumDefinitionImpl):
    """
    Values from assessment-common set oscal-characterization-facet-name-system-values.
    """
    _defn = EnumDefinition(
        name="OscalCharacterizationFacetNameSystemValuesEnum",
        description="Values from assessment-common set oscal-characterization-facet-name-system-values.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "http://fedramp.gov",
            PermissibleValue(text="http://fedramp.gov"))
        setattr(cls, "http://fedramp.gov/ns/oscal",
            PermissibleValue(text="http://fedramp.gov/ns/oscal"))
        setattr(cls, "http://csrc.nist.gov/ns/oscal",
            PermissibleValue(text="http://csrc.nist.gov/ns/oscal"))
        setattr(cls, "http://csrc.nist.gov/ns/oscal/unknown",
            PermissibleValue(text="http://csrc.nist.gov/ns/oscal/unknown"))
        setattr(cls, "http://cve.mitre.org",
            PermissibleValue(text="http://cve.mitre.org"))
        setattr(cls, "http://www.first.org/cvss/v2.0",
            PermissibleValue(text="http://www.first.org/cvss/v2.0"))
        setattr(cls, "http://www.first.org/cvss/v3.0",
            PermissibleValue(text="http://www.first.org/cvss/v3.0"))
        setattr(cls, "http://www.first.org/cvss/v3.1",
            PermissibleValue(text="http://www.first.org/cvss/v3.1"))
        setattr(cls, "https://www.first.org/cvss/v4-0",
            PermissibleValue(text="https://www.first.org/cvss/v4-0"))

class OscalFacetPropNameValuesEnum(EnumDefinitionImpl):
    """
    Values from assessment-common set oscal-facet-prop-name-values.
    """
    state = PermissibleValue(text="state")

    _defn = EnumDefinition(
        name="OscalFacetPropNameValuesEnum",
        description="Values from assessment-common set oscal-facet-prop-name-values.",
    )

class OscalFacetPropStateValuesEnum(EnumDefinitionImpl):
    """
    Values from assessment-common set oscal-facet-prop-state-values.
    """
    initial = PermissibleValue(text="initial")
    adjusted = PermissibleValue(text="adjusted")

    _defn = EnumDefinition(
        name="OscalFacetPropStateValuesEnum",
        description="Values from assessment-common set oscal-facet-prop-state-values.",
    )

class OscalFacetNameCoreValuesEnum(EnumDefinitionImpl):
    """
    Values from assessment-common set oscal-facet-name-core-values.
    """
    likelihood = PermissibleValue(text="likelihood")
    impact = PermissibleValue(text="impact")
    risk = PermissibleValue(text="risk")
    severity = PermissibleValue(text="severity")

    _defn = EnumDefinition(
        name="OscalFacetNameCoreValuesEnum",
        description="Values from assessment-common set oscal-facet-name-core-values.",
    )

class OscalFacetFedrampValuesEnum(EnumDefinitionImpl):
    """
    Values from assessment-common set oscal-facet-fedramp-values.
    """
    likelihood = PermissibleValue(text="likelihood")
    impact = PermissibleValue(text="impact")
    risk = PermissibleValue(text="risk")

    _defn = EnumDefinition(
        name="OscalFacetFedrampValuesEnum",
        description="Values from assessment-common set oscal-facet-fedramp-values.",
    )

class OscalFacetCveValuesEnum(EnumDefinitionImpl):
    """
    Values from assessment-common set oscal-facet-cve-values.
    """
    _defn = EnumDefinition(
        name="OscalFacetCveValuesEnum",
        description="Values from assessment-common set oscal-facet-cve-values.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "cve-id",
            PermissibleValue(text="cve-id"))

class OscalFacetCvss2NameValuesEnum(EnumDefinitionImpl):
    """
    Values from assessment-common set oscal-facet-cvss2-name-values.
    """
    authentication = PermissibleValue(text="authentication")
    exploitability = PermissibleValue(text="exploitability")

    _defn = EnumDefinition(
        name="OscalFacetCvss2NameValuesEnum",
        description="Values from assessment-common set oscal-facet-cvss2-name-values.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "access-vector",
            PermissibleValue(text="access-vector"))
        setattr(cls, "access-complexity",
            PermissibleValue(text="access-complexity"))
        setattr(cls, "confidentiality-impact",
            PermissibleValue(text="confidentiality-impact"))
        setattr(cls, "integrity-impact",
            PermissibleValue(text="integrity-impact"))
        setattr(cls, "availability-impact",
            PermissibleValue(text="availability-impact"))
        setattr(cls, "remediation-level",
            PermissibleValue(text="remediation-level"))
        setattr(cls, "report-confidence",
            PermissibleValue(text="report-confidence"))
        setattr(cls, "collateral-damage-potential",
            PermissibleValue(text="collateral-damage-potential"))
        setattr(cls, "target-distribution",
            PermissibleValue(text="target-distribution"))
        setattr(cls, "confidentiality-requirement",
            PermissibleValue(text="confidentiality-requirement"))
        setattr(cls, "integrity-requirement",
            PermissibleValue(text="integrity-requirement"))
        setattr(cls, "availability-requirement",
            PermissibleValue(text="availability-requirement"))

class OscalFacetCvss2AccessVectorValuesEnum(EnumDefinitionImpl):
    """
    Values from assessment-common set oscal-facet-cvss2-access-vector-values.
    """
    local = PermissibleValue(text="local")
    network = PermissibleValue(text="network")

    _defn = EnumDefinition(
        name="OscalFacetCvss2AccessVectorValuesEnum",
        description="Values from assessment-common set oscal-facet-cvss2-access-vector-values.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "adjacent-network",
            PermissibleValue(text="adjacent-network"))

class OscalFacetCvss2AccessComplexityValuesEnum(EnumDefinitionImpl):
    """
    Values from assessment-common set oscal-facet-cvss2-access-complexity-values.
    """
    high = PermissibleValue(text="high")
    medium = PermissibleValue(text="medium")
    low = PermissibleValue(text="low")

    _defn = EnumDefinition(
        name="OscalFacetCvss2AccessComplexityValuesEnum",
        description="Values from assessment-common set oscal-facet-cvss2-access-complexity-values.",
    )

class OscalFacetCvss2AuthenticationValuesEnum(EnumDefinitionImpl):
    """
    Values from assessment-common set oscal-facet-cvss2-authentication-values.
    """
    multiple = PermissibleValue(text="multiple")
    single = PermissibleValue(text="single")
    none = PermissibleValue(text="none")

    _defn = EnumDefinition(
        name="OscalFacetCvss2AuthenticationValuesEnum",
        description="Values from assessment-common set oscal-facet-cvss2-authentication-values.",
    )

class OscalFacetCvss2ConfidentialityImpactValuesEnum(EnumDefinitionImpl):
    """
    Values from assessment-common set oscal-facet-cvss2-confidentiality-impact-values.
    """
    none = PermissibleValue(text="none")
    partial = PermissibleValue(text="partial")
    complete = PermissibleValue(text="complete")

    _defn = EnumDefinition(
        name="OscalFacetCvss2ConfidentialityImpactValuesEnum",
        description="Values from assessment-common set oscal-facet-cvss2-confidentiality-impact-values.",
    )

class OscalFacetCvss2ExploitabilityValuesEnum(EnumDefinitionImpl):
    """
    Values from assessment-common set oscal-facet-cvss2-exploitability-values.
    """
    unproven = PermissibleValue(text="unproven")
    functional = PermissibleValue(text="functional")
    high = PermissibleValue(text="high")

    _defn = EnumDefinition(
        name="OscalFacetCvss2ExploitabilityValuesEnum",
        description="Values from assessment-common set oscal-facet-cvss2-exploitability-values.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "proof-of-concept",
            PermissibleValue(text="proof-of-concept"))
        setattr(cls, "not-defined",
            PermissibleValue(text="not-defined"))

class OscalFacetCvss2RemediationLevelValuesEnum(EnumDefinitionImpl):
    """
    Values from assessment-common set oscal-facet-cvss2-remediation-level-values.
    """
    workaround = PermissibleValue(text="workaround")
    unavailable = PermissibleValue(text="unavailable")

    _defn = EnumDefinition(
        name="OscalFacetCvss2RemediationLevelValuesEnum",
        description="Values from assessment-common set oscal-facet-cvss2-remediation-level-values.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "official-fix",
            PermissibleValue(text="official-fix"))
        setattr(cls, "temporary-fix",
            PermissibleValue(text="temporary-fix"))
        setattr(cls, "not-defined",
            PermissibleValue(text="not-defined"))

class OscalFacetCvss2ReportConfidenceValuesEnum(EnumDefinitionImpl):
    """
    Values from assessment-common set oscal-facet-cvss2-report-confidence-values.
    """
    unconfirmed = PermissibleValue(text="unconfirmed")
    uncorroborated = PermissibleValue(text="uncorroborated")
    confirmed = PermissibleValue(text="confirmed")

    _defn = EnumDefinition(
        name="OscalFacetCvss2ReportConfidenceValuesEnum",
        description="Values from assessment-common set oscal-facet-cvss2-report-confidence-values.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "not-defined",
            PermissibleValue(text="not-defined"))

class OscalFacetCvss2CollateralDamagePotentialValuesEnum(EnumDefinitionImpl):
    """
    Values from assessment-common set oscal-facet-cvss2-collateral-damage-potential-values.
    """
    none = PermissibleValue(text="none")
    low = PermissibleValue(text="low")
    high = PermissibleValue(text="high")

    _defn = EnumDefinition(
        name="OscalFacetCvss2CollateralDamagePotentialValuesEnum",
        description="Values from assessment-common set oscal-facet-cvss2-collateral-damage-potential-values.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "low-medium",
            PermissibleValue(text="low-medium"))
        setattr(cls, "medium-high",
            PermissibleValue(text="medium-high"))
        setattr(cls, "not-defined",
            PermissibleValue(text="not-defined"))

class OscalFacetCvss2CiaRequirementValuesEnum(EnumDefinitionImpl):
    """
    Values from assessment-common set oscal-facet-cvss2-cia-requirement-values.
    """
    none = PermissibleValue(text="none")
    low = PermissibleValue(text="low")
    medium = PermissibleValue(text="medium")
    high = PermissibleValue(text="high")

    _defn = EnumDefinition(
        name="OscalFacetCvss2CiaRequirementValuesEnum",
        description="Values from assessment-common set oscal-facet-cvss2-cia-requirement-values.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "not-defined",
            PermissibleValue(text="not-defined"))

class OscalFacetCvss3NameValuesEnum(EnumDefinitionImpl):
    """
    Values from assessment-common set oscal-facet-cvss3-name-values.
    """
    scope = PermissibleValue(text="scope")

    _defn = EnumDefinition(
        name="OscalFacetCvss3NameValuesEnum",
        description="Values from assessment-common set oscal-facet-cvss3-name-values.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "attack-vector",
            PermissibleValue(text="attack-vector"))
        setattr(cls, "access-complexity",
            PermissibleValue(text="access-complexity"))
        setattr(cls, "privileges-required",
            PermissibleValue(text="privileges-required"))
        setattr(cls, "user-interaction",
            PermissibleValue(text="user-interaction"))
        setattr(cls, "confidentiality-impact",
            PermissibleValue(text="confidentiality-impact"))
        setattr(cls, "integrity-impact",
            PermissibleValue(text="integrity-impact"))
        setattr(cls, "availability-impact",
            PermissibleValue(text="availability-impact"))
        setattr(cls, "exploit-code-maturity",
            PermissibleValue(text="exploit-code-maturity"))
        setattr(cls, "remediation-level",
            PermissibleValue(text="remediation-level"))
        setattr(cls, "report-confidence",
            PermissibleValue(text="report-confidence"))
        setattr(cls, "modified-attack-vector",
            PermissibleValue(text="modified-attack-vector"))
        setattr(cls, "modified-attack-complexity",
            PermissibleValue(text="modified-attack-complexity"))
        setattr(cls, "modified-privileges-required",
            PermissibleValue(text="modified-privileges-required"))
        setattr(cls, "modified-user-interaction",
            PermissibleValue(text="modified-user-interaction"))
        setattr(cls, "modified-scope",
            PermissibleValue(text="modified-scope"))
        setattr(cls, "modified-confidentiality",
            PermissibleValue(text="modified-confidentiality"))
        setattr(cls, "modified-integrity",
            PermissibleValue(text="modified-integrity"))
        setattr(cls, "modified-availability",
            PermissibleValue(text="modified-availability"))
        setattr(cls, "confidentiality-requirement",
            PermissibleValue(text="confidentiality-requirement"))
        setattr(cls, "integrity-requirement",
            PermissibleValue(text="integrity-requirement"))
        setattr(cls, "availability-requirement",
            PermissibleValue(text="availability-requirement"))

class OscalFacetCvss3AccessVectorValuesEnum(EnumDefinitionImpl):
    """
    Values from assessment-common set oscal-facet-cvss3-access-vector-values.
    """
    network = PermissibleValue(text="network")
    adjacent = PermissibleValue(text="adjacent")
    local = PermissibleValue(text="local")
    physical = PermissibleValue(text="physical")

    _defn = EnumDefinition(
        name="OscalFacetCvss3AccessVectorValuesEnum",
        description="Values from assessment-common set oscal-facet-cvss3-access-vector-values.",
    )

class OscalFacetCvss3AccessComplexityValuesEnum(EnumDefinitionImpl):
    """
    Values from assessment-common set oscal-facet-cvss3-access-complexity-values.
    """
    high = PermissibleValue(text="high")
    low = PermissibleValue(text="low")

    _defn = EnumDefinition(
        name="OscalFacetCvss3AccessComplexityValuesEnum",
        description="Values from assessment-common set oscal-facet-cvss3-access-complexity-values.",
    )

class OscalFacetCvss3CiaImpactValuesEnum(EnumDefinitionImpl):
    """
    Values from assessment-common set oscal-facet-cvss3-cia-impact-values.
    """
    none = PermissibleValue(text="none")
    low = PermissibleValue(text="low")
    high = PermissibleValue(text="high")

    _defn = EnumDefinition(
        name="OscalFacetCvss3CiaImpactValuesEnum",
        description="Values from assessment-common set oscal-facet-cvss3-cia-impact-values.",
    )

class OscalFacetCvss3UserInteractionEnum(EnumDefinitionImpl):
    """
    Values from assessment-common set oscal-facet-cvss3-user-interaction.
    """
    none = PermissibleValue(text="none")
    required = PermissibleValue(text="required")

    _defn = EnumDefinition(
        name="OscalFacetCvss3UserInteractionEnum",
        description="Values from assessment-common set oscal-facet-cvss3-user-interaction.",
    )

class OscalFacetCvss3ScopeEnum(EnumDefinitionImpl):
    """
    Values from assessment-common set oscal-facet-cvss3-scope.
    """
    unchanged = PermissibleValue(text="unchanged")
    changed = PermissibleValue(text="changed")

    _defn = EnumDefinition(
        name="OscalFacetCvss3ScopeEnum",
        description="Values from assessment-common set oscal-facet-cvss3-scope.",
    )

class OscalFacetCvss3ExploitCodeMaturityValuesEnum(EnumDefinitionImpl):
    """
    Values from assessment-common set oscal-facet-cvss3-exploit-code-maturity-values.
    """
    unproven = PermissibleValue(text="unproven")
    functional = PermissibleValue(text="functional")
    high = PermissibleValue(text="high")

    _defn = EnumDefinition(
        name="OscalFacetCvss3ExploitCodeMaturityValuesEnum",
        description="Values from assessment-common set oscal-facet-cvss3-exploit-code-maturity-values.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "not-defined",
            PermissibleValue(text="not-defined"))
        setattr(cls, "proof-of-concept",
            PermissibleValue(text="proof-of-concept"))

class OscalFacetCvss3RemediationLevelEnum(EnumDefinitionImpl):
    """
    Values from assessment-common set oscal-facet-cvss3-remediation-level.
    """
    workaround = PermissibleValue(text="workaround")
    unavailable = PermissibleValue(text="unavailable")

    _defn = EnumDefinition(
        name="OscalFacetCvss3RemediationLevelEnum",
        description="Values from assessment-common set oscal-facet-cvss3-remediation-level.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "not-defined",
            PermissibleValue(text="not-defined"))
        setattr(cls, "official-fix",
            PermissibleValue(text="official-fix"))
        setattr(cls, "temporary-fix",
            PermissibleValue(text="temporary-fix"))

class OscalFacetCvss3ReportConfidenceValuesEnum(EnumDefinitionImpl):
    """
    Values from assessment-common set oscal-facet-cvss3-report-confidence-values.
    """
    unknown = PermissibleValue(text="unknown")
    reasonable = PermissibleValue(text="reasonable")
    confirmed = PermissibleValue(text="confirmed")

    _defn = EnumDefinition(
        name="OscalFacetCvss3ReportConfidenceValuesEnum",
        description="Values from assessment-common set oscal-facet-cvss3-report-confidence-values.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "not-defined",
            PermissibleValue(text="not-defined"))

class OscalFacetCvss3CiaRequirementValuesEnum(EnumDefinitionImpl):
    """
    Values from assessment-common set oscal-facet-cvss3-cia-requirement-values.
    """
    low = PermissibleValue(text="low")
    medium = PermissibleValue(text="medium")
    high = PermissibleValue(text="high")

    _defn = EnumDefinition(
        name="OscalFacetCvss3CiaRequirementValuesEnum",
        description="Values from assessment-common set oscal-facet-cvss3-cia-requirement-values.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "not-defined",
            PermissibleValue(text="not-defined"))

class OscalFacetCvss3ModifiedAttackVectorValuesEnum(EnumDefinitionImpl):
    """
    Values from assessment-common set oscal-facet-cvss3-modified-attack-vector-values.
    """
    network = PermissibleValue(text="network")
    adjacent = PermissibleValue(text="adjacent")
    local = PermissibleValue(text="local")
    physical = PermissibleValue(text="physical")

    _defn = EnumDefinition(
        name="OscalFacetCvss3ModifiedAttackVectorValuesEnum",
        description="Values from assessment-common set oscal-facet-cvss3-modified-attack-vector-values.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "not-defined",
            PermissibleValue(text="not-defined"))

class OscalFacetCvss3ModifiedAttackComplexityValuesEnum(EnumDefinitionImpl):
    """
    Values from assessment-common set oscal-facet-cvss3-modified-attack-complexity-values.
    """
    high = PermissibleValue(text="high")
    low = PermissibleValue(text="low")

    _defn = EnumDefinition(
        name="OscalFacetCvss3ModifiedAttackComplexityValuesEnum",
        description="Values from assessment-common set oscal-facet-cvss3-modified-attack-complexity-values.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "not-defined",
            PermissibleValue(text="not-defined"))

class OscalFacetCvss3ModifiedCiaValuesEnum(EnumDefinitionImpl):
    """
    Values from assessment-common set oscal-facet-cvss3-modified-cia-values.
    """
    none = PermissibleValue(text="none")
    low = PermissibleValue(text="low")
    high = PermissibleValue(text="high")

    _defn = EnumDefinition(
        name="OscalFacetCvss3ModifiedCiaValuesEnum",
        description="Values from assessment-common set oscal-facet-cvss3-modified-cia-values.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "not-defined",
            PermissibleValue(text="not-defined"))

class OscalFacetCvss3ModifiedUserInteractionValuesEnum(EnumDefinitionImpl):
    """
    Values from assessment-common set oscal-facet-cvss3-modified-user-interaction-values.
    """
    none = PermissibleValue(text="none")
    required = PermissibleValue(text="required")

    _defn = EnumDefinition(
        name="OscalFacetCvss3ModifiedUserInteractionValuesEnum",
        description="Values from assessment-common set oscal-facet-cvss3-modified-user-interaction-values.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "not-defined",
            PermissibleValue(text="not-defined"))

class OscalFacetCvss3ModifiedScopeValuesEnum(EnumDefinitionImpl):
    """
    Values from assessment-common set oscal-facet-cvss3-modified-scope-values.
    """
    unchanged = PermissibleValue(text="unchanged")
    changed = PermissibleValue(text="changed")

    _defn = EnumDefinition(
        name="OscalFacetCvss3ModifiedScopeValuesEnum",
        description="Values from assessment-common set oscal-facet-cvss3-modified-scope-values.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "not-defined",
            PermissibleValue(text="not-defined"))

class OscalCvssV40VectorsEnum(EnumDefinitionImpl):
    """
    Values from assessment-common set oscal-cvss-v4.0-vectors.
    """
    av = PermissibleValue(text="av")
    ac = PermissibleValue(text="ac")
    at = PermissibleValue(text="at")
    pr = PermissibleValue(text="pr")
    ui = PermissibleValue(text="ui")
    vc = PermissibleValue(text="vc")
    vi = PermissibleValue(text="vi")
    va = PermissibleValue(text="va")
    sc = PermissibleValue(text="sc")
    si = PermissibleValue(text="si")
    sa = PermissibleValue(text="sa")
    s = PermissibleValue(text="s")
    au = PermissibleValue(text="au")
    r = PermissibleValue(text="r")
    v = PermissibleValue(text="v")
    re = PermissibleValue(text="re")
    u = PermissibleValue(text="u")
    mav = PermissibleValue(text="mav")
    mac = PermissibleValue(text="mac")
    mat = PermissibleValue(text="mat")
    mpr = PermissibleValue(text="mpr")
    mui = PermissibleValue(text="mui")
    mvc = PermissibleValue(text="mvc")
    mvi = PermissibleValue(text="mvi")
    mva = PermissibleValue(text="mva")
    msc = PermissibleValue(text="msc")
    msi = PermissibleValue(text="msi")
    msa = PermissibleValue(text="msa")
    cr = PermissibleValue(text="cr")
    ir = PermissibleValue(text="ir")
    ar = PermissibleValue(text="ar")
    e = PermissibleValue(text="e")

    _defn = EnumDefinition(
        name="OscalCvssV40VectorsEnum",
        description="Values from assessment-common set oscal-cvss-v4.0-vectors.",
    )

class OscalCvssV40AvValuesEnum(EnumDefinitionImpl):
    """
    Values from assessment-common set oscal-cvss-v4.0-av-values.
    """
    n = PermissibleValue(text="n")
    a = PermissibleValue(text="a")
    l = PermissibleValue(text="l")
    p = PermissibleValue(text="p")

    _defn = EnumDefinition(
        name="OscalCvssV40AvValuesEnum",
        description="Values from assessment-common set oscal-cvss-v4.0-av-values.",
    )

class OscalCvssV40AcValuesEnum(EnumDefinitionImpl):
    """
    Values from assessment-common set oscal-cvss-v4.0-ac-values.
    """
    h = PermissibleValue(text="h")
    l = PermissibleValue(text="l")

    _defn = EnumDefinition(
        name="OscalCvssV40AcValuesEnum",
        description="Values from assessment-common set oscal-cvss-v4.0-ac-values.",
    )

class OscalCvssV40AtValuesEnum(EnumDefinitionImpl):
    """
    Values from assessment-common set oscal-cvss-v4.0-at-values.
    """
    n = PermissibleValue(text="n")
    p = PermissibleValue(text="p")

    _defn = EnumDefinition(
        name="OscalCvssV40AtValuesEnum",
        description="Values from assessment-common set oscal-cvss-v4.0-at-values.",
    )

class OscalCvssV40PrCiaValuesEnum(EnumDefinitionImpl):
    """
    Values from assessment-common set oscal-cvss-v4.0-pr-cia-values.
    """
    n = PermissibleValue(text="n")
    l = PermissibleValue(text="l")
    h = PermissibleValue(text="h")

    _defn = EnumDefinition(
        name="OscalCvssV40PrCiaValuesEnum",
        description="Values from assessment-common set oscal-cvss-v4.0-pr-cia-values.",
    )

class OscalCvssV40UiValuesEnum(EnumDefinitionImpl):
    """
    Values from assessment-common set oscal-cvss-v4.0-ui-values.
    """
    n = PermissibleValue(text="n")
    p = PermissibleValue(text="p")
    a = PermissibleValue(text="a")

    _defn = EnumDefinition(
        name="OscalCvssV40UiValuesEnum",
        description="Values from assessment-common set oscal-cvss-v4.0-ui-values.",
    )

class OscalCvssV40SValuesEnum(EnumDefinitionImpl):
    """
    Values from assessment-common set oscal-cvss-v4.0-s-values.
    """
    x = PermissibleValue(text="x")
    n = PermissibleValue(text="n")
    p = PermissibleValue(text="p")

    _defn = EnumDefinition(
        name="OscalCvssV40SValuesEnum",
        description="Values from assessment-common set oscal-cvss-v4.0-s-values.",
    )

class OscalCvssV40AuValuesEnum(EnumDefinitionImpl):
    """
    Values from assessment-common set oscal-cvss-v4.0-au-values.
    """
    x = PermissibleValue(text="x")
    n = PermissibleValue(text="n")
    y = PermissibleValue(text="y")

    _defn = EnumDefinition(
        name="OscalCvssV40AuValuesEnum",
        description="Values from assessment-common set oscal-cvss-v4.0-au-values.",
    )

class OscalCvssV40RValuesEnum(EnumDefinitionImpl):
    """
    Values from assessment-common set oscal-cvss-v4.0-r-values.
    """
    x = PermissibleValue(text="x")
    a = PermissibleValue(text="a")
    u = PermissibleValue(text="u")
    i = PermissibleValue(text="i")

    _defn = EnumDefinition(
        name="OscalCvssV40RValuesEnum",
        description="Values from assessment-common set oscal-cvss-v4.0-r-values.",
    )

class OscalCvssV40VValuesEnum(EnumDefinitionImpl):
    """
    Values from assessment-common set oscal-cvss-v4.0-v-values.
    """
    x = PermissibleValue(text="x")
    a = PermissibleValue(text="a")
    u = PermissibleValue(text="u")
    i = PermissibleValue(text="i")

    _defn = EnumDefinition(
        name="OscalCvssV40VValuesEnum",
        description="Values from assessment-common set oscal-cvss-v4.0-v-values.",
    )

class OscalCvssV40ReValuesEnum(EnumDefinitionImpl):
    """
    Values from assessment-common set oscal-cvss-v4.0-re-values.
    """
    x = PermissibleValue(text="x")
    l = PermissibleValue(text="l")
    m = PermissibleValue(text="m")
    h = PermissibleValue(text="h")

    _defn = EnumDefinition(
        name="OscalCvssV40ReValuesEnum",
        description="Values from assessment-common set oscal-cvss-v4.0-re-values.",
    )

class OscalCvssV40UValuesEnum(EnumDefinitionImpl):
    """
    Values from assessment-common set oscal-cvss-v4.0-u-values.
    """
    x = PermissibleValue(text="x")
    clear = PermissibleValue(text="clear")
    green = PermissibleValue(text="green")
    amber = PermissibleValue(text="amber")
    red = PermissibleValue(text="red")

    _defn = EnumDefinition(
        name="OscalCvssV40UValuesEnum",
        description="Values from assessment-common set oscal-cvss-v4.0-u-values.",
    )

class OscalCvssV40MavValuesEnum(EnumDefinitionImpl):
    """
    Values from assessment-common set oscal-cvss-v4.0-mav-values.
    """
    x = PermissibleValue(text="x")
    n = PermissibleValue(text="n")
    a = PermissibleValue(text="a")
    l = PermissibleValue(text="l")
    p = PermissibleValue(text="p")

    _defn = EnumDefinition(
        name="OscalCvssV40MavValuesEnum",
        description="Values from assessment-common set oscal-cvss-v4.0-mav-values.",
    )

class OscalCvssV40MacValuesEnum(EnumDefinitionImpl):
    """
    Values from assessment-common set oscal-cvss-v4.0-mac-values.
    """
    x = PermissibleValue(text="x")
    h = PermissibleValue(text="h")
    l = PermissibleValue(text="l")

    _defn = EnumDefinition(
        name="OscalCvssV40MacValuesEnum",
        description="Values from assessment-common set oscal-cvss-v4.0-mac-values.",
    )

class OscalCvssV40MatValuesEnum(EnumDefinitionImpl):
    """
    Values from assessment-common set oscal-cvss-v4.0-mat-values.
    """
    x = PermissibleValue(text="x")
    n = PermissibleValue(text="n")
    p = PermissibleValue(text="p")

    _defn = EnumDefinition(
        name="OscalCvssV40MatValuesEnum",
        description="Values from assessment-common set oscal-cvss-v4.0-mat-values.",
    )

class OscalCvssV40MprMvsCiaValuesEnum(EnumDefinitionImpl):
    """
    Values from assessment-common set oscal-cvss-v4.0-mpr-mvs-cia-values.
    """
    x = PermissibleValue(text="x")
    n = PermissibleValue(text="n")
    l = PermissibleValue(text="l")
    h = PermissibleValue(text="h")

    _defn = EnumDefinition(
        name="OscalCvssV40MprMvsCiaValuesEnum",
        description="Values from assessment-common set oscal-cvss-v4.0-mpr-mvs-cia-values.",
    )

class OscalCvssV40MuiValuesEnum(EnumDefinitionImpl):
    """
    Values from assessment-common set oscal-cvss-v4.0-mui-values.
    """
    x = PermissibleValue(text="x")
    n = PermissibleValue(text="n")
    p = PermissibleValue(text="p")
    a = PermissibleValue(text="a")

    _defn = EnumDefinition(
        name="OscalCvssV40MuiValuesEnum",
        description="Values from assessment-common set oscal-cvss-v4.0-mui-values.",
    )

class OscalCvssV40MscValuesEnum(EnumDefinitionImpl):
    """
    Values from assessment-common set oscal-cvss-v4.0-msc-values.
    """
    x = PermissibleValue(text="x")
    n = PermissibleValue(text="n")
    l = PermissibleValue(text="l")
    h = PermissibleValue(text="h")

    _defn = EnumDefinition(
        name="OscalCvssV40MscValuesEnum",
        description="Values from assessment-common set oscal-cvss-v4.0-msc-values.",
    )

class OscalCvssV40MsiMsaCiaValuesEnum(EnumDefinitionImpl):
    """
    Values from assessment-common set oscal-cvss-v4.0-msi-msa-cia-values.
    """
    x = PermissibleValue(text="x")
    n = PermissibleValue(text="n")
    l = PermissibleValue(text="l")
    h = PermissibleValue(text="h")
    s = PermissibleValue(text="s")

    _defn = EnumDefinition(
        name="OscalCvssV40MsiMsaCiaValuesEnum",
        description="Values from assessment-common set oscal-cvss-v4.0-msi-msa-cia-values.",
    )

class OscalCvssV40EnvCiaValuesEnum(EnumDefinitionImpl):
    """
    Values from assessment-common set oscal-cvss-v4.0-env-cia-values.
    """
    x = PermissibleValue(text="x")
    l = PermissibleValue(text="l")
    m = PermissibleValue(text="m")
    h = PermissibleValue(text="h")

    _defn = EnumDefinition(
        name="OscalCvssV40EnvCiaValuesEnum",
        description="Values from assessment-common set oscal-cvss-v4.0-env-cia-values.",
    )

class OscalCvssV40EValuesEnum(EnumDefinitionImpl):
    """
    Values from assessment-common set oscal-cvss-v4.0-e-values.
    """
    x = PermissibleValue(text="x")
    a = PermissibleValue(text="a")
    p = PermissibleValue(text="p")
    u = PermissibleValue(text="u")

    _defn = EnumDefinition(
        name="OscalCvssV40EValuesEnum",
        description="Values from assessment-common set oscal-cvss-v4.0-e-values.",
    )

class OscalResponsePropTypeValueEnum(EnumDefinitionImpl):
    """
    Values from assessment-common set oscal-response-prop-type-value.
    """
    avoid = PermissibleValue(text="avoid")
    mitigate = PermissibleValue(text="mitigate")
    transfer = PermissibleValue(text="transfer")
    accept = PermissibleValue(text="accept")
    share = PermissibleValue(text="share")
    contingency = PermissibleValue(text="contingency")
    none = PermissibleValue(text="none")

    _defn = EnumDefinition(
        name="OscalResponsePropTypeValueEnum",
        description="Values from assessment-common set oscal-response-prop-type-value.",
    )

class ResponseLifecycleEnum(EnumDefinitionImpl):
    """
    Curated response lifecycle values. Other values are permitted (OSCAL allow-other="yes").
    """
    recommendation = PermissibleValue(text="recommendation")
    planned = PermissibleValue(text="planned")
    completed = PermissibleValue(text="completed")

    _defn = EnumDefinition(
        name="ResponseLifecycleEnum",
        description="""Curated response lifecycle values. Other values are permitted (OSCAL allow-other=\"yes\").""",
    )

class MappingMethodEnum(EnumDefinitionImpl):

    human = PermissibleValue(text="human")
    automation = PermissibleValue(text="automation")
    hybrid = PermissibleValue(text="hybrid")

    _defn = EnumDefinition(
        name="MappingMethodEnum",
    )

class MatchingRationaleEnum(EnumDefinitionImpl):

    syntactic = PermissibleValue(text="syntactic")
    semantic = PermissibleValue(text="semantic")
    functional = PermissibleValue(text="functional")

    _defn = EnumDefinition(
        name="MatchingRationaleEnum",
    )

class MappingStatusEnum(EnumDefinitionImpl):

    complete = PermissibleValue(text="complete")
    draft = PermissibleValue(text="draft")
    deprecated = PermissibleValue(text="deprecated")
    superseded = PermissibleValue(text="superseded")

    _defn = EnumDefinition(
        name="MappingStatusEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "not-complete",
            PermissibleValue(text="not-complete"))

class MappingSubjectTypeEnum(EnumDefinitionImpl):

    control = PermissibleValue(text="control")
    statement = PermissibleValue(text="statement")

    _defn = EnumDefinition(
        name="MappingSubjectTypeEnum",
    )

class QualifierSubjectEnum(EnumDefinitionImpl):

    source = PermissibleValue(text="source")
    target = PermissibleValue(text="target")
    both = PermissibleValue(text="both")

    _defn = EnumDefinition(
        name="QualifierSubjectEnum",
    )

class QualifierPredicateEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="QualifierPredicateEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "has-requirement",
            PermissibleValue(text="has-requirement"))
        setattr(cls, "has-incompatibility",
            PermissibleValue(text="has-incompatibility"))

class QualifierCategoryEnum(EnumDefinitionImpl):

    restricted = PermissibleValue(text="restricted")
    addressable = PermissibleValue(text="addressable")
    blocked = PermissibleValue(text="blocked")

    _defn = EnumDefinition(
        name="QualifierCategoryEnum",
    )

class RelationshipEnum(EnumDefinitionImpl):
    """
    Relationship values used for mapping entries in the OSCAL namespace.
    """
    _defn = EnumDefinition(
        name="RelationshipEnum",
        description="Relationship values used for mapping entries in the OSCAL namespace.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "equivalent-to",
            PermissibleValue(text="equivalent-to"))
        setattr(cls, "equal-to",
            PermissibleValue(text="equal-to"))
        setattr(cls, "subset-of",
            PermissibleValue(text="subset-of"))
        setattr(cls, "superset-of",
            PermissibleValue(text="superset-of"))
        setattr(cls, "intersects-with",
            PermissibleValue(text="intersects-with"))
        setattr(cls, "no-relationship",
            PermissibleValue(text="no-relationship"))

class MappingResourceTypeEnum(EnumDefinitionImpl):
    """
    Curated mapped resource type values. Other values are permitted (OSCAL allow-other="yes").
    """
    catalog = PermissibleValue(text="catalog")
    profile = PermissibleValue(text="profile")

    _defn = EnumDefinition(
        name="MappingResourceTypeEnum",
        description="Curated mapped resource type values. Other values are permitted (OSCAL allow-other=\"yes\").",
    )

class ConfidenceCategoryEnum(EnumDefinitionImpl):
    """
    Curated confidence category values for OSCAL mappings. Other values are permitted (OSCAL allow-other="yes").
    """
    unspecified = PermissibleValue(text="unspecified")
    high = PermissibleValue(text="high")
    medium = PermissibleValue(text="medium")
    low = PermissibleValue(text="low")

    _defn = EnumDefinition(
        name="ConfidenceCategoryEnum",
        description="""Curated confidence category values for OSCAL mappings. Other values are permitted (OSCAL allow-other=\"yes\").""",
    )

class CoverageGenerationMethodEnum(EnumDefinitionImpl):
    """
    Curated coverage generation method values. Other values are permitted (OSCAL allow-other="yes").
    """
    arbitrary = PermissibleValue(text="arbitrary")

    _defn = EnumDefinition(
        name="CoverageGenerationMethodEnum",
        description="Curated coverage generation method values. Other values are permitted (OSCAL allow-other=\"yes\").",
    )

# Slots
class slots:
    pass

slots.uuid = Slot(uri=OSCAL_CATALOG.uuid, name="uuid", curie=OSCAL_CATALOG.curie('uuid'),
                   model_uri=OSCAL.uuid, domain=None, range=Optional[str])

slots.title = Slot(uri=OSCAL_CATALOG.title, name="title", curie=OSCAL_CATALOG.curie('title'),
                   model_uri=OSCAL.title, domain=None, range=Optional[str])

slots.description = Slot(uri=OSCAL_CATALOG.description, name="description", curie=OSCAL_CATALOG.curie('description'),
                   model_uri=OSCAL.description, domain=None, range=Optional[str])

slots.set_parameters = Slot(uri=OSCAL_CATALOG.set_parameters, name="set-parameters", curie=OSCAL_CATALOG.curie('set_parameters'),
                   model_uri=OSCAL.set_parameters, domain=None, range=Optional[Union[str, list[str]]])

slots.remarks = Slot(uri=OSCAL_CATALOG.remarks, name="remarks", curie=OSCAL_CATALOG.curie('remarks'),
                   model_uri=OSCAL.remarks, domain=None, range=Optional[str])

slots.href = Slot(uri=OSCAL_CATALOG.href, name="href", curie=OSCAL_CATALOG.curie('href'),
                   model_uri=OSCAL.href, domain=None, range=Optional[str])

slots.props = Slot(uri=OSCAL_CATALOG.props, name="props", curie=OSCAL_CATALOG.curie('props'),
                   model_uri=OSCAL.props, domain=None, range=Optional[Union[Union[dict, Property], list[Union[dict, Property]]]])

slots.links = Slot(uri=OSCAL_CATALOG.links, name="links", curie=OSCAL_CATALOG.curie('links'),
                   model_uri=OSCAL.links, domain=None, range=Optional[Union[Union[dict, Link], list[Union[dict, Link]]]])

slots.responsible_roles = Slot(uri=OSCAL_CATALOG.responsible_roles, name="responsible-roles", curie=OSCAL_CATALOG.curie('responsible_roles'),
                   model_uri=OSCAL.responsible_roles, domain=None, range=Optional[Union[Union[dict, ResponsibleRole], list[Union[dict, ResponsibleRole]]]])

slots.responsible_parties = Slot(uri=OSCAL_CATALOG.responsible_parties, name="responsible-parties", curie=OSCAL_CATALOG.curie('responsible_parties'),
                   model_uri=OSCAL.responsible_parties, domain=None, range=Optional[Union[Union[dict, ResponsibleParty], list[Union[dict, ResponsibleParty]]]])

slots.id = Slot(uri=OSCAL_CATALOG.id, name="id", curie=OSCAL_CATALOG.curie('id'),
                   model_uri=OSCAL.id, domain=None, range=Optional[str])

slots._class = Slot(uri=OSCAL_CATALOG._class, name="_class", curie=OSCAL_CATALOG.curie('_class'),
                   model_uri=OSCAL._class, domain=None, range=Optional[str])

slots.name = Slot(uri=OSCAL_CATALOG.name, name="name", curie=OSCAL_CATALOG.curie('name'),
                   model_uri=OSCAL.name, domain=None, range=Optional[str])

slots.ns = Slot(uri=OSCAL_CATALOG.ns, name="ns", curie=OSCAL_CATALOG.curie('ns'),
                   model_uri=OSCAL.ns, domain=None, range=Optional[str])

slots.type = Slot(uri=OSCAL_CATALOG.type, name="type", curie=OSCAL_CATALOG.curie('type'),
                   model_uri=OSCAL.type, domain=None, range=Optional[str])

slots.value = Slot(uri=OSCAL_CATALOG.value, name="value", curie=OSCAL_CATALOG.curie('value'),
                   model_uri=OSCAL.value, domain=None, range=Optional[str])

slots.scheme = Slot(uri=OSCAL_CATALOG.scheme, name="scheme", curie=OSCAL_CATALOG.curie('scheme'),
                   model_uri=OSCAL.scheme, domain=None, range=Optional[str])

slots.role_id = Slot(uri=OSCAL_CATALOG.role_id, name="role-id", curie=OSCAL_CATALOG.curie('role_id'),
                   model_uri=OSCAL.role_id, domain=None, range=Optional[str])

slots.control_id = Slot(uri=OSCAL_CATALOG.control_id, name="control-id", curie=OSCAL_CATALOG.curie('control_id'),
                   model_uri=OSCAL.control_id, domain=None, range=Optional[str])

slots.include_all = Slot(uri=OSCAL_CATALOG.include_all, name="include-all", curie=OSCAL_CATALOG.curie('include_all'),
                   model_uri=OSCAL.include_all, domain=None, range=Optional[Union[dict, IncludeAll]])

slots.include_controls = Slot(uri=OSCAL_CATALOG.include_controls, name="include-controls", curie=OSCAL_CATALOG.curie('include_controls'),
                   model_uri=OSCAL.include_controls, domain=None, range=Optional[Union[str, list[str]]])

slots.exclude_controls = Slot(uri=OSCAL_CATALOG.exclude_controls, name="exclude-controls", curie=OSCAL_CATALOG.curie('exclude_controls'),
                   model_uri=OSCAL.exclude_controls, domain=None, range=Optional[Union[str, list[str]]])

slots.param_id = Slot(uri=OSCAL_CATALOG.param_id, name="param-id", curie=OSCAL_CATALOG.curie('param_id'),
                   model_uri=OSCAL.param_id, domain=None, range=Optional[str])

slots.statement_id = Slot(uri=OSCAL_CATALOG.statement_id, name="statement-id", curie=OSCAL_CATALOG.curie('statement_id'),
                   model_uri=OSCAL.statement_id, domain=None, range=Optional[str])

slots.implemented_requirements = Slot(uri=OSCAL_CATALOG.implemented_requirements, name="implemented-requirements", curie=OSCAL_CATALOG.curie('implemented_requirements'),
                   model_uri=OSCAL.implemented_requirements, domain=None, range=Optional[Union[str, list[str]]])

slots.statements = Slot(uri=OSCAL_CATALOG.statements, name="statements", curie=OSCAL_CATALOG.curie('statements'),
                   model_uri=OSCAL.statements, domain=None, range=Optional[Union[str, list[str]]])

slots.method = Slot(uri=OSCAL_CATALOG.method, name="method", curie=OSCAL_CATALOG.curie('method'),
                   model_uri=OSCAL.method, domain=None, range=Optional[str])

slots.status = Slot(uri=OSCAL_CATALOG.status, name="status", curie=OSCAL_CATALOG.curie('status'),
                   model_uri=OSCAL.status, domain=None, range=Optional[str])

slots.sources = Slot(uri=OSCAL_CATALOG.sources, name="sources", curie=OSCAL_CATALOG.curie('sources'),
                   model_uri=OSCAL.sources, domain=None, range=Optional[Union[str, list[str]]])

slots.party_uuids = Slot(uri=OSCAL_CATALOG.party_uuids, name="party-uuids", curie=OSCAL_CATALOG.curie('party_uuids'),
                   model_uri=OSCAL.party_uuids, domain=None, range=Optional[Union[str, list[str]]])

slots.email_addresses = Slot(uri=OSCAL_CATALOG.email_addresses, name="email-addresses", curie=OSCAL_CATALOG.curie('email_addresses'),
                   model_uri=OSCAL.email_addresses, domain=None, range=Optional[Union[str, list[str]]])

slots.telephone_numbers = Slot(uri=OSCAL_CATALOG.telephone_numbers, name="telephone-numbers", curie=OSCAL_CATALOG.curie('telephone_numbers'),
                   model_uri=OSCAL.telephone_numbers, domain=None, range=Optional[Union[Union[dict, TelephoneNumber], list[Union[dict, TelephoneNumber]]]])

slots.short_name = Slot(uri=OSCAL_CATALOG.short_name, name="short-name", curie=OSCAL_CATALOG.curie('short_name'),
                   model_uri=OSCAL.short_name, domain=None, range=Optional[str])

slots.published = Slot(uri=OSCAL_CATALOG.published, name="published", curie=OSCAL_CATALOG.curie('published'),
                   model_uri=OSCAL.published, domain=None, range=Optional[str])

slots.last_modified = Slot(uri=OSCAL_CATALOG.last_modified, name="last-modified", curie=OSCAL_CATALOG.curie('last_modified'),
                   model_uri=OSCAL.last_modified, domain=None, range=Optional[str])

slots.version = Slot(uri=OSCAL_CATALOG.version, name="version", curie=OSCAL_CATALOG.curie('version'),
                   model_uri=OSCAL.version, domain=None, range=Optional[str])

slots.oscal_version = Slot(uri=OSCAL_CATALOG.oscal_version, name="oscal-version", curie=OSCAL_CATALOG.curie('oscal_version'),
                   model_uri=OSCAL.oscal_version, domain=None, range=Optional[str])

slots.document_ids = Slot(uri=OSCAL_CATALOG.document_ids, name="document-ids", curie=OSCAL_CATALOG.curie('document_ids'),
                   model_uri=OSCAL.document_ids, domain=None, range=Optional[Union[Union[dict, DocumentId], list[Union[dict, DocumentId]]]])

slots.prose = Slot(uri=OSCAL_CATALOG.prose, name="prose", curie=OSCAL_CATALOG.curie('prose'),
                   model_uri=OSCAL.prose, domain=None, range=Optional[str])

slots.params = Slot(uri=OSCAL_CATALOG.params, name="params", curie=OSCAL_CATALOG.curie('params'),
                   model_uri=OSCAL.params, domain=None, range=Optional[Union[Union[dict, Parameter], list[Union[dict, Parameter]]]])

slots.controls = Slot(uri=OSCAL_CATALOG.controls, name="controls", curie=OSCAL_CATALOG.curie('controls'),
                   model_uri=OSCAL.controls, domain=None, range=Optional[Union[Union[dict, Control], list[Union[dict, Control]]]])

slots.groups = Slot(uri=OSCAL_CATALOG.groups, name="groups", curie=OSCAL_CATALOG.curie('groups'),
                   model_uri=OSCAL.groups, domain=None, range=Optional[Union[Union[dict, Group], list[Union[dict, Group]]]])

slots.parts = Slot(uri=OSCAL_CATALOG.parts, name="parts", curie=OSCAL_CATALOG.curie('parts'),
                   model_uri=OSCAL.parts, domain=None, range=Optional[Union[Union[dict, Part], list[Union[dict, Part]]]])

slots.media_type = Slot(uri=OSCAL_CATALOG.media_type, name="media-type", curie=OSCAL_CATALOG.curie('media_type'),
                   model_uri=OSCAL.media_type, domain=None, range=Optional[str])

slots.text = Slot(uri=OSCAL_CATALOG.text, name="text", curie=OSCAL_CATALOG.curie('text'),
                   model_uri=OSCAL.text, domain=None, range=Optional[str])

slots.how_many = Slot(uri=OSCAL_CATALOG.how_many, name="how-many", curie=OSCAL_CATALOG.curie('how_many'),
                   model_uri=OSCAL.how_many, domain=None, range=Optional[Union[str, "ParameterCardinalityEnum"]])

slots.choice = Slot(uri=OSCAL_CATALOG.choice, name="choice", curie=OSCAL_CATALOG.curie('choice'),
                   model_uri=OSCAL.choice, domain=None, range=Optional[Union[str, list[str]]])

slots.catalog = Slot(uri=OSCAL_CATALOG.catalog, name="catalog", curie=OSCAL_CATALOG.curie('catalog'),
                   model_uri=OSCAL.catalog, domain=None, range=Optional[Union[dict, Catalog]])

slots.metadata = Slot(uri=OSCAL_CATALOG.metadata, name="metadata", curie=OSCAL_CATALOG.curie('metadata'),
                   model_uri=OSCAL.metadata, domain=None, range=Optional[Union[dict, Metadata]])

slots.back_matter = Slot(uri=OSCAL_CATALOG.back_matter, name="back-matter", curie=OSCAL_CATALOG.curie('back_matter'),
                   model_uri=OSCAL.back_matter, domain=None, range=Optional[Union[dict, BackMatter]])

slots.revisions = Slot(uri=OSCAL_CATALOG.revisions, name="revisions", curie=OSCAL_CATALOG.curie('revisions'),
                   model_uri=OSCAL.revisions, domain=None, range=Optional[Union[Union[dict, Revision], list[Union[dict, Revision]]]])

slots.roles = Slot(uri=OSCAL_CATALOG.roles, name="roles", curie=OSCAL_CATALOG.curie('roles'),
                   model_uri=OSCAL.roles, domain=None, range=Optional[Union[Union[dict, Role], list[Union[dict, Role]]]])

slots.locations = Slot(uri=OSCAL_CATALOG.locations, name="locations", curie=OSCAL_CATALOG.curie('locations'),
                   model_uri=OSCAL.locations, domain=None, range=Optional[Union[Union[dict, Location], list[Union[dict, Location]]]])

slots.parties = Slot(uri=OSCAL_CATALOG.parties, name="parties", curie=OSCAL_CATALOG.curie('parties'),
                   model_uri=OSCAL.parties, domain=None, range=Optional[Union[Union[dict, Party], list[Union[dict, Party]]]])

slots.actions = Slot(uri=OSCAL_CATALOG.actions, name="actions", curie=OSCAL_CATALOG.curie('actions'),
                   model_uri=OSCAL.actions, domain=None, range=Optional[Union[Union[dict, Action], list[Union[dict, Action]]]])

slots.identifier = Slot(uri=OSCAL_CATALOG.identifier, name="identifier", curie=OSCAL_CATALOG.curie('identifier'),
                   model_uri=OSCAL.identifier, domain=None, range=Optional[str])

slots.address = Slot(uri=OSCAL_CATALOG.address, name="address", curie=OSCAL_CATALOG.curie('address'),
                   model_uri=OSCAL.address, domain=None, range=Optional[Union[dict, Address]])

slots.urls = Slot(uri=OSCAL_CATALOG.urls, name="urls", curie=OSCAL_CATALOG.curie('urls'),
                   model_uri=OSCAL.urls, domain=None, range=Optional[Union[str, list[str]]])

slots.external_ids = Slot(uri=OSCAL_CATALOG.external_ids, name="external-ids", curie=OSCAL_CATALOG.curie('external_ids'),
                   model_uri=OSCAL.external_ids, domain=None, range=Optional[Union[Union[dict, PartyExternalId], list[Union[dict, PartyExternalId]]]])

slots.addresses = Slot(uri=OSCAL_CATALOG.addresses, name="addresses", curie=OSCAL_CATALOG.curie('addresses'),
                   model_uri=OSCAL.addresses, domain=None, range=Optional[Union[Union[dict, Address], list[Union[dict, Address]]]])

slots.location_uuids = Slot(uri=OSCAL_CATALOG.location_uuids, name="location-uuids", curie=OSCAL_CATALOG.curie('location_uuids'),
                   model_uri=OSCAL.location_uuids, domain=None, range=Optional[Union[str, list[str]]])

slots.member_of_organizations = Slot(uri=OSCAL_CATALOG.member_of_organizations, name="member-of-organizations", curie=OSCAL_CATALOG.curie('member_of_organizations'),
                   model_uri=OSCAL.member_of_organizations, domain=None, range=Optional[Union[str, list[str]]])

slots.date = Slot(uri=OSCAL_CATALOG.date, name="date", curie=OSCAL_CATALOG.curie('date'),
                   model_uri=OSCAL.date, domain=None, range=Optional[str])

slots.system = Slot(uri=OSCAL_CATALOG.system, name="system", curie=OSCAL_CATALOG.curie('system'),
                   model_uri=OSCAL.system, domain=None, range=Optional[str])

slots.number = Slot(uri=OSCAL_CATALOG.number, name="number", curie=OSCAL_CATALOG.curie('number'),
                   model_uri=OSCAL.number, domain=None, range=Optional[str])

slots.addr_lines = Slot(uri=OSCAL_CATALOG.addr_lines, name="addr-lines", curie=OSCAL_CATALOG.curie('addr_lines'),
                   model_uri=OSCAL.addr_lines, domain=None, range=Optional[Union[str, list[str]]])

slots.city = Slot(uri=OSCAL_CATALOG.city, name="city", curie=OSCAL_CATALOG.curie('city'),
                   model_uri=OSCAL.city, domain=None, range=Optional[str])

slots.state = Slot(uri=OSCAL_CATALOG.state, name="state", curie=OSCAL_CATALOG.curie('state'),
                   model_uri=OSCAL.state, domain=None, range=Optional[str])

slots.postal_code = Slot(uri=OSCAL_CATALOG.postal_code, name="postal-code", curie=OSCAL_CATALOG.curie('postal_code'),
                   model_uri=OSCAL.postal_code, domain=None, range=Optional[str])

slots.country = Slot(uri=OSCAL_CATALOG.country, name="country", curie=OSCAL_CATALOG.curie('country'),
                   model_uri=OSCAL.country, domain=None, range=Optional[str])

slots.algorithm = Slot(uri=OSCAL_CATALOG.algorithm, name="algorithm", curie=OSCAL_CATALOG.curie('algorithm'),
                   model_uri=OSCAL.algorithm, domain=None, range=Optional[str])

slots.group = Slot(uri=OSCAL_CATALOG.group, name="group", curie=OSCAL_CATALOG.curie('group'),
                   model_uri=OSCAL.group, domain=None, range=Optional[str])

slots.rel = Slot(uri=OSCAL_CATALOG.rel, name="rel", curie=OSCAL_CATALOG.curie('rel'),
                   model_uri=OSCAL.rel, domain=None, range=Optional[str])

slots.resource_fragment = Slot(uri=OSCAL_CATALOG.resource_fragment, name="resource-fragment", curie=OSCAL_CATALOG.curie('resource_fragment'),
                   model_uri=OSCAL.resource_fragment, domain=None, range=Optional[str])

slots.resources = Slot(uri=OSCAL_CATALOG.resources, name="resources", curie=OSCAL_CATALOG.curie('resources'),
                   model_uri=OSCAL.resources, domain=None, range=Optional[Union[Union[dict, Resource], list[Union[dict, Resource]]]])

slots.citation = Slot(uri=OSCAL_CATALOG.citation, name="citation", curie=OSCAL_CATALOG.curie('citation'),
                   model_uri=OSCAL.citation, domain=None, range=Optional[Union[dict, Citation]])

slots.rlinks = Slot(uri=OSCAL_CATALOG.rlinks, name="rlinks", curie=OSCAL_CATALOG.curie('rlinks'),
                   model_uri=OSCAL.rlinks, domain=None, range=Optional[Union[Union[dict, ResourceLink], list[Union[dict, ResourceLink]]]])

slots.base64 = Slot(uri=OSCAL_CATALOG.base64, name="base64", curie=OSCAL_CATALOG.curie('base64'),
                   model_uri=OSCAL.base64, domain=None, range=Optional[Union[dict, Base64Resource]])

slots.hashes = Slot(uri=OSCAL_CATALOG.hashes, name="hashes", curie=OSCAL_CATALOG.curie('hashes'),
                   model_uri=OSCAL.hashes, domain=None, range=Optional[Union[Union[dict, Hash], list[Union[dict, Hash]]]])

slots.filename = Slot(uri=OSCAL_CATALOG.filename, name="filename", curie=OSCAL_CATALOG.curie('filename'),
                   model_uri=OSCAL.filename, domain=None, range=Optional[str])

slots.depends_on = Slot(uri=OSCAL_CATALOG.depends_on, name="depends-on", curie=OSCAL_CATALOG.curie('depends_on'),
                   model_uri=OSCAL.depends_on, domain=None, range=Optional[str])

slots.label = Slot(uri=OSCAL_CATALOG.label, name="label", curie=OSCAL_CATALOG.curie('label'),
                   model_uri=OSCAL.label, domain=None, range=Optional[str])

slots.usage = Slot(uri=OSCAL_CATALOG.usage, name="usage", curie=OSCAL_CATALOG.curie('usage'),
                   model_uri=OSCAL.usage, domain=None, range=Optional[str])

slots.constraints = Slot(uri=OSCAL_CATALOG.constraints, name="constraints", curie=OSCAL_CATALOG.curie('constraints'),
                   model_uri=OSCAL.constraints, domain=None, range=Optional[Union[Union[dict, ParameterConstraint], list[Union[dict, ParameterConstraint]]]])

slots.guidelines = Slot(uri=OSCAL_CATALOG.guidelines, name="guidelines", curie=OSCAL_CATALOG.curie('guidelines'),
                   model_uri=OSCAL.guidelines, domain=None, range=Optional[Union[Union[dict, ParameterGuideline], list[Union[dict, ParameterGuideline]]]])

slots.values = Slot(uri=OSCAL_CATALOG.values, name="values", curie=OSCAL_CATALOG.curie('values'),
                   model_uri=OSCAL.values, domain=None, range=Optional[Union[str, list[str]]])

slots.select = Slot(uri=OSCAL_CATALOG.select, name="select", curie=OSCAL_CATALOG.curie('select'),
                   model_uri=OSCAL.select, domain=None, range=Optional[Union[dict, ParameterSelection]])

slots.tests = Slot(uri=OSCAL_CATALOG.tests, name="tests", curie=OSCAL_CATALOG.curie('tests'),
                   model_uri=OSCAL.tests, domain=None, range=Optional[Union[Union[dict, ConstraintTest], list[Union[dict, ConstraintTest]]]])

slots.expression = Slot(uri=OSCAL_CATALOG.expression, name="expression", curie=OSCAL_CATALOG.curie('expression'),
                   model_uri=OSCAL.expression, domain=None, range=Optional[str])

slots.with_child_controls = Slot(uri=OSCAL_CATALOG.with_child_controls, name="with-child-controls", curie=OSCAL_CATALOG.curie('with_child_controls'),
                   model_uri=OSCAL.with_child_controls, domain=None, range=Optional[Union[str, "WithChildControlsEnum"]])

slots.with_ids = Slot(uri=OSCAL_CATALOG.with_ids, name="with-ids", curie=OSCAL_CATALOG.curie('with_ids'),
                   model_uri=OSCAL.with_ids, domain=None, range=Optional[Union[str, list[str]]])

slots.matching = Slot(uri=OSCAL_CATALOG.matching, name="matching", curie=OSCAL_CATALOG.curie('matching'),
                   model_uri=OSCAL.matching, domain=None, range=Optional[Union[Union[dict, ControlMatching], list[Union[dict, ControlMatching]]]])

slots.pattern = Slot(uri=OSCAL_CATALOG.pattern, name="pattern", curie=OSCAL_CATALOG.curie('pattern'),
                   model_uri=OSCAL.pattern, domain=None, range=Optional[str])

slots.profile = Slot(uri=OSCAL_PROFILE.profile, name="profile", curie=OSCAL_PROFILE.curie('profile'),
                   model_uri=OSCAL.profile, domain=None, range=Optional[Union[dict, Profile]])

slots.imports = Slot(uri=OSCAL_PROFILE.imports, name="imports", curie=OSCAL_PROFILE.curie('imports'),
                   model_uri=OSCAL.imports, domain=None, range=Optional[Union[Union[dict, ProfileImport], list[Union[dict, ProfileImport]]]])

slots.merge = Slot(uri=OSCAL_PROFILE.merge, name="merge", curie=OSCAL_PROFILE.curie('merge'),
                   model_uri=OSCAL.merge, domain=None, range=Optional[Union[dict, ProfileMerge]])

slots.modify = Slot(uri=OSCAL_PROFILE.modify, name="modify", curie=OSCAL_PROFILE.curie('modify'),
                   model_uri=OSCAL.modify, domain=None, range=Optional[Union[dict, ProfileModify]])

slots.insert_controls = Slot(uri=OSCAL_PROFILE.insert_controls, name="insert-controls", curie=OSCAL_PROFILE.curie('insert_controls'),
                   model_uri=OSCAL.insert_controls, domain=None, range=Optional[Union[Union[dict, InsertControls], list[Union[dict, InsertControls]]]])

slots.order = Slot(uri=OSCAL_PROFILE.order, name="order", curie=OSCAL_PROFILE.curie('order'),
                   model_uri=OSCAL.order, domain=None, range=Optional[Union[str, "InsertOrderEnum"]])

slots.combine = Slot(uri=OSCAL_PROFILE.combine, name="combine", curie=OSCAL_PROFILE.curie('combine'),
                   model_uri=OSCAL.combine, domain=None, range=Optional[Union[dict, CombinationRule]])

slots.flat = Slot(uri=OSCAL_PROFILE.flat, name="flat", curie=OSCAL_PROFILE.curie('flat'),
                   model_uri=OSCAL.flat, domain=None, range=Optional[Union[dict, MergeFlat]])

slots.as_is = Slot(uri=OSCAL_PROFILE.as_is, name="as-is", curie=OSCAL_PROFILE.curie('as_is'),
                   model_uri=OSCAL.as_is, domain=None, range=Optional[Union[bool, Bool]])

slots.custom = Slot(uri=OSCAL_PROFILE.custom, name="custom", curie=OSCAL_PROFILE.curie('custom'),
                   model_uri=OSCAL.custom, domain=None, range=Optional[Union[dict, MergeCustom]])

slots.alters = Slot(uri=OSCAL_PROFILE.alters, name="alters", curie=OSCAL_PROFILE.curie('alters'),
                   model_uri=OSCAL.alters, domain=None, range=Optional[Union[Union[dict, Alteration], list[Union[dict, Alteration]]]])

slots.removes = Slot(uri=OSCAL_PROFILE.removes, name="removes", curie=OSCAL_PROFILE.curie('removes'),
                   model_uri=OSCAL.removes, domain=None, range=Optional[Union[Union[dict, Removal], list[Union[dict, Removal]]]])

slots.adds = Slot(uri=OSCAL_PROFILE.adds, name="adds", curie=OSCAL_PROFILE.curie('adds'),
                   model_uri=OSCAL.adds, domain=None, range=Optional[Union[Union[dict, Addition], list[Union[dict, Addition]]]])

slots.by_name = Slot(uri=OSCAL_PROFILE.by_name, name="by-name", curie=OSCAL_PROFILE.curie('by_name'),
                   model_uri=OSCAL.by_name, domain=None, range=Optional[str])

slots.by_class = Slot(uri=OSCAL_PROFILE.by_class, name="by-class", curie=OSCAL_PROFILE.curie('by_class'),
                   model_uri=OSCAL.by_class, domain=None, range=Optional[str])

slots.by_id = Slot(uri=OSCAL_PROFILE.by_id, name="by-id", curie=OSCAL_PROFILE.curie('by_id'),
                   model_uri=OSCAL.by_id, domain=None, range=Optional[str])

slots.by_item_name = Slot(uri=OSCAL_PROFILE.by_item_name, name="by-item-name", curie=OSCAL_PROFILE.curie('by_item_name'),
                   model_uri=OSCAL.by_item_name, domain=None, range=Optional[Union[str, "ByItemNameEnum"]])

slots.by_ns = Slot(uri=OSCAL_PROFILE.by_ns, name="by-ns", curie=OSCAL_PROFILE.curie('by_ns'),
                   model_uri=OSCAL.by_ns, domain=None, range=Optional[str])

slots.position = Slot(uri=OSCAL_PROFILE.position, name="position", curie=OSCAL_PROFILE.curie('position'),
                   model_uri=OSCAL.position, domain=None, range=Optional[Union[str, "AdditionPositionEnum"]])

slots.system_security_plan = Slot(uri=OSCAL_SSP.system_security_plan, name="system-security-plan", curie=OSCAL_SSP.curie('system_security_plan'),
                   model_uri=OSCAL.system_security_plan, domain=None, range=Optional[Union[dict, SystemSecurityPlan]])

slots.import_profile = Slot(uri=OSCAL_SSP.import_profile, name="import-profile", curie=OSCAL_SSP.curie('import_profile'),
                   model_uri=OSCAL.import_profile, domain=None, range=Optional[Union[dict, ImportProfile]])

slots.system_characteristics = Slot(uri=OSCAL_SSP.system_characteristics, name="system-characteristics", curie=OSCAL_SSP.curie('system_characteristics'),
                   model_uri=OSCAL.system_characteristics, domain=None, range=Optional[Union[dict, SystemCharacteristics]])

slots.system_implementation = Slot(uri=OSCAL_SSP.system_implementation, name="system-implementation", curie=OSCAL_SSP.curie('system_implementation'),
                   model_uri=OSCAL.system_implementation, domain=None, range=Optional[Union[dict, SystemImplementation]])

slots.control_implementation = Slot(uri=OSCAL_SSP.control_implementation, name="control-implementation", curie=OSCAL_SSP.curie('control_implementation'),
                   model_uri=OSCAL.control_implementation, domain=None, range=Optional[Union[dict, SspControlImplementation]])

slots.system_ids = Slot(uri=OSCAL_SSP.system_ids, name="system-ids", curie=OSCAL_SSP.curie('system_ids'),
                   model_uri=OSCAL.system_ids, domain=None, range=Optional[Union[Union[dict, SystemId], list[Union[dict, SystemId]]]])

slots.system_name = Slot(uri=OSCAL_SSP.system_name, name="system-name", curie=OSCAL_SSP.curie('system_name'),
                   model_uri=OSCAL.system_name, domain=None, range=Optional[str])

slots.system_name_short = Slot(uri=OSCAL_SSP.system_name_short, name="system-name-short", curie=OSCAL_SSP.curie('system_name_short'),
                   model_uri=OSCAL.system_name_short, domain=None, range=Optional[str])

slots.date_authorized = Slot(uri=OSCAL_SSP.date_authorized, name="date-authorized", curie=OSCAL_SSP.curie('date_authorized'),
                   model_uri=OSCAL.date_authorized, domain=None, range=Optional[str])

slots.security_sensitivity_level = Slot(uri=OSCAL_SSP.security_sensitivity_level, name="security-sensitivity-level", curie=OSCAL_SSP.curie('security_sensitivity_level'),
                   model_uri=OSCAL.security_sensitivity_level, domain=None, range=Optional[str])

slots.system_information = Slot(uri=OSCAL_SSP.system_information, name="system-information", curie=OSCAL_SSP.curie('system_information'),
                   model_uri=OSCAL.system_information, domain=None, range=Optional[Union[dict, SystemInformation]])

slots.security_impact_level = Slot(uri=OSCAL_SSP.security_impact_level, name="security-impact-level", curie=OSCAL_SSP.curie('security_impact_level'),
                   model_uri=OSCAL.security_impact_level, domain=None, range=Optional[Union[dict, SecurityImpactLevel]])

slots.system_status = Slot(uri=OSCAL_SSP.system_status, name="system-status", curie=OSCAL_SSP.curie('system_status'),
                   model_uri=OSCAL.system_status, domain=None, range=Optional[Union[dict, SystemStatus]])

slots.authorization_boundary = Slot(uri=OSCAL_SSP.authorization_boundary, name="authorization-boundary", curie=OSCAL_SSP.curie('authorization_boundary'),
                   model_uri=OSCAL.authorization_boundary, domain=None, range=Optional[Union[dict, AuthorizationBoundary]])

slots.network_architecture = Slot(uri=OSCAL_SSP.network_architecture, name="network-architecture", curie=OSCAL_SSP.curie('network_architecture'),
                   model_uri=OSCAL.network_architecture, domain=None, range=Optional[Union[dict, NetworkArchitecture]])

slots.data_flow = Slot(uri=OSCAL_SSP.data_flow, name="data-flow", curie=OSCAL_SSP.curie('data_flow'),
                   model_uri=OSCAL.data_flow, domain=None, range=Optional[Union[dict, DataFlow]])

slots.information_types = Slot(uri=OSCAL_SSP.information_types, name="information-types", curie=OSCAL_SSP.curie('information_types'),
                   model_uri=OSCAL.information_types, domain=None, range=Optional[Union[Union[dict, InformationType], list[Union[dict, InformationType]]]])

slots.categorizations = Slot(uri=OSCAL_SSP.categorizations, name="categorizations", curie=OSCAL_SSP.curie('categorizations'),
                   model_uri=OSCAL.categorizations, domain=None, range=Optional[Union[Union[dict, InformationTypeCategorization], list[Union[dict, InformationTypeCategorization]]]])

slots.information_type_ids = Slot(uri=OSCAL_SSP.information_type_ids, name="information-type-ids", curie=OSCAL_SSP.curie('information_type_ids'),
                   model_uri=OSCAL.information_type_ids, domain=None, range=Optional[Union[str, list[str]]])

slots.confidentiality_impact = Slot(uri=OSCAL_SSP.confidentiality_impact, name="confidentiality-impact", curie=OSCAL_SSP.curie('confidentiality_impact'),
                   model_uri=OSCAL.confidentiality_impact, domain=None, range=Optional[Union[dict, ImpactLevel]])

slots.integrity_impact = Slot(uri=OSCAL_SSP.integrity_impact, name="integrity-impact", curie=OSCAL_SSP.curie('integrity_impact'),
                   model_uri=OSCAL.integrity_impact, domain=None, range=Optional[Union[dict, ImpactLevel]])

slots.availability_impact = Slot(uri=OSCAL_SSP.availability_impact, name="availability-impact", curie=OSCAL_SSP.curie('availability_impact'),
                   model_uri=OSCAL.availability_impact, domain=None, range=Optional[Union[dict, ImpactLevel]])

slots.base = Slot(uri=OSCAL_SSP.base, name="base", curie=OSCAL_SSP.curie('base'),
                   model_uri=OSCAL.base, domain=None, range=Optional[str])

slots.selected = Slot(uri=OSCAL_SSP.selected, name="selected", curie=OSCAL_SSP.curie('selected'),
                   model_uri=OSCAL.selected, domain=None, range=Optional[str])

slots.adjustment_justification = Slot(uri=OSCAL_SSP.adjustment_justification, name="adjustment-justification", curie=OSCAL_SSP.curie('adjustment_justification'),
                   model_uri=OSCAL.adjustment_justification, domain=None, range=Optional[str])

slots.security_objective_confidentiality = Slot(uri=OSCAL_SSP.security_objective_confidentiality, name="security-objective-confidentiality", curie=OSCAL_SSP.curie('security_objective_confidentiality'),
                   model_uri=OSCAL.security_objective_confidentiality, domain=None, range=Optional[str])

slots.security_objective_integrity = Slot(uri=OSCAL_SSP.security_objective_integrity, name="security-objective-integrity", curie=OSCAL_SSP.curie('security_objective_integrity'),
                   model_uri=OSCAL.security_objective_integrity, domain=None, range=Optional[str])

slots.security_objective_availability = Slot(uri=OSCAL_SSP.security_objective_availability, name="security-objective-availability", curie=OSCAL_SSP.curie('security_objective_availability'),
                   model_uri=OSCAL.security_objective_availability, domain=None, range=Optional[str])

slots.diagrams = Slot(uri=OSCAL_SSP.diagrams, name="diagrams", curie=OSCAL_SSP.curie('diagrams'),
                   model_uri=OSCAL.diagrams, domain=None, range=Optional[Union[Union[dict, Diagram], list[Union[dict, Diagram]]]])

slots.caption = Slot(uri=OSCAL_SSP.caption, name="caption", curie=OSCAL_SSP.curie('caption'),
                   model_uri=OSCAL.caption, domain=None, range=Optional[str])

slots.leveraged_authorizations = Slot(uri=OSCAL_SSP.leveraged_authorizations, name="leveraged-authorizations", curie=OSCAL_SSP.curie('leveraged_authorizations'),
                   model_uri=OSCAL.leveraged_authorizations, domain=None, range=Optional[Union[Union[dict, LeveragedAuthorization], list[Union[dict, LeveragedAuthorization]]]])

slots.by_components = Slot(uri=OSCAL_SSP.by_components, name="by-components", curie=OSCAL_SSP.curie('by_components'),
                   model_uri=OSCAL.by_components, domain=None, range=Optional[Union[Union[dict, ByComponent], list[Union[dict, ByComponent]]]])

slots.export = Slot(uri=OSCAL_SSP.export, name="export", curie=OSCAL_SSP.curie('export'),
                   model_uri=OSCAL.export, domain=None, range=Optional[Union[dict, Export]])

slots.provided = Slot(uri=OSCAL_SSP.provided, name="provided", curie=OSCAL_SSP.curie('provided'),
                   model_uri=OSCAL.provided, domain=None, range=Optional[Union[Union[dict, ProvidedControlImplementation], list[Union[dict, ProvidedControlImplementation]]]])

slots.responsibilities = Slot(uri=OSCAL_SSP.responsibilities, name="responsibilities", curie=OSCAL_SSP.curie('responsibilities'),
                   model_uri=OSCAL.responsibilities, domain=None, range=Optional[Union[Union[dict, ControlResponsibility], list[Union[dict, ControlResponsibility]]]])

slots.inherited = Slot(uri=OSCAL_SSP.inherited, name="inherited", curie=OSCAL_SSP.curie('inherited'),
                   model_uri=OSCAL.inherited, domain=None, range=Optional[Union[Union[dict, InheritedControlImplementation], list[Union[dict, InheritedControlImplementation]]]])

slots.satisfied = Slot(uri=OSCAL_SSP.satisfied, name="satisfied", curie=OSCAL_SSP.curie('satisfied'),
                   model_uri=OSCAL.satisfied, domain=None, range=Optional[Union[Union[dict, SatisfiedControlImplementation], list[Union[dict, SatisfiedControlImplementation]]]])

slots.provided_uuid = Slot(uri=OSCAL_SSP.provided_uuid, name="provided-uuid", curie=OSCAL_SSP.curie('provided_uuid'),
                   model_uri=OSCAL.provided_uuid, domain=None, range=Optional[str])

slots.responsibility_uuid = Slot(uri=OSCAL_SSP.responsibility_uuid, name="responsibility-uuid", curie=OSCAL_SSP.curie('responsibility_uuid'),
                   model_uri=OSCAL.responsibility_uuid, domain=None, range=Optional[str])

slots.subject_uuid = Slot(uri=OSCAL_ASSESSMENT_PLAN.subject_uuid, name="subject-uuid", curie=OSCAL_ASSESSMENT_PLAN.curie('subject_uuid'),
                   model_uri=OSCAL.subject_uuid, domain=None, range=Optional[str])

slots.task_uuid = Slot(uri=OSCAL_ASSESSMENT_PLAN.task_uuid, name="task-uuid", curie=OSCAL_ASSESSMENT_PLAN.curie('task_uuid'),
                   model_uri=OSCAL.task_uuid, domain=None, range=Optional[str])

slots.activity_uuid = Slot(uri=OSCAL_ASSESSMENT_PLAN.activity_uuid, name="activity-uuid", curie=OSCAL_ASSESSMENT_PLAN.curie('activity_uuid'),
                   model_uri=OSCAL.activity_uuid, domain=None, range=Optional[str])

slots.component_uuid = Slot(uri=OSCAL_ASSESSMENT_PLAN.component_uuid, name="component-uuid", curie=OSCAL_ASSESSMENT_PLAN.curie('component_uuid'),
                   model_uri=OSCAL.component_uuid, domain=None, range=Optional[str])

slots.subjects = Slot(uri=OSCAL_ASSESSMENT_PLAN.subjects, name="subjects", curie=OSCAL_ASSESSMENT_PLAN.curie('subjects'),
                   model_uri=OSCAL.subjects, domain=None, range=Optional[Union[str, list[str]]])

slots.origins = Slot(uri=OSCAL_ASSESSMENT_PLAN.origins, name="origins", curie=OSCAL_ASSESSMENT_PLAN.curie('origins'),
                   model_uri=OSCAL.origins, domain=None, range=Optional[Union[Union[dict, Origin], list[Union[dict, Origin]]]])

slots.reviewed_controls = Slot(uri=OSCAL_ASSESSMENT_PLAN.reviewed_controls, name="reviewed-controls", curie=OSCAL_ASSESSMENT_PLAN.curie('reviewed_controls'),
                   model_uri=OSCAL.reviewed_controls, domain=None, range=Optional[Union[dict, ReviewedControls]])

slots.tasks = Slot(uri=OSCAL_ASSESSMENT_PLAN.tasks, name="tasks", curie=OSCAL_ASSESSMENT_PLAN.curie('tasks'),
                   model_uri=OSCAL.tasks, domain=None, range=Optional[Union[Union[dict, Task], list[Union[dict, Task]]]])

slots.components = Slot(uri=OSCAL_ASSESSMENT_PLAN.components, name="components", curie=OSCAL_ASSESSMENT_PLAN.curie('components'),
                   model_uri=OSCAL.components, domain=None, range=Optional[Union[Union[dict, SystemComponent], list[Union[dict, SystemComponent]]]])

slots.related_observations = Slot(uri=OSCAL_ASSESSMENT_PLAN.related_observations, name="related-observations", curie=OSCAL_ASSESSMENT_PLAN.curie('related_observations'),
                   model_uri=OSCAL.related_observations, domain=None, range=Optional[Union[Union[dict, RelatedObservation], list[Union[dict, RelatedObservation]]]])

slots.related_tasks = Slot(uri=OSCAL_ASSESSMENT_PLAN.related_tasks, name="related-tasks", curie=OSCAL_ASSESSMENT_PLAN.curie('related_tasks'),
                   model_uri=OSCAL.related_tasks, domain=None, range=Optional[Union[Union[dict, RelatedTask], list[Union[dict, RelatedTask]]]])

slots.start = Slot(uri=OSCAL_ASSESSMENT_PLAN.start, name="start", curie=OSCAL_ASSESSMENT_PLAN.curie('start'),
                   model_uri=OSCAL.start, domain=None, range=Optional[str])

slots.end = Slot(uri=OSCAL_ASSESSMENT_PLAN.end, name="end", curie=OSCAL_ASSESSMENT_PLAN.curie('end'),
                   model_uri=OSCAL.end, domain=None, range=Optional[str])

slots.assessment_plan = Slot(uri=OSCAL_ASSESSMENT_PLAN.assessment_plan, name="assessment-plan", curie=OSCAL_ASSESSMENT_PLAN.curie('assessment_plan'),
                   model_uri=OSCAL.assessment_plan, domain=None, range=Optional[Union[dict, AssessmentPlan]])

slots.import_ssp = Slot(uri=OSCAL_ASSESSMENT_PLAN.import_ssp, name="import-ssp", curie=OSCAL_ASSESSMENT_PLAN.curie('import_ssp'),
                   model_uri=OSCAL.import_ssp, domain=None, range=Optional[Union[dict, ImportSSP]])

slots.local_definitions = Slot(uri=OSCAL_ASSESSMENT_PLAN.local_definitions, name="local-definitions", curie=OSCAL_ASSESSMENT_PLAN.curie('local_definitions'),
                   model_uri=OSCAL.local_definitions, domain=None, range=Optional[Union[dict, LocalDefinitions]])

slots.terms_and_conditions = Slot(uri=OSCAL_ASSESSMENT_PLAN.terms_and_conditions, name="terms-and-conditions", curie=OSCAL_ASSESSMENT_PLAN.curie('terms_and_conditions'),
                   model_uri=OSCAL.terms_and_conditions, domain=None, range=Optional[Union[dict, TermsAndConditions]])

slots.assessment_subjects = Slot(uri=OSCAL_ASSESSMENT_PLAN.assessment_subjects, name="assessment-subjects", curie=OSCAL_ASSESSMENT_PLAN.curie('assessment_subjects'),
                   model_uri=OSCAL.assessment_subjects, domain=None, range=Optional[Union[Union[dict, AssessmentSubject], list[Union[dict, AssessmentSubject]]]])

slots.assessment_assets = Slot(uri=OSCAL_ASSESSMENT_PLAN.assessment_assets, name="assessment-assets", curie=OSCAL_ASSESSMENT_PLAN.curie('assessment_assets'),
                   model_uri=OSCAL.assessment_assets, domain=None, range=Optional[Union[dict, AssessmentAssets]])

slots.inventory_items = Slot(uri=OSCAL_ASSESSMENT_PLAN.inventory_items, name="inventory-items", curie=OSCAL_ASSESSMENT_PLAN.curie('inventory_items'),
                   model_uri=OSCAL.inventory_items, domain=None, range=Optional[Union[Union[dict, InventoryItem], list[Union[dict, InventoryItem]]]])

slots.users = Slot(uri=OSCAL_ASSESSMENT_PLAN.users, name="users", curie=OSCAL_ASSESSMENT_PLAN.curie('users'),
                   model_uri=OSCAL.users, domain=None, range=Optional[Union[Union[dict, SystemUser], list[Union[dict, SystemUser]]]])

slots.objectives_and_methods = Slot(uri=OSCAL_ASSESSMENT_PLAN.objectives_and_methods, name="objectives-and-methods", curie=OSCAL_ASSESSMENT_PLAN.curie('objectives_and_methods'),
                   model_uri=OSCAL.objectives_and_methods, domain=None, range=Optional[Union[Union[dict, LocalObjective], list[Union[dict, LocalObjective]]]])

slots.activities = Slot(uri=OSCAL_ASSESSMENT_PLAN.activities, name="activities", curie=OSCAL_ASSESSMENT_PLAN.curie('activities'),
                   model_uri=OSCAL.activities, domain=None, range=Optional[Union[Union[dict, Activity], list[Union[dict, Activity]]]])

slots.control_selections = Slot(uri=OSCAL_ASSESSMENT_PLAN.control_selections, name="control-selections", curie=OSCAL_ASSESSMENT_PLAN.curie('control_selections'),
                   model_uri=OSCAL.control_selections, domain=None, range=Optional[Union[Union[dict, ControlSelection], list[Union[dict, ControlSelection]]]])

slots.control_objective_selections = Slot(uri=OSCAL_ASSESSMENT_PLAN.control_objective_selections, name="control-objective-selections", curie=OSCAL_ASSESSMENT_PLAN.curie('control_objective_selections'),
                   model_uri=OSCAL.control_objective_selections, domain=None, range=Optional[Union[Union[dict, ControlObjectiveSelection], list[Union[dict, ControlObjectiveSelection]]]])

slots.include_objectives = Slot(uri=OSCAL_ASSESSMENT_PLAN.include_objectives, name="include-objectives", curie=OSCAL_ASSESSMENT_PLAN.curie('include_objectives'),
                   model_uri=OSCAL.include_objectives, domain=None, range=Optional[Union[Union[dict, SelectObjectiveById], list[Union[dict, SelectObjectiveById]]]])

slots.exclude_objectives = Slot(uri=OSCAL_ASSESSMENT_PLAN.exclude_objectives, name="exclude-objectives", curie=OSCAL_ASSESSMENT_PLAN.curie('exclude_objectives'),
                   model_uri=OSCAL.exclude_objectives, domain=None, range=Optional[Union[Union[dict, SelectObjectiveById], list[Union[dict, SelectObjectiveById]]]])

slots.statement_ids = Slot(uri=OSCAL_ASSESSMENT_PLAN.statement_ids, name="statement-ids", curie=OSCAL_ASSESSMENT_PLAN.curie('statement_ids'),
                   model_uri=OSCAL.statement_ids, domain=None, range=Optional[Union[str, list[str]]])

slots.objective_id = Slot(uri=OSCAL_ASSESSMENT_PLAN.objective_id, name="objective-id", curie=OSCAL_ASSESSMENT_PLAN.curie('objective_id'),
                   model_uri=OSCAL.objective_id, domain=None, range=Optional[str])

slots.include_subjects = Slot(uri=OSCAL_ASSESSMENT_PLAN.include_subjects, name="include-subjects", curie=OSCAL_ASSESSMENT_PLAN.curie('include_subjects'),
                   model_uri=OSCAL.include_subjects, domain=None, range=Optional[Union[Union[dict, SelectSubjectById], list[Union[dict, SelectSubjectById]]]])

slots.exclude_subjects = Slot(uri=OSCAL_ASSESSMENT_PLAN.exclude_subjects, name="exclude-subjects", curie=OSCAL_ASSESSMENT_PLAN.curie('exclude_subjects'),
                   model_uri=OSCAL.exclude_subjects, domain=None, range=Optional[Union[Union[dict, SelectSubjectById], list[Union[dict, SelectSubjectById]]]])

slots.observations = Slot(uri=OSCAL_ASSESSMENT_PLAN.observations, name="observations", curie=OSCAL_ASSESSMENT_PLAN.curie('observations'),
                   model_uri=OSCAL.observations, domain=None, range=Optional[Union[Union[dict, Observation], list[Union[dict, Observation]]]])

slots.risks = Slot(uri=OSCAL_ASSESSMENT_PLAN.risks, name="risks", curie=OSCAL_ASSESSMENT_PLAN.curie('risks'),
                   model_uri=OSCAL.risks, domain=None, range=Optional[Union[Union[dict, Risk], list[Union[dict, Risk]]]])

slots.findings = Slot(uri=OSCAL_ASSESSMENT_PLAN.findings, name="findings", curie=OSCAL_ASSESSMENT_PLAN.curie('findings'),
                   model_uri=OSCAL.findings, domain=None, range=Optional[Union[Union[dict, Finding], list[Union[dict, Finding]]]])

slots.assessment_platforms = Slot(uri=OSCAL_ASSESSMENT_PLAN.assessment_platforms, name="assessment-platforms", curie=OSCAL_ASSESSMENT_PLAN.curie('assessment_platforms'),
                   model_uri=OSCAL.assessment_platforms, domain=None, range=Optional[Union[Union[dict, AssessmentPlatform], list[Union[dict, AssessmentPlatform]]]])

slots.uses_components = Slot(uri=OSCAL_ASSESSMENT_PLAN.uses_components, name="uses-components", curie=OSCAL_ASSESSMENT_PLAN.curie('uses_components'),
                   model_uri=OSCAL.uses_components, domain=None, range=Optional[Union[Union[dict, UsesComponent], list[Union[dict, UsesComponent]]]])

slots.part = Slot(uri=OSCAL_ASSESSMENT_PLAN.part, name="part", curie=OSCAL_ASSESSMENT_PLAN.curie('part'),
                   model_uri=OSCAL.part, domain=None, range=Optional[Union[dict, AssessmentPart]])

slots.steps = Slot(uri=OSCAL_ASSESSMENT_PLAN.steps, name="steps", curie=OSCAL_ASSESSMENT_PLAN.curie('steps'),
                   model_uri=OSCAL.steps, domain=None, range=Optional[Union[Union[dict, Step], list[Union[dict, Step]]]])

slots.related_controls = Slot(uri=OSCAL_ASSESSMENT_PLAN.related_controls, name="related-controls", curie=OSCAL_ASSESSMENT_PLAN.curie('related_controls'),
                   model_uri=OSCAL.related_controls, domain=None, range=Optional[Union[dict, ReviewedControls]])

slots.timing = Slot(uri=OSCAL_ASSESSMENT_PLAN.timing, name="timing", curie=OSCAL_ASSESSMENT_PLAN.curie('timing'),
                   model_uri=OSCAL.timing, domain=None, range=Optional[Union[dict, EventTiming]])

slots.dependencies = Slot(uri=OSCAL_ASSESSMENT_PLAN.dependencies, name="dependencies", curie=OSCAL_ASSESSMENT_PLAN.curie('dependencies'),
                   model_uri=OSCAL.dependencies, domain=None, range=Optional[Union[Union[dict, TaskDependency], list[Union[dict, TaskDependency]]]])

slots.associated_activities = Slot(uri=OSCAL_ASSESSMENT_PLAN.associated_activities, name="associated-activities", curie=OSCAL_ASSESSMENT_PLAN.curie('associated_activities'),
                   model_uri=OSCAL.associated_activities, domain=None, range=Optional[Union[Union[dict, AssociatedActivity], list[Union[dict, AssociatedActivity]]]])

slots.on_date = Slot(uri=OSCAL_ASSESSMENT_PLAN.on_date, name="on-date", curie=OSCAL_ASSESSMENT_PLAN.curie('on_date'),
                   model_uri=OSCAL.on_date, domain=None, range=Optional[Union[dict, OnDateCondition]])

slots.within_date_range = Slot(uri=OSCAL_ASSESSMENT_PLAN.within_date_range, name="within-date-range", curie=OSCAL_ASSESSMENT_PLAN.curie('within_date_range'),
                   model_uri=OSCAL.within_date_range, domain=None, range=Optional[Union[dict, WithinDateRange]])

slots.at_frequency = Slot(uri=OSCAL_ASSESSMENT_PLAN.at_frequency, name="at-frequency", curie=OSCAL_ASSESSMENT_PLAN.curie('at_frequency'),
                   model_uri=OSCAL.at_frequency, domain=None, range=Optional[Union[dict, AtFrequency]])

slots.period = Slot(uri=OSCAL_ASSESSMENT_PLAN.period, name="period", curie=OSCAL_ASSESSMENT_PLAN.curie('period'),
                   model_uri=OSCAL.period, domain=None, range=Optional[int])

slots.unit = Slot(uri=OSCAL_ASSESSMENT_PLAN.unit, name="unit", curie=OSCAL_ASSESSMENT_PLAN.curie('unit'),
                   model_uri=OSCAL.unit, domain=None, range=Optional[Union[str, "TimingUnitEnum"]])

slots.purpose = Slot(uri=OSCAL_ASSESSMENT_PLAN.purpose, name="purpose", curie=OSCAL_ASSESSMENT_PLAN.curie('purpose'),
                   model_uri=OSCAL.purpose, domain=None, range=Optional[str])

slots.protocols = Slot(uri=OSCAL_ASSESSMENT_PLAN.protocols, name="protocols", curie=OSCAL_ASSESSMENT_PLAN.curie('protocols'),
                   model_uri=OSCAL.protocols, domain=None, range=Optional[Union[Union[dict, Protocol], list[Union[dict, Protocol]]]])

slots.port_ranges = Slot(uri=OSCAL_ASSESSMENT_PLAN.port_ranges, name="port-ranges", curie=OSCAL_ASSESSMENT_PLAN.curie('port_ranges'),
                   model_uri=OSCAL.port_ranges, domain=None, range=Optional[Union[Union[dict, PortRange], list[Union[dict, PortRange]]]])

slots.transport = Slot(uri=OSCAL_ASSESSMENT_PLAN.transport, name="transport", curie=OSCAL_ASSESSMENT_PLAN.curie('transport'),
                   model_uri=OSCAL.transport, domain=None, range=Optional[Union[str, "TransportEnum"]])

slots.role_ids = Slot(uri=OSCAL_ASSESSMENT_PLAN.role_ids, name="role-ids", curie=OSCAL_ASSESSMENT_PLAN.curie('role_ids'),
                   model_uri=OSCAL.role_ids, domain=None, range=Optional[Union[str, list[str]]])

slots.authorized_privileges = Slot(uri=OSCAL_ASSESSMENT_PLAN.authorized_privileges, name="authorized-privileges", curie=OSCAL_ASSESSMENT_PLAN.curie('authorized_privileges'),
                   model_uri=OSCAL.authorized_privileges, domain=None, range=Optional[Union[Union[dict, AuthorizedPrivilege], list[Union[dict, AuthorizedPrivilege]]]])

slots.functions_performed = Slot(uri=OSCAL_ASSESSMENT_PLAN.functions_performed, name="functions-performed", curie=OSCAL_ASSESSMENT_PLAN.curie('functions_performed'),
                   model_uri=OSCAL.functions_performed, domain=None, range=Optional[Union[str, list[str]]])

slots.implemented_components = Slot(uri=OSCAL_ASSESSMENT_PLAN.implemented_components, name="implemented-components", curie=OSCAL_ASSESSMENT_PLAN.curie('implemented_components'),
                   model_uri=OSCAL.implemented_components, domain=None, range=Optional[Union[Union[dict, ImplementedComponent], list[Union[dict, ImplementedComponent]]]])

slots.identifier_type = Slot(uri=OSCAL_ASSESSMENT_PLAN.identifier_type, name="identifier-type", curie=OSCAL_ASSESSMENT_PLAN.curie('identifier_type'),
                   model_uri=OSCAL.identifier_type, domain=None, range=Optional[str])

slots.actors = Slot(uri=OSCAL_ASSESSMENT_PLAN.actors, name="actors", curie=OSCAL_ASSESSMENT_PLAN.curie('actors'),
                   model_uri=OSCAL.actors, domain=None, range=Optional[Union[Union[dict, OriginActor], list[Union[dict, OriginActor]]]])

slots.actor_uuid = Slot(uri=OSCAL_ASSESSMENT_PLAN.actor_uuid, name="actor-uuid", curie=OSCAL_ASSESSMENT_PLAN.curie('actor_uuid'),
                   model_uri=OSCAL.actor_uuid, domain=None, range=Optional[str])

slots.identified_subject = Slot(uri=OSCAL_ASSESSMENT_PLAN.identified_subject, name="identified-subject", curie=OSCAL_ASSESSMENT_PLAN.curie('identified_subject'),
                   model_uri=OSCAL.identified_subject, domain=None, range=Optional[Union[dict, IdentifiedSubject]])

slots.subject_placeholder_uuid = Slot(uri=OSCAL_ASSESSMENT_PLAN.subject_placeholder_uuid, name="subject-placeholder-uuid", curie=OSCAL_ASSESSMENT_PLAN.curie('subject_placeholder_uuid'),
                   model_uri=OSCAL.subject_placeholder_uuid, domain=None, range=Optional[str])

slots.methods = Slot(uri=OSCAL_ASSESSMENT_PLAN.methods, name="methods", curie=OSCAL_ASSESSMENT_PLAN.curie('methods'),
                   model_uri=OSCAL.methods, domain=None, range=Optional[Union[str, list[str]]])

slots.types = Slot(uri=OSCAL_ASSESSMENT_PLAN.types, name="types", curie=OSCAL_ASSESSMENT_PLAN.curie('types'),
                   model_uri=OSCAL.types, domain=None, range=Optional[Union[str, list[str]]])

slots.relevant_evidence = Slot(uri=OSCAL_ASSESSMENT_PLAN.relevant_evidence, name="relevant-evidence", curie=OSCAL_ASSESSMENT_PLAN.curie('relevant_evidence'),
                   model_uri=OSCAL.relevant_evidence, domain=None, range=Optional[Union[Union[dict, RelevantEvidence], list[Union[dict, RelevantEvidence]]]])

slots.collected = Slot(uri=OSCAL_ASSESSMENT_PLAN.collected, name="collected", curie=OSCAL_ASSESSMENT_PLAN.curie('collected'),
                   model_uri=OSCAL.collected, domain=None, range=Optional[str])

slots.expires = Slot(uri=OSCAL_ASSESSMENT_PLAN.expires, name="expires", curie=OSCAL_ASSESSMENT_PLAN.curie('expires'),
                   model_uri=OSCAL.expires, domain=None, range=Optional[str])

slots.target = Slot(uri=OSCAL_ASSESSMENT_PLAN.target, name="target", curie=OSCAL_ASSESSMENT_PLAN.curie('target'),
                   model_uri=OSCAL.target, domain=None, range=Optional[Union[dict, FindingTarget]])

slots.implementation_statement_uuid = Slot(uri=OSCAL_ASSESSMENT_PLAN.implementation_statement_uuid, name="implementation-statement-uuid", curie=OSCAL_ASSESSMENT_PLAN.curie('implementation_statement_uuid'),
                   model_uri=OSCAL.implementation_statement_uuid, domain=None, range=Optional[str])

slots.related_risks = Slot(uri=OSCAL_ASSESSMENT_PLAN.related_risks, name="related-risks", curie=OSCAL_ASSESSMENT_PLAN.curie('related_risks'),
                   model_uri=OSCAL.related_risks, domain=None, range=Optional[Union[Union[dict, AssociatedRisk], list[Union[dict, AssociatedRisk]]]])

slots.target_id = Slot(uri=OSCAL_ASSESSMENT_PLAN.target_id, name="target-id", curie=OSCAL_ASSESSMENT_PLAN.curie('target_id'),
                   model_uri=OSCAL.target_id, domain=None, range=Optional[str])

slots.implementation_status = Slot(uri=OSCAL_ASSESSMENT_PLAN.implementation_status, name="implementation-status", curie=OSCAL_ASSESSMENT_PLAN.curie('implementation_status'),
                   model_uri=OSCAL.implementation_status, domain=None, range=Optional[Union[dict, ImplementationStatus]])

slots.reason = Slot(uri=OSCAL_ASSESSMENT_PLAN.reason, name="reason", curie=OSCAL_ASSESSMENT_PLAN.curie('reason'),
                   model_uri=OSCAL.reason, domain=None, range=Optional[str])

slots.observation_uuid = Slot(uri=OSCAL_ASSESSMENT_PLAN.observation_uuid, name="observation-uuid", curie=OSCAL_ASSESSMENT_PLAN.curie('observation_uuid'),
                   model_uri=OSCAL.observation_uuid, domain=None, range=Optional[str])

slots.risk_uuid = Slot(uri=OSCAL_ASSESSMENT_PLAN.risk_uuid, name="risk-uuid", curie=OSCAL_ASSESSMENT_PLAN.curie('risk_uuid'),
                   model_uri=OSCAL.risk_uuid, domain=None, range=Optional[str])

slots.statement = Slot(uri=OSCAL_ASSESSMENT_PLAN.statement, name="statement", curie=OSCAL_ASSESSMENT_PLAN.curie('statement'),
                   model_uri=OSCAL.statement, domain=None, range=Optional[str])

slots.threat_ids = Slot(uri=OSCAL_ASSESSMENT_PLAN.threat_ids, name="threat-ids", curie=OSCAL_ASSESSMENT_PLAN.curie('threat_ids'),
                   model_uri=OSCAL.threat_ids, domain=None, range=Optional[Union[Union[dict, ThreatId], list[Union[dict, ThreatId]]]])

slots.characterizations = Slot(uri=OSCAL_ASSESSMENT_PLAN.characterizations, name="characterizations", curie=OSCAL_ASSESSMENT_PLAN.curie('characterizations'),
                   model_uri=OSCAL.characterizations, domain=None, range=Optional[Union[Union[dict, Characterization], list[Union[dict, Characterization]]]])

slots.mitigating_factors = Slot(uri=OSCAL_ASSESSMENT_PLAN.mitigating_factors, name="mitigating-factors", curie=OSCAL_ASSESSMENT_PLAN.curie('mitigating_factors'),
                   model_uri=OSCAL.mitigating_factors, domain=None, range=Optional[Union[Union[dict, MitigatingFactor], list[Union[dict, MitigatingFactor]]]])

slots.deadline = Slot(uri=OSCAL_ASSESSMENT_PLAN.deadline, name="deadline", curie=OSCAL_ASSESSMENT_PLAN.curie('deadline'),
                   model_uri=OSCAL.deadline, domain=None, range=Optional[str])

slots.remediations = Slot(uri=OSCAL_ASSESSMENT_PLAN.remediations, name="remediations", curie=OSCAL_ASSESSMENT_PLAN.curie('remediations'),
                   model_uri=OSCAL.remediations, domain=None, range=Optional[Union[Union[dict, Response], list[Union[dict, Response]]]])

slots.risk_log = Slot(uri=OSCAL_ASSESSMENT_PLAN.risk_log, name="risk-log", curie=OSCAL_ASSESSMENT_PLAN.curie('risk_log'),
                   model_uri=OSCAL.risk_log, domain=None, range=Optional[Union[dict, RiskLog]])

slots.origin = Slot(uri=OSCAL_ASSESSMENT_PLAN.origin, name="origin", curie=OSCAL_ASSESSMENT_PLAN.curie('origin'),
                   model_uri=OSCAL.origin, domain=None, range=Optional[Union[dict, Origin]])

slots.facets = Slot(uri=OSCAL_ASSESSMENT_PLAN.facets, name="facets", curie=OSCAL_ASSESSMENT_PLAN.curie('facets'),
                   model_uri=OSCAL.facets, domain=None, range=Optional[Union[Union[dict, Facet], list[Union[dict, Facet]]]])

slots.implementation_uuid = Slot(uri=OSCAL_ASSESSMENT_PLAN.implementation_uuid, name="implementation-uuid", curie=OSCAL_ASSESSMENT_PLAN.curie('implementation_uuid'),
                   model_uri=OSCAL.implementation_uuid, domain=None, range=Optional[str])

slots.lifecycle = Slot(uri=OSCAL_ASSESSMENT_PLAN.lifecycle, name="lifecycle", curie=OSCAL_ASSESSMENT_PLAN.curie('lifecycle'),
                   model_uri=OSCAL.lifecycle, domain=None, range=Optional[str])

slots.required_assets = Slot(uri=OSCAL_ASSESSMENT_PLAN.required_assets, name="required-assets", curie=OSCAL_ASSESSMENT_PLAN.curie('required_assets'),
                   model_uri=OSCAL.required_assets, domain=None, range=Optional[Union[Union[dict, RequiredAsset], list[Union[dict, RequiredAsset]]]])

slots.entries = Slot(uri=OSCAL_ASSESSMENT_PLAN.entries, name="entries", curie=OSCAL_ASSESSMENT_PLAN.curie('entries'),
                   model_uri=OSCAL.entries, domain=None, range=Optional[Union[Union[dict, RiskLogEntry], list[Union[dict, RiskLogEntry]]]])

slots.logged_by = Slot(uri=OSCAL_ASSESSMENT_PLAN.logged_by, name="logged-by", curie=OSCAL_ASSESSMENT_PLAN.curie('logged_by'),
                   model_uri=OSCAL.logged_by, domain=None, range=Optional[Union[Union[dict, LoggedBy], list[Union[dict, LoggedBy]]]])

slots.status_change = Slot(uri=OSCAL_ASSESSMENT_PLAN.status_change, name="status-change", curie=OSCAL_ASSESSMENT_PLAN.curie('status_change'),
                   model_uri=OSCAL.status_change, domain=None, range=Optional[str])

slots.related_responses = Slot(uri=OSCAL_ASSESSMENT_PLAN.related_responses, name="related-responses", curie=OSCAL_ASSESSMENT_PLAN.curie('related_responses'),
                   model_uri=OSCAL.related_responses, domain=None, range=Optional[Union[Union[dict, RiskResponseReference], list[Union[dict, RiskResponseReference]]]])

slots.party_uuid = Slot(uri=OSCAL_ASSESSMENT_PLAN.party_uuid, name="party-uuid", curie=OSCAL_ASSESSMENT_PLAN.curie('party_uuid'),
                   model_uri=OSCAL.party_uuid, domain=None, range=Optional[str])

slots.response_uuid = Slot(uri=OSCAL_ASSESSMENT_PLAN.response_uuid, name="response-uuid", curie=OSCAL_ASSESSMENT_PLAN.curie('response_uuid'),
                   model_uri=OSCAL.response_uuid, domain=None, range=Optional[str])

slots.assessment_results = Slot(uri=OSCAL_ASSESSMENT_RESULTS.assessment_results, name="assessment-results", curie=OSCAL_ASSESSMENT_RESULTS.curie('assessment_results'),
                   model_uri=OSCAL.assessment_results, domain=None, range=Optional[Union[dict, AssessmentResults]])

slots.import_ap = Slot(uri=OSCAL_ASSESSMENT_RESULTS.import_ap, name="import-ap", curie=OSCAL_ASSESSMENT_RESULTS.curie('import_ap'),
                   model_uri=OSCAL.import_ap, domain=None, range=Optional[Union[dict, ImportAssessmentPlan]])

slots.results = Slot(uri=OSCAL_ASSESSMENT_RESULTS.results, name="results", curie=OSCAL_ASSESSMENT_RESULTS.curie('results'),
                   model_uri=OSCAL.results, domain=None, range=Optional[Union[Union[dict, Result], list[Union[dict, Result]]]])

slots.attestations = Slot(uri=OSCAL_ASSESSMENT_RESULTS.attestations, name="attestations", curie=OSCAL_ASSESSMENT_RESULTS.curie('attestations'),
                   model_uri=OSCAL.attestations, domain=None, range=Optional[Union[Union[dict, Attestation], list[Union[dict, Attestation]]]])

slots.assessment_log = Slot(uri=OSCAL_ASSESSMENT_RESULTS.assessment_log, name="assessment-log", curie=OSCAL_ASSESSMENT_RESULTS.curie('assessment_log'),
                   model_uri=OSCAL.assessment_log, domain=None, range=Optional[Union[dict, AssessmentLog]])

slots.component_definition = Slot(uri=OSCAL_COMPONENT.component_definition, name="component-definition", curie=OSCAL_COMPONENT.curie('component_definition'),
                   model_uri=OSCAL.component_definition, domain=None, range=Optional[Union[dict, ComponentDefinition]])

slots.import_component_definitions = Slot(uri=OSCAL_COMPONENT.import_component_definitions, name="import-component-definitions", curie=OSCAL_COMPONENT.curie('import_component_definitions'),
                   model_uri=OSCAL.import_component_definitions, domain=None, range=Optional[Union[Union[dict, ImportComponentDefinition], list[Union[dict, ImportComponentDefinition]]]])

slots.capabilities = Slot(uri=OSCAL_COMPONENT.capabilities, name="capabilities", curie=OSCAL_COMPONENT.curie('capabilities'),
                   model_uri=OSCAL.capabilities, domain=None, range=Optional[Union[Union[dict, Capability], list[Union[dict, Capability]]]])

slots.source = Slot(uri=OSCAL_COMPONENT.source, name="source", curie=OSCAL_COMPONENT.curie('source'),
                   model_uri=OSCAL.source, domain=None, range=Optional[str])

slots.control_implementations = Slot(uri=OSCAL_COMPONENT.control_implementations, name="control-implementations", curie=OSCAL_COMPONENT.curie('control_implementations'),
                   model_uri=OSCAL.control_implementations, domain=None, range=Optional[Union[Union[dict, ControlImplementationSet], list[Union[dict, ControlImplementationSet]]]])

slots.incorporates_components = Slot(uri=OSCAL_COMPONENT.incorporates_components, name="incorporates-components", curie=OSCAL_COMPONENT.curie('incorporates_components'),
                   model_uri=OSCAL.incorporates_components, domain=None, range=Optional[Union[Union[dict, IncorporatesComponent], list[Union[dict, IncorporatesComponent]]]])

slots.mapping_collection = Slot(uri=OSCAL_MAPPING.mapping_collection, name="mapping-collection", curie=OSCAL_MAPPING.curie('mapping_collection'),
                   model_uri=OSCAL.mapping_collection, domain=None, range=Optional[Union[dict, MappingCollection]])

slots.provenance = Slot(uri=OSCAL_MAPPING.provenance, name="provenance", curie=OSCAL_MAPPING.curie('provenance'),
                   model_uri=OSCAL.provenance, domain=None, range=Optional[Union[dict, MappingProvenance]])

slots.mappings = Slot(uri=OSCAL_MAPPING.mappings, name="mappings", curie=OSCAL_MAPPING.curie('mappings'),
                   model_uri=OSCAL.mappings, domain=None, range=Optional[Union[Union[dict, Mapping], list[Union[dict, Mapping]]]])

slots.matching_rationale = Slot(uri=OSCAL_MAPPING.matching_rationale, name="matching-rationale", curie=OSCAL_MAPPING.curie('matching_rationale'),
                   model_uri=OSCAL.matching_rationale, domain=None, range=Optional[Union[str, "MatchingRationaleEnum"]])

slots.source_resource = Slot(uri=OSCAL_MAPPING.source_resource, name="source-resource", curie=OSCAL_MAPPING.curie('source_resource'),
                   model_uri=OSCAL.source_resource, domain=None, range=Optional[Union[dict, MappingResourceReference]])

slots.target_resource = Slot(uri=OSCAL_MAPPING.target_resource, name="target-resource", curie=OSCAL_MAPPING.curie('target_resource'),
                   model_uri=OSCAL.target_resource, domain=None, range=Optional[Union[dict, MappingResourceReference]])

slots.maps = Slot(uri=OSCAL_MAPPING.maps, name="maps", curie=OSCAL_MAPPING.curie('maps'),
                   model_uri=OSCAL.maps, domain=None, range=Optional[Union[Union[dict, Map], list[Union[dict, Map]]]])

slots.mapping_description = Slot(uri=OSCAL_MAPPING.mapping_description, name="mapping-description", curie=OSCAL_MAPPING.curie('mapping_description'),
                   model_uri=OSCAL.mapping_description, domain=None, range=Optional[str])

slots.source_gap_summary = Slot(uri=OSCAL_MAPPING.source_gap_summary, name="source-gap-summary", curie=OSCAL_MAPPING.curie('source_gap_summary'),
                   model_uri=OSCAL.source_gap_summary, domain=None, range=Optional[Union[dict, GapSummary]])

slots.target_gap_summary = Slot(uri=OSCAL_MAPPING.target_gap_summary, name="target-gap-summary", curie=OSCAL_MAPPING.curie('target_gap_summary'),
                   model_uri=OSCAL.target_gap_summary, domain=None, range=Optional[Union[dict, GapSummary]])

slots.confidence_score = Slot(uri=OSCAL_MAPPING.confidence_score, name="confidence-score", curie=OSCAL_MAPPING.curie('confidence_score'),
                   model_uri=OSCAL.confidence_score, domain=None, range=Optional[Union[dict, ConfidenceScore]])

slots.coverage = Slot(uri=OSCAL_MAPPING.coverage, name="coverage", curie=OSCAL_MAPPING.curie('coverage'),
                   model_uri=OSCAL.coverage, domain=None, range=Optional[Union[dict, Coverage]])

slots.relationship = Slot(uri=OSCAL_MAPPING.relationship, name="relationship", curie=OSCAL_MAPPING.curie('relationship'),
                   model_uri=OSCAL.relationship, domain=None, range=Optional[str])

slots.targets = Slot(uri=OSCAL_MAPPING.targets, name="targets", curie=OSCAL_MAPPING.curie('targets'),
                   model_uri=OSCAL.targets, domain=None, range=Optional[Union[Union[dict, MappingItem], list[Union[dict, MappingItem]]]])

slots.qualifiers = Slot(uri=OSCAL_MAPPING.qualifiers, name="qualifiers", curie=OSCAL_MAPPING.curie('qualifiers'),
                   model_uri=OSCAL.qualifiers, domain=None, range=Optional[Union[Union[dict, QualifierItem], list[Union[dict, QualifierItem]]]])

slots.id_ref = Slot(uri=OSCAL_MAPPING.id_ref, name="id-ref", curie=OSCAL_MAPPING.curie('id_ref'),
                   model_uri=OSCAL.id_ref, domain=None, range=Optional[str])

slots.subject = Slot(uri=OSCAL_MAPPING.subject, name="subject", curie=OSCAL_MAPPING.curie('subject'),
                   model_uri=OSCAL.subject, domain=None, range=Optional[Union[str, "QualifierSubjectEnum"]])

slots.predicate = Slot(uri=OSCAL_MAPPING.predicate, name="predicate", curie=OSCAL_MAPPING.curie('predicate'),
                   model_uri=OSCAL.predicate, domain=None, range=Optional[Union[str, "QualifierPredicateEnum"]])

slots.category = Slot(uri=OSCAL_MAPPING.category, name="category", curie=OSCAL_MAPPING.curie('category'),
                   model_uri=OSCAL.category, domain=None, range=Optional[str])

slots.unmapped_controls = Slot(uri=OSCAL_MAPPING.unmapped_controls, name="unmapped-controls", curie=OSCAL_MAPPING.curie('unmapped_controls'),
                   model_uri=OSCAL.unmapped_controls, domain=None, range=Optional[Union[Union[dict, SelectControlById], list[Union[dict, SelectControlById]]]])

slots.percentage = Slot(uri=OSCAL_MAPPING.percentage, name="percentage", curie=OSCAL_MAPPING.curie('percentage'),
                   model_uri=OSCAL.percentage, domain=None, range=Optional[float])

slots.generation_method = Slot(uri=OSCAL_MAPPING.generation_method, name="generation-method", curie=OSCAL_MAPPING.curie('generation_method'),
                   model_uri=OSCAL.generation_method, domain=None, range=Optional[str])

slots.target_coverage = Slot(uri=OSCAL_MAPPING.target_coverage, name="target-coverage", curie=OSCAL_MAPPING.curie('target_coverage'),
                   model_uri=OSCAL.target_coverage, domain=None, range=Optional[float])

slots.plan_of_action_and_milestones = Slot(uri=OSCAL_POAM.plan_of_action_and_milestones, name="plan-of-action-and-milestones", curie=OSCAL_POAM.curie('plan_of_action_and_milestones'),
                   model_uri=OSCAL.plan_of_action_and_milestones, domain=None, range=Optional[Union[dict, PlanOfActionAndMilestones]])

slots.system_id = Slot(uri=OSCAL_POAM.system_id, name="system-id", curie=OSCAL_POAM.curie('system_id'),
                   model_uri=OSCAL.system_id, domain=None, range=Optional[Union[dict, SystemId]])

slots.poam_items = Slot(uri=OSCAL_POAM.poam_items, name="poam-items", curie=OSCAL_POAM.curie('poam_items'),
                   model_uri=OSCAL.poam_items, domain=None, range=Optional[Union[Union[dict, PoamItem], list[Union[dict, PoamItem]]]])

slots.related_findings = Slot(uri=OSCAL_POAM.related_findings, name="related-findings", curie=OSCAL_POAM.curie('related_findings'),
                   model_uri=OSCAL.related_findings, domain=None, range=Optional[Union[Union[dict, RelatedFinding], list[Union[dict, RelatedFinding]]]])

slots.finding_uuid = Slot(uri=OSCAL_POAM.finding_uuid, name="finding-uuid", curie=OSCAL_POAM.curie('finding_uuid'),
                   model_uri=OSCAL.finding_uuid, domain=None, range=Optional[str])

slots.informationTypeCategorization__system = Slot(uri=OSCAL_SSP.system, name="informationTypeCategorization__system", curie=OSCAL_SSP.curie('system'),
                   model_uri=OSCAL.informationTypeCategorization__system, domain=None, range=str)

slots.informationTypeCategorization__information_type_ids = Slot(uri=OSCAL_SSP.information_type_ids, name="informationTypeCategorization__information_type_ids", curie=OSCAL_SSP.curie('information_type_ids'),
                   model_uri=OSCAL.informationTypeCategorization__information_type_ids, domain=None, range=Optional[Union[str, list[str]]])

slots.systemStatus__state = Slot(uri=OSCAL_SSP.state, name="systemStatus__state", curie=OSCAL_SSP.curie('state'),
                   model_uri=OSCAL.systemStatus__state, domain=None, range=Union[str, "SystemOperatingStatusEnum"])

slots.CatalogDocument_catalog = Slot(uri=OSCAL_CATALOG.catalog, name="CatalogDocument_catalog", curie=OSCAL_CATALOG.curie('catalog'),
                   model_uri=OSCAL.CatalogDocument_catalog, domain=CatalogDocument, range=Union[dict, "Catalog"])

slots.Catalog_uuid = Slot(uri=OSCAL_CATALOG.uuid, name="Catalog_uuid", curie=OSCAL_CATALOG.curie('uuid'),
                   model_uri=OSCAL.Catalog_uuid, domain=Catalog, range=str)

slots.Catalog_metadata = Slot(uri=OSCAL_CATALOG.metadata, name="Catalog_metadata", curie=OSCAL_CATALOG.curie('metadata'),
                   model_uri=OSCAL.Catalog_metadata, domain=Catalog, range=Union[dict, "Metadata"])

slots.Group_id = Slot(uri=OSCAL_CATALOG.id, name="Group_id", curie=OSCAL_CATALOG.curie('id'),
                   model_uri=OSCAL.Group_id, domain=Group, range=Optional[str])

slots.Group__class = Slot(uri=OSCAL_CATALOG._class, name="Group__class", curie=OSCAL_CATALOG.curie('_class'),
                   model_uri=OSCAL.Group__class, domain=Group, range=Optional[str])

slots.Group_title = Slot(uri=OSCAL_CATALOG.title, name="Group_title", curie=OSCAL_CATALOG.curie('title'),
                   model_uri=OSCAL.Group_title, domain=Group, range=str)

slots.Control_id = Slot(uri=OSCAL_CATALOG.id, name="Control_id", curie=OSCAL_CATALOG.curie('id'),
                   model_uri=OSCAL.Control_id, domain=Control, range=str)

slots.Control__class = Slot(uri=OSCAL_CATALOG._class, name="Control__class", curie=OSCAL_CATALOG.curie('_class'),
                   model_uri=OSCAL.Control__class, domain=Control, range=Optional[str])

slots.Control_title = Slot(uri=OSCAL_CATALOG.title, name="Control_title", curie=OSCAL_CATALOG.curie('title'),
                   model_uri=OSCAL.Control_title, domain=Control, range=str)

slots.Metadata_title = Slot(uri=OSCAL_CATALOG.title, name="Metadata_title", curie=OSCAL_CATALOG.curie('title'),
                   model_uri=OSCAL.Metadata_title, domain=Metadata, range=str)

slots.Metadata_last_modified = Slot(uri=OSCAL_CATALOG.last_modified, name="Metadata_last-modified", curie=OSCAL_CATALOG.curie('last_modified'),
                   model_uri=OSCAL.Metadata_last_modified, domain=Metadata, range=str)

slots.Metadata_version = Slot(uri=OSCAL_CATALOG.version, name="Metadata_version", curie=OSCAL_CATALOG.curie('version'),
                   model_uri=OSCAL.Metadata_version, domain=Metadata, range=str)

slots.Metadata_oscal_version = Slot(uri=OSCAL_CATALOG.oscal_version, name="Metadata_oscal-version", curie=OSCAL_CATALOG.curie('oscal_version'),
                   model_uri=OSCAL.Metadata_oscal_version, domain=Metadata, range=str)

slots.Metadata_props = Slot(uri=OSCAL_CATALOG.props, name="Metadata_props", curie=OSCAL_CATALOG.curie('props'),
                   model_uri=OSCAL.Metadata_props, domain=Metadata, range=Optional[Union[Union[dict, "MetadataProperty"], list[Union[dict, "MetadataProperty"]]]])

slots.Metadata_links = Slot(uri=OSCAL_CATALOG.links, name="Metadata_links", curie=OSCAL_CATALOG.curie('links'),
                   model_uri=OSCAL.Metadata_links, domain=Metadata, range=Optional[Union[Union[dict, "Link"], list[Union[dict, "Link"]]]])

slots.Revision_version = Slot(uri=OSCAL_CATALOG.version, name="Revision_version", curie=OSCAL_CATALOG.curie('version'),
                   model_uri=OSCAL.Revision_version, domain=Revision, range=str)

slots.Revision_props = Slot(uri=OSCAL_CATALOG.props, name="Revision_props", curie=OSCAL_CATALOG.curie('props'),
                   model_uri=OSCAL.Revision_props, domain=Revision, range=Optional[Union[Union[dict, "RevisionProperty"], list[Union[dict, "RevisionProperty"]]]])

slots.Revision_links = Slot(uri=OSCAL_CATALOG.links, name="Revision_links", curie=OSCAL_CATALOG.curie('links'),
                   model_uri=OSCAL.Revision_links, domain=Revision, range=Optional[Union[Union[dict, "Link"], list[Union[dict, "Link"]]]])

slots.DocumentId_scheme = Slot(uri=OSCAL_CATALOG.scheme, name="DocumentId_scheme", curie=OSCAL_CATALOG.curie('scheme'),
                   model_uri=OSCAL.DocumentId_scheme, domain=DocumentId, range=Optional[str])

slots.DocumentId_identifier = Slot(uri=OSCAL_CATALOG.identifier, name="DocumentId_identifier", curie=OSCAL_CATALOG.curie('identifier'),
                   model_uri=OSCAL.DocumentId_identifier, domain=DocumentId, range=str)

slots.Role_id = Slot(uri=OSCAL_CATALOG.id, name="Role_id", curie=OSCAL_CATALOG.curie('id'),
                   model_uri=OSCAL.Role_id, domain=Role, range=str)

slots.Role_title = Slot(uri=OSCAL_CATALOG.title, name="Role_title", curie=OSCAL_CATALOG.curie('title'),
                   model_uri=OSCAL.Role_title, domain=Role, range=str)

slots.Location_uuid = Slot(uri=OSCAL_CATALOG.uuid, name="Location_uuid", curie=OSCAL_CATALOG.curie('uuid'),
                   model_uri=OSCAL.Location_uuid, domain=Location, range=str)

slots.Location_props = Slot(uri=OSCAL_CATALOG.props, name="Location_props", curie=OSCAL_CATALOG.curie('props'),
                   model_uri=OSCAL.Location_props, domain=Location, range=Optional[Union[Union[dict, "LocationProperty"], list[Union[dict, "LocationProperty"]]]])

slots.Party_uuid = Slot(uri=OSCAL_CATALOG.uuid, name="Party_uuid", curie=OSCAL_CATALOG.curie('uuid'),
                   model_uri=OSCAL.Party_uuid, domain=Party, range=str)

slots.Party_type = Slot(uri=OSCAL_CATALOG.type, name="Party_type", curie=OSCAL_CATALOG.curie('type'),
                   model_uri=OSCAL.Party_type, domain=Party, range=Union[str, "PartyTypeEnum"])

slots.Party_name = Slot(uri=OSCAL_CATALOG.name, name="Party_name", curie=OSCAL_CATALOG.curie('name'),
                   model_uri=OSCAL.Party_name, domain=Party, range=Optional[str])

slots.Party_props = Slot(uri=OSCAL_CATALOG.props, name="Party_props", curie=OSCAL_CATALOG.curie('props'),
                   model_uri=OSCAL.Party_props, domain=Party, range=Optional[Union[Union[dict, "PartyProperty"], list[Union[dict, "PartyProperty"]]]])

slots.Party_external_ids = Slot(uri=OSCAL_CATALOG.external_ids, name="Party_external-ids", curie=OSCAL_CATALOG.curie('external_ids'),
                   model_uri=OSCAL.Party_external_ids, domain=Party, range=Optional[Union[Union[dict, "MetadataPartyExternalId"], list[Union[dict, "MetadataPartyExternalId"]]]])

slots.PartyExternalId_scheme = Slot(uri=OSCAL_CATALOG.scheme, name="PartyExternalId_scheme", curie=OSCAL_CATALOG.curie('scheme'),
                   model_uri=OSCAL.PartyExternalId_scheme, domain=PartyExternalId, range=str)

slots.PartyExternalId_id = Slot(uri=OSCAL_CATALOG.id, name="PartyExternalId_id", curie=OSCAL_CATALOG.curie('id'),
                   model_uri=OSCAL.PartyExternalId_id, domain=PartyExternalId, range=str)

slots.ResponsibleParty_role_id = Slot(uri=OSCAL_CATALOG.role_id, name="ResponsibleParty_role-id", curie=OSCAL_CATALOG.curie('role_id'),
                   model_uri=OSCAL.ResponsibleParty_role_id, domain=ResponsibleParty, range=str)

slots.ResponsibleParty_party_uuids = Slot(uri=OSCAL_CATALOG.party_uuids, name="ResponsibleParty_party-uuids", curie=OSCAL_CATALOG.curie('party_uuids'),
                   model_uri=OSCAL.ResponsibleParty_party_uuids, domain=ResponsibleParty, range=Union[str, list[str]])

slots.ResponsibleRole_role_id = Slot(uri=OSCAL_CATALOG.role_id, name="ResponsibleRole_role-id", curie=OSCAL_CATALOG.curie('role_id'),
                   model_uri=OSCAL.ResponsibleRole_role_id, domain=ResponsibleRole, range=str)

slots.Action_uuid = Slot(uri=OSCAL_CATALOG.uuid, name="Action_uuid", curie=OSCAL_CATALOG.curie('uuid'),
                   model_uri=OSCAL.Action_uuid, domain=Action, range=str)

slots.Action_type = Slot(uri=OSCAL_CATALOG.type, name="Action_type", curie=OSCAL_CATALOG.curie('type'),
                   model_uri=OSCAL.Action_type, domain=Action, range=Union[str, "ActionTypeEnum"])

slots.Action_system = Slot(uri=OSCAL_CATALOG.system, name="Action_system", curie=OSCAL_CATALOG.curie('system'),
                   model_uri=OSCAL.Action_system, domain=Action, range=str)

slots.TelephoneNumber_type = Slot(uri=OSCAL_CATALOG.type, name="TelephoneNumber_type", curie=OSCAL_CATALOG.curie('type'),
                   model_uri=OSCAL.TelephoneNumber_type, domain=TelephoneNumber, range=Optional[str])

slots.TelephoneNumber_number = Slot(uri=OSCAL_CATALOG.number, name="TelephoneNumber_number", curie=OSCAL_CATALOG.curie('number'),
                   model_uri=OSCAL.TelephoneNumber_number, domain=TelephoneNumber, range=str)

slots.Address_type = Slot(uri=OSCAL_CATALOG.type, name="Address_type", curie=OSCAL_CATALOG.curie('type'),
                   model_uri=OSCAL.Address_type, domain=Address, range=Optional[str])

slots.Hash_value = Slot(uri=OSCAL_CATALOG.value, name="Hash_value", curie=OSCAL_CATALOG.curie('value'),
                   model_uri=OSCAL.Hash_value, domain=Hash, range=str)

slots.Hash_algorithm = Slot(uri=OSCAL_CATALOG.algorithm, name="Hash_algorithm", curie=OSCAL_CATALOG.curie('algorithm'),
                   model_uri=OSCAL.Hash_algorithm, domain=Hash, range=str)

slots.Property_name = Slot(uri=OSCAL_CATALOG.name, name="Property_name", curie=OSCAL_CATALOG.curie('name'),
                   model_uri=OSCAL.Property_name, domain=Property, range=str)

slots.Property_uuid = Slot(uri=OSCAL_CATALOG.uuid, name="Property_uuid", curie=OSCAL_CATALOG.curie('uuid'),
                   model_uri=OSCAL.Property_uuid, domain=Property, range=Optional[str])

slots.Property_ns = Slot(uri=OSCAL_CATALOG.ns, name="Property_ns", curie=OSCAL_CATALOG.curie('ns'),
                   model_uri=OSCAL.Property_ns, domain=Property, range=Optional[str])

slots.Property_value = Slot(uri=OSCAL_CATALOG.value, name="Property_value", curie=OSCAL_CATALOG.curie('value'),
                   model_uri=OSCAL.Property_value, domain=Property, range=str)

slots.Property__class = Slot(uri=OSCAL_CATALOG._class, name="Property__class", curie=OSCAL_CATALOG.curie('_class'),
                   model_uri=OSCAL.Property__class, domain=Property, range=Optional[str])

slots.MetadataProperty_name = Slot(uri=OSCAL_CATALOG.name, name="MetadataProperty_name", curie=OSCAL_CATALOG.curie('name'),
                   model_uri=OSCAL.MetadataProperty_name, domain=MetadataProperty, range=Union[str, "MetadataPropNameEnum"])

slots.RevisionProperty_name = Slot(uri=OSCAL_CATALOG.name, name="RevisionProperty_name", curie=OSCAL_CATALOG.curie('name'),
                   model_uri=OSCAL.RevisionProperty_name, domain=RevisionProperty, range=Union[str, "RevisionPropNameEnum"])

slots.LocationProperty_name = Slot(uri=OSCAL_CATALOG.name, name="LocationProperty_name", curie=OSCAL_CATALOG.curie('name'),
                   model_uri=OSCAL.LocationProperty_name, domain=LocationProperty, range=Union[str, "LocationPropNameEnum"])

slots.LocationProperty_value = Slot(uri=OSCAL_CATALOG.value, name="LocationProperty_value", curie=OSCAL_CATALOG.curie('value'),
                   model_uri=OSCAL.LocationProperty_value, domain=LocationProperty, range=str)

slots.LocationProperty__class = Slot(uri=OSCAL_CATALOG._class, name="LocationProperty__class", curie=OSCAL_CATALOG.curie('_class'),
                   model_uri=OSCAL.LocationProperty__class, domain=LocationProperty, range=Optional[str])

slots.PartyProperty_name = Slot(uri=OSCAL_CATALOG.name, name="PartyProperty_name", curie=OSCAL_CATALOG.curie('name'),
                   model_uri=OSCAL.PartyProperty_name, domain=PartyProperty, range=Union[str, "PartyPropNameEnum"])

slots.ResourceProperty_name = Slot(uri=OSCAL_CATALOG.name, name="ResourceProperty_name", curie=OSCAL_CATALOG.curie('name'),
                   model_uri=OSCAL.ResourceProperty_name, domain=ResourceProperty, range=Union[str, "ResourcePropNameEnum"])

slots.ResourceProperty_value = Slot(uri=OSCAL_CATALOG.value, name="ResourceProperty_value", curie=OSCAL_CATALOG.curie('value'),
                   model_uri=OSCAL.ResourceProperty_value, domain=ResourceProperty, range=str)

slots.PartProperty_name = Slot(uri=OSCAL_CATALOG.name, name="PartProperty_name", curie=OSCAL_CATALOG.curie('name'),
                   model_uri=OSCAL.PartProperty_name, domain=PartProperty, range=Union[str, "PartPropNameEnum"])

slots.ParameterProperty_name = Slot(uri=OSCAL_CATALOG.name, name="ParameterProperty_name", curie=OSCAL_CATALOG.curie('name'),
                   model_uri=OSCAL.ParameterProperty_name, domain=ParameterProperty, range=str)

slots.Link_href = Slot(uri=OSCAL_CATALOG.href, name="Link_href", curie=OSCAL_CATALOG.curie('href'),
                   model_uri=OSCAL.Link_href, domain=Link, range=str)

slots.Link_rel = Slot(uri=OSCAL_CATALOG.rel, name="Link_rel", curie=OSCAL_CATALOG.curie('rel'),
                   model_uri=OSCAL.Link_rel, domain=Link, range=Optional[str])

slots.Resource_uuid = Slot(uri=OSCAL_CATALOG.uuid, name="Resource_uuid", curie=OSCAL_CATALOG.curie('uuid'),
                   model_uri=OSCAL.Resource_uuid, domain=Resource, range=str)

slots.Resource_title = Slot(uri=OSCAL_CATALOG.title, name="Resource_title", curie=OSCAL_CATALOG.curie('title'),
                   model_uri=OSCAL.Resource_title, domain=Resource, range=Optional[str])

slots.Resource_description = Slot(uri=OSCAL_CATALOG.description, name="Resource_description", curie=OSCAL_CATALOG.curie('description'),
                   model_uri=OSCAL.Resource_description, domain=Resource, range=Optional[str])

slots.Resource_props = Slot(uri=OSCAL_CATALOG.props, name="Resource_props", curie=OSCAL_CATALOG.curie('props'),
                   model_uri=OSCAL.Resource_props, domain=Resource, range=Optional[Union[Union[dict, ResourceProperty], list[Union[dict, ResourceProperty]]]])

slots.Resource_document_ids = Slot(uri=OSCAL_CATALOG.document_ids, name="Resource_document-ids", curie=OSCAL_CATALOG.curie('document_ids'),
                   model_uri=OSCAL.Resource_document_ids, domain=Resource, range=Optional[Union[Union[dict, DocumentId], list[Union[dict, DocumentId]]]])

slots.Citation_text = Slot(uri=OSCAL_CATALOG.text, name="Citation_text", curie=OSCAL_CATALOG.curie('text'),
                   model_uri=OSCAL.Citation_text, domain=Citation, range=str)

slots.Citation_links = Slot(uri=OSCAL_CATALOG.links, name="Citation_links", curie=OSCAL_CATALOG.curie('links'),
                   model_uri=OSCAL.Citation_links, domain=Citation, range=Optional[Union[Union[dict, Link], list[Union[dict, Link]]]])

slots.ResourceLink_href = Slot(uri=OSCAL_CATALOG.href, name="ResourceLink_href", curie=OSCAL_CATALOG.curie('href'),
                   model_uri=OSCAL.ResourceLink_href, domain=ResourceLink, range=str)

slots.Base64Resource_value = Slot(uri=OSCAL_CATALOG.value, name="Base64Resource_value", curie=OSCAL_CATALOG.curie('value'),
                   model_uri=OSCAL.Base64Resource_value, domain=Base64Resource, range=str)

slots.Part_id = Slot(uri=OSCAL_CATALOG.id, name="Part_id", curie=OSCAL_CATALOG.curie('id'),
                   model_uri=OSCAL.Part_id, domain=Part, range=Optional[str])

slots.Part_name = Slot(uri=OSCAL_CATALOG.name, name="Part_name", curie=OSCAL_CATALOG.curie('name'),
                   model_uri=OSCAL.Part_name, domain=Part, range=str)

slots.Part_ns = Slot(uri=OSCAL_CATALOG.ns, name="Part_ns", curie=OSCAL_CATALOG.curie('ns'),
                   model_uri=OSCAL.Part_ns, domain=Part, range=Optional[str])

slots.Part__class = Slot(uri=OSCAL_CATALOG._class, name="Part__class", curie=OSCAL_CATALOG.curie('_class'),
                   model_uri=OSCAL.Part__class, domain=Part, range=Optional[str])

slots.Part_title = Slot(uri=OSCAL_CATALOG.title, name="Part_title", curie=OSCAL_CATALOG.curie('title'),
                   model_uri=OSCAL.Part_title, domain=Part, range=Optional[str])

slots.Part_prose = Slot(uri=OSCAL_CATALOG.prose, name="Part_prose", curie=OSCAL_CATALOG.curie('prose'),
                   model_uri=OSCAL.Part_prose, domain=Part, range=Optional[str])

slots.Part_props = Slot(uri=OSCAL_CATALOG.props, name="Part_props", curie=OSCAL_CATALOG.curie('props'),
                   model_uri=OSCAL.Part_props, domain=Part, range=Optional[Union[Union[dict, PartProperty], list[Union[dict, PartProperty]]]])

slots.Parameter_id = Slot(uri=OSCAL_CATALOG.id, name="Parameter_id", curie=OSCAL_CATALOG.curie('id'),
                   model_uri=OSCAL.Parameter_id, domain=Parameter, range=str)

slots.Parameter__class = Slot(uri=OSCAL_CATALOG._class, name="Parameter__class", curie=OSCAL_CATALOG.curie('_class'),
                   model_uri=OSCAL.Parameter__class, domain=Parameter, range=Optional[str])

slots.Parameter_props = Slot(uri=OSCAL_CATALOG.props, name="Parameter_props", curie=OSCAL_CATALOG.curie('props'),
                   model_uri=OSCAL.Parameter_props, domain=Parameter, range=Optional[Union[Union[dict, ParameterProperty], list[Union[dict, ParameterProperty]]]])

slots.ParameterConstraint_description = Slot(uri=OSCAL_CATALOG.description, name="ParameterConstraint_description", curie=OSCAL_CATALOG.curie('description'),
                   model_uri=OSCAL.ParameterConstraint_description, domain=ParameterConstraint, range=Optional[str])

slots.ConstraintTest_expression = Slot(uri=OSCAL_CATALOG.expression, name="ConstraintTest_expression", curie=OSCAL_CATALOG.curie('expression'),
                   model_uri=OSCAL.ConstraintTest_expression, domain=ConstraintTest, range=str)

slots.ParameterGuideline_prose = Slot(uri=OSCAL_CATALOG.prose, name="ParameterGuideline_prose", curie=OSCAL_CATALOG.curie('prose'),
                   model_uri=OSCAL.ParameterGuideline_prose, domain=ParameterGuideline, range=str)

slots.ProfileDocument_profile = Slot(uri=OSCAL_PROFILE.profile, name="ProfileDocument_profile", curie=OSCAL_PROFILE.curie('profile'),
                   model_uri=OSCAL.ProfileDocument_profile, domain=ProfileDocument, range=Union[dict, "Profile"])

slots.Profile_uuid = Slot(uri=OSCAL_CATALOG.uuid, name="Profile_uuid", curie=OSCAL_CATALOG.curie('uuid'),
                   model_uri=OSCAL.Profile_uuid, domain=Profile, range=str)

slots.Profile_metadata = Slot(uri=OSCAL_CATALOG.metadata, name="Profile_metadata", curie=OSCAL_CATALOG.curie('metadata'),
                   model_uri=OSCAL.Profile_metadata, domain=Profile, range=Union[dict, Metadata])

slots.Profile_imports = Slot(uri=OSCAL_PROFILE.imports, name="Profile_imports", curie=OSCAL_PROFILE.curie('imports'),
                   model_uri=OSCAL.Profile_imports, domain=Profile, range=Union[Union[dict, "ProfileImport"], list[Union[dict, "ProfileImport"]]])

slots.ProfileImport_href = Slot(uri=OSCAL_CATALOG.href, name="ProfileImport_href", curie=OSCAL_CATALOG.curie('href'),
                   model_uri=OSCAL.ProfileImport_href, domain=ProfileImport, range=str)

slots.ProfileImport_include_controls = Slot(uri=OSCAL_CATALOG.include_controls, name="ProfileImport_include-controls", curie=OSCAL_CATALOG.curie('include_controls'),
                   model_uri=OSCAL.ProfileImport_include_controls, domain=ProfileImport, range=Optional[Union[Union[dict, SelectControlById], list[Union[dict, SelectControlById]]]])

slots.ProfileImport_exclude_controls = Slot(uri=OSCAL_CATALOG.exclude_controls, name="ProfileImport_exclude-controls", curie=OSCAL_CATALOG.curie('exclude_controls'),
                   model_uri=OSCAL.ProfileImport_exclude_controls, domain=ProfileImport, range=Optional[Union[Union[dict, SelectControlById], list[Union[dict, SelectControlById]]]])

slots.CombinationRule_method = Slot(uri=OSCAL_CATALOG.method, name="CombinationRule_method", curie=OSCAL_CATALOG.curie('method'),
                   model_uri=OSCAL.CombinationRule_method, domain=CombinationRule, range=Optional[Union[str, "CombinationMethodEnum"]])

slots.MergeCustom_groups = Slot(uri=OSCAL_CATALOG.groups, name="MergeCustom_groups", curie=OSCAL_CATALOG.curie('groups'),
                   model_uri=OSCAL.MergeCustom_groups, domain=MergeCustom, range=Optional[Union[Union[dict, "ProfileGroup"], list[Union[dict, "ProfileGroup"]]]])

slots.ProfileGroup_title = Slot(uri=OSCAL_CATALOG.title, name="ProfileGroup_title", curie=OSCAL_CATALOG.curie('title'),
                   model_uri=OSCAL.ProfileGroup_title, domain=ProfileGroup, range=str)

slots.ProfileGroup_groups = Slot(uri=OSCAL_CATALOG.groups, name="ProfileGroup_groups", curie=OSCAL_CATALOG.curie('groups'),
                   model_uri=OSCAL.ProfileGroup_groups, domain=ProfileGroup, range=Optional[Union[Union[dict, "ProfileGroup"], list[Union[dict, "ProfileGroup"]]]])

slots.ProfileModify_set_parameters = Slot(uri=OSCAL_CATALOG.set_parameters, name="ProfileModify_set-parameters", curie=OSCAL_CATALOG.curie('set_parameters'),
                   model_uri=OSCAL.ProfileModify_set_parameters, domain=ProfileModify, range=Optional[Union[Union[dict, "ParameterSetting"], list[Union[dict, "ParameterSetting"]]]])

slots.ParameterSetting_param_id = Slot(uri=OSCAL_CATALOG.param_id, name="ParameterSetting_param-id", curie=OSCAL_CATALOG.curie('param_id'),
                   model_uri=OSCAL.ParameterSetting_param_id, domain=ParameterSetting, range=str)

slots.Alteration_control_id = Slot(uri=OSCAL_CATALOG.control_id, name="Alteration_control-id", curie=OSCAL_CATALOG.curie('control_id'),
                   model_uri=OSCAL.Alteration_control_id, domain=Alteration, range=str)

slots.Addition_props = Slot(uri=OSCAL_CATALOG.props, name="Addition_props", curie=OSCAL_CATALOG.curie('props'),
                   model_uri=OSCAL.Addition_props, domain=Addition, range=Optional[Union[Union[dict, "ProfileAlterationProperty"], list[Union[dict, "ProfileAlterationProperty"]]]])

slots.ProfileAlterationProperty_name = Slot(uri=OSCAL_CATALOG.name, name="ProfileAlterationProperty_name", curie=OSCAL_CATALOG.curie('name'),
                   model_uri=OSCAL.ProfileAlterationProperty_name, domain=ProfileAlterationProperty, range=Union[str, "AlterationPropNameEnum"])

slots.InsertControls_include_controls = Slot(uri=OSCAL_CATALOG.include_controls, name="InsertControls_include-controls", curie=OSCAL_CATALOG.curie('include_controls'),
                   model_uri=OSCAL.InsertControls_include_controls, domain=InsertControls, range=Optional[Union[Union[dict, SelectControlById], list[Union[dict, SelectControlById]]]])

slots.InsertControls_exclude_controls = Slot(uri=OSCAL_CATALOG.exclude_controls, name="InsertControls_exclude-controls", curie=OSCAL_CATALOG.curie('exclude_controls'),
                   model_uri=OSCAL.InsertControls_exclude_controls, domain=InsertControls, range=Optional[Union[Union[dict, SelectControlById], list[Union[dict, SelectControlById]]]])

slots.SspDocument_system_security_plan = Slot(uri=OSCAL_SSP.system_security_plan, name="SspDocument_system-security-plan", curie=OSCAL_SSP.curie('system_security_plan'),
                   model_uri=OSCAL.SspDocument_system_security_plan, domain=SspDocument, range=Union[dict, "SystemSecurityPlan"])

slots.SystemSecurityPlan_uuid = Slot(uri=OSCAL_CATALOG.uuid, name="SystemSecurityPlan_uuid", curie=OSCAL_CATALOG.curie('uuid'),
                   model_uri=OSCAL.SystemSecurityPlan_uuid, domain=SystemSecurityPlan, range=str)

slots.SystemSecurityPlan_metadata = Slot(uri=OSCAL_CATALOG.metadata, name="SystemSecurityPlan_metadata", curie=OSCAL_CATALOG.curie('metadata'),
                   model_uri=OSCAL.SystemSecurityPlan_metadata, domain=SystemSecurityPlan, range=Union[dict, Metadata])

slots.SystemSecurityPlan_import_profile = Slot(uri=OSCAL_SSP.import_profile, name="SystemSecurityPlan_import-profile", curie=OSCAL_SSP.curie('import_profile'),
                   model_uri=OSCAL.SystemSecurityPlan_import_profile, domain=SystemSecurityPlan, range=Union[dict, "ImportProfile"])

slots.SystemSecurityPlan_system_characteristics = Slot(uri=OSCAL_SSP.system_characteristics, name="SystemSecurityPlan_system-characteristics", curie=OSCAL_SSP.curie('system_characteristics'),
                   model_uri=OSCAL.SystemSecurityPlan_system_characteristics, domain=SystemSecurityPlan, range=Union[dict, "SystemCharacteristics"])

slots.SystemSecurityPlan_system_implementation = Slot(uri=OSCAL_SSP.system_implementation, name="SystemSecurityPlan_system-implementation", curie=OSCAL_SSP.curie('system_implementation'),
                   model_uri=OSCAL.SystemSecurityPlan_system_implementation, domain=SystemSecurityPlan, range=Union[dict, "SystemImplementation"])

slots.SystemSecurityPlan_control_implementation = Slot(uri=OSCAL_SSP.control_implementation, name="SystemSecurityPlan_control-implementation", curie=OSCAL_SSP.curie('control_implementation'),
                   model_uri=OSCAL.SystemSecurityPlan_control_implementation, domain=SystemSecurityPlan, range=Union[dict, "SspControlImplementation"])

slots.ImportProfile_href = Slot(uri=OSCAL_CATALOG.href, name="ImportProfile_href", curie=OSCAL_CATALOG.curie('href'),
                   model_uri=OSCAL.ImportProfile_href, domain=ImportProfile, range=str)

slots.SystemCharacteristics_system_ids = Slot(uri=OSCAL_SSP.system_ids, name="SystemCharacteristics_system-ids", curie=OSCAL_SSP.curie('system_ids'),
                   model_uri=OSCAL.SystemCharacteristics_system_ids, domain=SystemCharacteristics, range=Union[Union[dict, "SystemId"], list[Union[dict, "SystemId"]]])

slots.SystemCharacteristics_system_name = Slot(uri=OSCAL_SSP.system_name, name="SystemCharacteristics_system-name", curie=OSCAL_SSP.curie('system_name'),
                   model_uri=OSCAL.SystemCharacteristics_system_name, domain=SystemCharacteristics, range=str)

slots.SystemCharacteristics_description = Slot(uri=OSCAL_CATALOG.description, name="SystemCharacteristics_description", curie=OSCAL_CATALOG.curie('description'),
                   model_uri=OSCAL.SystemCharacteristics_description, domain=SystemCharacteristics, range=str)

slots.SystemCharacteristics_system_information = Slot(uri=OSCAL_SSP.system_information, name="SystemCharacteristics_system-information", curie=OSCAL_SSP.curie('system_information'),
                   model_uri=OSCAL.SystemCharacteristics_system_information, domain=SystemCharacteristics, range=Union[dict, "SystemInformation"])

slots.SystemCharacteristics_system_status = Slot(uri=OSCAL_SSP.system_status, name="SystemCharacteristics_system-status", curie=OSCAL_SSP.curie('system_status'),
                   model_uri=OSCAL.SystemCharacteristics_system_status, domain=SystemCharacteristics, range=Union[dict, "SystemStatus"])

slots.SystemCharacteristics_authorization_boundary = Slot(uri=OSCAL_SSP.authorization_boundary, name="SystemCharacteristics_authorization-boundary", curie=OSCAL_SSP.curie('authorization_boundary'),
                   model_uri=OSCAL.SystemCharacteristics_authorization_boundary, domain=SystemCharacteristics, range=Union[dict, "AuthorizationBoundary"])

slots.SystemCharacteristics_props = Slot(uri=OSCAL_CATALOG.props, name="SystemCharacteristics_props", curie=OSCAL_CATALOG.curie('props'),
                   model_uri=OSCAL.SystemCharacteristics_props, domain=SystemCharacteristics, range=Optional[Union[Union[dict, "SspSystemCharacteristicsProp"], list[Union[dict, "SspSystemCharacteristicsProp"]]]])

slots.SystemCharacteristics_responsible_parties = Slot(uri=OSCAL_CATALOG.responsible_parties, name="SystemCharacteristics_responsible-parties", curie=OSCAL_CATALOG.curie('responsible_parties'),
                   model_uri=OSCAL.SystemCharacteristics_responsible_parties, domain=SystemCharacteristics, range=Optional[Union[Union[dict, "SspSystemCharacteristicsResponsibleParty"], list[Union[dict, "SspSystemCharacteristicsResponsibleParty"]]]])

slots.SystemInformation_information_types = Slot(uri=OSCAL_SSP.information_types, name="SystemInformation_information-types", curie=OSCAL_SSP.curie('information_types'),
                   model_uri=OSCAL.SystemInformation_information_types, domain=SystemInformation, range=Union[Union[dict, "InformationType"], list[Union[dict, "InformationType"]]])

slots.SystemInformation_props = Slot(uri=OSCAL_CATALOG.props, name="SystemInformation_props", curie=OSCAL_CATALOG.curie('props'),
                   model_uri=OSCAL.SystemInformation_props, domain=SystemInformation, range=Optional[Union[Union[dict, "SspSystemInformationProp"], list[Union[dict, "SspSystemInformationProp"]]]])

slots.SystemInformation_links = Slot(uri=OSCAL_CATALOG.links, name="SystemInformation_links", curie=OSCAL_CATALOG.curie('links'),
                   model_uri=OSCAL.SystemInformation_links, domain=SystemInformation, range=Optional[Union[Union[dict, "SspSystemInformationLink"], list[Union[dict, "SspSystemInformationLink"]]]])

slots.InformationType_title = Slot(uri=OSCAL_CATALOG.title, name="InformationType_title", curie=OSCAL_CATALOG.curie('title'),
                   model_uri=OSCAL.InformationType_title, domain=InformationType, range=str)

slots.InformationType_description = Slot(uri=OSCAL_CATALOG.description, name="InformationType_description", curie=OSCAL_CATALOG.curie('description'),
                   model_uri=OSCAL.InformationType_description, domain=InformationType, range=str)

slots.ImpactLevel_base = Slot(uri=OSCAL_SSP.base, name="ImpactLevel_base", curie=OSCAL_SSP.curie('base'),
                   model_uri=OSCAL.ImpactLevel_base, domain=ImpactLevel, range=str)

slots.ImpactLevel_selected = Slot(uri=OSCAL_SSP.selected, name="ImpactLevel_selected", curie=OSCAL_SSP.curie('selected'),
                   model_uri=OSCAL.ImpactLevel_selected, domain=ImpactLevel, range=Optional[str])

slots.SecurityImpactLevel_security_objective_confidentiality = Slot(uri=OSCAL_SSP.security_objective_confidentiality, name="SecurityImpactLevel_security-objective-confidentiality", curie=OSCAL_SSP.curie('security_objective_confidentiality'),
                   model_uri=OSCAL.SecurityImpactLevel_security_objective_confidentiality, domain=SecurityImpactLevel, range=str)

slots.SecurityImpactLevel_security_objective_integrity = Slot(uri=OSCAL_SSP.security_objective_integrity, name="SecurityImpactLevel_security-objective-integrity", curie=OSCAL_SSP.curie('security_objective_integrity'),
                   model_uri=OSCAL.SecurityImpactLevel_security_objective_integrity, domain=SecurityImpactLevel, range=str)

slots.SecurityImpactLevel_security_objective_availability = Slot(uri=OSCAL_SSP.security_objective_availability, name="SecurityImpactLevel_security-objective-availability", curie=OSCAL_SSP.curie('security_objective_availability'),
                   model_uri=OSCAL.SecurityImpactLevel_security_objective_availability, domain=SecurityImpactLevel, range=str)

slots.AuthorizationBoundary_description = Slot(uri=OSCAL_CATALOG.description, name="AuthorizationBoundary_description", curie=OSCAL_CATALOG.curie('description'),
                   model_uri=OSCAL.AuthorizationBoundary_description, domain=AuthorizationBoundary, range=str)

slots.Diagram_uuid = Slot(uri=OSCAL_CATALOG.uuid, name="Diagram_uuid", curie=OSCAL_CATALOG.curie('uuid'),
                   model_uri=OSCAL.Diagram_uuid, domain=Diagram, range=str)

slots.Diagram_links = Slot(uri=OSCAL_CATALOG.links, name="Diagram_links", curie=OSCAL_CATALOG.curie('links'),
                   model_uri=OSCAL.Diagram_links, domain=Diagram, range=Optional[Union[Union[dict, "SspDiagramLink"], list[Union[dict, "SspDiagramLink"]]]])

slots.NetworkArchitecture_description = Slot(uri=OSCAL_CATALOG.description, name="NetworkArchitecture_description", curie=OSCAL_CATALOG.curie('description'),
                   model_uri=OSCAL.NetworkArchitecture_description, domain=NetworkArchitecture, range=str)

slots.DataFlow_description = Slot(uri=OSCAL_CATALOG.description, name="DataFlow_description", curie=OSCAL_CATALOG.curie('description'),
                   model_uri=OSCAL.DataFlow_description, domain=DataFlow, range=str)

slots.SystemImplementation_components = Slot(uri=OSCAL_ASSESSMENT_PLAN.components, name="SystemImplementation_components", curie=OSCAL_ASSESSMENT_PLAN.curie('components'),
                   model_uri=OSCAL.SystemImplementation_components, domain=SystemImplementation, range=Union[Union[dict, "SspSystemComponent"], list[Union[dict, "SspSystemComponent"]]])

slots.SystemImplementation_inventory_items = Slot(uri=OSCAL_ASSESSMENT_PLAN.inventory_items, name="SystemImplementation_inventory-items", curie=OSCAL_ASSESSMENT_PLAN.curie('inventory_items'),
                   model_uri=OSCAL.SystemImplementation_inventory_items, domain=SystemImplementation, range=Optional[Union[Union[dict, "SspInventoryItem"], list[Union[dict, "SspInventoryItem"]]]])

slots.LeveragedAuthorization_uuid = Slot(uri=OSCAL_CATALOG.uuid, name="LeveragedAuthorization_uuid", curie=OSCAL_CATALOG.curie('uuid'),
                   model_uri=OSCAL.LeveragedAuthorization_uuid, domain=LeveragedAuthorization, range=str)

slots.LeveragedAuthorization_title = Slot(uri=OSCAL_CATALOG.title, name="LeveragedAuthorization_title", curie=OSCAL_CATALOG.curie('title'),
                   model_uri=OSCAL.LeveragedAuthorization_title, domain=LeveragedAuthorization, range=str)

slots.LeveragedAuthorization_party_uuid = Slot(uri=OSCAL_ASSESSMENT_PLAN.party_uuid, name="LeveragedAuthorization_party-uuid", curie=OSCAL_ASSESSMENT_PLAN.curie('party_uuid'),
                   model_uri=OSCAL.LeveragedAuthorization_party_uuid, domain=LeveragedAuthorization, range=str)

slots.LeveragedAuthorization_date_authorized = Slot(uri=OSCAL_SSP.date_authorized, name="LeveragedAuthorization_date-authorized", curie=OSCAL_SSP.curie('date_authorized'),
                   model_uri=OSCAL.LeveragedAuthorization_date_authorized, domain=LeveragedAuthorization, range=str)

slots.LeveragedAuthorization_links = Slot(uri=OSCAL_CATALOG.links, name="LeveragedAuthorization_links", curie=OSCAL_CATALOG.curie('links'),
                   model_uri=OSCAL.LeveragedAuthorization_links, domain=LeveragedAuthorization, range=Optional[Union[Union[dict, "SspLeveragedAuthorizationLink"], list[Union[dict, "SspLeveragedAuthorizationLink"]]]])

slots.SspControlImplementation_set_parameters = Slot(uri=OSCAL_CATALOG.set_parameters, name="SspControlImplementation_set-parameters", curie=OSCAL_CATALOG.curie('set_parameters'),
                   model_uri=OSCAL.SspControlImplementation_set_parameters, domain=SspControlImplementation, range=Optional[Union[Union[dict, "SetParameter"], list[Union[dict, "SetParameter"]]]])

slots.SspControlImplementation_implemented_requirements = Slot(uri=OSCAL_CATALOG.implemented_requirements, name="SspControlImplementation_implemented-requirements", curie=OSCAL_CATALOG.curie('implemented_requirements'),
                   model_uri=OSCAL.SspControlImplementation_implemented_requirements, domain=SspControlImplementation, range=Union[Union[dict, "SspImplementedRequirement"], list[Union[dict, "SspImplementedRequirement"]]])

slots.SspControlImplementation_description = Slot(uri=OSCAL_CATALOG.description, name="SspControlImplementation_description", curie=OSCAL_CATALOG.curie('description'),
                   model_uri=OSCAL.SspControlImplementation_description, domain=SspControlImplementation, range=str)

slots.SspImplementedRequirement_set_parameters = Slot(uri=OSCAL_CATALOG.set_parameters, name="SspImplementedRequirement_set-parameters", curie=OSCAL_CATALOG.curie('set_parameters'),
                   model_uri=OSCAL.SspImplementedRequirement_set_parameters, domain=SspImplementedRequirement, range=Optional[Union[Union[dict, "SetParameter"], list[Union[dict, "SetParameter"]]]])

slots.SspImplementedRequirement_statements = Slot(uri=OSCAL_CATALOG.statements, name="SspImplementedRequirement_statements", curie=OSCAL_CATALOG.curie('statements'),
                   model_uri=OSCAL.SspImplementedRequirement_statements, domain=SspImplementedRequirement, range=Optional[Union[Union[dict, "SspStatement"], list[Union[dict, "SspStatement"]]]])

slots.SspImplementedRequirement_uuid = Slot(uri=OSCAL_CATALOG.uuid, name="SspImplementedRequirement_uuid", curie=OSCAL_CATALOG.curie('uuid'),
                   model_uri=OSCAL.SspImplementedRequirement_uuid, domain=SspImplementedRequirement, range=str)

slots.SspImplementedRequirement_control_id = Slot(uri=OSCAL_CATALOG.control_id, name="SspImplementedRequirement_control-id", curie=OSCAL_CATALOG.curie('control_id'),
                   model_uri=OSCAL.SspImplementedRequirement_control_id, domain=SspImplementedRequirement, range=str)

slots.SspImplementedRequirement_props = Slot(uri=OSCAL_CATALOG.props, name="SspImplementedRequirement_props", curie=OSCAL_CATALOG.curie('props'),
                   model_uri=OSCAL.SspImplementedRequirement_props, domain=SspImplementedRequirement, range=Optional[Union[Union[dict, "SspControlOriginationProp"], list[Union[dict, "SspControlOriginationProp"]]]])

slots.SspImplementedRequirement_responsible_roles = Slot(uri=OSCAL_CATALOG.responsible_roles, name="SspImplementedRequirement_responsible-roles", curie=OSCAL_CATALOG.curie('responsible_roles'),
                   model_uri=OSCAL.SspImplementedRequirement_responsible_roles, domain=SspImplementedRequirement, range=Optional[Union[Union[dict, "SspImplementedRequirementResponsibleRole"], list[Union[dict, "SspImplementedRequirementResponsibleRole"]]]])

slots.SspStatement_statement_id = Slot(uri=OSCAL_CATALOG.statement_id, name="SspStatement_statement-id", curie=OSCAL_CATALOG.curie('statement_id'),
                   model_uri=OSCAL.SspStatement_statement_id, domain=SspStatement, range=str)

slots.SspStatement_uuid = Slot(uri=OSCAL_CATALOG.uuid, name="SspStatement_uuid", curie=OSCAL_CATALOG.curie('uuid'),
                   model_uri=OSCAL.SspStatement_uuid, domain=SspStatement, range=str)

slots.SspStatement_props = Slot(uri=OSCAL_CATALOG.props, name="SspStatement_props", curie=OSCAL_CATALOG.curie('props'),
                   model_uri=OSCAL.SspStatement_props, domain=SspStatement, range=Optional[Union[Union[dict, "SspControlOriginationProp"], list[Union[dict, "SspControlOriginationProp"]]]])

slots.SspStatement_responsible_roles = Slot(uri=OSCAL_CATALOG.responsible_roles, name="SspStatement_responsible-roles", curie=OSCAL_CATALOG.curie('responsible_roles'),
                   model_uri=OSCAL.SspStatement_responsible_roles, domain=SspStatement, range=Optional[Union[Union[dict, "SspImplementedRequirementResponsibleRole"], list[Union[dict, "SspImplementedRequirementResponsibleRole"]]]])

slots.ByComponent_set_parameters = Slot(uri=OSCAL_CATALOG.set_parameters, name="ByComponent_set-parameters", curie=OSCAL_CATALOG.curie('set_parameters'),
                   model_uri=OSCAL.ByComponent_set_parameters, domain=ByComponent, range=Optional[Union[Union[dict, "SetParameter"], list[Union[dict, "SetParameter"]]]])

slots.ByComponent_component_uuid = Slot(uri=OSCAL_ASSESSMENT_PLAN.component_uuid, name="ByComponent_component-uuid", curie=OSCAL_ASSESSMENT_PLAN.curie('component_uuid'),
                   model_uri=OSCAL.ByComponent_component_uuid, domain=ByComponent, range=str)

slots.ByComponent_uuid = Slot(uri=OSCAL_CATALOG.uuid, name="ByComponent_uuid", curie=OSCAL_CATALOG.curie('uuid'),
                   model_uri=OSCAL.ByComponent_uuid, domain=ByComponent, range=str)

slots.ByComponent_description = Slot(uri=OSCAL_CATALOG.description, name="ByComponent_description", curie=OSCAL_CATALOG.curie('description'),
                   model_uri=OSCAL.ByComponent_description, domain=ByComponent, range=str)

slots.ByComponent_props = Slot(uri=OSCAL_CATALOG.props, name="ByComponent_props", curie=OSCAL_CATALOG.curie('props'),
                   model_uri=OSCAL.ByComponent_props, domain=ByComponent, range=Optional[Union[Union[dict, "SspControlOriginationProp"], list[Union[dict, "SspControlOriginationProp"]]]])

slots.ByComponent_links = Slot(uri=OSCAL_CATALOG.links, name="ByComponent_links", curie=OSCAL_CATALOG.curie('links'),
                   model_uri=OSCAL.ByComponent_links, domain=ByComponent, range=Optional[Union[Union[dict, "SspByComponentLink"], list[Union[dict, "SspByComponentLink"]]]])

slots.ByComponent_responsible_roles = Slot(uri=OSCAL_CATALOG.responsible_roles, name="ByComponent_responsible-roles", curie=OSCAL_CATALOG.curie('responsible_roles'),
                   model_uri=OSCAL.ByComponent_responsible_roles, domain=ByComponent, range=Optional[Union[Union[dict, "SspByComponentResponsibleRole"], list[Union[dict, "SspByComponentResponsibleRole"]]]])

slots.ProvidedControlImplementation_uuid = Slot(uri=OSCAL_CATALOG.uuid, name="ProvidedControlImplementation_uuid", curie=OSCAL_CATALOG.curie('uuid'),
                   model_uri=OSCAL.ProvidedControlImplementation_uuid, domain=ProvidedControlImplementation, range=str)

slots.ProvidedControlImplementation_description = Slot(uri=OSCAL_CATALOG.description, name="ProvidedControlImplementation_description", curie=OSCAL_CATALOG.curie('description'),
                   model_uri=OSCAL.ProvidedControlImplementation_description, domain=ProvidedControlImplementation, range=str)

slots.ProvidedControlImplementation_responsible_roles = Slot(uri=OSCAL_CATALOG.responsible_roles, name="ProvidedControlImplementation_responsible-roles", curie=OSCAL_CATALOG.curie('responsible_roles'),
                   model_uri=OSCAL.ProvidedControlImplementation_responsible_roles, domain=ProvidedControlImplementation, range=Optional[Union[Union[dict, "SspByComponentResponsibleRole"], list[Union[dict, "SspByComponentResponsibleRole"]]]])

slots.ControlResponsibility_uuid = Slot(uri=OSCAL_CATALOG.uuid, name="ControlResponsibility_uuid", curie=OSCAL_CATALOG.curie('uuid'),
                   model_uri=OSCAL.ControlResponsibility_uuid, domain=ControlResponsibility, range=str)

slots.ControlResponsibility_description = Slot(uri=OSCAL_CATALOG.description, name="ControlResponsibility_description", curie=OSCAL_CATALOG.curie('description'),
                   model_uri=OSCAL.ControlResponsibility_description, domain=ControlResponsibility, range=str)

slots.ControlResponsibility_responsible_roles = Slot(uri=OSCAL_CATALOG.responsible_roles, name="ControlResponsibility_responsible-roles", curie=OSCAL_CATALOG.curie('responsible_roles'),
                   model_uri=OSCAL.ControlResponsibility_responsible_roles, domain=ControlResponsibility, range=Optional[Union[Union[dict, "SspByComponentResponsibleRole"], list[Union[dict, "SspByComponentResponsibleRole"]]]])

slots.InheritedControlImplementation_uuid = Slot(uri=OSCAL_CATALOG.uuid, name="InheritedControlImplementation_uuid", curie=OSCAL_CATALOG.curie('uuid'),
                   model_uri=OSCAL.InheritedControlImplementation_uuid, domain=InheritedControlImplementation, range=str)

slots.InheritedControlImplementation_description = Slot(uri=OSCAL_CATALOG.description, name="InheritedControlImplementation_description", curie=OSCAL_CATALOG.curie('description'),
                   model_uri=OSCAL.InheritedControlImplementation_description, domain=InheritedControlImplementation, range=str)

slots.InheritedControlImplementation_responsible_roles = Slot(uri=OSCAL_CATALOG.responsible_roles, name="InheritedControlImplementation_responsible-roles", curie=OSCAL_CATALOG.curie('responsible_roles'),
                   model_uri=OSCAL.InheritedControlImplementation_responsible_roles, domain=InheritedControlImplementation, range=Optional[Union[Union[dict, "SspByComponentResponsibleRole"], list[Union[dict, "SspByComponentResponsibleRole"]]]])

slots.SatisfiedControlImplementation_uuid = Slot(uri=OSCAL_CATALOG.uuid, name="SatisfiedControlImplementation_uuid", curie=OSCAL_CATALOG.curie('uuid'),
                   model_uri=OSCAL.SatisfiedControlImplementation_uuid, domain=SatisfiedControlImplementation, range=str)

slots.SatisfiedControlImplementation_description = Slot(uri=OSCAL_CATALOG.description, name="SatisfiedControlImplementation_description", curie=OSCAL_CATALOG.curie('description'),
                   model_uri=OSCAL.SatisfiedControlImplementation_description, domain=SatisfiedControlImplementation, range=str)

slots.SatisfiedControlImplementation_responsible_roles = Slot(uri=OSCAL_CATALOG.responsible_roles, name="SatisfiedControlImplementation_responsible-roles", curie=OSCAL_CATALOG.curie('responsible_roles'),
                   model_uri=OSCAL.SatisfiedControlImplementation_responsible_roles, domain=SatisfiedControlImplementation, range=Optional[Union[Union[dict, "SspByComponentResponsibleRole"], list[Union[dict, "SspByComponentResponsibleRole"]]]])

slots.SspSystemCharacteristicsProp_name = Slot(uri=OSCAL_CATALOG.name, name="SspSystemCharacteristicsProp_name", curie=OSCAL_CATALOG.curie('name'),
                   model_uri=OSCAL.SspSystemCharacteristicsProp_name, domain=SspSystemCharacteristicsProp, range=Union[str, "SystemCharacteristicsPropNameEnum"])

slots.SspSystemCharacteristicsProp_value = Slot(uri=OSCAL_CATALOG.value, name="SspSystemCharacteristicsProp_value", curie=OSCAL_CATALOG.curie('value'),
                   model_uri=OSCAL.SspSystemCharacteristicsProp_value, domain=SspSystemCharacteristicsProp, range=str)

slots.SspSystemInformationProp_name = Slot(uri=OSCAL_CATALOG.name, name="SspSystemInformationProp_name", curie=OSCAL_CATALOG.curie('name'),
                   model_uri=OSCAL.SspSystemInformationProp_name, domain=SspSystemInformationProp, range=Union[str, "SystemInformationPropNameEnum"])

slots.SspSystemInformationProp_value = Slot(uri=OSCAL_CATALOG.value, name="SspSystemInformationProp_value", curie=OSCAL_CATALOG.curie('value'),
                   model_uri=OSCAL.SspSystemInformationProp_value, domain=SspSystemInformationProp, range=Union[str, "PrivacyDesignationEnum"])

slots.SspControlOriginationProp_name = Slot(uri=OSCAL_CATALOG.name, name="SspControlOriginationProp_name", curie=OSCAL_CATALOG.curie('name'),
                   model_uri=OSCAL.SspControlOriginationProp_name, domain=SspControlOriginationProp, range=Union[str, "ControlOriginationPropNameEnum"])

slots.SspControlOriginationProp_value = Slot(uri=OSCAL_CATALOG.value, name="SspControlOriginationProp_value", curie=OSCAL_CATALOG.curie('value'),
                   model_uri=OSCAL.SspControlOriginationProp_value, domain=SspControlOriginationProp, range=Union[str, "ControlOriginationValueEnum"])

slots.SspAllowsAuthenticatedScanProp_name = Slot(uri=OSCAL_CATALOG.name, name="SspAllowsAuthenticatedScanProp_name", curie=OSCAL_CATALOG.curie('name'),
                   model_uri=OSCAL.SspAllowsAuthenticatedScanProp_name, domain=SspAllowsAuthenticatedScanProp, range=str)

slots.SspAllowsAuthenticatedScanProp_value = Slot(uri=OSCAL_CATALOG.value, name="SspAllowsAuthenticatedScanProp_value", curie=OSCAL_CATALOG.curie('value'),
                   model_uri=OSCAL.SspAllowsAuthenticatedScanProp_value, domain=SspAllowsAuthenticatedScanProp, range=Union[str, "AllowsAuthenticatedScanEnum"])

slots.SspSystemInformationLink_rel = Slot(uri=OSCAL_CATALOG.rel, name="SspSystemInformationLink_rel", curie=OSCAL_CATALOG.curie('rel'),
                   model_uri=OSCAL.SspSystemInformationLink_rel, domain=SspSystemInformationLink, range=Optional[str])

slots.SspDiagramLink_rel = Slot(uri=OSCAL_CATALOG.rel, name="SspDiagramLink_rel", curie=OSCAL_CATALOG.curie('rel'),
                   model_uri=OSCAL.SspDiagramLink_rel, domain=SspDiagramLink, range=Optional[str])

slots.SspLeveragedAuthorizationLink_rel = Slot(uri=OSCAL_CATALOG.rel, name="SspLeveragedAuthorizationLink_rel", curie=OSCAL_CATALOG.curie('rel'),
                   model_uri=OSCAL.SspLeveragedAuthorizationLink_rel, domain=SspLeveragedAuthorizationLink, range=Optional[str])

slots.SspByComponentLink_rel = Slot(uri=OSCAL_CATALOG.rel, name="SspByComponentLink_rel", curie=OSCAL_CATALOG.curie('rel'),
                   model_uri=OSCAL.SspByComponentLink_rel, domain=SspByComponentLink, range=Optional[str])

slots.SspSystemCharacteristicsResponsibleParty_role_id = Slot(uri=OSCAL_CATALOG.role_id, name="SspSystemCharacteristicsResponsibleParty_role-id", curie=OSCAL_CATALOG.curie('role_id'),
                   model_uri=OSCAL.SspSystemCharacteristicsResponsibleParty_role_id, domain=SspSystemCharacteristicsResponsibleParty, range=str)

slots.SspImplementedRequirementResponsibleRole_role_id = Slot(uri=OSCAL_CATALOG.role_id, name="SspImplementedRequirementResponsibleRole_role-id", curie=OSCAL_CATALOG.curie('role_id'),
                   model_uri=OSCAL.SspImplementedRequirementResponsibleRole_role_id, domain=SspImplementedRequirementResponsibleRole, range=str)

slots.SspByComponentResponsibleRole_role_id = Slot(uri=OSCAL_CATALOG.role_id, name="SspByComponentResponsibleRole_role-id", curie=OSCAL_CATALOG.curie('role_id'),
                   model_uri=OSCAL.SspByComponentResponsibleRole_role_id, domain=SspByComponentResponsibleRole, range=str)

slots.SspSystemComponent_props = Slot(uri=OSCAL_CATALOG.props, name="SspSystemComponent_props", curie=OSCAL_CATALOG.curie('props'),
                   model_uri=OSCAL.SspSystemComponent_props, domain=SspSystemComponent, range=Optional[Union[Union[dict, SspAllowsAuthenticatedScanProp], list[Union[dict, SspAllowsAuthenticatedScanProp]]]])

slots.SspInventoryItem_props = Slot(uri=OSCAL_CATALOG.props, name="SspInventoryItem_props", curie=OSCAL_CATALOG.curie('props'),
                   model_uri=OSCAL.SspInventoryItem_props, domain=SspInventoryItem, range=Optional[Union[Union[dict, SspAllowsAuthenticatedScanProp], list[Union[dict, SspAllowsAuthenticatedScanProp]]]])

slots.AssessmentPlanDocument_assessment_plan = Slot(uri=OSCAL_ASSESSMENT_PLAN.assessment_plan, name="AssessmentPlanDocument_assessment-plan", curie=OSCAL_ASSESSMENT_PLAN.curie('assessment_plan'),
                   model_uri=OSCAL.AssessmentPlanDocument_assessment_plan, domain=AssessmentPlanDocument, range=Union[dict, "AssessmentPlan"])

slots.AssessmentPlan_uuid = Slot(uri=OSCAL_CATALOG.uuid, name="AssessmentPlan_uuid", curie=OSCAL_CATALOG.curie('uuid'),
                   model_uri=OSCAL.AssessmentPlan_uuid, domain=AssessmentPlan, range=str)

slots.AssessmentPlan_metadata = Slot(uri=OSCAL_CATALOG.metadata, name="AssessmentPlan_metadata", curie=OSCAL_CATALOG.curie('metadata'),
                   model_uri=OSCAL.AssessmentPlan_metadata, domain=AssessmentPlan, range=Union[dict, Metadata])

slots.AssessmentPlan_import_ssp = Slot(uri=OSCAL_ASSESSMENT_PLAN.import_ssp, name="AssessmentPlan_import-ssp", curie=OSCAL_ASSESSMENT_PLAN.curie('import_ssp'),
                   model_uri=OSCAL.AssessmentPlan_import_ssp, domain=AssessmentPlan, range=Union[dict, "ImportSSP"])

slots.AssessmentPlan_reviewed_controls = Slot(uri=OSCAL_ASSESSMENT_PLAN.reviewed_controls, name="AssessmentPlan_reviewed-controls", curie=OSCAL_ASSESSMENT_PLAN.curie('reviewed_controls'),
                   model_uri=OSCAL.AssessmentPlan_reviewed_controls, domain=AssessmentPlan, range=Union[dict, "ReviewedControls"])

slots.ImportSSP_href = Slot(uri=OSCAL_CATALOG.href, name="ImportSSP_href", curie=OSCAL_CATALOG.curie('href'),
                   model_uri=OSCAL.ImportSSP_href, domain=ImportSSP, range=str)

slots.TermsAndConditions_parts = Slot(uri=OSCAL_CATALOG.parts, name="TermsAndConditions_parts", curie=OSCAL_CATALOG.curie('parts'),
                   model_uri=OSCAL.TermsAndConditions_parts, domain=TermsAndConditions, range=Optional[Union[Union[dict, "TermsAndConditionsPart"], list[Union[dict, "TermsAndConditionsPart"]]]])

slots.ReviewedControls_control_selections = Slot(uri=OSCAL_ASSESSMENT_PLAN.control_selections, name="ReviewedControls_control-selections", curie=OSCAL_ASSESSMENT_PLAN.curie('control_selections'),
                   model_uri=OSCAL.ReviewedControls_control_selections, domain=ReviewedControls, range=Union[Union[dict, "ControlSelection"], list[Union[dict, "ControlSelection"]]])

slots.ControlSelection_include_controls = Slot(uri=OSCAL_CATALOG.include_controls, name="ControlSelection_include-controls", curie=OSCAL_CATALOG.curie('include_controls'),
                   model_uri=OSCAL.ControlSelection_include_controls, domain=ControlSelection, range=Optional[Union[Union[dict, "AssessmentSelectControlById"], list[Union[dict, "AssessmentSelectControlById"]]]])

slots.ControlSelection_exclude_controls = Slot(uri=OSCAL_CATALOG.exclude_controls, name="ControlSelection_exclude-controls", curie=OSCAL_CATALOG.curie('exclude_controls'),
                   model_uri=OSCAL.ControlSelection_exclude_controls, domain=ControlSelection, range=Optional[Union[Union[dict, "AssessmentSelectControlById"], list[Union[dict, "AssessmentSelectControlById"]]]])

slots.AssessmentSelectControlById_control_id = Slot(uri=OSCAL_CATALOG.control_id, name="AssessmentSelectControlById_control-id", curie=OSCAL_CATALOG.curie('control_id'),
                   model_uri=OSCAL.AssessmentSelectControlById_control_id, domain=AssessmentSelectControlById, range=str)

slots.SelectObjectiveById_objective_id = Slot(uri=OSCAL_ASSESSMENT_PLAN.objective_id, name="SelectObjectiveById_objective-id", curie=OSCAL_ASSESSMENT_PLAN.curie('objective_id'),
                   model_uri=OSCAL.SelectObjectiveById_objective_id, domain=SelectObjectiveById, range=str)

slots.AssessmentSubject_type = Slot(uri=OSCAL_CATALOG.type, name="AssessmentSubject_type", curie=OSCAL_CATALOG.curie('type'),
                   model_uri=OSCAL.AssessmentSubject_type, domain=AssessmentSubject, range=str)

slots.SelectSubjectById_subject_uuid = Slot(uri=OSCAL_ASSESSMENT_PLAN.subject_uuid, name="SelectSubjectById_subject-uuid", curie=OSCAL_ASSESSMENT_PLAN.curie('subject_uuid'),
                   model_uri=OSCAL.SelectSubjectById_subject_uuid, domain=SelectSubjectById, range=str)

slots.SelectSubjectById_type = Slot(uri=OSCAL_CATALOG.type, name="SelectSubjectById_type", curie=OSCAL_CATALOG.curie('type'),
                   model_uri=OSCAL.SelectSubjectById_type, domain=SelectSubjectById, range=str)

slots.SubjectReference_subject_uuid = Slot(uri=OSCAL_ASSESSMENT_PLAN.subject_uuid, name="SubjectReference_subject-uuid", curie=OSCAL_ASSESSMENT_PLAN.curie('subject_uuid'),
                   model_uri=OSCAL.SubjectReference_subject_uuid, domain=SubjectReference, range=str)

slots.SubjectReference_type = Slot(uri=OSCAL_CATALOG.type, name="SubjectReference_type", curie=OSCAL_CATALOG.curie('type'),
                   model_uri=OSCAL.SubjectReference_type, domain=SubjectReference, range=str)

slots.AssessmentSubjectPlaceholder_uuid = Slot(uri=OSCAL_CATALOG.uuid, name="AssessmentSubjectPlaceholder_uuid", curie=OSCAL_CATALOG.curie('uuid'),
                   model_uri=OSCAL.AssessmentSubjectPlaceholder_uuid, domain=AssessmentSubjectPlaceholder, range=str)

slots.AssessmentSubjectPlaceholder_sources = Slot(uri=OSCAL_CATALOG.sources, name="AssessmentSubjectPlaceholder_sources", curie=OSCAL_CATALOG.curie('sources'),
                   model_uri=OSCAL.AssessmentSubjectPlaceholder_sources, domain=AssessmentSubjectPlaceholder, range=Union[Union[dict, "AssessmentSubjectSource"], list[Union[dict, "AssessmentSubjectSource"]]])

slots.AssessmentSubjectSource_task_uuid = Slot(uri=OSCAL_ASSESSMENT_PLAN.task_uuid, name="AssessmentSubjectSource_task-uuid", curie=OSCAL_ASSESSMENT_PLAN.curie('task_uuid'),
                   model_uri=OSCAL.AssessmentSubjectSource_task_uuid, domain=AssessmentSubjectSource, range=str)

slots.AssessmentAssets_assessment_platforms = Slot(uri=OSCAL_ASSESSMENT_PLAN.assessment_platforms, name="AssessmentAssets_assessment-platforms", curie=OSCAL_ASSESSMENT_PLAN.curie('assessment_platforms'),
                   model_uri=OSCAL.AssessmentAssets_assessment_platforms, domain=AssessmentAssets, range=Union[Union[dict, "AssessmentPlatform"], list[Union[dict, "AssessmentPlatform"]]])

slots.AssessmentPlatform_uuid = Slot(uri=OSCAL_CATALOG.uuid, name="AssessmentPlatform_uuid", curie=OSCAL_CATALOG.curie('uuid'),
                   model_uri=OSCAL.AssessmentPlatform_uuid, domain=AssessmentPlatform, range=str)

slots.UsesComponent_component_uuid = Slot(uri=OSCAL_ASSESSMENT_PLAN.component_uuid, name="UsesComponent_component-uuid", curie=OSCAL_ASSESSMENT_PLAN.curie('component_uuid'),
                   model_uri=OSCAL.UsesComponent_component_uuid, domain=UsesComponent, range=str)

slots.LocalObjective_control_id = Slot(uri=OSCAL_CATALOG.control_id, name="LocalObjective_control-id", curie=OSCAL_CATALOG.curie('control_id'),
                   model_uri=OSCAL.LocalObjective_control_id, domain=LocalObjective, range=str)

slots.LocalObjective_parts = Slot(uri=OSCAL_CATALOG.parts, name="LocalObjective_parts", curie=OSCAL_CATALOG.curie('parts'),
                   model_uri=OSCAL.LocalObjective_parts, domain=LocalObjective, range=Union[Union[dict, "ControlPart"], list[Union[dict, "ControlPart"]]])

slots.AssessmentMethod_uuid = Slot(uri=OSCAL_CATALOG.uuid, name="AssessmentMethod_uuid", curie=OSCAL_CATALOG.curie('uuid'),
                   model_uri=OSCAL.AssessmentMethod_uuid, domain=AssessmentMethod, range=str)

slots.AssessmentMethod_part = Slot(uri=OSCAL_ASSESSMENT_PLAN.part, name="AssessmentMethod_part", curie=OSCAL_ASSESSMENT_PLAN.curie('part'),
                   model_uri=OSCAL.AssessmentMethod_part, domain=AssessmentMethod, range=Union[dict, "AssessmentPart"])

slots.Activity_uuid = Slot(uri=OSCAL_CATALOG.uuid, name="Activity_uuid", curie=OSCAL_CATALOG.curie('uuid'),
                   model_uri=OSCAL.Activity_uuid, domain=Activity, range=str)

slots.Activity_description = Slot(uri=OSCAL_CATALOG.description, name="Activity_description", curie=OSCAL_CATALOG.curie('description'),
                   model_uri=OSCAL.Activity_description, domain=Activity, range=str)

slots.Step_uuid = Slot(uri=OSCAL_CATALOG.uuid, name="Step_uuid", curie=OSCAL_CATALOG.curie('uuid'),
                   model_uri=OSCAL.Step_uuid, domain=Step, range=str)

slots.Step_description = Slot(uri=OSCAL_CATALOG.description, name="Step_description", curie=OSCAL_CATALOG.curie('description'),
                   model_uri=OSCAL.Step_description, domain=Step, range=str)

slots.Task_uuid = Slot(uri=OSCAL_CATALOG.uuid, name="Task_uuid", curie=OSCAL_CATALOG.curie('uuid'),
                   model_uri=OSCAL.Task_uuid, domain=Task, range=str)

slots.Task_type = Slot(uri=OSCAL_CATALOG.type, name="Task_type", curie=OSCAL_CATALOG.curie('type'),
                   model_uri=OSCAL.Task_type, domain=Task, range=str)

slots.Task_title = Slot(uri=OSCAL_CATALOG.title, name="Task_title", curie=OSCAL_CATALOG.curie('title'),
                   model_uri=OSCAL.Task_title, domain=Task, range=str)

slots.Task_subjects = Slot(uri=OSCAL_ASSESSMENT_PLAN.subjects, name="Task_subjects", curie=OSCAL_ASSESSMENT_PLAN.curie('subjects'),
                   model_uri=OSCAL.Task_subjects, domain=Task, range=Optional[Union[Union[dict, AssessmentSubject], list[Union[dict, AssessmentSubject]]]])

slots.OnDateCondition_date = Slot(uri=OSCAL_CATALOG.date, name="OnDateCondition_date", curie=OSCAL_CATALOG.curie('date'),
                   model_uri=OSCAL.OnDateCondition_date, domain=OnDateCondition, range=str)

slots.WithinDateRange_start = Slot(uri=OSCAL_ASSESSMENT_PLAN.start, name="WithinDateRange_start", curie=OSCAL_ASSESSMENT_PLAN.curie('start'),
                   model_uri=OSCAL.WithinDateRange_start, domain=WithinDateRange, range=str)

slots.WithinDateRange_end = Slot(uri=OSCAL_ASSESSMENT_PLAN.end, name="WithinDateRange_end", curie=OSCAL_ASSESSMENT_PLAN.curie('end'),
                   model_uri=OSCAL.WithinDateRange_end, domain=WithinDateRange, range=str)

slots.AtFrequency_period = Slot(uri=OSCAL_ASSESSMENT_PLAN.period, name="AtFrequency_period", curie=OSCAL_ASSESSMENT_PLAN.curie('period'),
                   model_uri=OSCAL.AtFrequency_period, domain=AtFrequency, range=int)

slots.AtFrequency_unit = Slot(uri=OSCAL_ASSESSMENT_PLAN.unit, name="AtFrequency_unit", curie=OSCAL_ASSESSMENT_PLAN.curie('unit'),
                   model_uri=OSCAL.AtFrequency_unit, domain=AtFrequency, range=Union[str, "TimingUnitEnum"])

slots.TaskDependency_task_uuid = Slot(uri=OSCAL_ASSESSMENT_PLAN.task_uuid, name="TaskDependency_task-uuid", curie=OSCAL_ASSESSMENT_PLAN.curie('task_uuid'),
                   model_uri=OSCAL.TaskDependency_task_uuid, domain=TaskDependency, range=str)

slots.AssociatedActivity_activity_uuid = Slot(uri=OSCAL_ASSESSMENT_PLAN.activity_uuid, name="AssociatedActivity_activity-uuid", curie=OSCAL_ASSESSMENT_PLAN.curie('activity_uuid'),
                   model_uri=OSCAL.AssociatedActivity_activity_uuid, domain=AssociatedActivity, range=str)

slots.AssociatedActivity_subjects = Slot(uri=OSCAL_ASSESSMENT_PLAN.subjects, name="AssociatedActivity_subjects", curie=OSCAL_ASSESSMENT_PLAN.curie('subjects'),
                   model_uri=OSCAL.AssociatedActivity_subjects, domain=AssociatedActivity, range=Union[Union[dict, AssessmentSubject], list[Union[dict, AssessmentSubject]]])

slots.AssessmentPart_name = Slot(uri=OSCAL_CATALOG.name, name="AssessmentPart_name", curie=OSCAL_CATALOG.curie('name'),
                   model_uri=OSCAL.AssessmentPart_name, domain=AssessmentPart, range=str)

slots.AssessmentPart_parts = Slot(uri=OSCAL_CATALOG.parts, name="AssessmentPart_parts", curie=OSCAL_CATALOG.curie('parts'),
                   model_uri=OSCAL.AssessmentPart_parts, domain=AssessmentPart, range=Optional[Union[Union[dict, "AssessmentPart"], list[Union[dict, "AssessmentPart"]]]])

slots.TermsAndConditionsPart_name = Slot(uri=OSCAL_CATALOG.name, name="TermsAndConditionsPart_name", curie=OSCAL_CATALOG.curie('name'),
                   model_uri=OSCAL.TermsAndConditionsPart_name, domain=TermsAndConditionsPart, range=Union[str, "TermsAndConditionsPartNameEnum"])

slots.TermsAndConditionsPart_parts = Slot(uri=OSCAL_CATALOG.parts, name="TermsAndConditionsPart_parts", curie=OSCAL_CATALOG.curie('parts'),
                   model_uri=OSCAL.TermsAndConditionsPart_parts, domain=TermsAndConditionsPart, range=Optional[Union[Union[dict, "TermsAndConditionsPart"], list[Union[dict, "TermsAndConditionsPart"]]]])

slots.ControlPart_name = Slot(uri=OSCAL_CATALOG.name, name="ControlPart_name", curie=OSCAL_CATALOG.curie('name'),
                   model_uri=OSCAL.ControlPart_name, domain=ControlPart, range=str)

slots.ControlPart_parts = Slot(uri=OSCAL_CATALOG.parts, name="ControlPart_parts", curie=OSCAL_CATALOG.curie('parts'),
                   model_uri=OSCAL.ControlPart_parts, domain=ControlPart, range=Optional[Union[Union[dict, "ControlPart"], list[Union[dict, "ControlPart"]]]])

slots.SetParameter_param_id = Slot(uri=OSCAL_CATALOG.param_id, name="SetParameter_param-id", curie=OSCAL_CATALOG.curie('param_id'),
                   model_uri=OSCAL.SetParameter_param_id, domain=SetParameter, range=str)

slots.SetParameter_values = Slot(uri=OSCAL_CATALOG.values, name="SetParameter_values", curie=OSCAL_CATALOG.curie('values'),
                   model_uri=OSCAL.SetParameter_values, domain=SetParameter, range=Union[str, list[str]])

slots.SystemComponent_uuid = Slot(uri=OSCAL_CATALOG.uuid, name="SystemComponent_uuid", curie=OSCAL_CATALOG.curie('uuid'),
                   model_uri=OSCAL.SystemComponent_uuid, domain=SystemComponent, range=str)

slots.SystemComponent_type = Slot(uri=OSCAL_CATALOG.type, name="SystemComponent_type", curie=OSCAL_CATALOG.curie('type'),
                   model_uri=OSCAL.SystemComponent_type, domain=SystemComponent, range=str)

slots.SystemComponent_title = Slot(uri=OSCAL_CATALOG.title, name="SystemComponent_title", curie=OSCAL_CATALOG.curie('title'),
                   model_uri=OSCAL.SystemComponent_title, domain=SystemComponent, range=str)

slots.SystemComponent_description = Slot(uri=OSCAL_CATALOG.description, name="SystemComponent_description", curie=OSCAL_CATALOG.curie('description'),
                   model_uri=OSCAL.SystemComponent_description, domain=SystemComponent, range=str)

slots.SystemComponent_status = Slot(uri=OSCAL_CATALOG.status, name="SystemComponent_status", curie=OSCAL_CATALOG.curie('status'),
                   model_uri=OSCAL.SystemComponent_status, domain=SystemComponent, range=Union[dict, "ComponentStatus"])

slots.SystemComponent_props = Slot(uri=OSCAL_CATALOG.props, name="SystemComponent_props", curie=OSCAL_CATALOG.curie('props'),
                   model_uri=OSCAL.SystemComponent_props, domain=SystemComponent, range=Optional[Union[Union[dict, "ImplementationCommonProperty"], list[Union[dict, "ImplementationCommonProperty"]]]])

slots.SystemComponent_links = Slot(uri=OSCAL_CATALOG.links, name="SystemComponent_links", curie=OSCAL_CATALOG.curie('links'),
                   model_uri=OSCAL.SystemComponent_links, domain=SystemComponent, range=Optional[Union[Union[dict, "ImplementationCommonLink"], list[Union[dict, "ImplementationCommonLink"]]]])

slots.SystemComponent_responsible_roles = Slot(uri=OSCAL_CATALOG.responsible_roles, name="SystemComponent_responsible-roles", curie=OSCAL_CATALOG.curie('responsible_roles'),
                   model_uri=OSCAL.SystemComponent_responsible_roles, domain=SystemComponent, range=Optional[Union[Union[dict, "ImplementationResponsibleRole"], list[Union[dict, "ImplementationResponsibleRole"]]]])

slots.ComponentStatus_state = Slot(uri=OSCAL_CATALOG.state, name="ComponentStatus_state", curie=OSCAL_CATALOG.curie('state'),
                   model_uri=OSCAL.ComponentStatus_state, domain=ComponentStatus, range=Union[str, "ComponentStateEnum"])

slots.Protocol_name = Slot(uri=OSCAL_CATALOG.name, name="Protocol_name", curie=OSCAL_CATALOG.curie('name'),
                   model_uri=OSCAL.Protocol_name, domain=Protocol, range=Optional[str])

slots.PortRange_start = Slot(uri=OSCAL_ASSESSMENT_PLAN.start, name="PortRange_start", curie=OSCAL_ASSESSMENT_PLAN.curie('start'),
                   model_uri=OSCAL.PortRange_start, domain=PortRange, range=Optional[int])

slots.PortRange_end = Slot(uri=OSCAL_ASSESSMENT_PLAN.end, name="PortRange_end", curie=OSCAL_ASSESSMENT_PLAN.curie('end'),
                   model_uri=OSCAL.PortRange_end, domain=PortRange, range=Optional[int])

slots.ImplementationStatus_state = Slot(uri=OSCAL_CATALOG.state, name="ImplementationStatus_state", curie=OSCAL_CATALOG.curie('state'),
                   model_uri=OSCAL.ImplementationStatus_state, domain=ImplementationStatus, range=str)

slots.SystemUser_uuid = Slot(uri=OSCAL_CATALOG.uuid, name="SystemUser_uuid", curie=OSCAL_CATALOG.curie('uuid'),
                   model_uri=OSCAL.SystemUser_uuid, domain=SystemUser, range=str)

slots.SystemUser_props = Slot(uri=OSCAL_CATALOG.props, name="SystemUser_props", curie=OSCAL_CATALOG.curie('props'),
                   model_uri=OSCAL.SystemUser_props, domain=SystemUser, range=Optional[Union[Union[dict, "ImplementationCommonProperty"], list[Union[dict, "ImplementationCommonProperty"]]]])

slots.SystemUser_links = Slot(uri=OSCAL_CATALOG.links, name="SystemUser_links", curie=OSCAL_CATALOG.curie('links'),
                   model_uri=OSCAL.SystemUser_links, domain=SystemUser, range=Optional[Union[Union[dict, "ImplementationCommonLink"], list[Union[dict, "ImplementationCommonLink"]]]])

slots.AuthorizedPrivilege_title = Slot(uri=OSCAL_CATALOG.title, name="AuthorizedPrivilege_title", curie=OSCAL_CATALOG.curie('title'),
                   model_uri=OSCAL.AuthorizedPrivilege_title, domain=AuthorizedPrivilege, range=str)

slots.AuthorizedPrivilege_functions_performed = Slot(uri=OSCAL_ASSESSMENT_PLAN.functions_performed, name="AuthorizedPrivilege_functions-performed", curie=OSCAL_ASSESSMENT_PLAN.curie('functions_performed'),
                   model_uri=OSCAL.AuthorizedPrivilege_functions_performed, domain=AuthorizedPrivilege, range=Union[str, list[str]])

slots.InventoryItem_uuid = Slot(uri=OSCAL_CATALOG.uuid, name="InventoryItem_uuid", curie=OSCAL_CATALOG.curie('uuid'),
                   model_uri=OSCAL.InventoryItem_uuid, domain=InventoryItem, range=str)

slots.InventoryItem_description = Slot(uri=OSCAL_CATALOG.description, name="InventoryItem_description", curie=OSCAL_CATALOG.curie('description'),
                   model_uri=OSCAL.InventoryItem_description, domain=InventoryItem, range=str)

slots.InventoryItem_props = Slot(uri=OSCAL_CATALOG.props, name="InventoryItem_props", curie=OSCAL_CATALOG.curie('props'),
                   model_uri=OSCAL.InventoryItem_props, domain=InventoryItem, range=Optional[Union[Union[dict, "ImplementationCommonProperty"], list[Union[dict, "ImplementationCommonProperty"]]]])

slots.InventoryItem_links = Slot(uri=OSCAL_CATALOG.links, name="InventoryItem_links", curie=OSCAL_CATALOG.curie('links'),
                   model_uri=OSCAL.InventoryItem_links, domain=InventoryItem, range=Optional[Union[Union[dict, "ImplementationCommonLink"], list[Union[dict, "ImplementationCommonLink"]]]])

slots.InventoryItem_responsible_parties = Slot(uri=OSCAL_CATALOG.responsible_parties, name="InventoryItem_responsible-parties", curie=OSCAL_CATALOG.curie('responsible_parties'),
                   model_uri=OSCAL.InventoryItem_responsible_parties, domain=InventoryItem, range=Optional[Union[Union[dict, "ImplementationResponsibleParty"], list[Union[dict, "ImplementationResponsibleParty"]]]])

slots.ImplementedComponent_component_uuid = Slot(uri=OSCAL_ASSESSMENT_PLAN.component_uuid, name="ImplementedComponent_component-uuid", curie=OSCAL_ASSESSMENT_PLAN.curie('component_uuid'),
                   model_uri=OSCAL.ImplementedComponent_component_uuid, domain=ImplementedComponent, range=str)

slots.ImplementedComponent_props = Slot(uri=OSCAL_CATALOG.props, name="ImplementedComponent_props", curie=OSCAL_CATALOG.curie('props'),
                   model_uri=OSCAL.ImplementedComponent_props, domain=ImplementedComponent, range=Optional[Union[Union[dict, "ImplementationCommonProperty"], list[Union[dict, "ImplementationCommonProperty"]]]])

slots.ImplementedComponent_links = Slot(uri=OSCAL_CATALOG.links, name="ImplementedComponent_links", curie=OSCAL_CATALOG.curie('links'),
                   model_uri=OSCAL.ImplementedComponent_links, domain=ImplementedComponent, range=Optional[Union[Union[dict, "ImplementationCommonLink"], list[Union[dict, "ImplementationCommonLink"]]]])

slots.ImplementedComponent_responsible_parties = Slot(uri=OSCAL_CATALOG.responsible_parties, name="ImplementedComponent_responsible-parties", curie=OSCAL_CATALOG.curie('responsible_parties'),
                   model_uri=OSCAL.ImplementedComponent_responsible_parties, domain=ImplementedComponent, range=Optional[Union[Union[dict, "ImplementationResponsibleParty"], list[Union[dict, "ImplementationResponsibleParty"]]]])

slots.SystemId_id = Slot(uri=OSCAL_CATALOG.id, name="SystemId_id", curie=OSCAL_CATALOG.curie('id'),
                   model_uri=OSCAL.SystemId_id, domain=SystemId, range=str)

slots.SystemId_identifier_type = Slot(uri=OSCAL_ASSESSMENT_PLAN.identifier_type, name="SystemId_identifier-type", curie=OSCAL_ASSESSMENT_PLAN.curie('identifier_type'),
                   model_uri=OSCAL.SystemId_identifier_type, domain=SystemId, range=Optional[str])

slots.ImplementationCommonProperty_name = Slot(uri=OSCAL_CATALOG.name, name="ImplementationCommonProperty_name", curie=OSCAL_CATALOG.curie('name'),
                   model_uri=OSCAL.ImplementationCommonProperty_name, domain=ImplementationCommonProperty, range=Union[str, "ImplementationPropNameEnum"])

slots.ImplementationCommonProperty_value = Slot(uri=OSCAL_CATALOG.value, name="ImplementationCommonProperty_value", curie=OSCAL_CATALOG.curie('value'),
                   model_uri=OSCAL.ImplementationCommonProperty_value, domain=ImplementationCommonProperty, range=str)

slots.ImplementationCommonLink_rel = Slot(uri=OSCAL_CATALOG.rel, name="ImplementationCommonLink_rel", curie=OSCAL_CATALOG.curie('rel'),
                   model_uri=OSCAL.ImplementationCommonLink_rel, domain=ImplementationCommonLink, range=Optional[str])

slots.ImplementationResponsibleRole_role_id = Slot(uri=OSCAL_CATALOG.role_id, name="ImplementationResponsibleRole_role-id", curie=OSCAL_CATALOG.curie('role_id'),
                   model_uri=OSCAL.ImplementationResponsibleRole_role_id, domain=ImplementationResponsibleRole, range=str)

slots.ImplementationResponsibleParty_role_id = Slot(uri=OSCAL_CATALOG.role_id, name="ImplementationResponsibleParty_role-id", curie=OSCAL_CATALOG.curie('role_id'),
                   model_uri=OSCAL.ImplementationResponsibleParty_role_id, domain=ImplementationResponsibleParty, range=str)

slots.Origin_actors = Slot(uri=OSCAL_ASSESSMENT_PLAN.actors, name="Origin_actors", curie=OSCAL_ASSESSMENT_PLAN.curie('actors'),
                   model_uri=OSCAL.Origin_actors, domain=Origin, range=Union[Union[dict, "OriginActor"], list[Union[dict, "OriginActor"]]])

slots.OriginActor_type = Slot(uri=OSCAL_CATALOG.type, name="OriginActor_type", curie=OSCAL_CATALOG.curie('type'),
                   model_uri=OSCAL.OriginActor_type, domain=OriginActor, range=Union[str, "OriginActorTypeEnum"])

slots.OriginActor_actor_uuid = Slot(uri=OSCAL_ASSESSMENT_PLAN.actor_uuid, name="OriginActor_actor-uuid", curie=OSCAL_ASSESSMENT_PLAN.curie('actor_uuid'),
                   model_uri=OSCAL.OriginActor_actor_uuid, domain=OriginActor, range=str)

slots.RelatedTask_task_uuid = Slot(uri=OSCAL_ASSESSMENT_PLAN.task_uuid, name="RelatedTask_task-uuid", curie=OSCAL_ASSESSMENT_PLAN.curie('task_uuid'),
                   model_uri=OSCAL.RelatedTask_task_uuid, domain=RelatedTask, range=str)

slots.RelatedTask_subjects = Slot(uri=OSCAL_ASSESSMENT_PLAN.subjects, name="RelatedTask_subjects", curie=OSCAL_ASSESSMENT_PLAN.curie('subjects'),
                   model_uri=OSCAL.RelatedTask_subjects, domain=RelatedTask, range=Optional[Union[Union[dict, AssessmentSubject], list[Union[dict, AssessmentSubject]]]])

slots.IdentifiedSubject_subject_placeholder_uuid = Slot(uri=OSCAL_ASSESSMENT_PLAN.subject_placeholder_uuid, name="IdentifiedSubject_subject-placeholder-uuid", curie=OSCAL_ASSESSMENT_PLAN.curie('subject_placeholder_uuid'),
                   model_uri=OSCAL.IdentifiedSubject_subject_placeholder_uuid, domain=IdentifiedSubject, range=str)

slots.IdentifiedSubject_subjects = Slot(uri=OSCAL_ASSESSMENT_PLAN.subjects, name="IdentifiedSubject_subjects", curie=OSCAL_ASSESSMENT_PLAN.curie('subjects'),
                   model_uri=OSCAL.IdentifiedSubject_subjects, domain=IdentifiedSubject, range=Union[Union[dict, AssessmentSubject], list[Union[dict, AssessmentSubject]]])

slots.Observation_uuid = Slot(uri=OSCAL_CATALOG.uuid, name="Observation_uuid", curie=OSCAL_CATALOG.curie('uuid'),
                   model_uri=OSCAL.Observation_uuid, domain=Observation, range=str)

slots.Observation_description = Slot(uri=OSCAL_CATALOG.description, name="Observation_description", curie=OSCAL_CATALOG.curie('description'),
                   model_uri=OSCAL.Observation_description, domain=Observation, range=str)

slots.Observation_subjects = Slot(uri=OSCAL_ASSESSMENT_PLAN.subjects, name="Observation_subjects", curie=OSCAL_ASSESSMENT_PLAN.curie('subjects'),
                   model_uri=OSCAL.Observation_subjects, domain=Observation, range=Optional[Union[Union[dict, SubjectReference], list[Union[dict, SubjectReference]]]])

slots.Observation_methods = Slot(uri=OSCAL_ASSESSMENT_PLAN.methods, name="Observation_methods", curie=OSCAL_ASSESSMENT_PLAN.curie('methods'),
                   model_uri=OSCAL.Observation_methods, domain=Observation, range=Union[str, list[str]])

slots.Observation_collected = Slot(uri=OSCAL_ASSESSMENT_PLAN.collected, name="Observation_collected", curie=OSCAL_ASSESSMENT_PLAN.curie('collected'),
                   model_uri=OSCAL.Observation_collected, domain=Observation, range=str)

slots.RelevantEvidence_description = Slot(uri=OSCAL_CATALOG.description, name="RelevantEvidence_description", curie=OSCAL_CATALOG.curie('description'),
                   model_uri=OSCAL.RelevantEvidence_description, domain=RelevantEvidence, range=str)

slots.Finding_uuid = Slot(uri=OSCAL_CATALOG.uuid, name="Finding_uuid", curie=OSCAL_CATALOG.curie('uuid'),
                   model_uri=OSCAL.Finding_uuid, domain=Finding, range=str)

slots.Finding_title = Slot(uri=OSCAL_CATALOG.title, name="Finding_title", curie=OSCAL_CATALOG.curie('title'),
                   model_uri=OSCAL.Finding_title, domain=Finding, range=str)

slots.Finding_description = Slot(uri=OSCAL_CATALOG.description, name="Finding_description", curie=OSCAL_CATALOG.curie('description'),
                   model_uri=OSCAL.Finding_description, domain=Finding, range=str)

slots.Finding_target = Slot(uri=OSCAL_ASSESSMENT_PLAN.target, name="Finding_target", curie=OSCAL_ASSESSMENT_PLAN.curie('target'),
                   model_uri=OSCAL.Finding_target, domain=Finding, range=Union[dict, "FindingTarget"])

slots.FindingTarget_type = Slot(uri=OSCAL_CATALOG.type, name="FindingTarget_type", curie=OSCAL_CATALOG.curie('type'),
                   model_uri=OSCAL.FindingTarget_type, domain=FindingTarget, range=Union[str, "FindingTargetTypeEnum"])

slots.FindingTarget_target_id = Slot(uri=OSCAL_ASSESSMENT_PLAN.target_id, name="FindingTarget_target-id", curie=OSCAL_ASSESSMENT_PLAN.curie('target_id'),
                   model_uri=OSCAL.FindingTarget_target_id, domain=FindingTarget, range=str)

slots.FindingTarget_status = Slot(uri=OSCAL_CATALOG.status, name="FindingTarget_status", curie=OSCAL_CATALOG.curie('status'),
                   model_uri=OSCAL.FindingTarget_status, domain=FindingTarget, range=Union[dict, "ObjectiveStatus"])

slots.ObjectiveStatus_state = Slot(uri=OSCAL_CATALOG.state, name="ObjectiveStatus_state", curie=OSCAL_CATALOG.curie('state'),
                   model_uri=OSCAL.ObjectiveStatus_state, domain=ObjectiveStatus, range=Union[str, "ObjectiveStatusStateEnum"])

slots.RelatedObservation_observation_uuid = Slot(uri=OSCAL_ASSESSMENT_PLAN.observation_uuid, name="RelatedObservation_observation-uuid", curie=OSCAL_ASSESSMENT_PLAN.curie('observation_uuid'),
                   model_uri=OSCAL.RelatedObservation_observation_uuid, domain=RelatedObservation, range=str)

slots.AssociatedRisk_risk_uuid = Slot(uri=OSCAL_ASSESSMENT_PLAN.risk_uuid, name="AssociatedRisk_risk-uuid", curie=OSCAL_ASSESSMENT_PLAN.curie('risk_uuid'),
                   model_uri=OSCAL.AssociatedRisk_risk_uuid, domain=AssociatedRisk, range=str)

slots.Risk_uuid = Slot(uri=OSCAL_CATALOG.uuid, name="Risk_uuid", curie=OSCAL_CATALOG.curie('uuid'),
                   model_uri=OSCAL.Risk_uuid, domain=Risk, range=str)

slots.Risk_title = Slot(uri=OSCAL_CATALOG.title, name="Risk_title", curie=OSCAL_CATALOG.curie('title'),
                   model_uri=OSCAL.Risk_title, domain=Risk, range=str)

slots.Risk_description = Slot(uri=OSCAL_CATALOG.description, name="Risk_description", curie=OSCAL_CATALOG.curie('description'),
                   model_uri=OSCAL.Risk_description, domain=Risk, range=str)

slots.Risk_statement = Slot(uri=OSCAL_ASSESSMENT_PLAN.statement, name="Risk_statement", curie=OSCAL_ASSESSMENT_PLAN.curie('statement'),
                   model_uri=OSCAL.Risk_statement, domain=Risk, range=str)

slots.Risk_status = Slot(uri=OSCAL_CATALOG.status, name="Risk_status", curie=OSCAL_CATALOG.curie('status'),
                   model_uri=OSCAL.Risk_status, domain=Risk, range=str)

slots.ThreatId_system = Slot(uri=OSCAL_CATALOG.system, name="ThreatId_system", curie=OSCAL_CATALOG.curie('system'),
                   model_uri=OSCAL.ThreatId_system, domain=ThreatId, range=str)

slots.ThreatId_id = Slot(uri=OSCAL_CATALOG.id, name="ThreatId_id", curie=OSCAL_CATALOG.curie('id'),
                   model_uri=OSCAL.ThreatId_id, domain=ThreatId, range=str)

slots.Characterization_origin = Slot(uri=OSCAL_ASSESSMENT_PLAN.origin, name="Characterization_origin", curie=OSCAL_ASSESSMENT_PLAN.curie('origin'),
                   model_uri=OSCAL.Characterization_origin, domain=Characterization, range=Union[dict, Origin])

slots.Characterization_facets = Slot(uri=OSCAL_ASSESSMENT_PLAN.facets, name="Characterization_facets", curie=OSCAL_ASSESSMENT_PLAN.curie('facets'),
                   model_uri=OSCAL.Characterization_facets, domain=Characterization, range=Union[Union[dict, "Facet"], list[Union[dict, "Facet"]]])

slots.Facet_name = Slot(uri=OSCAL_CATALOG.name, name="Facet_name", curie=OSCAL_CATALOG.curie('name'),
                   model_uri=OSCAL.Facet_name, domain=Facet, range=str)

slots.Facet_value = Slot(uri=OSCAL_CATALOG.value, name="Facet_value", curie=OSCAL_CATALOG.curie('value'),
                   model_uri=OSCAL.Facet_value, domain=Facet, range=str)

slots.Facet_system = Slot(uri=OSCAL_CATALOG.system, name="Facet_system", curie=OSCAL_CATALOG.curie('system'),
                   model_uri=OSCAL.Facet_system, domain=Facet, range=str)

slots.MitigatingFactor_uuid = Slot(uri=OSCAL_CATALOG.uuid, name="MitigatingFactor_uuid", curie=OSCAL_CATALOG.curie('uuid'),
                   model_uri=OSCAL.MitigatingFactor_uuid, domain=MitigatingFactor, range=str)

slots.MitigatingFactor_description = Slot(uri=OSCAL_CATALOG.description, name="MitigatingFactor_description", curie=OSCAL_CATALOG.curie('description'),
                   model_uri=OSCAL.MitigatingFactor_description, domain=MitigatingFactor, range=str)

slots.MitigatingFactor_subjects = Slot(uri=OSCAL_ASSESSMENT_PLAN.subjects, name="MitigatingFactor_subjects", curie=OSCAL_ASSESSMENT_PLAN.curie('subjects'),
                   model_uri=OSCAL.MitigatingFactor_subjects, domain=MitigatingFactor, range=Optional[Union[Union[dict, SubjectReference], list[Union[dict, SubjectReference]]]])

slots.Response_uuid = Slot(uri=OSCAL_CATALOG.uuid, name="Response_uuid", curie=OSCAL_CATALOG.curie('uuid'),
                   model_uri=OSCAL.Response_uuid, domain=Response, range=str)

slots.Response_title = Slot(uri=OSCAL_CATALOG.title, name="Response_title", curie=OSCAL_CATALOG.curie('title'),
                   model_uri=OSCAL.Response_title, domain=Response, range=str)

slots.Response_description = Slot(uri=OSCAL_CATALOG.description, name="Response_description", curie=OSCAL_CATALOG.curie('description'),
                   model_uri=OSCAL.Response_description, domain=Response, range=str)

slots.Response_lifecycle = Slot(uri=OSCAL_ASSESSMENT_PLAN.lifecycle, name="Response_lifecycle", curie=OSCAL_ASSESSMENT_PLAN.curie('lifecycle'),
                   model_uri=OSCAL.Response_lifecycle, domain=Response, range=str)

slots.RequiredAsset_uuid = Slot(uri=OSCAL_CATALOG.uuid, name="RequiredAsset_uuid", curie=OSCAL_CATALOG.curie('uuid'),
                   model_uri=OSCAL.RequiredAsset_uuid, domain=RequiredAsset, range=str)

slots.RequiredAsset_description = Slot(uri=OSCAL_CATALOG.description, name="RequiredAsset_description", curie=OSCAL_CATALOG.curie('description'),
                   model_uri=OSCAL.RequiredAsset_description, domain=RequiredAsset, range=str)

slots.RequiredAsset_subjects = Slot(uri=OSCAL_ASSESSMENT_PLAN.subjects, name="RequiredAsset_subjects", curie=OSCAL_ASSESSMENT_PLAN.curie('subjects'),
                   model_uri=OSCAL.RequiredAsset_subjects, domain=RequiredAsset, range=Optional[Union[Union[dict, SubjectReference], list[Union[dict, SubjectReference]]]])

slots.RiskLog_entries = Slot(uri=OSCAL_ASSESSMENT_PLAN.entries, name="RiskLog_entries", curie=OSCAL_ASSESSMENT_PLAN.curie('entries'),
                   model_uri=OSCAL.RiskLog_entries, domain=RiskLog, range=Union[Union[dict, "RiskLogEntry"], list[Union[dict, "RiskLogEntry"]]])

slots.RiskLogEntry_uuid = Slot(uri=OSCAL_CATALOG.uuid, name="RiskLogEntry_uuid", curie=OSCAL_CATALOG.curie('uuid'),
                   model_uri=OSCAL.RiskLogEntry_uuid, domain=RiskLogEntry, range=str)

slots.RiskLogEntry_start = Slot(uri=OSCAL_ASSESSMENT_PLAN.start, name="RiskLogEntry_start", curie=OSCAL_ASSESSMENT_PLAN.curie('start'),
                   model_uri=OSCAL.RiskLogEntry_start, domain=RiskLogEntry, range=str)

slots.LoggedBy_party_uuid = Slot(uri=OSCAL_ASSESSMENT_PLAN.party_uuid, name="LoggedBy_party-uuid", curie=OSCAL_ASSESSMENT_PLAN.curie('party_uuid'),
                   model_uri=OSCAL.LoggedBy_party_uuid, domain=LoggedBy, range=str)

slots.RiskResponseReference_response_uuid = Slot(uri=OSCAL_ASSESSMENT_PLAN.response_uuid, name="RiskResponseReference_response-uuid", curie=OSCAL_ASSESSMENT_PLAN.curie('response_uuid'),
                   model_uri=OSCAL.RiskResponseReference_response_uuid, domain=RiskResponseReference, range=str)

slots.AssessmentResultsDocument_assessment_results = Slot(uri=OSCAL_ASSESSMENT_RESULTS.assessment_results, name="AssessmentResultsDocument_assessment-results", curie=OSCAL_ASSESSMENT_RESULTS.curie('assessment_results'),
                   model_uri=OSCAL.AssessmentResultsDocument_assessment_results, domain=AssessmentResultsDocument, range=Union[dict, "AssessmentResults"])

slots.AssessmentResults_uuid = Slot(uri=OSCAL_CATALOG.uuid, name="AssessmentResults_uuid", curie=OSCAL_CATALOG.curie('uuid'),
                   model_uri=OSCAL.AssessmentResults_uuid, domain=AssessmentResults, range=str)

slots.AssessmentResults_metadata = Slot(uri=OSCAL_CATALOG.metadata, name="AssessmentResults_metadata", curie=OSCAL_CATALOG.curie('metadata'),
                   model_uri=OSCAL.AssessmentResults_metadata, domain=AssessmentResults, range=Union[dict, Metadata])

slots.AssessmentResults_import_ap = Slot(uri=OSCAL_ASSESSMENT_RESULTS.import_ap, name="AssessmentResults_import-ap", curie=OSCAL_ASSESSMENT_RESULTS.curie('import_ap'),
                   model_uri=OSCAL.AssessmentResults_import_ap, domain=AssessmentResults, range=Union[dict, "ImportAssessmentPlan"])

slots.AssessmentResults_local_definitions = Slot(uri=OSCAL_ASSESSMENT_PLAN.local_definitions, name="AssessmentResults_local-definitions", curie=OSCAL_ASSESSMENT_PLAN.curie('local_definitions'),
                   model_uri=OSCAL.AssessmentResults_local_definitions, domain=AssessmentResults, range=Optional[Union[dict, "AssessmentResultsLocalDefinitions"]])

slots.AssessmentResults_results = Slot(uri=OSCAL_ASSESSMENT_RESULTS.results, name="AssessmentResults_results", curie=OSCAL_ASSESSMENT_RESULTS.curie('results'),
                   model_uri=OSCAL.AssessmentResults_results, domain=AssessmentResults, range=Union[Union[dict, "Result"], list[Union[dict, "Result"]]])

slots.ImportAssessmentPlan_href = Slot(uri=OSCAL_CATALOG.href, name="ImportAssessmentPlan_href", curie=OSCAL_CATALOG.curie('href'),
                   model_uri=OSCAL.ImportAssessmentPlan_href, domain=ImportAssessmentPlan, range=str)

slots.Result_uuid = Slot(uri=OSCAL_CATALOG.uuid, name="Result_uuid", curie=OSCAL_CATALOG.curie('uuid'),
                   model_uri=OSCAL.Result_uuid, domain=Result, range=str)

slots.Result_title = Slot(uri=OSCAL_CATALOG.title, name="Result_title", curie=OSCAL_CATALOG.curie('title'),
                   model_uri=OSCAL.Result_title, domain=Result, range=str)

slots.Result_description = Slot(uri=OSCAL_CATALOG.description, name="Result_description", curie=OSCAL_CATALOG.curie('description'),
                   model_uri=OSCAL.Result_description, domain=Result, range=str)

slots.Result_start = Slot(uri=OSCAL_ASSESSMENT_PLAN.start, name="Result_start", curie=OSCAL_ASSESSMENT_PLAN.curie('start'),
                   model_uri=OSCAL.Result_start, domain=Result, range=str)

slots.Result_local_definitions = Slot(uri=OSCAL_ASSESSMENT_PLAN.local_definitions, name="Result_local-definitions", curie=OSCAL_ASSESSMENT_PLAN.curie('local_definitions'),
                   model_uri=OSCAL.Result_local_definitions, domain=Result, range=Optional[Union[dict, "ResultLocalDefinitions"]])

slots.Result_reviewed_controls = Slot(uri=OSCAL_ASSESSMENT_PLAN.reviewed_controls, name="Result_reviewed-controls", curie=OSCAL_ASSESSMENT_PLAN.curie('reviewed_controls'),
                   model_uri=OSCAL.Result_reviewed_controls, domain=Result, range=Union[dict, ReviewedControls])

slots.Result_assessment_log = Slot(uri=OSCAL_ASSESSMENT_RESULTS.assessment_log, name="Result_assessment-log", curie=OSCAL_ASSESSMENT_RESULTS.curie('assessment_log'),
                   model_uri=OSCAL.Result_assessment_log, domain=Result, range=Optional[Union[dict, "AssessmentLog"]])

slots.Attestation_parts = Slot(uri=OSCAL_CATALOG.parts, name="Attestation_parts", curie=OSCAL_CATALOG.curie('parts'),
                   model_uri=OSCAL.Attestation_parts, domain=Attestation, range=Union[Union[dict, AssessmentPart], list[Union[dict, AssessmentPart]]])

slots.AssessmentLog_entries = Slot(uri=OSCAL_ASSESSMENT_PLAN.entries, name="AssessmentLog_entries", curie=OSCAL_ASSESSMENT_PLAN.curie('entries'),
                   model_uri=OSCAL.AssessmentLog_entries, domain=AssessmentLog, range=Union[Union[dict, "AssessmentLogEntry"], list[Union[dict, "AssessmentLogEntry"]]])

slots.AssessmentLogEntry_uuid = Slot(uri=OSCAL_CATALOG.uuid, name="AssessmentLogEntry_uuid", curie=OSCAL_CATALOG.curie('uuid'),
                   model_uri=OSCAL.AssessmentLogEntry_uuid, domain=AssessmentLogEntry, range=str)

slots.AssessmentLogEntry_start = Slot(uri=OSCAL_ASSESSMENT_PLAN.start, name="AssessmentLogEntry_start", curie=OSCAL_ASSESSMENT_PLAN.curie('start'),
                   model_uri=OSCAL.AssessmentLogEntry_start, domain=AssessmentLogEntry, range=str)

slots.ComponentDefinitionDocument_component_definition = Slot(uri=OSCAL_COMPONENT.component_definition, name="ComponentDefinitionDocument_component-definition", curie=OSCAL_COMPONENT.curie('component_definition'),
                   model_uri=OSCAL.ComponentDefinitionDocument_component_definition, domain=ComponentDefinitionDocument, range=Union[dict, "ComponentDefinition"])

slots.ComponentDefinition_uuid = Slot(uri=OSCAL_CATALOG.uuid, name="ComponentDefinition_uuid", curie=OSCAL_CATALOG.curie('uuid'),
                   model_uri=OSCAL.ComponentDefinition_uuid, domain=ComponentDefinition, range=str)

slots.ComponentDefinition_metadata = Slot(uri=OSCAL_CATALOG.metadata, name="ComponentDefinition_metadata", curie=OSCAL_CATALOG.curie('metadata'),
                   model_uri=OSCAL.ComponentDefinition_metadata, domain=ComponentDefinition, range=Union[dict, Metadata])

slots.ComponentDefinition_components = Slot(uri=OSCAL_ASSESSMENT_PLAN.components, name="ComponentDefinition_components", curie=OSCAL_ASSESSMENT_PLAN.curie('components'),
                   model_uri=OSCAL.ComponentDefinition_components, domain=ComponentDefinition, range=Optional[Union[Union[dict, "DefinedComponent"], list[Union[dict, "DefinedComponent"]]]])

slots.ImportComponentDefinition_href = Slot(uri=OSCAL_CATALOG.href, name="ImportComponentDefinition_href", curie=OSCAL_CATALOG.curie('href'),
                   model_uri=OSCAL.ImportComponentDefinition_href, domain=ImportComponentDefinition, range=str)

slots.DefinedComponent_uuid = Slot(uri=OSCAL_CATALOG.uuid, name="DefinedComponent_uuid", curie=OSCAL_CATALOG.curie('uuid'),
                   model_uri=OSCAL.DefinedComponent_uuid, domain=DefinedComponent, range=str)

slots.DefinedComponent_type = Slot(uri=OSCAL_CATALOG.type, name="DefinedComponent_type", curie=OSCAL_CATALOG.curie('type'),
                   model_uri=OSCAL.DefinedComponent_type, domain=DefinedComponent, range=str)

slots.DefinedComponent_title = Slot(uri=OSCAL_CATALOG.title, name="DefinedComponent_title", curie=OSCAL_CATALOG.curie('title'),
                   model_uri=OSCAL.DefinedComponent_title, domain=DefinedComponent, range=str)

slots.DefinedComponent_description = Slot(uri=OSCAL_CATALOG.description, name="DefinedComponent_description", curie=OSCAL_CATALOG.curie('description'),
                   model_uri=OSCAL.DefinedComponent_description, domain=DefinedComponent, range=str)

slots.Capability_uuid = Slot(uri=OSCAL_CATALOG.uuid, name="Capability_uuid", curie=OSCAL_CATALOG.curie('uuid'),
                   model_uri=OSCAL.Capability_uuid, domain=Capability, range=str)

slots.Capability_name = Slot(uri=OSCAL_CATALOG.name, name="Capability_name", curie=OSCAL_CATALOG.curie('name'),
                   model_uri=OSCAL.Capability_name, domain=Capability, range=str)

slots.Capability_description = Slot(uri=OSCAL_CATALOG.description, name="Capability_description", curie=OSCAL_CATALOG.curie('description'),
                   model_uri=OSCAL.Capability_description, domain=Capability, range=str)

slots.IncorporatesComponent_component_uuid = Slot(uri=OSCAL_ASSESSMENT_PLAN.component_uuid, name="IncorporatesComponent_component-uuid", curie=OSCAL_ASSESSMENT_PLAN.curie('component_uuid'),
                   model_uri=OSCAL.IncorporatesComponent_component_uuid, domain=IncorporatesComponent, range=str)

slots.IncorporatesComponent_description = Slot(uri=OSCAL_CATALOG.description, name="IncorporatesComponent_description", curie=OSCAL_CATALOG.curie('description'),
                   model_uri=OSCAL.IncorporatesComponent_description, domain=IncorporatesComponent, range=str)

slots.ControlImplementationSet_set_parameters = Slot(uri=OSCAL_CATALOG.set_parameters, name="ControlImplementationSet_set-parameters", curie=OSCAL_CATALOG.curie('set_parameters'),
                   model_uri=OSCAL.ControlImplementationSet_set_parameters, domain=ControlImplementationSet, range=Optional[Union[Union[dict, SetParameter], list[Union[dict, SetParameter]]]])

slots.ControlImplementationSet_implemented_requirements = Slot(uri=OSCAL_CATALOG.implemented_requirements, name="ControlImplementationSet_implemented-requirements", curie=OSCAL_CATALOG.curie('implemented_requirements'),
                   model_uri=OSCAL.ControlImplementationSet_implemented_requirements, domain=ControlImplementationSet, range=Union[Union[dict, "ImplementedRequirement"], list[Union[dict, "ImplementedRequirement"]]])

slots.ControlImplementationSet_uuid = Slot(uri=OSCAL_CATALOG.uuid, name="ControlImplementationSet_uuid", curie=OSCAL_CATALOG.curie('uuid'),
                   model_uri=OSCAL.ControlImplementationSet_uuid, domain=ControlImplementationSet, range=str)

slots.ControlImplementationSet_source = Slot(uri=OSCAL_COMPONENT.source, name="ControlImplementationSet_source", curie=OSCAL_COMPONENT.curie('source'),
                   model_uri=OSCAL.ControlImplementationSet_source, domain=ControlImplementationSet, range=str)

slots.ControlImplementationSet_description = Slot(uri=OSCAL_CATALOG.description, name="ControlImplementationSet_description", curie=OSCAL_CATALOG.curie('description'),
                   model_uri=OSCAL.ControlImplementationSet_description, domain=ControlImplementationSet, range=str)

slots.ImplementedRequirement_set_parameters = Slot(uri=OSCAL_CATALOG.set_parameters, name="ImplementedRequirement_set-parameters", curie=OSCAL_CATALOG.curie('set_parameters'),
                   model_uri=OSCAL.ImplementedRequirement_set_parameters, domain=ImplementedRequirement, range=Optional[Union[Union[dict, SetParameter], list[Union[dict, SetParameter]]]])

slots.ImplementedRequirement_statements = Slot(uri=OSCAL_CATALOG.statements, name="ImplementedRequirement_statements", curie=OSCAL_CATALOG.curie('statements'),
                   model_uri=OSCAL.ImplementedRequirement_statements, domain=ImplementedRequirement, range=Optional[Union[Union[dict, "ImplementedControlStatement"], list[Union[dict, "ImplementedControlStatement"]]]])

slots.ImplementedRequirement_uuid = Slot(uri=OSCAL_CATALOG.uuid, name="ImplementedRequirement_uuid", curie=OSCAL_CATALOG.curie('uuid'),
                   model_uri=OSCAL.ImplementedRequirement_uuid, domain=ImplementedRequirement, range=str)

slots.ImplementedRequirement_control_id = Slot(uri=OSCAL_CATALOG.control_id, name="ImplementedRequirement_control-id", curie=OSCAL_CATALOG.curie('control_id'),
                   model_uri=OSCAL.ImplementedRequirement_control_id, domain=ImplementedRequirement, range=str)

slots.ImplementedRequirement_description = Slot(uri=OSCAL_CATALOG.description, name="ImplementedRequirement_description", curie=OSCAL_CATALOG.curie('description'),
                   model_uri=OSCAL.ImplementedRequirement_description, domain=ImplementedRequirement, range=str)

slots.ImplementedControlStatement_statement_id = Slot(uri=OSCAL_CATALOG.statement_id, name="ImplementedControlStatement_statement-id", curie=OSCAL_CATALOG.curie('statement_id'),
                   model_uri=OSCAL.ImplementedControlStatement_statement_id, domain=ImplementedControlStatement, range=str)

slots.ImplementedControlStatement_uuid = Slot(uri=OSCAL_CATALOG.uuid, name="ImplementedControlStatement_uuid", curie=OSCAL_CATALOG.curie('uuid'),
                   model_uri=OSCAL.ImplementedControlStatement_uuid, domain=ImplementedControlStatement, range=str)

slots.ImplementedControlStatement_description = Slot(uri=OSCAL_CATALOG.description, name="ImplementedControlStatement_description", curie=OSCAL_CATALOG.curie('description'),
                   model_uri=OSCAL.ImplementedControlStatement_description, domain=ImplementedControlStatement, range=str)

slots.MappingCollectionDocument_mapping_collection = Slot(uri=OSCAL_MAPPING.mapping_collection, name="MappingCollectionDocument_mapping-collection", curie=OSCAL_MAPPING.curie('mapping_collection'),
                   model_uri=OSCAL.MappingCollectionDocument_mapping_collection, domain=MappingCollectionDocument, range=Union[dict, "MappingCollection"])

slots.MappingCollection_uuid = Slot(uri=OSCAL_CATALOG.uuid, name="MappingCollection_uuid", curie=OSCAL_CATALOG.curie('uuid'),
                   model_uri=OSCAL.MappingCollection_uuid, domain=MappingCollection, range=str)

slots.MappingCollection_metadata = Slot(uri=OSCAL_CATALOG.metadata, name="MappingCollection_metadata", curie=OSCAL_CATALOG.curie('metadata'),
                   model_uri=OSCAL.MappingCollection_metadata, domain=MappingCollection, range=Union[dict, Metadata])

slots.MappingCollection_provenance = Slot(uri=OSCAL_MAPPING.provenance, name="MappingCollection_provenance", curie=OSCAL_MAPPING.curie('provenance'),
                   model_uri=OSCAL.MappingCollection_provenance, domain=MappingCollection, range=Union[dict, "MappingProvenance"])

slots.MappingCollection_mappings = Slot(uri=OSCAL_MAPPING.mappings, name="MappingCollection_mappings", curie=OSCAL_MAPPING.curie('mappings'),
                   model_uri=OSCAL.MappingCollection_mappings, domain=MappingCollection, range=Union[Union[dict, "Mapping"], list[Union[dict, "Mapping"]]])

slots.MappingProvenance_method = Slot(uri=OSCAL_CATALOG.method, name="MappingProvenance_method", curie=OSCAL_CATALOG.curie('method'),
                   model_uri=OSCAL.MappingProvenance_method, domain=MappingProvenance, range=Union[str, "MappingMethodEnum"])

slots.MappingProvenance_matching_rationale = Slot(uri=OSCAL_MAPPING.matching_rationale, name="MappingProvenance_matching-rationale", curie=OSCAL_MAPPING.curie('matching_rationale'),
                   model_uri=OSCAL.MappingProvenance_matching_rationale, domain=MappingProvenance, range=Union[str, "MatchingRationaleEnum"])

slots.MappingProvenance_status = Slot(uri=OSCAL_CATALOG.status, name="MappingProvenance_status", curie=OSCAL_CATALOG.curie('status'),
                   model_uri=OSCAL.MappingProvenance_status, domain=MappingProvenance, range=Union[str, "MappingStatusEnum"])

slots.MappingProvenance_mapping_description = Slot(uri=OSCAL_MAPPING.mapping_description, name="MappingProvenance_mapping-description", curie=OSCAL_MAPPING.curie('mapping_description'),
                   model_uri=OSCAL.MappingProvenance_mapping_description, domain=MappingProvenance, range=str)

slots.Mapping_uuid = Slot(uri=OSCAL_CATALOG.uuid, name="Mapping_uuid", curie=OSCAL_CATALOG.curie('uuid'),
                   model_uri=OSCAL.Mapping_uuid, domain=Mapping, range=str)

slots.Mapping_method = Slot(uri=OSCAL_CATALOG.method, name="Mapping_method", curie=OSCAL_CATALOG.curie('method'),
                   model_uri=OSCAL.Mapping_method, domain=Mapping, range=Optional[Union[str, "MappingMethodEnum"]])

slots.Mapping_status = Slot(uri=OSCAL_CATALOG.status, name="Mapping_status", curie=OSCAL_CATALOG.curie('status'),
                   model_uri=OSCAL.Mapping_status, domain=Mapping, range=Optional[Union[str, "MappingStatusEnum"]])

slots.Mapping_source_resource = Slot(uri=OSCAL_MAPPING.source_resource, name="Mapping_source-resource", curie=OSCAL_MAPPING.curie('source_resource'),
                   model_uri=OSCAL.Mapping_source_resource, domain=Mapping, range=Union[dict, "MappingResourceReference"])

slots.Mapping_target_resource = Slot(uri=OSCAL_MAPPING.target_resource, name="Mapping_target-resource", curie=OSCAL_MAPPING.curie('target_resource'),
                   model_uri=OSCAL.Mapping_target_resource, domain=Mapping, range=Union[dict, "MappingResourceReference"])

slots.Mapping_maps = Slot(uri=OSCAL_MAPPING.maps, name="Mapping_maps", curie=OSCAL_MAPPING.curie('maps'),
                   model_uri=OSCAL.Mapping_maps, domain=Mapping, range=Union[Union[dict, "Map"], list[Union[dict, "Map"]]])

slots.Map_uuid = Slot(uri=OSCAL_CATALOG.uuid, name="Map_uuid", curie=OSCAL_CATALOG.curie('uuid'),
                   model_uri=OSCAL.Map_uuid, domain=Map, range=str)

slots.Map_relationship = Slot(uri=OSCAL_MAPPING.relationship, name="Map_relationship", curie=OSCAL_MAPPING.curie('relationship'),
                   model_uri=OSCAL.Map_relationship, domain=Map, range=str)

slots.Map_sources = Slot(uri=OSCAL_CATALOG.sources, name="Map_sources", curie=OSCAL_CATALOG.curie('sources'),
                   model_uri=OSCAL.Map_sources, domain=Map, range=Union[Union[dict, "MappingItem"], list[Union[dict, "MappingItem"]]])

slots.Map_targets = Slot(uri=OSCAL_MAPPING.targets, name="Map_targets", curie=OSCAL_MAPPING.curie('targets'),
                   model_uri=OSCAL.Map_targets, domain=Map, range=Union[Union[dict, "MappingItem"], list[Union[dict, "MappingItem"]]])

slots.MappingItem_type = Slot(uri=OSCAL_CATALOG.type, name="MappingItem_type", curie=OSCAL_CATALOG.curie('type'),
                   model_uri=OSCAL.MappingItem_type, domain=MappingItem, range=Union[str, "MappingSubjectTypeEnum"])

slots.MappingItem_id_ref = Slot(uri=OSCAL_MAPPING.id_ref, name="MappingItem_id-ref", curie=OSCAL_MAPPING.curie('id_ref'),
                   model_uri=OSCAL.MappingItem_id_ref, domain=MappingItem, range=str)

slots.MappingResourceReference_type = Slot(uri=OSCAL_CATALOG.type, name="MappingResourceReference_type", curie=OSCAL_CATALOG.curie('type'),
                   model_uri=OSCAL.MappingResourceReference_type, domain=MappingResourceReference, range=str)

slots.MappingResourceReference_href = Slot(uri=OSCAL_CATALOG.href, name="MappingResourceReference_href", curie=OSCAL_CATALOG.curie('href'),
                   model_uri=OSCAL.MappingResourceReference_href, domain=MappingResourceReference, range=str)

slots.QualifierItem_category = Slot(uri=OSCAL_MAPPING.category, name="QualifierItem_category", curie=OSCAL_MAPPING.curie('category'),
                   model_uri=OSCAL.QualifierItem_category, domain=QualifierItem, range=Union[str, "QualifierCategoryEnum"])

slots.QualifierItem_description = Slot(uri=OSCAL_CATALOG.description, name="QualifierItem_description", curie=OSCAL_CATALOG.curie('description'),
                   model_uri=OSCAL.QualifierItem_description, domain=QualifierItem, range=str)

slots.QualifierItem_predicate = Slot(uri=OSCAL_MAPPING.predicate, name="QualifierItem_predicate", curie=OSCAL_MAPPING.curie('predicate'),
                   model_uri=OSCAL.QualifierItem_predicate, domain=QualifierItem, range=Union[str, "QualifierPredicateEnum"])

slots.QualifierItem_subject = Slot(uri=OSCAL_MAPPING.subject, name="QualifierItem_subject", curie=OSCAL_MAPPING.curie('subject'),
                   model_uri=OSCAL.QualifierItem_subject, domain=QualifierItem, range=Union[str, "QualifierSubjectEnum"])

slots.GapSummary_uuid = Slot(uri=OSCAL_CATALOG.uuid, name="GapSummary_uuid", curie=OSCAL_CATALOG.curie('uuid'),
                   model_uri=OSCAL.GapSummary_uuid, domain=GapSummary, range=str)

slots.GapSummary_unmapped_controls = Slot(uri=OSCAL_MAPPING.unmapped_controls, name="GapSummary_unmapped-controls", curie=OSCAL_MAPPING.curie('unmapped_controls'),
                   model_uri=OSCAL.GapSummary_unmapped_controls, domain=GapSummary, range=Union[Union[dict, SelectControlById], list[Union[dict, SelectControlById]]])

slots.ConfidenceScore_category = Slot(uri=OSCAL_MAPPING.category, name="ConfidenceScore_category", curie=OSCAL_MAPPING.curie('category'),
                   model_uri=OSCAL.ConfidenceScore_category, domain=ConfidenceScore, range=Optional[str])

slots.Coverage_target_coverage = Slot(uri=OSCAL_MAPPING.target_coverage, name="Coverage_target-coverage", curie=OSCAL_MAPPING.curie('target_coverage'),
                   model_uri=OSCAL.Coverage_target_coverage, domain=Coverage, range=float)

slots.PoamDocument_plan_of_action_and_milestones = Slot(uri=OSCAL_POAM.plan_of_action_and_milestones, name="PoamDocument_plan-of-action-and-milestones", curie=OSCAL_POAM.curie('plan_of_action_and_milestones'),
                   model_uri=OSCAL.PoamDocument_plan_of_action_and_milestones, domain=PoamDocument, range=Union[dict, "PlanOfActionAndMilestones"])

slots.PlanOfActionAndMilestones_uuid = Slot(uri=OSCAL_CATALOG.uuid, name="PlanOfActionAndMilestones_uuid", curie=OSCAL_CATALOG.curie('uuid'),
                   model_uri=OSCAL.PlanOfActionAndMilestones_uuid, domain=PlanOfActionAndMilestones, range=str)

slots.PlanOfActionAndMilestones_metadata = Slot(uri=OSCAL_CATALOG.metadata, name="PlanOfActionAndMilestones_metadata", curie=OSCAL_CATALOG.curie('metadata'),
                   model_uri=OSCAL.PlanOfActionAndMilestones_metadata, domain=PlanOfActionAndMilestones, range=Union[dict, Metadata])

slots.PlanOfActionAndMilestones_local_definitions = Slot(uri=OSCAL_ASSESSMENT_PLAN.local_definitions, name="PlanOfActionAndMilestones_local-definitions", curie=OSCAL_ASSESSMENT_PLAN.curie('local_definitions'),
                   model_uri=OSCAL.PlanOfActionAndMilestones_local_definitions, domain=PlanOfActionAndMilestones, range=Optional[Union[dict, "PoamLocalDefinitions"]])

slots.PlanOfActionAndMilestones_poam_items = Slot(uri=OSCAL_POAM.poam_items, name="PlanOfActionAndMilestones_poam-items", curie=OSCAL_POAM.curie('poam_items'),
                   model_uri=OSCAL.PlanOfActionAndMilestones_poam_items, domain=PlanOfActionAndMilestones, range=Union[Union[dict, "PoamItem"], list[Union[dict, "PoamItem"]]])

slots.PoamItem_title = Slot(uri=OSCAL_CATALOG.title, name="PoamItem_title", curie=OSCAL_CATALOG.curie('title'),
                   model_uri=OSCAL.PoamItem_title, domain=PoamItem, range=str)

slots.PoamItem_description = Slot(uri=OSCAL_CATALOG.description, name="PoamItem_description", curie=OSCAL_CATALOG.curie('description'),
                   model_uri=OSCAL.PoamItem_description, domain=PoamItem, range=str)

slots.RelatedFinding_finding_uuid = Slot(uri=OSCAL_POAM.finding_uuid, name="RelatedFinding_finding-uuid", curie=OSCAL_POAM.curie('finding_uuid'),
                   model_uri=OSCAL.RelatedFinding_finding_uuid, domain=RelatedFinding, range=str)
