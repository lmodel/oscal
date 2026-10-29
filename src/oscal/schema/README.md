# Schema Directory

This folder holds the LinkML schema of OSCAL 1.2.3, one module per OSCAL
model, and the OSCAL release it renders.

- `oscal.yaml`, the umbrella schema, which imports every module
- `oscal_catalog.yaml`
- `oscal_profile.yaml`
- `oscal_component.yaml`
- `oscal_ssp.yaml`
- `oscal_assessment_plan.yaml`
- `oscal_assessment_results.yaml`
- `oscal_poam.yaml`
- `oscal_mapping.yaml`
- `metaschema/`, OSCAL's metaschema sources from the v1.2.3 release, copied
  byte for byte with NIST's `LICENSE.md`. Never edit them; replace them from
  the next release and move the pins in `scripts/check_upstream_release.py`.
