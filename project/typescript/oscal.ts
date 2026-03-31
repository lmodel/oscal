
export enum PartyTypeEnum {
    
    person = "person",
    organization = "organization",
};
/**
* Curated hash algorithm values. Other values are permitted (OSCAL allow-other="yes").

*/
export enum HashAlgorithmEnum {
    
    SHA_224 = "SHA-224",
    SHA_256 = "SHA-256",
    SHA_384 = "SHA-384",
    SHA_512 = "SHA-512",
    SHA3_224 = "SHA3-224",
    SHA3_256 = "SHA3-256",
    SHA3_384 = "SHA3-384",
    SHA3_512 = "SHA3-512",
};
/**
* Curated telephone number type values. Other values are permitted (OSCAL allow-other="yes").

*/
export enum PhoneTypeEnum {
    
    home = "home",
    office = "office",
    mobile = "mobile",
};
/**
* Curated address type values. Other values are permitted (OSCAL allow-other="yes").

*/
export enum AddressTypeEnum {
    
    home = "home",
    work = "work",
};
/**
* Curated metadata link relation values. Other values are permitted (OSCAL allow-other="yes").

*/
export enum MetadataLinkRelEnum {
    
    canonical = "canonical",
    alternate = "alternate",
    latest_version = "latest-version",
    predecessor_version = "predecessor-version",
    successor_version = "successor-version",
    version_history = "version-history",
    reference = "reference",
    source_profile = "source-profile",
    source_profile_uuid = "source-profile-uuid",
};
/**
* Allowed OSCAL property names for metadata locations.
*/
export enum LocationPropNameEnum {
    
    type = "type",
};
/**
* Curated OSCAL location type property values. Other values are permitted (OSCAL allow-other="yes").

*/
export enum LocationPropTypeEnum {
    
    data_center = "data-center",
};
/**
* Curated OSCAL location class values for data-center type. Other values are permitted (OSCAL allow-other="yes").

*/
export enum LocationDataCenterClassEnum {
    
    primary = "primary",
    alternate = "alternate",
};
/**
* Curated external identifier scheme values for metadata parties. Other values are permitted (OSCAL allow-other="yes").

*/
export enum PartyExternalIdSchemeEnum {
    
    httpCOLONSOLIDUSSOLIDUSorcidFULL_STOPorgSOLIDUS = "http://orcid.org/",
};
/**
* Allowed OSCAL property names for metadata parties.
*/
export enum PartyPropNameEnum {
    
    mail_stop = "mail-stop",
    office = "office",
    job_title = "job-title",
};
/**
* Curated metadata responsible-party role identifiers. Other values are permitted (OSCAL allow-other="yes").

*/
export enum MetadataResponsiblePartyRoleIdEnum {
    
    creator = "creator",
    prepared_by = "prepared-by",
    prepared_for = "prepared-for",
    content_approver = "content-approver",
    contact = "contact",
};
/**
* Allowed OSCAL property names for metadata.
*/
export enum MetadataPropNameEnum {
    
    keywords = "keywords",
    resolution_tool = "resolution-tool",
    source_profile_uuid = "source-profile-uuid",
};
/**
* Allowed OSCAL property names for metadata revisions.
*/
export enum RevisionPropNameEnum {
    
    marking = "marking",
};
/**
* Allowed OSCAL property names for back-matter resources.
*/
export enum ResourcePropNameEnum {
    
    type = "type",
    version = "version",
    published = "published",
};
/**
* Allowed OSCAL back-matter resource type property values.
*/
export enum ResourcePropTypeEnum {
    
    logo = "logo",
    image = "image",
    screen_shot = "screen-shot",
    law = "law",
    regulation = "regulation",
    standard = "standard",
    external_guidance = "external-guidance",
    acronyms = "acronyms",
    citation = "citation",
    policy = "policy",
    procedure = "procedure",
    system_guide = "system-guide",
    users_guide = "users-guide",
    administrators_guide = "administrators-guide",
    rules_of_behavior = "rules-of-behavior",
    plan = "plan",
    artifact = "artifact",
    evidence = "evidence",
    tool_output = "tool-output",
    raw_data = "raw-data",
    interview_notes = "interview-notes",
    questionnaire = "questionnaire",
    report = "report",
    agreement = "agreement",
};
/**
* Curated OSCAL action system values. Other values are permitted (OSCAL allow-other="yes").

*/
export enum ActionSystemEnum {
    
    httpCOLONSOLIDUSSOLIDUScsrcFULL_STOPnistFULL_STOPgovSOLIDUSnsSOLIDUSoscal = "http://csrc.nist.gov/ns/oscal",
};
/**
* Allowed OSCAL action type values.
*/
export enum ActionTypeEnum {
    
    approval = "approval",
    request_changes = "request-changes",
};
/**
* Curated document identifier scheme values. Other values are permitted (OSCAL allow-other="yes").

*/
export enum DocumentIdSchemeEnum {
    
    httpCOLONSOLIDUSSOLIDUSwwwFULL_STOPdoiFULL_STOPorgSOLIDUS = "http://www.doi.org/",
};

export enum ParameterCardinalityEnum {
    
    one = "one",
    one_or_more = "one-or-more",
};
/**
* Allowed OSCAL property names for control-common parts.
*/
export enum PartPropNameEnum {
    
    label = "label",
    sort_id = "sort-id",
    alt_identifier = "alt-identifier",
};
/**
* Allowed OSCAL property names for control-common parameters.
*/
export enum ParameterPropNameEnum {
    
    label = "label",
    sort_id = "sort-id",
    alt_identifier = "alt-identifier",
    alt_label = "alt-label",
};
/**
* Allowed OSCAL RMF parameter property names.
*/
export enum RmfParameterPropNameEnum {
    
    aggregates = "aggregates",
};
/**
* Allowed OSCAL part names for catalog groups.
*/
export enum GroupPartNameEnum {
    
    overview = "overview",
    instruction = "instruction",
};
/**
* Allowed OSCAL property names for catalog controls.
*/
export enum ControlPropNameEnum {
    
    label = "label",
    sort_id = "sort-id",
    alt_identifier = "alt-identifier",
    status = "status",
};
/**
* Allowed OSCAL status property values for catalog controls.
*/
export enum ControlPropStatusValueEnum {
    
    withdrawn = "withdrawn",
    Withdrawn = "Withdrawn",
};
/**
* Curated OSCAL link relation values for catalog controls. Other values are permitted (OSCAL allow-other="yes").
*/
export enum ControlLinkRelEnum {
    
    reference = "reference",
    related = "related",
    required = "required",
    incorporated_into = "incorporated-into",
    moved_to = "moved-to",
};
/**
* Allowed top-level OSCAL part names for catalog controls.
*/
export enum ControlPartNameEnum {
    
    overview = "overview",
    statement = "statement",
    guidance = "guidance",
    example = "example",
    assessment = "assessment",
    assessment_method = "assessment-method",
};
/**
* Allowed OSCAL subpart names for control statement parts.
*/
export enum ControlStatementPartSubpartNameEnum {
    
    item = "item",
};
/**
* Allowed OSCAL part names for control statement parts.
*/
export enum ControlStatementPartNameEnum {
    
    objective = "objective",
    assessment_objective = "assessment-objective",
};
/**
* Allowed OSCAL subpart names for control objective parts.
*/
export enum ControlObjectivePartSubpartNameEnum {
    
    objects = "objects",
    assessment_objects = "assessment-objects",
};
/**
* Allowed OSCAL property names for control statement parts.
*/
export enum ControlStatementPartPropNameEnum {
    
    method = "method",
};
/**
* Allowed OSCAL RMF property names for control statement parts.
*/
export enum ControlStatementPartRmfPropNameEnum {
    
    method = "method",
};
/**
* Allowed OSCAL method property values for control objectives.
*/
export enum ControlObjectivePartMethodPropValueEnum {
    
    INTERVIEW = "INTERVIEW",
    EXAMINE = "EXAMINE",
    TEST = "TEST",
};

export enum WithChildControlsEnum {
    
    yes = "yes",
    no = "no",
};
/**
* Ordering options for a selection of controls.
*/
export enum InsertOrderEnum {
    
    keep = "keep",
    ascending = "ascending",
    descending = "descending",
};
/**
* Where new content is added relative to the targeted element.
*/
export enum AdditionPositionEnum {
    
    before = "before",
    after = "after",
    starting = "starting",
    ending = "ending",
};
/**
* Identifies content to remove by the item's object type name.
*/
export enum ByItemNameEnum {
    
    param = "param",
    prop = "prop",
    link = "link",
    part = "part",
    mapping = "mapping",
    map = "map",
};
/**
* Methods for resolving duplicate control instances during merge.
*/
export enum CombinationMethodEnum {
    
    use_first = "use-first",
    merge = "merge",
    keep = "keep",
};
/**
* Allowed OSCAL property names for profile modification additions.
*/
export enum AlterationPropNameEnum {
    
    label = "label",
    sort_id = "sort-id",
    alt_identifier = "alt-identifier",
};
/**
* Curated task type values. Other values are permitted (OSCAL allow-other="yes").

*/
export enum TaskTypeEnum {
    
    milestone = "milestone",
    action = "action",
};

export enum TimingUnitEnum {
    
    seconds = "seconds",
    minutes = "minutes",
    hours = "hours",
    days = "days",
    months = "months",
    years = "years",
};
/**
* Curated assessment subject type values. Other values are permitted (OSCAL allow-other="yes").

*/
export enum AssessmentSubjectTypeEnum {
    
    component = "component",
    inventory_item = "inventory-item",
    location = "location",
    party = "party",
    user = "user",
};
/**
* Curated subject type values for subject selection. Other values are permitted (OSCAL allow-other="yes").

*/
export enum SelectSubjectTypeEnum {
    
    component = "component",
    inventory_item = "inventory-item",
    location = "location",
    party = "party",
    user = "user",
    resource = "resource",
};

export enum OriginActorTypeEnum {
    
    tool = "tool",
    assessment_platform = "assessment-platform",
    party = "party",
};
/**
* Curated observation method values. Other values are permitted (OSCAL allow-other="yes").

*/
export enum ObservationMethodEnum {
    
    EXAMINE = "EXAMINE",
    INTERVIEW = "INTERVIEW",
    TEST = "TEST",
    UNKNOWN = "UNKNOWN",
};
/**
* Curated observation type values. Other values are permitted (OSCAL allow-other="yes").

*/
export enum ObservationTypeEnum {
    
    ssp_statement_issue = "ssp-statement-issue",
    control_objective = "control-objective",
    mitigation = "mitigation",
    finding = "finding",
    discovery = "discovery",
    historic = "historic",
};
/**
* Curated risk status values. Other values are permitted (OSCAL allow-other="yes").

*/
export enum RiskStatusEnum {
    
    open = "open",
    investigating = "investigating",
    remediating = "remediating",
    deviation_requested = "deviation-requested",
    deviation_approved = "deviation-approved",
    closed = "closed",
};

export enum FindingTargetTypeEnum {
    
    statement_id = "statement-id",
    objective_id = "objective-id",
};

export enum ObjectiveStatusStateEnum {
    
    satisfied = "satisfied",
    not_satisfied = "not-satisfied",
};
/**
* Curated objective status reason values. Other values are permitted (OSCAL allow-other="yes").

*/
export enum ObjectiveStatusReasonEnum {
    
    pass = "pass",
    fail = "fail",
    other = "other",
};
/**
* Curated implementation status state values. Other values are permitted (OSCAL allow-other="yes").

*/
export enum ImplementationStatusStateEnum {
    
    implemented = "implemented",
    partial = "partial",
    planned = "planned",
    alternative = "alternative",
    not_applicable = "not-applicable",
};
/**
* Curated component type values. Other values are permitted (OSCAL allow-other="yes").

*/
export enum ComponentTypeEnum {
    
    this_system = "this-system",
    system = "system",
    interconnection = "interconnection",
    software = "software",
    hardware = "hardware",
    service = "service",
    policy = "policy",
    physical = "physical",
    process_procedure = "process-procedure",
    plan = "plan",
    guidance = "guidance",
    standard = "standard",
    validation = "validation",
    network = "network",
};

export enum ComponentStateEnum {
    
    under_development = "under-development",
    operational = "operational",
    disposition = "disposition",
    other = "other",
};

export enum TransportEnum {
    
    TCP = "TCP",
    UDP = "UDP",
};
/**
* Allowed OSCAL implementation-common property names.
*/
export enum ImplementationPropNameEnum {
    
    implementation_point = "implementation-point",
    leveraged_authorization_uuid = "leveraged-authorization-uuid",
    inherited_uuid = "inherited-uuid",
    asset_type = "asset-type",
    asset_id = "asset-id",
    asset_tag = "asset-tag",
    public = "public",
    virtual = "virtual",
    vlan_id = "vlan-id",
    network_id = "network-id",
    label = "label",
    sort_id = "sort-id",
    baseline_configuration_name = "baseline-configuration-name",
    allows_authenticated_scan = "allows-authenticated-scan",
    function = "function",
    hardware_model = "hardware-model",
    model = "model",
    os_name = "os-name",
    os_version = "os-version",
    software_name = "software-name",
    software_version = "software-version",
    software_patch_level = "software-patch-level",
    version = "version",
    patch_level = "patch-level",
    release_date = "release-date",
    validation_type = "validation-type",
    validation_reference = "validation-reference",
    vendor_name = "vendor-name",
    software_identifier = "software-identifier",
    isa_title = "isa-title",
    isa_date = "isa-date",
    isa_remote_system_name = "isa-remote-system-name",
    ipv4_address = "ipv4-address",
    ipv6_address = "ipv6-address",
    direction = "direction",
    uri = "uri",
    fqdn = "fqdn",
    serial_number = "serial-number",
    netbios_name = "netbios-name",
    mac_address = "mac-address",
    physical_location = "physical-location",
    is_scanned = "is-scanned",
    type = "type",
    privilege_level = "privilege-level",
};
/**
* Curated implementation-common link relation values. Other values are permitted (OSCAL allow-other="yes").
*/
export enum ImplementationLinkRelEnum {
    
    depends_on = "depends-on",
    validation = "validation",
    proof_of_compliance = "proof-of-compliance",
    baseline_template = "baseline-template",
    uses_service = "uses-service",
    system_security_plan = "system-security-plan",
    uses_network = "uses-network",
    imported_from = "imported-from",
    validation_details = "validation-details",
    provided_by = "provided-by",
    used_by = "used-by",
    isa_agreement = "isa-agreement",
};
/**
* Curated implementation asset type values. Other values are permitted (OSCAL allow-other="yes").
*/
export enum ImplementationAssetTypeEnum {
    
    operating_system = "operating-system",
    database = "database",
    web_server = "web-server",
    dns_server = "dns-server",
    email_server = "email-server",
    directory_server = "directory-server",
    pbx = "pbx",
    firewall = "firewall",
    router = "router",
    switch = "switch",
    storage_array = "storage-array",
    appliance = "appliance",
};

export enum ImplementationPointEnum {
    
    internal = "internal",
    external = "external",
};

export enum ImplementationIpAddressClassEnum {
    
    local = "local",
    remote = "remote",
};

export enum ImplementationDirectionEnum {
    
    incoming = "incoming",
    outgoing = "outgoing",
};

export enum UserTypeEnum {
    
    internal = "internal",
    external = "external",
    general_public = "general-public",
};

export enum UserPrivilegeLevelEnum {
    
    privileged = "privileged",
    non_privileged = "non-privileged",
    no_logical_access = "no-logical-access",
};
/**
* Curated interconnection responsible-role identifiers. Other values are permitted (OSCAL allow-other="yes").
*/
export enum InterconnectionResponsibleRoleIdEnum {
    
    isa_poc_local = "isa-poc-local",
    isa_poc_remote = "isa-poc-remote",
    isa_authorizing_official_local = "isa-authorizing-official-local",
    isa_authorizing_official_remote = "isa-authorizing-official-remote",
};
/**
* Curated implementation-common role identifiers used in responsible role and responsible party contexts. Other values are permitted (OSCAL allow-other="yes").
*/
export enum ImplementationResponsibleRoleIdEnum {
    
    asset_owner = "asset-owner",
    asset_administrator = "asset-administrator",
    security_operations = "security-operations",
    network_operations = "network-operations",
    incident_response = "incident-response",
    help_desk = "help-desk",
    configuration_management = "configuration-management",
    maintainer = "maintainer",
    provider = "provider",
};
/**
* Implementation-common yes/no value set used by several properties.
*/
export enum ImplementationYesNoEnum {
    
    yes = "yes",
    no = "no",
};
/**
* Curated system identifier type URIs. Other values are permitted (OSCAL allow-other="yes").
*/
export enum SystemIdentifierTypeEnum {
    
    httpCOLONSOLIDUSSOLIDUSfedrampFULL_STOPgov = "http://fedramp.gov",
    httpCOLONSOLIDUSSOLIDUSfedrampFULL_STOPgovSOLIDUSnsSOLIDUSoscal = "http://fedramp.gov/ns/oscal",
    httpsCOLONSOLIDUSSOLIDUSietfFULL_STOPorgSOLIDUSrfcSOLIDUSrfc4122 = "https://ietf.org/rfc/rfc4122",
    httpCOLONSOLIDUSSOLIDUSietfFULL_STOPorgSOLIDUSrfcSOLIDUSrfc4122 = "http://ietf.org/rfc/rfc4122",
    httpCOLONSOLIDUSSOLIDUSdatatrackerFULL_STOPietfFULL_STOPorgSOLIDUSdocSOLIDUShtmlSOLIDUSrfc4122 = "http://datatracker.ietf.org/doc/html/rfc4122",
};
/**
* Curated assessment part name values. Other values are permitted (OSCAL allow-other="yes").

*/
export enum AssessmentPartNameEnum {
    
    asset = "asset",
    method = "method",
    objective = "objective",
};
/**
* Allowed part names in assessment plan terms-and-conditions.
*/
export enum TermsAndConditionsPartNameEnum {
    
    rules_of_engagement = "rules-of-engagement",
    disclosures = "disclosures",
    assessment_inclusions = "assessment-inclusions",
    assessment_exclusions = "assessment-exclusions",
    results_delivery = "results-delivery",
    assumptions = "assumptions",
    methodology = "methodology",
};
/**
* Values from assessment-common set oscal-assessment-objective-types.
*/
export enum OscalAssessmentObjectiveTypesEnum {
    
    objective = "objective",
    assessment = "assessment",
    assessment_objective = "assessment-objective",
    assessment_method = "assessment-method",
};
/**
* Values from assessment-common set oscal-risk-prop-type-values.
*/
export enum OscalRiskPropTypeValuesEnum {
    
    vendor_check_in = "vendor-check-in",
    status_update = "status-update",
    milestone_complete = "milestone-complete",
    mitigation = "mitigation",
    remediated = "remediated",
    closed = "closed",
    dr_submission = "dr-submission",
    dr_updated = "dr-updated",
    dr_approved = "dr-approved",
    dr_rejected = "dr-rejected",
};
/**
* Values from assessment-common set oscal-risk-prop-name-values.
*/
export enum OscalRiskPropNameValuesEnum {
    
    false_positive = "false-positive",
    accepted = "accepted",
    risk_adjusted = "risk-adjusted",
    priority = "priority",
};
/**
* Values from assessment-common set oscal-characterization-facet-name-system-values.
*/
export enum OscalCharacterizationFacetNameSystemValuesEnum {
    
    httpCOLONSOLIDUSSOLIDUSfedrampFULL_STOPgov = "http://fedramp.gov",
    httpCOLONSOLIDUSSOLIDUSfedrampFULL_STOPgovSOLIDUSnsSOLIDUSoscal = "http://fedramp.gov/ns/oscal",
    httpCOLONSOLIDUSSOLIDUScsrcFULL_STOPnistFULL_STOPgovSOLIDUSnsSOLIDUSoscal = "http://csrc.nist.gov/ns/oscal",
    httpCOLONSOLIDUSSOLIDUScsrcFULL_STOPnistFULL_STOPgovSOLIDUSnsSOLIDUSoscalSOLIDUSunknown = "http://csrc.nist.gov/ns/oscal/unknown",
    httpCOLONSOLIDUSSOLIDUScveFULL_STOPmitreFULL_STOPorg = "http://cve.mitre.org",
    httpCOLONSOLIDUSSOLIDUSwwwFULL_STOPfirstFULL_STOPorgSOLIDUScvssSOLIDUSv2FULL_STOP0 = "http://www.first.org/cvss/v2.0",
    httpCOLONSOLIDUSSOLIDUSwwwFULL_STOPfirstFULL_STOPorgSOLIDUScvssSOLIDUSv3FULL_STOP0 = "http://www.first.org/cvss/v3.0",
    httpCOLONSOLIDUSSOLIDUSwwwFULL_STOPfirstFULL_STOPorgSOLIDUScvssSOLIDUSv3FULL_STOP1 = "http://www.first.org/cvss/v3.1",
    httpsCOLONSOLIDUSSOLIDUSwwwFULL_STOPfirstFULL_STOPorgSOLIDUScvssSOLIDUSv4_0 = "https://www.first.org/cvss/v4-0",
};
/**
* Values from assessment-common set oscal-facet-prop-name-values.
*/
export enum OscalFacetPropNameValuesEnum {
    
    state = "state",
};
/**
* Values from assessment-common set oscal-facet-prop-state-values.
*/
export enum OscalFacetPropStateValuesEnum {
    
    initial = "initial",
    adjusted = "adjusted",
};
/**
* Values from assessment-common set oscal-facet-name-core-values.
*/
export enum OscalFacetNameCoreValuesEnum {
    
    likelihood = "likelihood",
    impact = "impact",
    risk = "risk",
    severity = "severity",
};
/**
* Values from assessment-common set oscal-facet-fedramp-values.
*/
export enum OscalFacetFedrampValuesEnum {
    
    likelihood = "likelihood",
    impact = "impact",
    risk = "risk",
};
/**
* Values from assessment-common set oscal-facet-cve-values.
*/
export enum OscalFacetCveValuesEnum {
    
    cve_id = "cve-id",
};
/**
* Values from assessment-common set oscal-facet-cvss2-name-values.
*/
export enum OscalFacetCvss2NameValuesEnum {
    
    access_vector = "access-vector",
    access_complexity = "access-complexity",
    authentication = "authentication",
    confidentiality_impact = "confidentiality-impact",
    integrity_impact = "integrity-impact",
    availability_impact = "availability-impact",
    exploitability = "exploitability",
    remediation_level = "remediation-level",
    report_confidence = "report-confidence",
    collateral_damage_potential = "collateral-damage-potential",
    target_distribution = "target-distribution",
    confidentiality_requirement = "confidentiality-requirement",
    integrity_requirement = "integrity-requirement",
    availability_requirement = "availability-requirement",
};
/**
* Values from assessment-common set oscal-facet-cvss2-access-vector-values.
*/
export enum OscalFacetCvss2AccessVectorValuesEnum {
    
    local = "local",
    adjacent_network = "adjacent-network",
    network = "network",
};
/**
* Values from assessment-common set oscal-facet-cvss2-access-complexity-values.
*/
export enum OscalFacetCvss2AccessComplexityValuesEnum {
    
    high = "high",
    medium = "medium",
    low = "low",
};
/**
* Values from assessment-common set oscal-facet-cvss2-authentication-values.
*/
export enum OscalFacetCvss2AuthenticationValuesEnum {
    
    multiple = "multiple",
    single = "single",
    none = "none",
};
/**
* Values from assessment-common set oscal-facet-cvss2-confidentiality-impact-values.
*/
export enum OscalFacetCvss2ConfidentialityImpactValuesEnum {
    
    none = "none",
    partial = "partial",
    complete = "complete",
};
/**
* Values from assessment-common set oscal-facet-cvss2-exploitability-values.
*/
export enum OscalFacetCvss2ExploitabilityValuesEnum {
    
    unproven = "unproven",
    proof_of_concept = "proof-of-concept",
    functional = "functional",
    high = "high",
    not_defined = "not-defined",
};
/**
* Values from assessment-common set oscal-facet-cvss2-remediation-level-values.
*/
export enum OscalFacetCvss2RemediationLevelValuesEnum {
    
    official_fix = "official-fix",
    temporary_fix = "temporary-fix",
    workaround = "workaround",
    unavailable = "unavailable",
    not_defined = "not-defined",
};
/**
* Values from assessment-common set oscal-facet-cvss2-report-confidence-values.
*/
export enum OscalFacetCvss2ReportConfidenceValuesEnum {
    
    unconfirmed = "unconfirmed",
    uncorroborated = "uncorroborated",
    confirmed = "confirmed",
    not_defined = "not-defined",
};
/**
* Values from assessment-common set oscal-facet-cvss2-collateral-damage-potential-values.
*/
export enum OscalFacetCvss2CollateralDamagePotentialValuesEnum {
    
    none = "none",
    low = "low",
    low_medium = "low-medium",
    medium_high = "medium-high",
    high = "high",
    not_defined = "not-defined",
};
/**
* Values from assessment-common set oscal-facet-cvss2-cia-requirement-values.
*/
export enum OscalFacetCvss2CiaRequirementValuesEnum {
    
    none = "none",
    low = "low",
    medium = "medium",
    high = "high",
    not_defined = "not-defined",
};
/**
* Values from assessment-common set oscal-facet-cvss3-name-values.
*/
export enum OscalFacetCvss3NameValuesEnum {
    
    attack_vector = "attack-vector",
    access_complexity = "access-complexity",
    privileges_required = "privileges-required",
    user_interaction = "user-interaction",
    scope = "scope",
    confidentiality_impact = "confidentiality-impact",
    integrity_impact = "integrity-impact",
    availability_impact = "availability-impact",
    exploit_code_maturity = "exploit-code-maturity",
    remediation_level = "remediation-level",
    report_confidence = "report-confidence",
    modified_attack_vector = "modified-attack-vector",
    modified_attack_complexity = "modified-attack-complexity",
    modified_privileges_required = "modified-privileges-required",
    modified_user_interaction = "modified-user-interaction",
    modified_scope = "modified-scope",
    modified_confidentiality = "modified-confidentiality",
    modified_integrity = "modified-integrity",
    modified_availability = "modified-availability",
    confidentiality_requirement = "confidentiality-requirement",
    integrity_requirement = "integrity-requirement",
    availability_requirement = "availability-requirement",
};
/**
* Values from assessment-common set oscal-facet-cvss3-access-vector-values.
*/
export enum OscalFacetCvss3AccessVectorValuesEnum {
    
    network = "network",
    adjacent = "adjacent",
    local = "local",
    physical = "physical",
};
/**
* Values from assessment-common set oscal-facet-cvss3-access-complexity-values.
*/
export enum OscalFacetCvss3AccessComplexityValuesEnum {
    
    high = "high",
    low = "low",
};
/**
* Values from assessment-common set oscal-facet-cvss3-cia-impact-values.
*/
export enum OscalFacetCvss3CiaImpactValuesEnum {
    
    none = "none",
    low = "low",
    high = "high",
};
/**
* Values from assessment-common set oscal-facet-cvss3-user-interaction.
*/
export enum OscalFacetCvss3UserInteractionEnum {
    
    none = "none",
    required = "required",
};
/**
* Values from assessment-common set oscal-facet-cvss3-scope.
*/
export enum OscalFacetCvss3ScopeEnum {
    
    unchanged = "unchanged",
    changed = "changed",
};
/**
* Values from assessment-common set oscal-facet-cvss3-exploit-code-maturity-values.
*/
export enum OscalFacetCvss3ExploitCodeMaturityValuesEnum {
    
    not_defined = "not-defined",
    unproven = "unproven",
    proof_of_concept = "proof-of-concept",
    functional = "functional",
    high = "high",
};
/**
* Values from assessment-common set oscal-facet-cvss3-remediation-level.
*/
export enum OscalFacetCvss3RemediationLevelEnum {
    
    not_defined = "not-defined",
    official_fix = "official-fix",
    temporary_fix = "temporary-fix",
    workaround = "workaround",
    unavailable = "unavailable",
};
/**
* Values from assessment-common set oscal-facet-cvss3-report-confidence-values.
*/
export enum OscalFacetCvss3ReportConfidenceValuesEnum {
    
    not_defined = "not-defined",
    unknown = "unknown",
    reasonable = "reasonable",
    confirmed = "confirmed",
};
/**
* Values from assessment-common set oscal-facet-cvss3-cia-requirement-values.
*/
export enum OscalFacetCvss3CiaRequirementValuesEnum {
    
    not_defined = "not-defined",
    low = "low",
    medium = "medium",
    high = "high",
};
/**
* Values from assessment-common set oscal-facet-cvss3-modified-attack-vector-values.
*/
export enum OscalFacetCvss3ModifiedAttackVectorValuesEnum {
    
    not_defined = "not-defined",
    network = "network",
    adjacent = "adjacent",
    local = "local",
    physical = "physical",
};
/**
* Values from assessment-common set oscal-facet-cvss3-modified-attack-complexity-values.
*/
export enum OscalFacetCvss3ModifiedAttackComplexityValuesEnum {
    
    not_defined = "not-defined",
    high = "high",
    low = "low",
};
/**
* Values from assessment-common set oscal-facet-cvss3-modified-cia-values.
*/
export enum OscalFacetCvss3ModifiedCiaValuesEnum {
    
    not_defined = "not-defined",
    none = "none",
    low = "low",
    high = "high",
};
/**
* Values from assessment-common set oscal-facet-cvss3-modified-user-interaction-values.
*/
export enum OscalFacetCvss3ModifiedUserInteractionValuesEnum {
    
    not_defined = "not-defined",
    none = "none",
    required = "required",
};
/**
* Values from assessment-common set oscal-facet-cvss3-modified-scope-values.
*/
export enum OscalFacetCvss3ModifiedScopeValuesEnum {
    
    not_defined = "not-defined",
    unchanged = "unchanged",
    changed = "changed",
};
/**
* Values from assessment-common set oscal-cvss-v4.0-vectors.
*/
export enum OscalCvssV40VectorsEnum {
    
    av = "av",
    ac = "ac",
    at = "at",
    pr = "pr",
    ui = "ui",
    vc = "vc",
    vi = "vi",
    va = "va",
    sc = "sc",
    si = "si",
    sa = "sa",
    s = "s",
    au = "au",
    r = "r",
    v = "v",
    re = "re",
    u = "u",
    mav = "mav",
    mac = "mac",
    mat = "mat",
    mpr = "mpr",
    mui = "mui",
    mvc = "mvc",
    mvi = "mvi",
    mva = "mva",
    msc = "msc",
    msi = "msi",
    msa = "msa",
    cr = "cr",
    ir = "ir",
    ar = "ar",
    e = "e",
};
/**
* Values from assessment-common set oscal-cvss-v4.0-av-values.
*/
export enum OscalCvssV40AvValuesEnum {
    
    n = "n",
    a = "a",
    l = "l",
    p = "p",
};
/**
* Values from assessment-common set oscal-cvss-v4.0-ac-values.
*/
export enum OscalCvssV40AcValuesEnum {
    
    h = "h",
    l = "l",
};
/**
* Values from assessment-common set oscal-cvss-v4.0-at-values.
*/
export enum OscalCvssV40AtValuesEnum {
    
    n = "n",
    p = "p",
};
/**
* Values from assessment-common set oscal-cvss-v4.0-pr-cia-values.
*/
export enum OscalCvssV40PrCiaValuesEnum {
    
    n = "n",
    l = "l",
    h = "h",
};
/**
* Values from assessment-common set oscal-cvss-v4.0-ui-values.
*/
export enum OscalCvssV40UiValuesEnum {
    
    n = "n",
    p = "p",
    a = "a",
};
/**
* Values from assessment-common set oscal-cvss-v4.0-s-values.
*/
export enum OscalCvssV40SValuesEnum {
    
    x = "x",
    n = "n",
    p = "p",
};
/**
* Values from assessment-common set oscal-cvss-v4.0-au-values.
*/
export enum OscalCvssV40AuValuesEnum {
    
    x = "x",
    n = "n",
    y = "y",
};
/**
* Values from assessment-common set oscal-cvss-v4.0-r-values.
*/
export enum OscalCvssV40RValuesEnum {
    
    x = "x",
    a = "a",
    u = "u",
    i = "i",
};
/**
* Values from assessment-common set oscal-cvss-v4.0-v-values.
*/
export enum OscalCvssV40VValuesEnum {
    
    x = "x",
    a = "a",
    u = "u",
    i = "i",
};
/**
* Values from assessment-common set oscal-cvss-v4.0-re-values.
*/
export enum OscalCvssV40ReValuesEnum {
    
    x = "x",
    l = "l",
    m = "m",
    h = "h",
};
/**
* Values from assessment-common set oscal-cvss-v4.0-u-values.
*/
export enum OscalCvssV40UValuesEnum {
    
    x = "x",
    clear = "clear",
    green = "green",
    amber = "amber",
    red = "red",
};
/**
* Values from assessment-common set oscal-cvss-v4.0-mav-values.
*/
export enum OscalCvssV40MavValuesEnum {
    
    x = "x",
    n = "n",
    a = "a",
    l = "l",
    p = "p",
};
/**
* Values from assessment-common set oscal-cvss-v4.0-mac-values.
*/
export enum OscalCvssV40MacValuesEnum {
    
    x = "x",
    h = "h",
    l = "l",
};
/**
* Values from assessment-common set oscal-cvss-v4.0-mat-values.
*/
export enum OscalCvssV40MatValuesEnum {
    
    x = "x",
    n = "n",
    p = "p",
};
/**
* Values from assessment-common set oscal-cvss-v4.0-mpr-mvs-cia-values.
*/
export enum OscalCvssV40MprMvsCiaValuesEnum {
    
    x = "x",
    n = "n",
    l = "l",
    h = "h",
};
/**
* Values from assessment-common set oscal-cvss-v4.0-mui-values.
*/
export enum OscalCvssV40MuiValuesEnum {
    
    x = "x",
    n = "n",
    p = "p",
    a = "a",
};
/**
* Values from assessment-common set oscal-cvss-v4.0-msc-values.
*/
export enum OscalCvssV40MscValuesEnum {
    
    x = "x",
    n = "n",
    l = "l",
    h = "h",
};
/**
* Values from assessment-common set oscal-cvss-v4.0-msi-msa-cia-values.
*/
export enum OscalCvssV40MsiMsaCiaValuesEnum {
    
    x = "x",
    n = "n",
    l = "l",
    h = "h",
    s = "s",
};
/**
* Values from assessment-common set oscal-cvss-v4.0-env-cia-values.
*/
export enum OscalCvssV40EnvCiaValuesEnum {
    
    x = "x",
    l = "l",
    m = "m",
    h = "h",
};
/**
* Values from assessment-common set oscal-cvss-v4.0-e-values.
*/
export enum OscalCvssV40EValuesEnum {
    
    x = "x",
    a = "a",
    p = "p",
    u = "u",
};
/**
* Values from assessment-common set oscal-response-prop-type-value.
*/
export enum OscalResponsePropTypeValueEnum {
    
    avoid = "avoid",
    mitigate = "mitigate",
    transfer = "transfer",
    accept = "accept",
    share = "share",
    contingency = "contingency",
    none = "none",
};
/**
* Curated response lifecycle values. Other values are permitted (OSCAL allow-other="yes").

*/
export enum ResponseLifecycleEnum {
    
    recommendation = "recommendation",
    planned = "planned",
    completed = "completed",
};
/**
* Allowable operational states for an OSCAL-described system.
*/
export enum SystemOperatingStatusEnum {
    
    /** The system is currently operating in production. */
    operational = "operational",
    /** The system is being designed, developed, or implemented. */
    under_development = "under-development",
    /** The system is undergoing a major change, development, or transition. */
    under_major_modification = "under-major-modification",
    /** The system is no longer operational. */
    disposition = "disposition",
    /** Some other state. */
    other = "other",
};
/**
* OSCAL-defined property names used within system characteristics.
*/
export enum SystemCharacteristicsPropNameEnum {
    
    identity_assurance_level = "identity-assurance-level",
    authenticator_assurance_level = "authenticator-assurance-level",
    federation_assurance_level = "federation-assurance-level",
    cloud_deployment_model = "cloud-deployment-model",
    cloud_service_model = "cloud-service-model",
};
/**
* NIST SP 800-63 assurance level values.
*/
export enum AssuranceLevelValueEnum {
    
    number_1 = "1",
    number_2 = "2",
    number_3 = "3",
};
/**
* Cloud deployment model values used by OSCAL SSP properties.
*/
export enum CloudDeploymentModelEnum {
    
    public_cloud = "public-cloud",
    private_cloud = "private-cloud",
    community_cloud = "community-cloud",
    hybrid_cloud = "hybrid-cloud",
    government_only_cloud = "government-only-cloud",
    other = "other",
};
/**
* Cloud service model values used by OSCAL SSP properties.
*/
export enum CloudServiceModelEnum {
    
    saas = "saas",
    paas = "paas",
    iaas = "iaas",
    other = "other",
};
/**
* Curated role identifiers for system characteristics responsible parties. Other values are permitted (OSCAL allow-other="yes").
*/
export enum SystemCharacteristicsResponsibleRoleIdEnum {
    
    authorizing_official = "authorizing-official",
    authorizing_official_poc = "authorizing-official-poc",
    system_owner = "system-owner",
    system_poc_management = "system-poc-management",
    system_poc_technical = "system-poc-technical",
    system_poc_other = "system-poc-other",
    information_system_security_officer = "information-system-security-officer",
    privacy_poc = "privacy-poc",
};
/**
* Curated information type categorization system URIs. Other values are permitted (OSCAL allow-other="yes").
*/
export enum InformationTypeCategorizationSystemEnum {
    
    httpCOLONSOLIDUSSOLIDUSdoiFULL_STOPorgSOLIDUS10FULL_STOP6028SOLIDUSNISTFULL_STOPSPFULL_STOP800_60v2r1 = "http://doi.org/10.6028/NIST.SP.800-60v2r1",
};
/**
* OSCAL-defined property names used within system information.
*/
export enum SystemInformationPropNameEnum {
    
    privacy_designation = "privacy-designation",
};
/**
* Privacy designation property values.
*/
export enum PrivacyDesignationEnum {
    
    yes = "yes",
    no = "no",
};
/**
* Curated relation values for links in system information. Other values are permitted (OSCAL allow-other="yes").
*/
export enum SystemInformationLinkRelEnum {
    
    privacy_impact_assessment = "privacy-impact-assessment",
};
/**
* Curated FIPS 199 impact level values. Other values are permitted (OSCAL allow-other="yes").
*/
export enum Fips199ImpactLevelEnum {
    
    fips_199_low = "fips-199-low",
    fips_199_moderate = "fips-199-moderate",
    fips_199_high = "fips-199-high",
};
/**
* Curated relation values for links in diagram objects. Other values are permitted (OSCAL allow-other="yes").
*/
export enum DiagramLinkRelEnum {
    
    diagram = "diagram",
};
/**
* Curated relation values for links in leveraged authorization objects. Other values are permitted (OSCAL allow-other="yes").
*/
export enum LeveragedAuthorizationLinkRelEnum {
    
    system_security_plan = "system-security-plan",
};
/**
* Values for allows-authenticated-scan property in SSP component and inventory contexts.
*/
export enum AllowsAuthenticatedScanEnum {
    
    yes = "yes",
    no = "no",
};
/**
* OSCAL-defined property names used in implementation statements.
*/
export enum ControlOriginationPropNameEnum {
    
    control_origination = "control-origination",
};
/**
* Control origination values.
*/
export enum ControlOriginationValueEnum {
    
    organization = "organization",
    system_specific = "system-specific",
    customer_configured = "customer-configured",
    customer_provided = "customer-provided",
    inherited = "inherited",
};
/**
* Curated role identifiers for implemented requirement and statement responsible roles. Other values are permitted (OSCAL allow-other="yes").
*/
export enum ImplementedRequirementResponsibleRoleIdEnum {
    
    asset_owner = "asset-owner",
    asset_administrator = "asset-administrator",
    security_operations = "security-operations",
    network_operations = "network-operations",
    incident_response = "incident-response",
    help_desk = "help-desk",
    configuration_management = "configuration-management",
};
/**
* Curated relation values for links in by-component objects. Other values are permitted (OSCAL allow-other="yes").
*/
export enum ByComponentLinkRelEnum {
    
    imported_from = "imported-from",
    provided_by = "provided-by",
};
/**
* Curated role identifiers for by-component responsible roles. Other values are permitted (OSCAL allow-other="yes").
*/
export enum ByComponentResponsibleRoleIdEnum {
    
    asset_owner = "asset-owner",
    asset_administrator = "asset-administrator",
    security_operations = "security-operations",
    network_operations = "network-operations",
    incident_response = "incident-response",
    help_desk = "help-desk",
    configuration_management = "configuration-management",
    maintainer = "maintainer",
    provider = "provider",
};

export enum MappingMethodEnum {
    
    human = "human",
    automation = "automation",
    hybrid = "hybrid",
};

export enum MatchingRationaleEnum {
    
    syntactic = "syntactic",
    semantic = "semantic",
    functional = "functional",
};

export enum MappingStatusEnum {
    
    complete = "complete",
    not_complete = "not-complete",
    draft = "draft",
    deprecated = "deprecated",
    superseded = "superseded",
};

export enum MappingSubjectTypeEnum {
    
    control = "control",
    statement = "statement",
};

export enum QualifierSubjectEnum {
    
    source = "source",
    target = "target",
    both = "both",
};

export enum QualifierPredicateEnum {
    
    has_requirement = "has-requirement",
    has_incompatibility = "has-incompatibility",
};

export enum QualifierCategoryEnum {
    
    restricted = "restricted",
    addressable = "addressable",
    blocked = "blocked",
};
/**
* Relationship values used for mapping entries in the OSCAL namespace.
*/
export enum RelationshipEnum {
    
    equivalent_to = "equivalent-to",
    equal_to = "equal-to",
    subset_of = "subset-of",
    superset_of = "superset-of",
    intersects_with = "intersects-with",
    no_relationship = "no-relationship",
};
/**
* Curated mapped resource type values. Other values are permitted (OSCAL allow-other="yes").
*/
export enum MappingResourceTypeEnum {
    
    catalog = "catalog",
    profile = "profile",
};
/**
* Curated confidence category values for OSCAL mappings. Other values are permitted (OSCAL allow-other="yes").
*/
export enum ConfidenceCategoryEnum {
    
    unspecified = "unspecified",
    high = "high",
    medium = "medium",
    low = "low",
};
/**
* Curated coverage generation method values. Other values are permitted (OSCAL allow-other="yes").
*/
export enum CoverageGenerationMethodEnum {
    
    arbitrary = "arbitrary",
};


/**
 * Mixin providing the props and links slots that are common to many OSCAL objects.
 */
export interface HasPropsAndLinks {
    /** A list of properties. */
    props?: Property[],
    /** A list of links. */
    links?: Link[],
}


/**
 * Mixin providing props, links, and remarks slots common to most OSCAL objects. Extends HasPropsAndLinks.
 */
export interface OscalCommon extends HasPropsAndLinks {
    /** Additional commentary about the containing object. */
    remarks?: string,
}


/**
 * Mixin providing the responsible-roles slot for objects that carry role assignments.
 */
export interface HasResponsibleRoles {
    /** Responsible role assignments. */
    responsible_roles?: ResponsibleRole[],
}


/**
 * Mixin providing the responsible-parties slot for objects that carry party assignments.
 */
export interface HasResponsibleParties {
    /** Responsible party assignments. */
    responsible_parties?: ResponsibleParty[],
}


/**
 * A root wrapper for an OSCAL document, which may be of any OSCAL document type (e.g. Catalog, Profile, Assessment Plan, SSP).
 */
export interface OscalDocument {
}


/**
 * Root wrapper for an OSCAL Catalog document.
 */
export interface CatalogDocument extends OscalDocument {
    /** Root catalog document. */
    catalog: Catalog,
}


/**
 * A structured, organized collection of control information.
 */
export interface Catalog {
    /** Provides a globally unique means to identify a given catalog instance. */
    uuid: string,
    /** Provides information about the containing document, and defines concepts shared across the document. */
    metadata: Metadata,
    /** A collection of resources that may be referenced from within the OSCAL document instance. */
    back_matter?: BackMatter,
    /** Parameters providing a mechanism for the dynamic assignment of value(s) in a control. */
    params?: Parameter[],
    /** A collection of controls. */
    controls?: Control[],
    /** A collection of control groups. */
    groups?: Group[],
}


/**
 * A group of controls, or of groups of controls.
 */
export interface Group extends HasPropsAndLinks {
    /** Identifies the group for the purpose of cross-linking within the defining instance or from other instances that reference the catalog. */
    id?: string,
    /** A textual label that provides a sub-type or characterization of the group. */
    _class?: string,
    /** A name given to the group, which may be used by a tool for display and navigation. */
    title: string,
    /** Parameters providing a mechanism for the dynamic assignment of value(s) in a control. */
    params?: Parameter[],
    /** A collection of parts. */
    parts?: Part[],
    /** A collection of control groups. */
    groups?: Group[],
    /** A collection of controls. */
    controls?: Control[],
}


/**
 * A structured object representing a requirement or guideline, which when implemented will reduce an aspect of risk related to an information system and its information.
 */
export interface Control extends HasPropsAndLinks {
    /** Identifies a control such that it can be referenced in the defining catalog and other OSCAL instances (e.g., profiles). */
    id: string,
    /** A textual label that provides a sub-type or characterization of the control. */
    _class?: string,
    /** A name given to the control, which may be used by a tool for display and navigation. */
    title: string,
    /** Parameters providing a mechanism for the dynamic assignment of value(s) in a control. */
    params?: Parameter[],
    /** A collection of parts. */
    parts?: Part[],
    /** A collection of controls. */
    controls?: Control[],
}


/**
 * Provides information about the containing document, and defines concepts shared across the document.
 */
export interface Metadata extends OscalCommon, HasResponsibleParties {
    /** A name given to the document. */
    title: string,
    /** The date and time the document was last made available. */
    published?: string,
    /** The date and time the document was last stored for later retrieval. */
    last_modified: string,
    /** Used to distinguish a specific revision of an OSCAL document. */
    version: string,
    /** The OSCAL model version the document was authored against. */
    oscal_version: string,
    /** Document identifiers qualified by an identifier scheme. */
    document_ids?: DocumentId[],
    /** An entry in a sequential list of revisions to the containing document, expected to be in reverse chronological order (i.e. latest first). */
    revisions?: Revision[],
    /** Defines a function, which might be assigned to a party in a specific situation. */
    roles?: Role[],
    /** A physical point of presence, which may be associated with people, organizations, or other concepts within the current or linked OSCAL document. */
    locations?: Location[],
    /** An organization or person, which may be associated with roles or other concepts within the current or linked OSCAL document. */
    parties?: Party[],
    /** An action applied by a role within a given party to the content. */
    actions?: Action[],
}


/**
 * An entry in a sequential list of revisions to the containing document.
 */
export interface Revision extends OscalCommon {
    /** A human-readable name or title. */
    title?: string,
    /** The date and time the document was last made available. */
    published?: string,
    /** The date and time the document was last modified. */
    last_modified?: string,
    /** Used to distinguish a specific revision of an OSCAL document from other previous and future versions. */
    version: string,
    /** The OSCAL model version the document was authored against and will conform to as valid. */
    oscal_version?: string,
}


/**
 * A document identifier qualified by an identifier scheme.
 */
export interface DocumentId {
    /** Qualifies the kind of identifier using a URI. */
    scheme?: string,
    /** A document identifier value. */
    identifier: string,
}


/**
 * Defines a function, which might be assigned to a party in a specific situation.
 */
export interface Role extends OscalCommon {
    /** A unique identifier for the role. */
    id: string,
    /** A human-readable name or title. */
    title: string,
    /** A short common name, abbreviation, or acronym. */
    short_name?: string,
    /** A human-readable description. */
    description?: string,
}


/**
 * A physical point of presence, which may be associated with people, organizations, or other concepts within the current or linked OSCAL document.
 */
export interface Location extends OscalCommon {
    /** A machine-oriented, globally unique identifier with a cross-instance scope. */
    uuid: string,
    /** A human-readable name or title. */
    title?: string,
    /** Email addresses associated with the containing object. */
    email_addresses?: string[],
    /** Telephone numbers associated with the containing object. */
    telephone_numbers?: TelephoneNumber[],
    /** A postal address for the location. */
    address?: Address,
    /** The uniform resource locator (URL) for a web site or other resource associated with the location. */
    urls?: string[],
}


/**
 * An organization or person, which may be associated with roles or other concepts within the current or linked OSCAL document.
 */
export interface Party extends OscalCommon {
    /** A machine-oriented, globally unique identifier with a cross-instance scope. */
    uuid: string,
    /** A category describing the kind of party the object describes. */
    type: string,
    /** The full name of the party. */
    name?: string,
    /** A short common name, abbreviation, or acronym. */
    short_name?: string,
    /** Email addresses associated with the containing object. */
    email_addresses?: string[],
    /** Telephone numbers associated with the containing object. */
    telephone_numbers?: TelephoneNumber[],
    /** An identifier for a person or organization using a designated scheme, e.g. an Open Researcher and Contributor ID (ORCID). */
    external_ids?: MetadataPartyExternalId[],
    /** Postal addresses associated with the containing object. */
    addresses?: Address[],
    /** Reference to a location by UUID. */
    location_uuids?: string[],
    /** A reference to another party by UUID, typically an organization, that this subject is associated with. */
    member_of_organizations?: string[],
}


/**
 * An identifier for a person or organization using a designated scheme, e.g. an Open Researcher and Contributor ID (ORCID).
 */
export interface PartyExternalId {
    /** Indicates the type of external identifier. */
    scheme: string,
    /** A unique human-oriented identifier within a particular context. */
    id: string,
}


/**
 * A reference to a set of persons and/or organizations that have responsibility for performing the referenced role in the context of the containing object.
 */
export interface ResponsibleParty extends OscalCommon {
    /** A reference to a role performed by a party. */
    role_id: string,
    /** References to party UUIDs. */
    party_uuids: string[],
}


/**
 * A reference to a role with responsibility for performing a function relative to the containing object, optionally associated with a set of persons and/or organizations that perform that role.
 */
export interface ResponsibleRole extends OscalCommon {
    /** A human-oriented identifier reference to a role performed. */
    role_id: string,
    /** References to party UUIDs. */
    party_uuids?: string[],
}


/**
 * An action applied by a role within a given party to the content.
 */
export interface Action extends OscalCommon, HasResponsibleParties {
    /** A unique identifier that can be used to reference this defined action elsewhere in an OSCAL document. */
    uuid: string,
    /** The type of action documented by the assembly, such as an approval. */
    type: string,
    /** The date and time when the action occurred. */
    date?: string,
    /** Specifies the action type system used. */
    system: string,
}


/**
 * A telephone service number as defined by ITU-T E.164.
 */
export interface TelephoneNumber {
    /** Indicates the type of phone number. Recommended values: home, office, mobile. Other values are permitted (OSCAL allow-other="yes"). */
    type?: string,
    /** A telephone number value. */
    number: string,
}


/**
 * A postal address for the location.
 */
export interface Address {
    /** Indicates the type of address. Recommended values: home, work. Other values are permitted (OSCAL allow-other="yes"). */
    type?: string,
    /** A single line of an address. */
    addr_lines?: string[],
    /** City, town or geographical region for the mailing address. */
    city?: string,
    /** State, province or analogous geographical region for a mailing address. */
    state?: string,
    /** Postal or ZIP code for mailing address. */
    postal_code?: string,
    /** The ISO 3166-1 alpha-2 country code for the mailing address. */
    country?: string,
}


/**
 * A representation of a cryptographic digest generated over a resource using a specified hash algorithm.
 */
export interface Hash {
    /** The value associated with the containing object. */
    value: string,
    /** The digest method by which a hash is derived. Recommended values are in HashAlgorithmEnum; other values are permitted (OSCAL allow-other="yes"). */
    algorithm: string,
}


/**
 * An attribute, characteristic, or quality of the containing object expressed as a namespace qualified name/value pair.
 */
export interface Property {
    /** A textual label, within a namespace, that identifies a specific attribute, characteristic, or quality of the property's containing object. */
    name: string,
    /** A unique identifier for a property. */
    uuid?: string,
    /** A namespace qualifying the property's name. This allows different organizations to associate distinct semantics with the same name. */
    ns?: string,
    /** Indicates the value of the attribute, characteristic, or quality. */
    value: string,
    /** A textual label that provides a sub-type or characterization of the property's name. */
    _class?: string,
    /** Additional commentary about the containing object. */
    remarks?: string,
    /** An identifier for relating distinct sets of properties. */
    group?: string,
}


/**
 * Metadata-scoped OSCAL property.
 */
export interface MetadataProperty extends Property {
}


/**
 * Revision-scoped OSCAL property.
 */
export interface RevisionProperty extends Property {
}


/**
 * Location-scoped OSCAL property.
 */
export interface LocationProperty extends Property {
}


/**
 * Party-scoped OSCAL property.
 */
export interface PartyProperty extends Property {
}


/**
 * Back-matter resource-scoped OSCAL property.
 */
export interface ResourceProperty extends Property {
}


/**
 * Control-common part-scoped OSCAL property.
 */
export interface PartProperty extends Property {
}


/**
 * Control-common parameter-scoped OSCAL property.
 */
export interface ParameterProperty extends Property {
}


/**
 * Metadata-scoped external identifier.
 */
export interface MetadataPartyExternalId extends PartyExternalId {
}


/**
 * A reference to a local or remote resource, that has a specific relation to the containing object.
 */
export interface Link {
    /** A resolvable URL reference to a resource. */
    href: string,
    /** Describes the type of relationship provided by the link's hypertext reference. This can be an indicator of the link's purpose. */
    rel?: string,
    /** In case where the href points to a back-matter/resource, this value will indicate the URI fragment to append to any rlink associated with the resource. This value MUST be URI encoded. */
    resource_fragment?: string,
    /** A label that indicates the nature of a resource, as a data serialization or format. */
    media_type?: string,
    /** A textual label to associate with the containing object. */
    text?: string,
}


/**
 * A collection of resources that may be referenced from within the OSCAL document instance.
 */
export interface BackMatter {
    /** A resource associated with content in the containing document instance. A resource may be directly included in the document using base64 encoding or may point to one or more equivalent internet resources. */
    resources?: Resource[],
}


/**
 * A resource associated with content in the containing document instance. A resource may be directly included in the document using base64 encoding or may point to one or more equivalent internet resources.
 */
export interface Resource {
    /** A unique identifier for a resource. */
    uuid: string,
    /** An optional name given to the resource, which may be used by a tool for display and navigation. */
    title?: string,
    /** An optional short summary of the resource used to indicate the purpose of the resource. */
    description?: string,
    /** A list of properties. */
    props?: ResourceProperty[],
    /** Document identifiers qualified by an identifier scheme. */
    document_ids?: DocumentId[],
    /** Additional commentary about the containing object. */
    remarks?: string,
    /** An optional citation consisting of end note text using structured markup. */
    citation?: Citation,
    /** A URL-based pointer to an external resource with an optional hash for verification and change detection. */
    rlinks?: ResourceLink[],
    /** A resource encoded using the Base64 alphabet defined by RFC 2045. */
    base64?: Base64Resource,
}


/**
 * An optional citation consisting of end note text using structured markup.
 */
export interface Citation extends HasPropsAndLinks {
    /** A line of citation text. */
    text: string,
}


/**
 * A URL-based pointer to an external resource with an optional hash for verification and change detection.
 */
export interface ResourceLink {
    /** A resolvable URL pointing to the referenced resource. */
    href: string,
    /** A label that indicates the nature of a resource, as a data serialization or format. */
    media_type?: string,
    /** A representation of a cryptographic digest generated over a resource using a specified hash algorithm. */
    hashes?: Hash[],
}


/**
 * A resource encoded using the Base64 alphabet defined by RFC 2045.
 */
export interface Base64Resource {
    /** A label that indicates the nature of a resource, as a data serialization or format. */
    media_type?: string,
    /** The value associated with the containing object. */
    value: string,
    /** Name of the file before it was encoded as Base64 to be embedded in a resource. */
    filename?: string,
}


/**
 * An annotated, markup-based textual element of a control's or catalog group's definition, or a child of another part.
 */
export interface Part extends HasPropsAndLinks {
    /** A unique identifier for the part. */
    id?: string,
    /** A textual label that uniquely identifies the part's semantic type, which exists in a value space qualified by the ns. */
    name: string,
    /** An optional namespace qualifying the part's name. This allows different organizations to associate distinct semantics with the same name. */
    ns?: string,
    /** An optional textual providing a sub-type or characterization of the part's name, or a category to which the part belongs. */
    _class?: string,
    /** An optional name given to the part, which may be used by a tool for display and navigation. */
    title?: string,
    /** Permits multiple paragraphs, lists, tables etc. */
    prose?: string,
    /** A collection of parts. */
    parts?: Part[],
}


/**
 * Parameters provide a mechanism for the dynamic assignment of value(s) in a control.
 */
export interface Parameter extends OscalCommon {
    /** A unique identifier for the parameter. */
    id: string,
    /** A textual label that provides a characterization of the type, purpose, use or scope of the parameter. */
    _class?: string,
    /** (deprecated) Another parameter invoking this one. This construct has been deprecated and should not be used. */
    depends_on?: string,
    /** A short, placeholder name for the parameter, which can be used as a substitute for a value if no value is assigned. */
    label?: string,
    /** Describes the purpose and use of a parameter. */
    usage?: string,
    /** A formal or informal expression of a constraint or test. */
    constraints?: ParameterConstraint[],
    /** A prose statement that provides a recommendation for the use of a parameter. */
    guidelines?: ParameterGuideline[],
    /** A parameter value or set of values. */
    values?: string[],
    /** Presenting a choice among alternatives. */
    select?: ParameterSelection,
}


/**
 * A formal or informal expression of a constraint or test.
 */
export interface ParameterConstraint {
    /** A textual summary of the constraint to be applied. */
    description?: string,
    /** A test expression which is expected to be evaluated by a tool. */
    tests?: ConstraintTest[],
}


/**
 * A test expression which is expected to be evaluated by a tool.
 */
export interface ConstraintTest {
    /** Additional commentary about the containing object. */
    remarks?: string,
    /** A formal (executable) expression of a constraint. */
    expression: string,
}


/**
 * A prose statement that provides a recommendation for the use of a parameter.
 */
export interface ParameterGuideline {
    /** Prose permits multiple paragraphs, lists, tables etc. */
    prose: string,
}


/**
 * Presenting a choice among alternatives.
 */
export interface ParameterSelection {
    /** Describes the number of selections that must occur. Without this setting, only one value should be assumed to be permitted. */
    how_many?: string,
    /** A value selection among several such options. */
    choice?: string[],
}


/**
 * Include all controls from the imported catalog or profile resources.
 */
export interface IncludeAll {
}


/**
 * Selecting a set of controls by matching their IDs with a wildcard pattern.
 */
export interface ControlMatching {
    /** Additional commentary about the containing object. */
    remarks?: string,
    /** A glob expression matching the IDs of one or more controls to be selected. */
    pattern?: string,
}


/**
 * Select a control or controls from an imported control set.
 */
export interface SelectControlById {
    /** When a control is included, whether its child (dependent) controls are also included. */
    with_child_controls?: string,
    /** Selecting a control by its ID given as a literal. */
    with_ids?: string[],
    /** Selecting a set of controls by matching their IDs with a wildcard pattern. */
    matching?: ControlMatching[],
}


/**
 * Root wrapper for an OSCAL Profile document.
 */
export interface ProfileDocument extends OscalDocument {
    /** The root profile object. */
    profile: Profile,
}


/**
 * An OSCAL Profile that designates a set of controls from one or more catalogs or profiles, optionally restructures and modifies them, to describe a basis for a security standard or body of practice.
 */
export interface Profile {
    /** A machine-oriented, globally unique identifier with a cross-instance scope. */
    uuid: string,
    /** Provides information about the containing document, and defines concepts shared across the document. */
    metadata: Metadata,
    /** Designates source catalog or profile resources to be imported into the profile. */
    imports: ProfileImport[],
    /** Structuring directives for how controls are organized after profile resolution. */
    merge?: ProfileMerge,
    /** Set parameters or amend controls in resolution. */
    modify?: ProfileModify,
    /** A collection of resources that may be referenced from within the OSCAL document instance. */
    back_matter?: BackMatter,
}


/**
 * Designates a referenced source catalog or profile that provides a source of control information for use in creating a new overlay or baseline.
 */
export interface ProfileImport {
    /** A resolvable URL reference to a resource. */
    href: string,
    /** Include all selectable objects in the containing OSCAL selection context. */
    include_all?: IncludeAll,
    /** Control-selection entries to include in the containing OSCAL context. The concrete entry class is selected by class-level slot_usage. */
    include_controls?: SelectControlById[],
    /** Control-selection entries to exclude in the containing OSCAL context. The concrete entry class is selected by class-level slot_usage. */
    exclude_controls?: SelectControlById[],
}


/**
 * Provides structuring directives that instruct how controls are organized after profile resolution.
 */
export interface ProfileMerge {
    /** Defines how to resolve duplicate instances of the same control. */
    combine?: CombinationRule,
    /** Directs that controls appear without any grouping structure. */
    flat?: MergeFlat,
    /** When true, retain the original grouping structure as defined in the import source. */
    as_is?: boolean,
    /** Provides an alternate grouping structure that selected controls will be placed in. */
    custom?: MergeCustom,
}


/**
 * Defines how to resolve duplicate instances of the same control (e.g., controls with the same ID) encountered in a profile merge.
 */
export interface CombinationRule {
    /** Method indicator used by the containing OSCAL context. Allowed values are constrained by class-level slot_usage. */
    method?: string,
}


/**
 * Directs that controls appear without any grouping structure after profile resolution.
 */
export interface MergeFlat {
}


/**
 * Provides an alternate grouping structure that selected controls will be placed in after profile resolution.
 */
export interface MergeCustom {
    /** A collection of control groups. */
    groups?: ProfileGroup[],
    /** Specifies which controls to use in the containing context. */
    insert_controls?: InsertControls[],
}


/**
 * A group of (selected) controls or of groups of controls within a profile custom merge structure.
 */
export interface ProfileGroup extends OscalCommon {
    /** A unique human-oriented identifier within a particular context. */
    id?: string,
    /** A textual label that provides a sub-type or characterization. */
    _class?: string,
    /** A human-readable name or title. */
    title: string,
    /** Parameters providing a mechanism for the dynamic assignment of value(s) in a control. */
    params?: Parameter[],
    /** A collection of parts. */
    parts?: Part[],
    /** A collection of control groups. */
    groups?: ProfileGroup[],
    /** Specifies which controls to use in the containing context. */
    insert_controls?: InsertControls[],
}


/**
 * Set parameters or amend controls in resolution.
 */
export interface ProfileModify {
    /** A parameter setting to be propagated to points of insertion. */
    set_parameters?: ParameterSetting[],
    /** Specifies changes to be made to included controls in resolution. */
    alters?: Alteration[],
}


/**
 * A parameter setting to be propagated to points of insertion in a resolved profile.
 */
export interface ParameterSetting extends HasPropsAndLinks {
    /** The identifier for the parameter being set or referenced. */
    param_id: string,
    /** A textual label that provides a sub-type or characterization. */
    _class?: string,
    /** (deprecated) Another parameter invoking this one. This construct has been deprecated and should not be used. */
    depends_on?: string,
    /** A short, placeholder name for the parameter, which can be used as a substitute for a value if no value is assigned. */
    label?: string,
    /** Describes the purpose and use of a parameter. */
    usage?: string,
    /** A formal or informal expression of a constraint or test. */
    constraints?: ParameterConstraint[],
    /** A prose statement that provides a recommendation for the use of a parameter. */
    guidelines?: ParameterGuideline[],
    /** A parameter value or set of values. */
    values?: string[],
    /** Presenting a choice among alternatives. */
    select?: ParameterSelection,
}


/**
 * Specifies changes to be made to an included control when a profile is resolved.
 */
export interface Alteration {
    /** A reference to a control by its identifier. */
    control_id: string,
    /** Specifies objects to be removed from a control in resolution. */
    removes?: Removal[],
    /** Specifies content to be added into a control in resolution. */
    adds?: Addition[],
}


/**
 * Specifies objects to be removed from a control based on aspects of the object that must all match.
 */
export interface Removal {
    /** Identify items to remove by their assigned name. */
    by_name?: string,
    /** Identify items to remove by their class label. */
    by_class?: string,
    /** Identify or target items by their id value. */
    by_id?: string,
    /** Identify items to remove by the item's information object type name. */
    by_item_name?: string,
    /** Identify items to remove by the item's namespace. */
    by_ns?: string,
    /** Additional commentary about the containing object. */
    remarks?: string,
}


/**
 * Specifies content to be added into controls in resolution.
 */
export interface Addition {
    /** Where to add new content relative to the targeted element. */
    position?: string,
    /** Identify or target items by their id value. */
    by_id?: string,
    /** A human-readable name or title. */
    title?: string,
    /** Parameters providing a mechanism for the dynamic assignment of value(s) in a control. */
    params?: Parameter[],
    /** A list of properties. */
    props?: ProfileAlterationProperty[],
    /** A list of links. */
    links?: Link[],
    /** A collection of parts. */
    parts?: Part[],
}


/**
 * OSCAL property entries allowed in profile modify additions.
 */
export interface ProfileAlterationProperty extends Property {
}


/**
 * Specifies which controls to use in the containing context (as part of a group or custom merge structure).
 */
export interface InsertControls {
    /** A designation of how a selection of controls is to be ordered. */
    order?: string,
    /** Include all selectable objects in the containing OSCAL selection context. */
    include_all?: IncludeAll,
    /** Control-selection entries to include in the containing OSCAL context. The concrete entry class is selected by class-level slot_usage. */
    include_controls?: SelectControlById[],
    /** Control-selection entries to exclude in the containing OSCAL context. The concrete entry class is selected by class-level slot_usage. */
    exclude_controls?: SelectControlById[],
}


/**
 * Root wrapper for an OSCAL Assessment Plan document.
 */
export interface AssessmentPlanDocument extends OscalDocument {
    /** The root assessment plan object. */
    assessment_plan: AssessmentPlan,
}


/**
 * An assessment plan, such as those provided by a FedRAMP assessor.
 */
export interface AssessmentPlan {
    /** Assessment Plan Universally Unique Identifier. */
    uuid: string,
    /** Provides information about the containing document, and defines concepts shared across the document. */
    metadata: Metadata,
    /** Used to import information about the system from an SSP. */
    import_ssp: ImportSSP,
    /** Used to define data objects that do not appear in the referenced SSP. */
    local_definitions?: LocalDefinitions,
    /** Terms and conditions under which an assessment can be performed. */
    terms_and_conditions?: TermsAndConditions,
    /** Identifies system elements being assessed. */
    assessment_subjects?: AssessmentSubject[],
    /** Identifies the assets used to perform this assessment. */
    assessment_assets?: AssessmentAssets,
    /** Identifies the controls being assessed and their control objectives. */
    reviewed_controls: ReviewedControls,
    /** A collection of tasks. */
    tasks?: Task[],
    /** A collection of resources that may be referenced from within the OSCAL document instance. */
    back_matter?: BackMatter,
}


/**
 * Used by the assessment plan and POA&M to import information about the system.
 */
export interface ImportSSP {
    /** A resolvable URL reference to a resource. */
    href: string,
    /** Additional commentary about the containing object. */
    remarks?: string,
}


/**
 * Used to define data objects that are used in the assessment plan, that do not appear in the referenced SSP.
 */
export interface LocalDefinitions {
    /** A collection of system components. */
    components?: SystemComponent[],
    /** A collection of inventory items. */
    inventory_items?: InventoryItem[],
    /** A collection of system users. */
    users?: SystemUser[],
    /** A collection of locally-defined control objectives. */
    objectives_and_methods?: LocalObjective[],
    /** A collection of activities. */
    activities?: Activity[],
    /** Additional commentary about the containing object. */
    remarks?: string,
}


/**
 * Used to define various terms and conditions under which an assessment can be performed.
 */
export interface TermsAndConditions {
    /** A collection of parts. */
    parts?: TermsAndConditionsPart[],
}


/**
 * Identifies the controls being assessed and their control objectives.
 */
export interface ReviewedControls extends OscalCommon {
    /** A human-readable description. */
    description?: string,
    /** Identifies the controls being assessed. */
    control_selections: ControlSelection[],
    /** Identifies the control objectives of the assessment. */
    control_objective_selections?: ControlObjectiveSelection[],
}


/**
 * Identifies the controls being assessed.
 */
export interface ControlSelection extends OscalCommon {
    /** A human-readable description. */
    description?: string,
    /** Include all selectable objects in the containing OSCAL selection context. */
    include_all?: IncludeAll,
    /** Control-selection entries to include in the containing OSCAL context. The concrete entry class is selected by class-level slot_usage. */
    include_controls?: AssessmentSelectControlById[],
    /** Control-selection entries to exclude in the containing OSCAL context. The concrete entry class is selected by class-level slot_usage. */
    exclude_controls?: AssessmentSelectControlById[],
}


/**
 * Identifies the control objectives of the assessment.
 */
export interface ControlObjectiveSelection extends OscalCommon {
    /** A human-readable description. */
    description?: string,
    /** Include all selectable objects in the containing OSCAL selection context. */
    include_all?: IncludeAll,
    /** Objectives to include in the assessment. */
    include_objectives?: SelectObjectiveById[],
    /** Objectives to exclude from the assessment. */
    exclude_objectives?: SelectObjectiveById[],
}


/**
 * Select a specific control for inclusion/exclusion in the assessment by literal control ID and optional statement IDs.
 */
export interface AssessmentSelectControlById {
    /** A reference to a control by its identifier. */
    control_id: string,
    /** Statement IDs for control selection. */
    statement_ids?: string[],
}


/**
 * Used to select a control objective for inclusion/exclusion.
 */
export interface SelectObjectiveById {
    /** Reference to a control objective by its identifier. */
    objective_id: string,
    /** Additional commentary about the containing object. */
    remarks?: string,
}


/**
 * Identifies system elements being assessed, such as components, inventory items, and locations.
 */
export interface AssessmentSubject extends OscalCommon {
    /** Indicates the nature or kind of the containing object. */
    type: string,
    /** A human-readable description. */
    description?: string,
    /** Include all selectable objects in the containing OSCAL selection context. */
    include_all?: IncludeAll,
    /** Assessment subjects to include. */
    include_subjects?: SelectSubjectById[],
    /** Assessment subjects to exclude. */
    exclude_subjects?: SelectSubjectById[],
}


/**
 * Identifies a set of assessment subjects to include/exclude by UUID.
 */
export interface SelectSubjectById extends OscalCommon {
    /** A UUID reference to the identified subject. */
    subject_uuid: string,
    /** Indicates the nature or kind of the containing object. */
    type: string,
}


/**
 * A human-oriented identifier reference to a resource. Use type to indicate whether the identified resource is a component, inventory item, location, user, or something else.
 */
export interface SubjectReference extends OscalCommon {
    /** A UUID reference to the identified subject. */
    subject_uuid: string,
    /** Indicates the nature or kind of the containing object. */
    type: string,
    /** A human-readable name or title. */
    title?: string,
}


/**
 * Used when the assessment subjects will be determined as part of one or more other assessment activities.
 */
export interface AssessmentSubjectPlaceholder extends OscalCommon {
    /** A machine-oriented, globally unique identifier with a cross-instance scope. */
    uuid: string,
    /** A human-readable description. */
    description?: string,
    /** Source references or source-participation entries in the containing OSCAL context. The concrete entry class is selected by class-level slot_usage. */
    sources: AssessmentSubjectSource[],
}


/**
 * Assessment subjects will be identified while conducting the referenced activity.
 */
export interface AssessmentSubjectSource {
    /** A UUID reference to a task. */
    task_uuid: string,
    /** Additional commentary about the containing object. */
    remarks?: string,
}


/**
 * Identifies the assets used to perform this assessment.
 */
export interface AssessmentAssets {
    /** A collection of system components. */
    components?: SystemComponent[],
    /** A collection of assessment platforms. */
    assessment_platforms: AssessmentPlatform[],
}


/**
 * Used to represent the toolset used to perform aspects of the assessment.
 */
export interface AssessmentPlatform extends OscalCommon {
    /** A machine-oriented, globally unique identifier with a cross-instance scope. */
    uuid: string,
    /** A human-readable name or title. */
    title?: string,
    /** The set of components used by the assessment platform. */
    uses_components?: UsesComponent[],
}


/**
 * The set of components that are used by the assessment platform.
 */
export interface UsesComponent extends OscalCommon, HasResponsibleParties {
    /** A UUID reference to a component. */
    component_uuid: string,
}


/**
 * A local definition of a control objective for this assessment. Uses catalog syntax for control objective and assessment actions.
 */
export interface LocalObjective extends OscalCommon {
    /** A reference to a control by its identifier. */
    control_id: string,
    /** A human-readable description. */
    description?: string,
    /** A collection of parts. */
    parts: ControlPart[],
}


/**
 * A local definition of a control objective.
 */
export interface AssessmentMethod extends OscalCommon {
    /** A machine-oriented, globally unique identifier with a cross-instance scope. */
    uuid: string,
    /** A human-readable description. */
    description?: string,
    /** An assessment part. */
    part: AssessmentPart,
}


/**
 * Identifies an assessment or related process that can be performed. In the assessment plan, this is an intended activity.
 */
export interface Activity extends OscalCommon, HasResponsibleRoles {
    /** A machine-oriented, globally unique identifier with a cross-instance scope. */
    uuid: string,
    /** A human-readable name or title. */
    title?: string,
    /** A human-readable description. */
    description: string,
    /** A collection of steps in an activity. */
    steps?: Step[],
    /** A reference to reviewed controls for this activity or step. */
    related_controls?: ReviewedControls,
}


/**
 * Identifies an individual step in a series of steps related to an activity, such as an assessment test or examination procedure.
 */
export interface Step extends OscalCommon, HasResponsibleRoles {
    /** A machine-oriented, globally unique identifier with a cross-instance scope. */
    uuid: string,
    /** A human-readable name or title. */
    title?: string,
    /** A human-readable description. */
    description: string,
    /** Identifies the controls being assessed and their control objectives. */
    reviewed_controls?: ReviewedControls,
}


/**
 * Represents a scheduled event or milestone, which may be associated with a series of assessment actions.
 */
export interface Task extends OscalCommon, HasResponsibleRoles {
    /** A machine-oriented, globally unique identifier with a cross-instance scope. */
    uuid: string,
    /** Indicates the nature or kind of the containing object. */
    type: string,
    /** A human-readable name or title. */
    title: string,
    /** A human-readable description. */
    description?: string,
    /** The timing under which a task is intended to occur. */
    timing?: EventTiming,
    /** Tasks that this task depends on. */
    dependencies?: TaskDependency[],
    /** Activities associated with this task. */
    associated_activities?: AssociatedActivity[],
    /** A collection of tasks. */
    tasks?: Task[],
    /** Assessment subjects or subject references for this object. */
    subjects?: AssessmentSubject[],
}


/**
 * The timing under which the task is intended to occur.
 */
export interface EventTiming {
    /** The task is intended to occur on the specified date. */
    on_date?: OnDateCondition,
    /** The task is intended to occur within the specified date range. */
    within_date_range?: WithinDateRange,
    /** The task is intended to occur at the specified frequency. */
    at_frequency?: AtFrequency,
}


/**
 * The task is intended to occur on the specified date.
 */
export interface OnDateCondition {
    /** The date and time when the action occurred. */
    date: string,
    /** Additional commentary about the containing object. */
    remarks?: string,
}


/**
 * The task is intended to occur within the specified date range.
 */
export interface WithinDateRange {
    /** The start date/time. */
    start: string,
    /** The end date/time. */
    end: string,
    /** Additional commentary about the containing object. */
    remarks?: string,
}


/**
 * The task is intended to occur at the specified frequency.
 */
export interface AtFrequency {
    /** The task must occur every period (in the given units). */
    period: number,
    /** The unit of time for the period. */
    unit: string,
    /** Additional commentary about the containing object. */
    remarks?: string,
}


/**
 * Used to indicate that a task is dependent on another task.
 */
export interface TaskDependency {
    /** A UUID reference to a task. */
    task_uuid: string,
    /** Additional commentary about the containing object. */
    remarks?: string,
}


/**
 * Identifies an individual activity to be performed as part of a task.
 */
export interface AssociatedActivity extends OscalCommon, HasResponsibleRoles {
    /** A UUID reference to an activity. */
    activity_uuid: string,
    /** Assessment subjects or subject references for this object. */
    subjects: AssessmentSubject[],
}


/**
 * A partition of an assessment plan or results or a child of another part.
 */
export interface AssessmentPart extends HasPropsAndLinks {
    /** A machine-oriented, globally unique identifier with a cross-instance scope. */
    uuid?: string,
    /** A textual label that uniquely identifies an attribute or semantic type. */
    name: string,
    /** An optional namespace qualifying a name. Allows different organizations to associate distinct semantics with the same name. */
    ns?: string,
    /** A textual label that provides a sub-type or characterization. */
    _class?: string,
    /** A human-readable name or title. */
    title?: string,
    /** Permits multiple paragraphs, lists, tables etc. */
    prose?: string,
    /** A collection of parts. */
    parts?: AssessmentPart[],
}


/**
 * A terms-and-conditions scoped assessment part.
 */
export interface TermsAndConditionsPart extends AssessmentPart {
}


/**
 * An annotated, markup-based textual element of a control's or catalog group's definition, or a child of another part.
 */
export interface ControlPart extends HasPropsAndLinks {
    /** A unique human-oriented identifier within a particular context. */
    id?: string,
    /** A textual label that uniquely identifies an attribute or semantic type. */
    name: string,
    /** An optional namespace qualifying a name. Allows different organizations to associate distinct semantics with the same name. */
    ns?: string,
    /** A textual label that provides a sub-type or characterization. */
    _class?: string,
    /** A human-readable name or title. */
    title?: string,
    /** Permits multiple paragraphs, lists, tables etc. */
    prose?: string,
    /** A collection of parts. */
    parts?: ControlPart[],
}


/**
 * Identifies the parameter that will be set by the enclosed value.
 */
export interface SetParameter {
    /** The identifier for the parameter being set or referenced. */
    param_id: string,
    /** A parameter value or set of values. */
    values: string[],
    /** Additional commentary about the containing object. */
    remarks?: string,
}


/**
 * A defined component that can be part of an implemented system.
 */
export interface SystemComponent extends OscalCommon, HasResponsibleRoles {
    /** A machine-oriented, globally unique identifier with a cross-instance scope. */
    uuid: string,
    /** Indicates the nature or kind of the containing object. */
    type: string,
    /** A human-readable name or title. */
    title: string,
    /** A human-readable description. */
    description: string,
    /** A summary of the technological or business purpose of the component. */
    purpose?: string,
    /** Information about the protocol used to provide a service. */
    protocols?: Protocol[],
    /** Status indicator used by the containing OSCAL context. Allowed values are constrained by class-level slot_usage. */
    status: ComponentStatus,
}


/**
 * Describes the operational status of the system component.
 */
export interface ComponentStatus {
    /** The operational status. */
    state: string,
    /** Additional commentary about the containing object. */
    remarks?: string,
}


/**
 * Information about the protocol used to provide a service.
 */
export interface Protocol {
    /** A machine-oriented, globally unique identifier with a cross-instance scope. */
    uuid?: string,
    /** A textual label that uniquely identifies an attribute or semantic type. */
    name?: string,
    /** A human-readable name or title. */
    title?: string,
    /** Where applicable, the transport layer protocol port range. */
    port_ranges?: PortRange[],
}


/**
 * Where applicable, the transport layer protocol port range.
 */
export interface PortRange {
    /** The start date/time. */
    start?: number,
    /** The end date/time. */
    end?: number,
    /** Indicates the transport type. */
    transport?: string,
    /** Additional commentary about the containing object. */
    remarks?: string,
}


/**
 * Indicates the degree to which a given control is implemented.
 */
export interface ImplementationStatus {
    /** Identifies the implementation status of the control or control objective. Recommended values are in ImplementationStatusStateEnum; other values are permitted (OSCAL allow-other="yes"). */
    state: string,
    /** Additional commentary about the containing object. */
    remarks?: string,
}


/**
 * A type of user that interacts with the system based on an associated role.
 */
export interface SystemUser extends OscalCommon {
    /** A machine-oriented, globally unique identifier with a cross-instance scope. */
    uuid: string,
    /** A human-readable name or title. */
    title?: string,
    /** A short common name, abbreviation, or acronym. */
    short_name?: string,
    /** A human-readable description. */
    description?: string,
    /** Role identifiers associated with the user. */
    role_ids?: string[],
    /** A collection of authorized privileges. */
    authorized_privileges?: AuthorizedPrivilege[],
}


/**
 * Identifies a specific system privilege held by the user, along with an associated description and/or rationale for the privilege.
 */
export interface AuthorizedPrivilege {
    /** A human-readable name or title. */
    title: string,
    /** A human-readable description. */
    description?: string,
    /** Describes a function performed for a given authorized privilege. */
    functions_performed: string[],
}


/**
 * A single managed inventory item within the system.
 */
export interface InventoryItem extends OscalCommon, HasResponsibleParties {
    /** A machine-oriented, globally unique identifier with a cross-instance scope. */
    uuid: string,
    /** A human-readable description. */
    description: string,
    /** A collection of implemented components. */
    implemented_components?: ImplementedComponent[],
}


/**
 * The set of components that are implemented in a given system inventory item.
 */
export interface ImplementedComponent extends OscalCommon, HasResponsibleParties {
    /** A UUID reference to a component. */
    component_uuid: string,
}


/**
 * A human-oriented, globally unique identifier for a system.
 */
export interface SystemId {
    /** A unique human-oriented identifier within a particular context. */
    id: string,
    /** A human-readable label for a specific identifier scheme. Recommended values are in SystemIdentifierTypeEnum; other URI values are permitted (OSCAL allow-other="yes"). */
    identifier_type?: string,
}


/**
 * Implementation-common scoped OSCAL property.
 */
export interface ImplementationCommonProperty extends Property {
}


/**
 * Implementation-common scoped OSCAL link.
 */
export interface ImplementationCommonLink extends Link {
}


/**
 * Implementation-common scoped responsible role.
 */
export interface ImplementationResponsibleRole extends ResponsibleRole {
}


/**
 * Implementation-common scoped responsible party.
 */
export interface ImplementationResponsibleParty extends ResponsibleParty {
}


/**
 * Identifies the source of the finding, such as a tool, interviewed person, or activity.
 */
export interface Origin {
    /** The actor that produces an observation, a finding, or a risk. */
    actors: OriginActor[],
    /** Identifies tasks for which the containing object is a consequence. */
    related_tasks?: RelatedTask[],
}


/**
 * The actor that produces an observation, a finding, or a risk.
 */
export interface OriginActor extends HasPropsAndLinks {
    /** Indicates the nature or kind of the containing object. */
    type: string,
    /** A machine-oriented identifier reference to the tool or person based on the associated type. */
    actor_uuid: string,
    /** A reference to a role by its identifier. */
    role_id?: string,
}


/**
 * Identifies an individual task for which the containing object is a consequence of.
 */
export interface RelatedTask extends OscalCommon, HasResponsibleParties {
    /** A UUID reference to a task. */
    task_uuid: string,
    /** Assessment subjects or subject references for this object. */
    subjects?: AssessmentSubject[],
    /** Used to detail assessment subjects that were identified by this task. */
    identified_subject?: IdentifiedSubject,
}


/**
 * Used to detail assessment subjects that were identified by this task.
 */
export interface IdentifiedSubject {
    /** A reference to an assessment subject placeholder defined in the assessment plan. */
    subject_placeholder_uuid: string,
    /** Assessment subjects or subject references for this object. */
    subjects: AssessmentSubject[],
}


/**
 * Describes an individual observation.
 */
export interface Observation extends OscalCommon {
    /** A machine-oriented, globally unique identifier with a cross-instance scope. */
    uuid: string,
    /** A human-readable name or title. */
    title?: string,
    /** A human-readable description. */
    description: string,
    /** Identifies how the observation was made. Recommended values are in ObservationMethodEnum; other values are permitted (OSCAL allow-other="yes"). */
    methods: string[],
    /** Identifies the nature of the observation. Recommended values are in ObservationTypeEnum; other values are permitted (OSCAL allow-other="yes"). */
    types?: string[],
    /** Identifies the source of observations, findings, or risks. */
    origins?: Origin[],
    /** Assessment subjects or subject references for this object. */
    subjects?: SubjectReference[],
    /** Links the observation to relevant evidence. */
    relevant_evidence?: RelevantEvidence[],
    /** Date/time stamp identifying when the finding information was collected. */
    collected: string,
    /** Date/time identifying when the finding information is no longer considered valid. */
    expires?: string,
}


/**
 * Links this observation to relevant evidence.
 */
export interface RelevantEvidence extends OscalCommon {
    /** A resolvable URL reference to a resource. */
    href?: string,
    /** A human-readable description. */
    description: string,
}


/**
 * Describes an individual finding.
 */
export interface Finding extends OscalCommon {
    /** A machine-oriented, globally unique identifier with a cross-instance scope. */
    uuid: string,
    /** A human-readable name or title. */
    title: string,
    /** A human-readable description. */
    description: string,
    /** Identifies the target of a finding. */
    target: FindingTarget,
    /** A reference to the implementation statement in the SSP to which this finding is related. */
    implementation_statement_uuid?: string,
    /** Identifies the source of observations, findings, or risks. */
    origins?: Origin[],
    /** Relates the containing object to a set of referenced observations. */
    related_observations?: RelatedObservation[],
    /** Relates the finding to a set of referenced risks. */
    related_risks?: AssociatedRisk[],
}


/**
 * Captures an assessor's conclusions regarding the degree to which an objective is satisfied.
 */
export interface FindingTarget extends OscalCommon {
    /** Indicates the nature or kind of the containing object. */
    type: string,
    /** Identifies the specific target qualified by the type. */
    target_id: string,
    /** A human-readable name or title. */
    title?: string,
    /** A human-readable description. */
    description?: string,
    /** Identifies the implementation status of the control. */
    implementation_status?: ImplementationStatus,
    /** Status indicator used by the containing OSCAL context. Allowed values are constrained by class-level slot_usage. */
    status: ObjectiveStatus,
}


/**
 * A determination of if the objective is satisfied or not within a given system.
 */
export interface ObjectiveStatus {
    /** An indication as to whether the objective is satisfied or not. */
    state: string,
    /** The reason the objective was given its status. Recommended values are in ObjectiveStatusReasonEnum; other values are permitted (OSCAL allow-other="yes"). */
    reason?: string,
    /** Additional commentary about the containing object. */
    remarks?: string,
}


/**
 * Relates the identified element to a set of referenced observations.
 */
export interface RelatedObservation {
    /** A machine-oriented identifier reference to an observation defined in the list of observations. */
    observation_uuid: string,
    /** Additional commentary about the containing object. */
    remarks?: string,
}


/**
 * Relates the finding to a set of referenced risks.
 */
export interface AssociatedRisk {
    /** A machine-oriented identifier reference to a risk defined in the list of risks. */
    risk_uuid: string,
    /** Additional commentary about the containing object. */
    remarks?: string,
}


/**
 * An identified risk.
 */
export interface Risk extends HasPropsAndLinks {
    /** A machine-oriented, globally unique identifier with a cross-instance scope. */
    uuid: string,
    /** A human-readable name or title. */
    title: string,
    /** A human-readable description. */
    description: string,
    /** An assessor's summary of the risk, in narrative form. */
    statement: string,
    /** Identifies the source of observations, findings, or risks. */
    origins?: Origin[],
    /** The referenced threat identifiers. */
    threat_ids?: ThreatId[],
    /** Supporting information about the risk and how it relates to the system. */
    characterizations?: Characterization[],
    /** Describes existing mitigating factors that may affect the overall determination of the risk. */
    mitigating_factors?: MitigatingFactor[],
    /** The date/time by which the risk must be resolved. */
    deadline?: string,
    /** Describes either recommended or actual responses to a risk. */
    remediations?: Response[],
    /** A log of all risk-related tasks taken. */
    risk_log?: RiskLog,
    /** Relates the containing object to a set of referenced observations. */
    related_observations?: RelatedObservation[],
    /** Status indicator used by the containing OSCAL context. Allowed values are constrained by class-level slot_usage. */
    status: string,
}


/**
 * A pointer, by ID, to an externally-defined threat.
 */
export interface ThreatId {
    /** A resolvable URL reference to a resource. */
    href?: string,
    /** Specifies the system or scheme from which the identifier originates. */
    system: string,
    /** A unique human-oriented identifier within a particular context. */
    id: string,
}


/**
 * A collection of descriptive data about the containing object from a specific origin.
 */
export interface Characterization extends HasPropsAndLinks {
    /** The source of the finding. */
    origin: Origin,
    /** An individual characteristic that is part of a larger set produced by the same actor. */
    facets: Facet[],
}


/**
 * An individual characteristic that is part of a larger set produced by the same actor.
 */
export interface Facet extends OscalCommon {
    /** A textual label that uniquely identifies an attribute or semantic type. */
    name: string,
    /** The value associated with the containing object. */
    value: string,
    /** Specifies the system or scheme from which the identifier originates. */
    system: string,
}


/**
 * Describes an existing mitigating factor that may affect the overall determination of the risk.
 */
export interface MitigatingFactor extends HasPropsAndLinks {
    /** A machine-oriented, globally unique identifier with a cross-instance scope. */
    uuid: string,
    /** A human-readable description. */
    description: string,
    /** A machine-oriented, globally unique identifier with cross-instance scope that can be used to reference this implementation statement elsewhere in this or other OSCAL instances. */
    implementation_uuid?: string,
    /** Assessment subjects or subject references for this object. */
    subjects?: SubjectReference[],
}


/**
 * Describes either recommended or an actual plan for addressing the risk.
 */
export interface Response extends OscalCommon {
    /** A machine-oriented, globally unique identifier with a cross-instance scope. */
    uuid: string,
    /** A human-readable name or title. */
    title: string,
    /** A human-readable description. */
    description: string,
    /** Identifies whether this is a recommendation or an actual plan. Recommended values are in ResponseLifecycleEnum; other values are permitted (OSCAL allow-other="yes"). */
    lifecycle: string,
    /** Identifies the source of observations, findings, or risks. */
    origins?: Origin[],
    /** Identifies an asset required to achieve remediation. */
    required_assets?: RequiredAsset[],
    /** A collection of tasks. */
    tasks?: Task[],
}


/**
 * Identifies an asset required to achieve remediation.
 */
export interface RequiredAsset extends OscalCommon {
    /** A machine-oriented, globally unique identifier with a cross-instance scope. */
    uuid: string,
    /** A human-readable name or title. */
    title?: string,
    /** A human-readable description. */
    description: string,
    /** Assessment subjects or subject references for this object. */
    subjects?: SubjectReference[],
}


/**
 * A log of all risk-related tasks taken.
 */
export interface RiskLog {
    /** Identifies an individual risk response that occurred as part of managing an identified risk. */
    entries: RiskLogEntry[],
}


/**
 * Identifies an individual risk response that occurred as part of managing an identified risk.
 */
export interface RiskLogEntry extends OscalCommon {
    /** A machine-oriented, globally unique identifier with a cross-instance scope. */
    uuid: string,
    /** A human-readable name or title. */
    title?: string,
    /** A human-readable description. */
    description?: string,
    /** The start date/time. */
    start: string,
    /** The end date/time. */
    end?: string,
    /** Used to indicate who created a log entry in what role. */
    logged_by?: LoggedBy[],
    /** Identifies the risk change that prompted the log entry. Recommended values are in RiskStatusEnum; other values are permitted (OSCAL allow-other="yes"). */
    status_change?: string,
    /** Identifies an individual risk response that this log entry is for. */
    related_responses?: RiskResponseReference[],
}


/**
 * Used to indicate who created a log entry in what role.
 */
export interface LoggedBy {
    /** A machine-oriented identifier reference to the party who is making the log entry. */
    party_uuid: string,
    /** A reference to a role by its identifier. */
    role_id?: string,
    /** Additional commentary about the containing object. */
    remarks?: string,
}


/**
 * Identifies an individual risk response that this log entry is for.
 */
export interface RiskResponseReference extends OscalCommon {
    /** A machine-oriented identifier reference to a unique risk response. */
    response_uuid: string,
    /** Identifies tasks for which the containing object is a consequence. */
    related_tasks?: RelatedTask[],
}


/**
 * Root wrapper for an OSCAL System Security Plan document.
 */
export interface SspDocument extends OscalDocument {
    /** A system security plan, such as those described in NIST SP 800-18. */
    system_security_plan: SystemSecurityPlan,
}


/**
 * A system security plan, such as those described in NIST SP 800-18.
 */
export interface SystemSecurityPlan {
    /** A machine-oriented, globally unique identifier with a cross-instance scope. */
    uuid: string,
    /** Provides information about the containing document, and defines concepts shared across the document. */
    metadata: Metadata,
    /** Used to import the OSCAL profile representing the system's control baseline. */
    import_profile: ImportProfile,
    /** Contains the characteristics of the system, such as its name, purpose, and security impact level. */
    system_characteristics: SystemCharacteristics,
    /** Provides information as to how the system is implemented. */
    system_implementation: SystemImplementation,
    /** Describes how the system satisfies a set of controls. */
    control_implementation: SspControlImplementation,
    /** A collection of resources that may be referenced from within the OSCAL document instance. */
    back_matter?: BackMatter,
}


/**
 * Used to import the OSCAL profile representing the system's control baseline.
 */
export interface ImportProfile {
    /** A resolvable URL reference to a resource. */
    href: string,
    /** Additional commentary about the containing object. */
    remarks?: string,
}


/**
 * Contains the characteristics of the system, such as its name, purpose, and security impact level.
 */
export interface SystemCharacteristics {
    /** Unique identifiers for the system. */
    system_ids: SystemId[],
    /** The full name of the system. */
    system_name: string,
    /** A short name for the system, such as an acronym, that is suitable for display in a data table or summary list. */
    system_name_short?: string,
    /** A human-readable description. */
    description: string,
    /** The date the system received its authorization. */
    date_authorized?: string,
    /** The overall information system sensitivity categorization, such as defined by FIPS-199. */
    security_sensitivity_level?: string,
    /** Contains details about all information types that are stored, processed, or transmitted by the system. */
    system_information: SystemInformation,
    /** The overall level of expected impact resulting from unauthorized disclosure, modification, or loss of access to information. */
    security_impact_level?: SecurityImpactLevel,
    /** Describes the operational status of the system. */
    system_status: SystemStatus,
    /** A description of this system's authorization boundary, optionally supplemented with diagrams that illustrate the authorization boundary. */
    authorization_boundary: AuthorizationBoundary,
    /** A description of the system's network architecture, optionally supplemented with diagrams that illustrate the network architecture. */
    network_architecture?: NetworkArchitecture,
    /** A description of the logical flow of information within the system and across its boundaries, optionally supplemented with diagrams. */
    data_flow?: DataFlow,
    /** Responsible party assignments. */
    responsible_parties?: SspSystemCharacteristicsResponsibleParty[],
    /** Additional commentary about the containing object. */
    remarks?: string,
}


/**
 * Contains details about all information types that are stored, processed, or transmitted by the system, such as privacy information.
 */
export interface SystemInformation {
    /** A list of properties. */
    props?: SspSystemInformationProp[],
    /** A list of links. */
    links?: SspSystemInformationLink[],
    /** Contains details about one information type that is stored, processed, or transmitted by the system. */
    information_types: InformationType[],
}


/**
 * Contains details about one information type that is stored, processed, or transmitted by the system, such as privacy information, and its impact level.
 */
export interface InformationType {
    /** A machine-oriented, globally unique identifier with a cross-instance scope. */
    uuid?: string,
    /** A human-readable name or title. */
    title: string,
    /** A human-readable description. */
    description: string,
    /** A set of information type identifiers qualified by the given identification system used. */
    categorizations?: InformationTypeCategorization[],
    /** A list of properties. */
    props?: Property[],
    /** A list of links. */
    links?: Link[],
    /** The expected level of impact resulting from the unauthorized disclosure of the described information. */
    confidentiality_impact?: ImpactLevel,
    /** The expected level of impact resulting from the unauthorized modification of the described information. */
    integrity_impact?: ImpactLevel,
    /** The expected level of impact resulting from the disruption of access to or use of the described information or the information system. */
    availability_impact?: ImpactLevel,
}


/**
 * A set of information type identifiers qualified by the given identification system used.
 */
export interface InformationTypeCategorization {
    /** Specifies the information type identification system used. Recommended values are in InformationTypeCategorizationSystemEnum; other values are permitted (OSCAL allow-other="yes"). */
    system: string,
    /** An identifier qualified by the given identification system used, such as NIST SP 800-60. */
    information_type_ids?: string[],
}


/**
 * The expected level of impact resulting from the described information's confidentiality, integrity, or availability affect.
 */
export interface ImpactLevel {
    /** A list of properties. */
    props?: Property[],
    /** A list of links. */
    links?: Link[],
    /** The prescribed base (Confidentiality, Integrity, or Availability) security impact level. */
    base: string,
    /** The selected (Confidentiality, Integrity, or Availability) security impact level. */
    selected?: string,
    /** If the selected security level is different from the base security level, this contains the justification for the change. */
    adjustment_justification?: string,
}


/**
 * The overall level of expected impact resulting from unauthorized disclosure, modification, or loss of access to information.
 */
export interface SecurityImpactLevel {
    /** A target-level of confidentiality for the system, based on the sensitivity of information within the system. */
    security_objective_confidentiality: string,
    /** A target-level of integrity for the system, based on the sensitivity of information within the system. */
    security_objective_integrity: string,
    /** A target-level of availability for the system, based on the sensitivity of information within the system. */
    security_objective_availability: string,
}


/**
 * Describes the operational status of the system.
 */
export interface SystemStatus {
    /** Additional commentary about the containing object. */
    remarks?: string,
    /** The current operating status of the system. */
    state: string,
}


/**
 * A description of this system's authorization boundary, optionally supplemented with diagrams that illustrate the authorization boundary.
 */
export interface AuthorizationBoundary {
    /** A human-readable description. */
    description: string,
    /** A list of properties. */
    props?: Property[],
    /** A list of links. */
    links?: Link[],
    /** A collection of diagrams that visually depict the subject. */
    diagrams?: Diagram[],
    /** Additional commentary about the containing object. */
    remarks?: string,
}


/**
 * A graphic that provides a visual representation the system, or some aspect of it.
 */
export interface Diagram {
    /** A machine-oriented, globally unique identifier with a cross-instance scope. */
    uuid: string,
    /** A human-readable description. */
    description?: string,
    /** A list of properties. */
    props?: Property[],
    /** A list of links. */
    links?: SspDiagramLink[],
    /** A brief caption to annotate the diagram. */
    caption?: string,
    /** Additional commentary about the containing object. */
    remarks?: string,
}


/**
 * A description of the system's network architecture, optionally supplemented with diagrams that illustrate the network architecture.
 */
export interface NetworkArchitecture {
    /** A human-readable description. */
    description: string,
    /** A list of properties. */
    props?: Property[],
    /** A list of links. */
    links?: Link[],
    /** A collection of diagrams that visually depict the subject. */
    diagrams?: Diagram[],
    /** Additional commentary about the containing object. */
    remarks?: string,
}


/**
 * A description of the logical flow of information within the system and across its boundaries, optionally supplemented with diagrams.
 */
export interface DataFlow {
    /** A human-readable description. */
    description: string,
    /** A list of properties. */
    props?: Property[],
    /** A list of links. */
    links?: Link[],
    /** A collection of diagrams that visually depict the subject. */
    diagrams?: Diagram[],
    /** Additional commentary about the containing object. */
    remarks?: string,
}


/**
 * Provides information as to how the system is implemented.
 */
export interface SystemImplementation {
    /** A list of properties. */
    props?: Property[],
    /** A list of links. */
    links?: Link[],
    /** A description of another authorized system from which this system inherits capabilities that satisfy security requirements. */
    leveraged_authorizations?: LeveragedAuthorization[],
    /** A collection of system users. */
    users?: SystemUser[],
    /** A collection of system components. */
    components: SspSystemComponent[],
    /** A collection of inventory items. */
    inventory_items?: SspInventoryItem[],
    /** Additional commentary about the containing object. */
    remarks?: string,
}


/**
 * A description of another authorized system from which this system inherits capabilities that satisfy security requirements. Another term for this concept is a common control provider.
 */
export interface LeveragedAuthorization {
    /** A machine-oriented, globally unique identifier with a cross-instance scope. */
    uuid: string,
    /** A human-readable name or title. */
    title: string,
    /** A list of properties. */
    props?: Property[],
    /** A list of links. */
    links?: SspLeveragedAuthorizationLink[],
    /** A machine-oriented identifier reference to the party who is making the log entry. */
    party_uuid: string,
    /** The date the system received its authorization. */
    date_authorized: string,
    /** Additional commentary about the containing object. */
    remarks?: string,
}


/**
 * Describes how the system satisfies a set of controls.
 */
export interface SspControlImplementation {
    /** A human-readable description. */
    description: string,
    /** Identifies the parameter that will be set by the enclosed value. */
    set_parameters?: SetParameter[],
    /** Control implementation requirement entries in the containing OSCAL context. The concrete entry class is selected by class-level slot_usage. */
    implemented_requirements: SspImplementedRequirement[],
}


/**
 * Describes how the system satisfies an individual control.
 */
export interface SspImplementedRequirement {
    /** A machine-oriented, globally unique identifier with a cross-instance scope. */
    uuid: string,
    /** A reference to a control by its identifier. */
    control_id: string,
    /** A list of properties. */
    props?: SspControlOriginationProp[],
    /** A list of links. */
    links?: Link[],
    /** Identifies the parameter that will be set by the enclosed value. */
    set_parameters?: SetParameter[],
    /** Responsible role assignments. */
    responsible_roles?: SspImplementedRequirementResponsibleRole[],
    /** Control statement implementation entries in the containing OSCAL context. The concrete entry class is selected by class-level slot_usage. */
    statements?: SspStatement[],
    /** Defines how the referenced component implements a set of controls. */
    by_components?: ByComponent[],
    /** Additional commentary about the containing object. */
    remarks?: string,
}


/**
 * Identifies which statements within a control are addressed.
 */
export interface SspStatement {
    /** A reference to a control statement identifier. */
    statement_id: string,
    /** A machine-oriented, globally unique identifier with a cross-instance scope. */
    uuid: string,
    /** A list of properties. */
    props?: SspControlOriginationProp[],
    /** A list of links. */
    links?: Link[],
    /** Responsible role assignments. */
    responsible_roles?: SspImplementedRequirementResponsibleRole[],
    /** Defines how the referenced component implements a set of controls. */
    by_components?: ByComponent[],
    /** Additional commentary about the containing object. */
    remarks?: string,
}


/**
 * Defines how the referenced component implements a set of controls.
 */
export interface ByComponent {
    /** A UUID reference to a component. */
    component_uuid: string,
    /** A machine-oriented, globally unique identifier with a cross-instance scope. */
    uuid: string,
    /** A human-readable description. */
    description: string,
    /** A list of properties. */
    props?: SspControlOriginationProp[],
    /** A list of links. */
    links?: SspByComponentLink[],
    /** Identifies the parameter that will be set by the enclosed value. */
    set_parameters?: SetParameter[],
    /** Identifies the implementation status of the control. */
    implementation_status?: ImplementationStatus,
    /** Defines a set of control implementations that are provided as reference implementations for use by organizations implementing the leveraged system. */
    export?: Export,
    /** Describes a control implementation inherited by a leveraging system. */
    inherited?: InheritedControlImplementation[],
    /** Describes how this system satisfies a responsibility imposed by a leveraged system. */
    satisfied?: SatisfiedControlImplementation[],
    /** Responsible role assignments. */
    responsible_roles?: SspByComponentResponsibleRole[],
    /** Additional commentary about the containing object. */
    remarks?: string,
}


/**
 * Defines a set of control implementations that are provided as reference implementations for use by organizations implementing the leveraged system.
 */
export interface Export {
    /** A human-readable description. */
    description?: string,
    /** A list of properties. */
    props?: Property[],
    /** A list of links. */
    links?: Link[],
    /** Describes a capability which may be inherited by a leveraging system. */
    provided?: ProvidedControlImplementation[],
    /** Describes a control implementation responsibility imposed on a leveraging system. */
    responsibilities?: ControlResponsibility[],
}


/**
 * Describes a capability which may be inherited by a leveraging system.
 */
export interface ProvidedControlImplementation {
    /** A machine-oriented, globally unique identifier with a cross-instance scope. */
    uuid: string,
    /** A human-readable description. */
    description: string,
    /** A list of properties. */
    props?: Property[],
    /** A list of links. */
    links?: Link[],
    /** Responsible role assignments. */
    responsible_roles?: SspByComponentResponsibleRole[],
    /** Additional commentary about the containing object. */
    remarks?: string,
}


/**
 * Describes a control implementation responsibility imposed on a leveraging system.
 */
export interface ControlResponsibility {
    /** A machine-oriented, globally unique identifier with a cross-instance scope. */
    uuid: string,
    /** Machine-oriented identifier reference to an inherited control implementation that a leveraging system is implementing. */
    provided_uuid?: string,
    /** A human-readable description. */
    description: string,
    /** A list of properties. */
    props?: Property[],
    /** A list of links. */
    links?: Link[],
    /** Responsible role assignments. */
    responsible_roles?: SspByComponentResponsibleRole[],
    /** Additional commentary about the containing object. */
    remarks?: string,
}


/**
 * Describes a control implementation inherited by a leveraging system.
 */
export interface InheritedControlImplementation {
    /** A machine-oriented, globally unique identifier with a cross-instance scope. */
    uuid: string,
    /** Machine-oriented identifier reference to an inherited control implementation that a leveraging system is implementing. */
    provided_uuid?: string,
    /** A human-readable description. */
    description: string,
    /** A list of properties. */
    props?: Property[],
    /** A list of links. */
    links?: Link[],
    /** Responsible role assignments. */
    responsible_roles?: SspByComponentResponsibleRole[],
    /** Additional commentary about the containing object. */
    remarks?: string,
}


/**
 * Describes how this system satisfies a responsibility imposed by a leveraged system.
 */
export interface SatisfiedControlImplementation {
    /** A machine-oriented, globally unique identifier with a cross-instance scope. */
    uuid: string,
    /** Machine-oriented identifier reference to a control implementation responsibility imposed by a leveraged system. */
    responsibility_uuid?: string,
    /** A human-readable description. */
    description: string,
    /** A list of properties. */
    props?: Property[],
    /** A list of links. */
    links?: Link[],
    /** Responsible role assignments. */
    responsible_roles?: SspByComponentResponsibleRole[],
    /** Additional commentary about the containing object. */
    remarks?: string,
}


/**
 * SSP-scoped property used in system characteristics.
 */
export interface SspSystemCharacteristicsProp extends Property {
}


/**
 * SSP-scoped property used in system information.
 */
export interface SspSystemInformationProp extends Property {
}


/**
 * SSP-scoped property used in implemented requirement and by-component contexts.
 */
export interface SspControlOriginationProp extends Property {
}


/**
 * SSP-scoped property used for component and inventory allows-authenticated-scan.
 */
export interface SspAllowsAuthenticatedScanProp extends Property {
}


/**
 * SSP-scoped link used in system information.
 */
export interface SspSystemInformationLink extends Link {
}


/**
 * SSP-scoped link used in diagram objects.
 */
export interface SspDiagramLink extends Link {
}


/**
 * SSP-scoped link used in leveraged authorization objects.
 */
export interface SspLeveragedAuthorizationLink extends Link {
}


/**
 * SSP-scoped link used in by-component contexts.
 */
export interface SspByComponentLink extends Link {
}


/**
 * SSP-scoped responsible party for system characteristics.
 */
export interface SspSystemCharacteristicsResponsibleParty extends ResponsibleParty {
}


/**
 * SSP-scoped responsible role used by implemented requirement and statement contexts.
 */
export interface SspImplementedRequirementResponsibleRole extends ResponsibleRole {
}


/**
 * SSP-scoped responsible role used by by-component contexts.
 */
export interface SspByComponentResponsibleRole extends ResponsibleRole {
}


/**
 * SSP-scoped system component with allows-authenticated-scan property typing.
 */
export interface SspSystemComponent extends SystemComponent {
}


/**
 * SSP-scoped inventory item with allows-authenticated-scan property typing.
 */
export interface SspInventoryItem extends InventoryItem {
}


/**
 * Root wrapper for an OSCAL Assessment Results document.
 */
export interface AssessmentResultsDocument extends OscalDocument {
    /** The root assessment results object. */
    assessment_results: AssessmentResults,
}


/**
 * Security assessment results, such as those provided by a FedRAMP assessor in a security assessment report.
 */
export interface AssessmentResults {
    /** Assessment Results Universally Unique Identifier. */
    uuid: string,
    /** Provides information about the containing document, and defines concepts shared across the document. */
    metadata: Metadata,
    /** Used to import information about the governing assessment plan. */
    import_ap: ImportAssessmentPlan,
    /** Used to define data objects that do not appear in the referenced SSP. */
    local_definitions?: AssessmentResultsLocalDefinitions,
    /** A collection of assessment results. */
    results: Result[],
    /** A collection of resources that may be referenced from within the OSCAL document instance. */
    back_matter?: BackMatter,
}


/**
 * Used by assessment-results to import information about the original plan for assessing the system.
 */
export interface ImportAssessmentPlan {
    /** A resolvable URL reference to a resource. */
    href: string,
    /** Additional commentary about the containing object. */
    remarks?: string,
}


/**
 * Used to define data objects that are referenced by the assessment results but do not appear in the imported assessment plan.
 */
export interface AssessmentResultsLocalDefinitions {
    /** A collection of locally-defined control objectives. */
    objectives_and_methods?: LocalObjective[],
    /** A collection of activities. */
    activities?: Activity[],
    /** Additional commentary about the containing object. */
    remarks?: string,
}


/**
 * Identifies all of the assessment observations and findings, initial and residual risks, deviations, and disposition for a particular execution of the assessment.
 */
export interface Result extends OscalCommon {
    /** A machine-oriented, globally unique identifier with a cross-instance scope. */
    uuid: string,
    /** A human-readable name or title. */
    title: string,
    /** A human-readable description. */
    description: string,
    /** The start date/time. */
    start: string,
    /** The end date/time. */
    end?: string,
    /** Used to define data objects that do not appear in the referenced SSP. */
    local_definitions?: ResultLocalDefinitions,
    /** Identifies the controls being assessed and their control objectives. */
    reviewed_controls: ReviewedControls,
    /** A set of attestation statements for the result. */
    attestations?: Attestation[],
    /** A log of assessment-related actions taken. */
    assessment_log?: AssessmentLog,
    /** A collection of observations captured in the containing context. */
    observations?: Observation[],
    /** A collection of risks captured in the containing context. */
    risks?: Risk[],
    /** A collection of findings captured in the containing context. */
    findings?: Finding[],
}


/**
 * Used to define local implementation and assessment assets referenced by a result that do not appear in the imported system security plan.
 */
export interface ResultLocalDefinitions {
    /** A collection of system components. */
    components?: SystemComponent[],
    /** A collection of inventory items. */
    inventory_items?: InventoryItem[],
    /** A collection of system users. */
    users?: SystemUser[],
    /** Identifies the assets used to perform this assessment. */
    assessment_assets?: AssessmentAssets,
    /** A collection of tasks. */
    tasks?: Task[],
}


/**
 * A set of textual attestation statements, typically written by the assessor.
 */
export interface Attestation extends HasResponsibleParties {
    /** A collection of parts. */
    parts: AssessmentPart[],
}


/**
 * A log of all assessment-related actions taken.
 */
export interface AssessmentLog {
    /** Identifies an individual risk response that occurred as part of managing an identified risk. */
    entries: AssessmentLogEntry[],
}


/**
 * Identifies the result of an action and/or task that occurred as part of executing an assessment plan or assessment event.
 */
export interface AssessmentLogEntry extends OscalCommon {
    /** A machine-oriented, globally unique identifier with a cross-instance scope. */
    uuid: string,
    /** A human-readable name or title. */
    title?: string,
    /** A human-readable description. */
    description?: string,
    /** The start date/time. */
    start: string,
    /** The end date/time. */
    end?: string,
    /** Used to indicate who created a log entry in what role. */
    logged_by?: LoggedBy[],
    /** Identifies tasks for which the containing object is a consequence. */
    related_tasks?: RelatedTask[],
}


/**
 * Root wrapper for an OSCAL Component Definition document.
 */
export interface ComponentDefinitionDocument extends OscalDocument {
    /** The root component-definition object. */
    component_definition: ComponentDefinition,
}


/**
 * A collection of component descriptions, which may optionally be grouped by capability.
 */
export interface ComponentDefinition {
    /** A machine-oriented, globally unique identifier with a cross-instance scope. */
    uuid: string,
    /** Provides information about the containing document, and defines concepts shared across the document. */
    metadata: Metadata,
    /** Component-definition resources imported into this document. */
    import_component_definitions?: ImportComponentDefinition[],
    /** A collection of system components. */
    components?: DefinedComponent[],
    /** Capability groupings for the defined components. */
    capabilities?: Capability[],
    /** A collection of resources that may be referenced from within the OSCAL document instance. */
    back_matter?: BackMatter,
}


/**
 * Loads a component definition from another resource.
 */
export interface ImportComponentDefinition {
    /** A resolvable URL reference to a resource. */
    href: string,
    /** Additional commentary about the containing object. */
    remarks?: string,
}


/**
 * A defined component that can be part of an implemented system.
 */
export interface DefinedComponent extends OscalCommon, HasResponsibleRoles {
    /** A machine-oriented, globally unique identifier with a cross-instance scope. */
    uuid: string,
    /** Indicates the nature or kind of the containing object. */
    type: string,
    /** A human-readable name or title. */
    title: string,
    /** A human-readable description. */
    description: string,
    /** A summary of the technological or business purpose of the component. */
    purpose?: string,
    /** Information about the protocol used to provide a service. */
    protocols?: Protocol[],
    /** Control implementation sets for a component or capability. */
    control_implementations?: ControlImplementationSet[],
}


/**
 * A grouping of other components and/or capabilities.
 */
export interface Capability extends OscalCommon {
    /** A machine-oriented, globally unique identifier with a cross-instance scope. */
    uuid: string,
    /** A textual label that uniquely identifies an attribute or semantic type. */
    name: string,
    /** A human-readable description. */
    description: string,
    /** Component references incorporated by a capability. */
    incorporates_components?: IncorporatesComponent[],
    /** Control implementation sets for a component or capability. */
    control_implementations?: ControlImplementationSet[],
}


/**
 * The collection of components comprising a capability.
 */
export interface IncorporatesComponent {
    /** A UUID reference to a component. */
    component_uuid: string,
    /** A human-readable description. */
    description: string,
}


/**
 * Defines how the component or capability supports a set of controls.
 */
export interface ControlImplementationSet extends HasPropsAndLinks {
    /** A machine-oriented, globally unique identifier with a cross-instance scope. */
    uuid: string,
    /** Reference to an external catalog or profile resource. */
    source: string,
    /** A human-readable description. */
    description: string,
    /** Parameter values applied in the containing implementation context. */
    set_parameters?: SetParameter[],
    /** Control implementation requirement entries in the containing OSCAL context. The concrete entry class is selected by class-level slot_usage. */
    implemented_requirements: ImplementedRequirement[],
}


/**
 * Describes how the containing component or capability implements an individual control.
 */
export interface ImplementedRequirement extends HasPropsAndLinks, HasResponsibleRoles {
    /** A machine-oriented, globally unique identifier with a cross-instance scope. */
    uuid: string,
    /** A reference to a control by its identifier. */
    control_id: string,
    /** A human-readable description. */
    description: string,
    /** Parameter values applied in the containing implementation context. */
    set_parameters?: SetParameter[],
    /** Control statement implementation entries in the containing OSCAL context. The concrete entry class is selected by class-level slot_usage. */
    statements?: ImplementedControlStatement[],
    /** Additional commentary about the containing object. */
    remarks?: string,
}


/**
 * Identifies which statements within a control are addressed.
 */
export interface ImplementedControlStatement extends HasPropsAndLinks, HasResponsibleRoles {
    /** A reference to a control statement identifier. */
    statement_id: string,
    /** A machine-oriented, globally unique identifier with a cross-instance scope. */
    uuid: string,
    /** A human-readable description. */
    description: string,
    /** Additional commentary about the containing object. */
    remarks?: string,
}


/**
 * Root wrapper for an OSCAL Mapping Collection document.
 */
export interface MappingCollectionDocument extends OscalDocument {
    /** The root mapping collection object. */
    mapping_collection: MappingCollection,
}


/**
 * A collection of control mappings between source and target resources.
 */
export interface MappingCollection {
    /** A machine-oriented, globally unique identifier with a cross-instance scope. */
    uuid: string,
    /** Provides information about the containing document, and defines concepts shared across the document. */
    metadata: Metadata,
    /** Global provenance and mapping method metadata. */
    provenance: MappingProvenance,
    /** A collection of control mappings. */
    mappings: Mapping[],
    /** A collection of resources that may be referenced from within the OSCAL document instance. */
    back_matter?: BackMatter,
}


/**
 * Mapping-level provenance details and mapping defaults.
 */
export interface MappingProvenance extends OscalCommon, HasResponsibleParties {
    /** Method indicator used by the containing OSCAL context. Allowed values are constrained by class-level slot_usage. */
    method: string,
    /** The rationale method used to relate mapped items. */
    matching_rationale: string,
    /** Status indicator used by the containing OSCAL context. Allowed values are constrained by class-level slot_usage. */
    status: string,
    /** Confidence descriptor for a mapping. */
    confidence_score?: ConfidenceScore,
    /** Coverage metadata for a mapping. */
    coverage?: Coverage,
    /** Description of the context and intended use of the mapping. */
    mapping_description: string,
}


/**
 * A mapping between two mapped resources.
 */
export interface Mapping extends OscalCommon {
    /** A machine-oriented, globally unique identifier with a cross-instance scope. */
    uuid: string,
    /** Method indicator used by the containing OSCAL context. Allowed values are constrained by class-level slot_usage. */
    method?: string,
    /** The rationale method used to relate mapped items. */
    matching_rationale?: string,
    /** Status indicator used by the containing OSCAL context. Allowed values are constrained by class-level slot_usage. */
    status?: string,
    /** Reference to the mapping source resource. */
    source_resource: MappingResourceReference,
    /** Reference to the mapping target resource. */
    target_resource: MappingResourceReference,
    /** Mapping entries relating source items to target items. */
    maps: Map[],
    /** Description of the context and intended use of the mapping. */
    mapping_description?: string,
    /** Summary of unmapped source controls. */
    source_gap_summary?: GapSummary,
    /** Summary of unmapped target controls. */
    target_gap_summary?: GapSummary,
    /** Confidence descriptor for a mapping. */
    confidence_score?: ConfidenceScore,
    /** Coverage metadata for a mapping. */
    coverage?: Coverage,
}


/**
 * A relationship-based mapping entry between source and target sets.
 */
export interface Map extends OscalCommon {
    /** A machine-oriented, globally unique identifier with a cross-instance scope. */
    uuid: string,
    /** An optional namespace qualifying a name. Allows different organizations to associate distinct semantics with the same name. */
    ns?: string,
    /** The rationale method used to relate mapped items. */
    matching_rationale?: string,
    /** Relationship type for a mapping entry. OSCAL namespace values are defined by RelationshipEnum. */
    relationship: string,
    /** Source references or source-participation entries in the containing OSCAL context. The concrete entry class is selected by class-level slot_usage. */
    sources: MappingItem[],
    /** Target subjects participating in a mapping entry. */
    targets: MappingItem[],
    /** Qualifier statements for a mapping entry. */
    qualifiers?: QualifierItem[],
    /** Confidence descriptor for a mapping. */
    confidence_score?: ConfidenceScore,
    /** Coverage metadata for a mapping. */
    coverage?: Coverage,
}


/**
 * A source or target item participating in a mapping entry.
 */
export interface MappingItem extends OscalCommon {
    /** Indicates the nature or kind of the containing object. */
    type: string,
    /** Identifier reference of a source/target subject. */
    id_ref: string,
}


/**
 * A reference to the source or target resource for a mapping.
 */
export interface MappingResourceReference extends OscalCommon {
    /** An optional namespace qualifying a name. Allows different organizations to associate distinct semantics with the same name. */
    ns?: string,
    /** The semantic type of the referenced resource. OSCAL defines catalog and profile, while locally defined values are also permitted. */
    type: string,
    /** A resolvable URL reference to a resource. */
    href: string,
}


/**
 * A qualifier describing requirements or incompatibilities.
 */
export interface QualifierItem {
    /** Subject to which the qualifier applies. */
    subject: string,
    /** Predicate describing qualifier semantics. */
    predicate: string,
    /** Confidence category label or qualifier category value. */
    category: string,
    /** A human-readable description. */
    description: string,
    /** Additional commentary about the containing object. */
    remarks?: string,
}


/**
 * A summary of controls that were not mapped.
 */
export interface GapSummary {
    /** A machine-oriented, globally unique identifier with a cross-instance scope. */
    uuid: string,
    /** Controls that remain unmapped. */
    unmapped_controls: SelectControlById[],
}


/**
 * Confidence represented as a category and/or percentage value.
 */
export interface ConfidenceScore {
    /** Confidence category label or qualifier category value. */
    category?: string,
    /** A decimal percentage value in the range 0 to 1. */
    percentage?: number,
}


/**
 * A percentage representing target coverage by source mappings.
 */
export interface Coverage {
    /** Method used to determine the coverage value. Recommended values are in CoverageGenerationMethodEnum; other values are permitted. */
    generation_method?: string,
    /** Percentage coverage of targets by sources. */
    target_coverage: number,
}


/**
 * Root wrapper for an OSCAL Plan of Action and Milestones document.
 */
export interface PoamDocument extends OscalDocument {
    /** The root plan of action and milestones object. */
    plan_of_action_and_milestones: PlanOfActionAndMilestones,
}


/**
 * A plan of action and milestones that identifies initial and residual risks, deviations, and disposition.
 */
export interface PlanOfActionAndMilestones {
    /** A machine-oriented, globally unique identifier with a cross-instance scope. */
    uuid: string,
    /** Provides information about the containing document, and defines concepts shared across the document. */
    metadata: Metadata,
    /** Used to import information about the system from an SSP. */
    import_ssp?: ImportSSP,
    /** A human-oriented, globally unique identifier for a system. */
    system_id?: SystemId,
    /** Used to define data objects that do not appear in the referenced SSP. */
    local_definitions?: PoamLocalDefinitions,
    /** A collection of observations captured in the containing context. */
    observations?: Observation[],
    /** A collection of risks captured in the containing context. */
    risks?: Risk[],
    /** A collection of findings captured in the containing context. */
    findings?: Finding[],
    /** A collection of POA&M items. */
    poam_items: PoamItem[],
    /** A collection of resources that may be referenced from within the OSCAL document instance. */
    back_matter?: BackMatter,
}


/**
 * Allows components and inventory items to be defined within the POA&M for cases where no OSCAL SSP is available with the POA&M.
 */
export interface PoamLocalDefinitions {
    /** A collection of system components. */
    components?: SystemComponent[],
    /** A collection of inventory items. */
    inventory_items?: InventoryItem[],
    /** Identifies the assets used to perform this assessment. */
    assessment_assets?: AssessmentAssets,
    /** Additional commentary about the containing object. */
    remarks?: string,
}


/**
 * Describes an individual POA&M item.
 */
export interface PoamItem extends OscalCommon {
    /** A machine-oriented, globally unique identifier with a cross-instance scope. */
    uuid?: string,
    /** A human-readable name or title. */
    title: string,
    /** A human-readable description. */
    description: string,
    /** Identifies the source of observations, findings, or risks. */
    origins?: Origin[],
    /** Relates a POA&M item to one or more findings. */
    related_findings?: RelatedFinding[],
    /** Relates the containing object to a set of referenced observations. */
    related_observations?: RelatedObservation[],
    /** Relates the finding to a set of referenced risks. */
    related_risks?: AssociatedRisk[],
}


/**
 * Relates a POA&M item to a referenced finding.
 */
export interface RelatedFinding {
    /** A UUID reference to a finding. */
    finding_uuid: string,
    /** Additional commentary about the containing object. */
    remarks?: string,
}



