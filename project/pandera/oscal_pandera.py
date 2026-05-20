import pandera.polars as pla
from pandera.api.polars.types import PolarsData
from . import panderagen_polars_schema as pa_pl
import polars as pl
from typing import Optional


from pandera.typing import (
    Index,
    DataFrame,
    Series
)
from pandera.engines.polars_engine import (
    DateTime,
    Date,
    Time,
    Enum,
    Struct,
    List,
    Object
)


from linkml.generators.panderagen.linkml_pandera_validator import LinkmlPanderaValidator as _LinkmlPanderaValidator


# These are all str for now
ID_TYPES = {
    "Property": "str",
    "Link": "str",
    "HasPropsAndLinks": "str",
    "OscalCommon": "str",
    "ResponsibleRole": "str",
    "HasResponsibleRoles": "str",
    "ResponsibleParty": "str",
    "HasResponsibleParties": "str",
    "DocumentId": "str",
    "RevisionProperty": "str",
    "Revision": "str",
    "Role": "str",
    "TelephoneNumber": "str",
    "Address": "str",
    "LocationProperty": "str",
    "Location": "str",
    "PartyExternalId": "str",
    "MetadataPartyExternalId": "str",
    "PartyProperty": "str",
    "Party": "str",
    "Action": "str",
    "MetadataProperty": "str",
    "Metadata": "str",
    "ResourceProperty": "str",
    "Citation": "str",
    "Hash": "str",
    "ResourceLink": "str",
    "Base64Resource": "str",
    "Resource": "str",
    "BackMatter": "str",
    "ConstraintTest": "str",
    "ParameterConstraint": "str",
    "ParameterGuideline": "str",
    "ParameterSelection": "str",
    "ParameterProperty": "str",
    "Parameter": "str",
    "PartProperty": "str",
    "Part": "str",
    "Control": "str",
    "Group": "str",
    "Catalog": "str",
    "OscalDocument": "str",
    "CatalogDocument": "str",
    "ControlMatching": "str",
    "SelectControlById": "str",
    "IncludeAll": "str",
    "ProfileImport": "str",
    "CombinationRule": "str",
    "MergeFlat": "str",
    "InsertControls": "str",
    "ProfileGroup": "str",
    "MergeCustom": "str",
    "ProfileMerge": "str",
    "ParameterSetting": "str",
    "Removal": "str",
    "ProfileAlterationProperty": "str",
    "Addition": "str",
    "Alteration": "str",
    "ProfileModify": "str",
    "Profile": "str",
    "ProfileDocument": "str",
    "ImportSSP": "str",
    "PortRange": "str",
    "Protocol": "str",
    "ComponentStatus": "str",
    "ImplementationResponsibleRole": "str",
    "ImplementationCommonProperty": "str",
    "ImplementationCommonLink": "str",
    "SystemComponent": "str",
    "ImplementationResponsibleParty": "str",
    "ImplementedComponent": "str",
    "InventoryItem": "str",
    "AuthorizedPrivilege": "str",
    "SystemUser": "str",
    "ControlPart": "str",
    "LocalObjective": "str",
    "AssessmentSelectControlById": "str",
    "ControlSelection": "str",
    "SelectObjectiveById": "str",
    "ControlObjectiveSelection": "str",
    "ReviewedControls": "str",
    "Step": "str",
    "Activity": "str",
    "LocalDefinitions": "str",
    "AssessmentPart": "str",
    "TermsAndConditionsPart": "str",
    "TermsAndConditions": "str",
    "SelectSubjectById": "str",
    "AssessmentSubject": "str",
    "UsesComponent": "str",
    "AssessmentPlatform": "str",
    "AssessmentAssets": "str",
    "OnDateCondition": "str",
    "WithinDateRange": "str",
    "AtFrequency": "str",
    "EventTiming": "str",
    "TaskDependency": "str",
    "AssociatedActivity": "str",
    "Task": "str",
    "AssessmentPlan": "str",
    "AssessmentPlanDocument": "str",
    "SubjectReference": "str",
    "AssessmentSubjectSource": "str",
    "AssessmentSubjectPlaceholder": "str",
    "AssessmentMethod": "str",
    "OriginActor": "str",
    "IdentifiedSubject": "str",
    "RelatedTask": "str",
    "Origin": "str",
    "RelevantEvidence": "str",
    "Observation": "str",
    "ImplementationStatus": "str",
    "ObjectiveStatus": "str",
    "FindingTarget": "str",
    "RelatedObservation": "str",
    "AssociatedRisk": "str",
    "Finding": "str",
    "ThreatId": "str",
    "Facet": "str",
    "Characterization": "str",
    "MitigatingFactor": "str",
    "RequiredAsset": "str",
    "Response": "str",
    "LoggedBy": "str",
    "RiskResponseReference": "str",
    "RiskLogEntry": "str",
    "RiskLog": "str",
    "Risk": "str",
    "ImportProfile": "str",
    "SystemId": "str",
    "SspSystemInformationProp": "str",
    "SspSystemInformationLink": "str",
    "InformationTypeCategorization": "str",
    "ImpactLevel": "str",
    "InformationType": "str",
    "SystemInformation": "str",
    "SecurityImpactLevel": "str",
    "SystemStatus": "str",
    "SspDiagramLink": "str",
    "Diagram": "str",
    "AuthorizationBoundary": "str",
    "NetworkArchitecture": "str",
    "DataFlow": "str",
    "SspSystemCharacteristicsResponsibleParty": "str",
    "SystemCharacteristics": "str",
    "SspLeveragedAuthorizationLink": "str",
    "LeveragedAuthorization": "str",
    "SspAllowsAuthenticatedScanProp": "str",
    "SspSystemComponent": "str",
    "SspInventoryItem": "str",
    "SystemImplementation": "str",
    "SetParameter": "str",
    "SspControlOriginationProp": "str",
    "SspImplementedRequirementResponsibleRole": "str",
    "SspByComponentLink": "str",
    "SspByComponentResponsibleRole": "str",
    "ProvidedControlImplementation": "str",
    "ControlResponsibility": "str",
    "Export": "str",
    "InheritedControlImplementation": "str",
    "SatisfiedControlImplementation": "str",
    "ByComponent": "str",
    "SspStatement": "str",
    "SspImplementedRequirement": "str",
    "SspControlImplementation": "str",
    "SystemSecurityPlan": "str",
    "SspDocument": "str",
    "ImportAssessmentPlan": "str",
    "AssessmentResultsLocalDefinitions": "str",
    "ResultLocalDefinitions": "str",
    "Attestation": "str",
    "AssessmentLogEntry": "str",
    "AssessmentLog": "str",
    "Result": "str",
    "AssessmentResults": "str",
    "AssessmentResultsDocument": "str",
    "ImportComponentDefinition": "str",
    "ImplementedControlStatement": "str",
    "ImplementedRequirement": "str",
    "ControlImplementationSet": "str",
    "DefinedComponent": "str",
    "IncorporatesComponent": "str",
    "Capability": "str",
    "ComponentDefinition": "str",
    "ComponentDefinitionDocument": "str",
    "ConfidenceScore": "str",
    "Coverage": "str",
    "MappingProvenance": "str",
    "MappingResourceReference": "str",
    "MappingItem": "str",
    "QualifierItem": "str",
    "Map": "str",
    "GapSummary": "str",
    "Mapping": "str",
    "MappingCollection": "str",
    "MappingCollectionDocument": "str",
    "PoamLocalDefinitions": "str",
    "RelatedFinding": "str",
    "PoamItem": "str",
    "PlanOfActionAndMilestones": "str",
    "PoamDocument": "str",
    "SspSystemCharacteristicsProp": "str",
}

# metamodel_version: 1.11.0
# version: 1.2.1class Property(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    An attribute, characteristic, or quality of the containing object expressed as a namespace qualified name/value pair.
    """

    _id_name : str = None
    name: str = pla.Field()
    """
    A textual label, within a namespace, that identifies a specific attribute, characteristic, or quality of the property's containing object.
    """
    
    uuid: Optional[str] = pla.Field(nullable=True, )
    """
    A unique identifier for a property.
    """
    
    ns: Optional[str] = pla.Field(nullable=True, )
    """
    A namespace qualifying the property's name. This allows different organizations to associate distinct semantics with the same name.
    """
    
    value: str = pla.Field()
    """
    Indicates the value of the attribute, characteristic, or quality.
    """
    
    _class: Optional[str] = pla.Field(nullable=True, )
    """
    A textual label that provides a sub-type or characterization of the property's name.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    group: Optional[str] = pla.Field(nullable=True, )
    """
    An identifier for relating distinct sets of properties.
    """
    
    
class Link(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A reference to a local or remote resource, that has a specific relation to the containing object.
    """

    _id_name : str = None
    href: str = pla.Field()
    """
    A resolvable URL reference to a resource.
    """
    
    rel: Optional[str] = pla.Field(nullable=True, )
    """
    Describes the type of relationship provided by the link's hypertext reference. This can be an indicator of the link's purpose.
    """
    
    resource_fragment: Optional[str] = pla.Field(nullable=True, )
    """
    In case where the href points to a back-matter/resource, this value will indicate the URI fragment to append to any rlink associated with the resource. This value MUST be URI encoded.
    """
    
    media_type: Optional[str] = pla.Field(nullable=True, )
    """
    A label that indicates the nature of a resource, as a data serialization or format.
    """
    
    text: Optional[str] = pla.Field(nullable=True, )
    """
    A textual label to associate with the containing object.
    """
    
    
class HasPropsAndLinks(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Mixin providing the props and links slots that are common to many OSCAL objects.
    """

    _id_name : str = None
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Property, pa_pl.PropertyDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Link, pa_pl.LinkDict)
        
class OscalCommon(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Mixin providing props, links, and remarks slots common to most OSCAL objects. Extends HasPropsAndLinks.
    """

    _id_name : str = None
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Property, pa_pl.PropertyDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Link, pa_pl.LinkDict)
        
class ResponsibleRole(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A reference to a role with responsibility for performing a function relative to the containing object, optionally associated with a set of persons and/or organizations that perform that role.
    """

    _id_name : str = None
    role_id: str = pla.Field()
    """
    A human-oriented identifier reference to a role performed.
    """
    
    party_uuids: Optional[str] = pla.Field(nullable=True, )
    """
    References to party UUIDs.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Property, pa_pl.PropertyDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Link, pa_pl.LinkDict)
        
class HasResponsibleRoles(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Mixin providing the responsible-roles slot for objects that carry role assignments.
    """

    _id_name : str = None
    responsible_roles: Optional[List] = pla.Field(nullable=True, )
    """
    Responsible role assignments.
    """
    
    
    @pla.check("responsible_roles")
    def check_nested_struct_responsible_roles(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, ResponsibleRole, pa_pl.ResponsibleRoleDict)
        
class ResponsibleParty(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A reference to a set of persons and/or organizations that have responsibility for performing the referenced role in the context of the containing object.
    """

    _id_name : str = None
    role_id: str = pla.Field()
    """
    A reference to a role performed by a party.
    """
    
    party_uuids: str = pla.Field()
    """
    References to party UUIDs.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Property, pa_pl.PropertyDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Link, pa_pl.LinkDict)
        
class HasResponsibleParties(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Mixin providing the responsible-parties slot for objects that carry party assignments.
    """

    _id_name : str = None
    responsible_parties: Optional[List] = pla.Field(nullable=True, )
    """
    Responsible party assignments.
    """
    
    
    @pla.check("responsible_parties")
    def check_nested_struct_responsible_parties(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, ResponsibleParty, pa_pl.ResponsiblePartyDict)
        
class DocumentId(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A document identifier qualified by an identifier scheme.
    """

    _id_name : str = None
    scheme: Optional[str] = pla.Field(nullable=True, )
    """
    Qualifies the kind of identifier using a URI.
    """
    
    identifier: str = pla.Field()
    """
    A document identifier value.
    """
    
    
class RevisionProperty(Property):
    """
    Revision-scoped OSCAL property.
    """

    _id_name : str = None
    pass
    
    
class Revision(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    An entry in a sequential list of revisions to the containing document.
    """

    _id_name : str = None
    title: Optional[str] = pla.Field(nullable=True, )
    """
    A human-readable name or title.
    """
    
    published: Optional[DateTime()] = pla.Field(nullable=True, )
    """
    The date and time the document was last made available.
    """
    
    last_modified: Optional[DateTime()] = pla.Field(nullable=True, )
    """
    The date and time the document was last modified.
    """
    
    version: str = pla.Field()
    """
    Used to distinguish a specific revision of an OSCAL document from other previous and future versions.
    """
    
    oscal_version: Optional[str] = pla.Field(nullable=True, )
    """
    The OSCAL model version the document was authored against and will conform to as valid.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, RevisionProperty, pa_pl.RevisionPropertyDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Link, pa_pl.LinkDict)
        
class Role(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Defines a function, which might be assigned to a party in a specific situation.
    """

    _id_name : str = None
    id: str = pla.Field()
    """
    A unique identifier for the role.
    """
    
    title: str = pla.Field()
    """
    A human-readable name or title.
    """
    
    short_name: Optional[str] = pla.Field(nullable=True, )
    """
    A short common name, abbreviation, or acronym.
    """
    
    description: Optional[str] = pla.Field(nullable=True, )
    """
    A human-readable description.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Property, pa_pl.PropertyDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Link, pa_pl.LinkDict)
        
class TelephoneNumber(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A telephone service number as defined by ITU-T E.164.
    """

    _id_name : str = None
    type: Optional[str] = pla.Field(nullable=True, )
    """
    Indicates the type of phone number. Recommended values: home, office, mobile. Other values are permitted (OSCAL allow-other="yes").
    """
    
    number: str = pla.Field()
    """
    A telephone number value.
    """
    
    
class Address(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A postal address for the location.
    """

    _id_name : str = None
    type: Optional[str] = pla.Field(nullable=True, )
    """
    Indicates the type of address. Recommended values: home, work. Other values are permitted (OSCAL allow-other="yes").
    """
    
    addr_lines: Optional[str] = pla.Field(nullable=True, )
    """
    A single line of an address.
    """
    
    city: Optional[str] = pla.Field(nullable=True, )
    """
    City, town or geographical region for the mailing address.
    """
    
    state: Optional[str] = pla.Field(nullable=True, )
    """
    State, province or analogous geographical region for a mailing address.
    """
    
    postal_code: Optional[str] = pla.Field(nullable=True, )
    """
    Postal or ZIP code for mailing address.
    """
    
    country: Optional[str] = pla.Field(nullable=True, )
    """
    The ISO 3166-1 alpha-2 country code for the mailing address.
    """
    
    
class LocationProperty(Property):
    """
    Location-scoped OSCAL property.
    """

    _id_name : str = None
    pass
    
    
class Location(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A physical point of presence, which may be associated with people, organizations, or other concepts within the current or linked OSCAL document.
    """

    _id_name : str = None
    uuid: str = pla.Field()
    """
    A machine-oriented, globally unique identifier with a cross-instance scope.
    """
    
    title: Optional[str] = pla.Field(nullable=True, )
    """
    A human-readable name or title.
    """
    
    email_addresses: Optional[str] = pla.Field(nullable=True, )
    """
    Email addresses associated with the containing object.
    """
    
    telephone_numbers: Optional[List] = pla.Field(nullable=True, )
    """
    Telephone numbers associated with the containing object.
    """
    
    address: Optional[Struct] = pla.Field(nullable=True, )
    """
    A postal address for the location.
    """
    
    urls: Optional[str] = pla.Field(nullable=True, )
    """
    The uniform resource locator (URL) for a web site or other resource associated with the location.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    
    @pla.check("telephone_numbers")
    def check_nested_struct_telephone_numbers(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, TelephoneNumber, pa_pl.TelephoneNumberDict)
        
    @pla.check("address")
    def check_nested_struct_address(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, Address, pa_pl.Address)
        
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, LocationProperty, pa_pl.LocationPropertyDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Link, pa_pl.LinkDict)
        
class PartyExternalId(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    An identifier for a person or organization using a designated scheme, e.g. an Open Researcher and Contributor ID (ORCID).
    """

    _id_name : str = None
    scheme: str = pla.Field()
    """
    Indicates the type of external identifier.
    """
    
    id: str = pla.Field()
    """
    A unique human-oriented identifier within a particular context.
    """
    
    
class MetadataPartyExternalId(PartyExternalId):
    """
    Metadata-scoped external identifier.
    """

    _id_name : str = None
    pass
    
    
class PartyProperty(Property):
    """
    Party-scoped OSCAL property.
    """

    _id_name : str = None
    pass
    
    
class Party(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    An organization or person, which may be associated with roles or other concepts within the current or linked OSCAL document.
    """

    _id_name : str = None
    uuid: str = pla.Field()
    """
    A machine-oriented, globally unique identifier with a cross-instance scope.
    """
    
    type: Enum = pla.Field(dtype_kwargs={"categories":('person','organization',)})
    """
    A category describing the kind of party the object describes.
    """
    
    name: Optional[str] = pla.Field(nullable=True, )
    """
    The full name of the party.
    """
    
    short_name: Optional[str] = pla.Field(nullable=True, )
    """
    A short common name, abbreviation, or acronym.
    """
    
    email_addresses: Optional[str] = pla.Field(nullable=True, )
    """
    Email addresses associated with the containing object.
    """
    
    telephone_numbers: Optional[List] = pla.Field(nullable=True, )
    """
    Telephone numbers associated with the containing object.
    """
    
    external_ids: Optional[List] = pla.Field(nullable=True, )
    """
    An identifier for a person or organization using a designated scheme, e.g. an Open Researcher and Contributor ID (ORCID).
    """
    
    addresses: Optional[List] = pla.Field(nullable=True, )
    """
    Postal addresses associated with the containing object.
    """
    
    location_uuids: Optional[str] = pla.Field(nullable=True, )
    """
    Reference to a location by UUID.
    """
    
    member_of_organizations: Optional[str] = pla.Field(nullable=True, )
    """
    A reference to another party by UUID, typically an organization, that this subject is associated with.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    
    @pla.check("telephone_numbers")
    def check_nested_struct_telephone_numbers(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, TelephoneNumber, pa_pl.TelephoneNumberDict)
        
    @pla.check("external_ids")
    def check_nested_struct_external_ids(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, MetadataPartyExternalId, pa_pl.MetadataPartyExternalIdDict)
        
    @pla.check("addresses")
    def check_nested_struct_addresses(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Address, pa_pl.AddressDict)
        
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, PartyProperty, pa_pl.PartyPropertyDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Link, pa_pl.LinkDict)
        
class Action(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    An action applied by a role within a given party to the content.
    """

    _id_name : str = None
    uuid: str = pla.Field()
    """
    A unique identifier that can be used to reference this defined action elsewhere in an OSCAL document.
    """
    
    type: Enum = pla.Field(dtype_kwargs={"categories":('approval','request-changes',)})
    """
    The type of action documented by the assembly, such as an approval.
    """
    
    date: Optional[DateTime()] = pla.Field(nullable=True, )
    """
    The date and time when the action occurred.
    """
    
    system: str = pla.Field()
    """
    Specifies the action type system used.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    responsible_parties: Optional[List] = pla.Field(nullable=True, )
    """
    Responsible party assignments.
    """
    
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    
    @pla.check("responsible_parties")
    def check_nested_struct_responsible_parties(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, ResponsibleParty, pa_pl.ResponsiblePartyDict)
        
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Property, pa_pl.PropertyDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Link, pa_pl.LinkDict)
        
class MetadataProperty(Property):
    """
    Metadata-scoped OSCAL property.
    """

    _id_name : str = None
    pass
    
    
class Metadata(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Provides information about the containing document, and defines concepts shared across the document.
    """

    _id_name : str = None
    title: str = pla.Field()
    """
    A name given to the document.
    """
    
    published: Optional[DateTime()] = pla.Field(nullable=True, )
    """
    The date and time the document was last made available.
    """
    
    last_modified: DateTime() = pla.Field()
    """
    The date and time the document was last stored for later retrieval.
    """
    
    version: str = pla.Field()
    """
    Used to distinguish a specific revision of an OSCAL document.
    """
    
    oscal_version: str = pla.Field()
    """
    The OSCAL model version the document was authored against.
    """
    
    document_ids: Optional[List] = pla.Field(nullable=True, )
    """
    Document identifiers qualified by an identifier scheme.
    """
    
    revisions: Optional[List] = pla.Field(nullable=True, )
    """
    An entry in a sequential list of revisions to the containing document, expected to be in reverse chronological order (i.e. latest first).
    """
    
    roles: Optional[List] = pla.Field(nullable=True, )
    """
    Defines a function, which might be assigned to a party in a specific situation.
    """
    
    locations: Optional[List] = pla.Field(nullable=True, )
    """
    A physical point of presence, which may be associated with people, organizations, or other concepts within the current or linked OSCAL document.
    """
    
    parties: Optional[List] = pla.Field(nullable=True, )
    """
    An organization or person, which may be associated with roles or other concepts within the current or linked OSCAL document.
    """
    
    actions: Optional[List] = pla.Field(nullable=True, )
    """
    An action applied by a role within a given party to the content.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    responsible_parties: Optional[List] = pla.Field(nullable=True, )
    """
    Responsible party assignments.
    """
    
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    
    @pla.check("document_ids")
    def check_nested_struct_document_ids(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, DocumentId, pa_pl.DocumentIdDict)
        
    @pla.check("revisions")
    def check_nested_struct_revisions(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Revision, pa_pl.RevisionDict)
        
    @pla.check("roles")
    def check_nested_struct_roles(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Role, pa_pl.RoleDict)
        
    @pla.check("locations")
    def check_nested_struct_locations(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Location, pa_pl.LocationDict)
        
    @pla.check("parties")
    def check_nested_struct_parties(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Party, pa_pl.PartyDict)
        
    @pla.check("actions")
    def check_nested_struct_actions(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Action, pa_pl.ActionDict)
        
    @pla.check("responsible_parties")
    def check_nested_struct_responsible_parties(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, ResponsibleParty, pa_pl.ResponsiblePartyDict)
        
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, MetadataProperty, pa_pl.MetadataPropertyDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Link, pa_pl.LinkDict)
        
class ResourceProperty(Property):
    """
    Back-matter resource-scoped OSCAL property.
    """

    _id_name : str = None
    pass
    
    
class Citation(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    An optional citation consisting of end note text using structured markup.
    """

    _id_name : str = None
    text: str = pla.Field()
    """
    A line of citation text.
    """
    
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Property, pa_pl.PropertyDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Link, pa_pl.LinkDict)
        
class Hash(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A representation of a cryptographic digest generated over a resource using a specified hash algorithm.
    """

    _id_name : str = None
    value: str = pla.Field()
    """
    The value associated with the containing object.
    """
    
    algorithm: str = pla.Field()
    """
    The digest method by which a hash is derived. Recommended values are in HashAlgorithmEnum; other values are permitted (OSCAL allow-other="yes").
    """
    
    
class ResourceLink(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A URL-based pointer to an external resource with an optional hash for verification and change detection.
    """

    _id_name : str = None
    href: str = pla.Field()
    """
    A resolvable URL pointing to the referenced resource.
    """
    
    media_type: Optional[str] = pla.Field(nullable=True, )
    """
    A label that indicates the nature of a resource, as a data serialization or format.
    """
    
    hashes: Optional[List] = pla.Field(nullable=True, )
    """
    A representation of a cryptographic digest generated over a resource using a specified hash algorithm.
    """
    
    
    @pla.check("hashes")
    def check_nested_struct_hashes(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Hash, pa_pl.HashDict)
        
class Base64Resource(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A resource encoded using the Base64 alphabet defined by RFC 2045.
    """

    _id_name : str = None
    media_type: Optional[str] = pla.Field(nullable=True, )
    """
    A label that indicates the nature of a resource, as a data serialization or format.
    """
    
    value: str = pla.Field()
    """
    The value associated with the containing object.
    """
    
    filename: Optional[str] = pla.Field(nullable=True, )
    """
    Name of the file before it was encoded as Base64 to be embedded in a resource.
    """
    
    
class Resource(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A resource associated with content in the containing document instance. A resource may be directly included in the document using base64 encoding or may point to one or more equivalent internet resources.
    """

    _id_name : str = None
    uuid: str = pla.Field()
    """
    A unique identifier for a resource.
    """
    
    title: Optional[str] = pla.Field(nullable=True, )
    """
    An optional name given to the resource, which may be used by a tool for display and navigation.
    """
    
    description: Optional[str] = pla.Field(nullable=True, )
    """
    An optional short summary of the resource used to indicate the purpose of the resource.
    """
    
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    document_ids: Optional[List] = pla.Field(nullable=True, )
    """
    Document identifiers qualified by an identifier scheme.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    citation: Optional[Struct] = pla.Field(nullable=True, )
    """
    An optional citation consisting of end note text using structured markup.
    """
    
    rlinks: Optional[List] = pla.Field(nullable=True, )
    """
    A URL-based pointer to an external resource with an optional hash for verification and change detection.
    """
    
    base64: Optional[Struct] = pla.Field(nullable=True, )
    """
    A resource encoded using the Base64 alphabet defined by RFC 2045.
    """
    
    
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, ResourceProperty, pa_pl.ResourcePropertyDict)
        
    @pla.check("document_ids")
    def check_nested_struct_document_ids(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, DocumentId, pa_pl.DocumentIdDict)
        
    @pla.check("citation")
    def check_nested_struct_citation(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, Citation, pa_pl.Citation)
        
    @pla.check("rlinks")
    def check_nested_struct_rlinks(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, ResourceLink, pa_pl.ResourceLinkDict)
        
    @pla.check("base64")
    def check_nested_struct_base64(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, Base64Resource, pa_pl.Base64Resource)
        
class BackMatter(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A collection of resources that may be referenced from within the OSCAL document instance.
    """

    _id_name : str = None
    resources: Optional[List] = pla.Field(nullable=True, )
    """
    A resource associated with content in the containing document instance. A resource may be directly included in the document using base64 encoding or may point to one or more equivalent internet resources.
    """
    
    
    @pla.check("resources")
    def check_nested_struct_resources(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Resource, pa_pl.ResourceDict)
        
class ConstraintTest(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A test expression which is expected to be evaluated by a tool.
    """

    _id_name : str = None
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    expression: str = pla.Field()
    """
    A formal (executable) expression of a constraint.
    """
    
    
class ParameterConstraint(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A formal or informal expression of a constraint or test.
    """

    _id_name : str = None
    description: Optional[str] = pla.Field(nullable=True, )
    """
    A textual summary of the constraint to be applied.
    """
    
    tests: Optional[List] = pla.Field(nullable=True, )
    """
    A test expression which is expected to be evaluated by a tool.
    """
    
    
    @pla.check("tests")
    def check_nested_struct_tests(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, ConstraintTest, pa_pl.ConstraintTestDict)
        
class ParameterGuideline(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A prose statement that provides a recommendation for the use of a parameter.
    """

    _id_name : str = None
    prose: str = pla.Field()
    """
    Prose permits multiple paragraphs, lists, tables etc.
    """
    
    
class ParameterSelection(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Presenting a choice among alternatives.
    """

    _id_name : str = None
    how_many: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('one','one-or-more',)})
    """
    Describes the number of selections that must occur. Without this setting, only one value should be assumed to be permitted.
    """
    
    choice: Optional[str] = pla.Field(nullable=True, )
    """
    A value selection among several such options.
    """
    
    
class ParameterProperty(Property):
    """
    Control-common parameter-scoped OSCAL property.
    """

    _id_name : str = None
    pass
    
    
class Parameter(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Parameters provide a mechanism for the dynamic assignment of value(s) in a control.
    """

    _id_name : str = None
    id: str = pla.Field()
    """
    A unique identifier for the parameter.
    """
    
    _class: Optional[str] = pla.Field(nullable=True, )
    """
    A textual label that provides a characterization of the type, purpose, use or scope of the parameter.
    """
    
    depends_on: Optional[str] = pla.Field(nullable=True, )
    """
    (deprecated) Another parameter invoking this one. This construct has been deprecated and should not be used.
    """
    
    label: Optional[str] = pla.Field(nullable=True, )
    """
    A short, placeholder name for the parameter, which can be used as a substitute for a value if no value is assigned.
    """
    
    usage: Optional[str] = pla.Field(nullable=True, )
    """
    Describes the purpose and use of a parameter.
    """
    
    constraints: Optional[List] = pla.Field(nullable=True, )
    """
    A formal or informal expression of a constraint or test.
    """
    
    guidelines: Optional[List] = pla.Field(nullable=True, )
    """
    A prose statement that provides a recommendation for the use of a parameter.
    """
    
    values: Optional[str] = pla.Field(nullable=True, )
    """
    A parameter value or set of values.
    """
    
    select: Optional[Struct] = pla.Field(nullable=True, )
    """
    Presenting a choice among alternatives.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    
    @pla.check("constraints")
    def check_nested_struct_constraints(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, ParameterConstraint, pa_pl.ParameterConstraintDict)
        
    @pla.check("guidelines")
    def check_nested_struct_guidelines(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, ParameterGuideline, pa_pl.ParameterGuidelineDict)
        
    @pla.check("select")
    def check_nested_struct_select(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, ParameterSelection, pa_pl.ParameterSelection)
        
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, ParameterProperty, pa_pl.ParameterPropertyDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Link, pa_pl.LinkDict)
        
class PartProperty(Property):
    """
    Control-common part-scoped OSCAL property.
    """

    _id_name : str = None
    pass
    
    
class Part(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    An annotated, markup-based textual element of a control's or catalog group's definition, or a child of another part.
    """

    _id_name : str = None
    id: Optional[str] = pla.Field(nullable=True, )
    """
    A unique identifier for the part.
    """
    
    name: str = pla.Field()
    """
    A textual label that uniquely identifies the part's semantic type, which exists in a value space qualified by the ns.
    """
    
    ns: Optional[str] = pla.Field(nullable=True, )
    """
    An optional namespace qualifying the part's name. This allows different organizations to associate distinct semantics with the same name.
    """
    
    _class: Optional[str] = pla.Field(nullable=True, )
    """
    An optional textual providing a sub-type or characterization of the part's name, or a category to which the part belongs.
    """
    
    title: Optional[str] = pla.Field(nullable=True, )
    """
    An optional name given to the part, which may be used by a tool for display and navigation.
    """
    
    prose: Optional[str] = pla.Field(nullable=True, )
    """
    Permits multiple paragraphs, lists, tables etc.
    """
    
    parts: Optional[List] = pla.Field(nullable=True, )
    """
    A collection of parts.
    """
    
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    
    @pla.check("parts")
    def check_nested_struct_parts(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Part, pa_pl.PartDict)
        
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, PartProperty, pa_pl.PartPropertyDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Link, pa_pl.LinkDict)
        
class Control(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A structured object representing a requirement or guideline, which when implemented will reduce an aspect of risk related to an information system and its information.
    """

    _id_name : str = None
    id: str = pla.Field()
    """
    Identifies a control such that it can be referenced in the defining catalog and other OSCAL instances (e.g., profiles).
    """
    
    _class: Optional[str] = pla.Field(nullable=True, )
    """
    A textual label that provides a sub-type or characterization of the control.
    """
    
    title: str = pla.Field()
    """
    A name given to the control, which may be used by a tool for display and navigation.
    """
    
    params: Optional[List] = pla.Field(nullable=True, )
    """
    Parameters providing a mechanism for the dynamic assignment of value(s) in a control.
    """
    
    parts: Optional[List] = pla.Field(nullable=True, )
    """
    A collection of parts.
    """
    
    controls: Optional[List] = pla.Field(nullable=True, )
    """
    A collection of controls.
    """
    
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    
    @pla.check("params")
    def check_nested_struct_params(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Parameter, pa_pl.ParameterDict)
        
    @pla.check("parts")
    def check_nested_struct_parts(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Part, pa_pl.PartDict)
        
    @pla.check("controls")
    def check_nested_struct_controls(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Control, pa_pl.ControlDict)
        
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Property, pa_pl.PropertyDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Link, pa_pl.LinkDict)
        
class Group(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A group of controls, or of groups of controls.
    """

    _id_name : str = None
    id: Optional[str] = pla.Field(nullable=True, )
    """
    Identifies the group for the purpose of cross-linking within the defining instance or from other instances that reference the catalog.
    """
    
    _class: Optional[str] = pla.Field(nullable=True, )
    """
    A textual label that provides a sub-type or characterization of the group.
    """
    
    title: str = pla.Field()
    """
    A name given to the group, which may be used by a tool for display and navigation.
    """
    
    params: Optional[List] = pla.Field(nullable=True, )
    """
    Parameters providing a mechanism for the dynamic assignment of value(s) in a control.
    """
    
    parts: Optional[List] = pla.Field(nullable=True, )
    """
    A collection of parts.
    """
    
    groups: Optional[List] = pla.Field(nullable=True, )
    """
    A collection of control groups.
    """
    
    controls: Optional[List] = pla.Field(nullable=True, )
    """
    A collection of controls.
    """
    
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    
    @pla.check("params")
    def check_nested_struct_params(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Parameter, pa_pl.ParameterDict)
        
    @pla.check("parts")
    def check_nested_struct_parts(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Part, pa_pl.PartDict)
        
    @pla.check("groups")
    def check_nested_struct_groups(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Group, pa_pl.GroupDict)
        
    @pla.check("controls")
    def check_nested_struct_controls(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Control, pa_pl.ControlDict)
        
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Property, pa_pl.PropertyDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Link, pa_pl.LinkDict)
        
class Catalog(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A structured, organized collection of control information.
    """

    _id_name : str = None
    uuid: str = pla.Field()
    """
    Provides a globally unique means to identify a given catalog instance.
    """
    
    metadata: Struct = pla.Field()
    """
    Provides information about the containing document, and defines concepts shared across the document.
    """
    
    back_matter: Optional[Struct] = pla.Field(nullable=True, )
    """
    A collection of resources that may be referenced from within the OSCAL document instance.
    """
    
    params: Optional[List] = pla.Field(nullable=True, )
    """
    Parameters providing a mechanism for the dynamic assignment of value(s) in a control.
    """
    
    controls: Optional[List] = pla.Field(nullable=True, )
    """
    A collection of controls.
    """
    
    groups: Optional[List] = pla.Field(nullable=True, )
    """
    A collection of control groups.
    """
    
    
    @pla.check("metadata")
    def check_nested_struct_metadata(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, Metadata, pa_pl.Metadata)
        
    @pla.check("back_matter")
    def check_nested_struct_back_matter(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, BackMatter, pa_pl.BackMatter)
        
    @pla.check("params")
    def check_nested_struct_params(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Parameter, pa_pl.ParameterDict)
        
    @pla.check("controls")
    def check_nested_struct_controls(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Control, pa_pl.ControlDict)
        
    @pla.check("groups")
    def check_nested_struct_groups(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Group, pa_pl.GroupDict)
        
class OscalDocument(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A root wrapper for an OSCAL document, which may be of any OSCAL document type (e.g. Catalog, Profile, Assessment Plan, SSP).
    """

    _id_name : str = None
    pass
    
    
class CatalogDocument(OscalDocument):
    """
    Root wrapper for an OSCAL Catalog document.
    """

    _id_name : str = None
    catalog: Struct = pla.Field()
    """
    Root catalog document.
    """
    
    
    @pla.check("catalog")
    def check_nested_struct_catalog(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, Catalog, pa_pl.Catalog)
        
class ControlMatching(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Selecting a set of controls by matching their IDs with a wildcard pattern.
    """

    _id_name : str = None
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    pattern: Optional[str] = pla.Field(nullable=True, )
    """
    A glob expression matching the IDs of one or more controls to be selected.
    """
    
    
class SelectControlById(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Select a control or controls from an imported control set.
    """

    _id_name : str = None
    with_child_controls: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('yes','no',)})
    """
    When a control is included, whether its child (dependent) controls are also included.
    """
    
    with_ids: Optional[str] = pla.Field(nullable=True, )
    """
    Selecting a control by its ID given as a literal.
    """
    
    matching: Optional[List] = pla.Field(nullable=True, )
    """
    Selecting a set of controls by matching their IDs with a wildcard pattern.
    """
    
    
    @pla.check("matching")
    def check_nested_struct_matching(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, ControlMatching, pa_pl.ControlMatchingDict)
        
class IncludeAll(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Include all controls from the imported catalog or profile resources.
    """

    _id_name : str = None
    pass
    
    
class ProfileImport(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Designates a referenced source catalog or profile that provides a source of control information for use in creating a new overlay or baseline.
    """

    _id_name : str = None
    href: str = pla.Field()
    """
    A resolvable URL reference to a resource.
    """
    
    include_all: Optional[Struct] = pla.Field(nullable=True, )
    """
    Include all selectable objects in the containing OSCAL selection context.
    """
    
    include_controls: Optional[List] = pla.Field(nullable=True, )
    """
    Control-selection entries to include in the containing OSCAL context. The concrete entry class is selected by class-level slot_usage.
    """
    
    exclude_controls: Optional[List] = pla.Field(nullable=True, )
    """
    Control-selection entries to exclude in the containing OSCAL context. The concrete entry class is selected by class-level slot_usage.
    """
    
    
    @pla.check("include_all")
    def check_nested_struct_include_all(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, IncludeAll, pa_pl.IncludeAll)
        
    @pla.check("include_controls")
    def check_nested_struct_include_controls(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, SelectControlById, pa_pl.SelectControlByIdDict)
        
    @pla.check("exclude_controls")
    def check_nested_struct_exclude_controls(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, SelectControlById, pa_pl.SelectControlByIdDict)
        
class CombinationRule(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Defines how to resolve duplicate instances of the same control (e.g., controls with the same ID) encountered in a profile merge.
    """

    _id_name : str = None
    method: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('use-first','merge','keep',)})
    """
    Method indicator used by the containing OSCAL context. Allowed values are constrained by class-level slot_usage.
    """
    
    
class MergeFlat(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Directs that controls appear without any grouping structure after profile resolution.
    """

    _id_name : str = None
    pass
    
    
class InsertControls(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Specifies which controls to use in the containing context (as part of a group or custom merge structure).
    """

    _id_name : str = None
    order: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('keep','ascending','descending',)})
    """
    A designation of how a selection of controls is to be ordered.
    """
    
    include_all: Optional[Struct] = pla.Field(nullable=True, )
    """
    Include all selectable objects in the containing OSCAL selection context.
    """
    
    include_controls: Optional[List] = pla.Field(nullable=True, )
    """
    Control-selection entries to include in the containing OSCAL context. The concrete entry class is selected by class-level slot_usage.
    """
    
    exclude_controls: Optional[List] = pla.Field(nullable=True, )
    """
    Control-selection entries to exclude in the containing OSCAL context. The concrete entry class is selected by class-level slot_usage.
    """
    
    
    @pla.check("include_all")
    def check_nested_struct_include_all(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, IncludeAll, pa_pl.IncludeAll)
        
    @pla.check("include_controls")
    def check_nested_struct_include_controls(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, SelectControlById, pa_pl.SelectControlByIdDict)
        
    @pla.check("exclude_controls")
    def check_nested_struct_exclude_controls(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, SelectControlById, pa_pl.SelectControlByIdDict)
        
class ProfileGroup(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A group of (selected) controls or of groups of controls within a profile custom merge structure.
    """

    _id_name : str = None
    id: Optional[str] = pla.Field(nullable=True, )
    """
    A unique human-oriented identifier within a particular context.
    """
    
    _class: Optional[str] = pla.Field(nullable=True, )
    """
    A textual label that provides a sub-type or characterization.
    """
    
    title: str = pla.Field()
    """
    A human-readable name or title.
    """
    
    params: Optional[List] = pla.Field(nullable=True, )
    """
    Parameters providing a mechanism for the dynamic assignment of value(s) in a control.
    """
    
    parts: Optional[List] = pla.Field(nullable=True, )
    """
    A collection of parts.
    """
    
    groups: Optional[List] = pla.Field(nullable=True, )
    """
    A collection of control groups.
    """
    
    insert_controls: Optional[List] = pla.Field(nullable=True, )
    """
    Specifies which controls to use in the containing context.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    
    @pla.check("params")
    def check_nested_struct_params(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Parameter, pa_pl.ParameterDict)
        
    @pla.check("parts")
    def check_nested_struct_parts(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Part, pa_pl.PartDict)
        
    @pla.check("groups")
    def check_nested_struct_groups(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, ProfileGroup, pa_pl.ProfileGroupDict)
        
    @pla.check("insert_controls")
    def check_nested_struct_insert_controls(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, InsertControls, pa_pl.InsertControlsDict)
        
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Property, pa_pl.PropertyDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Link, pa_pl.LinkDict)
        
class MergeCustom(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Provides an alternate grouping structure that selected controls will be placed in after profile resolution.
    """

    _id_name : str = None
    groups: Optional[List] = pla.Field(nullable=True, )
    """
    A collection of control groups.
    """
    
    insert_controls: Optional[List] = pla.Field(nullable=True, )
    """
    Specifies which controls to use in the containing context.
    """
    
    
    @pla.check("groups")
    def check_nested_struct_groups(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, ProfileGroup, pa_pl.ProfileGroupDict)
        
    @pla.check("insert_controls")
    def check_nested_struct_insert_controls(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, InsertControls, pa_pl.InsertControlsDict)
        
class ProfileMerge(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Provides structuring directives that instruct how controls are organized after profile resolution.
    """

    _id_name : str = None
    combine: Optional[Struct] = pla.Field(nullable=True, )
    """
    Defines how to resolve duplicate instances of the same control.
    """
    
    flat: Optional[Struct] = pla.Field(nullable=True, )
    """
    Directs that controls appear without any grouping structure.
    """
    
    as_is: Optional[bool] = pla.Field(nullable=True, )
    """
    When true, retain the original grouping structure as defined in the import source.
    """
    
    custom: Optional[Struct] = pla.Field(nullable=True, )
    """
    Provides an alternate grouping structure that selected controls will be placed in.
    """
    
    
    @pla.check("combine")
    def check_nested_struct_combine(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, CombinationRule, pa_pl.CombinationRule)
        
    @pla.check("flat")
    def check_nested_struct_flat(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, MergeFlat, pa_pl.MergeFlat)
        
    @pla.check("custom")
    def check_nested_struct_custom(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, MergeCustom, pa_pl.MergeCustom)
        
class ParameterSetting(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A parameter setting to be propagated to points of insertion in a resolved profile.
    """

    _id_name : str = None
    param_id: str = pla.Field()
    """
    The identifier for the parameter being set or referenced.
    """
    
    _class: Optional[str] = pla.Field(nullable=True, )
    """
    A textual label that provides a sub-type or characterization.
    """
    
    depends_on: Optional[str] = pla.Field(nullable=True, )
    """
    (deprecated) Another parameter invoking this one. This construct has been deprecated and should not be used.
    """
    
    label: Optional[str] = pla.Field(nullable=True, )
    """
    A short, placeholder name for the parameter, which can be used as a substitute for a value if no value is assigned.
    """
    
    usage: Optional[str] = pla.Field(nullable=True, )
    """
    Describes the purpose and use of a parameter.
    """
    
    constraints: Optional[List] = pla.Field(nullable=True, )
    """
    A formal or informal expression of a constraint or test.
    """
    
    guidelines: Optional[List] = pla.Field(nullable=True, )
    """
    A prose statement that provides a recommendation for the use of a parameter.
    """
    
    values: Optional[str] = pla.Field(nullable=True, )
    """
    A parameter value or set of values.
    """
    
    select: Optional[Struct] = pla.Field(nullable=True, )
    """
    Presenting a choice among alternatives.
    """
    
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    
    @pla.check("constraints")
    def check_nested_struct_constraints(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, ParameterConstraint, pa_pl.ParameterConstraintDict)
        
    @pla.check("guidelines")
    def check_nested_struct_guidelines(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, ParameterGuideline, pa_pl.ParameterGuidelineDict)
        
    @pla.check("select")
    def check_nested_struct_select(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, ParameterSelection, pa_pl.ParameterSelection)
        
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Property, pa_pl.PropertyDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Link, pa_pl.LinkDict)
        
class Removal(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Specifies objects to be removed from a control based on aspects of the object that must all match.
    """

    _id_name : str = None
    by_name: Optional[str] = pla.Field(nullable=True, )
    """
    Identify items to remove by their assigned name.
    """
    
    by_class: Optional[str] = pla.Field(nullable=True, )
    """
    Identify items to remove by their class label.
    """
    
    by_id: Optional[str] = pla.Field(nullable=True, )
    """
    Identify or target items by their id value.
    """
    
    by_item_name: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('param','prop','link','part','mapping','map',)})
    """
    Identify items to remove by the item's information object type name.
    """
    
    by_ns: Optional[str] = pla.Field(nullable=True, )
    """
    Identify items to remove by the item's namespace.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    
class ProfileAlterationProperty(Property):
    """
    OSCAL property entries allowed in profile modify additions.
    """

    _id_name : str = None
    pass
    
    
class Addition(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Specifies content to be added into controls in resolution.
    """

    _id_name : str = None
    position: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('before','after','starting','ending',)})
    """
    Where to add new content relative to the targeted element.
    """
    
    by_id: Optional[str] = pla.Field(nullable=True, )
    """
    Identify or target items by their id value.
    """
    
    title: Optional[str] = pla.Field(nullable=True, )
    """
    A human-readable name or title.
    """
    
    params: Optional[List] = pla.Field(nullable=True, )
    """
    Parameters providing a mechanism for the dynamic assignment of value(s) in a control.
    """
    
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    parts: Optional[List] = pla.Field(nullable=True, )
    """
    A collection of parts.
    """
    
    
    @pla.check("params")
    def check_nested_struct_params(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Parameter, pa_pl.ParameterDict)
        
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, ProfileAlterationProperty, pa_pl.ProfileAlterationPropertyDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Link, pa_pl.LinkDict)
        
    @pla.check("parts")
    def check_nested_struct_parts(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Part, pa_pl.PartDict)
        
class Alteration(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Specifies changes to be made to an included control when a profile is resolved.
    """

    _id_name : str = None
    control_id: str = pla.Field()
    """
    A reference to a control by its identifier.
    """
    
    removes: Optional[List] = pla.Field(nullable=True, )
    """
    Specifies objects to be removed from a control in resolution.
    """
    
    adds: Optional[List] = pla.Field(nullable=True, )
    """
    Specifies content to be added into a control in resolution.
    """
    
    
    @pla.check("removes")
    def check_nested_struct_removes(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Removal, pa_pl.RemovalDict)
        
    @pla.check("adds")
    def check_nested_struct_adds(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Addition, pa_pl.AdditionDict)
        
class ProfileModify(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Set parameters or amend controls in resolution.
    """

    _id_name : str = None
    set_parameters: Optional[List] = pla.Field(nullable=True, )
    """
    A parameter setting to be propagated to points of insertion.
    """
    
    alters: Optional[List] = pla.Field(nullable=True, )
    """
    Specifies changes to be made to included controls in resolution.
    """
    
    
    @pla.check("set_parameters")
    def check_nested_struct_set_parameters(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, ParameterSetting, pa_pl.ParameterSettingDict)
        
    @pla.check("alters")
    def check_nested_struct_alters(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Alteration, pa_pl.AlterationDict)
        
class Profile(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    An OSCAL Profile that designates a set of controls from one or more catalogs or profiles, optionally restructures and modifies them, to describe a basis for a security standard or body of practice.
    """

    _id_name : str = None
    uuid: str = pla.Field()
    """
    A machine-oriented, globally unique identifier with a cross-instance scope.
    """
    
    metadata: Struct = pla.Field()
    """
    Provides information about the containing document, and defines concepts shared across the document.
    """
    
    imports: List = pla.Field()
    """
    Designates source catalog or profile resources to be imported into the profile.
    """
    
    merge: Optional[Struct] = pla.Field(nullable=True, )
    """
    Structuring directives for how controls are organized after profile resolution.
    """
    
    modify: Optional[Struct] = pla.Field(nullable=True, )
    """
    Set parameters or amend controls in resolution.
    """
    
    back_matter: Optional[Struct] = pla.Field(nullable=True, )
    """
    A collection of resources that may be referenced from within the OSCAL document instance.
    """
    
    
    @pla.check("metadata")
    def check_nested_struct_metadata(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, Metadata, pa_pl.Metadata)
        
    @pla.check("imports")
    def check_nested_struct_imports(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, ProfileImport, pa_pl.ProfileImportDict)
        
    @pla.check("merge")
    def check_nested_struct_merge(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, ProfileMerge, pa_pl.ProfileMerge)
        
    @pla.check("modify")
    def check_nested_struct_modify(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, ProfileModify, pa_pl.ProfileModify)
        
    @pla.check("back_matter")
    def check_nested_struct_back_matter(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, BackMatter, pa_pl.BackMatter)
        
class ProfileDocument(OscalDocument):
    """
    Root wrapper for an OSCAL Profile document.
    """

    _id_name : str = None
    profile: Struct = pla.Field()
    """
    The root profile object.
    """
    
    
    @pla.check("profile")
    def check_nested_struct_profile(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, Profile, pa_pl.Profile)
        
class ImportSSP(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Used by the assessment plan and POA&M to import information about the system.
    """

    _id_name : str = None
    href: str = pla.Field()
    """
    A resolvable URL reference to a resource.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    
class PortRange(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Where applicable, the transport layer protocol port range.
    """

    _id_name : str = None
    start: Optional[int] = pla.Field(nullable=True, )
    """
    The start date/time.
    """
    
    end: Optional[int] = pla.Field(nullable=True, )
    """
    The end date/time.
    """
    
    transport: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('TCP','UDP',)})
    """
    Indicates the transport type.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    
class Protocol(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Information about the protocol used to provide a service.
    """

    _id_name : str = None
    uuid: Optional[str] = pla.Field(nullable=True, )
    """
    A machine-oriented, globally unique identifier with a cross-instance scope.
    """
    
    name: Optional[str] = pla.Field(nullable=True, )
    """
    A textual label that uniquely identifies an attribute or semantic type.
    """
    
    title: Optional[str] = pla.Field(nullable=True, )
    """
    A human-readable name or title.
    """
    
    port_ranges: Optional[List] = pla.Field(nullable=True, )
    """
    Where applicable, the transport layer protocol port range.
    """
    
    
    @pla.check("port_ranges")
    def check_nested_struct_port_ranges(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, PortRange, pa_pl.PortRangeDict)
        
class ComponentStatus(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Describes the operational status of the system component.
    """

    _id_name : str = None
    state: Enum = pla.Field(dtype_kwargs={"categories":('under-development','operational','disposition','other',)})
    """
    The operational status.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    
class ImplementationResponsibleRole(ResponsibleRole):
    """
    Implementation-common scoped responsible role.
    """

    _id_name : str = None
    pass
    
    
class ImplementationCommonProperty(Property):
    """
    Implementation-common scoped OSCAL property.
    """

    _id_name : str = None
    pass
    
    
class ImplementationCommonLink(Link):
    """
    Implementation-common scoped OSCAL link.
    """

    _id_name : str = None
    pass
    
    
class SystemComponent(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A defined component that can be part of an implemented system.
    """

    _id_name : str = None
    uuid: str = pla.Field()
    """
    A machine-oriented, globally unique identifier with a cross-instance scope.
    """
    
    type: str = pla.Field()
    """
    Indicates the nature or kind of the containing object.
    """
    
    title: str = pla.Field()
    """
    A human-readable name or title.
    """
    
    description: str = pla.Field()
    """
    A human-readable description.
    """
    
    purpose: Optional[str] = pla.Field(nullable=True, )
    """
    A summary of the technological or business purpose of the component.
    """
    
    protocols: Optional[List] = pla.Field(nullable=True, )
    """
    Information about the protocol used to provide a service.
    """
    
    status: Struct = pla.Field()
    """
    Status indicator used by the containing OSCAL context. Allowed values are constrained by class-level slot_usage.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    responsible_roles: Optional[List] = pla.Field(nullable=True, )
    """
    Responsible role assignments.
    """
    
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    
    @pla.check("protocols")
    def check_nested_struct_protocols(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Protocol, pa_pl.ProtocolDict)
        
    @pla.check("status")
    def check_nested_struct_status(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, ComponentStatus, pa_pl.ComponentStatus)
        
    @pla.check("responsible_roles")
    def check_nested_struct_responsible_roles(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, ImplementationResponsibleRole, pa_pl.ImplementationResponsibleRoleDict)
        
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, ImplementationCommonProperty, pa_pl.ImplementationCommonPropertyDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, ImplementationCommonLink, pa_pl.ImplementationCommonLinkDict)
        
class ImplementationResponsibleParty(ResponsibleParty):
    """
    Implementation-common scoped responsible party.
    """

    _id_name : str = None
    pass
    
    
class ImplementedComponent(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    The set of components that are implemented in a given system inventory item.
    """

    _id_name : str = None
    component_uuid: str = pla.Field()
    """
    A UUID reference to a component.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    responsible_parties: Optional[List] = pla.Field(nullable=True, )
    """
    Responsible party assignments.
    """
    
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    
    @pla.check("responsible_parties")
    def check_nested_struct_responsible_parties(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, ImplementationResponsibleParty, pa_pl.ImplementationResponsiblePartyDict)
        
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, ImplementationCommonProperty, pa_pl.ImplementationCommonPropertyDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, ImplementationCommonLink, pa_pl.ImplementationCommonLinkDict)
        
class InventoryItem(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A single managed inventory item within the system.
    """

    _id_name : str = None
    uuid: str = pla.Field()
    """
    A machine-oriented, globally unique identifier with a cross-instance scope.
    """
    
    description: str = pla.Field()
    """
    A human-readable description.
    """
    
    implemented_components: Optional[List] = pla.Field(nullable=True, )
    """
    A collection of implemented components.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    responsible_parties: Optional[List] = pla.Field(nullable=True, )
    """
    Responsible party assignments.
    """
    
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    
    @pla.check("implemented_components")
    def check_nested_struct_implemented_components(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, ImplementedComponent, pa_pl.ImplementedComponentDict)
        
    @pla.check("responsible_parties")
    def check_nested_struct_responsible_parties(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, ImplementationResponsibleParty, pa_pl.ImplementationResponsiblePartyDict)
        
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, ImplementationCommonProperty, pa_pl.ImplementationCommonPropertyDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, ImplementationCommonLink, pa_pl.ImplementationCommonLinkDict)
        
class AuthorizedPrivilege(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Identifies a specific system privilege held by the user, along with an associated description and/or rationale for the privilege.
    """

    _id_name : str = None
    title: str = pla.Field()
    """
    A human-readable name or title.
    """
    
    description: Optional[str] = pla.Field(nullable=True, )
    """
    A human-readable description.
    """
    
    functions_performed: str = pla.Field()
    """
    Describes a function performed for a given authorized privilege.
    """
    
    
class SystemUser(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A type of user that interacts with the system based on an associated role.
    """

    _id_name : str = None
    uuid: str = pla.Field()
    """
    A machine-oriented, globally unique identifier with a cross-instance scope.
    """
    
    title: Optional[str] = pla.Field(nullable=True, )
    """
    A human-readable name or title.
    """
    
    short_name: Optional[str] = pla.Field(nullable=True, )
    """
    A short common name, abbreviation, or acronym.
    """
    
    description: Optional[str] = pla.Field(nullable=True, )
    """
    A human-readable description.
    """
    
    role_ids: Optional[str] = pla.Field(nullable=True, )
    """
    Role identifiers associated with the user.
    """
    
    authorized_privileges: Optional[List] = pla.Field(nullable=True, )
    """
    A collection of authorized privileges.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    
    @pla.check("authorized_privileges")
    def check_nested_struct_authorized_privileges(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, AuthorizedPrivilege, pa_pl.AuthorizedPrivilegeDict)
        
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, ImplementationCommonProperty, pa_pl.ImplementationCommonPropertyDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, ImplementationCommonLink, pa_pl.ImplementationCommonLinkDict)
        
class ControlPart(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    An annotated, markup-based textual element of a control's or catalog group's definition, or a child of another part.
    """

    _id_name : str = None
    id: Optional[str] = pla.Field(nullable=True, )
    """
    A unique human-oriented identifier within a particular context.
    """
    
    name: str = pla.Field()
    """
    A textual label that uniquely identifies an attribute or semantic type.
    """
    
    ns: Optional[str] = pla.Field(nullable=True, )
    """
    An optional namespace qualifying a name. Allows different organizations to associate distinct semantics with the same name.
    """
    
    _class: Optional[str] = pla.Field(nullable=True, )
    """
    A textual label that provides a sub-type or characterization.
    """
    
    title: Optional[str] = pla.Field(nullable=True, )
    """
    A human-readable name or title.
    """
    
    prose: Optional[str] = pla.Field(nullable=True, )
    """
    Permits multiple paragraphs, lists, tables etc.
    """
    
    parts: Optional[List] = pla.Field(nullable=True, )
    """
    A collection of parts.
    """
    
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    
    @pla.check("parts")
    def check_nested_struct_parts(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, ControlPart, pa_pl.ControlPartDict)
        
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Property, pa_pl.PropertyDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Link, pa_pl.LinkDict)
        
class LocalObjective(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A local definition of a control objective for this assessment. Uses catalog syntax for control objective and assessment actions.
    """

    _id_name : str = None
    control_id: str = pla.Field()
    """
    A reference to a control by its identifier.
    """
    
    description: Optional[str] = pla.Field(nullable=True, )
    """
    A human-readable description.
    """
    
    parts: List = pla.Field()
    """
    A collection of parts.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    
    @pla.check("parts")
    def check_nested_struct_parts(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, ControlPart, pa_pl.ControlPartDict)
        
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Property, pa_pl.PropertyDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Link, pa_pl.LinkDict)
        
class AssessmentSelectControlById(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Select a specific control for inclusion/exclusion in the assessment by literal control ID and optional statement IDs.
    """

    _id_name : str = None
    control_id: str = pla.Field()
    """
    A reference to a control by its identifier.
    """
    
    statement_ids: Optional[str] = pla.Field(nullable=True, )
    """
    Statement IDs for control selection.
    """
    
    
class ControlSelection(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Identifies the controls being assessed.
    """

    _id_name : str = None
    description: Optional[str] = pla.Field(nullable=True, )
    """
    A human-readable description.
    """
    
    include_all: Optional[Struct] = pla.Field(nullable=True, )
    """
    Include all selectable objects in the containing OSCAL selection context.
    """
    
    include_controls: Optional[List] = pla.Field(nullable=True, )
    """
    Control-selection entries to include in the containing OSCAL context. The concrete entry class is selected by class-level slot_usage.
    """
    
    exclude_controls: Optional[List] = pla.Field(nullable=True, )
    """
    Control-selection entries to exclude in the containing OSCAL context. The concrete entry class is selected by class-level slot_usage.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    
    @pla.check("include_all")
    def check_nested_struct_include_all(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, IncludeAll, pa_pl.IncludeAll)
        
    @pla.check("include_controls")
    def check_nested_struct_include_controls(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, AssessmentSelectControlById, pa_pl.AssessmentSelectControlByIdDict)
        
    @pla.check("exclude_controls")
    def check_nested_struct_exclude_controls(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, AssessmentSelectControlById, pa_pl.AssessmentSelectControlByIdDict)
        
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Property, pa_pl.PropertyDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Link, pa_pl.LinkDict)
        
class SelectObjectiveById(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Used to select a control objective for inclusion/exclusion.
    """

    _id_name : str = None
    objective_id: str = pla.Field()
    """
    Reference to a control objective by its identifier.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    
class ControlObjectiveSelection(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Identifies the control objectives of the assessment.
    """

    _id_name : str = None
    description: Optional[str] = pla.Field(nullable=True, )
    """
    A human-readable description.
    """
    
    include_all: Optional[Struct] = pla.Field(nullable=True, )
    """
    Include all selectable objects in the containing OSCAL selection context.
    """
    
    include_objectives: Optional[List] = pla.Field(nullable=True, )
    """
    Objectives to include in the assessment.
    """
    
    exclude_objectives: Optional[List] = pla.Field(nullable=True, )
    """
    Objectives to exclude from the assessment.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    
    @pla.check("include_all")
    def check_nested_struct_include_all(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, IncludeAll, pa_pl.IncludeAll)
        
    @pla.check("include_objectives")
    def check_nested_struct_include_objectives(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, SelectObjectiveById, pa_pl.SelectObjectiveByIdDict)
        
    @pla.check("exclude_objectives")
    def check_nested_struct_exclude_objectives(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, SelectObjectiveById, pa_pl.SelectObjectiveByIdDict)
        
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Property, pa_pl.PropertyDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Link, pa_pl.LinkDict)
        
class ReviewedControls(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Identifies the controls being assessed and their control objectives.
    """

    _id_name : str = None
    description: Optional[str] = pla.Field(nullable=True, )
    """
    A human-readable description.
    """
    
    control_selections: List = pla.Field()
    """
    Identifies the controls being assessed.
    """
    
    control_objective_selections: Optional[List] = pla.Field(nullable=True, )
    """
    Identifies the control objectives of the assessment.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    
    @pla.check("control_selections")
    def check_nested_struct_control_selections(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, ControlSelection, pa_pl.ControlSelectionDict)
        
    @pla.check("control_objective_selections")
    def check_nested_struct_control_objective_selections(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, ControlObjectiveSelection, pa_pl.ControlObjectiveSelectionDict)
        
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Property, pa_pl.PropertyDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Link, pa_pl.LinkDict)
        
class Step(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Identifies an individual step in a series of steps related to an activity, such as an assessment test or examination procedure.
    """

    _id_name : str = None
    uuid: str = pla.Field()
    """
    A machine-oriented, globally unique identifier with a cross-instance scope.
    """
    
    title: Optional[str] = pla.Field(nullable=True, )
    """
    A human-readable name or title.
    """
    
    description: str = pla.Field()
    """
    A human-readable description.
    """
    
    reviewed_controls: Optional[Struct] = pla.Field(nullable=True, )
    """
    Identifies the controls being assessed and their control objectives.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    responsible_roles: Optional[List] = pla.Field(nullable=True, )
    """
    Responsible role assignments.
    """
    
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    
    @pla.check("reviewed_controls")
    def check_nested_struct_reviewed_controls(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, ReviewedControls, pa_pl.ReviewedControls)
        
    @pla.check("responsible_roles")
    def check_nested_struct_responsible_roles(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, ResponsibleRole, pa_pl.ResponsibleRoleDict)
        
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Property, pa_pl.PropertyDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Link, pa_pl.LinkDict)
        
class Activity(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Identifies an assessment or related process that can be performed. In the assessment plan, this is an intended activity.
    """

    _id_name : str = None
    uuid: str = pla.Field()
    """
    A machine-oriented, globally unique identifier with a cross-instance scope.
    """
    
    title: Optional[str] = pla.Field(nullable=True, )
    """
    A human-readable name or title.
    """
    
    description: str = pla.Field()
    """
    A human-readable description.
    """
    
    steps: Optional[List] = pla.Field(nullable=True, )
    """
    A collection of steps in an activity.
    """
    
    related_controls: Optional[Struct] = pla.Field(nullable=True, )
    """
    A reference to reviewed controls for this activity or step.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    responsible_roles: Optional[List] = pla.Field(nullable=True, )
    """
    Responsible role assignments.
    """
    
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    
    @pla.check("steps")
    def check_nested_struct_steps(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Step, pa_pl.StepDict)
        
    @pla.check("related_controls")
    def check_nested_struct_related_controls(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, ReviewedControls, pa_pl.ReviewedControls)
        
    @pla.check("responsible_roles")
    def check_nested_struct_responsible_roles(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, ResponsibleRole, pa_pl.ResponsibleRoleDict)
        
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Property, pa_pl.PropertyDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Link, pa_pl.LinkDict)
        
class LocalDefinitions(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Used to define data objects that are used in the assessment plan, that do not appear in the referenced SSP.
    """

    _id_name : str = None
    components: Optional[List] = pla.Field(nullable=True, )
    """
    A collection of system components.
    """
    
    inventory_items: Optional[List] = pla.Field(nullable=True, )
    """
    A collection of inventory items.
    """
    
    users: Optional[List] = pla.Field(nullable=True, )
    """
    A collection of system users.
    """
    
    objectives_and_methods: Optional[List] = pla.Field(nullable=True, )
    """
    A collection of locally-defined control objectives.
    """
    
    activities: Optional[List] = pla.Field(nullable=True, )
    """
    A collection of activities.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    
    @pla.check("components")
    def check_nested_struct_components(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, SystemComponent, pa_pl.SystemComponentDict)
        
    @pla.check("inventory_items")
    def check_nested_struct_inventory_items(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, InventoryItem, pa_pl.InventoryItemDict)
        
    @pla.check("users")
    def check_nested_struct_users(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, SystemUser, pa_pl.SystemUserDict)
        
    @pla.check("objectives_and_methods")
    def check_nested_struct_objectives_and_methods(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, LocalObjective, pa_pl.LocalObjectiveDict)
        
    @pla.check("activities")
    def check_nested_struct_activities(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Activity, pa_pl.ActivityDict)
        
class AssessmentPart(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A partition of an assessment plan or results or a child of another part.
    """

    _id_name : str = None
    uuid: Optional[str] = pla.Field(nullable=True, )
    """
    A machine-oriented, globally unique identifier with a cross-instance scope.
    """
    
    name: str = pla.Field()
    """
    A textual label that uniquely identifies an attribute or semantic type.
    """
    
    ns: Optional[str] = pla.Field(nullable=True, )
    """
    An optional namespace qualifying a name. Allows different organizations to associate distinct semantics with the same name.
    """
    
    _class: Optional[str] = pla.Field(nullable=True, )
    """
    A textual label that provides a sub-type or characterization.
    """
    
    title: Optional[str] = pla.Field(nullable=True, )
    """
    A human-readable name or title.
    """
    
    prose: Optional[str] = pla.Field(nullable=True, )
    """
    Permits multiple paragraphs, lists, tables etc.
    """
    
    parts: Optional[List] = pla.Field(nullable=True, )
    """
    A collection of parts.
    """
    
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    
    @pla.check("parts")
    def check_nested_struct_parts(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, AssessmentPart, pa_pl.AssessmentPartDict)
        
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Property, pa_pl.PropertyDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Link, pa_pl.LinkDict)
        
class TermsAndConditionsPart(AssessmentPart):
    """
    A terms-and-conditions scoped assessment part.
    """

    _id_name : str = None
    pass
    
    
class TermsAndConditions(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Used to define various terms and conditions under which an assessment can be performed.
    """

    _id_name : str = None
    parts: Optional[List] = pla.Field(nullable=True, )
    """
    A collection of parts.
    """
    
    
    @pla.check("parts")
    def check_nested_struct_parts(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, TermsAndConditionsPart, pa_pl.TermsAndConditionsPartDict)
        
class SelectSubjectById(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Identifies a set of assessment subjects to include/exclude by UUID.
    """

    _id_name : str = None
    subject_uuid: str = pla.Field()
    """
    A UUID reference to the identified subject.
    """
    
    type: str = pla.Field()
    """
    Indicates the nature or kind of the containing object.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Property, pa_pl.PropertyDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Link, pa_pl.LinkDict)
        
class AssessmentSubject(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Identifies system elements being assessed, such as components, inventory items, and locations.
    """

    _id_name : str = None
    type: str = pla.Field()
    """
    Indicates the nature or kind of the containing object.
    """
    
    description: Optional[str] = pla.Field(nullable=True, )
    """
    A human-readable description.
    """
    
    include_all: Optional[Struct] = pla.Field(nullable=True, )
    """
    Include all selectable objects in the containing OSCAL selection context.
    """
    
    include_subjects: Optional[List] = pla.Field(nullable=True, )
    """
    Assessment subjects to include.
    """
    
    exclude_subjects: Optional[List] = pla.Field(nullable=True, )
    """
    Assessment subjects to exclude.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    
    @pla.check("include_all")
    def check_nested_struct_include_all(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, IncludeAll, pa_pl.IncludeAll)
        
    @pla.check("include_subjects")
    def check_nested_struct_include_subjects(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, SelectSubjectById, pa_pl.SelectSubjectByIdDict)
        
    @pla.check("exclude_subjects")
    def check_nested_struct_exclude_subjects(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, SelectSubjectById, pa_pl.SelectSubjectByIdDict)
        
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Property, pa_pl.PropertyDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Link, pa_pl.LinkDict)
        
class UsesComponent(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    The set of components that are used by the assessment platform.
    """

    _id_name : str = None
    component_uuid: str = pla.Field()
    """
    A UUID reference to a component.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    responsible_parties: Optional[List] = pla.Field(nullable=True, )
    """
    Responsible party assignments.
    """
    
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    
    @pla.check("responsible_parties")
    def check_nested_struct_responsible_parties(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, ResponsibleParty, pa_pl.ResponsiblePartyDict)
        
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Property, pa_pl.PropertyDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Link, pa_pl.LinkDict)
        
class AssessmentPlatform(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Used to represent the toolset used to perform aspects of the assessment.
    """

    _id_name : str = None
    uuid: str = pla.Field()
    """
    A machine-oriented, globally unique identifier with a cross-instance scope.
    """
    
    title: Optional[str] = pla.Field(nullable=True, )
    """
    A human-readable name or title.
    """
    
    uses_components: Optional[List] = pla.Field(nullable=True, )
    """
    The set of components used by the assessment platform.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    
    @pla.check("uses_components")
    def check_nested_struct_uses_components(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, UsesComponent, pa_pl.UsesComponentDict)
        
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Property, pa_pl.PropertyDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Link, pa_pl.LinkDict)
        
class AssessmentAssets(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Identifies the assets used to perform this assessment.
    """

    _id_name : str = None
    components: Optional[List] = pla.Field(nullable=True, )
    """
    A collection of system components.
    """
    
    assessment_platforms: List = pla.Field()
    """
    A collection of assessment platforms.
    """
    
    
    @pla.check("components")
    def check_nested_struct_components(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, SystemComponent, pa_pl.SystemComponentDict)
        
    @pla.check("assessment_platforms")
    def check_nested_struct_assessment_platforms(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, AssessmentPlatform, pa_pl.AssessmentPlatformDict)
        
class OnDateCondition(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    The task is intended to occur on the specified date.
    """

    _id_name : str = None
    date: DateTime() = pla.Field()
    """
    The date and time when the action occurred.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    
class WithinDateRange(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    The task is intended to occur within the specified date range.
    """

    _id_name : str = None
    start: DateTime() = pla.Field()
    """
    The start date/time.
    """
    
    end: DateTime() = pla.Field()
    """
    The end date/time.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    
class AtFrequency(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    The task is intended to occur at the specified frequency.
    """

    _id_name : str = None
    period: int = pla.Field()
    """
    The task must occur every period (in the given units).
    """
    
    unit: Enum = pla.Field(dtype_kwargs={"categories":('seconds','minutes','hours','days','months','years',)})
    """
    The unit of time for the period.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    
class EventTiming(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    The timing under which the task is intended to occur.
    """

    _id_name : str = None
    on_date: Optional[Struct] = pla.Field(nullable=True, )
    """
    The task is intended to occur on the specified date.
    """
    
    within_date_range: Optional[Struct] = pla.Field(nullable=True, )
    """
    The task is intended to occur within the specified date range.
    """
    
    at_frequency: Optional[Struct] = pla.Field(nullable=True, )
    """
    The task is intended to occur at the specified frequency.
    """
    
    
    @pla.check("on_date")
    def check_nested_struct_on_date(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, OnDateCondition, pa_pl.OnDateCondition)
        
    @pla.check("within_date_range")
    def check_nested_struct_within_date_range(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, WithinDateRange, pa_pl.WithinDateRange)
        
    @pla.check("at_frequency")
    def check_nested_struct_at_frequency(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, AtFrequency, pa_pl.AtFrequency)
        
class TaskDependency(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Used to indicate that a task is dependent on another task.
    """

    _id_name : str = None
    task_uuid: str = pla.Field()
    """
    A UUID reference to a task.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    
class AssociatedActivity(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Identifies an individual activity to be performed as part of a task.
    """

    _id_name : str = None
    activity_uuid: str = pla.Field()
    """
    A UUID reference to an activity.
    """
    
    subjects: List = pla.Field()
    """
    Assessment subjects or subject references for this object.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    responsible_roles: Optional[List] = pla.Field(nullable=True, )
    """
    Responsible role assignments.
    """
    
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    
    @pla.check("subjects")
    def check_nested_struct_subjects(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, AssessmentSubject, pa_pl.AssessmentSubjectDict)
        
    @pla.check("responsible_roles")
    def check_nested_struct_responsible_roles(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, ResponsibleRole, pa_pl.ResponsibleRoleDict)
        
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Property, pa_pl.PropertyDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Link, pa_pl.LinkDict)
        
class Task(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Represents a scheduled event or milestone, which may be associated with a series of assessment actions.
    """

    _id_name : str = None
    uuid: str = pla.Field()
    """
    A machine-oriented, globally unique identifier with a cross-instance scope.
    """
    
    type: str = pla.Field()
    """
    Indicates the nature or kind of the containing object.
    """
    
    title: str = pla.Field()
    """
    A human-readable name or title.
    """
    
    description: Optional[str] = pla.Field(nullable=True, )
    """
    A human-readable description.
    """
    
    timing: Optional[Struct] = pla.Field(nullable=True, )
    """
    The timing under which a task is intended to occur.
    """
    
    dependencies: Optional[List] = pla.Field(nullable=True, )
    """
    Tasks that this task depends on.
    """
    
    associated_activities: Optional[List] = pla.Field(nullable=True, )
    """
    Activities associated with this task.
    """
    
    tasks: Optional[List] = pla.Field(nullable=True, )
    """
    A collection of tasks.
    """
    
    subjects: Optional[List] = pla.Field(nullable=True, )
    """
    Assessment subjects or subject references for this object.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    responsible_roles: Optional[List] = pla.Field(nullable=True, )
    """
    Responsible role assignments.
    """
    
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    
    @pla.check("timing")
    def check_nested_struct_timing(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, EventTiming, pa_pl.EventTiming)
        
    @pla.check("dependencies")
    def check_nested_struct_dependencies(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, TaskDependency, pa_pl.TaskDependencyDict)
        
    @pla.check("associated_activities")
    def check_nested_struct_associated_activities(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, AssociatedActivity, pa_pl.AssociatedActivityDict)
        
    @pla.check("tasks")
    def check_nested_struct_tasks(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Task, pa_pl.TaskDict)
        
    @pla.check("subjects")
    def check_nested_struct_subjects(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, AssessmentSubject, pa_pl.AssessmentSubjectDict)
        
    @pla.check("responsible_roles")
    def check_nested_struct_responsible_roles(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, ResponsibleRole, pa_pl.ResponsibleRoleDict)
        
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Property, pa_pl.PropertyDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Link, pa_pl.LinkDict)
        
class AssessmentPlan(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    An assessment plan, such as those provided by a FedRAMP assessor.
    """

    _id_name : str = None
    uuid: str = pla.Field()
    """
    Assessment Plan Universally Unique Identifier.
    """
    
    metadata: Struct = pla.Field()
    """
    Provides information about the containing document, and defines concepts shared across the document.
    """
    
    import_ssp: Struct = pla.Field()
    """
    Used to import information about the system from an SSP.
    """
    
    local_definitions: Optional[Struct] = pla.Field(nullable=True, )
    """
    Used to define data objects that do not appear in the referenced SSP.
    """
    
    terms_and_conditions: Optional[Struct] = pla.Field(nullable=True, )
    """
    Terms and conditions under which an assessment can be performed.
    """
    
    assessment_subjects: Optional[List] = pla.Field(nullable=True, )
    """
    Identifies system elements being assessed.
    """
    
    assessment_assets: Optional[Struct] = pla.Field(nullable=True, )
    """
    Identifies the assets used to perform this assessment.
    """
    
    reviewed_controls: Struct = pla.Field()
    """
    Identifies the controls being assessed and their control objectives.
    """
    
    tasks: Optional[List] = pla.Field(nullable=True, )
    """
    A collection of tasks.
    """
    
    back_matter: Optional[Struct] = pla.Field(nullable=True, )
    """
    A collection of resources that may be referenced from within the OSCAL document instance.
    """
    
    
    @pla.check("metadata")
    def check_nested_struct_metadata(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, Metadata, pa_pl.Metadata)
        
    @pla.check("import_ssp")
    def check_nested_struct_import_ssp(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, ImportSSP, pa_pl.ImportSSP)
        
    @pla.check("local_definitions")
    def check_nested_struct_local_definitions(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, LocalDefinitions, pa_pl.LocalDefinitions)
        
    @pla.check("terms_and_conditions")
    def check_nested_struct_terms_and_conditions(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, TermsAndConditions, pa_pl.TermsAndConditions)
        
    @pla.check("assessment_subjects")
    def check_nested_struct_assessment_subjects(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, AssessmentSubject, pa_pl.AssessmentSubjectDict)
        
    @pla.check("assessment_assets")
    def check_nested_struct_assessment_assets(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, AssessmentAssets, pa_pl.AssessmentAssets)
        
    @pla.check("reviewed_controls")
    def check_nested_struct_reviewed_controls(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, ReviewedControls, pa_pl.ReviewedControls)
        
    @pla.check("tasks")
    def check_nested_struct_tasks(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Task, pa_pl.TaskDict)
        
    @pla.check("back_matter")
    def check_nested_struct_back_matter(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, BackMatter, pa_pl.BackMatter)
        
class AssessmentPlanDocument(OscalDocument):
    """
    Root wrapper for an OSCAL Assessment Plan document.
    """

    _id_name : str = None
    assessment_plan: Struct = pla.Field()
    """
    The root assessment plan object.
    """
    
    
    @pla.check("assessment_plan")
    def check_nested_struct_assessment_plan(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, AssessmentPlan, pa_pl.AssessmentPlan)
        
class SubjectReference(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A human-oriented identifier reference to a resource. Use type to indicate whether the identified resource is a component, inventory item, location, user, or something else.
    """

    _id_name : str = None
    subject_uuid: str = pla.Field()
    """
    A UUID reference to the identified subject.
    """
    
    type: str = pla.Field()
    """
    Indicates the nature or kind of the containing object.
    """
    
    title: Optional[str] = pla.Field(nullable=True, )
    """
    A human-readable name or title.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Property, pa_pl.PropertyDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Link, pa_pl.LinkDict)
        
class AssessmentSubjectSource(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Assessment subjects will be identified while conducting the referenced activity.
    """

    _id_name : str = None
    task_uuid: str = pla.Field()
    """
    A UUID reference to a task.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    
class AssessmentSubjectPlaceholder(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Used when the assessment subjects will be determined as part of one or more other assessment activities.
    """

    _id_name : str = None
    uuid: str = pla.Field()
    """
    A machine-oriented, globally unique identifier with a cross-instance scope.
    """
    
    description: Optional[str] = pla.Field(nullable=True, )
    """
    A human-readable description.
    """
    
    sources: List = pla.Field()
    """
    Source references or source-participation entries in the containing OSCAL context. The concrete entry class is selected by class-level slot_usage.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    
    @pla.check("sources")
    def check_nested_struct_sources(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, AssessmentSubjectSource, pa_pl.AssessmentSubjectSourceDict)
        
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Property, pa_pl.PropertyDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Link, pa_pl.LinkDict)
        
class AssessmentMethod(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A local definition of a control objective.
    """

    _id_name : str = None
    uuid: str = pla.Field()
    """
    A machine-oriented, globally unique identifier with a cross-instance scope.
    """
    
    description: Optional[str] = pla.Field(nullable=True, )
    """
    A human-readable description.
    """
    
    part: Struct = pla.Field()
    """
    An assessment part.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    
    @pla.check("part")
    def check_nested_struct_part(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, AssessmentPart, pa_pl.AssessmentPart)
        
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Property, pa_pl.PropertyDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Link, pa_pl.LinkDict)
        
class OriginActor(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    The actor that produces an observation, a finding, or a risk.
    """

    _id_name : str = None
    type: Enum = pla.Field(dtype_kwargs={"categories":('tool','assessment-platform','party',)})
    """
    Indicates the nature or kind of the containing object.
    """
    
    actor_uuid: str = pla.Field()
    """
    A machine-oriented identifier reference to the tool or person based on the associated type.
    """
    
    role_id: Optional[str] = pla.Field(nullable=True, )
    """
    A reference to a role by its identifier.
    """
    
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Property, pa_pl.PropertyDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Link, pa_pl.LinkDict)
        
class IdentifiedSubject(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Used to detail assessment subjects that were identified by this task.
    """

    _id_name : str = None
    subject_placeholder_uuid: str = pla.Field()
    """
    A reference to an assessment subject placeholder defined in the assessment plan.
    """
    
    subjects: List = pla.Field()
    """
    Assessment subjects or subject references for this object.
    """
    
    
    @pla.check("subjects")
    def check_nested_struct_subjects(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, AssessmentSubject, pa_pl.AssessmentSubjectDict)
        
class RelatedTask(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Identifies an individual task for which the containing object is a consequence of.
    """

    _id_name : str = None
    task_uuid: str = pla.Field()
    """
    A UUID reference to a task.
    """
    
    subjects: Optional[List] = pla.Field(nullable=True, )
    """
    Assessment subjects or subject references for this object.
    """
    
    identified_subject: Optional[Struct] = pla.Field(nullable=True, )
    """
    Used to detail assessment subjects that were identified by this task.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    responsible_parties: Optional[List] = pla.Field(nullable=True, )
    """
    Responsible party assignments.
    """
    
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    
    @pla.check("subjects")
    def check_nested_struct_subjects(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, AssessmentSubject, pa_pl.AssessmentSubjectDict)
        
    @pla.check("identified_subject")
    def check_nested_struct_identified_subject(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, IdentifiedSubject, pa_pl.IdentifiedSubject)
        
    @pla.check("responsible_parties")
    def check_nested_struct_responsible_parties(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, ResponsibleParty, pa_pl.ResponsiblePartyDict)
        
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Property, pa_pl.PropertyDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Link, pa_pl.LinkDict)
        
class Origin(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Identifies the source of the finding, such as a tool, interviewed person, or activity.
    """

    _id_name : str = None
    actors: List = pla.Field()
    """
    The actor that produces an observation, a finding, or a risk.
    """
    
    related_tasks: Optional[List] = pla.Field(nullable=True, )
    """
    Identifies tasks for which the containing object is a consequence.
    """
    
    
    @pla.check("actors")
    def check_nested_struct_actors(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, OriginActor, pa_pl.OriginActorDict)
        
    @pla.check("related_tasks")
    def check_nested_struct_related_tasks(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, RelatedTask, pa_pl.RelatedTaskDict)
        
class RelevantEvidence(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Links this observation to relevant evidence.
    """

    _id_name : str = None
    href: Optional[str] = pla.Field(nullable=True, )
    """
    A resolvable URL reference to a resource.
    """
    
    description: str = pla.Field()
    """
    A human-readable description.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Property, pa_pl.PropertyDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Link, pa_pl.LinkDict)
        
class Observation(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Describes an individual observation.
    """

    _id_name : str = None
    uuid: str = pla.Field()
    """
    A machine-oriented, globally unique identifier with a cross-instance scope.
    """
    
    title: Optional[str] = pla.Field(nullable=True, )
    """
    A human-readable name or title.
    """
    
    description: str = pla.Field()
    """
    A human-readable description.
    """
    
    methods: str = pla.Field()
    """
    Identifies how the observation was made. Recommended values are in ObservationMethodEnum; other values are permitted (OSCAL allow-other="yes").
    """
    
    types: Optional[str] = pla.Field(nullable=True, )
    """
    Identifies the nature of the observation. Recommended values are in ObservationTypeEnum; other values are permitted (OSCAL allow-other="yes").
    """
    
    origins: Optional[List] = pla.Field(nullable=True, )
    """
    Identifies the source of observations, findings, or risks.
    """
    
    subjects: Optional[List] = pla.Field(nullable=True, )
    """
    Assessment subjects or subject references for this object.
    """
    
    relevant_evidence: Optional[List] = pla.Field(nullable=True, )
    """
    Links the observation to relevant evidence.
    """
    
    collected: DateTime() = pla.Field()
    """
    Date/time stamp identifying when the finding information was collected.
    """
    
    expires: Optional[DateTime()] = pla.Field(nullable=True, )
    """
    Date/time identifying when the finding information is no longer considered valid.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    
    @pla.check("origins")
    def check_nested_struct_origins(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Origin, pa_pl.OriginDict)
        
    @pla.check("subjects")
    def check_nested_struct_subjects(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, SubjectReference, pa_pl.SubjectReferenceDict)
        
    @pla.check("relevant_evidence")
    def check_nested_struct_relevant_evidence(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, RelevantEvidence, pa_pl.RelevantEvidenceDict)
        
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Property, pa_pl.PropertyDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Link, pa_pl.LinkDict)
        
class ImplementationStatus(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Indicates the degree to which a given control is implemented.
    """

    _id_name : str = None
    state: str = pla.Field()
    """
    Identifies the implementation status of the control or control objective. Recommended values are in ImplementationStatusStateEnum; other values are permitted (OSCAL allow-other="yes").
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    
class ObjectiveStatus(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A determination of if the objective is satisfied or not within a given system.
    """

    _id_name : str = None
    state: Enum = pla.Field(dtype_kwargs={"categories":('satisfied','not-satisfied',)})
    """
    An indication as to whether the objective is satisfied or not.
    """
    
    reason: Optional[str] = pla.Field(nullable=True, )
    """
    The reason the objective was given its status. Recommended values are in ObjectiveStatusReasonEnum; other values are permitted (OSCAL allow-other="yes").
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    
class FindingTarget(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Captures an assessor's conclusions regarding the degree to which an objective is satisfied.
    """

    _id_name : str = None
    type: Enum = pla.Field(dtype_kwargs={"categories":('statement-id','objective-id',)})
    """
    Indicates the nature or kind of the containing object.
    """
    
    target_id: str = pla.Field()
    """
    Identifies the specific target qualified by the type.
    """
    
    title: Optional[str] = pla.Field(nullable=True, )
    """
    A human-readable name or title.
    """
    
    description: Optional[str] = pla.Field(nullable=True, )
    """
    A human-readable description.
    """
    
    implementation_status: Optional[Struct] = pla.Field(nullable=True, )
    """
    Identifies the implementation status of the control.
    """
    
    status: Struct = pla.Field()
    """
    Status indicator used by the containing OSCAL context. Allowed values are constrained by class-level slot_usage.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    
    @pla.check("implementation_status")
    def check_nested_struct_implementation_status(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, ImplementationStatus, pa_pl.ImplementationStatus)
        
    @pla.check("status")
    def check_nested_struct_status(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, ObjectiveStatus, pa_pl.ObjectiveStatus)
        
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Property, pa_pl.PropertyDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Link, pa_pl.LinkDict)
        
class RelatedObservation(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Relates the identified element to a set of referenced observations.
    """

    _id_name : str = None
    observation_uuid: str = pla.Field()
    """
    A machine-oriented identifier reference to an observation defined in the list of observations.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    
class AssociatedRisk(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Relates the finding to a set of referenced risks.
    """

    _id_name : str = None
    risk_uuid: str = pla.Field()
    """
    A machine-oriented identifier reference to a risk defined in the list of risks.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    
class Finding(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Describes an individual finding.
    """

    _id_name : str = None
    uuid: str = pla.Field()
    """
    A machine-oriented, globally unique identifier with a cross-instance scope.
    """
    
    title: str = pla.Field()
    """
    A human-readable name or title.
    """
    
    description: str = pla.Field()
    """
    A human-readable description.
    """
    
    target: Struct = pla.Field()
    """
    Identifies the target of a finding.
    """
    
    implementation_statement_uuid: Optional[str] = pla.Field(nullable=True, )
    """
    A reference to the implementation statement in the SSP to which this finding is related.
    """
    
    origins: Optional[List] = pla.Field(nullable=True, )
    """
    Identifies the source of observations, findings, or risks.
    """
    
    related_observations: Optional[List] = pla.Field(nullable=True, )
    """
    Relates the containing object to a set of referenced observations.
    """
    
    related_risks: Optional[List] = pla.Field(nullable=True, )
    """
    Relates the finding to a set of referenced risks.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    
    @pla.check("target")
    def check_nested_struct_target(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, FindingTarget, pa_pl.FindingTarget)
        
    @pla.check("origins")
    def check_nested_struct_origins(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Origin, pa_pl.OriginDict)
        
    @pla.check("related_observations")
    def check_nested_struct_related_observations(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, RelatedObservation, pa_pl.RelatedObservationDict)
        
    @pla.check("related_risks")
    def check_nested_struct_related_risks(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, AssociatedRisk, pa_pl.AssociatedRiskDict)
        
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Property, pa_pl.PropertyDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Link, pa_pl.LinkDict)
        
class ThreatId(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A pointer, by ID, to an externally-defined threat.
    """

    _id_name : str = None
    href: Optional[str] = pla.Field(nullable=True, )
    """
    A resolvable URL reference to a resource.
    """
    
    system: str = pla.Field()
    """
    Specifies the system or scheme from which the identifier originates.
    """
    
    id: str = pla.Field()
    """
    A unique human-oriented identifier within a particular context.
    """
    
    
class Facet(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    An individual characteristic that is part of a larger set produced by the same actor.
    """

    _id_name : str = None
    name: str = pla.Field()
    """
    A textual label that uniquely identifies an attribute or semantic type.
    """
    
    value: str = pla.Field()
    """
    The value associated with the containing object.
    """
    
    system: str = pla.Field()
    """
    Specifies the system or scheme from which the identifier originates.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Property, pa_pl.PropertyDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Link, pa_pl.LinkDict)
        
class Characterization(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A collection of descriptive data about the containing object from a specific origin.
    """

    _id_name : str = None
    origin: Struct = pla.Field()
    """
    The source of the finding.
    """
    
    facets: List = pla.Field()
    """
    An individual characteristic that is part of a larger set produced by the same actor.
    """
    
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    
    @pla.check("origin")
    def check_nested_struct_origin(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, Origin, pa_pl.Origin)
        
    @pla.check("facets")
    def check_nested_struct_facets(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Facet, pa_pl.FacetDict)
        
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Property, pa_pl.PropertyDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Link, pa_pl.LinkDict)
        
class MitigatingFactor(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Describes an existing mitigating factor that may affect the overall determination of the risk.
    """

    _id_name : str = None
    uuid: str = pla.Field()
    """
    A machine-oriented, globally unique identifier with a cross-instance scope.
    """
    
    description: str = pla.Field()
    """
    A human-readable description.
    """
    
    implementation_uuid: Optional[str] = pla.Field(nullable=True, )
    """
    A machine-oriented, globally unique identifier with cross-instance scope that can be used to reference this implementation statement elsewhere in this or other OSCAL instances.
    """
    
    subjects: Optional[List] = pla.Field(nullable=True, )
    """
    Assessment subjects or subject references for this object.
    """
    
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    
    @pla.check("subjects")
    def check_nested_struct_subjects(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, SubjectReference, pa_pl.SubjectReferenceDict)
        
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Property, pa_pl.PropertyDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Link, pa_pl.LinkDict)
        
class RequiredAsset(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Identifies an asset required to achieve remediation.
    """

    _id_name : str = None
    uuid: str = pla.Field()
    """
    A machine-oriented, globally unique identifier with a cross-instance scope.
    """
    
    title: Optional[str] = pla.Field(nullable=True, )
    """
    A human-readable name or title.
    """
    
    description: str = pla.Field()
    """
    A human-readable description.
    """
    
    subjects: Optional[List] = pla.Field(nullable=True, )
    """
    Assessment subjects or subject references for this object.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    
    @pla.check("subjects")
    def check_nested_struct_subjects(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, SubjectReference, pa_pl.SubjectReferenceDict)
        
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Property, pa_pl.PropertyDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Link, pa_pl.LinkDict)
        
class Response(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Describes either recommended or an actual plan for addressing the risk.
    """

    _id_name : str = None
    uuid: str = pla.Field()
    """
    A machine-oriented, globally unique identifier with a cross-instance scope.
    """
    
    title: str = pla.Field()
    """
    A human-readable name or title.
    """
    
    description: str = pla.Field()
    """
    A human-readable description.
    """
    
    lifecycle: str = pla.Field()
    """
    Identifies whether this is a recommendation or an actual plan. Recommended values are in ResponseLifecycleEnum; other values are permitted (OSCAL allow-other="yes").
    """
    
    origins: Optional[List] = pla.Field(nullable=True, )
    """
    Identifies the source of observations, findings, or risks.
    """
    
    required_assets: Optional[List] = pla.Field(nullable=True, )
    """
    Identifies an asset required to achieve remediation.
    """
    
    tasks: Optional[List] = pla.Field(nullable=True, )
    """
    A collection of tasks.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    
    @pla.check("origins")
    def check_nested_struct_origins(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Origin, pa_pl.OriginDict)
        
    @pla.check("required_assets")
    def check_nested_struct_required_assets(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, RequiredAsset, pa_pl.RequiredAssetDict)
        
    @pla.check("tasks")
    def check_nested_struct_tasks(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Task, pa_pl.TaskDict)
        
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Property, pa_pl.PropertyDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Link, pa_pl.LinkDict)
        
class LoggedBy(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Used to indicate who created a log entry in what role.
    """

    _id_name : str = None
    party_uuid: str = pla.Field()
    """
    A machine-oriented identifier reference to the party who is making the log entry.
    """
    
    role_id: Optional[str] = pla.Field(nullable=True, )
    """
    A reference to a role by its identifier.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    
class RiskResponseReference(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Identifies an individual risk response that this log entry is for.
    """

    _id_name : str = None
    response_uuid: str = pla.Field()
    """
    A machine-oriented identifier reference to a unique risk response.
    """
    
    related_tasks: Optional[List] = pla.Field(nullable=True, )
    """
    Identifies tasks for which the containing object is a consequence.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    
    @pla.check("related_tasks")
    def check_nested_struct_related_tasks(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, RelatedTask, pa_pl.RelatedTaskDict)
        
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Property, pa_pl.PropertyDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Link, pa_pl.LinkDict)
        
class RiskLogEntry(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Identifies an individual risk response that occurred as part of managing an identified risk.
    """

    _id_name : str = None
    uuid: str = pla.Field()
    """
    A machine-oriented, globally unique identifier with a cross-instance scope.
    """
    
    title: Optional[str] = pla.Field(nullable=True, )
    """
    A human-readable name or title.
    """
    
    description: Optional[str] = pla.Field(nullable=True, )
    """
    A human-readable description.
    """
    
    start: DateTime() = pla.Field()
    """
    The start date/time.
    """
    
    end: Optional[DateTime()] = pla.Field(nullable=True, )
    """
    The end date/time.
    """
    
    logged_by: Optional[List] = pla.Field(nullable=True, )
    """
    Used to indicate who created a log entry in what role.
    """
    
    status_change: Optional[str] = pla.Field(nullable=True, )
    """
    Identifies the risk change that prompted the log entry. Recommended values are in RiskStatusEnum; other values are permitted (OSCAL allow-other="yes").
    """
    
    related_responses: Optional[List] = pla.Field(nullable=True, )
    """
    Identifies an individual risk response that this log entry is for.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    
    @pla.check("logged_by")
    def check_nested_struct_logged_by(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, LoggedBy, pa_pl.LoggedByDict)
        
    @pla.check("related_responses")
    def check_nested_struct_related_responses(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, RiskResponseReference, pa_pl.RiskResponseReferenceDict)
        
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Property, pa_pl.PropertyDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Link, pa_pl.LinkDict)
        
class RiskLog(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A log of all risk-related tasks taken.
    """

    _id_name : str = None
    entries: List = pla.Field()
    """
    Identifies an individual risk response that occurred as part of managing an identified risk.
    """
    
    
    @pla.check("entries")
    def check_nested_struct_entries(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, RiskLogEntry, pa_pl.RiskLogEntryDict)
        
class Risk(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    An identified risk.
    """

    _id_name : str = None
    uuid: str = pla.Field()
    """
    A machine-oriented, globally unique identifier with a cross-instance scope.
    """
    
    title: str = pla.Field()
    """
    A human-readable name or title.
    """
    
    description: str = pla.Field()
    """
    A human-readable description.
    """
    
    statement: str = pla.Field()
    """
    An assessor's summary of the risk, in narrative form.
    """
    
    origins: Optional[List] = pla.Field(nullable=True, )
    """
    Identifies the source of observations, findings, or risks.
    """
    
    threat_ids: Optional[List] = pla.Field(nullable=True, )
    """
    The referenced threat identifiers.
    """
    
    characterizations: Optional[List] = pla.Field(nullable=True, )
    """
    Supporting information about the risk and how it relates to the system.
    """
    
    mitigating_factors: Optional[List] = pla.Field(nullable=True, )
    """
    Describes existing mitigating factors that may affect the overall determination of the risk.
    """
    
    deadline: Optional[DateTime()] = pla.Field(nullable=True, )
    """
    The date/time by which the risk must be resolved.
    """
    
    remediations: Optional[List] = pla.Field(nullable=True, )
    """
    Describes either recommended or actual responses to a risk.
    """
    
    risk_log: Optional[Struct] = pla.Field(nullable=True, )
    """
    A log of all risk-related tasks taken.
    """
    
    related_observations: Optional[List] = pla.Field(nullable=True, )
    """
    Relates the containing object to a set of referenced observations.
    """
    
    status: str = pla.Field()
    """
    Status indicator used by the containing OSCAL context. Allowed values are constrained by class-level slot_usage.
    """
    
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    
    @pla.check("origins")
    def check_nested_struct_origins(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Origin, pa_pl.OriginDict)
        
    @pla.check("threat_ids")
    def check_nested_struct_threat_ids(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, ThreatId, pa_pl.ThreatIdDict)
        
    @pla.check("characterizations")
    def check_nested_struct_characterizations(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Characterization, pa_pl.CharacterizationDict)
        
    @pla.check("mitigating_factors")
    def check_nested_struct_mitigating_factors(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, MitigatingFactor, pa_pl.MitigatingFactorDict)
        
    @pla.check("remediations")
    def check_nested_struct_remediations(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Response, pa_pl.ResponseDict)
        
    @pla.check("risk_log")
    def check_nested_struct_risk_log(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, RiskLog, pa_pl.RiskLog)
        
    @pla.check("related_observations")
    def check_nested_struct_related_observations(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, RelatedObservation, pa_pl.RelatedObservationDict)
        
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Property, pa_pl.PropertyDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Link, pa_pl.LinkDict)
        
class ImportProfile(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Used to import the OSCAL profile representing the system's control baseline.
    """

    _id_name : str = None
    href: str = pla.Field()
    """
    A resolvable URL reference to a resource.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    
class SystemId(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A human-oriented, globally unique identifier for a system.
    """

    _id_name : str = None
    id: str = pla.Field()
    """
    A unique human-oriented identifier within a particular context.
    """
    
    identifier_type: Optional[str] = pla.Field(nullable=True, )
    """
    A human-readable label for a specific identifier scheme. Recommended values are in SystemIdentifierTypeEnum; other URI values are permitted (OSCAL allow-other="yes").
    """
    
    
class SspSystemInformationProp(Property):
    """
    SSP-scoped property used in system information.
    """

    _id_name : str = None
    pass
    
    
class SspSystemInformationLink(Link):
    """
    SSP-scoped link used in system information.
    """

    _id_name : str = None
    pass
    
    
class InformationTypeCategorization(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A set of information type identifiers qualified by the given identification system used.
    """

    _id_name : str = None
    system: str = pla.Field()
    """
    Specifies the information type identification system used. Recommended values are in InformationTypeCategorizationSystemEnum; other values are permitted (OSCAL allow-other="yes").
    """
    
    information_type_ids: Optional[str] = pla.Field(nullable=True, )
    """
    An identifier qualified by the given identification system used, such as NIST SP 800-60.
    """
    
    
class ImpactLevel(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    The expected level of impact resulting from the described information's confidentiality, integrity, or availability affect.
    """

    _id_name : str = None
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    base: str = pla.Field()
    """
    The prescribed base (Confidentiality, Integrity, or Availability) security impact level.
    """
    
    selected: Optional[str] = pla.Field(nullable=True, )
    """
    The selected (Confidentiality, Integrity, or Availability) security impact level.
    """
    
    adjustment_justification: Optional[str] = pla.Field(nullable=True, )
    """
    If the selected security level is different from the base security level, this contains the justification for the change.
    """
    
    
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Property, pa_pl.PropertyDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Link, pa_pl.LinkDict)
        
class InformationType(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Contains details about one information type that is stored, processed, or transmitted by the system, such as privacy information, and its impact level.
    """

    _id_name : str = None
    uuid: Optional[str] = pla.Field(nullable=True, )
    """
    A machine-oriented, globally unique identifier with a cross-instance scope.
    """
    
    title: str = pla.Field()
    """
    A human-readable name or title.
    """
    
    description: str = pla.Field()
    """
    A human-readable description.
    """
    
    categorizations: Optional[List] = pla.Field(nullable=True, )
    """
    A set of information type identifiers qualified by the given identification system used.
    """
    
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    confidentiality_impact: Optional[Struct] = pla.Field(nullable=True, )
    """
    The expected level of impact resulting from the unauthorized disclosure of the described information.
    """
    
    integrity_impact: Optional[Struct] = pla.Field(nullable=True, )
    """
    The expected level of impact resulting from the unauthorized modification of the described information.
    """
    
    availability_impact: Optional[Struct] = pla.Field(nullable=True, )
    """
    The expected level of impact resulting from the disruption of access to or use of the described information or the information system.
    """
    
    
    @pla.check("categorizations")
    def check_nested_struct_categorizations(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, InformationTypeCategorization, pa_pl.InformationTypeCategorizationDict)
        
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Property, pa_pl.PropertyDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Link, pa_pl.LinkDict)
        
    @pla.check("confidentiality_impact")
    def check_nested_struct_confidentiality_impact(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, ImpactLevel, pa_pl.ImpactLevel)
        
    @pla.check("integrity_impact")
    def check_nested_struct_integrity_impact(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, ImpactLevel, pa_pl.ImpactLevel)
        
    @pla.check("availability_impact")
    def check_nested_struct_availability_impact(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, ImpactLevel, pa_pl.ImpactLevel)
        
class SystemInformation(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Contains details about all information types that are stored, processed, or transmitted by the system, such as privacy information.
    """

    _id_name : str = None
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    information_types: List = pla.Field()
    """
    Contains details about one information type that is stored, processed, or transmitted by the system.
    """
    
    
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, SspSystemInformationProp, pa_pl.SspSystemInformationPropDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, SspSystemInformationLink, pa_pl.SspSystemInformationLinkDict)
        
    @pla.check("information_types")
    def check_nested_struct_information_types(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, InformationType, pa_pl.InformationTypeDict)
        
class SecurityImpactLevel(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    The overall level of expected impact resulting from unauthorized disclosure, modification, or loss of access to information.
    """

    _id_name : str = None
    security_objective_confidentiality: str = pla.Field()
    """
    A target-level of confidentiality for the system, based on the sensitivity of information within the system.
    """
    
    security_objective_integrity: str = pla.Field()
    """
    A target-level of integrity for the system, based on the sensitivity of information within the system.
    """
    
    security_objective_availability: str = pla.Field()
    """
    A target-level of availability for the system, based on the sensitivity of information within the system.
    """
    
    
class SystemStatus(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Describes the operational status of the system.
    """

    _id_name : str = None
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    state: Enum = pla.Field(dtype_kwargs={"categories":('operational','under-development','under-major-modification','disposition','other',)})
    """
    The current operating status of the system.
    """
    
    
class SspDiagramLink(Link):
    """
    SSP-scoped link used in diagram objects.
    """

    _id_name : str = None
    pass
    
    
class Diagram(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A graphic that provides a visual representation the system, or some aspect of it.
    """

    _id_name : str = None
    uuid: str = pla.Field()
    """
    A machine-oriented, globally unique identifier with a cross-instance scope.
    """
    
    description: Optional[str] = pla.Field(nullable=True, )
    """
    A human-readable description.
    """
    
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    caption: Optional[str] = pla.Field(nullable=True, )
    """
    A brief caption to annotate the diagram.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Property, pa_pl.PropertyDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, SspDiagramLink, pa_pl.SspDiagramLinkDict)
        
class AuthorizationBoundary(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A description of this system's authorization boundary, optionally supplemented with diagrams that illustrate the authorization boundary.
    """

    _id_name : str = None
    description: str = pla.Field()
    """
    A human-readable description.
    """
    
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    diagrams: Optional[List] = pla.Field(nullable=True, )
    """
    A collection of diagrams that visually depict the subject.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Property, pa_pl.PropertyDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Link, pa_pl.LinkDict)
        
    @pla.check("diagrams")
    def check_nested_struct_diagrams(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Diagram, pa_pl.DiagramDict)
        
class NetworkArchitecture(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A description of the system's network architecture, optionally supplemented with diagrams that illustrate the network architecture.
    """

    _id_name : str = None
    description: str = pla.Field()
    """
    A human-readable description.
    """
    
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    diagrams: Optional[List] = pla.Field(nullable=True, )
    """
    A collection of diagrams that visually depict the subject.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Property, pa_pl.PropertyDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Link, pa_pl.LinkDict)
        
    @pla.check("diagrams")
    def check_nested_struct_diagrams(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Diagram, pa_pl.DiagramDict)
        
class DataFlow(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A description of the logical flow of information within the system and across its boundaries, optionally supplemented with diagrams.
    """

    _id_name : str = None
    description: str = pla.Field()
    """
    A human-readable description.
    """
    
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    diagrams: Optional[List] = pla.Field(nullable=True, )
    """
    A collection of diagrams that visually depict the subject.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Property, pa_pl.PropertyDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Link, pa_pl.LinkDict)
        
    @pla.check("diagrams")
    def check_nested_struct_diagrams(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Diagram, pa_pl.DiagramDict)
        
class SspSystemCharacteristicsResponsibleParty(ResponsibleParty):
    """
    SSP-scoped responsible party for system characteristics.
    """

    _id_name : str = None
    pass
    
    
class SystemCharacteristics(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Contains the characteristics of the system, such as its name, purpose, and security impact level.
    """

    _id_name : str = None
    system_ids: List = pla.Field()
    """
    Unique identifiers for the system.
    """
    
    system_name: str = pla.Field()
    """
    The full name of the system.
    """
    
    system_name_short: Optional[str] = pla.Field(nullable=True, )
    """
    A short name for the system, such as an acronym, that is suitable for display in a data table or summary list.
    """
    
    description: str = pla.Field()
    """
    A human-readable description.
    """
    
    date_authorized: Optional[str] = pla.Field(nullable=True, )
    """
    The date the system received its authorization.
    """
    
    security_sensitivity_level: Optional[str] = pla.Field(nullable=True, )
    """
    The overall information system sensitivity categorization, such as defined by FIPS-199.
    """
    
    system_information: Struct = pla.Field()
    """
    Contains details about all information types that are stored, processed, or transmitted by the system.
    """
    
    security_impact_level: Optional[Struct] = pla.Field(nullable=True, )
    """
    The overall level of expected impact resulting from unauthorized disclosure, modification, or loss of access to information.
    """
    
    system_status: Struct = pla.Field()
    """
    Describes the operational status of the system.
    """
    
    authorization_boundary: Struct = pla.Field()
    """
    A description of this system's authorization boundary, optionally supplemented with diagrams that illustrate the authorization boundary.
    """
    
    network_architecture: Optional[Struct] = pla.Field(nullable=True, )
    """
    A description of the system's network architecture, optionally supplemented with diagrams that illustrate the network architecture.
    """
    
    data_flow: Optional[Struct] = pla.Field(nullable=True, )
    """
    A description of the logical flow of information within the system and across its boundaries, optionally supplemented with diagrams.
    """
    
    responsible_parties: Optional[List] = pla.Field(nullable=True, )
    """
    Responsible party assignments.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    
    @pla.check("system_ids")
    def check_nested_struct_system_ids(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, SystemId, pa_pl.SystemIdDict)
        
    @pla.check("system_information")
    def check_nested_struct_system_information(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, SystemInformation, pa_pl.SystemInformation)
        
    @pla.check("security_impact_level")
    def check_nested_struct_security_impact_level(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, SecurityImpactLevel, pa_pl.SecurityImpactLevel)
        
    @pla.check("system_status")
    def check_nested_struct_system_status(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, SystemStatus, pa_pl.SystemStatus)
        
    @pla.check("authorization_boundary")
    def check_nested_struct_authorization_boundary(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, AuthorizationBoundary, pa_pl.AuthorizationBoundary)
        
    @pla.check("network_architecture")
    def check_nested_struct_network_architecture(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, NetworkArchitecture, pa_pl.NetworkArchitecture)
        
    @pla.check("data_flow")
    def check_nested_struct_data_flow(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, DataFlow, pa_pl.DataFlow)
        
    @pla.check("responsible_parties")
    def check_nested_struct_responsible_parties(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, SspSystemCharacteristicsResponsibleParty, pa_pl.SspSystemCharacteristicsResponsiblePartyDict)
        
class SspLeveragedAuthorizationLink(Link):
    """
    SSP-scoped link used in leveraged authorization objects.
    """

    _id_name : str = None
    pass
    
    
class LeveragedAuthorization(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A description of another authorized system from which this system inherits capabilities that satisfy security requirements. Another term for this concept is a common control provider.
    """

    _id_name : str = None
    uuid: str = pla.Field()
    """
    A machine-oriented, globally unique identifier with a cross-instance scope.
    """
    
    title: str = pla.Field()
    """
    A human-readable name or title.
    """
    
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    party_uuid: str = pla.Field()
    """
    A machine-oriented identifier reference to the party who is making the log entry.
    """
    
    date_authorized: str = pla.Field()
    """
    The date the system received its authorization.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Property, pa_pl.PropertyDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, SspLeveragedAuthorizationLink, pa_pl.SspLeveragedAuthorizationLinkDict)
        
class SspAllowsAuthenticatedScanProp(Property):
    """
    SSP-scoped property used for component and inventory allows-authenticated-scan.
    """

    _id_name : str = None
    pass
    
    
class SspSystemComponent(SystemComponent):
    """
    SSP-scoped system component with allows-authenticated-scan property typing.
    """

    _id_name : str = None
    pass
    
    
class SspInventoryItem(InventoryItem):
    """
    SSP-scoped inventory item with allows-authenticated-scan property typing.
    """

    _id_name : str = None
    pass
    
    
class SystemImplementation(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Provides information as to how the system is implemented.
    """

    _id_name : str = None
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    leveraged_authorizations: Optional[List] = pla.Field(nullable=True, )
    """
    A description of another authorized system from which this system inherits capabilities that satisfy security requirements.
    """
    
    users: Optional[List] = pla.Field(nullable=True, )
    """
    A collection of system users.
    """
    
    components: List = pla.Field()
    """
    A collection of system components.
    """
    
    inventory_items: Optional[List] = pla.Field(nullable=True, )
    """
    A collection of inventory items.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Property, pa_pl.PropertyDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Link, pa_pl.LinkDict)
        
    @pla.check("leveraged_authorizations")
    def check_nested_struct_leveraged_authorizations(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, LeveragedAuthorization, pa_pl.LeveragedAuthorizationDict)
        
    @pla.check("users")
    def check_nested_struct_users(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, SystemUser, pa_pl.SystemUserDict)
        
    @pla.check("components")
    def check_nested_struct_components(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, SspSystemComponent, pa_pl.SspSystemComponentDict)
        
    @pla.check("inventory_items")
    def check_nested_struct_inventory_items(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, SspInventoryItem, pa_pl.SspInventoryItemDict)
        
class SetParameter(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Identifies the parameter that will be set by the enclosed value.
    """

    _id_name : str = None
    param_id: str = pla.Field()
    """
    The identifier for the parameter being set or referenced.
    """
    
    values: str = pla.Field()
    """
    A parameter value or set of values.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    
class SspControlOriginationProp(Property):
    """
    SSP-scoped property used in implemented requirement and by-component contexts.
    """

    _id_name : str = None
    pass
    
    
class SspImplementedRequirementResponsibleRole(ResponsibleRole):
    """
    SSP-scoped responsible role used by implemented requirement and statement contexts.
    """

    _id_name : str = None
    pass
    
    
class SspByComponentLink(Link):
    """
    SSP-scoped link used in by-component contexts.
    """

    _id_name : str = None
    pass
    
    
class SspByComponentResponsibleRole(ResponsibleRole):
    """
    SSP-scoped responsible role used by by-component contexts.
    """

    _id_name : str = None
    pass
    
    
class ProvidedControlImplementation(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Describes a capability which may be inherited by a leveraging system.
    """

    _id_name : str = None
    uuid: str = pla.Field()
    """
    A machine-oriented, globally unique identifier with a cross-instance scope.
    """
    
    description: str = pla.Field()
    """
    A human-readable description.
    """
    
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    responsible_roles: Optional[List] = pla.Field(nullable=True, )
    """
    Responsible role assignments.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Property, pa_pl.PropertyDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Link, pa_pl.LinkDict)
        
    @pla.check("responsible_roles")
    def check_nested_struct_responsible_roles(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, SspByComponentResponsibleRole, pa_pl.SspByComponentResponsibleRoleDict)
        
class ControlResponsibility(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Describes a control implementation responsibility imposed on a leveraging system.
    """

    _id_name : str = None
    uuid: str = pla.Field()
    """
    A machine-oriented, globally unique identifier with a cross-instance scope.
    """
    
    provided_uuid: Optional[str] = pla.Field(nullable=True, )
    """
    Machine-oriented identifier reference to an inherited control implementation that a leveraging system is implementing.
    """
    
    description: str = pla.Field()
    """
    A human-readable description.
    """
    
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    responsible_roles: Optional[List] = pla.Field(nullable=True, )
    """
    Responsible role assignments.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Property, pa_pl.PropertyDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Link, pa_pl.LinkDict)
        
    @pla.check("responsible_roles")
    def check_nested_struct_responsible_roles(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, SspByComponentResponsibleRole, pa_pl.SspByComponentResponsibleRoleDict)
        
class Export(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Defines a set of control implementations that are provided as reference implementations for use by organizations implementing the leveraged system.
    """

    _id_name : str = None
    description: Optional[str] = pla.Field(nullable=True, )
    """
    A human-readable description.
    """
    
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    provided: Optional[List] = pla.Field(nullable=True, )
    """
    Describes a capability which may be inherited by a leveraging system.
    """
    
    responsibilities: Optional[List] = pla.Field(nullable=True, )
    """
    Describes a control implementation responsibility imposed on a leveraging system.
    """
    
    
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Property, pa_pl.PropertyDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Link, pa_pl.LinkDict)
        
    @pla.check("provided")
    def check_nested_struct_provided(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, ProvidedControlImplementation, pa_pl.ProvidedControlImplementationDict)
        
    @pla.check("responsibilities")
    def check_nested_struct_responsibilities(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, ControlResponsibility, pa_pl.ControlResponsibilityDict)
        
class InheritedControlImplementation(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Describes a control implementation inherited by a leveraging system.
    """

    _id_name : str = None
    uuid: str = pla.Field()
    """
    A machine-oriented, globally unique identifier with a cross-instance scope.
    """
    
    provided_uuid: Optional[str] = pla.Field(nullable=True, )
    """
    Machine-oriented identifier reference to an inherited control implementation that a leveraging system is implementing.
    """
    
    description: str = pla.Field()
    """
    A human-readable description.
    """
    
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    responsible_roles: Optional[List] = pla.Field(nullable=True, )
    """
    Responsible role assignments.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Property, pa_pl.PropertyDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Link, pa_pl.LinkDict)
        
    @pla.check("responsible_roles")
    def check_nested_struct_responsible_roles(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, SspByComponentResponsibleRole, pa_pl.SspByComponentResponsibleRoleDict)
        
class SatisfiedControlImplementation(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Describes how this system satisfies a responsibility imposed by a leveraged system.
    """

    _id_name : str = None
    uuid: str = pla.Field()
    """
    A machine-oriented, globally unique identifier with a cross-instance scope.
    """
    
    responsibility_uuid: Optional[str] = pla.Field(nullable=True, )
    """
    Machine-oriented identifier reference to a control implementation responsibility imposed by a leveraged system.
    """
    
    description: str = pla.Field()
    """
    A human-readable description.
    """
    
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    responsible_roles: Optional[List] = pla.Field(nullable=True, )
    """
    Responsible role assignments.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Property, pa_pl.PropertyDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Link, pa_pl.LinkDict)
        
    @pla.check("responsible_roles")
    def check_nested_struct_responsible_roles(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, SspByComponentResponsibleRole, pa_pl.SspByComponentResponsibleRoleDict)
        
class ByComponent(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Defines how the referenced component implements a set of controls.
    """

    _id_name : str = None
    component_uuid: str = pla.Field()
    """
    A UUID reference to a component.
    """
    
    uuid: str = pla.Field()
    """
    A machine-oriented, globally unique identifier with a cross-instance scope.
    """
    
    description: str = pla.Field()
    """
    A human-readable description.
    """
    
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    set_parameters: Optional[List] = pla.Field(nullable=True, )
    """
    Identifies the parameter that will be set by the enclosed value.
    """
    
    implementation_status: Optional[Struct] = pla.Field(nullable=True, )
    """
    Identifies the implementation status of the control.
    """
    
    export: Optional[Struct] = pla.Field(nullable=True, )
    """
    Defines a set of control implementations that are provided as reference implementations for use by organizations implementing the leveraged system.
    """
    
    inherited: Optional[List] = pla.Field(nullable=True, )
    """
    Describes a control implementation inherited by a leveraging system.
    """
    
    satisfied: Optional[List] = pla.Field(nullable=True, )
    """
    Describes how this system satisfies a responsibility imposed by a leveraged system.
    """
    
    responsible_roles: Optional[List] = pla.Field(nullable=True, )
    """
    Responsible role assignments.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, SspControlOriginationProp, pa_pl.SspControlOriginationPropDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, SspByComponentLink, pa_pl.SspByComponentLinkDict)
        
    @pla.check("set_parameters")
    def check_nested_struct_set_parameters(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, SetParameter, pa_pl.SetParameterDict)
        
    @pla.check("implementation_status")
    def check_nested_struct_implementation_status(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, ImplementationStatus, pa_pl.ImplementationStatus)
        
    @pla.check("export")
    def check_nested_struct_export(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, Export, pa_pl.Export)
        
    @pla.check("inherited")
    def check_nested_struct_inherited(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, InheritedControlImplementation, pa_pl.InheritedControlImplementationDict)
        
    @pla.check("satisfied")
    def check_nested_struct_satisfied(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, SatisfiedControlImplementation, pa_pl.SatisfiedControlImplementationDict)
        
    @pla.check("responsible_roles")
    def check_nested_struct_responsible_roles(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, SspByComponentResponsibleRole, pa_pl.SspByComponentResponsibleRoleDict)
        
class SspStatement(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Identifies which statements within a control are addressed.
    """

    _id_name : str = None
    statement_id: str = pla.Field()
    """
    A reference to a control statement identifier.
    """
    
    uuid: str = pla.Field()
    """
    A machine-oriented, globally unique identifier with a cross-instance scope.
    """
    
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    responsible_roles: Optional[List] = pla.Field(nullable=True, )
    """
    Responsible role assignments.
    """
    
    by_components: Optional[List] = pla.Field(nullable=True, )
    """
    Defines how the referenced component implements a set of controls.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, SspControlOriginationProp, pa_pl.SspControlOriginationPropDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Link, pa_pl.LinkDict)
        
    @pla.check("responsible_roles")
    def check_nested_struct_responsible_roles(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, SspImplementedRequirementResponsibleRole, pa_pl.SspImplementedRequirementResponsibleRoleDict)
        
    @pla.check("by_components")
    def check_nested_struct_by_components(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, ByComponent, pa_pl.ByComponentDict)
        
class SspImplementedRequirement(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Describes how the system satisfies an individual control.
    """

    _id_name : str = None
    uuid: str = pla.Field()
    """
    A machine-oriented, globally unique identifier with a cross-instance scope.
    """
    
    control_id: str = pla.Field()
    """
    A reference to a control by its identifier.
    """
    
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    set_parameters: Optional[List] = pla.Field(nullable=True, )
    """
    Identifies the parameter that will be set by the enclosed value.
    """
    
    responsible_roles: Optional[List] = pla.Field(nullable=True, )
    """
    Responsible role assignments.
    """
    
    statements: Optional[List] = pla.Field(nullable=True, )
    """
    Control statement implementation entries in the containing OSCAL context. The concrete entry class is selected by class-level slot_usage.
    """
    
    by_components: Optional[List] = pla.Field(nullable=True, )
    """
    Defines how the referenced component implements a set of controls.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, SspControlOriginationProp, pa_pl.SspControlOriginationPropDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Link, pa_pl.LinkDict)
        
    @pla.check("set_parameters")
    def check_nested_struct_set_parameters(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, SetParameter, pa_pl.SetParameterDict)
        
    @pla.check("responsible_roles")
    def check_nested_struct_responsible_roles(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, SspImplementedRequirementResponsibleRole, pa_pl.SspImplementedRequirementResponsibleRoleDict)
        
    @pla.check("statements")
    def check_nested_struct_statements(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, SspStatement, pa_pl.SspStatementDict)
        
    @pla.check("by_components")
    def check_nested_struct_by_components(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, ByComponent, pa_pl.ByComponentDict)
        
class SspControlImplementation(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Describes how the system satisfies a set of controls.
    """

    _id_name : str = None
    description: str = pla.Field()
    """
    A human-readable description.
    """
    
    set_parameters: Optional[List] = pla.Field(nullable=True, )
    """
    Identifies the parameter that will be set by the enclosed value.
    """
    
    implemented_requirements: List = pla.Field()
    """
    Control implementation requirement entries in the containing OSCAL context. The concrete entry class is selected by class-level slot_usage.
    """
    
    
    @pla.check("set_parameters")
    def check_nested_struct_set_parameters(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, SetParameter, pa_pl.SetParameterDict)
        
    @pla.check("implemented_requirements")
    def check_nested_struct_implemented_requirements(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, SspImplementedRequirement, pa_pl.SspImplementedRequirementDict)
        
class SystemSecurityPlan(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A system security plan, such as those described in NIST SP 800-18.
    """

    _id_name : str = None
    uuid: str = pla.Field()
    """
    A machine-oriented, globally unique identifier with a cross-instance scope.
    """
    
    metadata: Struct = pla.Field()
    """
    Provides information about the containing document, and defines concepts shared across the document.
    """
    
    import_profile: Struct = pla.Field()
    """
    Used to import the OSCAL profile representing the system's control baseline.
    """
    
    system_characteristics: Struct = pla.Field()
    """
    Contains the characteristics of the system, such as its name, purpose, and security impact level.
    """
    
    system_implementation: Struct = pla.Field()
    """
    Provides information as to how the system is implemented.
    """
    
    control_implementation: Struct = pla.Field()
    """
    Describes how the system satisfies a set of controls.
    """
    
    back_matter: Optional[Struct] = pla.Field(nullable=True, )
    """
    A collection of resources that may be referenced from within the OSCAL document instance.
    """
    
    
    @pla.check("metadata")
    def check_nested_struct_metadata(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, Metadata, pa_pl.Metadata)
        
    @pla.check("import_profile")
    def check_nested_struct_import_profile(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, ImportProfile, pa_pl.ImportProfile)
        
    @pla.check("system_characteristics")
    def check_nested_struct_system_characteristics(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, SystemCharacteristics, pa_pl.SystemCharacteristics)
        
    @pla.check("system_implementation")
    def check_nested_struct_system_implementation(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, SystemImplementation, pa_pl.SystemImplementation)
        
    @pla.check("control_implementation")
    def check_nested_struct_control_implementation(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, SspControlImplementation, pa_pl.SspControlImplementation)
        
    @pla.check("back_matter")
    def check_nested_struct_back_matter(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, BackMatter, pa_pl.BackMatter)
        
class SspDocument(OscalDocument):
    """
    Root wrapper for an OSCAL System Security Plan document.
    """

    _id_name : str = None
    system_security_plan: Struct = pla.Field()
    """
    A system security plan, such as those described in NIST SP 800-18.
    """
    
    
    @pla.check("system_security_plan")
    def check_nested_struct_system_security_plan(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, SystemSecurityPlan, pa_pl.SystemSecurityPlan)
        
class ImportAssessmentPlan(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Used by assessment-results to import information about the original plan for assessing the system.
    """

    _id_name : str = None
    href: str = pla.Field()
    """
    A resolvable URL reference to a resource.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    
class AssessmentResultsLocalDefinitions(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Used to define data objects that are referenced by the assessment results but do not appear in the imported assessment plan.
    """

    _id_name : str = None
    objectives_and_methods: Optional[List] = pla.Field(nullable=True, )
    """
    A collection of locally-defined control objectives.
    """
    
    activities: Optional[List] = pla.Field(nullable=True, )
    """
    A collection of activities.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    
    @pla.check("objectives_and_methods")
    def check_nested_struct_objectives_and_methods(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, LocalObjective, pa_pl.LocalObjectiveDict)
        
    @pla.check("activities")
    def check_nested_struct_activities(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Activity, pa_pl.ActivityDict)
        
class ResultLocalDefinitions(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Used to define local implementation and assessment assets referenced by a result that do not appear in the imported system security plan.
    """

    _id_name : str = None
    components: Optional[List] = pla.Field(nullable=True, )
    """
    A collection of system components.
    """
    
    inventory_items: Optional[List] = pla.Field(nullable=True, )
    """
    A collection of inventory items.
    """
    
    users: Optional[List] = pla.Field(nullable=True, )
    """
    A collection of system users.
    """
    
    assessment_assets: Optional[Struct] = pla.Field(nullable=True, )
    """
    Identifies the assets used to perform this assessment.
    """
    
    tasks: Optional[List] = pla.Field(nullable=True, )
    """
    A collection of tasks.
    """
    
    
    @pla.check("components")
    def check_nested_struct_components(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, SystemComponent, pa_pl.SystemComponentDict)
        
    @pla.check("inventory_items")
    def check_nested_struct_inventory_items(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, InventoryItem, pa_pl.InventoryItemDict)
        
    @pla.check("users")
    def check_nested_struct_users(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, SystemUser, pa_pl.SystemUserDict)
        
    @pla.check("assessment_assets")
    def check_nested_struct_assessment_assets(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, AssessmentAssets, pa_pl.AssessmentAssets)
        
    @pla.check("tasks")
    def check_nested_struct_tasks(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Task, pa_pl.TaskDict)
        
class Attestation(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A set of textual attestation statements, typically written by the assessor.
    """

    _id_name : str = None
    parts: List = pla.Field()
    """
    A collection of parts.
    """
    
    responsible_parties: Optional[List] = pla.Field(nullable=True, )
    """
    Responsible party assignments.
    """
    
    
    @pla.check("parts")
    def check_nested_struct_parts(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, AssessmentPart, pa_pl.AssessmentPartDict)
        
    @pla.check("responsible_parties")
    def check_nested_struct_responsible_parties(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, ResponsibleParty, pa_pl.ResponsiblePartyDict)
        
class AssessmentLogEntry(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Identifies the result of an action and/or task that occurred as part of executing an assessment plan or assessment event.
    """

    _id_name : str = None
    uuid: str = pla.Field()
    """
    A machine-oriented, globally unique identifier with a cross-instance scope.
    """
    
    title: Optional[str] = pla.Field(nullable=True, )
    """
    A human-readable name or title.
    """
    
    description: Optional[str] = pla.Field(nullable=True, )
    """
    A human-readable description.
    """
    
    start: DateTime() = pla.Field()
    """
    The start date/time.
    """
    
    end: Optional[DateTime()] = pla.Field(nullable=True, )
    """
    The end date/time.
    """
    
    logged_by: Optional[List] = pla.Field(nullable=True, )
    """
    Used to indicate who created a log entry in what role.
    """
    
    related_tasks: Optional[List] = pla.Field(nullable=True, )
    """
    Identifies tasks for which the containing object is a consequence.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    
    @pla.check("logged_by")
    def check_nested_struct_logged_by(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, LoggedBy, pa_pl.LoggedByDict)
        
    @pla.check("related_tasks")
    def check_nested_struct_related_tasks(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, RelatedTask, pa_pl.RelatedTaskDict)
        
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Property, pa_pl.PropertyDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Link, pa_pl.LinkDict)
        
class AssessmentLog(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A log of all assessment-related actions taken.
    """

    _id_name : str = None
    entries: List = pla.Field()
    """
    Identifies an individual risk response that occurred as part of managing an identified risk.
    """
    
    
    @pla.check("entries")
    def check_nested_struct_entries(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, AssessmentLogEntry, pa_pl.AssessmentLogEntryDict)
        
class Result(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Identifies all of the assessment observations and findings, initial and residual risks, deviations, and disposition for a particular execution of the assessment.
    """

    _id_name : str = None
    uuid: str = pla.Field()
    """
    A machine-oriented, globally unique identifier with a cross-instance scope.
    """
    
    title: str = pla.Field()
    """
    A human-readable name or title.
    """
    
    description: str = pla.Field()
    """
    A human-readable description.
    """
    
    start: DateTime() = pla.Field()
    """
    The start date/time.
    """
    
    end: Optional[DateTime()] = pla.Field(nullable=True, )
    """
    The end date/time.
    """
    
    local_definitions: Optional[Struct] = pla.Field(nullable=True, )
    """
    Used to define data objects that do not appear in the referenced SSP.
    """
    
    reviewed_controls: Struct = pla.Field()
    """
    Identifies the controls being assessed and their control objectives.
    """
    
    attestations: Optional[List] = pla.Field(nullable=True, )
    """
    A set of attestation statements for the result.
    """
    
    assessment_log: Optional[Struct] = pla.Field(nullable=True, )
    """
    A log of assessment-related actions taken.
    """
    
    observations: Optional[List] = pla.Field(nullable=True, )
    """
    A collection of observations captured in the containing context.
    """
    
    risks: Optional[List] = pla.Field(nullable=True, )
    """
    A collection of risks captured in the containing context.
    """
    
    findings: Optional[List] = pla.Field(nullable=True, )
    """
    A collection of findings captured in the containing context.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    
    @pla.check("local_definitions")
    def check_nested_struct_local_definitions(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, ResultLocalDefinitions, pa_pl.ResultLocalDefinitions)
        
    @pla.check("reviewed_controls")
    def check_nested_struct_reviewed_controls(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, ReviewedControls, pa_pl.ReviewedControls)
        
    @pla.check("attestations")
    def check_nested_struct_attestations(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Attestation, pa_pl.AttestationDict)
        
    @pla.check("assessment_log")
    def check_nested_struct_assessment_log(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, AssessmentLog, pa_pl.AssessmentLog)
        
    @pla.check("observations")
    def check_nested_struct_observations(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Observation, pa_pl.ObservationDict)
        
    @pla.check("risks")
    def check_nested_struct_risks(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Risk, pa_pl.RiskDict)
        
    @pla.check("findings")
    def check_nested_struct_findings(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Finding, pa_pl.FindingDict)
        
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Property, pa_pl.PropertyDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Link, pa_pl.LinkDict)
        
class AssessmentResults(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Security assessment results, such as those provided by a FedRAMP assessor in a security assessment report.
    """

    _id_name : str = None
    uuid: str = pla.Field()
    """
    Assessment Results Universally Unique Identifier.
    """
    
    metadata: Struct = pla.Field()
    """
    Provides information about the containing document, and defines concepts shared across the document.
    """
    
    import_ap: Struct = pla.Field()
    """
    Used to import information about the governing assessment plan.
    """
    
    local_definitions: Optional[Struct] = pla.Field(nullable=True, )
    """
    Used to define data objects that do not appear in the referenced SSP.
    """
    
    results: List = pla.Field()
    """
    A collection of assessment results.
    """
    
    back_matter: Optional[Struct] = pla.Field(nullable=True, )
    """
    A collection of resources that may be referenced from within the OSCAL document instance.
    """
    
    
    @pla.check("metadata")
    def check_nested_struct_metadata(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, Metadata, pa_pl.Metadata)
        
    @pla.check("import_ap")
    def check_nested_struct_import_ap(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, ImportAssessmentPlan, pa_pl.ImportAssessmentPlan)
        
    @pla.check("local_definitions")
    def check_nested_struct_local_definitions(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, AssessmentResultsLocalDefinitions, pa_pl.AssessmentResultsLocalDefinitions)
        
    @pla.check("results")
    def check_nested_struct_results(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Result, pa_pl.ResultDict)
        
    @pla.check("back_matter")
    def check_nested_struct_back_matter(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, BackMatter, pa_pl.BackMatter)
        
class AssessmentResultsDocument(OscalDocument):
    """
    Root wrapper for an OSCAL Assessment Results document.
    """

    _id_name : str = None
    assessment_results: Struct = pla.Field()
    """
    The root assessment results object.
    """
    
    
    @pla.check("assessment_results")
    def check_nested_struct_assessment_results(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, AssessmentResults, pa_pl.AssessmentResults)
        
class ImportComponentDefinition(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Loads a component definition from another resource.
    """

    _id_name : str = None
    href: str = pla.Field()
    """
    A resolvable URL reference to a resource.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    
class ImplementedControlStatement(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Identifies which statements within a control are addressed.
    """

    _id_name : str = None
    statement_id: str = pla.Field()
    """
    A reference to a control statement identifier.
    """
    
    uuid: str = pla.Field()
    """
    A machine-oriented, globally unique identifier with a cross-instance scope.
    """
    
    description: str = pla.Field()
    """
    A human-readable description.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    responsible_roles: Optional[List] = pla.Field(nullable=True, )
    """
    Responsible role assignments.
    """
    
    
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Property, pa_pl.PropertyDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Link, pa_pl.LinkDict)
        
    @pla.check("responsible_roles")
    def check_nested_struct_responsible_roles(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, ResponsibleRole, pa_pl.ResponsibleRoleDict)
        
class ImplementedRequirement(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Describes how the containing component or capability implements an individual control.
    """

    _id_name : str = None
    uuid: str = pla.Field()
    """
    A machine-oriented, globally unique identifier with a cross-instance scope.
    """
    
    control_id: str = pla.Field()
    """
    A reference to a control by its identifier.
    """
    
    description: str = pla.Field()
    """
    A human-readable description.
    """
    
    set_parameters: Optional[List] = pla.Field(nullable=True, )
    """
    Parameter values applied in the containing implementation context.
    """
    
    statements: Optional[List] = pla.Field(nullable=True, )
    """
    Control statement implementation entries in the containing OSCAL context. The concrete entry class is selected by class-level slot_usage.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    responsible_roles: Optional[List] = pla.Field(nullable=True, )
    """
    Responsible role assignments.
    """
    
    
    @pla.check("set_parameters")
    def check_nested_struct_set_parameters(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, SetParameter, pa_pl.SetParameterDict)
        
    @pla.check("statements")
    def check_nested_struct_statements(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, ImplementedControlStatement, pa_pl.ImplementedControlStatementDict)
        
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Property, pa_pl.PropertyDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Link, pa_pl.LinkDict)
        
    @pla.check("responsible_roles")
    def check_nested_struct_responsible_roles(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, ResponsibleRole, pa_pl.ResponsibleRoleDict)
        
class ControlImplementationSet(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Defines how the component or capability supports a set of controls.
    """

    _id_name : str = None
    uuid: str = pla.Field()
    """
    A machine-oriented, globally unique identifier with a cross-instance scope.
    """
    
    source: str = pla.Field()
    """
    Reference to an external catalog or profile resource.
    """
    
    description: str = pla.Field()
    """
    A human-readable description.
    """
    
    set_parameters: Optional[List] = pla.Field(nullable=True, )
    """
    Parameter values applied in the containing implementation context.
    """
    
    implemented_requirements: List = pla.Field()
    """
    Control implementation requirement entries in the containing OSCAL context. The concrete entry class is selected by class-level slot_usage.
    """
    
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    
    @pla.check("set_parameters")
    def check_nested_struct_set_parameters(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, SetParameter, pa_pl.SetParameterDict)
        
    @pla.check("implemented_requirements")
    def check_nested_struct_implemented_requirements(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, ImplementedRequirement, pa_pl.ImplementedRequirementDict)
        
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Property, pa_pl.PropertyDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Link, pa_pl.LinkDict)
        
class DefinedComponent(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A defined component that can be part of an implemented system.
    """

    _id_name : str = None
    uuid: str = pla.Field()
    """
    A machine-oriented, globally unique identifier with a cross-instance scope.
    """
    
    type: str = pla.Field()
    """
    Indicates the nature or kind of the containing object.
    """
    
    title: str = pla.Field()
    """
    A human-readable name or title.
    """
    
    description: str = pla.Field()
    """
    A human-readable description.
    """
    
    purpose: Optional[str] = pla.Field(nullable=True, )
    """
    A summary of the technological or business purpose of the component.
    """
    
    protocols: Optional[List] = pla.Field(nullable=True, )
    """
    Information about the protocol used to provide a service.
    """
    
    control_implementations: Optional[List] = pla.Field(nullable=True, )
    """
    Control implementation sets for a component or capability.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    responsible_roles: Optional[List] = pla.Field(nullable=True, )
    """
    Responsible role assignments.
    """
    
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    
    @pla.check("protocols")
    def check_nested_struct_protocols(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Protocol, pa_pl.ProtocolDict)
        
    @pla.check("control_implementations")
    def check_nested_struct_control_implementations(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, ControlImplementationSet, pa_pl.ControlImplementationSetDict)
        
    @pla.check("responsible_roles")
    def check_nested_struct_responsible_roles(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, ResponsibleRole, pa_pl.ResponsibleRoleDict)
        
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Property, pa_pl.PropertyDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Link, pa_pl.LinkDict)
        
class IncorporatesComponent(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    The collection of components comprising a capability.
    """

    _id_name : str = None
    component_uuid: str = pla.Field()
    """
    A UUID reference to a component.
    """
    
    description: str = pla.Field()
    """
    A human-readable description.
    """
    
    
class Capability(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A grouping of other components and/or capabilities.
    """

    _id_name : str = None
    uuid: str = pla.Field()
    """
    A machine-oriented, globally unique identifier with a cross-instance scope.
    """
    
    name: str = pla.Field()
    """
    A textual label that uniquely identifies an attribute or semantic type.
    """
    
    description: str = pla.Field()
    """
    A human-readable description.
    """
    
    incorporates_components: Optional[List] = pla.Field(nullable=True, )
    """
    Component references incorporated by a capability.
    """
    
    control_implementations: Optional[List] = pla.Field(nullable=True, )
    """
    Control implementation sets for a component or capability.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    
    @pla.check("incorporates_components")
    def check_nested_struct_incorporates_components(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, IncorporatesComponent, pa_pl.IncorporatesComponentDict)
        
    @pla.check("control_implementations")
    def check_nested_struct_control_implementations(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, ControlImplementationSet, pa_pl.ControlImplementationSetDict)
        
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Property, pa_pl.PropertyDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Link, pa_pl.LinkDict)
        
class ComponentDefinition(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A collection of component descriptions, which may optionally be grouped by capability.
    """

    _id_name : str = None
    uuid: str = pla.Field()
    """
    A machine-oriented, globally unique identifier with a cross-instance scope.
    """
    
    metadata: Struct = pla.Field()
    """
    Provides information about the containing document, and defines concepts shared across the document.
    """
    
    import_component_definitions: Optional[List] = pla.Field(nullable=True, )
    """
    Component-definition resources imported into this document.
    """
    
    components: Optional[List] = pla.Field(nullable=True, )
    """
    A collection of system components.
    """
    
    capabilities: Optional[List] = pla.Field(nullable=True, )
    """
    Capability groupings for the defined components.
    """
    
    back_matter: Optional[Struct] = pla.Field(nullable=True, )
    """
    A collection of resources that may be referenced from within the OSCAL document instance.
    """
    
    
    @pla.check("metadata")
    def check_nested_struct_metadata(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, Metadata, pa_pl.Metadata)
        
    @pla.check("import_component_definitions")
    def check_nested_struct_import_component_definitions(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, ImportComponentDefinition, pa_pl.ImportComponentDefinitionDict)
        
    @pla.check("components")
    def check_nested_struct_components(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, DefinedComponent, pa_pl.DefinedComponentDict)
        
    @pla.check("capabilities")
    def check_nested_struct_capabilities(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Capability, pa_pl.CapabilityDict)
        
    @pla.check("back_matter")
    def check_nested_struct_back_matter(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, BackMatter, pa_pl.BackMatter)
        
class ComponentDefinitionDocument(OscalDocument):
    """
    Root wrapper for an OSCAL Component Definition document.
    """

    _id_name : str = None
    component_definition: Struct = pla.Field()
    """
    The root component-definition object.
    """
    
    
    @pla.check("component_definition")
    def check_nested_struct_component_definition(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, ComponentDefinition, pa_pl.ComponentDefinition)
        
class ConfidenceScore(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Confidence represented as a category and/or percentage value.
    """

    _id_name : str = None
    category: Optional[str] = pla.Field(nullable=True, )
    """
    Confidence category label or qualifier category value.
    """
    
    percentage: Optional[float] = pla.Field(ge=0, le=1, nullable=True, )
    """
    A decimal percentage value in the range 0 to 1.
    """
    
    
class Coverage(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A percentage representing target coverage by source mappings.
    """

    _id_name : str = None
    generation_method: Optional[str] = pla.Field(nullable=True, )
    """
    Method used to determine the coverage value. Recommended values are in CoverageGenerationMethodEnum; other values are permitted.
    """
    
    target_coverage: float = pla.Field(ge=0, le=1, )
    """
    Percentage coverage of targets by sources.
    """
    
    
class MappingProvenance(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Mapping-level provenance details and mapping defaults.
    """

    _id_name : str = None
    method: Enum = pla.Field(dtype_kwargs={"categories":('human','automation','hybrid',)})
    """
    Method indicator used by the containing OSCAL context. Allowed values are constrained by class-level slot_usage.
    """
    
    matching_rationale: Enum = pla.Field(dtype_kwargs={"categories":('syntactic','semantic','functional',)})
    """
    The rationale method used to relate mapped items.
    """
    
    status: Enum = pla.Field(dtype_kwargs={"categories":('complete','not-complete','draft','deprecated','superseded',)})
    """
    Status indicator used by the containing OSCAL context. Allowed values are constrained by class-level slot_usage.
    """
    
    confidence_score: Optional[Struct] = pla.Field(nullable=True, )
    """
    Confidence descriptor for a mapping.
    """
    
    coverage: Optional[Struct] = pla.Field(nullable=True, )
    """
    Coverage metadata for a mapping.
    """
    
    mapping_description: str = pla.Field()
    """
    Description of the context and intended use of the mapping.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    responsible_parties: Optional[List] = pla.Field(nullable=True, )
    """
    Responsible party assignments.
    """
    
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    
    @pla.check("confidence_score")
    def check_nested_struct_confidence_score(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, ConfidenceScore, pa_pl.ConfidenceScore)
        
    @pla.check("coverage")
    def check_nested_struct_coverage(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, Coverage, pa_pl.Coverage)
        
    @pla.check("responsible_parties")
    def check_nested_struct_responsible_parties(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, ResponsibleParty, pa_pl.ResponsiblePartyDict)
        
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Property, pa_pl.PropertyDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Link, pa_pl.LinkDict)
        
class MappingResourceReference(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A reference to the source or target resource for a mapping.
    """

    _id_name : str = None
    ns: Optional[str] = pla.Field(nullable=True, )
    """
    An optional namespace qualifying a name. Allows different organizations to associate distinct semantics with the same name.
    """
    
    type: str = pla.Field()
    """
    The semantic type of the referenced resource. OSCAL defines catalog and profile, while locally defined values are also permitted.
    """
    
    href: str = pla.Field()
    """
    A resolvable URL reference to a resource.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Property, pa_pl.PropertyDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Link, pa_pl.LinkDict)
        
class MappingItem(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A source or target item participating in a mapping entry.
    """

    _id_name : str = None
    type: Enum = pla.Field(dtype_kwargs={"categories":('control','statement',)})
    """
    Indicates the nature or kind of the containing object.
    """
    
    id_ref: str = pla.Field()
    """
    Identifier reference of a source/target subject.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Property, pa_pl.PropertyDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Link, pa_pl.LinkDict)
        
class QualifierItem(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A qualifier describing requirements or incompatibilities.
    """

    _id_name : str = None
    subject: Enum = pla.Field(dtype_kwargs={"categories":('source','target','both',)})
    """
    Subject to which the qualifier applies.
    """
    
    predicate: Enum = pla.Field(dtype_kwargs={"categories":('has-requirement','has-incompatibility',)})
    """
    Predicate describing qualifier semantics.
    """
    
    category: Enum = pla.Field(dtype_kwargs={"categories":('restricted','addressable','blocked',)})
    """
    Confidence category label or qualifier category value.
    """
    
    description: str = pla.Field()
    """
    A human-readable description.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    
class Map(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A relationship-based mapping entry between source and target sets.
    """

    _id_name : str = None
    uuid: str = pla.Field()
    """
    A machine-oriented, globally unique identifier with a cross-instance scope.
    """
    
    ns: Optional[str] = pla.Field(nullable=True, )
    """
    An optional namespace qualifying a name. Allows different organizations to associate distinct semantics with the same name.
    """
    
    matching_rationale: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('syntactic','semantic','functional',)})
    """
    The rationale method used to relate mapped items.
    """
    
    relationship: str = pla.Field()
    """
    Relationship type for a mapping entry. OSCAL namespace values are defined by RelationshipEnum.
    """
    
    sources: List = pla.Field()
    """
    Source references or source-participation entries in the containing OSCAL context. The concrete entry class is selected by class-level slot_usage.
    """
    
    targets: List = pla.Field()
    """
    Target subjects participating in a mapping entry.
    """
    
    qualifiers: Optional[List] = pla.Field(nullable=True, )
    """
    Qualifier statements for a mapping entry.
    """
    
    confidence_score: Optional[Struct] = pla.Field(nullable=True, )
    """
    Confidence descriptor for a mapping.
    """
    
    coverage: Optional[Struct] = pla.Field(nullable=True, )
    """
    Coverage metadata for a mapping.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    
    @pla.check("sources")
    def check_nested_struct_sources(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, MappingItem, pa_pl.MappingItemDict)
        
    @pla.check("targets")
    def check_nested_struct_targets(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, MappingItem, pa_pl.MappingItemDict)
        
    @pla.check("qualifiers")
    def check_nested_struct_qualifiers(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, QualifierItem, pa_pl.QualifierItemDict)
        
    @pla.check("confidence_score")
    def check_nested_struct_confidence_score(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, ConfidenceScore, pa_pl.ConfidenceScore)
        
    @pla.check("coverage")
    def check_nested_struct_coverage(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, Coverage, pa_pl.Coverage)
        
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Property, pa_pl.PropertyDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Link, pa_pl.LinkDict)
        
class GapSummary(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A summary of controls that were not mapped.
    """

    _id_name : str = None
    uuid: str = pla.Field()
    """
    A machine-oriented, globally unique identifier with a cross-instance scope.
    """
    
    unmapped_controls: List = pla.Field()
    """
    Controls that remain unmapped.
    """
    
    
    @pla.check("unmapped_controls")
    def check_nested_struct_unmapped_controls(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, SelectControlById, pa_pl.SelectControlByIdDict)
        
class Mapping(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A mapping between two mapped resources.
    """

    _id_name : str = None
    uuid: str = pla.Field()
    """
    A machine-oriented, globally unique identifier with a cross-instance scope.
    """
    
    method: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('human','automation','hybrid',)})
    """
    Method indicator used by the containing OSCAL context. Allowed values are constrained by class-level slot_usage.
    """
    
    matching_rationale: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('syntactic','semantic','functional',)})
    """
    The rationale method used to relate mapped items.
    """
    
    status: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('complete','not-complete','draft','deprecated','superseded',)})
    """
    Status indicator used by the containing OSCAL context. Allowed values are constrained by class-level slot_usage.
    """
    
    source_resource: Struct = pla.Field()
    """
    Reference to the mapping source resource.
    """
    
    target_resource: Struct = pla.Field()
    """
    Reference to the mapping target resource.
    """
    
    maps: List = pla.Field()
    """
    Mapping entries relating source items to target items.
    """
    
    mapping_description: Optional[str] = pla.Field(nullable=True, )
    """
    Description of the context and intended use of the mapping.
    """
    
    source_gap_summary: Optional[Struct] = pla.Field(nullable=True, )
    """
    Summary of unmapped source controls.
    """
    
    target_gap_summary: Optional[Struct] = pla.Field(nullable=True, )
    """
    Summary of unmapped target controls.
    """
    
    confidence_score: Optional[Struct] = pla.Field(nullable=True, )
    """
    Confidence descriptor for a mapping.
    """
    
    coverage: Optional[Struct] = pla.Field(nullable=True, )
    """
    Coverage metadata for a mapping.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    
    @pla.check("source_resource")
    def check_nested_struct_source_resource(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, MappingResourceReference, pa_pl.MappingResourceReference)
        
    @pla.check("target_resource")
    def check_nested_struct_target_resource(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, MappingResourceReference, pa_pl.MappingResourceReference)
        
    @pla.check("maps")
    def check_nested_struct_maps(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Map, pa_pl.MapDict)
        
    @pla.check("source_gap_summary")
    def check_nested_struct_source_gap_summary(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, GapSummary, pa_pl.GapSummary)
        
    @pla.check("target_gap_summary")
    def check_nested_struct_target_gap_summary(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, GapSummary, pa_pl.GapSummary)
        
    @pla.check("confidence_score")
    def check_nested_struct_confidence_score(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, ConfidenceScore, pa_pl.ConfidenceScore)
        
    @pla.check("coverage")
    def check_nested_struct_coverage(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, Coverage, pa_pl.Coverage)
        
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Property, pa_pl.PropertyDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Link, pa_pl.LinkDict)
        
class MappingCollection(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A collection of control mappings between source and target resources.
    """

    _id_name : str = None
    uuid: str = pla.Field()
    """
    A machine-oriented, globally unique identifier with a cross-instance scope.
    """
    
    metadata: Struct = pla.Field()
    """
    Provides information about the containing document, and defines concepts shared across the document.
    """
    
    provenance: Struct = pla.Field()
    """
    Global provenance and mapping method metadata.
    """
    
    mappings: List = pla.Field()
    """
    A collection of control mappings.
    """
    
    back_matter: Optional[Struct] = pla.Field(nullable=True, )
    """
    A collection of resources that may be referenced from within the OSCAL document instance.
    """
    
    
    @pla.check("metadata")
    def check_nested_struct_metadata(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, Metadata, pa_pl.Metadata)
        
    @pla.check("provenance")
    def check_nested_struct_provenance(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, MappingProvenance, pa_pl.MappingProvenance)
        
    @pla.check("mappings")
    def check_nested_struct_mappings(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Mapping, pa_pl.MappingDict)
        
    @pla.check("back_matter")
    def check_nested_struct_back_matter(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, BackMatter, pa_pl.BackMatter)
        
class MappingCollectionDocument(OscalDocument):
    """
    Root wrapper for an OSCAL Mapping Collection document.
    """

    _id_name : str = None
    mapping_collection: Struct = pla.Field()
    """
    The root mapping collection object.
    """
    
    
    @pla.check("mapping_collection")
    def check_nested_struct_mapping_collection(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, MappingCollection, pa_pl.MappingCollection)
        
class PoamLocalDefinitions(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Allows components and inventory items to be defined within the POA&M for cases where no OSCAL SSP is available with the POA&M.
    """

    _id_name : str = None
    components: Optional[List] = pla.Field(nullable=True, )
    """
    A collection of system components.
    """
    
    inventory_items: Optional[List] = pla.Field(nullable=True, )
    """
    A collection of inventory items.
    """
    
    assessment_assets: Optional[Struct] = pla.Field(nullable=True, )
    """
    Identifies the assets used to perform this assessment.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    
    @pla.check("components")
    def check_nested_struct_components(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, SystemComponent, pa_pl.SystemComponentDict)
        
    @pla.check("inventory_items")
    def check_nested_struct_inventory_items(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, InventoryItem, pa_pl.InventoryItemDict)
        
    @pla.check("assessment_assets")
    def check_nested_struct_assessment_assets(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, AssessmentAssets, pa_pl.AssessmentAssets)
        
class RelatedFinding(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Relates a POA&M item to a referenced finding.
    """

    _id_name : str = None
    finding_uuid: str = pla.Field()
    """
    A UUID reference to a finding.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    
class PoamItem(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Describes an individual POA&M item.
    """

    _id_name : str = None
    uuid: Optional[str] = pla.Field(nullable=True, )
    """
    A machine-oriented, globally unique identifier with a cross-instance scope.
    """
    
    title: str = pla.Field()
    """
    A human-readable name or title.
    """
    
    description: str = pla.Field()
    """
    A human-readable description.
    """
    
    origins: Optional[List] = pla.Field(nullable=True, )
    """
    Identifies the source of observations, findings, or risks.
    """
    
    related_findings: Optional[List] = pla.Field(nullable=True, )
    """
    Relates a POA&M item to one or more findings.
    """
    
    related_observations: Optional[List] = pla.Field(nullable=True, )
    """
    Relates the containing object to a set of referenced observations.
    """
    
    related_risks: Optional[List] = pla.Field(nullable=True, )
    """
    Relates the finding to a set of referenced risks.
    """
    
    remarks: Optional[str] = pla.Field(nullable=True, )
    """
    Additional commentary about the containing object.
    """
    
    props: Optional[List] = pla.Field(nullable=True, )
    """
    A list of properties.
    """
    
    links: Optional[List] = pla.Field(nullable=True, )
    """
    A list of links.
    """
    
    
    @pla.check("origins")
    def check_nested_struct_origins(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Origin, pa_pl.OriginDict)
        
    @pla.check("related_findings")
    def check_nested_struct_related_findings(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, RelatedFinding, pa_pl.RelatedFindingDict)
        
    @pla.check("related_observations")
    def check_nested_struct_related_observations(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, RelatedObservation, pa_pl.RelatedObservationDict)
        
    @pla.check("related_risks")
    def check_nested_struct_related_risks(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, AssociatedRisk, pa_pl.AssociatedRiskDict)
        
    @pla.check("props")
    def check_nested_struct_props(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Property, pa_pl.PropertyDict)
        
    @pla.check("links")
    def check_nested_struct_links(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Link, pa_pl.LinkDict)
        
class PlanOfActionAndMilestones(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A plan of action and milestones that identifies initial and residual risks, deviations, and disposition.
    """

    _id_name : str = None
    uuid: str = pla.Field()
    """
    A machine-oriented, globally unique identifier with a cross-instance scope.
    """
    
    metadata: Struct = pla.Field()
    """
    Provides information about the containing document, and defines concepts shared across the document.
    """
    
    import_ssp: Optional[Struct] = pla.Field(nullable=True, )
    """
    Used to import information about the system from an SSP.
    """
    
    system_id: Optional[Struct] = pla.Field(nullable=True, )
    """
    A human-oriented, globally unique identifier for a system.
    """
    
    local_definitions: Optional[Struct] = pla.Field(nullable=True, )
    """
    Used to define data objects that do not appear in the referenced SSP.
    """
    
    observations: Optional[List] = pla.Field(nullable=True, )
    """
    A collection of observations captured in the containing context.
    """
    
    risks: Optional[List] = pla.Field(nullable=True, )
    """
    A collection of risks captured in the containing context.
    """
    
    findings: Optional[List] = pla.Field(nullable=True, )
    """
    A collection of findings captured in the containing context.
    """
    
    poam_items: List = pla.Field()
    """
    A collection of POA&M items.
    """
    
    back_matter: Optional[Struct] = pla.Field(nullable=True, )
    """
    A collection of resources that may be referenced from within the OSCAL document instance.
    """
    
    
    @pla.check("metadata")
    def check_nested_struct_metadata(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, Metadata, pa_pl.Metadata)
        
    @pla.check("import_ssp")
    def check_nested_struct_import_ssp(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, ImportSSP, pa_pl.ImportSSP)
        
    @pla.check("system_id")
    def check_nested_struct_system_id(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, SystemId, pa_pl.SystemId)
        
    @pla.check("local_definitions")
    def check_nested_struct_local_definitions(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, PoamLocalDefinitions, pa_pl.PoamLocalDefinitions)
        
    @pla.check("observations")
    def check_nested_struct_observations(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Observation, pa_pl.ObservationDict)
        
    @pla.check("risks")
    def check_nested_struct_risks(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Risk, pa_pl.RiskDict)
        
    @pla.check("findings")
    def check_nested_struct_findings(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Finding, pa_pl.FindingDict)
        
    @pla.check("poam_items")
    def check_nested_struct_poam_items(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, PoamItem, pa_pl.PoamItemDict)
        
    @pla.check("back_matter")
    def check_nested_struct_back_matter(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, BackMatter, pa_pl.BackMatter)
        
class PoamDocument(OscalDocument):
    """
    Root wrapper for an OSCAL Plan of Action and Milestones document.
    """

    _id_name : str = None
    plan_of_action_and_milestones: Struct = pla.Field()
    """
    The root plan of action and milestones object.
    """
    
    
    @pla.check("plan_of_action_and_milestones")
    def check_nested_struct_plan_of_action_and_milestones(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, PlanOfActionAndMilestones, pa_pl.PlanOfActionAndMilestones)
        
class SspSystemCharacteristicsProp(Property):
    """
    SSP-scoped property used in system characteristics.
    """

    _id_name : str = None
    pass
    
    

