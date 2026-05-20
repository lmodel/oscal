
from sqlalchemy import Column, Index, Table, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import *
from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.associationproxy import association_proxy

Base = declarative_base()
metadata = Base.metadata


class HasPropsAndLinks(Base):
    """
    Mixin providing the props and links slots that are common to many OSCAL objects.
    """
    __tablename__ = 'HasPropsAndLinks'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    
    
    # One-To-Many: OneToAnyMapping(source_class='HasPropsAndLinks', source_slot='props', mapping_type=None, target_class='Property', target_slot='HasPropsAndLinks_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "Property", foreign_keys="[Property.HasPropsAndLinks_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='HasPropsAndLinks', source_slot='links', mapping_type=None, target_class='Link', target_slot='HasPropsAndLinks_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "Link", foreign_keys="[Link.HasPropsAndLinks_id]")
    

    def __repr__(self):
        return f"HasPropsAndLinks(id={self.id},)"



    


class OscalCommon(Base):
    """
    Mixin providing props, links, and remarks slots common to most OSCAL objects. Extends HasPropsAndLinks.
    """
    __tablename__ = 'OscalCommon'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    remarks = Column(Text())
    
    
    # One-To-Many: OneToAnyMapping(source_class='OscalCommon', source_slot='props', mapping_type=None, target_class='Property', target_slot='OscalCommon_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "Property", foreign_keys="[Property.OscalCommon_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='OscalCommon', source_slot='links', mapping_type=None, target_class='Link', target_slot='OscalCommon_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "Link", foreign_keys="[Link.OscalCommon_id]")
    

    def __repr__(self):
        return f"OscalCommon(id={self.id},remarks={self.remarks},)"



    


class HasResponsibleRoles(Base):
    """
    Mixin providing the responsible-roles slot for objects that carry role assignments.
    """
    __tablename__ = 'HasResponsibleRoles'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    
    
    # One-To-Many: OneToAnyMapping(source_class='HasResponsibleRoles', source_slot='responsible_roles', mapping_type=None, target_class='ResponsibleRole', target_slot='HasResponsibleRoles_id', join_class=None, uses_join_table=None, multivalued=False)
    responsible_roles = relationship( "ResponsibleRole", foreign_keys="[ResponsibleRole.HasResponsibleRoles_id]")
    

    def __repr__(self):
        return f"HasResponsibleRoles(id={self.id},)"



    


class HasResponsibleParties(Base):
    """
    Mixin providing the responsible-parties slot for objects that carry party assignments.
    """
    __tablename__ = 'HasResponsibleParties'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    
    
    # One-To-Many: OneToAnyMapping(source_class='HasResponsibleParties', source_slot='responsible_parties', mapping_type=None, target_class='ResponsibleParty', target_slot='HasResponsibleParties_id', join_class=None, uses_join_table=None, multivalued=False)
    responsible_parties = relationship( "ResponsibleParty", foreign_keys="[ResponsibleParty.HasResponsibleParties_id]")
    

    def __repr__(self):
        return f"HasResponsibleParties(id={self.id},)"



    


class OscalDocument(Base):
    """
    A root wrapper for an OSCAL document, which may be of any OSCAL document type (e.g. Catalog, Profile, Assessment Plan, SSP).
    """
    __tablename__ = 'OscalDocument'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    

    def __repr__(self):
        return f"OscalDocument(id={self.id},)"



    


class Catalog(Base):
    """
    A structured, organized collection of control information.
    """
    __tablename__ = 'Catalog'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    uuid = Column(Text(), nullable=False )
    metadata_id = Column(Integer(), ForeignKey('Metadata.id'), nullable=False )
    metadata = relationship("Metadata", uselist=False, foreign_keys=[metadata_id])
    back_matter_id = Column(Integer(), ForeignKey('BackMatter.id'))
    back_matter = relationship("BackMatter", uselist=False, foreign_keys=[back_matter_id])
    
    
    # One-To-Many: OneToAnyMapping(source_class='Catalog', source_slot='params', mapping_type=None, target_class='Parameter', target_slot='Catalog_id', join_class=None, uses_join_table=None, multivalued=False)
    params = relationship( "Parameter", foreign_keys="[Parameter.Catalog_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Catalog', source_slot='controls', mapping_type=None, target_class='Control', target_slot='Catalog_id', join_class=None, uses_join_table=None, multivalued=False)
    controls = relationship( "Control", foreign_keys="[Control.Catalog_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Catalog', source_slot='groups', mapping_type=None, target_class='Group', target_slot='Catalog_id', join_class=None, uses_join_table=None, multivalued=False)
    groups = relationship( "Group", foreign_keys="[Group.Catalog_id]")
    

    def __repr__(self):
        return f"Catalog(id={self.id},uuid={self.uuid},metadata_id={self.metadata_id},back_matter_id={self.back_matter_id},)"



    


class Group(Base):
    """
    A group of controls, or of groups of controls.
    """
    __tablename__ = 'Group'

    uid = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    id = Column(Text())
    _class = Column(Text())
    title = Column(Text(), nullable=False )
    Catalog_id = Column(Integer(), ForeignKey('Catalog.id'))
    Group_uid = Column(Integer(), ForeignKey('Group.uid'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='Group', source_slot='params', mapping_type=None, target_class='Parameter', target_slot='Group_uid', join_class=None, uses_join_table=None, multivalued=False)
    params = relationship( "Parameter", foreign_keys="[Parameter.Group_uid]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Group', source_slot='parts', mapping_type=None, target_class='Part', target_slot='Group_uid', join_class=None, uses_join_table=None, multivalued=False)
    parts = relationship( "Part", foreign_keys="[Part.Group_uid]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Group', source_slot='groups', mapping_type=None, target_class='Group', target_slot='Group_uid', join_class=None, uses_join_table=None, multivalued=False)
    groups = relationship( "Group", foreign_keys="[Group.Group_uid]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Group', source_slot='controls', mapping_type=None, target_class='Control', target_slot='Group_uid', join_class=None, uses_join_table=None, multivalued=False)
    controls = relationship( "Control", foreign_keys="[Control.Group_uid]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Group', source_slot='props', mapping_type=None, target_class='Property', target_slot='Group_uid', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "Property", foreign_keys="[Property.Group_uid]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Group', source_slot='links', mapping_type=None, target_class='Link', target_slot='Group_uid', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "Link", foreign_keys="[Link.Group_uid]")
    

    def __repr__(self):
        return f"Group(uid={self.uid},id={self.id},_class={self._class},title={self.title},Catalog_id={self.Catalog_id},Group_uid={self.Group_uid},)"



    


class Control(Base):
    """
    A structured object representing a requirement or guideline, which when implemented will reduce an aspect of risk related to an information system and its information.
    """
    __tablename__ = 'Control'

    uid = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    id = Column(Text(), nullable=False )
    _class = Column(Text())
    title = Column(Text(), nullable=False )
    Catalog_id = Column(Integer(), ForeignKey('Catalog.id'))
    Group_uid = Column(Integer(), ForeignKey('Group.uid'))
    Control_uid = Column(Integer(), ForeignKey('Control.uid'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='Control', source_slot='params', mapping_type=None, target_class='Parameter', target_slot='Control_uid', join_class=None, uses_join_table=None, multivalued=False)
    params = relationship( "Parameter", foreign_keys="[Parameter.Control_uid]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Control', source_slot='parts', mapping_type=None, target_class='Part', target_slot='Control_uid', join_class=None, uses_join_table=None, multivalued=False)
    parts = relationship( "Part", foreign_keys="[Part.Control_uid]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Control', source_slot='controls', mapping_type=None, target_class='Control', target_slot='Control_uid', join_class=None, uses_join_table=None, multivalued=False)
    controls = relationship( "Control", foreign_keys="[Control.Control_uid]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Control', source_slot='props', mapping_type=None, target_class='Property', target_slot='Control_uid', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "Property", foreign_keys="[Property.Control_uid]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Control', source_slot='links', mapping_type=None, target_class='Link', target_slot='Control_uid', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "Link", foreign_keys="[Link.Control_uid]")
    

    def __repr__(self):
        return f"Control(uid={self.uid},id={self.id},_class={self._class},title={self.title},Catalog_id={self.Catalog_id},Group_uid={self.Group_uid},Control_uid={self.Control_uid},)"



    


class Metadata(Base):
    """
    Provides information about the containing document, and defines concepts shared across the document.
    """
    __tablename__ = 'Metadata'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    title = Column(Text(), nullable=False )
    published = Column(Text())
    last_modified = Column(Text(), nullable=False )
    version = Column(Text(), nullable=False )
    oscal_version = Column(Text(), nullable=False )
    remarks = Column(Text())
    
    
    # One-To-Many: OneToAnyMapping(source_class='Metadata', source_slot='document_ids', mapping_type=None, target_class='DocumentId', target_slot='Metadata_id', join_class=None, uses_join_table=None, multivalued=False)
    document_ids = relationship( "DocumentId", foreign_keys="[DocumentId.Metadata_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Metadata', source_slot='revisions', mapping_type=None, target_class='Revision', target_slot='Metadata_id', join_class=None, uses_join_table=None, multivalued=False)
    revisions = relationship( "Revision", foreign_keys="[Revision.Metadata_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Metadata', source_slot='roles', mapping_type=None, target_class='Role', target_slot='Metadata_id', join_class=None, uses_join_table=None, multivalued=False)
    roles = relationship( "Role", foreign_keys="[Role.Metadata_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Metadata', source_slot='locations', mapping_type=None, target_class='Location', target_slot='Metadata_id', join_class=None, uses_join_table=None, multivalued=False)
    locations = relationship( "Location", foreign_keys="[Location.Metadata_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Metadata', source_slot='parties', mapping_type=None, target_class='Party', target_slot='Metadata_id', join_class=None, uses_join_table=None, multivalued=False)
    parties = relationship( "Party", foreign_keys="[Party.Metadata_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Metadata', source_slot='actions', mapping_type=None, target_class='Action', target_slot='Metadata_id', join_class=None, uses_join_table=None, multivalued=False)
    actions = relationship( "Action", foreign_keys="[Action.Metadata_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Metadata', source_slot='responsible_parties', mapping_type=None, target_class='ResponsibleParty', target_slot='Metadata_id', join_class=None, uses_join_table=None, multivalued=False)
    responsible_parties = relationship( "ResponsibleParty", foreign_keys="[ResponsibleParty.Metadata_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Metadata', source_slot='props', mapping_type=None, target_class='MetadataProperty', target_slot='Metadata_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "MetadataProperty", foreign_keys="[MetadataProperty.Metadata_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Metadata', source_slot='links', mapping_type=None, target_class='Link', target_slot='Metadata_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "Link", foreign_keys="[Link.Metadata_id]")
    

    def __repr__(self):
        return f"Metadata(id={self.id},title={self.title},published={self.published},last_modified={self.last_modified},version={self.version},oscal_version={self.oscal_version},remarks={self.remarks},)"



    


class Revision(Base):
    """
    An entry in a sequential list of revisions to the containing document.
    """
    __tablename__ = 'Revision'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    title = Column(Text())
    published = Column(Text())
    last_modified = Column(Text())
    version = Column(Text(), nullable=False )
    oscal_version = Column(Text())
    remarks = Column(Text())
    Metadata_id = Column(Integer(), ForeignKey('Metadata.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='Revision', source_slot='props', mapping_type=None, target_class='RevisionProperty', target_slot='Revision_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "RevisionProperty", foreign_keys="[RevisionProperty.Revision_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Revision', source_slot='links', mapping_type=None, target_class='Link', target_slot='Revision_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "Link", foreign_keys="[Link.Revision_id]")
    

    def __repr__(self):
        return f"Revision(id={self.id},title={self.title},published={self.published},last_modified={self.last_modified},version={self.version},oscal_version={self.oscal_version},remarks={self.remarks},Metadata_id={self.Metadata_id},)"



    


class DocumentId(Base):
    """
    A document identifier qualified by an identifier scheme.
    """
    __tablename__ = 'DocumentId'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    scheme = Column(Text())
    identifier = Column(Text(), nullable=False )
    Metadata_id = Column(Integer(), ForeignKey('Metadata.id'))
    Resource_id = Column(Integer(), ForeignKey('Resource.id'))
    

    def __repr__(self):
        return f"DocumentId(id={self.id},scheme={self.scheme},identifier={self.identifier},Metadata_id={self.Metadata_id},Resource_id={self.Resource_id},)"



    


class Role(Base):
    """
    Defines a function, which might be assigned to a party in a specific situation.
    """
    __tablename__ = 'Role'

    uid = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    id = Column(Text(), nullable=False )
    title = Column(Text(), nullable=False )
    short_name = Column(Text())
    description = Column(Text())
    remarks = Column(Text())
    Metadata_id = Column(Integer(), ForeignKey('Metadata.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='Role', source_slot='props', mapping_type=None, target_class='Property', target_slot='Role_uid', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "Property", foreign_keys="[Property.Role_uid]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Role', source_slot='links', mapping_type=None, target_class='Link', target_slot='Role_uid', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "Link", foreign_keys="[Link.Role_uid]")
    

    def __repr__(self):
        return f"Role(uid={self.uid},id={self.id},title={self.title},short_name={self.short_name},description={self.description},remarks={self.remarks},Metadata_id={self.Metadata_id},)"



    


class Location(Base):
    """
    A physical point of presence, which may be associated with people, organizations, or other concepts within the current or linked OSCAL document.
    """
    __tablename__ = 'Location'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    uuid = Column(Text(), nullable=False )
    title = Column(Text())
    remarks = Column(Text())
    Metadata_id = Column(Integer(), ForeignKey('Metadata.id'))
    address_id = Column(Integer(), ForeignKey('Address.id'))
    address = relationship("Address", uselist=False, foreign_keys=[address_id])
    
    
    email_addresses_rel = relationship( "LocationEmailAddresses" )
    email_addresses = association_proxy("email_addresses_rel", "email_addresses",
                                  creator=lambda x_: LocationEmailAddresses(email_addresses=x_))
    
    
    # One-To-Many: OneToAnyMapping(source_class='Location', source_slot='telephone_numbers', mapping_type=None, target_class='TelephoneNumber', target_slot='Location_id', join_class=None, uses_join_table=None, multivalued=False)
    telephone_numbers = relationship( "TelephoneNumber", foreign_keys="[TelephoneNumber.Location_id]")
    
    
    urls_rel = relationship( "LocationUrls" )
    urls = association_proxy("urls_rel", "urls",
                                  creator=lambda x_: LocationUrls(urls=x_))
    
    
    # One-To-Many: OneToAnyMapping(source_class='Location', source_slot='props', mapping_type=None, target_class='LocationProperty', target_slot='Location_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "LocationProperty", foreign_keys="[LocationProperty.Location_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Location', source_slot='links', mapping_type=None, target_class='Link', target_slot='Location_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "Link", foreign_keys="[Link.Location_id]")
    

    def __repr__(self):
        return f"Location(id={self.id},uuid={self.uuid},title={self.title},remarks={self.remarks},Metadata_id={self.Metadata_id},address_id={self.address_id},)"



    


class Party(Base):
    """
    An organization or person, which may be associated with roles or other concepts within the current or linked OSCAL document.
    """
    __tablename__ = 'Party'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    uuid = Column(Text(), nullable=False )
    type = Column(Enum('person', 'organization', name='PartyTypeEnum'), nullable=False )
    name = Column(Text())
    short_name = Column(Text())
    remarks = Column(Text())
    Metadata_id = Column(Integer(), ForeignKey('Metadata.id'))
    
    
    email_addresses_rel = relationship( "PartyEmailAddresses" )
    email_addresses = association_proxy("email_addresses_rel", "email_addresses",
                                  creator=lambda x_: PartyEmailAddresses(email_addresses=x_))
    
    
    # One-To-Many: OneToAnyMapping(source_class='Party', source_slot='telephone_numbers', mapping_type=None, target_class='TelephoneNumber', target_slot='Party_id', join_class=None, uses_join_table=None, multivalued=False)
    telephone_numbers = relationship( "TelephoneNumber", foreign_keys="[TelephoneNumber.Party_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Party', source_slot='external_ids', mapping_type=None, target_class='MetadataPartyExternalId', target_slot='Party_id', join_class=None, uses_join_table=None, multivalued=False)
    external_ids = relationship( "MetadataPartyExternalId", foreign_keys="[MetadataPartyExternalId.Party_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Party', source_slot='addresses', mapping_type=None, target_class='Address', target_slot='Party_id', join_class=None, uses_join_table=None, multivalued=False)
    addresses = relationship( "Address", foreign_keys="[Address.Party_id]")
    
    
    location_uuids_rel = relationship( "PartyLocationUuids" )
    location_uuids = association_proxy("location_uuids_rel", "location_uuids",
                                  creator=lambda x_: PartyLocationUuids(location_uuids=x_))
    
    
    member_of_organizations_rel = relationship( "PartyMemberOfOrganizations" )
    member_of_organizations = association_proxy("member_of_organizations_rel", "member_of_organizations",
                                  creator=lambda x_: PartyMemberOfOrganizations(member_of_organizations=x_))
    
    
    # One-To-Many: OneToAnyMapping(source_class='Party', source_slot='props', mapping_type=None, target_class='PartyProperty', target_slot='Party_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "PartyProperty", foreign_keys="[PartyProperty.Party_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Party', source_slot='links', mapping_type=None, target_class='Link', target_slot='Party_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "Link", foreign_keys="[Link.Party_id]")
    

    def __repr__(self):
        return f"Party(id={self.id},uuid={self.uuid},type={self.type},name={self.name},short_name={self.short_name},remarks={self.remarks},Metadata_id={self.Metadata_id},)"



    


class PartyExternalId(Base):
    """
    An identifier for a person or organization using a designated scheme, e.g. an Open Researcher and Contributor ID (ORCID).
    """
    __tablename__ = 'PartyExternalId'

    uid = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    scheme = Column(Text(), nullable=False )
    id = Column(Text(), nullable=False )
    

    def __repr__(self):
        return f"PartyExternalId(uid={self.uid},scheme={self.scheme},id={self.id},)"



    


class ResponsibleParty(Base):
    """
    A reference to a set of persons and/or organizations that have responsibility for performing the referenced role in the context of the containing object.
    """
    __tablename__ = 'ResponsibleParty'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    role_id = Column(Text(), nullable=False )
    remarks = Column(Text())
    HasResponsibleParties_id = Column(Integer(), ForeignKey('HasResponsibleParties.id'))
    Metadata_id = Column(Integer(), ForeignKey('Metadata.id'))
    Action_id = Column(Integer(), ForeignKey('Action.id'))
    UsesComponent_id = Column(Integer(), ForeignKey('UsesComponent.id'))
    RelatedTask_id = Column(Integer(), ForeignKey('RelatedTask.id'))
    Attestation_id = Column(Integer(), ForeignKey('Attestation.id'))
    MappingProvenance_id = Column(Integer(), ForeignKey('MappingProvenance.id'))
    
    
    party_uuids_rel = relationship( "ResponsiblePartyPartyUuids" )
    party_uuids = association_proxy("party_uuids_rel", "party_uuids",
                                  creator=lambda x_: ResponsiblePartyPartyUuids(party_uuids=x_))
    
    
    # One-To-Many: OneToAnyMapping(source_class='ResponsibleParty', source_slot='props', mapping_type=None, target_class='Property', target_slot='ResponsibleParty_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "Property", foreign_keys="[Property.ResponsibleParty_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='ResponsibleParty', source_slot='links', mapping_type=None, target_class='Link', target_slot='ResponsibleParty_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "Link", foreign_keys="[Link.ResponsibleParty_id]")
    

    def __repr__(self):
        return f"ResponsibleParty(id={self.id},role_id={self.role_id},remarks={self.remarks},HasResponsibleParties_id={self.HasResponsibleParties_id},Metadata_id={self.Metadata_id},Action_id={self.Action_id},UsesComponent_id={self.UsesComponent_id},RelatedTask_id={self.RelatedTask_id},Attestation_id={self.Attestation_id},MappingProvenance_id={self.MappingProvenance_id},)"



    


class ResponsibleRole(Base):
    """
    A reference to a role with responsibility for performing a function relative to the containing object, optionally associated with a set of persons and/or organizations that perform that role.
    """
    __tablename__ = 'ResponsibleRole'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    role_id = Column(Text(), nullable=False )
    remarks = Column(Text())
    HasResponsibleRoles_id = Column(Integer(), ForeignKey('HasResponsibleRoles.id'))
    Activity_id = Column(Integer(), ForeignKey('Activity.id'))
    Step_id = Column(Integer(), ForeignKey('Step.id'))
    Task_id = Column(Integer(), ForeignKey('Task.id'))
    AssociatedActivity_id = Column(Integer(), ForeignKey('AssociatedActivity.id'))
    DefinedComponent_id = Column(Integer(), ForeignKey('DefinedComponent.id'))
    ImplementedRequirement_id = Column(Integer(), ForeignKey('ImplementedRequirement.id'))
    ImplementedControlStatement_id = Column(Integer(), ForeignKey('ImplementedControlStatement.id'))
    
    
    party_uuids_rel = relationship( "ResponsibleRolePartyUuids" )
    party_uuids = association_proxy("party_uuids_rel", "party_uuids",
                                  creator=lambda x_: ResponsibleRolePartyUuids(party_uuids=x_))
    
    
    # One-To-Many: OneToAnyMapping(source_class='ResponsibleRole', source_slot='props', mapping_type=None, target_class='Property', target_slot='ResponsibleRole_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "Property", foreign_keys="[Property.ResponsibleRole_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='ResponsibleRole', source_slot='links', mapping_type=None, target_class='Link', target_slot='ResponsibleRole_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "Link", foreign_keys="[Link.ResponsibleRole_id]")
    

    def __repr__(self):
        return f"ResponsibleRole(id={self.id},role_id={self.role_id},remarks={self.remarks},HasResponsibleRoles_id={self.HasResponsibleRoles_id},Activity_id={self.Activity_id},Step_id={self.Step_id},Task_id={self.Task_id},AssociatedActivity_id={self.AssociatedActivity_id},DefinedComponent_id={self.DefinedComponent_id},ImplementedRequirement_id={self.ImplementedRequirement_id},ImplementedControlStatement_id={self.ImplementedControlStatement_id},)"



    


class Action(Base):
    """
    An action applied by a role within a given party to the content.
    """
    __tablename__ = 'Action'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    uuid = Column(Text(), nullable=False )
    type = Column(Enum('approval', 'request-changes', name='ActionTypeEnum'), nullable=False )
    date = Column(Text())
    system = Column(Text(), nullable=False )
    remarks = Column(Text())
    Metadata_id = Column(Integer(), ForeignKey('Metadata.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='Action', source_slot='responsible_parties', mapping_type=None, target_class='ResponsibleParty', target_slot='Action_id', join_class=None, uses_join_table=None, multivalued=False)
    responsible_parties = relationship( "ResponsibleParty", foreign_keys="[ResponsibleParty.Action_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Action', source_slot='props', mapping_type=None, target_class='Property', target_slot='Action_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "Property", foreign_keys="[Property.Action_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Action', source_slot='links', mapping_type=None, target_class='Link', target_slot='Action_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "Link", foreign_keys="[Link.Action_id]")
    

    def __repr__(self):
        return f"Action(id={self.id},uuid={self.uuid},type={self.type},date={self.date},system={self.system},remarks={self.remarks},Metadata_id={self.Metadata_id},)"



    


class TelephoneNumber(Base):
    """
    A telephone service number as defined by ITU-T E.164.
    """
    __tablename__ = 'TelephoneNumber'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    type = Column(Text())
    number = Column(Text(), nullable=False )
    Location_id = Column(Integer(), ForeignKey('Location.id'))
    Party_id = Column(Integer(), ForeignKey('Party.id'))
    

    def __repr__(self):
        return f"TelephoneNumber(id={self.id},type={self.type},number={self.number},Location_id={self.Location_id},Party_id={self.Party_id},)"



    


class Address(Base):
    """
    A postal address for the location.
    """
    __tablename__ = 'Address'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    type = Column(Text())
    city = Column(Text())
    state = Column(Text())
    postal_code = Column(Text())
    country = Column(Text())
    Party_id = Column(Integer(), ForeignKey('Party.id'))
    
    
    addr_lines_rel = relationship( "AddressAddrLines" )
    addr_lines = association_proxy("addr_lines_rel", "addr_lines",
                                  creator=lambda x_: AddressAddrLines(addr_lines=x_))
    

    def __repr__(self):
        return f"Address(id={self.id},type={self.type},city={self.city},state={self.state},postal_code={self.postal_code},country={self.country},Party_id={self.Party_id},)"



    


class Hash(Base):
    """
    A representation of a cryptographic digest generated over a resource using a specified hash algorithm.
    """
    __tablename__ = 'Hash'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    value = Column(Text(), nullable=False )
    algorithm = Column(Text(), nullable=False )
    ResourceLink_id = Column(Integer(), ForeignKey('ResourceLink.id'))
    

    def __repr__(self):
        return f"Hash(id={self.id},value={self.value},algorithm={self.algorithm},ResourceLink_id={self.ResourceLink_id},)"



    


class Property(Base):
    """
    An attribute, characteristic, or quality of the containing object expressed as a namespace qualified name/value pair.
    """
    __tablename__ = 'Property'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    name = Column(Text(), nullable=False )
    uuid = Column(Text())
    ns = Column(Text())
    value = Column(Text(), nullable=False )
    _class = Column(Text())
    remarks = Column(Text())
    group = Column(Text())
    HasPropsAndLinks_id = Column(Integer(), ForeignKey('HasPropsAndLinks.id'))
    OscalCommon_id = Column(Integer(), ForeignKey('OscalCommon.id'))
    Group_uid = Column(Integer(), ForeignKey('Group.uid'))
    Control_uid = Column(Integer(), ForeignKey('Control.uid'))
    Role_uid = Column(Integer(), ForeignKey('Role.uid'))
    ResponsibleParty_id = Column(Integer(), ForeignKey('ResponsibleParty.id'))
    ResponsibleRole_id = Column(Integer(), ForeignKey('ResponsibleRole.id'))
    Action_id = Column(Integer(), ForeignKey('Action.id'))
    Citation_id = Column(Integer(), ForeignKey('Citation.id'))
    ProfileGroup_uid = Column(Integer(), ForeignKey('ProfileGroup.uid'))
    ParameterSetting_id = Column(Integer(), ForeignKey('ParameterSetting.id'))
    ReviewedControls_id = Column(Integer(), ForeignKey('ReviewedControls.id'))
    ControlSelection_id = Column(Integer(), ForeignKey('ControlSelection.id'))
    ControlObjectiveSelection_id = Column(Integer(), ForeignKey('ControlObjectiveSelection.id'))
    AssessmentSubject_id = Column(Integer(), ForeignKey('AssessmentSubject.id'))
    SelectSubjectById_id = Column(Integer(), ForeignKey('SelectSubjectById.id'))
    SubjectReference_id = Column(Integer(), ForeignKey('SubjectReference.id'))
    AssessmentSubjectPlaceholder_id = Column(Integer(), ForeignKey('AssessmentSubjectPlaceholder.id'))
    AssessmentPlatform_id = Column(Integer(), ForeignKey('AssessmentPlatform.id'))
    UsesComponent_id = Column(Integer(), ForeignKey('UsesComponent.id'))
    LocalObjective_id = Column(Integer(), ForeignKey('LocalObjective.id'))
    AssessmentMethod_id = Column(Integer(), ForeignKey('AssessmentMethod.id'))
    Activity_id = Column(Integer(), ForeignKey('Activity.id'))
    Step_id = Column(Integer(), ForeignKey('Step.id'))
    Task_id = Column(Integer(), ForeignKey('Task.id'))
    AssociatedActivity_id = Column(Integer(), ForeignKey('AssociatedActivity.id'))
    AssessmentPart_id = Column(Integer(), ForeignKey('AssessmentPart.id'))
    TermsAndConditionsPart_id = Column(Integer(), ForeignKey('TermsAndConditionsPart.id'))
    ControlPart_uid = Column(Integer(), ForeignKey('ControlPart.uid'))
    ImplementationResponsibleRole_id = Column(Integer(), ForeignKey('ImplementationResponsibleRole.id'))
    ImplementationResponsibleParty_id = Column(Integer(), ForeignKey('ImplementationResponsibleParty.id'))
    OriginActor_id = Column(Integer(), ForeignKey('OriginActor.id'))
    RelatedTask_id = Column(Integer(), ForeignKey('RelatedTask.id'))
    Observation_id = Column(Integer(), ForeignKey('Observation.id'))
    RelevantEvidence_id = Column(Integer(), ForeignKey('RelevantEvidence.id'))
    Finding_id = Column(Integer(), ForeignKey('Finding.id'))
    FindingTarget_id = Column(Integer(), ForeignKey('FindingTarget.id'))
    Risk_id = Column(Integer(), ForeignKey('Risk.id'))
    Characterization_id = Column(Integer(), ForeignKey('Characterization.id'))
    Facet_id = Column(Integer(), ForeignKey('Facet.id'))
    MitigatingFactor_id = Column(Integer(), ForeignKey('MitigatingFactor.id'))
    Response_id = Column(Integer(), ForeignKey('Response.id'))
    RequiredAsset_id = Column(Integer(), ForeignKey('RequiredAsset.id'))
    RiskLogEntry_id = Column(Integer(), ForeignKey('RiskLogEntry.id'))
    RiskResponseReference_id = Column(Integer(), ForeignKey('RiskResponseReference.id'))
    InformationType_id = Column(Integer(), ForeignKey('InformationType.id'))
    ImpactLevel_id = Column(Integer(), ForeignKey('ImpactLevel.id'))
    AuthorizationBoundary_id = Column(Integer(), ForeignKey('AuthorizationBoundary.id'))
    Diagram_id = Column(Integer(), ForeignKey('Diagram.id'))
    NetworkArchitecture_id = Column(Integer(), ForeignKey('NetworkArchitecture.id'))
    DataFlow_id = Column(Integer(), ForeignKey('DataFlow.id'))
    SystemImplementation_id = Column(Integer(), ForeignKey('SystemImplementation.id'))
    LeveragedAuthorization_id = Column(Integer(), ForeignKey('LeveragedAuthorization.id'))
    Export_id = Column(Integer(), ForeignKey('Export.id'))
    ProvidedControlImplementation_id = Column(Integer(), ForeignKey('ProvidedControlImplementation.id'))
    ControlResponsibility_id = Column(Integer(), ForeignKey('ControlResponsibility.id'))
    InheritedControlImplementation_id = Column(Integer(), ForeignKey('InheritedControlImplementation.id'))
    SatisfiedControlImplementation_id = Column(Integer(), ForeignKey('SatisfiedControlImplementation.id'))
    SspSystemCharacteristicsResponsibleParty_id = Column(Integer(), ForeignKey('SspSystemCharacteristicsResponsibleParty.id'))
    SspImplementedRequirementResponsibleRole_id = Column(Integer(), ForeignKey('SspImplementedRequirementResponsibleRole.id'))
    SspByComponentResponsibleRole_id = Column(Integer(), ForeignKey('SspByComponentResponsibleRole.id'))
    Result_id = Column(Integer(), ForeignKey('Result.id'))
    AssessmentLogEntry_id = Column(Integer(), ForeignKey('AssessmentLogEntry.id'))
    DefinedComponent_id = Column(Integer(), ForeignKey('DefinedComponent.id'))
    Capability_id = Column(Integer(), ForeignKey('Capability.id'))
    ControlImplementationSet_id = Column(Integer(), ForeignKey('ControlImplementationSet.id'))
    ImplementedRequirement_id = Column(Integer(), ForeignKey('ImplementedRequirement.id'))
    ImplementedControlStatement_id = Column(Integer(), ForeignKey('ImplementedControlStatement.id'))
    MappingProvenance_id = Column(Integer(), ForeignKey('MappingProvenance.id'))
    Mapping_id = Column(Integer(), ForeignKey('Mapping.id'))
    Map_id = Column(Integer(), ForeignKey('Map.id'))
    MappingItem_id = Column(Integer(), ForeignKey('MappingItem.id'))
    MappingResourceReference_id = Column(Integer(), ForeignKey('MappingResourceReference.id'))
    PoamItem_id = Column(Integer(), ForeignKey('PoamItem.id'))
    

    def __repr__(self):
        return f"Property(id={self.id},name={self.name},uuid={self.uuid},ns={self.ns},value={self.value},_class={self._class},remarks={self.remarks},group={self.group},HasPropsAndLinks_id={self.HasPropsAndLinks_id},OscalCommon_id={self.OscalCommon_id},Group_uid={self.Group_uid},Control_uid={self.Control_uid},Role_uid={self.Role_uid},ResponsibleParty_id={self.ResponsibleParty_id},ResponsibleRole_id={self.ResponsibleRole_id},Action_id={self.Action_id},Citation_id={self.Citation_id},ProfileGroup_uid={self.ProfileGroup_uid},ParameterSetting_id={self.ParameterSetting_id},ReviewedControls_id={self.ReviewedControls_id},ControlSelection_id={self.ControlSelection_id},ControlObjectiveSelection_id={self.ControlObjectiveSelection_id},AssessmentSubject_id={self.AssessmentSubject_id},SelectSubjectById_id={self.SelectSubjectById_id},SubjectReference_id={self.SubjectReference_id},AssessmentSubjectPlaceholder_id={self.AssessmentSubjectPlaceholder_id},AssessmentPlatform_id={self.AssessmentPlatform_id},UsesComponent_id={self.UsesComponent_id},LocalObjective_id={self.LocalObjective_id},AssessmentMethod_id={self.AssessmentMethod_id},Activity_id={self.Activity_id},Step_id={self.Step_id},Task_id={self.Task_id},AssociatedActivity_id={self.AssociatedActivity_id},AssessmentPart_id={self.AssessmentPart_id},TermsAndConditionsPart_id={self.TermsAndConditionsPart_id},ControlPart_uid={self.ControlPart_uid},ImplementationResponsibleRole_id={self.ImplementationResponsibleRole_id},ImplementationResponsibleParty_id={self.ImplementationResponsibleParty_id},OriginActor_id={self.OriginActor_id},RelatedTask_id={self.RelatedTask_id},Observation_id={self.Observation_id},RelevantEvidence_id={self.RelevantEvidence_id},Finding_id={self.Finding_id},FindingTarget_id={self.FindingTarget_id},Risk_id={self.Risk_id},Characterization_id={self.Characterization_id},Facet_id={self.Facet_id},MitigatingFactor_id={self.MitigatingFactor_id},Response_id={self.Response_id},RequiredAsset_id={self.RequiredAsset_id},RiskLogEntry_id={self.RiskLogEntry_id},RiskResponseReference_id={self.RiskResponseReference_id},InformationType_id={self.InformationType_id},ImpactLevel_id={self.ImpactLevel_id},AuthorizationBoundary_id={self.AuthorizationBoundary_id},Diagram_id={self.Diagram_id},NetworkArchitecture_id={self.NetworkArchitecture_id},DataFlow_id={self.DataFlow_id},SystemImplementation_id={self.SystemImplementation_id},LeveragedAuthorization_id={self.LeveragedAuthorization_id},Export_id={self.Export_id},ProvidedControlImplementation_id={self.ProvidedControlImplementation_id},ControlResponsibility_id={self.ControlResponsibility_id},InheritedControlImplementation_id={self.InheritedControlImplementation_id},SatisfiedControlImplementation_id={self.SatisfiedControlImplementation_id},SspSystemCharacteristicsResponsibleParty_id={self.SspSystemCharacteristicsResponsibleParty_id},SspImplementedRequirementResponsibleRole_id={self.SspImplementedRequirementResponsibleRole_id},SspByComponentResponsibleRole_id={self.SspByComponentResponsibleRole_id},Result_id={self.Result_id},AssessmentLogEntry_id={self.AssessmentLogEntry_id},DefinedComponent_id={self.DefinedComponent_id},Capability_id={self.Capability_id},ControlImplementationSet_id={self.ControlImplementationSet_id},ImplementedRequirement_id={self.ImplementedRequirement_id},ImplementedControlStatement_id={self.ImplementedControlStatement_id},MappingProvenance_id={self.MappingProvenance_id},Mapping_id={self.Mapping_id},Map_id={self.Map_id},MappingItem_id={self.MappingItem_id},MappingResourceReference_id={self.MappingResourceReference_id},PoamItem_id={self.PoamItem_id},)"



    


class Link(Base):
    """
    A reference to a local or remote resource, that has a specific relation to the containing object.
    """
    __tablename__ = 'Link'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    href = Column(Text(), nullable=False )
    rel = Column(Text())
    resource_fragment = Column(Text())
    media_type = Column(Text())
    text = Column(Text())
    HasPropsAndLinks_id = Column(Integer(), ForeignKey('HasPropsAndLinks.id'))
    OscalCommon_id = Column(Integer(), ForeignKey('OscalCommon.id'))
    Group_uid = Column(Integer(), ForeignKey('Group.uid'))
    Control_uid = Column(Integer(), ForeignKey('Control.uid'))
    Metadata_id = Column(Integer(), ForeignKey('Metadata.id'))
    Revision_id = Column(Integer(), ForeignKey('Revision.id'))
    Role_uid = Column(Integer(), ForeignKey('Role.uid'))
    Location_id = Column(Integer(), ForeignKey('Location.id'))
    Party_id = Column(Integer(), ForeignKey('Party.id'))
    ResponsibleParty_id = Column(Integer(), ForeignKey('ResponsibleParty.id'))
    ResponsibleRole_id = Column(Integer(), ForeignKey('ResponsibleRole.id'))
    Action_id = Column(Integer(), ForeignKey('Action.id'))
    Citation_id = Column(Integer(), ForeignKey('Citation.id'))
    Part_uid = Column(Integer(), ForeignKey('Part.uid'))
    Parameter_uid = Column(Integer(), ForeignKey('Parameter.uid'))
    ProfileGroup_uid = Column(Integer(), ForeignKey('ProfileGroup.uid'))
    ParameterSetting_id = Column(Integer(), ForeignKey('ParameterSetting.id'))
    Addition_id = Column(Integer(), ForeignKey('Addition.id'))
    ReviewedControls_id = Column(Integer(), ForeignKey('ReviewedControls.id'))
    ControlSelection_id = Column(Integer(), ForeignKey('ControlSelection.id'))
    ControlObjectiveSelection_id = Column(Integer(), ForeignKey('ControlObjectiveSelection.id'))
    AssessmentSubject_id = Column(Integer(), ForeignKey('AssessmentSubject.id'))
    SelectSubjectById_id = Column(Integer(), ForeignKey('SelectSubjectById.id'))
    SubjectReference_id = Column(Integer(), ForeignKey('SubjectReference.id'))
    AssessmentSubjectPlaceholder_id = Column(Integer(), ForeignKey('AssessmentSubjectPlaceholder.id'))
    AssessmentPlatform_id = Column(Integer(), ForeignKey('AssessmentPlatform.id'))
    UsesComponent_id = Column(Integer(), ForeignKey('UsesComponent.id'))
    LocalObjective_id = Column(Integer(), ForeignKey('LocalObjective.id'))
    AssessmentMethod_id = Column(Integer(), ForeignKey('AssessmentMethod.id'))
    Activity_id = Column(Integer(), ForeignKey('Activity.id'))
    Step_id = Column(Integer(), ForeignKey('Step.id'))
    Task_id = Column(Integer(), ForeignKey('Task.id'))
    AssociatedActivity_id = Column(Integer(), ForeignKey('AssociatedActivity.id'))
    AssessmentPart_id = Column(Integer(), ForeignKey('AssessmentPart.id'))
    TermsAndConditionsPart_id = Column(Integer(), ForeignKey('TermsAndConditionsPart.id'))
    ControlPart_uid = Column(Integer(), ForeignKey('ControlPart.uid'))
    ImplementationResponsibleRole_id = Column(Integer(), ForeignKey('ImplementationResponsibleRole.id'))
    ImplementationResponsibleParty_id = Column(Integer(), ForeignKey('ImplementationResponsibleParty.id'))
    OriginActor_id = Column(Integer(), ForeignKey('OriginActor.id'))
    RelatedTask_id = Column(Integer(), ForeignKey('RelatedTask.id'))
    Observation_id = Column(Integer(), ForeignKey('Observation.id'))
    RelevantEvidence_id = Column(Integer(), ForeignKey('RelevantEvidence.id'))
    Finding_id = Column(Integer(), ForeignKey('Finding.id'))
    FindingTarget_id = Column(Integer(), ForeignKey('FindingTarget.id'))
    Risk_id = Column(Integer(), ForeignKey('Risk.id'))
    Characterization_id = Column(Integer(), ForeignKey('Characterization.id'))
    Facet_id = Column(Integer(), ForeignKey('Facet.id'))
    MitigatingFactor_id = Column(Integer(), ForeignKey('MitigatingFactor.id'))
    Response_id = Column(Integer(), ForeignKey('Response.id'))
    RequiredAsset_id = Column(Integer(), ForeignKey('RequiredAsset.id'))
    RiskLogEntry_id = Column(Integer(), ForeignKey('RiskLogEntry.id'))
    RiskResponseReference_id = Column(Integer(), ForeignKey('RiskResponseReference.id'))
    InformationType_id = Column(Integer(), ForeignKey('InformationType.id'))
    ImpactLevel_id = Column(Integer(), ForeignKey('ImpactLevel.id'))
    AuthorizationBoundary_id = Column(Integer(), ForeignKey('AuthorizationBoundary.id'))
    NetworkArchitecture_id = Column(Integer(), ForeignKey('NetworkArchitecture.id'))
    DataFlow_id = Column(Integer(), ForeignKey('DataFlow.id'))
    SystemImplementation_id = Column(Integer(), ForeignKey('SystemImplementation.id'))
    SspImplementedRequirement_id = Column(Integer(), ForeignKey('SspImplementedRequirement.id'))
    SspStatement_id = Column(Integer(), ForeignKey('SspStatement.id'))
    Export_id = Column(Integer(), ForeignKey('Export.id'))
    ProvidedControlImplementation_id = Column(Integer(), ForeignKey('ProvidedControlImplementation.id'))
    ControlResponsibility_id = Column(Integer(), ForeignKey('ControlResponsibility.id'))
    InheritedControlImplementation_id = Column(Integer(), ForeignKey('InheritedControlImplementation.id'))
    SatisfiedControlImplementation_id = Column(Integer(), ForeignKey('SatisfiedControlImplementation.id'))
    SspSystemCharacteristicsResponsibleParty_id = Column(Integer(), ForeignKey('SspSystemCharacteristicsResponsibleParty.id'))
    SspImplementedRequirementResponsibleRole_id = Column(Integer(), ForeignKey('SspImplementedRequirementResponsibleRole.id'))
    SspByComponentResponsibleRole_id = Column(Integer(), ForeignKey('SspByComponentResponsibleRole.id'))
    Result_id = Column(Integer(), ForeignKey('Result.id'))
    AssessmentLogEntry_id = Column(Integer(), ForeignKey('AssessmentLogEntry.id'))
    DefinedComponent_id = Column(Integer(), ForeignKey('DefinedComponent.id'))
    Capability_id = Column(Integer(), ForeignKey('Capability.id'))
    ControlImplementationSet_id = Column(Integer(), ForeignKey('ControlImplementationSet.id'))
    ImplementedRequirement_id = Column(Integer(), ForeignKey('ImplementedRequirement.id'))
    ImplementedControlStatement_id = Column(Integer(), ForeignKey('ImplementedControlStatement.id'))
    MappingProvenance_id = Column(Integer(), ForeignKey('MappingProvenance.id'))
    Mapping_id = Column(Integer(), ForeignKey('Mapping.id'))
    Map_id = Column(Integer(), ForeignKey('Map.id'))
    MappingItem_id = Column(Integer(), ForeignKey('MappingItem.id'))
    MappingResourceReference_id = Column(Integer(), ForeignKey('MappingResourceReference.id'))
    PoamItem_id = Column(Integer(), ForeignKey('PoamItem.id'))
    

    def __repr__(self):
        return f"Link(id={self.id},href={self.href},rel={self.rel},resource_fragment={self.resource_fragment},media_type={self.media_type},text={self.text},HasPropsAndLinks_id={self.HasPropsAndLinks_id},OscalCommon_id={self.OscalCommon_id},Group_uid={self.Group_uid},Control_uid={self.Control_uid},Metadata_id={self.Metadata_id},Revision_id={self.Revision_id},Role_uid={self.Role_uid},Location_id={self.Location_id},Party_id={self.Party_id},ResponsibleParty_id={self.ResponsibleParty_id},ResponsibleRole_id={self.ResponsibleRole_id},Action_id={self.Action_id},Citation_id={self.Citation_id},Part_uid={self.Part_uid},Parameter_uid={self.Parameter_uid},ProfileGroup_uid={self.ProfileGroup_uid},ParameterSetting_id={self.ParameterSetting_id},Addition_id={self.Addition_id},ReviewedControls_id={self.ReviewedControls_id},ControlSelection_id={self.ControlSelection_id},ControlObjectiveSelection_id={self.ControlObjectiveSelection_id},AssessmentSubject_id={self.AssessmentSubject_id},SelectSubjectById_id={self.SelectSubjectById_id},SubjectReference_id={self.SubjectReference_id},AssessmentSubjectPlaceholder_id={self.AssessmentSubjectPlaceholder_id},AssessmentPlatform_id={self.AssessmentPlatform_id},UsesComponent_id={self.UsesComponent_id},LocalObjective_id={self.LocalObjective_id},AssessmentMethod_id={self.AssessmentMethod_id},Activity_id={self.Activity_id},Step_id={self.Step_id},Task_id={self.Task_id},AssociatedActivity_id={self.AssociatedActivity_id},AssessmentPart_id={self.AssessmentPart_id},TermsAndConditionsPart_id={self.TermsAndConditionsPart_id},ControlPart_uid={self.ControlPart_uid},ImplementationResponsibleRole_id={self.ImplementationResponsibleRole_id},ImplementationResponsibleParty_id={self.ImplementationResponsibleParty_id},OriginActor_id={self.OriginActor_id},RelatedTask_id={self.RelatedTask_id},Observation_id={self.Observation_id},RelevantEvidence_id={self.RelevantEvidence_id},Finding_id={self.Finding_id},FindingTarget_id={self.FindingTarget_id},Risk_id={self.Risk_id},Characterization_id={self.Characterization_id},Facet_id={self.Facet_id},MitigatingFactor_id={self.MitigatingFactor_id},Response_id={self.Response_id},RequiredAsset_id={self.RequiredAsset_id},RiskLogEntry_id={self.RiskLogEntry_id},RiskResponseReference_id={self.RiskResponseReference_id},InformationType_id={self.InformationType_id},ImpactLevel_id={self.ImpactLevel_id},AuthorizationBoundary_id={self.AuthorizationBoundary_id},NetworkArchitecture_id={self.NetworkArchitecture_id},DataFlow_id={self.DataFlow_id},SystemImplementation_id={self.SystemImplementation_id},SspImplementedRequirement_id={self.SspImplementedRequirement_id},SspStatement_id={self.SspStatement_id},Export_id={self.Export_id},ProvidedControlImplementation_id={self.ProvidedControlImplementation_id},ControlResponsibility_id={self.ControlResponsibility_id},InheritedControlImplementation_id={self.InheritedControlImplementation_id},SatisfiedControlImplementation_id={self.SatisfiedControlImplementation_id},SspSystemCharacteristicsResponsibleParty_id={self.SspSystemCharacteristicsResponsibleParty_id},SspImplementedRequirementResponsibleRole_id={self.SspImplementedRequirementResponsibleRole_id},SspByComponentResponsibleRole_id={self.SspByComponentResponsibleRole_id},Result_id={self.Result_id},AssessmentLogEntry_id={self.AssessmentLogEntry_id},DefinedComponent_id={self.DefinedComponent_id},Capability_id={self.Capability_id},ControlImplementationSet_id={self.ControlImplementationSet_id},ImplementedRequirement_id={self.ImplementedRequirement_id},ImplementedControlStatement_id={self.ImplementedControlStatement_id},MappingProvenance_id={self.MappingProvenance_id},Mapping_id={self.Mapping_id},Map_id={self.Map_id},MappingItem_id={self.MappingItem_id},MappingResourceReference_id={self.MappingResourceReference_id},PoamItem_id={self.PoamItem_id},)"



    


class BackMatter(Base):
    """
    A collection of resources that may be referenced from within the OSCAL document instance.
    """
    __tablename__ = 'BackMatter'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    
    
    # One-To-Many: OneToAnyMapping(source_class='BackMatter', source_slot='resources', mapping_type=None, target_class='Resource', target_slot='BackMatter_id', join_class=None, uses_join_table=None, multivalued=False)
    resources = relationship( "Resource", foreign_keys="[Resource.BackMatter_id]")
    

    def __repr__(self):
        return f"BackMatter(id={self.id},)"



    


class Resource(Base):
    """
    A resource associated with content in the containing document instance. A resource may be directly included in the document using base64 encoding or may point to one or more equivalent internet resources.
    """
    __tablename__ = 'Resource'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    uuid = Column(Text(), nullable=False )
    title = Column(Text())
    description = Column(Text())
    remarks = Column(Text())
    BackMatter_id = Column(Integer(), ForeignKey('BackMatter.id'))
    citation_id = Column(Integer(), ForeignKey('Citation.id'))
    citation = relationship("Citation", uselist=False, foreign_keys=[citation_id])
    base64_id = Column(Integer(), ForeignKey('Base64Resource.id'))
    base64 = relationship("Base64Resource", uselist=False, foreign_keys=[base64_id])
    
    
    # One-To-Many: OneToAnyMapping(source_class='Resource', source_slot='props', mapping_type=None, target_class='ResourceProperty', target_slot='Resource_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "ResourceProperty", foreign_keys="[ResourceProperty.Resource_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Resource', source_slot='document_ids', mapping_type=None, target_class='DocumentId', target_slot='Resource_id', join_class=None, uses_join_table=None, multivalued=False)
    document_ids = relationship( "DocumentId", foreign_keys="[DocumentId.Resource_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Resource', source_slot='rlinks', mapping_type=None, target_class='ResourceLink', target_slot='Resource_id', join_class=None, uses_join_table=None, multivalued=False)
    rlinks = relationship( "ResourceLink", foreign_keys="[ResourceLink.Resource_id]")
    

    def __repr__(self):
        return f"Resource(id={self.id},uuid={self.uuid},title={self.title},description={self.description},remarks={self.remarks},BackMatter_id={self.BackMatter_id},citation_id={self.citation_id},base64_id={self.base64_id},)"



    


class Citation(Base):
    """
    An optional citation consisting of end note text using structured markup.
    """
    __tablename__ = 'Citation'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    text = Column(Text(), nullable=False )
    
    
    # One-To-Many: OneToAnyMapping(source_class='Citation', source_slot='props', mapping_type=None, target_class='Property', target_slot='Citation_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "Property", foreign_keys="[Property.Citation_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Citation', source_slot='links', mapping_type=None, target_class='Link', target_slot='Citation_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "Link", foreign_keys="[Link.Citation_id]")
    

    def __repr__(self):
        return f"Citation(id={self.id},text={self.text},)"



    


class ResourceLink(Base):
    """
    A URL-based pointer to an external resource with an optional hash for verification and change detection.
    """
    __tablename__ = 'ResourceLink'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    href = Column(Text(), nullable=False )
    media_type = Column(Text())
    Resource_id = Column(Integer(), ForeignKey('Resource.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='ResourceLink', source_slot='hashes', mapping_type=None, target_class='Hash', target_slot='ResourceLink_id', join_class=None, uses_join_table=None, multivalued=False)
    hashes = relationship( "Hash", foreign_keys="[Hash.ResourceLink_id]")
    

    def __repr__(self):
        return f"ResourceLink(id={self.id},href={self.href},media_type={self.media_type},Resource_id={self.Resource_id},)"



    


class Base64Resource(Base):
    """
    A resource encoded using the Base64 alphabet defined by RFC 2045.
    """
    __tablename__ = 'Base64Resource'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    media_type = Column(Text())
    value = Column(Text(), nullable=False )
    filename = Column(Text())
    

    def __repr__(self):
        return f"Base64Resource(id={self.id},media_type={self.media_type},value={self.value},filename={self.filename},)"



    


class Part(Base):
    """
    An annotated, markup-based textual element of a control's or catalog group's definition, or a child of another part.
    """
    __tablename__ = 'Part'

    uid = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    id = Column(Text())
    name = Column(Text(), nullable=False )
    ns = Column(Text())
    _class = Column(Text())
    title = Column(Text())
    prose = Column(Text())
    Group_uid = Column(Integer(), ForeignKey('Group.uid'))
    Control_uid = Column(Integer(), ForeignKey('Control.uid'))
    Part_uid = Column(Integer(), ForeignKey('Part.uid'))
    ProfileGroup_uid = Column(Integer(), ForeignKey('ProfileGroup.uid'))
    Addition_id = Column(Integer(), ForeignKey('Addition.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='Part', source_slot='parts', mapping_type=None, target_class='Part', target_slot='Part_uid', join_class=None, uses_join_table=None, multivalued=False)
    parts = relationship( "Part", foreign_keys="[Part.Part_uid]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Part', source_slot='props', mapping_type=None, target_class='PartProperty', target_slot='Part_uid', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "PartProperty", foreign_keys="[PartProperty.Part_uid]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Part', source_slot='links', mapping_type=None, target_class='Link', target_slot='Part_uid', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "Link", foreign_keys="[Link.Part_uid]")
    

    def __repr__(self):
        return f"Part(uid={self.uid},id={self.id},name={self.name},ns={self.ns},_class={self._class},title={self.title},prose={self.prose},Group_uid={self.Group_uid},Control_uid={self.Control_uid},Part_uid={self.Part_uid},ProfileGroup_uid={self.ProfileGroup_uid},Addition_id={self.Addition_id},)"



    


class Parameter(Base):
    """
    Parameters provide a mechanism for the dynamic assignment of value(s) in a control.
    """
    __tablename__ = 'Parameter'

    uid = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    id = Column(Text(), nullable=False )
    _class = Column(Text())
    depends_on = Column(Text())
    label = Column(Text())
    usage = Column(Text())
    remarks = Column(Text())
    Catalog_id = Column(Integer(), ForeignKey('Catalog.id'))
    Group_uid = Column(Integer(), ForeignKey('Group.uid'))
    Control_uid = Column(Integer(), ForeignKey('Control.uid'))
    ProfileGroup_uid = Column(Integer(), ForeignKey('ProfileGroup.uid'))
    Addition_id = Column(Integer(), ForeignKey('Addition.id'))
    select_id = Column(Integer(), ForeignKey('ParameterSelection.id'))
    select = relationship("ParameterSelection", uselist=False, foreign_keys=[select_id])
    
    
    # One-To-Many: OneToAnyMapping(source_class='Parameter', source_slot='constraints', mapping_type=None, target_class='ParameterConstraint', target_slot='Parameter_uid', join_class=None, uses_join_table=None, multivalued=False)
    constraints = relationship( "ParameterConstraint", foreign_keys="[ParameterConstraint.Parameter_uid]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Parameter', source_slot='guidelines', mapping_type=None, target_class='ParameterGuideline', target_slot='Parameter_uid', join_class=None, uses_join_table=None, multivalued=False)
    guidelines = relationship( "ParameterGuideline", foreign_keys="[ParameterGuideline.Parameter_uid]")
    
    
    values_rel = relationship( "ParameterValues" )
    values = association_proxy("values_rel", "values",
                                  creator=lambda x_: ParameterValues(values=x_))
    
    
    # One-To-Many: OneToAnyMapping(source_class='Parameter', source_slot='props', mapping_type=None, target_class='ParameterProperty', target_slot='Parameter_uid', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "ParameterProperty", foreign_keys="[ParameterProperty.Parameter_uid]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Parameter', source_slot='links', mapping_type=None, target_class='Link', target_slot='Parameter_uid', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "Link", foreign_keys="[Link.Parameter_uid]")
    

    def __repr__(self):
        return f"Parameter(uid={self.uid},id={self.id},_class={self._class},depends_on={self.depends_on},label={self.label},usage={self.usage},remarks={self.remarks},Catalog_id={self.Catalog_id},Group_uid={self.Group_uid},Control_uid={self.Control_uid},ProfileGroup_uid={self.ProfileGroup_uid},Addition_id={self.Addition_id},select_id={self.select_id},)"



    


class ParameterConstraint(Base):
    """
    A formal or informal expression of a constraint or test.
    """
    __tablename__ = 'ParameterConstraint'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    description = Column(Text())
    Parameter_uid = Column(Integer(), ForeignKey('Parameter.uid'))
    ParameterSetting_id = Column(Integer(), ForeignKey('ParameterSetting.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='ParameterConstraint', source_slot='tests', mapping_type=None, target_class='ConstraintTest', target_slot='ParameterConstraint_id', join_class=None, uses_join_table=None, multivalued=False)
    tests = relationship( "ConstraintTest", foreign_keys="[ConstraintTest.ParameterConstraint_id]")
    

    def __repr__(self):
        return f"ParameterConstraint(id={self.id},description={self.description},Parameter_uid={self.Parameter_uid},ParameterSetting_id={self.ParameterSetting_id},)"



    


class ConstraintTest(Base):
    """
    A test expression which is expected to be evaluated by a tool.
    """
    __tablename__ = 'ConstraintTest'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    remarks = Column(Text())
    expression = Column(Text(), nullable=False )
    ParameterConstraint_id = Column(Integer(), ForeignKey('ParameterConstraint.id'))
    

    def __repr__(self):
        return f"ConstraintTest(id={self.id},remarks={self.remarks},expression={self.expression},ParameterConstraint_id={self.ParameterConstraint_id},)"



    


class ParameterGuideline(Base):
    """
    A prose statement that provides a recommendation for the use of a parameter.
    """
    __tablename__ = 'ParameterGuideline'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    prose = Column(Text(), nullable=False )
    Parameter_uid = Column(Integer(), ForeignKey('Parameter.uid'))
    ParameterSetting_id = Column(Integer(), ForeignKey('ParameterSetting.id'))
    

    def __repr__(self):
        return f"ParameterGuideline(id={self.id},prose={self.prose},Parameter_uid={self.Parameter_uid},ParameterSetting_id={self.ParameterSetting_id},)"



    


class ParameterSelection(Base):
    """
    Presenting a choice among alternatives.
    """
    __tablename__ = 'ParameterSelection'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    how_many = Column(Enum('one', 'one-or-more', name='ParameterCardinalityEnum'))
    
    
    choice_rel = relationship( "ParameterSelectionChoice" )
    choice = association_proxy("choice_rel", "choice",
                                  creator=lambda x_: ParameterSelectionChoice(choice=x_))
    

    def __repr__(self):
        return f"ParameterSelection(id={self.id},how_many={self.how_many},)"



    


class IncludeAll(Base):
    """
    Include all controls from the imported catalog or profile resources.
    """
    __tablename__ = 'IncludeAll'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    

    def __repr__(self):
        return f"IncludeAll(id={self.id},)"



    


class ControlMatching(Base):
    """
    Selecting a set of controls by matching their IDs with a wildcard pattern.
    """
    __tablename__ = 'ControlMatching'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    remarks = Column(Text())
    pattern = Column(Text())
    SelectControlById_id = Column(Integer(), ForeignKey('SelectControlById.id'))
    

    def __repr__(self):
        return f"ControlMatching(id={self.id},remarks={self.remarks},pattern={self.pattern},SelectControlById_id={self.SelectControlById_id},)"



    


class SelectControlById(Base):
    """
    Select a control or controls from an imported control set.
    """
    __tablename__ = 'SelectControlById'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    with_child_controls = Column(Enum('yes', 'no', name='WithChildControlsEnum'))
    ProfileImport_id = Column(Integer(), ForeignKey('ProfileImport.id'))
    InsertControls_id = Column(Integer(), ForeignKey('InsertControls.id'))
    GapSummary_id = Column(Integer(), ForeignKey('GapSummary.id'))
    
    
    with_ids_rel = relationship( "SelectControlByIdWithIds" )
    with_ids = association_proxy("with_ids_rel", "with_ids",
                                  creator=lambda x_: SelectControlByIdWithIds(with_ids=x_))
    
    
    # One-To-Many: OneToAnyMapping(source_class='SelectControlById', source_slot='matching', mapping_type=None, target_class='ControlMatching', target_slot='SelectControlById_id', join_class=None, uses_join_table=None, multivalued=False)
    matching = relationship( "ControlMatching", foreign_keys="[ControlMatching.SelectControlById_id]")
    

    def __repr__(self):
        return f"SelectControlById(id={self.id},with_child_controls={self.with_child_controls},ProfileImport_id={self.ProfileImport_id},InsertControls_id={self.InsertControls_id},GapSummary_id={self.GapSummary_id},)"



    


class Profile(Base):
    """
    An OSCAL Profile that designates a set of controls from one or more catalogs or profiles, optionally restructures and modifies them, to describe a basis for a security standard or body of practice.
    """
    __tablename__ = 'Profile'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    uuid = Column(Text(), nullable=False )
    metadata_id = Column(Integer(), ForeignKey('Metadata.id'), nullable=False )
    metadata = relationship("Metadata", uselist=False, foreign_keys=[metadata_id])
    merge_id = Column(Integer(), ForeignKey('ProfileMerge.id'))
    merge = relationship("ProfileMerge", uselist=False, foreign_keys=[merge_id])
    modify_id = Column(Integer(), ForeignKey('ProfileModify.id'))
    modify = relationship("ProfileModify", uselist=False, foreign_keys=[modify_id])
    back_matter_id = Column(Integer(), ForeignKey('BackMatter.id'))
    back_matter = relationship("BackMatter", uselist=False, foreign_keys=[back_matter_id])
    
    
    # One-To-Many: OneToAnyMapping(source_class='Profile', source_slot='imports', mapping_type=None, target_class='ProfileImport', target_slot='Profile_id', join_class=None, uses_join_table=None, multivalued=False)
    imports = relationship( "ProfileImport", foreign_keys="[ProfileImport.Profile_id]")
    

    def __repr__(self):
        return f"Profile(id={self.id},uuid={self.uuid},metadata_id={self.metadata_id},merge_id={self.merge_id},modify_id={self.modify_id},back_matter_id={self.back_matter_id},)"



    


class ProfileImport(Base):
    """
    Designates a referenced source catalog or profile that provides a source of control information for use in creating a new overlay or baseline.
    """
    __tablename__ = 'ProfileImport'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    href = Column(Text(), nullable=False )
    Profile_id = Column(Integer(), ForeignKey('Profile.id'))
    include_all_id = Column(Integer(), ForeignKey('IncludeAll.id'))
    include_all = relationship("IncludeAll", uselist=False, foreign_keys=[include_all_id])
    
    
    # One-To-Many: OneToAnyMapping(source_class='ProfileImport', source_slot='include_controls', mapping_type=None, target_class='SelectControlById', target_slot='ProfileImport_id', join_class=None, uses_join_table=None, multivalued=False)
    include_controls = relationship( "SelectControlById", foreign_keys="[SelectControlById.ProfileImport_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='ProfileImport', source_slot='exclude_controls', mapping_type=None, target_class='SelectControlById', target_slot='ProfileImport_id', join_class=None, uses_join_table=None, multivalued=False)
    exclude_controls = relationship( "SelectControlById", foreign_keys="[SelectControlById.ProfileImport_id]")
    

    def __repr__(self):
        return f"ProfileImport(id={self.id},href={self.href},Profile_id={self.Profile_id},include_all_id={self.include_all_id},)"



    


class ProfileMerge(Base):
    """
    Provides structuring directives that instruct how controls are organized after profile resolution.
    """
    __tablename__ = 'ProfileMerge'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    as_is = Column(Boolean())
    combine_id = Column(Integer(), ForeignKey('CombinationRule.id'))
    combine = relationship("CombinationRule", uselist=False, foreign_keys=[combine_id])
    flat_id = Column(Integer(), ForeignKey('MergeFlat.id'))
    flat = relationship("MergeFlat", uselist=False, foreign_keys=[flat_id])
    custom_id = Column(Integer(), ForeignKey('MergeCustom.id'))
    custom = relationship("MergeCustom", uselist=False, foreign_keys=[custom_id])
    

    def __repr__(self):
        return f"ProfileMerge(id={self.id},as_is={self.as_is},combine_id={self.combine_id},flat_id={self.flat_id},custom_id={self.custom_id},)"



    


class CombinationRule(Base):
    """
    Defines how to resolve duplicate instances of the same control (e.g., controls with the same ID) encountered in a profile merge.
    """
    __tablename__ = 'CombinationRule'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    method = Column(Enum('use-first', 'merge', 'keep', name='CombinationMethodEnum'))
    

    def __repr__(self):
        return f"CombinationRule(id={self.id},method={self.method},)"



    


class MergeFlat(Base):
    """
    Directs that controls appear without any grouping structure after profile resolution.
    """
    __tablename__ = 'MergeFlat'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    

    def __repr__(self):
        return f"MergeFlat(id={self.id},)"



    


class MergeCustom(Base):
    """
    Provides an alternate grouping structure that selected controls will be placed in after profile resolution.
    """
    __tablename__ = 'MergeCustom'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    
    
    # One-To-Many: OneToAnyMapping(source_class='MergeCustom', source_slot='groups', mapping_type=None, target_class='ProfileGroup', target_slot='MergeCustom_id', join_class=None, uses_join_table=None, multivalued=False)
    groups = relationship( "ProfileGroup", foreign_keys="[ProfileGroup.MergeCustom_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='MergeCustom', source_slot='insert_controls', mapping_type=None, target_class='InsertControls', target_slot='MergeCustom_id', join_class=None, uses_join_table=None, multivalued=False)
    insert_controls = relationship( "InsertControls", foreign_keys="[InsertControls.MergeCustom_id]")
    

    def __repr__(self):
        return f"MergeCustom(id={self.id},)"



    


class ProfileGroup(Base):
    """
    A group of (selected) controls or of groups of controls within a profile custom merge structure.
    """
    __tablename__ = 'ProfileGroup'

    uid = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    id = Column(Text())
    _class = Column(Text())
    title = Column(Text(), nullable=False )
    remarks = Column(Text())
    MergeCustom_id = Column(Integer(), ForeignKey('MergeCustom.id'))
    ProfileGroup_uid = Column(Integer(), ForeignKey('ProfileGroup.uid'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='ProfileGroup', source_slot='params', mapping_type=None, target_class='Parameter', target_slot='ProfileGroup_uid', join_class=None, uses_join_table=None, multivalued=False)
    params = relationship( "Parameter", foreign_keys="[Parameter.ProfileGroup_uid]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='ProfileGroup', source_slot='parts', mapping_type=None, target_class='Part', target_slot='ProfileGroup_uid', join_class=None, uses_join_table=None, multivalued=False)
    parts = relationship( "Part", foreign_keys="[Part.ProfileGroup_uid]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='ProfileGroup', source_slot='groups', mapping_type=None, target_class='ProfileGroup', target_slot='ProfileGroup_uid', join_class=None, uses_join_table=None, multivalued=False)
    groups = relationship( "ProfileGroup", foreign_keys="[ProfileGroup.ProfileGroup_uid]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='ProfileGroup', source_slot='insert_controls', mapping_type=None, target_class='InsertControls', target_slot='ProfileGroup_uid', join_class=None, uses_join_table=None, multivalued=False)
    insert_controls = relationship( "InsertControls", foreign_keys="[InsertControls.ProfileGroup_uid]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='ProfileGroup', source_slot='props', mapping_type=None, target_class='Property', target_slot='ProfileGroup_uid', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "Property", foreign_keys="[Property.ProfileGroup_uid]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='ProfileGroup', source_slot='links', mapping_type=None, target_class='Link', target_slot='ProfileGroup_uid', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "Link", foreign_keys="[Link.ProfileGroup_uid]")
    

    def __repr__(self):
        return f"ProfileGroup(uid={self.uid},id={self.id},_class={self._class},title={self.title},remarks={self.remarks},MergeCustom_id={self.MergeCustom_id},ProfileGroup_uid={self.ProfileGroup_uid},)"



    


class ProfileModify(Base):
    """
    Set parameters or amend controls in resolution.
    """
    __tablename__ = 'ProfileModify'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    
    
    # One-To-Many: OneToAnyMapping(source_class='ProfileModify', source_slot='set_parameters', mapping_type=None, target_class='ParameterSetting', target_slot='ProfileModify_id', join_class=None, uses_join_table=None, multivalued=False)
    set_parameters = relationship( "ParameterSetting", foreign_keys="[ParameterSetting.ProfileModify_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='ProfileModify', source_slot='alters', mapping_type=None, target_class='Alteration', target_slot='ProfileModify_id', join_class=None, uses_join_table=None, multivalued=False)
    alters = relationship( "Alteration", foreign_keys="[Alteration.ProfileModify_id]")
    

    def __repr__(self):
        return f"ProfileModify(id={self.id},)"



    


class ParameterSetting(Base):
    """
    A parameter setting to be propagated to points of insertion in a resolved profile.
    """
    __tablename__ = 'ParameterSetting'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    param_id = Column(Text(), nullable=False )
    _class = Column(Text())
    depends_on = Column(Text())
    label = Column(Text())
    usage = Column(Text())
    ProfileModify_id = Column(Integer(), ForeignKey('ProfileModify.id'))
    select_id = Column(Integer(), ForeignKey('ParameterSelection.id'))
    select = relationship("ParameterSelection", uselist=False, foreign_keys=[select_id])
    
    
    # One-To-Many: OneToAnyMapping(source_class='ParameterSetting', source_slot='constraints', mapping_type=None, target_class='ParameterConstraint', target_slot='ParameterSetting_id', join_class=None, uses_join_table=None, multivalued=False)
    constraints = relationship( "ParameterConstraint", foreign_keys="[ParameterConstraint.ParameterSetting_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='ParameterSetting', source_slot='guidelines', mapping_type=None, target_class='ParameterGuideline', target_slot='ParameterSetting_id', join_class=None, uses_join_table=None, multivalued=False)
    guidelines = relationship( "ParameterGuideline", foreign_keys="[ParameterGuideline.ParameterSetting_id]")
    
    
    values_rel = relationship( "ParameterSettingValues" )
    values = association_proxy("values_rel", "values",
                                  creator=lambda x_: ParameterSettingValues(values=x_))
    
    
    # One-To-Many: OneToAnyMapping(source_class='ParameterSetting', source_slot='props', mapping_type=None, target_class='Property', target_slot='ParameterSetting_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "Property", foreign_keys="[Property.ParameterSetting_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='ParameterSetting', source_slot='links', mapping_type=None, target_class='Link', target_slot='ParameterSetting_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "Link", foreign_keys="[Link.ParameterSetting_id]")
    

    def __repr__(self):
        return f"ParameterSetting(id={self.id},param_id={self.param_id},_class={self._class},depends_on={self.depends_on},label={self.label},usage={self.usage},ProfileModify_id={self.ProfileModify_id},select_id={self.select_id},)"



    


class Alteration(Base):
    """
    Specifies changes to be made to an included control when a profile is resolved.
    """
    __tablename__ = 'Alteration'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    control_id = Column(Text(), nullable=False )
    ProfileModify_id = Column(Integer(), ForeignKey('ProfileModify.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='Alteration', source_slot='removes', mapping_type=None, target_class='Removal', target_slot='Alteration_id', join_class=None, uses_join_table=None, multivalued=False)
    removes = relationship( "Removal", foreign_keys="[Removal.Alteration_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Alteration', source_slot='adds', mapping_type=None, target_class='Addition', target_slot='Alteration_id', join_class=None, uses_join_table=None, multivalued=False)
    adds = relationship( "Addition", foreign_keys="[Addition.Alteration_id]")
    

    def __repr__(self):
        return f"Alteration(id={self.id},control_id={self.control_id},ProfileModify_id={self.ProfileModify_id},)"



    


class Removal(Base):
    """
    Specifies objects to be removed from a control based on aspects of the object that must all match.
    """
    __tablename__ = 'Removal'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    by_name = Column(Text())
    by_class = Column(Text())
    by_id = Column(Text())
    by_item_name = Column(Enum('param', 'prop', 'link', 'part', 'mapping', 'map', name='ByItemNameEnum'))
    by_ns = Column(Text())
    remarks = Column(Text())
    Alteration_id = Column(Integer(), ForeignKey('Alteration.id'))
    

    def __repr__(self):
        return f"Removal(id={self.id},by_name={self.by_name},by_class={self.by_class},by_id={self.by_id},by_item_name={self.by_item_name},by_ns={self.by_ns},remarks={self.remarks},Alteration_id={self.Alteration_id},)"



    


class Addition(Base):
    """
    Specifies content to be added into controls in resolution.
    """
    __tablename__ = 'Addition'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    position = Column(Enum('before', 'after', 'starting', 'ending', name='AdditionPositionEnum'))
    by_id = Column(Text())
    title = Column(Text())
    Alteration_id = Column(Integer(), ForeignKey('Alteration.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='Addition', source_slot='params', mapping_type=None, target_class='Parameter', target_slot='Addition_id', join_class=None, uses_join_table=None, multivalued=False)
    params = relationship( "Parameter", foreign_keys="[Parameter.Addition_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Addition', source_slot='props', mapping_type=None, target_class='ProfileAlterationProperty', target_slot='Addition_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "ProfileAlterationProperty", foreign_keys="[ProfileAlterationProperty.Addition_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Addition', source_slot='links', mapping_type=None, target_class='Link', target_slot='Addition_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "Link", foreign_keys="[Link.Addition_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Addition', source_slot='parts', mapping_type=None, target_class='Part', target_slot='Addition_id', join_class=None, uses_join_table=None, multivalued=False)
    parts = relationship( "Part", foreign_keys="[Part.Addition_id]")
    

    def __repr__(self):
        return f"Addition(id={self.id},position={self.position},by_id={self.by_id},title={self.title},Alteration_id={self.Alteration_id},)"



    


class InsertControls(Base):
    """
    Specifies which controls to use in the containing context (as part of a group or custom merge structure).
    """
    __tablename__ = 'InsertControls'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    order = Column(Enum('keep', 'ascending', 'descending', name='InsertOrderEnum'))
    MergeCustom_id = Column(Integer(), ForeignKey('MergeCustom.id'))
    ProfileGroup_uid = Column(Integer(), ForeignKey('ProfileGroup.uid'))
    include_all_id = Column(Integer(), ForeignKey('IncludeAll.id'))
    include_all = relationship("IncludeAll", uselist=False, foreign_keys=[include_all_id])
    
    
    # One-To-Many: OneToAnyMapping(source_class='InsertControls', source_slot='include_controls', mapping_type=None, target_class='SelectControlById', target_slot='InsertControls_id', join_class=None, uses_join_table=None, multivalued=False)
    include_controls = relationship( "SelectControlById", foreign_keys="[SelectControlById.InsertControls_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='InsertControls', source_slot='exclude_controls', mapping_type=None, target_class='SelectControlById', target_slot='InsertControls_id', join_class=None, uses_join_table=None, multivalued=False)
    exclude_controls = relationship( "SelectControlById", foreign_keys="[SelectControlById.InsertControls_id]")
    

    def __repr__(self):
        return f"InsertControls(id={self.id},order={self.order},MergeCustom_id={self.MergeCustom_id},ProfileGroup_uid={self.ProfileGroup_uid},include_all_id={self.include_all_id},)"



    


class AssessmentPlan(Base):
    """
    An assessment plan, such as those provided by a FedRAMP assessor.
    """
    __tablename__ = 'AssessmentPlan'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    uuid = Column(Text(), nullable=False )
    metadata_id = Column(Integer(), ForeignKey('Metadata.id'), nullable=False )
    metadata = relationship("Metadata", uselist=False, foreign_keys=[metadata_id])
    import_ssp_id = Column(Integer(), ForeignKey('ImportSSP.id'), nullable=False )
    import_ssp = relationship("ImportSSP", uselist=False, foreign_keys=[import_ssp_id])
    local_definitions_id = Column(Integer(), ForeignKey('LocalDefinitions.id'))
    local_definitions = relationship("LocalDefinitions", uselist=False, foreign_keys=[local_definitions_id])
    terms_and_conditions_id = Column(Integer(), ForeignKey('TermsAndConditions.id'))
    terms_and_conditions = relationship("TermsAndConditions", uselist=False, foreign_keys=[terms_and_conditions_id])
    assessment_assets_id = Column(Integer(), ForeignKey('AssessmentAssets.id'))
    assessment_assets = relationship("AssessmentAssets", uselist=False, foreign_keys=[assessment_assets_id])
    reviewed_controls_id = Column(Integer(), ForeignKey('ReviewedControls.id'), nullable=False )
    reviewed_controls = relationship("ReviewedControls", uselist=False, foreign_keys=[reviewed_controls_id])
    back_matter_id = Column(Integer(), ForeignKey('BackMatter.id'))
    back_matter = relationship("BackMatter", uselist=False, foreign_keys=[back_matter_id])
    
    
    # One-To-Many: OneToAnyMapping(source_class='AssessmentPlan', source_slot='assessment_subjects', mapping_type=None, target_class='AssessmentSubject', target_slot='AssessmentPlan_id', join_class=None, uses_join_table=None, multivalued=False)
    assessment_subjects = relationship( "AssessmentSubject", foreign_keys="[AssessmentSubject.AssessmentPlan_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='AssessmentPlan', source_slot='tasks', mapping_type=None, target_class='Task', target_slot='AssessmentPlan_id', join_class=None, uses_join_table=None, multivalued=False)
    tasks = relationship( "Task", foreign_keys="[Task.AssessmentPlan_id]")
    

    def __repr__(self):
        return f"AssessmentPlan(id={self.id},uuid={self.uuid},metadata_id={self.metadata_id},import_ssp_id={self.import_ssp_id},local_definitions_id={self.local_definitions_id},terms_and_conditions_id={self.terms_and_conditions_id},assessment_assets_id={self.assessment_assets_id},reviewed_controls_id={self.reviewed_controls_id},back_matter_id={self.back_matter_id},)"



    


class ImportSSP(Base):
    """
    Used by the assessment plan and POA&M to import information about the system.
    """
    __tablename__ = 'ImportSSP'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    href = Column(Text(), nullable=False )
    remarks = Column(Text())
    

    def __repr__(self):
        return f"ImportSSP(id={self.id},href={self.href},remarks={self.remarks},)"



    


class LocalDefinitions(Base):
    """
    Used to define data objects that are used in the assessment plan, that do not appear in the referenced SSP.
    """
    __tablename__ = 'LocalDefinitions'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    remarks = Column(Text())
    
    
    # One-To-Many: OneToAnyMapping(source_class='LocalDefinitions', source_slot='components', mapping_type=None, target_class='SystemComponent', target_slot='LocalDefinitions_id', join_class=None, uses_join_table=None, multivalued=False)
    components = relationship( "SystemComponent", foreign_keys="[SystemComponent.LocalDefinitions_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='LocalDefinitions', source_slot='inventory_items', mapping_type=None, target_class='InventoryItem', target_slot='LocalDefinitions_id', join_class=None, uses_join_table=None, multivalued=False)
    inventory_items = relationship( "InventoryItem", foreign_keys="[InventoryItem.LocalDefinitions_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='LocalDefinitions', source_slot='users', mapping_type=None, target_class='SystemUser', target_slot='LocalDefinitions_id', join_class=None, uses_join_table=None, multivalued=False)
    users = relationship( "SystemUser", foreign_keys="[SystemUser.LocalDefinitions_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='LocalDefinitions', source_slot='objectives_and_methods', mapping_type=None, target_class='LocalObjective', target_slot='LocalDefinitions_id', join_class=None, uses_join_table=None, multivalued=False)
    objectives_and_methods = relationship( "LocalObjective", foreign_keys="[LocalObjective.LocalDefinitions_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='LocalDefinitions', source_slot='activities', mapping_type=None, target_class='Activity', target_slot='LocalDefinitions_id', join_class=None, uses_join_table=None, multivalued=False)
    activities = relationship( "Activity", foreign_keys="[Activity.LocalDefinitions_id]")
    

    def __repr__(self):
        return f"LocalDefinitions(id={self.id},remarks={self.remarks},)"



    


class TermsAndConditions(Base):
    """
    Used to define various terms and conditions under which an assessment can be performed.
    """
    __tablename__ = 'TermsAndConditions'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    
    
    # One-To-Many: OneToAnyMapping(source_class='TermsAndConditions', source_slot='parts', mapping_type=None, target_class='TermsAndConditionsPart', target_slot='TermsAndConditions_id', join_class=None, uses_join_table=None, multivalued=False)
    parts = relationship( "TermsAndConditionsPart", foreign_keys="[TermsAndConditionsPart.TermsAndConditions_id]")
    

    def __repr__(self):
        return f"TermsAndConditions(id={self.id},)"



    


class ReviewedControls(Base):
    """
    Identifies the controls being assessed and their control objectives.
    """
    __tablename__ = 'ReviewedControls'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    description = Column(Text())
    remarks = Column(Text())
    
    
    # One-To-Many: OneToAnyMapping(source_class='ReviewedControls', source_slot='control_selections', mapping_type=None, target_class='ControlSelection', target_slot='ReviewedControls_id', join_class=None, uses_join_table=None, multivalued=False)
    control_selections = relationship( "ControlSelection", foreign_keys="[ControlSelection.ReviewedControls_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='ReviewedControls', source_slot='control_objective_selections', mapping_type=None, target_class='ControlObjectiveSelection', target_slot='ReviewedControls_id', join_class=None, uses_join_table=None, multivalued=False)
    control_objective_selections = relationship( "ControlObjectiveSelection", foreign_keys="[ControlObjectiveSelection.ReviewedControls_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='ReviewedControls', source_slot='props', mapping_type=None, target_class='Property', target_slot='ReviewedControls_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "Property", foreign_keys="[Property.ReviewedControls_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='ReviewedControls', source_slot='links', mapping_type=None, target_class='Link', target_slot='ReviewedControls_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "Link", foreign_keys="[Link.ReviewedControls_id]")
    

    def __repr__(self):
        return f"ReviewedControls(id={self.id},description={self.description},remarks={self.remarks},)"



    


class ControlSelection(Base):
    """
    Identifies the controls being assessed.
    """
    __tablename__ = 'ControlSelection'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    description = Column(Text())
    remarks = Column(Text())
    ReviewedControls_id = Column(Integer(), ForeignKey('ReviewedControls.id'))
    include_all_id = Column(Integer(), ForeignKey('IncludeAll.id'))
    include_all = relationship("IncludeAll", uselist=False, foreign_keys=[include_all_id])
    
    
    # One-To-Many: OneToAnyMapping(source_class='ControlSelection', source_slot='include_controls', mapping_type=None, target_class='AssessmentSelectControlById', target_slot='ControlSelection_id', join_class=None, uses_join_table=None, multivalued=False)
    include_controls = relationship( "AssessmentSelectControlById", foreign_keys="[AssessmentSelectControlById.ControlSelection_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='ControlSelection', source_slot='exclude_controls', mapping_type=None, target_class='AssessmentSelectControlById', target_slot='ControlSelection_id', join_class=None, uses_join_table=None, multivalued=False)
    exclude_controls = relationship( "AssessmentSelectControlById", foreign_keys="[AssessmentSelectControlById.ControlSelection_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='ControlSelection', source_slot='props', mapping_type=None, target_class='Property', target_slot='ControlSelection_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "Property", foreign_keys="[Property.ControlSelection_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='ControlSelection', source_slot='links', mapping_type=None, target_class='Link', target_slot='ControlSelection_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "Link", foreign_keys="[Link.ControlSelection_id]")
    

    def __repr__(self):
        return f"ControlSelection(id={self.id},description={self.description},remarks={self.remarks},ReviewedControls_id={self.ReviewedControls_id},include_all_id={self.include_all_id},)"



    


class ControlObjectiveSelection(Base):
    """
    Identifies the control objectives of the assessment.
    """
    __tablename__ = 'ControlObjectiveSelection'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    description = Column(Text())
    remarks = Column(Text())
    ReviewedControls_id = Column(Integer(), ForeignKey('ReviewedControls.id'))
    include_all_id = Column(Integer(), ForeignKey('IncludeAll.id'))
    include_all = relationship("IncludeAll", uselist=False, foreign_keys=[include_all_id])
    
    
    # One-To-Many: OneToAnyMapping(source_class='ControlObjectiveSelection', source_slot='include_objectives', mapping_type=None, target_class='SelectObjectiveById', target_slot='ControlObjectiveSelection_id', join_class=None, uses_join_table=None, multivalued=False)
    include_objectives = relationship( "SelectObjectiveById", foreign_keys="[SelectObjectiveById.ControlObjectiveSelection_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='ControlObjectiveSelection', source_slot='exclude_objectives', mapping_type=None, target_class='SelectObjectiveById', target_slot='ControlObjectiveSelection_id', join_class=None, uses_join_table=None, multivalued=False)
    exclude_objectives = relationship( "SelectObjectiveById", foreign_keys="[SelectObjectiveById.ControlObjectiveSelection_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='ControlObjectiveSelection', source_slot='props', mapping_type=None, target_class='Property', target_slot='ControlObjectiveSelection_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "Property", foreign_keys="[Property.ControlObjectiveSelection_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='ControlObjectiveSelection', source_slot='links', mapping_type=None, target_class='Link', target_slot='ControlObjectiveSelection_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "Link", foreign_keys="[Link.ControlObjectiveSelection_id]")
    

    def __repr__(self):
        return f"ControlObjectiveSelection(id={self.id},description={self.description},remarks={self.remarks},ReviewedControls_id={self.ReviewedControls_id},include_all_id={self.include_all_id},)"



    


class AssessmentSelectControlById(Base):
    """
    Select a specific control for inclusion/exclusion in the assessment by literal control ID and optional statement IDs.
    """
    __tablename__ = 'AssessmentSelectControlById'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    control_id = Column(Text(), nullable=False )
    ControlSelection_id = Column(Integer(), ForeignKey('ControlSelection.id'))
    
    
    statement_ids_rel = relationship( "AssessmentSelectControlByIdStatementIds" )
    statement_ids = association_proxy("statement_ids_rel", "statement_ids",
                                  creator=lambda x_: AssessmentSelectControlByIdStatementIds(statement_ids=x_))
    

    def __repr__(self):
        return f"AssessmentSelectControlById(id={self.id},control_id={self.control_id},ControlSelection_id={self.ControlSelection_id},)"



    


class SelectObjectiveById(Base):
    """
    Used to select a control objective for inclusion/exclusion.
    """
    __tablename__ = 'SelectObjectiveById'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    objective_id = Column(Text(), nullable=False )
    remarks = Column(Text())
    ControlObjectiveSelection_id = Column(Integer(), ForeignKey('ControlObjectiveSelection.id'))
    

    def __repr__(self):
        return f"SelectObjectiveById(id={self.id},objective_id={self.objective_id},remarks={self.remarks},ControlObjectiveSelection_id={self.ControlObjectiveSelection_id},)"



    


class AssessmentSubject(Base):
    """
    Identifies system elements being assessed, such as components, inventory items, and locations.
    """
    __tablename__ = 'AssessmentSubject'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    type = Column(Text(), nullable=False )
    description = Column(Text())
    remarks = Column(Text())
    AssessmentPlan_id = Column(Integer(), ForeignKey('AssessmentPlan.id'))
    Task_id = Column(Integer(), ForeignKey('Task.id'))
    AssociatedActivity_id = Column(Integer(), ForeignKey('AssociatedActivity.id'))
    RelatedTask_id = Column(Integer(), ForeignKey('RelatedTask.id'))
    IdentifiedSubject_id = Column(Integer(), ForeignKey('IdentifiedSubject.id'))
    include_all_id = Column(Integer(), ForeignKey('IncludeAll.id'))
    include_all = relationship("IncludeAll", uselist=False, foreign_keys=[include_all_id])
    
    
    # One-To-Many: OneToAnyMapping(source_class='AssessmentSubject', source_slot='include_subjects', mapping_type=None, target_class='SelectSubjectById', target_slot='AssessmentSubject_id', join_class=None, uses_join_table=None, multivalued=False)
    include_subjects = relationship( "SelectSubjectById", foreign_keys="[SelectSubjectById.AssessmentSubject_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='AssessmentSubject', source_slot='exclude_subjects', mapping_type=None, target_class='SelectSubjectById', target_slot='AssessmentSubject_id', join_class=None, uses_join_table=None, multivalued=False)
    exclude_subjects = relationship( "SelectSubjectById", foreign_keys="[SelectSubjectById.AssessmentSubject_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='AssessmentSubject', source_slot='props', mapping_type=None, target_class='Property', target_slot='AssessmentSubject_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "Property", foreign_keys="[Property.AssessmentSubject_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='AssessmentSubject', source_slot='links', mapping_type=None, target_class='Link', target_slot='AssessmentSubject_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "Link", foreign_keys="[Link.AssessmentSubject_id]")
    

    def __repr__(self):
        return f"AssessmentSubject(id={self.id},type={self.type},description={self.description},remarks={self.remarks},AssessmentPlan_id={self.AssessmentPlan_id},Task_id={self.Task_id},AssociatedActivity_id={self.AssociatedActivity_id},RelatedTask_id={self.RelatedTask_id},IdentifiedSubject_id={self.IdentifiedSubject_id},include_all_id={self.include_all_id},)"



    


class SelectSubjectById(Base):
    """
    Identifies a set of assessment subjects to include/exclude by UUID.
    """
    __tablename__ = 'SelectSubjectById'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    subject_uuid = Column(Text(), nullable=False )
    type = Column(Text(), nullable=False )
    remarks = Column(Text())
    AssessmentSubject_id = Column(Integer(), ForeignKey('AssessmentSubject.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='SelectSubjectById', source_slot='props', mapping_type=None, target_class='Property', target_slot='SelectSubjectById_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "Property", foreign_keys="[Property.SelectSubjectById_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='SelectSubjectById', source_slot='links', mapping_type=None, target_class='Link', target_slot='SelectSubjectById_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "Link", foreign_keys="[Link.SelectSubjectById_id]")
    

    def __repr__(self):
        return f"SelectSubjectById(id={self.id},subject_uuid={self.subject_uuid},type={self.type},remarks={self.remarks},AssessmentSubject_id={self.AssessmentSubject_id},)"



    


class SubjectReference(Base):
    """
    A human-oriented identifier reference to a resource. Use type to indicate whether the identified resource is a component, inventory item, location, user, or something else.
    """
    __tablename__ = 'SubjectReference'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    subject_uuid = Column(Text(), nullable=False )
    type = Column(Text(), nullable=False )
    title = Column(Text())
    remarks = Column(Text())
    Observation_id = Column(Integer(), ForeignKey('Observation.id'))
    MitigatingFactor_id = Column(Integer(), ForeignKey('MitigatingFactor.id'))
    RequiredAsset_id = Column(Integer(), ForeignKey('RequiredAsset.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='SubjectReference', source_slot='props', mapping_type=None, target_class='Property', target_slot='SubjectReference_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "Property", foreign_keys="[Property.SubjectReference_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='SubjectReference', source_slot='links', mapping_type=None, target_class='Link', target_slot='SubjectReference_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "Link", foreign_keys="[Link.SubjectReference_id]")
    

    def __repr__(self):
        return f"SubjectReference(id={self.id},subject_uuid={self.subject_uuid},type={self.type},title={self.title},remarks={self.remarks},Observation_id={self.Observation_id},MitigatingFactor_id={self.MitigatingFactor_id},RequiredAsset_id={self.RequiredAsset_id},)"



    


class AssessmentSubjectPlaceholder(Base):
    """
    Used when the assessment subjects will be determined as part of one or more other assessment activities.
    """
    __tablename__ = 'AssessmentSubjectPlaceholder'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    uuid = Column(Text(), nullable=False )
    description = Column(Text())
    remarks = Column(Text())
    
    
    # One-To-Many: OneToAnyMapping(source_class='AssessmentSubjectPlaceholder', source_slot='sources', mapping_type=None, target_class='AssessmentSubjectSource', target_slot='AssessmentSubjectPlaceholder_id', join_class=None, uses_join_table=None, multivalued=False)
    sources = relationship( "AssessmentSubjectSource", foreign_keys="[AssessmentSubjectSource.AssessmentSubjectPlaceholder_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='AssessmentSubjectPlaceholder', source_slot='props', mapping_type=None, target_class='Property', target_slot='AssessmentSubjectPlaceholder_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "Property", foreign_keys="[Property.AssessmentSubjectPlaceholder_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='AssessmentSubjectPlaceholder', source_slot='links', mapping_type=None, target_class='Link', target_slot='AssessmentSubjectPlaceholder_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "Link", foreign_keys="[Link.AssessmentSubjectPlaceholder_id]")
    

    def __repr__(self):
        return f"AssessmentSubjectPlaceholder(id={self.id},uuid={self.uuid},description={self.description},remarks={self.remarks},)"



    


class AssessmentSubjectSource(Base):
    """
    Assessment subjects will be identified while conducting the referenced activity.
    """
    __tablename__ = 'AssessmentSubjectSource'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    task_uuid = Column(Text(), nullable=False )
    remarks = Column(Text())
    AssessmentSubjectPlaceholder_id = Column(Integer(), ForeignKey('AssessmentSubjectPlaceholder.id'))
    

    def __repr__(self):
        return f"AssessmentSubjectSource(id={self.id},task_uuid={self.task_uuid},remarks={self.remarks},AssessmentSubjectPlaceholder_id={self.AssessmentSubjectPlaceholder_id},)"



    


class AssessmentAssets(Base):
    """
    Identifies the assets used to perform this assessment.
    """
    __tablename__ = 'AssessmentAssets'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    
    
    # One-To-Many: OneToAnyMapping(source_class='AssessmentAssets', source_slot='components', mapping_type=None, target_class='SystemComponent', target_slot='AssessmentAssets_id', join_class=None, uses_join_table=None, multivalued=False)
    components = relationship( "SystemComponent", foreign_keys="[SystemComponent.AssessmentAssets_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='AssessmentAssets', source_slot='assessment_platforms', mapping_type=None, target_class='AssessmentPlatform', target_slot='AssessmentAssets_id', join_class=None, uses_join_table=None, multivalued=False)
    assessment_platforms = relationship( "AssessmentPlatform", foreign_keys="[AssessmentPlatform.AssessmentAssets_id]")
    

    def __repr__(self):
        return f"AssessmentAssets(id={self.id},)"



    


class AssessmentPlatform(Base):
    """
    Used to represent the toolset used to perform aspects of the assessment.
    """
    __tablename__ = 'AssessmentPlatform'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    uuid = Column(Text(), nullable=False )
    title = Column(Text())
    remarks = Column(Text())
    AssessmentAssets_id = Column(Integer(), ForeignKey('AssessmentAssets.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='AssessmentPlatform', source_slot='uses_components', mapping_type=None, target_class='UsesComponent', target_slot='AssessmentPlatform_id', join_class=None, uses_join_table=None, multivalued=False)
    uses_components = relationship( "UsesComponent", foreign_keys="[UsesComponent.AssessmentPlatform_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='AssessmentPlatform', source_slot='props', mapping_type=None, target_class='Property', target_slot='AssessmentPlatform_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "Property", foreign_keys="[Property.AssessmentPlatform_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='AssessmentPlatform', source_slot='links', mapping_type=None, target_class='Link', target_slot='AssessmentPlatform_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "Link", foreign_keys="[Link.AssessmentPlatform_id]")
    

    def __repr__(self):
        return f"AssessmentPlatform(id={self.id},uuid={self.uuid},title={self.title},remarks={self.remarks},AssessmentAssets_id={self.AssessmentAssets_id},)"



    


class UsesComponent(Base):
    """
    The set of components that are used by the assessment platform.
    """
    __tablename__ = 'UsesComponent'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    component_uuid = Column(Text(), nullable=False )
    remarks = Column(Text())
    AssessmentPlatform_id = Column(Integer(), ForeignKey('AssessmentPlatform.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='UsesComponent', source_slot='responsible_parties', mapping_type=None, target_class='ResponsibleParty', target_slot='UsesComponent_id', join_class=None, uses_join_table=None, multivalued=False)
    responsible_parties = relationship( "ResponsibleParty", foreign_keys="[ResponsibleParty.UsesComponent_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='UsesComponent', source_slot='props', mapping_type=None, target_class='Property', target_slot='UsesComponent_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "Property", foreign_keys="[Property.UsesComponent_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='UsesComponent', source_slot='links', mapping_type=None, target_class='Link', target_slot='UsesComponent_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "Link", foreign_keys="[Link.UsesComponent_id]")
    

    def __repr__(self):
        return f"UsesComponent(id={self.id},component_uuid={self.component_uuid},remarks={self.remarks},AssessmentPlatform_id={self.AssessmentPlatform_id},)"



    


class LocalObjective(Base):
    """
    A local definition of a control objective for this assessment. Uses catalog syntax for control objective and assessment actions.
    """
    __tablename__ = 'LocalObjective'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    control_id = Column(Text(), nullable=False )
    description = Column(Text())
    remarks = Column(Text())
    LocalDefinitions_id = Column(Integer(), ForeignKey('LocalDefinitions.id'))
    AssessmentResultsLocalDefinitions_id = Column(Integer(), ForeignKey('AssessmentResultsLocalDefinitions.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='LocalObjective', source_slot='parts', mapping_type=None, target_class='ControlPart', target_slot='LocalObjective_id', join_class=None, uses_join_table=None, multivalued=False)
    parts = relationship( "ControlPart", foreign_keys="[ControlPart.LocalObjective_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='LocalObjective', source_slot='props', mapping_type=None, target_class='Property', target_slot='LocalObjective_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "Property", foreign_keys="[Property.LocalObjective_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='LocalObjective', source_slot='links', mapping_type=None, target_class='Link', target_slot='LocalObjective_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "Link", foreign_keys="[Link.LocalObjective_id]")
    

    def __repr__(self):
        return f"LocalObjective(id={self.id},control_id={self.control_id},description={self.description},remarks={self.remarks},LocalDefinitions_id={self.LocalDefinitions_id},AssessmentResultsLocalDefinitions_id={self.AssessmentResultsLocalDefinitions_id},)"



    


class AssessmentMethod(Base):
    """
    A local definition of a control objective.
    """
    __tablename__ = 'AssessmentMethod'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    uuid = Column(Text(), nullable=False )
    description = Column(Text())
    remarks = Column(Text())
    part_id = Column(Integer(), ForeignKey('AssessmentPart.id'), nullable=False )
    part = relationship("AssessmentPart", uselist=False, foreign_keys=[part_id])
    
    
    # One-To-Many: OneToAnyMapping(source_class='AssessmentMethod', source_slot='props', mapping_type=None, target_class='Property', target_slot='AssessmentMethod_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "Property", foreign_keys="[Property.AssessmentMethod_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='AssessmentMethod', source_slot='links', mapping_type=None, target_class='Link', target_slot='AssessmentMethod_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "Link", foreign_keys="[Link.AssessmentMethod_id]")
    

    def __repr__(self):
        return f"AssessmentMethod(id={self.id},uuid={self.uuid},description={self.description},remarks={self.remarks},part_id={self.part_id},)"



    


class Activity(Base):
    """
    Identifies an assessment or related process that can be performed. In the assessment plan, this is an intended activity.
    """
    __tablename__ = 'Activity'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    uuid = Column(Text(), nullable=False )
    title = Column(Text())
    description = Column(Text(), nullable=False )
    remarks = Column(Text())
    LocalDefinitions_id = Column(Integer(), ForeignKey('LocalDefinitions.id'))
    AssessmentResultsLocalDefinitions_id = Column(Integer(), ForeignKey('AssessmentResultsLocalDefinitions.id'))
    related_controls_id = Column(Integer(), ForeignKey('ReviewedControls.id'))
    related_controls = relationship("ReviewedControls", uselist=False, foreign_keys=[related_controls_id])
    
    
    # One-To-Many: OneToAnyMapping(source_class='Activity', source_slot='steps', mapping_type=None, target_class='Step', target_slot='Activity_id', join_class=None, uses_join_table=None, multivalued=False)
    steps = relationship( "Step", foreign_keys="[Step.Activity_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Activity', source_slot='responsible_roles', mapping_type=None, target_class='ResponsibleRole', target_slot='Activity_id', join_class=None, uses_join_table=None, multivalued=False)
    responsible_roles = relationship( "ResponsibleRole", foreign_keys="[ResponsibleRole.Activity_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Activity', source_slot='props', mapping_type=None, target_class='Property', target_slot='Activity_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "Property", foreign_keys="[Property.Activity_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Activity', source_slot='links', mapping_type=None, target_class='Link', target_slot='Activity_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "Link", foreign_keys="[Link.Activity_id]")
    

    def __repr__(self):
        return f"Activity(id={self.id},uuid={self.uuid},title={self.title},description={self.description},remarks={self.remarks},LocalDefinitions_id={self.LocalDefinitions_id},AssessmentResultsLocalDefinitions_id={self.AssessmentResultsLocalDefinitions_id},related_controls_id={self.related_controls_id},)"



    


class Step(Base):
    """
    Identifies an individual step in a series of steps related to an activity, such as an assessment test or examination procedure.
    """
    __tablename__ = 'Step'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    uuid = Column(Text(), nullable=False )
    title = Column(Text())
    description = Column(Text(), nullable=False )
    remarks = Column(Text())
    Activity_id = Column(Integer(), ForeignKey('Activity.id'))
    reviewed_controls_id = Column(Integer(), ForeignKey('ReviewedControls.id'))
    reviewed_controls = relationship("ReviewedControls", uselist=False, foreign_keys=[reviewed_controls_id])
    
    
    # One-To-Many: OneToAnyMapping(source_class='Step', source_slot='responsible_roles', mapping_type=None, target_class='ResponsibleRole', target_slot='Step_id', join_class=None, uses_join_table=None, multivalued=False)
    responsible_roles = relationship( "ResponsibleRole", foreign_keys="[ResponsibleRole.Step_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Step', source_slot='props', mapping_type=None, target_class='Property', target_slot='Step_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "Property", foreign_keys="[Property.Step_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Step', source_slot='links', mapping_type=None, target_class='Link', target_slot='Step_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "Link", foreign_keys="[Link.Step_id]")
    

    def __repr__(self):
        return f"Step(id={self.id},uuid={self.uuid},title={self.title},description={self.description},remarks={self.remarks},Activity_id={self.Activity_id},reviewed_controls_id={self.reviewed_controls_id},)"



    


class Task(Base):
    """
    Represents a scheduled event or milestone, which may be associated with a series of assessment actions.
    """
    __tablename__ = 'Task'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    uuid = Column(Text(), nullable=False )
    type = Column(Text(), nullable=False )
    title = Column(Text(), nullable=False )
    description = Column(Text())
    remarks = Column(Text())
    AssessmentPlan_id = Column(Integer(), ForeignKey('AssessmentPlan.id'))
    Task_id = Column(Integer(), ForeignKey('Task.id'))
    Response_id = Column(Integer(), ForeignKey('Response.id'))
    ResultLocalDefinitions_id = Column(Integer(), ForeignKey('ResultLocalDefinitions.id'))
    timing_id = Column(Integer(), ForeignKey('EventTiming.id'))
    timing = relationship("EventTiming", uselist=False, foreign_keys=[timing_id])
    
    
    # One-To-Many: OneToAnyMapping(source_class='Task', source_slot='dependencies', mapping_type=None, target_class='TaskDependency', target_slot='Task_id', join_class=None, uses_join_table=None, multivalued=False)
    dependencies = relationship( "TaskDependency", foreign_keys="[TaskDependency.Task_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Task', source_slot='associated_activities', mapping_type=None, target_class='AssociatedActivity', target_slot='Task_id', join_class=None, uses_join_table=None, multivalued=False)
    associated_activities = relationship( "AssociatedActivity", foreign_keys="[AssociatedActivity.Task_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Task', source_slot='tasks', mapping_type=None, target_class='Task', target_slot='Task_id', join_class=None, uses_join_table=None, multivalued=False)
    tasks = relationship( "Task", foreign_keys="[Task.Task_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Task', source_slot='subjects', mapping_type=None, target_class='AssessmentSubject', target_slot='Task_id', join_class=None, uses_join_table=None, multivalued=False)
    subjects = relationship( "AssessmentSubject", foreign_keys="[AssessmentSubject.Task_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Task', source_slot='responsible_roles', mapping_type=None, target_class='ResponsibleRole', target_slot='Task_id', join_class=None, uses_join_table=None, multivalued=False)
    responsible_roles = relationship( "ResponsibleRole", foreign_keys="[ResponsibleRole.Task_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Task', source_slot='props', mapping_type=None, target_class='Property', target_slot='Task_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "Property", foreign_keys="[Property.Task_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Task', source_slot='links', mapping_type=None, target_class='Link', target_slot='Task_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "Link", foreign_keys="[Link.Task_id]")
    

    def __repr__(self):
        return f"Task(id={self.id},uuid={self.uuid},type={self.type},title={self.title},description={self.description},remarks={self.remarks},AssessmentPlan_id={self.AssessmentPlan_id},Task_id={self.Task_id},Response_id={self.Response_id},ResultLocalDefinitions_id={self.ResultLocalDefinitions_id},timing_id={self.timing_id},)"



    


class EventTiming(Base):
    """
    The timing under which the task is intended to occur.
    """
    __tablename__ = 'EventTiming'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    on_date_id = Column(Integer(), ForeignKey('OnDateCondition.id'))
    on_date = relationship("OnDateCondition", uselist=False, foreign_keys=[on_date_id])
    within_date_range_id = Column(Integer(), ForeignKey('WithinDateRange.id'))
    within_date_range = relationship("WithinDateRange", uselist=False, foreign_keys=[within_date_range_id])
    at_frequency_id = Column(Integer(), ForeignKey('AtFrequency.id'))
    at_frequency = relationship("AtFrequency", uselist=False, foreign_keys=[at_frequency_id])
    

    def __repr__(self):
        return f"EventTiming(id={self.id},on_date_id={self.on_date_id},within_date_range_id={self.within_date_range_id},at_frequency_id={self.at_frequency_id},)"



    


class OnDateCondition(Base):
    """
    The task is intended to occur on the specified date.
    """
    __tablename__ = 'OnDateCondition'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    date = Column(Text(), nullable=False )
    remarks = Column(Text())
    

    def __repr__(self):
        return f"OnDateCondition(id={self.id},date={self.date},remarks={self.remarks},)"



    


class WithinDateRange(Base):
    """
    The task is intended to occur within the specified date range.
    """
    __tablename__ = 'WithinDateRange'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    start = Column(Text(), nullable=False )
    end = Column(Text(), nullable=False )
    remarks = Column(Text())
    

    def __repr__(self):
        return f"WithinDateRange(id={self.id},start={self.start},end={self.end},remarks={self.remarks},)"



    


class AtFrequency(Base):
    """
    The task is intended to occur at the specified frequency.
    """
    __tablename__ = 'AtFrequency'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    period = Column(Integer(), nullable=False )
    unit = Column(Enum('seconds', 'minutes', 'hours', 'days', 'months', 'years', name='TimingUnitEnum'), nullable=False )
    remarks = Column(Text())
    

    def __repr__(self):
        return f"AtFrequency(id={self.id},period={self.period},unit={self.unit},remarks={self.remarks},)"



    


class TaskDependency(Base):
    """
    Used to indicate that a task is dependent on another task.
    """
    __tablename__ = 'TaskDependency'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    task_uuid = Column(Text(), nullable=False )
    remarks = Column(Text())
    Task_id = Column(Integer(), ForeignKey('Task.id'))
    

    def __repr__(self):
        return f"TaskDependency(id={self.id},task_uuid={self.task_uuid},remarks={self.remarks},Task_id={self.Task_id},)"



    


class AssociatedActivity(Base):
    """
    Identifies an individual activity to be performed as part of a task.
    """
    __tablename__ = 'AssociatedActivity'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    activity_uuid = Column(Text(), nullable=False )
    remarks = Column(Text())
    Task_id = Column(Integer(), ForeignKey('Task.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='AssociatedActivity', source_slot='subjects', mapping_type=None, target_class='AssessmentSubject', target_slot='AssociatedActivity_id', join_class=None, uses_join_table=None, multivalued=False)
    subjects = relationship( "AssessmentSubject", foreign_keys="[AssessmentSubject.AssociatedActivity_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='AssociatedActivity', source_slot='responsible_roles', mapping_type=None, target_class='ResponsibleRole', target_slot='AssociatedActivity_id', join_class=None, uses_join_table=None, multivalued=False)
    responsible_roles = relationship( "ResponsibleRole", foreign_keys="[ResponsibleRole.AssociatedActivity_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='AssociatedActivity', source_slot='props', mapping_type=None, target_class='Property', target_slot='AssociatedActivity_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "Property", foreign_keys="[Property.AssociatedActivity_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='AssociatedActivity', source_slot='links', mapping_type=None, target_class='Link', target_slot='AssociatedActivity_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "Link", foreign_keys="[Link.AssociatedActivity_id]")
    

    def __repr__(self):
        return f"AssociatedActivity(id={self.id},activity_uuid={self.activity_uuid},remarks={self.remarks},Task_id={self.Task_id},)"



    


class AssessmentPart(Base):
    """
    A partition of an assessment plan or results or a child of another part.
    """
    __tablename__ = 'AssessmentPart'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    uuid = Column(Text())
    name = Column(Text(), nullable=False )
    ns = Column(Text())
    _class = Column(Text())
    title = Column(Text())
    prose = Column(Text())
    AssessmentPart_id = Column(Integer(), ForeignKey('AssessmentPart.id'))
    Attestation_id = Column(Integer(), ForeignKey('Attestation.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='AssessmentPart', source_slot='parts', mapping_type=None, target_class='AssessmentPart', target_slot='AssessmentPart_id', join_class=None, uses_join_table=None, multivalued=False)
    parts = relationship( "AssessmentPart", foreign_keys="[AssessmentPart.AssessmentPart_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='AssessmentPart', source_slot='props', mapping_type=None, target_class='Property', target_slot='AssessmentPart_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "Property", foreign_keys="[Property.AssessmentPart_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='AssessmentPart', source_slot='links', mapping_type=None, target_class='Link', target_slot='AssessmentPart_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "Link", foreign_keys="[Link.AssessmentPart_id]")
    

    def __repr__(self):
        return f"AssessmentPart(id={self.id},uuid={self.uuid},name={self.name},ns={self.ns},_class={self._class},title={self.title},prose={self.prose},AssessmentPart_id={self.AssessmentPart_id},Attestation_id={self.Attestation_id},)"



    


class ControlPart(Base):
    """
    An annotated, markup-based textual element of a control's or catalog group's definition, or a child of another part.
    """
    __tablename__ = 'ControlPart'

    uid = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    id = Column(Text())
    name = Column(Text(), nullable=False )
    ns = Column(Text())
    _class = Column(Text())
    title = Column(Text())
    prose = Column(Text())
    LocalObjective_id = Column(Integer(), ForeignKey('LocalObjective.id'))
    ControlPart_uid = Column(Integer(), ForeignKey('ControlPart.uid'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='ControlPart', source_slot='parts', mapping_type=None, target_class='ControlPart', target_slot='ControlPart_uid', join_class=None, uses_join_table=None, multivalued=False)
    parts = relationship( "ControlPart", foreign_keys="[ControlPart.ControlPart_uid]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='ControlPart', source_slot='props', mapping_type=None, target_class='Property', target_slot='ControlPart_uid', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "Property", foreign_keys="[Property.ControlPart_uid]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='ControlPart', source_slot='links', mapping_type=None, target_class='Link', target_slot='ControlPart_uid', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "Link", foreign_keys="[Link.ControlPart_uid]")
    

    def __repr__(self):
        return f"ControlPart(uid={self.uid},id={self.id},name={self.name},ns={self.ns},_class={self._class},title={self.title},prose={self.prose},LocalObjective_id={self.LocalObjective_id},ControlPart_uid={self.ControlPart_uid},)"



    


class SetParameter(Base):
    """
    Identifies the parameter that will be set by the enclosed value.
    """
    __tablename__ = 'SetParameter'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    param_id = Column(Text(), nullable=False )
    remarks = Column(Text())
    SspControlImplementation_id = Column(Integer(), ForeignKey('SspControlImplementation.id'))
    SspImplementedRequirement_id = Column(Integer(), ForeignKey('SspImplementedRequirement.id'))
    ByComponent_id = Column(Integer(), ForeignKey('ByComponent.id'))
    ControlImplementationSet_id = Column(Integer(), ForeignKey('ControlImplementationSet.id'))
    ImplementedRequirement_id = Column(Integer(), ForeignKey('ImplementedRequirement.id'))
    
    
    values_rel = relationship( "SetParameterValues" )
    values = association_proxy("values_rel", "values",
                                  creator=lambda x_: SetParameterValues(values=x_))
    

    def __repr__(self):
        return f"SetParameter(id={self.id},param_id={self.param_id},remarks={self.remarks},SspControlImplementation_id={self.SspControlImplementation_id},SspImplementedRequirement_id={self.SspImplementedRequirement_id},ByComponent_id={self.ByComponent_id},ControlImplementationSet_id={self.ControlImplementationSet_id},ImplementedRequirement_id={self.ImplementedRequirement_id},)"



    


class SystemComponent(Base):
    """
    A defined component that can be part of an implemented system.
    """
    __tablename__ = 'SystemComponent'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    uuid = Column(Text(), nullable=False )
    type = Column(Text(), nullable=False )
    title = Column(Text(), nullable=False )
    description = Column(Text(), nullable=False )
    purpose = Column(Text())
    remarks = Column(Text())
    LocalDefinitions_id = Column(Integer(), ForeignKey('LocalDefinitions.id'))
    AssessmentAssets_id = Column(Integer(), ForeignKey('AssessmentAssets.id'))
    ResultLocalDefinitions_id = Column(Integer(), ForeignKey('ResultLocalDefinitions.id'))
    PoamLocalDefinitions_id = Column(Integer(), ForeignKey('PoamLocalDefinitions.id'))
    status_id = Column(Integer(), ForeignKey('ComponentStatus.id'), nullable=False )
    status = relationship("ComponentStatus", uselist=False, foreign_keys=[status_id])
    
    
    # One-To-Many: OneToAnyMapping(source_class='SystemComponent', source_slot='protocols', mapping_type=None, target_class='Protocol', target_slot='SystemComponent_id', join_class=None, uses_join_table=None, multivalued=False)
    protocols = relationship( "Protocol", foreign_keys="[Protocol.SystemComponent_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='SystemComponent', source_slot='responsible_roles', mapping_type=None, target_class='ImplementationResponsibleRole', target_slot='SystemComponent_id', join_class=None, uses_join_table=None, multivalued=False)
    responsible_roles = relationship( "ImplementationResponsibleRole", foreign_keys="[ImplementationResponsibleRole.SystemComponent_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='SystemComponent', source_slot='props', mapping_type=None, target_class='ImplementationCommonProperty', target_slot='SystemComponent_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "ImplementationCommonProperty", foreign_keys="[ImplementationCommonProperty.SystemComponent_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='SystemComponent', source_slot='links', mapping_type=None, target_class='ImplementationCommonLink', target_slot='SystemComponent_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "ImplementationCommonLink", foreign_keys="[ImplementationCommonLink.SystemComponent_id]")
    

    def __repr__(self):
        return f"SystemComponent(id={self.id},uuid={self.uuid},type={self.type},title={self.title},description={self.description},purpose={self.purpose},remarks={self.remarks},LocalDefinitions_id={self.LocalDefinitions_id},AssessmentAssets_id={self.AssessmentAssets_id},ResultLocalDefinitions_id={self.ResultLocalDefinitions_id},PoamLocalDefinitions_id={self.PoamLocalDefinitions_id},status_id={self.status_id},)"



    


class ComponentStatus(Base):
    """
    Describes the operational status of the system component.
    """
    __tablename__ = 'ComponentStatus'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    state = Column(Enum('under-development', 'operational', 'disposition', 'other', name='ComponentStateEnum'), nullable=False )
    remarks = Column(Text())
    

    def __repr__(self):
        return f"ComponentStatus(id={self.id},state={self.state},remarks={self.remarks},)"



    


class Protocol(Base):
    """
    Information about the protocol used to provide a service.
    """
    __tablename__ = 'Protocol'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    uuid = Column(Text())
    name = Column(Text())
    title = Column(Text())
    SystemComponent_id = Column(Integer(), ForeignKey('SystemComponent.id'))
    SspSystemComponent_id = Column(Integer(), ForeignKey('SspSystemComponent.id'))
    DefinedComponent_id = Column(Integer(), ForeignKey('DefinedComponent.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='Protocol', source_slot='port_ranges', mapping_type=None, target_class='PortRange', target_slot='Protocol_id', join_class=None, uses_join_table=None, multivalued=False)
    port_ranges = relationship( "PortRange", foreign_keys="[PortRange.Protocol_id]")
    

    def __repr__(self):
        return f"Protocol(id={self.id},uuid={self.uuid},name={self.name},title={self.title},SystemComponent_id={self.SystemComponent_id},SspSystemComponent_id={self.SspSystemComponent_id},DefinedComponent_id={self.DefinedComponent_id},)"



    


class PortRange(Base):
    """
    Where applicable, the transport layer protocol port range.
    """
    __tablename__ = 'PortRange'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    start = Column(Integer())
    end = Column(Integer())
    transport = Column(Enum('TCP', 'UDP', name='TransportEnum'))
    remarks = Column(Text())
    Protocol_id = Column(Integer(), ForeignKey('Protocol.id'))
    

    def __repr__(self):
        return f"PortRange(id={self.id},start={self.start},end={self.end},transport={self.transport},remarks={self.remarks},Protocol_id={self.Protocol_id},)"



    


class ImplementationStatus(Base):
    """
    Indicates the degree to which a given control is implemented.
    """
    __tablename__ = 'ImplementationStatus'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    state = Column(Text(), nullable=False )
    remarks = Column(Text())
    

    def __repr__(self):
        return f"ImplementationStatus(id={self.id},state={self.state},remarks={self.remarks},)"



    


class SystemUser(Base):
    """
    A type of user that interacts with the system based on an associated role.
    """
    __tablename__ = 'SystemUser'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    uuid = Column(Text(), nullable=False )
    title = Column(Text())
    short_name = Column(Text())
    description = Column(Text())
    remarks = Column(Text())
    LocalDefinitions_id = Column(Integer(), ForeignKey('LocalDefinitions.id'))
    SystemImplementation_id = Column(Integer(), ForeignKey('SystemImplementation.id'))
    ResultLocalDefinitions_id = Column(Integer(), ForeignKey('ResultLocalDefinitions.id'))
    
    
    role_ids_rel = relationship( "SystemUserRoleIds" )
    role_ids = association_proxy("role_ids_rel", "role_ids",
                                  creator=lambda x_: SystemUserRoleIds(role_ids=x_))
    
    
    # One-To-Many: OneToAnyMapping(source_class='SystemUser', source_slot='authorized_privileges', mapping_type=None, target_class='AuthorizedPrivilege', target_slot='SystemUser_id', join_class=None, uses_join_table=None, multivalued=False)
    authorized_privileges = relationship( "AuthorizedPrivilege", foreign_keys="[AuthorizedPrivilege.SystemUser_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='SystemUser', source_slot='props', mapping_type=None, target_class='ImplementationCommonProperty', target_slot='SystemUser_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "ImplementationCommonProperty", foreign_keys="[ImplementationCommonProperty.SystemUser_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='SystemUser', source_slot='links', mapping_type=None, target_class='ImplementationCommonLink', target_slot='SystemUser_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "ImplementationCommonLink", foreign_keys="[ImplementationCommonLink.SystemUser_id]")
    

    def __repr__(self):
        return f"SystemUser(id={self.id},uuid={self.uuid},title={self.title},short_name={self.short_name},description={self.description},remarks={self.remarks},LocalDefinitions_id={self.LocalDefinitions_id},SystemImplementation_id={self.SystemImplementation_id},ResultLocalDefinitions_id={self.ResultLocalDefinitions_id},)"



    


class AuthorizedPrivilege(Base):
    """
    Identifies a specific system privilege held by the user, along with an associated description and/or rationale for the privilege.
    """
    __tablename__ = 'AuthorizedPrivilege'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    title = Column(Text(), nullable=False )
    description = Column(Text())
    SystemUser_id = Column(Integer(), ForeignKey('SystemUser.id'))
    
    
    functions_performed_rel = relationship( "AuthorizedPrivilegeFunctionsPerformed" )
    functions_performed = association_proxy("functions_performed_rel", "functions_performed",
                                  creator=lambda x_: AuthorizedPrivilegeFunctionsPerformed(functions_performed=x_))
    

    def __repr__(self):
        return f"AuthorizedPrivilege(id={self.id},title={self.title},description={self.description},SystemUser_id={self.SystemUser_id},)"



    


class InventoryItem(Base):
    """
    A single managed inventory item within the system.
    """
    __tablename__ = 'InventoryItem'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    uuid = Column(Text(), nullable=False )
    description = Column(Text(), nullable=False )
    remarks = Column(Text())
    LocalDefinitions_id = Column(Integer(), ForeignKey('LocalDefinitions.id'))
    ResultLocalDefinitions_id = Column(Integer(), ForeignKey('ResultLocalDefinitions.id'))
    PoamLocalDefinitions_id = Column(Integer(), ForeignKey('PoamLocalDefinitions.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='InventoryItem', source_slot='implemented_components', mapping_type=None, target_class='ImplementedComponent', target_slot='InventoryItem_id', join_class=None, uses_join_table=None, multivalued=False)
    implemented_components = relationship( "ImplementedComponent", foreign_keys="[ImplementedComponent.InventoryItem_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='InventoryItem', source_slot='responsible_parties', mapping_type=None, target_class='ImplementationResponsibleParty', target_slot='InventoryItem_id', join_class=None, uses_join_table=None, multivalued=False)
    responsible_parties = relationship( "ImplementationResponsibleParty", foreign_keys="[ImplementationResponsibleParty.InventoryItem_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='InventoryItem', source_slot='props', mapping_type=None, target_class='ImplementationCommonProperty', target_slot='InventoryItem_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "ImplementationCommonProperty", foreign_keys="[ImplementationCommonProperty.InventoryItem_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='InventoryItem', source_slot='links', mapping_type=None, target_class='ImplementationCommonLink', target_slot='InventoryItem_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "ImplementationCommonLink", foreign_keys="[ImplementationCommonLink.InventoryItem_id]")
    

    def __repr__(self):
        return f"InventoryItem(id={self.id},uuid={self.uuid},description={self.description},remarks={self.remarks},LocalDefinitions_id={self.LocalDefinitions_id},ResultLocalDefinitions_id={self.ResultLocalDefinitions_id},PoamLocalDefinitions_id={self.PoamLocalDefinitions_id},)"



    


class ImplementedComponent(Base):
    """
    The set of components that are implemented in a given system inventory item.
    """
    __tablename__ = 'ImplementedComponent'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    component_uuid = Column(Text(), nullable=False )
    remarks = Column(Text())
    InventoryItem_id = Column(Integer(), ForeignKey('InventoryItem.id'))
    SspInventoryItem_id = Column(Integer(), ForeignKey('SspInventoryItem.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='ImplementedComponent', source_slot='responsible_parties', mapping_type=None, target_class='ImplementationResponsibleParty', target_slot='ImplementedComponent_id', join_class=None, uses_join_table=None, multivalued=False)
    responsible_parties = relationship( "ImplementationResponsibleParty", foreign_keys="[ImplementationResponsibleParty.ImplementedComponent_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='ImplementedComponent', source_slot='props', mapping_type=None, target_class='ImplementationCommonProperty', target_slot='ImplementedComponent_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "ImplementationCommonProperty", foreign_keys="[ImplementationCommonProperty.ImplementedComponent_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='ImplementedComponent', source_slot='links', mapping_type=None, target_class='ImplementationCommonLink', target_slot='ImplementedComponent_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "ImplementationCommonLink", foreign_keys="[ImplementationCommonLink.ImplementedComponent_id]")
    

    def __repr__(self):
        return f"ImplementedComponent(id={self.id},component_uuid={self.component_uuid},remarks={self.remarks},InventoryItem_id={self.InventoryItem_id},SspInventoryItem_id={self.SspInventoryItem_id},)"



    


class SystemId(Base):
    """
    A human-oriented, globally unique identifier for a system.
    """
    __tablename__ = 'SystemId'

    uid = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    id = Column(Text(), nullable=False )
    identifier_type = Column(Text())
    SystemCharacteristics_id = Column(Integer(), ForeignKey('SystemCharacteristics.id'))
    

    def __repr__(self):
        return f"SystemId(uid={self.uid},id={self.id},identifier_type={self.identifier_type},SystemCharacteristics_id={self.SystemCharacteristics_id},)"



    


class Origin(Base):
    """
    Identifies the source of the finding, such as a tool, interviewed person, or activity.
    """
    __tablename__ = 'Origin'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    Observation_id = Column(Integer(), ForeignKey('Observation.id'))
    Finding_id = Column(Integer(), ForeignKey('Finding.id'))
    Risk_id = Column(Integer(), ForeignKey('Risk.id'))
    Response_id = Column(Integer(), ForeignKey('Response.id'))
    PoamItem_id = Column(Integer(), ForeignKey('PoamItem.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='Origin', source_slot='actors', mapping_type=None, target_class='OriginActor', target_slot='Origin_id', join_class=None, uses_join_table=None, multivalued=False)
    actors = relationship( "OriginActor", foreign_keys="[OriginActor.Origin_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Origin', source_slot='related_tasks', mapping_type=None, target_class='RelatedTask', target_slot='Origin_id', join_class=None, uses_join_table=None, multivalued=False)
    related_tasks = relationship( "RelatedTask", foreign_keys="[RelatedTask.Origin_id]")
    

    def __repr__(self):
        return f"Origin(id={self.id},Observation_id={self.Observation_id},Finding_id={self.Finding_id},Risk_id={self.Risk_id},Response_id={self.Response_id},PoamItem_id={self.PoamItem_id},)"



    


class OriginActor(Base):
    """
    The actor that produces an observation, a finding, or a risk.
    """
    __tablename__ = 'OriginActor'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    type = Column(Enum('tool', 'assessment-platform', 'party', name='OriginActorTypeEnum'), nullable=False )
    actor_uuid = Column(Text(), nullable=False )
    role_id = Column(Text())
    Origin_id = Column(Integer(), ForeignKey('Origin.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='OriginActor', source_slot='props', mapping_type=None, target_class='Property', target_slot='OriginActor_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "Property", foreign_keys="[Property.OriginActor_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='OriginActor', source_slot='links', mapping_type=None, target_class='Link', target_slot='OriginActor_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "Link", foreign_keys="[Link.OriginActor_id]")
    

    def __repr__(self):
        return f"OriginActor(id={self.id},type={self.type},actor_uuid={self.actor_uuid},role_id={self.role_id},Origin_id={self.Origin_id},)"



    


class RelatedTask(Base):
    """
    Identifies an individual task for which the containing object is a consequence of.
    """
    __tablename__ = 'RelatedTask'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    task_uuid = Column(Text(), nullable=False )
    remarks = Column(Text())
    Origin_id = Column(Integer(), ForeignKey('Origin.id'))
    RiskResponseReference_id = Column(Integer(), ForeignKey('RiskResponseReference.id'))
    AssessmentLogEntry_id = Column(Integer(), ForeignKey('AssessmentLogEntry.id'))
    identified_subject_id = Column(Integer(), ForeignKey('IdentifiedSubject.id'))
    identified_subject = relationship("IdentifiedSubject", uselist=False, foreign_keys=[identified_subject_id])
    
    
    # One-To-Many: OneToAnyMapping(source_class='RelatedTask', source_slot='subjects', mapping_type=None, target_class='AssessmentSubject', target_slot='RelatedTask_id', join_class=None, uses_join_table=None, multivalued=False)
    subjects = relationship( "AssessmentSubject", foreign_keys="[AssessmentSubject.RelatedTask_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='RelatedTask', source_slot='responsible_parties', mapping_type=None, target_class='ResponsibleParty', target_slot='RelatedTask_id', join_class=None, uses_join_table=None, multivalued=False)
    responsible_parties = relationship( "ResponsibleParty", foreign_keys="[ResponsibleParty.RelatedTask_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='RelatedTask', source_slot='props', mapping_type=None, target_class='Property', target_slot='RelatedTask_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "Property", foreign_keys="[Property.RelatedTask_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='RelatedTask', source_slot='links', mapping_type=None, target_class='Link', target_slot='RelatedTask_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "Link", foreign_keys="[Link.RelatedTask_id]")
    

    def __repr__(self):
        return f"RelatedTask(id={self.id},task_uuid={self.task_uuid},remarks={self.remarks},Origin_id={self.Origin_id},RiskResponseReference_id={self.RiskResponseReference_id},AssessmentLogEntry_id={self.AssessmentLogEntry_id},identified_subject_id={self.identified_subject_id},)"



    


class IdentifiedSubject(Base):
    """
    Used to detail assessment subjects that were identified by this task.
    """
    __tablename__ = 'IdentifiedSubject'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    subject_placeholder_uuid = Column(Text(), nullable=False )
    
    
    # One-To-Many: OneToAnyMapping(source_class='IdentifiedSubject', source_slot='subjects', mapping_type=None, target_class='AssessmentSubject', target_slot='IdentifiedSubject_id', join_class=None, uses_join_table=None, multivalued=False)
    subjects = relationship( "AssessmentSubject", foreign_keys="[AssessmentSubject.IdentifiedSubject_id]")
    

    def __repr__(self):
        return f"IdentifiedSubject(id={self.id},subject_placeholder_uuid={self.subject_placeholder_uuid},)"



    


class Observation(Base):
    """
    Describes an individual observation.
    """
    __tablename__ = 'Observation'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    uuid = Column(Text(), nullable=False )
    title = Column(Text())
    description = Column(Text(), nullable=False )
    collected = Column(Text(), nullable=False )
    expires = Column(Text())
    remarks = Column(Text())
    Result_id = Column(Integer(), ForeignKey('Result.id'))
    PlanOfActionAndMilestones_id = Column(Integer(), ForeignKey('PlanOfActionAndMilestones.id'))
    
    
    methods_rel = relationship( "ObservationMethods" )
    methods = association_proxy("methods_rel", "methods",
                                  creator=lambda x_: ObservationMethods(methods=x_))
    
    
    types_rel = relationship( "ObservationTypes" )
    types = association_proxy("types_rel", "types",
                                  creator=lambda x_: ObservationTypes(types=x_))
    
    
    # One-To-Many: OneToAnyMapping(source_class='Observation', source_slot='origins', mapping_type=None, target_class='Origin', target_slot='Observation_id', join_class=None, uses_join_table=None, multivalued=False)
    origins = relationship( "Origin", foreign_keys="[Origin.Observation_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Observation', source_slot='subjects', mapping_type=None, target_class='SubjectReference', target_slot='Observation_id', join_class=None, uses_join_table=None, multivalued=False)
    subjects = relationship( "SubjectReference", foreign_keys="[SubjectReference.Observation_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Observation', source_slot='relevant_evidence', mapping_type=None, target_class='RelevantEvidence', target_slot='Observation_id', join_class=None, uses_join_table=None, multivalued=False)
    relevant_evidence = relationship( "RelevantEvidence", foreign_keys="[RelevantEvidence.Observation_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Observation', source_slot='props', mapping_type=None, target_class='Property', target_slot='Observation_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "Property", foreign_keys="[Property.Observation_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Observation', source_slot='links', mapping_type=None, target_class='Link', target_slot='Observation_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "Link", foreign_keys="[Link.Observation_id]")
    

    def __repr__(self):
        return f"Observation(id={self.id},uuid={self.uuid},title={self.title},description={self.description},collected={self.collected},expires={self.expires},remarks={self.remarks},Result_id={self.Result_id},PlanOfActionAndMilestones_id={self.PlanOfActionAndMilestones_id},)"



    


class RelevantEvidence(Base):
    """
    Links this observation to relevant evidence.
    """
    __tablename__ = 'RelevantEvidence'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    href = Column(Text())
    description = Column(Text(), nullable=False )
    remarks = Column(Text())
    Observation_id = Column(Integer(), ForeignKey('Observation.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='RelevantEvidence', source_slot='props', mapping_type=None, target_class='Property', target_slot='RelevantEvidence_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "Property", foreign_keys="[Property.RelevantEvidence_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='RelevantEvidence', source_slot='links', mapping_type=None, target_class='Link', target_slot='RelevantEvidence_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "Link", foreign_keys="[Link.RelevantEvidence_id]")
    

    def __repr__(self):
        return f"RelevantEvidence(id={self.id},href={self.href},description={self.description},remarks={self.remarks},Observation_id={self.Observation_id},)"



    


class Finding(Base):
    """
    Describes an individual finding.
    """
    __tablename__ = 'Finding'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    uuid = Column(Text(), nullable=False )
    title = Column(Text(), nullable=False )
    description = Column(Text(), nullable=False )
    implementation_statement_uuid = Column(Text())
    remarks = Column(Text())
    Result_id = Column(Integer(), ForeignKey('Result.id'))
    PlanOfActionAndMilestones_id = Column(Integer(), ForeignKey('PlanOfActionAndMilestones.id'))
    target_id = Column(Integer(), ForeignKey('FindingTarget.id'), nullable=False )
    target = relationship("FindingTarget", uselist=False, foreign_keys=[target_id])
    
    
    # One-To-Many: OneToAnyMapping(source_class='Finding', source_slot='origins', mapping_type=None, target_class='Origin', target_slot='Finding_id', join_class=None, uses_join_table=None, multivalued=False)
    origins = relationship( "Origin", foreign_keys="[Origin.Finding_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Finding', source_slot='related_observations', mapping_type=None, target_class='RelatedObservation', target_slot='Finding_id', join_class=None, uses_join_table=None, multivalued=False)
    related_observations = relationship( "RelatedObservation", foreign_keys="[RelatedObservation.Finding_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Finding', source_slot='related_risks', mapping_type=None, target_class='AssociatedRisk', target_slot='Finding_id', join_class=None, uses_join_table=None, multivalued=False)
    related_risks = relationship( "AssociatedRisk", foreign_keys="[AssociatedRisk.Finding_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Finding', source_slot='props', mapping_type=None, target_class='Property', target_slot='Finding_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "Property", foreign_keys="[Property.Finding_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Finding', source_slot='links', mapping_type=None, target_class='Link', target_slot='Finding_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "Link", foreign_keys="[Link.Finding_id]")
    

    def __repr__(self):
        return f"Finding(id={self.id},uuid={self.uuid},title={self.title},description={self.description},implementation_statement_uuid={self.implementation_statement_uuid},remarks={self.remarks},Result_id={self.Result_id},PlanOfActionAndMilestones_id={self.PlanOfActionAndMilestones_id},target_id={self.target_id},)"



    


class FindingTarget(Base):
    """
    Captures an assessor's conclusions regarding the degree to which an objective is satisfied.
    """
    __tablename__ = 'FindingTarget'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    type = Column(Enum('statement-id', 'objective-id', name='FindingTargetTypeEnum'), nullable=False )
    target_id = Column(Text(), nullable=False )
    title = Column(Text())
    description = Column(Text())
    remarks = Column(Text())
    implementation_status_id = Column(Integer(), ForeignKey('ImplementationStatus.id'))
    implementation_status = relationship("ImplementationStatus", uselist=False, foreign_keys=[implementation_status_id])
    status_id = Column(Integer(), ForeignKey('ObjectiveStatus.id'), nullable=False )
    status = relationship("ObjectiveStatus", uselist=False, foreign_keys=[status_id])
    
    
    # One-To-Many: OneToAnyMapping(source_class='FindingTarget', source_slot='props', mapping_type=None, target_class='Property', target_slot='FindingTarget_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "Property", foreign_keys="[Property.FindingTarget_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='FindingTarget', source_slot='links', mapping_type=None, target_class='Link', target_slot='FindingTarget_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "Link", foreign_keys="[Link.FindingTarget_id]")
    

    def __repr__(self):
        return f"FindingTarget(id={self.id},type={self.type},target_id={self.target_id},title={self.title},description={self.description},remarks={self.remarks},implementation_status_id={self.implementation_status_id},status_id={self.status_id},)"



    


class ObjectiveStatus(Base):
    """
    A determination of if the objective is satisfied or not within a given system.
    """
    __tablename__ = 'ObjectiveStatus'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    state = Column(Enum('satisfied', 'not-satisfied', name='ObjectiveStatusStateEnum'), nullable=False )
    reason = Column(Text())
    remarks = Column(Text())
    

    def __repr__(self):
        return f"ObjectiveStatus(id={self.id},state={self.state},reason={self.reason},remarks={self.remarks},)"



    


class RelatedObservation(Base):
    """
    Relates the identified element to a set of referenced observations.
    """
    __tablename__ = 'RelatedObservation'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    observation_uuid = Column(Text(), nullable=False )
    remarks = Column(Text())
    Finding_id = Column(Integer(), ForeignKey('Finding.id'))
    Risk_id = Column(Integer(), ForeignKey('Risk.id'))
    PoamItem_id = Column(Integer(), ForeignKey('PoamItem.id'))
    

    def __repr__(self):
        return f"RelatedObservation(id={self.id},observation_uuid={self.observation_uuid},remarks={self.remarks},Finding_id={self.Finding_id},Risk_id={self.Risk_id},PoamItem_id={self.PoamItem_id},)"



    


class AssociatedRisk(Base):
    """
    Relates the finding to a set of referenced risks.
    """
    __tablename__ = 'AssociatedRisk'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    risk_uuid = Column(Text(), nullable=False )
    remarks = Column(Text())
    Finding_id = Column(Integer(), ForeignKey('Finding.id'))
    PoamItem_id = Column(Integer(), ForeignKey('PoamItem.id'))
    

    def __repr__(self):
        return f"AssociatedRisk(id={self.id},risk_uuid={self.risk_uuid},remarks={self.remarks},Finding_id={self.Finding_id},PoamItem_id={self.PoamItem_id},)"



    


class Risk(Base):
    """
    An identified risk.
    """
    __tablename__ = 'Risk'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    uuid = Column(Text(), nullable=False )
    title = Column(Text(), nullable=False )
    description = Column(Text(), nullable=False )
    statement = Column(Text(), nullable=False )
    deadline = Column(Text())
    status = Column(Text(), nullable=False )
    Result_id = Column(Integer(), ForeignKey('Result.id'))
    PlanOfActionAndMilestones_id = Column(Integer(), ForeignKey('PlanOfActionAndMilestones.id'))
    risk_log_id = Column(Integer(), ForeignKey('RiskLog.id'))
    risk_log = relationship("RiskLog", uselist=False, foreign_keys=[risk_log_id])
    
    
    # One-To-Many: OneToAnyMapping(source_class='Risk', source_slot='origins', mapping_type=None, target_class='Origin', target_slot='Risk_id', join_class=None, uses_join_table=None, multivalued=False)
    origins = relationship( "Origin", foreign_keys="[Origin.Risk_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Risk', source_slot='threat_ids', mapping_type=None, target_class='ThreatId', target_slot='Risk_id', join_class=None, uses_join_table=None, multivalued=False)
    threat_ids = relationship( "ThreatId", foreign_keys="[ThreatId.Risk_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Risk', source_slot='characterizations', mapping_type=None, target_class='Characterization', target_slot='Risk_id', join_class=None, uses_join_table=None, multivalued=False)
    characterizations = relationship( "Characterization", foreign_keys="[Characterization.Risk_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Risk', source_slot='mitigating_factors', mapping_type=None, target_class='MitigatingFactor', target_slot='Risk_id', join_class=None, uses_join_table=None, multivalued=False)
    mitigating_factors = relationship( "MitigatingFactor", foreign_keys="[MitigatingFactor.Risk_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Risk', source_slot='remediations', mapping_type=None, target_class='Response', target_slot='Risk_id', join_class=None, uses_join_table=None, multivalued=False)
    remediations = relationship( "Response", foreign_keys="[Response.Risk_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Risk', source_slot='related_observations', mapping_type=None, target_class='RelatedObservation', target_slot='Risk_id', join_class=None, uses_join_table=None, multivalued=False)
    related_observations = relationship( "RelatedObservation", foreign_keys="[RelatedObservation.Risk_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Risk', source_slot='props', mapping_type=None, target_class='Property', target_slot='Risk_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "Property", foreign_keys="[Property.Risk_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Risk', source_slot='links', mapping_type=None, target_class='Link', target_slot='Risk_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "Link", foreign_keys="[Link.Risk_id]")
    

    def __repr__(self):
        return f"Risk(id={self.id},uuid={self.uuid},title={self.title},description={self.description},statement={self.statement},deadline={self.deadline},status={self.status},Result_id={self.Result_id},PlanOfActionAndMilestones_id={self.PlanOfActionAndMilestones_id},risk_log_id={self.risk_log_id},)"



    


class ThreatId(Base):
    """
    A pointer, by ID, to an externally-defined threat.
    """
    __tablename__ = 'ThreatId'

    uid = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    href = Column(Text())
    system = Column(Text(), nullable=False )
    id = Column(Text(), nullable=False )
    Risk_id = Column(Integer(), ForeignKey('Risk.id'))
    

    def __repr__(self):
        return f"ThreatId(uid={self.uid},href={self.href},system={self.system},id={self.id},Risk_id={self.Risk_id},)"



    


class Characterization(Base):
    """
    A collection of descriptive data about the containing object from a specific origin.
    """
    __tablename__ = 'Characterization'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    Risk_id = Column(Integer(), ForeignKey('Risk.id'))
    origin_id = Column(Integer(), ForeignKey('Origin.id'), nullable=False )
    origin = relationship("Origin", uselist=False, foreign_keys=[origin_id])
    
    
    # One-To-Many: OneToAnyMapping(source_class='Characterization', source_slot='facets', mapping_type=None, target_class='Facet', target_slot='Characterization_id', join_class=None, uses_join_table=None, multivalued=False)
    facets = relationship( "Facet", foreign_keys="[Facet.Characterization_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Characterization', source_slot='props', mapping_type=None, target_class='Property', target_slot='Characterization_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "Property", foreign_keys="[Property.Characterization_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Characterization', source_slot='links', mapping_type=None, target_class='Link', target_slot='Characterization_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "Link", foreign_keys="[Link.Characterization_id]")
    

    def __repr__(self):
        return f"Characterization(id={self.id},Risk_id={self.Risk_id},origin_id={self.origin_id},)"



    


class Facet(Base):
    """
    An individual characteristic that is part of a larger set produced by the same actor.
    """
    __tablename__ = 'Facet'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    name = Column(Text(), nullable=False )
    value = Column(Text(), nullable=False )
    system = Column(Text(), nullable=False )
    remarks = Column(Text())
    Characterization_id = Column(Integer(), ForeignKey('Characterization.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='Facet', source_slot='props', mapping_type=None, target_class='Property', target_slot='Facet_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "Property", foreign_keys="[Property.Facet_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Facet', source_slot='links', mapping_type=None, target_class='Link', target_slot='Facet_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "Link", foreign_keys="[Link.Facet_id]")
    

    def __repr__(self):
        return f"Facet(id={self.id},name={self.name},value={self.value},system={self.system},remarks={self.remarks},Characterization_id={self.Characterization_id},)"



    


class MitigatingFactor(Base):
    """
    Describes an existing mitigating factor that may affect the overall determination of the risk.
    """
    __tablename__ = 'MitigatingFactor'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    uuid = Column(Text(), nullable=False )
    description = Column(Text(), nullable=False )
    implementation_uuid = Column(Text())
    Risk_id = Column(Integer(), ForeignKey('Risk.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='MitigatingFactor', source_slot='subjects', mapping_type=None, target_class='SubjectReference', target_slot='MitigatingFactor_id', join_class=None, uses_join_table=None, multivalued=False)
    subjects = relationship( "SubjectReference", foreign_keys="[SubjectReference.MitigatingFactor_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='MitigatingFactor', source_slot='props', mapping_type=None, target_class='Property', target_slot='MitigatingFactor_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "Property", foreign_keys="[Property.MitigatingFactor_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='MitigatingFactor', source_slot='links', mapping_type=None, target_class='Link', target_slot='MitigatingFactor_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "Link", foreign_keys="[Link.MitigatingFactor_id]")
    

    def __repr__(self):
        return f"MitigatingFactor(id={self.id},uuid={self.uuid},description={self.description},implementation_uuid={self.implementation_uuid},Risk_id={self.Risk_id},)"



    


class Response(Base):
    """
    Describes either recommended or an actual plan for addressing the risk.
    """
    __tablename__ = 'Response'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    uuid = Column(Text(), nullable=False )
    title = Column(Text(), nullable=False )
    description = Column(Text(), nullable=False )
    lifecycle = Column(Text(), nullable=False )
    remarks = Column(Text())
    Risk_id = Column(Integer(), ForeignKey('Risk.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='Response', source_slot='origins', mapping_type=None, target_class='Origin', target_slot='Response_id', join_class=None, uses_join_table=None, multivalued=False)
    origins = relationship( "Origin", foreign_keys="[Origin.Response_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Response', source_slot='required_assets', mapping_type=None, target_class='RequiredAsset', target_slot='Response_id', join_class=None, uses_join_table=None, multivalued=False)
    required_assets = relationship( "RequiredAsset", foreign_keys="[RequiredAsset.Response_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Response', source_slot='tasks', mapping_type=None, target_class='Task', target_slot='Response_id', join_class=None, uses_join_table=None, multivalued=False)
    tasks = relationship( "Task", foreign_keys="[Task.Response_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Response', source_slot='props', mapping_type=None, target_class='Property', target_slot='Response_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "Property", foreign_keys="[Property.Response_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Response', source_slot='links', mapping_type=None, target_class='Link', target_slot='Response_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "Link", foreign_keys="[Link.Response_id]")
    

    def __repr__(self):
        return f"Response(id={self.id},uuid={self.uuid},title={self.title},description={self.description},lifecycle={self.lifecycle},remarks={self.remarks},Risk_id={self.Risk_id},)"



    


class RequiredAsset(Base):
    """
    Identifies an asset required to achieve remediation.
    """
    __tablename__ = 'RequiredAsset'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    uuid = Column(Text(), nullable=False )
    title = Column(Text())
    description = Column(Text(), nullable=False )
    remarks = Column(Text())
    Response_id = Column(Integer(), ForeignKey('Response.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='RequiredAsset', source_slot='subjects', mapping_type=None, target_class='SubjectReference', target_slot='RequiredAsset_id', join_class=None, uses_join_table=None, multivalued=False)
    subjects = relationship( "SubjectReference", foreign_keys="[SubjectReference.RequiredAsset_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='RequiredAsset', source_slot='props', mapping_type=None, target_class='Property', target_slot='RequiredAsset_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "Property", foreign_keys="[Property.RequiredAsset_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='RequiredAsset', source_slot='links', mapping_type=None, target_class='Link', target_slot='RequiredAsset_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "Link", foreign_keys="[Link.RequiredAsset_id]")
    

    def __repr__(self):
        return f"RequiredAsset(id={self.id},uuid={self.uuid},title={self.title},description={self.description},remarks={self.remarks},Response_id={self.Response_id},)"



    


class RiskLog(Base):
    """
    A log of all risk-related tasks taken.
    """
    __tablename__ = 'RiskLog'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    
    
    # One-To-Many: OneToAnyMapping(source_class='RiskLog', source_slot='entries', mapping_type=None, target_class='RiskLogEntry', target_slot='RiskLog_id', join_class=None, uses_join_table=None, multivalued=False)
    entries = relationship( "RiskLogEntry", foreign_keys="[RiskLogEntry.RiskLog_id]")
    

    def __repr__(self):
        return f"RiskLog(id={self.id},)"



    


class RiskLogEntry(Base):
    """
    Identifies an individual risk response that occurred as part of managing an identified risk.
    """
    __tablename__ = 'RiskLogEntry'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    uuid = Column(Text(), nullable=False )
    title = Column(Text())
    description = Column(Text())
    start = Column(Text(), nullable=False )
    end = Column(Text())
    status_change = Column(Text())
    remarks = Column(Text())
    RiskLog_id = Column(Integer(), ForeignKey('RiskLog.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='RiskLogEntry', source_slot='logged_by', mapping_type=None, target_class='LoggedBy', target_slot='RiskLogEntry_id', join_class=None, uses_join_table=None, multivalued=False)
    logged_by = relationship( "LoggedBy", foreign_keys="[LoggedBy.RiskLogEntry_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='RiskLogEntry', source_slot='related_responses', mapping_type=None, target_class='RiskResponseReference', target_slot='RiskLogEntry_id', join_class=None, uses_join_table=None, multivalued=False)
    related_responses = relationship( "RiskResponseReference", foreign_keys="[RiskResponseReference.RiskLogEntry_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='RiskLogEntry', source_slot='props', mapping_type=None, target_class='Property', target_slot='RiskLogEntry_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "Property", foreign_keys="[Property.RiskLogEntry_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='RiskLogEntry', source_slot='links', mapping_type=None, target_class='Link', target_slot='RiskLogEntry_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "Link", foreign_keys="[Link.RiskLogEntry_id]")
    

    def __repr__(self):
        return f"RiskLogEntry(id={self.id},uuid={self.uuid},title={self.title},description={self.description},start={self.start},end={self.end},status_change={self.status_change},remarks={self.remarks},RiskLog_id={self.RiskLog_id},)"



    


class LoggedBy(Base):
    """
    Used to indicate who created a log entry in what role.
    """
    __tablename__ = 'LoggedBy'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    party_uuid = Column(Text(), nullable=False )
    role_id = Column(Text())
    remarks = Column(Text())
    RiskLogEntry_id = Column(Integer(), ForeignKey('RiskLogEntry.id'))
    AssessmentLogEntry_id = Column(Integer(), ForeignKey('AssessmentLogEntry.id'))
    

    def __repr__(self):
        return f"LoggedBy(id={self.id},party_uuid={self.party_uuid},role_id={self.role_id},remarks={self.remarks},RiskLogEntry_id={self.RiskLogEntry_id},AssessmentLogEntry_id={self.AssessmentLogEntry_id},)"



    


class RiskResponseReference(Base):
    """
    Identifies an individual risk response that this log entry is for.
    """
    __tablename__ = 'RiskResponseReference'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    response_uuid = Column(Text(), nullable=False )
    remarks = Column(Text())
    RiskLogEntry_id = Column(Integer(), ForeignKey('RiskLogEntry.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='RiskResponseReference', source_slot='related_tasks', mapping_type=None, target_class='RelatedTask', target_slot='RiskResponseReference_id', join_class=None, uses_join_table=None, multivalued=False)
    related_tasks = relationship( "RelatedTask", foreign_keys="[RelatedTask.RiskResponseReference_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='RiskResponseReference', source_slot='props', mapping_type=None, target_class='Property', target_slot='RiskResponseReference_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "Property", foreign_keys="[Property.RiskResponseReference_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='RiskResponseReference', source_slot='links', mapping_type=None, target_class='Link', target_slot='RiskResponseReference_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "Link", foreign_keys="[Link.RiskResponseReference_id]")
    

    def __repr__(self):
        return f"RiskResponseReference(id={self.id},response_uuid={self.response_uuid},remarks={self.remarks},RiskLogEntry_id={self.RiskLogEntry_id},)"



    


class SystemSecurityPlan(Base):
    """
    A system security plan, such as those described in NIST SP 800-18.
    """
    __tablename__ = 'SystemSecurityPlan'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    uuid = Column(Text(), nullable=False )
    metadata_id = Column(Integer(), ForeignKey('Metadata.id'), nullable=False )
    metadata = relationship("Metadata", uselist=False, foreign_keys=[metadata_id])
    import_profile_id = Column(Integer(), ForeignKey('ImportProfile.id'), nullable=False )
    import_profile = relationship("ImportProfile", uselist=False, foreign_keys=[import_profile_id])
    system_characteristics_id = Column(Integer(), ForeignKey('SystemCharacteristics.id'), nullable=False )
    system_characteristics = relationship("SystemCharacteristics", uselist=False, foreign_keys=[system_characteristics_id])
    system_implementation_id = Column(Integer(), ForeignKey('SystemImplementation.id'), nullable=False )
    system_implementation = relationship("SystemImplementation", uselist=False, foreign_keys=[system_implementation_id])
    control_implementation_id = Column(Integer(), ForeignKey('SspControlImplementation.id'), nullable=False )
    control_implementation = relationship("SspControlImplementation", uselist=False, foreign_keys=[control_implementation_id])
    back_matter_id = Column(Integer(), ForeignKey('BackMatter.id'))
    back_matter = relationship("BackMatter", uselist=False, foreign_keys=[back_matter_id])
    

    def __repr__(self):
        return f"SystemSecurityPlan(id={self.id},uuid={self.uuid},metadata_id={self.metadata_id},import_profile_id={self.import_profile_id},system_characteristics_id={self.system_characteristics_id},system_implementation_id={self.system_implementation_id},control_implementation_id={self.control_implementation_id},back_matter_id={self.back_matter_id},)"



    


class ImportProfile(Base):
    """
    Used to import the OSCAL profile representing the system's control baseline.
    """
    __tablename__ = 'ImportProfile'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    href = Column(Text(), nullable=False )
    remarks = Column(Text())
    

    def __repr__(self):
        return f"ImportProfile(id={self.id},href={self.href},remarks={self.remarks},)"



    


class SystemCharacteristics(Base):
    """
    Contains the characteristics of the system, such as its name, purpose, and security impact level.
    """
    __tablename__ = 'SystemCharacteristics'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    system_name = Column(Text(), nullable=False )
    system_name_short = Column(Text())
    description = Column(Text(), nullable=False )
    date_authorized = Column(Text())
    security_sensitivity_level = Column(Text())
    remarks = Column(Text())
    system_information_id = Column(Integer(), ForeignKey('SystemInformation.id'), nullable=False )
    system_information = relationship("SystemInformation", uselist=False, foreign_keys=[system_information_id])
    security_impact_level_id = Column(Integer(), ForeignKey('SecurityImpactLevel.id'))
    security_impact_level = relationship("SecurityImpactLevel", uselist=False, foreign_keys=[security_impact_level_id])
    system_status_id = Column(Integer(), ForeignKey('SystemStatus.id'), nullable=False )
    system_status = relationship("SystemStatus", uselist=False, foreign_keys=[system_status_id])
    authorization_boundary_id = Column(Integer(), ForeignKey('AuthorizationBoundary.id'), nullable=False )
    authorization_boundary = relationship("AuthorizationBoundary", uselist=False, foreign_keys=[authorization_boundary_id])
    network_architecture_id = Column(Integer(), ForeignKey('NetworkArchitecture.id'))
    network_architecture = relationship("NetworkArchitecture", uselist=False, foreign_keys=[network_architecture_id])
    data_flow_id = Column(Integer(), ForeignKey('DataFlow.id'))
    data_flow = relationship("DataFlow", uselist=False, foreign_keys=[data_flow_id])
    
    
    # One-To-Many: OneToAnyMapping(source_class='SystemCharacteristics', source_slot='system_ids', mapping_type=None, target_class='SystemId', target_slot='SystemCharacteristics_id', join_class=None, uses_join_table=None, multivalued=False)
    system_ids = relationship( "SystemId", foreign_keys="[SystemId.SystemCharacteristics_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='SystemCharacteristics', source_slot='responsible_parties', mapping_type=None, target_class='SspSystemCharacteristicsResponsibleParty', target_slot='SystemCharacteristics_id', join_class=None, uses_join_table=None, multivalued=False)
    responsible_parties = relationship( "SspSystemCharacteristicsResponsibleParty", foreign_keys="[SspSystemCharacteristicsResponsibleParty.SystemCharacteristics_id]")
    

    def __repr__(self):
        return f"SystemCharacteristics(id={self.id},system_name={self.system_name},system_name_short={self.system_name_short},description={self.description},date_authorized={self.date_authorized},security_sensitivity_level={self.security_sensitivity_level},remarks={self.remarks},system_information_id={self.system_information_id},security_impact_level_id={self.security_impact_level_id},system_status_id={self.system_status_id},authorization_boundary_id={self.authorization_boundary_id},network_architecture_id={self.network_architecture_id},data_flow_id={self.data_flow_id},)"



    


class SystemInformation(Base):
    """
    Contains details about all information types that are stored, processed, or transmitted by the system, such as privacy information.
    """
    __tablename__ = 'SystemInformation'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    
    
    # One-To-Many: OneToAnyMapping(source_class='SystemInformation', source_slot='props', mapping_type=None, target_class='SspSystemInformationProp', target_slot='SystemInformation_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "SspSystemInformationProp", foreign_keys="[SspSystemInformationProp.SystemInformation_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='SystemInformation', source_slot='links', mapping_type=None, target_class='SspSystemInformationLink', target_slot='SystemInformation_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "SspSystemInformationLink", foreign_keys="[SspSystemInformationLink.SystemInformation_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='SystemInformation', source_slot='information_types', mapping_type=None, target_class='InformationType', target_slot='SystemInformation_id', join_class=None, uses_join_table=None, multivalued=False)
    information_types = relationship( "InformationType", foreign_keys="[InformationType.SystemInformation_id]")
    

    def __repr__(self):
        return f"SystemInformation(id={self.id},)"



    


class InformationType(Base):
    """
    Contains details about one information type that is stored, processed, or transmitted by the system, such as privacy information, and its impact level.
    """
    __tablename__ = 'InformationType'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    uuid = Column(Text())
    title = Column(Text(), nullable=False )
    description = Column(Text(), nullable=False )
    SystemInformation_id = Column(Integer(), ForeignKey('SystemInformation.id'))
    confidentiality_impact_id = Column(Integer(), ForeignKey('ImpactLevel.id'))
    confidentiality_impact = relationship("ImpactLevel", uselist=False, foreign_keys=[confidentiality_impact_id])
    integrity_impact_id = Column(Integer(), ForeignKey('ImpactLevel.id'))
    integrity_impact = relationship("ImpactLevel", uselist=False, foreign_keys=[integrity_impact_id])
    availability_impact_id = Column(Integer(), ForeignKey('ImpactLevel.id'))
    availability_impact = relationship("ImpactLevel", uselist=False, foreign_keys=[availability_impact_id])
    
    
    # One-To-Many: OneToAnyMapping(source_class='InformationType', source_slot='categorizations', mapping_type=None, target_class='InformationTypeCategorization', target_slot='InformationType_id', join_class=None, uses_join_table=None, multivalued=False)
    categorizations = relationship( "InformationTypeCategorization", foreign_keys="[InformationTypeCategorization.InformationType_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='InformationType', source_slot='props', mapping_type=None, target_class='Property', target_slot='InformationType_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "Property", foreign_keys="[Property.InformationType_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='InformationType', source_slot='links', mapping_type=None, target_class='Link', target_slot='InformationType_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "Link", foreign_keys="[Link.InformationType_id]")
    

    def __repr__(self):
        return f"InformationType(id={self.id},uuid={self.uuid},title={self.title},description={self.description},SystemInformation_id={self.SystemInformation_id},confidentiality_impact_id={self.confidentiality_impact_id},integrity_impact_id={self.integrity_impact_id},availability_impact_id={self.availability_impact_id},)"



    


class InformationTypeCategorization(Base):
    """
    A set of information type identifiers qualified by the given identification system used.
    """
    __tablename__ = 'InformationTypeCategorization'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    system = Column(Text(), nullable=False )
    InformationType_id = Column(Integer(), ForeignKey('InformationType.id'))
    
    
    information_type_ids_rel = relationship( "InformationTypeCategorizationInformationTypeIds" )
    information_type_ids = association_proxy("information_type_ids_rel", "information_type_ids",
                                  creator=lambda x_: InformationTypeCategorizationInformationTypeIds(information_type_ids=x_))
    

    def __repr__(self):
        return f"InformationTypeCategorization(id={self.id},system={self.system},InformationType_id={self.InformationType_id},)"



    


class ImpactLevel(Base):
    """
    The expected level of impact resulting from the described information's confidentiality, integrity, or availability affect.
    """
    __tablename__ = 'ImpactLevel'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    base = Column(Text(), nullable=False )
    selected = Column(Text())
    adjustment_justification = Column(Text())
    
    
    # One-To-Many: OneToAnyMapping(source_class='ImpactLevel', source_slot='props', mapping_type=None, target_class='Property', target_slot='ImpactLevel_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "Property", foreign_keys="[Property.ImpactLevel_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='ImpactLevel', source_slot='links', mapping_type=None, target_class='Link', target_slot='ImpactLevel_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "Link", foreign_keys="[Link.ImpactLevel_id]")
    

    def __repr__(self):
        return f"ImpactLevel(id={self.id},base={self.base},selected={self.selected},adjustment_justification={self.adjustment_justification},)"



    


class SecurityImpactLevel(Base):
    """
    The overall level of expected impact resulting from unauthorized disclosure, modification, or loss of access to information.
    """
    __tablename__ = 'SecurityImpactLevel'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    security_objective_confidentiality = Column(Text(), nullable=False )
    security_objective_integrity = Column(Text(), nullable=False )
    security_objective_availability = Column(Text(), nullable=False )
    

    def __repr__(self):
        return f"SecurityImpactLevel(id={self.id},security_objective_confidentiality={self.security_objective_confidentiality},security_objective_integrity={self.security_objective_integrity},security_objective_availability={self.security_objective_availability},)"



    


class SystemStatus(Base):
    """
    Describes the operational status of the system.
    """
    __tablename__ = 'SystemStatus'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    remarks = Column(Text())
    state = Column(Enum('operational', 'under-development', 'under-major-modification', 'disposition', 'other', name='SystemOperatingStatusEnum'), nullable=False )
    

    def __repr__(self):
        return f"SystemStatus(id={self.id},remarks={self.remarks},state={self.state},)"



    


class AuthorizationBoundary(Base):
    """
    A description of this system's authorization boundary, optionally supplemented with diagrams that illustrate the authorization boundary.
    """
    __tablename__ = 'AuthorizationBoundary'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    description = Column(Text(), nullable=False )
    remarks = Column(Text())
    
    
    # One-To-Many: OneToAnyMapping(source_class='AuthorizationBoundary', source_slot='props', mapping_type=None, target_class='Property', target_slot='AuthorizationBoundary_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "Property", foreign_keys="[Property.AuthorizationBoundary_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='AuthorizationBoundary', source_slot='links', mapping_type=None, target_class='Link', target_slot='AuthorizationBoundary_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "Link", foreign_keys="[Link.AuthorizationBoundary_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='AuthorizationBoundary', source_slot='diagrams', mapping_type=None, target_class='Diagram', target_slot='AuthorizationBoundary_id', join_class=None, uses_join_table=None, multivalued=False)
    diagrams = relationship( "Diagram", foreign_keys="[Diagram.AuthorizationBoundary_id]")
    

    def __repr__(self):
        return f"AuthorizationBoundary(id={self.id},description={self.description},remarks={self.remarks},)"



    


class Diagram(Base):
    """
    A graphic that provides a visual representation the system, or some aspect of it.
    """
    __tablename__ = 'Diagram'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    uuid = Column(Text(), nullable=False )
    description = Column(Text())
    caption = Column(Text())
    remarks = Column(Text())
    AuthorizationBoundary_id = Column(Integer(), ForeignKey('AuthorizationBoundary.id'))
    NetworkArchitecture_id = Column(Integer(), ForeignKey('NetworkArchitecture.id'))
    DataFlow_id = Column(Integer(), ForeignKey('DataFlow.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='Diagram', source_slot='props', mapping_type=None, target_class='Property', target_slot='Diagram_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "Property", foreign_keys="[Property.Diagram_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Diagram', source_slot='links', mapping_type=None, target_class='SspDiagramLink', target_slot='Diagram_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "SspDiagramLink", foreign_keys="[SspDiagramLink.Diagram_id]")
    

    def __repr__(self):
        return f"Diagram(id={self.id},uuid={self.uuid},description={self.description},caption={self.caption},remarks={self.remarks},AuthorizationBoundary_id={self.AuthorizationBoundary_id},NetworkArchitecture_id={self.NetworkArchitecture_id},DataFlow_id={self.DataFlow_id},)"



    


class NetworkArchitecture(Base):
    """
    A description of the system's network architecture, optionally supplemented with diagrams that illustrate the network architecture.
    """
    __tablename__ = 'NetworkArchitecture'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    description = Column(Text(), nullable=False )
    remarks = Column(Text())
    
    
    # One-To-Many: OneToAnyMapping(source_class='NetworkArchitecture', source_slot='props', mapping_type=None, target_class='Property', target_slot='NetworkArchitecture_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "Property", foreign_keys="[Property.NetworkArchitecture_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='NetworkArchitecture', source_slot='links', mapping_type=None, target_class='Link', target_slot='NetworkArchitecture_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "Link", foreign_keys="[Link.NetworkArchitecture_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='NetworkArchitecture', source_slot='diagrams', mapping_type=None, target_class='Diagram', target_slot='NetworkArchitecture_id', join_class=None, uses_join_table=None, multivalued=False)
    diagrams = relationship( "Diagram", foreign_keys="[Diagram.NetworkArchitecture_id]")
    

    def __repr__(self):
        return f"NetworkArchitecture(id={self.id},description={self.description},remarks={self.remarks},)"



    


class DataFlow(Base):
    """
    A description of the logical flow of information within the system and across its boundaries, optionally supplemented with diagrams.
    """
    __tablename__ = 'DataFlow'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    description = Column(Text(), nullable=False )
    remarks = Column(Text())
    
    
    # One-To-Many: OneToAnyMapping(source_class='DataFlow', source_slot='props', mapping_type=None, target_class='Property', target_slot='DataFlow_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "Property", foreign_keys="[Property.DataFlow_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='DataFlow', source_slot='links', mapping_type=None, target_class='Link', target_slot='DataFlow_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "Link", foreign_keys="[Link.DataFlow_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='DataFlow', source_slot='diagrams', mapping_type=None, target_class='Diagram', target_slot='DataFlow_id', join_class=None, uses_join_table=None, multivalued=False)
    diagrams = relationship( "Diagram", foreign_keys="[Diagram.DataFlow_id]")
    

    def __repr__(self):
        return f"DataFlow(id={self.id},description={self.description},remarks={self.remarks},)"



    


class SystemImplementation(Base):
    """
    Provides information as to how the system is implemented.
    """
    __tablename__ = 'SystemImplementation'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    remarks = Column(Text())
    
    
    # One-To-Many: OneToAnyMapping(source_class='SystemImplementation', source_slot='props', mapping_type=None, target_class='Property', target_slot='SystemImplementation_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "Property", foreign_keys="[Property.SystemImplementation_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='SystemImplementation', source_slot='links', mapping_type=None, target_class='Link', target_slot='SystemImplementation_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "Link", foreign_keys="[Link.SystemImplementation_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='SystemImplementation', source_slot='leveraged_authorizations', mapping_type=None, target_class='LeveragedAuthorization', target_slot='SystemImplementation_id', join_class=None, uses_join_table=None, multivalued=False)
    leveraged_authorizations = relationship( "LeveragedAuthorization", foreign_keys="[LeveragedAuthorization.SystemImplementation_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='SystemImplementation', source_slot='users', mapping_type=None, target_class='SystemUser', target_slot='SystemImplementation_id', join_class=None, uses_join_table=None, multivalued=False)
    users = relationship( "SystemUser", foreign_keys="[SystemUser.SystemImplementation_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='SystemImplementation', source_slot='components', mapping_type=None, target_class='SspSystemComponent', target_slot='SystemImplementation_id', join_class=None, uses_join_table=None, multivalued=False)
    components = relationship( "SspSystemComponent", foreign_keys="[SspSystemComponent.SystemImplementation_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='SystemImplementation', source_slot='inventory_items', mapping_type=None, target_class='SspInventoryItem', target_slot='SystemImplementation_id', join_class=None, uses_join_table=None, multivalued=False)
    inventory_items = relationship( "SspInventoryItem", foreign_keys="[SspInventoryItem.SystemImplementation_id]")
    

    def __repr__(self):
        return f"SystemImplementation(id={self.id},remarks={self.remarks},)"



    


class LeveragedAuthorization(Base):
    """
    A description of another authorized system from which this system inherits capabilities that satisfy security requirements. Another term for this concept is a common control provider.
    """
    __tablename__ = 'LeveragedAuthorization'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    uuid = Column(Text(), nullable=False )
    title = Column(Text(), nullable=False )
    party_uuid = Column(Text(), nullable=False )
    date_authorized = Column(Text(), nullable=False )
    remarks = Column(Text())
    SystemImplementation_id = Column(Integer(), ForeignKey('SystemImplementation.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='LeveragedAuthorization', source_slot='props', mapping_type=None, target_class='Property', target_slot='LeveragedAuthorization_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "Property", foreign_keys="[Property.LeveragedAuthorization_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='LeveragedAuthorization', source_slot='links', mapping_type=None, target_class='SspLeveragedAuthorizationLink', target_slot='LeveragedAuthorization_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "SspLeveragedAuthorizationLink", foreign_keys="[SspLeveragedAuthorizationLink.LeveragedAuthorization_id]")
    

    def __repr__(self):
        return f"LeveragedAuthorization(id={self.id},uuid={self.uuid},title={self.title},party_uuid={self.party_uuid},date_authorized={self.date_authorized},remarks={self.remarks},SystemImplementation_id={self.SystemImplementation_id},)"



    


class SspControlImplementation(Base):
    """
    Describes how the system satisfies a set of controls.
    """
    __tablename__ = 'SspControlImplementation'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    description = Column(Text(), nullable=False )
    
    
    # One-To-Many: OneToAnyMapping(source_class='SspControlImplementation', source_slot='set_parameters', mapping_type=None, target_class='SetParameter', target_slot='SspControlImplementation_id', join_class=None, uses_join_table=None, multivalued=False)
    set_parameters = relationship( "SetParameter", foreign_keys="[SetParameter.SspControlImplementation_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='SspControlImplementation', source_slot='implemented_requirements', mapping_type=None, target_class='SspImplementedRequirement', target_slot='SspControlImplementation_id', join_class=None, uses_join_table=None, multivalued=False)
    implemented_requirements = relationship( "SspImplementedRequirement", foreign_keys="[SspImplementedRequirement.SspControlImplementation_id]")
    

    def __repr__(self):
        return f"SspControlImplementation(id={self.id},description={self.description},)"



    


class SspImplementedRequirement(Base):
    """
    Describes how the system satisfies an individual control.
    """
    __tablename__ = 'SspImplementedRequirement'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    uuid = Column(Text(), nullable=False )
    control_id = Column(Text(), nullable=False )
    remarks = Column(Text())
    SspControlImplementation_id = Column(Integer(), ForeignKey('SspControlImplementation.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='SspImplementedRequirement', source_slot='props', mapping_type=None, target_class='SspControlOriginationProp', target_slot='SspImplementedRequirement_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "SspControlOriginationProp", foreign_keys="[SspControlOriginationProp.SspImplementedRequirement_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='SspImplementedRequirement', source_slot='links', mapping_type=None, target_class='Link', target_slot='SspImplementedRequirement_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "Link", foreign_keys="[Link.SspImplementedRequirement_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='SspImplementedRequirement', source_slot='set_parameters', mapping_type=None, target_class='SetParameter', target_slot='SspImplementedRequirement_id', join_class=None, uses_join_table=None, multivalued=False)
    set_parameters = relationship( "SetParameter", foreign_keys="[SetParameter.SspImplementedRequirement_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='SspImplementedRequirement', source_slot='responsible_roles', mapping_type=None, target_class='SspImplementedRequirementResponsibleRole', target_slot='SspImplementedRequirement_id', join_class=None, uses_join_table=None, multivalued=False)
    responsible_roles = relationship( "SspImplementedRequirementResponsibleRole", foreign_keys="[SspImplementedRequirementResponsibleRole.SspImplementedRequirement_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='SspImplementedRequirement', source_slot='statements', mapping_type=None, target_class='SspStatement', target_slot='SspImplementedRequirement_id', join_class=None, uses_join_table=None, multivalued=False)
    statements = relationship( "SspStatement", foreign_keys="[SspStatement.SspImplementedRequirement_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='SspImplementedRequirement', source_slot='by_components', mapping_type=None, target_class='ByComponent', target_slot='SspImplementedRequirement_id', join_class=None, uses_join_table=None, multivalued=False)
    by_components = relationship( "ByComponent", foreign_keys="[ByComponent.SspImplementedRequirement_id]")
    

    def __repr__(self):
        return f"SspImplementedRequirement(id={self.id},uuid={self.uuid},control_id={self.control_id},remarks={self.remarks},SspControlImplementation_id={self.SspControlImplementation_id},)"



    


class SspStatement(Base):
    """
    Identifies which statements within a control are addressed.
    """
    __tablename__ = 'SspStatement'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    statement_id = Column(Text(), nullable=False )
    uuid = Column(Text(), nullable=False )
    remarks = Column(Text())
    SspImplementedRequirement_id = Column(Integer(), ForeignKey('SspImplementedRequirement.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='SspStatement', source_slot='props', mapping_type=None, target_class='SspControlOriginationProp', target_slot='SspStatement_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "SspControlOriginationProp", foreign_keys="[SspControlOriginationProp.SspStatement_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='SspStatement', source_slot='links', mapping_type=None, target_class='Link', target_slot='SspStatement_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "Link", foreign_keys="[Link.SspStatement_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='SspStatement', source_slot='responsible_roles', mapping_type=None, target_class='SspImplementedRequirementResponsibleRole', target_slot='SspStatement_id', join_class=None, uses_join_table=None, multivalued=False)
    responsible_roles = relationship( "SspImplementedRequirementResponsibleRole", foreign_keys="[SspImplementedRequirementResponsibleRole.SspStatement_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='SspStatement', source_slot='by_components', mapping_type=None, target_class='ByComponent', target_slot='SspStatement_id', join_class=None, uses_join_table=None, multivalued=False)
    by_components = relationship( "ByComponent", foreign_keys="[ByComponent.SspStatement_id]")
    

    def __repr__(self):
        return f"SspStatement(id={self.id},statement_id={self.statement_id},uuid={self.uuid},remarks={self.remarks},SspImplementedRequirement_id={self.SspImplementedRequirement_id},)"



    


class ByComponent(Base):
    """
    Defines how the referenced component implements a set of controls.
    """
    __tablename__ = 'ByComponent'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    component_uuid = Column(Text(), nullable=False )
    uuid = Column(Text(), nullable=False )
    description = Column(Text(), nullable=False )
    remarks = Column(Text())
    SspImplementedRequirement_id = Column(Integer(), ForeignKey('SspImplementedRequirement.id'))
    SspStatement_id = Column(Integer(), ForeignKey('SspStatement.id'))
    implementation_status_id = Column(Integer(), ForeignKey('ImplementationStatus.id'))
    implementation_status = relationship("ImplementationStatus", uselist=False, foreign_keys=[implementation_status_id])
    export_id = Column(Integer(), ForeignKey('Export.id'))
    export = relationship("Export", uselist=False, foreign_keys=[export_id])
    
    
    # One-To-Many: OneToAnyMapping(source_class='ByComponent', source_slot='props', mapping_type=None, target_class='SspControlOriginationProp', target_slot='ByComponent_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "SspControlOriginationProp", foreign_keys="[SspControlOriginationProp.ByComponent_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='ByComponent', source_slot='links', mapping_type=None, target_class='SspByComponentLink', target_slot='ByComponent_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "SspByComponentLink", foreign_keys="[SspByComponentLink.ByComponent_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='ByComponent', source_slot='set_parameters', mapping_type=None, target_class='SetParameter', target_slot='ByComponent_id', join_class=None, uses_join_table=None, multivalued=False)
    set_parameters = relationship( "SetParameter", foreign_keys="[SetParameter.ByComponent_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='ByComponent', source_slot='inherited', mapping_type=None, target_class='InheritedControlImplementation', target_slot='ByComponent_id', join_class=None, uses_join_table=None, multivalued=False)
    inherited = relationship( "InheritedControlImplementation", foreign_keys="[InheritedControlImplementation.ByComponent_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='ByComponent', source_slot='satisfied', mapping_type=None, target_class='SatisfiedControlImplementation', target_slot='ByComponent_id', join_class=None, uses_join_table=None, multivalued=False)
    satisfied = relationship( "SatisfiedControlImplementation", foreign_keys="[SatisfiedControlImplementation.ByComponent_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='ByComponent', source_slot='responsible_roles', mapping_type=None, target_class='SspByComponentResponsibleRole', target_slot='ByComponent_id', join_class=None, uses_join_table=None, multivalued=False)
    responsible_roles = relationship( "SspByComponentResponsibleRole", foreign_keys="[SspByComponentResponsibleRole.ByComponent_id]")
    

    def __repr__(self):
        return f"ByComponent(id={self.id},component_uuid={self.component_uuid},uuid={self.uuid},description={self.description},remarks={self.remarks},SspImplementedRequirement_id={self.SspImplementedRequirement_id},SspStatement_id={self.SspStatement_id},implementation_status_id={self.implementation_status_id},export_id={self.export_id},)"



    


class Export(Base):
    """
    Defines a set of control implementations that are provided as reference implementations for use by organizations implementing the leveraged system.
    """
    __tablename__ = 'Export'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    description = Column(Text())
    
    
    # One-To-Many: OneToAnyMapping(source_class='Export', source_slot='props', mapping_type=None, target_class='Property', target_slot='Export_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "Property", foreign_keys="[Property.Export_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Export', source_slot='links', mapping_type=None, target_class='Link', target_slot='Export_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "Link", foreign_keys="[Link.Export_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Export', source_slot='provided', mapping_type=None, target_class='ProvidedControlImplementation', target_slot='Export_id', join_class=None, uses_join_table=None, multivalued=False)
    provided = relationship( "ProvidedControlImplementation", foreign_keys="[ProvidedControlImplementation.Export_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Export', source_slot='responsibilities', mapping_type=None, target_class='ControlResponsibility', target_slot='Export_id', join_class=None, uses_join_table=None, multivalued=False)
    responsibilities = relationship( "ControlResponsibility", foreign_keys="[ControlResponsibility.Export_id]")
    

    def __repr__(self):
        return f"Export(id={self.id},description={self.description},)"



    


class ProvidedControlImplementation(Base):
    """
    Describes a capability which may be inherited by a leveraging system.
    """
    __tablename__ = 'ProvidedControlImplementation'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    uuid = Column(Text(), nullable=False )
    description = Column(Text(), nullable=False )
    remarks = Column(Text())
    Export_id = Column(Integer(), ForeignKey('Export.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='ProvidedControlImplementation', source_slot='props', mapping_type=None, target_class='Property', target_slot='ProvidedControlImplementation_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "Property", foreign_keys="[Property.ProvidedControlImplementation_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='ProvidedControlImplementation', source_slot='links', mapping_type=None, target_class='Link', target_slot='ProvidedControlImplementation_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "Link", foreign_keys="[Link.ProvidedControlImplementation_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='ProvidedControlImplementation', source_slot='responsible_roles', mapping_type=None, target_class='SspByComponentResponsibleRole', target_slot='ProvidedControlImplementation_id', join_class=None, uses_join_table=None, multivalued=False)
    responsible_roles = relationship( "SspByComponentResponsibleRole", foreign_keys="[SspByComponentResponsibleRole.ProvidedControlImplementation_id]")
    

    def __repr__(self):
        return f"ProvidedControlImplementation(id={self.id},uuid={self.uuid},description={self.description},remarks={self.remarks},Export_id={self.Export_id},)"



    


class ControlResponsibility(Base):
    """
    Describes a control implementation responsibility imposed on a leveraging system.
    """
    __tablename__ = 'ControlResponsibility'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    uuid = Column(Text(), nullable=False )
    provided_uuid = Column(Text())
    description = Column(Text(), nullable=False )
    remarks = Column(Text())
    Export_id = Column(Integer(), ForeignKey('Export.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='ControlResponsibility', source_slot='props', mapping_type=None, target_class='Property', target_slot='ControlResponsibility_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "Property", foreign_keys="[Property.ControlResponsibility_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='ControlResponsibility', source_slot='links', mapping_type=None, target_class='Link', target_slot='ControlResponsibility_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "Link", foreign_keys="[Link.ControlResponsibility_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='ControlResponsibility', source_slot='responsible_roles', mapping_type=None, target_class='SspByComponentResponsibleRole', target_slot='ControlResponsibility_id', join_class=None, uses_join_table=None, multivalued=False)
    responsible_roles = relationship( "SspByComponentResponsibleRole", foreign_keys="[SspByComponentResponsibleRole.ControlResponsibility_id]")
    

    def __repr__(self):
        return f"ControlResponsibility(id={self.id},uuid={self.uuid},provided_uuid={self.provided_uuid},description={self.description},remarks={self.remarks},Export_id={self.Export_id},)"



    


class InheritedControlImplementation(Base):
    """
    Describes a control implementation inherited by a leveraging system.
    """
    __tablename__ = 'InheritedControlImplementation'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    uuid = Column(Text(), nullable=False )
    provided_uuid = Column(Text())
    description = Column(Text(), nullable=False )
    remarks = Column(Text())
    ByComponent_id = Column(Integer(), ForeignKey('ByComponent.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='InheritedControlImplementation', source_slot='props', mapping_type=None, target_class='Property', target_slot='InheritedControlImplementation_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "Property", foreign_keys="[Property.InheritedControlImplementation_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='InheritedControlImplementation', source_slot='links', mapping_type=None, target_class='Link', target_slot='InheritedControlImplementation_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "Link", foreign_keys="[Link.InheritedControlImplementation_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='InheritedControlImplementation', source_slot='responsible_roles', mapping_type=None, target_class='SspByComponentResponsibleRole', target_slot='InheritedControlImplementation_id', join_class=None, uses_join_table=None, multivalued=False)
    responsible_roles = relationship( "SspByComponentResponsibleRole", foreign_keys="[SspByComponentResponsibleRole.InheritedControlImplementation_id]")
    

    def __repr__(self):
        return f"InheritedControlImplementation(id={self.id},uuid={self.uuid},provided_uuid={self.provided_uuid},description={self.description},remarks={self.remarks},ByComponent_id={self.ByComponent_id},)"



    


class SatisfiedControlImplementation(Base):
    """
    Describes how this system satisfies a responsibility imposed by a leveraged system.
    """
    __tablename__ = 'SatisfiedControlImplementation'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    uuid = Column(Text(), nullable=False )
    responsibility_uuid = Column(Text())
    description = Column(Text(), nullable=False )
    remarks = Column(Text())
    ByComponent_id = Column(Integer(), ForeignKey('ByComponent.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='SatisfiedControlImplementation', source_slot='props', mapping_type=None, target_class='Property', target_slot='SatisfiedControlImplementation_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "Property", foreign_keys="[Property.SatisfiedControlImplementation_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='SatisfiedControlImplementation', source_slot='links', mapping_type=None, target_class='Link', target_slot='SatisfiedControlImplementation_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "Link", foreign_keys="[Link.SatisfiedControlImplementation_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='SatisfiedControlImplementation', source_slot='responsible_roles', mapping_type=None, target_class='SspByComponentResponsibleRole', target_slot='SatisfiedControlImplementation_id', join_class=None, uses_join_table=None, multivalued=False)
    responsible_roles = relationship( "SspByComponentResponsibleRole", foreign_keys="[SspByComponentResponsibleRole.SatisfiedControlImplementation_id]")
    

    def __repr__(self):
        return f"SatisfiedControlImplementation(id={self.id},uuid={self.uuid},responsibility_uuid={self.responsibility_uuid},description={self.description},remarks={self.remarks},ByComponent_id={self.ByComponent_id},)"



    


class AssessmentResults(Base):
    """
    Security assessment results, such as those provided by a FedRAMP assessor in a security assessment report.
    """
    __tablename__ = 'AssessmentResults'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    uuid = Column(Text(), nullable=False )
    metadata_id = Column(Integer(), ForeignKey('Metadata.id'), nullable=False )
    metadata = relationship("Metadata", uselist=False, foreign_keys=[metadata_id])
    import_ap_id = Column(Integer(), ForeignKey('ImportAssessmentPlan.id'), nullable=False )
    import_ap = relationship("ImportAssessmentPlan", uselist=False, foreign_keys=[import_ap_id])
    local_definitions_id = Column(Integer(), ForeignKey('AssessmentResultsLocalDefinitions.id'))
    local_definitions = relationship("AssessmentResultsLocalDefinitions", uselist=False, foreign_keys=[local_definitions_id])
    back_matter_id = Column(Integer(), ForeignKey('BackMatter.id'))
    back_matter = relationship("BackMatter", uselist=False, foreign_keys=[back_matter_id])
    
    
    # One-To-Many: OneToAnyMapping(source_class='AssessmentResults', source_slot='results', mapping_type=None, target_class='Result', target_slot='AssessmentResults_id', join_class=None, uses_join_table=None, multivalued=False)
    results = relationship( "Result", foreign_keys="[Result.AssessmentResults_id]")
    

    def __repr__(self):
        return f"AssessmentResults(id={self.id},uuid={self.uuid},metadata_id={self.metadata_id},import_ap_id={self.import_ap_id},local_definitions_id={self.local_definitions_id},back_matter_id={self.back_matter_id},)"



    


class ImportAssessmentPlan(Base):
    """
    Used by assessment-results to import information about the original plan for assessing the system.
    """
    __tablename__ = 'ImportAssessmentPlan'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    href = Column(Text(), nullable=False )
    remarks = Column(Text())
    

    def __repr__(self):
        return f"ImportAssessmentPlan(id={self.id},href={self.href},remarks={self.remarks},)"



    


class AssessmentResultsLocalDefinitions(Base):
    """
    Used to define data objects that are referenced by the assessment results but do not appear in the imported assessment plan.
    """
    __tablename__ = 'AssessmentResultsLocalDefinitions'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    remarks = Column(Text())
    
    
    # One-To-Many: OneToAnyMapping(source_class='AssessmentResultsLocalDefinitions', source_slot='objectives_and_methods', mapping_type=None, target_class='LocalObjective', target_slot='AssessmentResultsLocalDefinitions_id', join_class=None, uses_join_table=None, multivalued=False)
    objectives_and_methods = relationship( "LocalObjective", foreign_keys="[LocalObjective.AssessmentResultsLocalDefinitions_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='AssessmentResultsLocalDefinitions', source_slot='activities', mapping_type=None, target_class='Activity', target_slot='AssessmentResultsLocalDefinitions_id', join_class=None, uses_join_table=None, multivalued=False)
    activities = relationship( "Activity", foreign_keys="[Activity.AssessmentResultsLocalDefinitions_id]")
    

    def __repr__(self):
        return f"AssessmentResultsLocalDefinitions(id={self.id},remarks={self.remarks},)"



    


class Result(Base):
    """
    Identifies all of the assessment observations and findings, initial and residual risks, deviations, and disposition for a particular execution of the assessment.
    """
    __tablename__ = 'Result'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    uuid = Column(Text(), nullable=False )
    title = Column(Text(), nullable=False )
    description = Column(Text(), nullable=False )
    start = Column(Text(), nullable=False )
    end = Column(Text())
    remarks = Column(Text())
    AssessmentResults_id = Column(Integer(), ForeignKey('AssessmentResults.id'))
    local_definitions_id = Column(Integer(), ForeignKey('ResultLocalDefinitions.id'))
    local_definitions = relationship("ResultLocalDefinitions", uselist=False, foreign_keys=[local_definitions_id])
    reviewed_controls_id = Column(Integer(), ForeignKey('ReviewedControls.id'), nullable=False )
    reviewed_controls = relationship("ReviewedControls", uselist=False, foreign_keys=[reviewed_controls_id])
    assessment_log_id = Column(Integer(), ForeignKey('AssessmentLog.id'))
    assessment_log = relationship("AssessmentLog", uselist=False, foreign_keys=[assessment_log_id])
    
    
    # One-To-Many: OneToAnyMapping(source_class='Result', source_slot='attestations', mapping_type=None, target_class='Attestation', target_slot='Result_id', join_class=None, uses_join_table=None, multivalued=False)
    attestations = relationship( "Attestation", foreign_keys="[Attestation.Result_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Result', source_slot='observations', mapping_type=None, target_class='Observation', target_slot='Result_id', join_class=None, uses_join_table=None, multivalued=False)
    observations = relationship( "Observation", foreign_keys="[Observation.Result_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Result', source_slot='risks', mapping_type=None, target_class='Risk', target_slot='Result_id', join_class=None, uses_join_table=None, multivalued=False)
    risks = relationship( "Risk", foreign_keys="[Risk.Result_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Result', source_slot='findings', mapping_type=None, target_class='Finding', target_slot='Result_id', join_class=None, uses_join_table=None, multivalued=False)
    findings = relationship( "Finding", foreign_keys="[Finding.Result_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Result', source_slot='props', mapping_type=None, target_class='Property', target_slot='Result_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "Property", foreign_keys="[Property.Result_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Result', source_slot='links', mapping_type=None, target_class='Link', target_slot='Result_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "Link", foreign_keys="[Link.Result_id]")
    

    def __repr__(self):
        return f"Result(id={self.id},uuid={self.uuid},title={self.title},description={self.description},start={self.start},end={self.end},remarks={self.remarks},AssessmentResults_id={self.AssessmentResults_id},local_definitions_id={self.local_definitions_id},reviewed_controls_id={self.reviewed_controls_id},assessment_log_id={self.assessment_log_id},)"



    


class ResultLocalDefinitions(Base):
    """
    Used to define local implementation and assessment assets referenced by a result that do not appear in the imported system security plan.
    """
    __tablename__ = 'ResultLocalDefinitions'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    assessment_assets_id = Column(Integer(), ForeignKey('AssessmentAssets.id'))
    assessment_assets = relationship("AssessmentAssets", uselist=False, foreign_keys=[assessment_assets_id])
    
    
    # One-To-Many: OneToAnyMapping(source_class='ResultLocalDefinitions', source_slot='components', mapping_type=None, target_class='SystemComponent', target_slot='ResultLocalDefinitions_id', join_class=None, uses_join_table=None, multivalued=False)
    components = relationship( "SystemComponent", foreign_keys="[SystemComponent.ResultLocalDefinitions_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='ResultLocalDefinitions', source_slot='inventory_items', mapping_type=None, target_class='InventoryItem', target_slot='ResultLocalDefinitions_id', join_class=None, uses_join_table=None, multivalued=False)
    inventory_items = relationship( "InventoryItem", foreign_keys="[InventoryItem.ResultLocalDefinitions_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='ResultLocalDefinitions', source_slot='users', mapping_type=None, target_class='SystemUser', target_slot='ResultLocalDefinitions_id', join_class=None, uses_join_table=None, multivalued=False)
    users = relationship( "SystemUser", foreign_keys="[SystemUser.ResultLocalDefinitions_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='ResultLocalDefinitions', source_slot='tasks', mapping_type=None, target_class='Task', target_slot='ResultLocalDefinitions_id', join_class=None, uses_join_table=None, multivalued=False)
    tasks = relationship( "Task", foreign_keys="[Task.ResultLocalDefinitions_id]")
    

    def __repr__(self):
        return f"ResultLocalDefinitions(id={self.id},assessment_assets_id={self.assessment_assets_id},)"



    


class Attestation(Base):
    """
    A set of textual attestation statements, typically written by the assessor.
    """
    __tablename__ = 'Attestation'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    Result_id = Column(Integer(), ForeignKey('Result.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='Attestation', source_slot='parts', mapping_type=None, target_class='AssessmentPart', target_slot='Attestation_id', join_class=None, uses_join_table=None, multivalued=False)
    parts = relationship( "AssessmentPart", foreign_keys="[AssessmentPart.Attestation_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Attestation', source_slot='responsible_parties', mapping_type=None, target_class='ResponsibleParty', target_slot='Attestation_id', join_class=None, uses_join_table=None, multivalued=False)
    responsible_parties = relationship( "ResponsibleParty", foreign_keys="[ResponsibleParty.Attestation_id]")
    

    def __repr__(self):
        return f"Attestation(id={self.id},Result_id={self.Result_id},)"



    


class AssessmentLog(Base):
    """
    A log of all assessment-related actions taken.
    """
    __tablename__ = 'AssessmentLog'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    
    
    # One-To-Many: OneToAnyMapping(source_class='AssessmentLog', source_slot='entries', mapping_type=None, target_class='AssessmentLogEntry', target_slot='AssessmentLog_id', join_class=None, uses_join_table=None, multivalued=False)
    entries = relationship( "AssessmentLogEntry", foreign_keys="[AssessmentLogEntry.AssessmentLog_id]")
    

    def __repr__(self):
        return f"AssessmentLog(id={self.id},)"



    


class AssessmentLogEntry(Base):
    """
    Identifies the result of an action and/or task that occurred as part of executing an assessment plan or assessment event.
    """
    __tablename__ = 'AssessmentLogEntry'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    uuid = Column(Text(), nullable=False )
    title = Column(Text())
    description = Column(Text())
    start = Column(Text(), nullable=False )
    end = Column(Text())
    remarks = Column(Text())
    AssessmentLog_id = Column(Integer(), ForeignKey('AssessmentLog.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='AssessmentLogEntry', source_slot='logged_by', mapping_type=None, target_class='LoggedBy', target_slot='AssessmentLogEntry_id', join_class=None, uses_join_table=None, multivalued=False)
    logged_by = relationship( "LoggedBy", foreign_keys="[LoggedBy.AssessmentLogEntry_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='AssessmentLogEntry', source_slot='related_tasks', mapping_type=None, target_class='RelatedTask', target_slot='AssessmentLogEntry_id', join_class=None, uses_join_table=None, multivalued=False)
    related_tasks = relationship( "RelatedTask", foreign_keys="[RelatedTask.AssessmentLogEntry_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='AssessmentLogEntry', source_slot='props', mapping_type=None, target_class='Property', target_slot='AssessmentLogEntry_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "Property", foreign_keys="[Property.AssessmentLogEntry_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='AssessmentLogEntry', source_slot='links', mapping_type=None, target_class='Link', target_slot='AssessmentLogEntry_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "Link", foreign_keys="[Link.AssessmentLogEntry_id]")
    

    def __repr__(self):
        return f"AssessmentLogEntry(id={self.id},uuid={self.uuid},title={self.title},description={self.description},start={self.start},end={self.end},remarks={self.remarks},AssessmentLog_id={self.AssessmentLog_id},)"



    


class ComponentDefinition(Base):
    """
    A collection of component descriptions, which may optionally be grouped by capability.
    """
    __tablename__ = 'ComponentDefinition'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    uuid = Column(Text(), nullable=False )
    metadata_id = Column(Integer(), ForeignKey('Metadata.id'), nullable=False )
    metadata = relationship("Metadata", uselist=False, foreign_keys=[metadata_id])
    back_matter_id = Column(Integer(), ForeignKey('BackMatter.id'))
    back_matter = relationship("BackMatter", uselist=False, foreign_keys=[back_matter_id])
    
    
    # One-To-Many: OneToAnyMapping(source_class='ComponentDefinition', source_slot='import_component_definitions', mapping_type=None, target_class='ImportComponentDefinition', target_slot='ComponentDefinition_id', join_class=None, uses_join_table=None, multivalued=False)
    import_component_definitions = relationship( "ImportComponentDefinition", foreign_keys="[ImportComponentDefinition.ComponentDefinition_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='ComponentDefinition', source_slot='components', mapping_type=None, target_class='DefinedComponent', target_slot='ComponentDefinition_id', join_class=None, uses_join_table=None, multivalued=False)
    components = relationship( "DefinedComponent", foreign_keys="[DefinedComponent.ComponentDefinition_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='ComponentDefinition', source_slot='capabilities', mapping_type=None, target_class='Capability', target_slot='ComponentDefinition_id', join_class=None, uses_join_table=None, multivalued=False)
    capabilities = relationship( "Capability", foreign_keys="[Capability.ComponentDefinition_id]")
    

    def __repr__(self):
        return f"ComponentDefinition(id={self.id},uuid={self.uuid},metadata_id={self.metadata_id},back_matter_id={self.back_matter_id},)"



    


class ImportComponentDefinition(Base):
    """
    Loads a component definition from another resource.
    """
    __tablename__ = 'ImportComponentDefinition'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    href = Column(Text(), nullable=False )
    remarks = Column(Text())
    ComponentDefinition_id = Column(Integer(), ForeignKey('ComponentDefinition.id'))
    

    def __repr__(self):
        return f"ImportComponentDefinition(id={self.id},href={self.href},remarks={self.remarks},ComponentDefinition_id={self.ComponentDefinition_id},)"



    


class DefinedComponent(Base):
    """
    A defined component that can be part of an implemented system.
    """
    __tablename__ = 'DefinedComponent'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    uuid = Column(Text(), nullable=False )
    type = Column(Text(), nullable=False )
    title = Column(Text(), nullable=False )
    description = Column(Text(), nullable=False )
    purpose = Column(Text())
    remarks = Column(Text())
    ComponentDefinition_id = Column(Integer(), ForeignKey('ComponentDefinition.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='DefinedComponent', source_slot='protocols', mapping_type=None, target_class='Protocol', target_slot='DefinedComponent_id', join_class=None, uses_join_table=None, multivalued=False)
    protocols = relationship( "Protocol", foreign_keys="[Protocol.DefinedComponent_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='DefinedComponent', source_slot='control_implementations', mapping_type=None, target_class='ControlImplementationSet', target_slot='DefinedComponent_id', join_class=None, uses_join_table=None, multivalued=False)
    control_implementations = relationship( "ControlImplementationSet", foreign_keys="[ControlImplementationSet.DefinedComponent_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='DefinedComponent', source_slot='responsible_roles', mapping_type=None, target_class='ResponsibleRole', target_slot='DefinedComponent_id', join_class=None, uses_join_table=None, multivalued=False)
    responsible_roles = relationship( "ResponsibleRole", foreign_keys="[ResponsibleRole.DefinedComponent_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='DefinedComponent', source_slot='props', mapping_type=None, target_class='Property', target_slot='DefinedComponent_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "Property", foreign_keys="[Property.DefinedComponent_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='DefinedComponent', source_slot='links', mapping_type=None, target_class='Link', target_slot='DefinedComponent_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "Link", foreign_keys="[Link.DefinedComponent_id]")
    

    def __repr__(self):
        return f"DefinedComponent(id={self.id},uuid={self.uuid},type={self.type},title={self.title},description={self.description},purpose={self.purpose},remarks={self.remarks},ComponentDefinition_id={self.ComponentDefinition_id},)"



    


class Capability(Base):
    """
    A grouping of other components and/or capabilities.
    """
    __tablename__ = 'Capability'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    uuid = Column(Text(), nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text(), nullable=False )
    remarks = Column(Text())
    ComponentDefinition_id = Column(Integer(), ForeignKey('ComponentDefinition.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='Capability', source_slot='incorporates_components', mapping_type=None, target_class='IncorporatesComponent', target_slot='Capability_id', join_class=None, uses_join_table=None, multivalued=False)
    incorporates_components = relationship( "IncorporatesComponent", foreign_keys="[IncorporatesComponent.Capability_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Capability', source_slot='control_implementations', mapping_type=None, target_class='ControlImplementationSet', target_slot='Capability_id', join_class=None, uses_join_table=None, multivalued=False)
    control_implementations = relationship( "ControlImplementationSet", foreign_keys="[ControlImplementationSet.Capability_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Capability', source_slot='props', mapping_type=None, target_class='Property', target_slot='Capability_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "Property", foreign_keys="[Property.Capability_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Capability', source_slot='links', mapping_type=None, target_class='Link', target_slot='Capability_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "Link", foreign_keys="[Link.Capability_id]")
    

    def __repr__(self):
        return f"Capability(id={self.id},uuid={self.uuid},name={self.name},description={self.description},remarks={self.remarks},ComponentDefinition_id={self.ComponentDefinition_id},)"



    


class IncorporatesComponent(Base):
    """
    The collection of components comprising a capability.
    """
    __tablename__ = 'IncorporatesComponent'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    component_uuid = Column(Text(), nullable=False )
    description = Column(Text(), nullable=False )
    Capability_id = Column(Integer(), ForeignKey('Capability.id'))
    

    def __repr__(self):
        return f"IncorporatesComponent(id={self.id},component_uuid={self.component_uuid},description={self.description},Capability_id={self.Capability_id},)"



    


class ControlImplementationSet(Base):
    """
    Defines how the component or capability supports a set of controls.
    """
    __tablename__ = 'ControlImplementationSet'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    uuid = Column(Text(), nullable=False )
    source = Column(Text(), nullable=False )
    description = Column(Text(), nullable=False )
    DefinedComponent_id = Column(Integer(), ForeignKey('DefinedComponent.id'))
    Capability_id = Column(Integer(), ForeignKey('Capability.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='ControlImplementationSet', source_slot='set_parameters', mapping_type=None, target_class='SetParameter', target_slot='ControlImplementationSet_id', join_class=None, uses_join_table=None, multivalued=False)
    set_parameters = relationship( "SetParameter", foreign_keys="[SetParameter.ControlImplementationSet_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='ControlImplementationSet', source_slot='implemented_requirements', mapping_type=None, target_class='ImplementedRequirement', target_slot='ControlImplementationSet_id', join_class=None, uses_join_table=None, multivalued=False)
    implemented_requirements = relationship( "ImplementedRequirement", foreign_keys="[ImplementedRequirement.ControlImplementationSet_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='ControlImplementationSet', source_slot='props', mapping_type=None, target_class='Property', target_slot='ControlImplementationSet_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "Property", foreign_keys="[Property.ControlImplementationSet_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='ControlImplementationSet', source_slot='links', mapping_type=None, target_class='Link', target_slot='ControlImplementationSet_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "Link", foreign_keys="[Link.ControlImplementationSet_id]")
    

    def __repr__(self):
        return f"ControlImplementationSet(id={self.id},uuid={self.uuid},source={self.source},description={self.description},DefinedComponent_id={self.DefinedComponent_id},Capability_id={self.Capability_id},)"



    


class ImplementedRequirement(Base):
    """
    Describes how the containing component or capability implements an individual control.
    """
    __tablename__ = 'ImplementedRequirement'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    uuid = Column(Text(), nullable=False )
    control_id = Column(Text(), nullable=False )
    description = Column(Text(), nullable=False )
    remarks = Column(Text())
    ControlImplementationSet_id = Column(Integer(), ForeignKey('ControlImplementationSet.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='ImplementedRequirement', source_slot='set_parameters', mapping_type=None, target_class='SetParameter', target_slot='ImplementedRequirement_id', join_class=None, uses_join_table=None, multivalued=False)
    set_parameters = relationship( "SetParameter", foreign_keys="[SetParameter.ImplementedRequirement_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='ImplementedRequirement', source_slot='statements', mapping_type=None, target_class='ImplementedControlStatement', target_slot='ImplementedRequirement_id', join_class=None, uses_join_table=None, multivalued=False)
    statements = relationship( "ImplementedControlStatement", foreign_keys="[ImplementedControlStatement.ImplementedRequirement_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='ImplementedRequirement', source_slot='props', mapping_type=None, target_class='Property', target_slot='ImplementedRequirement_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "Property", foreign_keys="[Property.ImplementedRequirement_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='ImplementedRequirement', source_slot='links', mapping_type=None, target_class='Link', target_slot='ImplementedRequirement_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "Link", foreign_keys="[Link.ImplementedRequirement_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='ImplementedRequirement', source_slot='responsible_roles', mapping_type=None, target_class='ResponsibleRole', target_slot='ImplementedRequirement_id', join_class=None, uses_join_table=None, multivalued=False)
    responsible_roles = relationship( "ResponsibleRole", foreign_keys="[ResponsibleRole.ImplementedRequirement_id]")
    

    def __repr__(self):
        return f"ImplementedRequirement(id={self.id},uuid={self.uuid},control_id={self.control_id},description={self.description},remarks={self.remarks},ControlImplementationSet_id={self.ControlImplementationSet_id},)"



    


class ImplementedControlStatement(Base):
    """
    Identifies which statements within a control are addressed.
    """
    __tablename__ = 'ImplementedControlStatement'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    statement_id = Column(Text(), nullable=False )
    uuid = Column(Text(), nullable=False )
    description = Column(Text(), nullable=False )
    remarks = Column(Text())
    ImplementedRequirement_id = Column(Integer(), ForeignKey('ImplementedRequirement.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='ImplementedControlStatement', source_slot='props', mapping_type=None, target_class='Property', target_slot='ImplementedControlStatement_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "Property", foreign_keys="[Property.ImplementedControlStatement_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='ImplementedControlStatement', source_slot='links', mapping_type=None, target_class='Link', target_slot='ImplementedControlStatement_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "Link", foreign_keys="[Link.ImplementedControlStatement_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='ImplementedControlStatement', source_slot='responsible_roles', mapping_type=None, target_class='ResponsibleRole', target_slot='ImplementedControlStatement_id', join_class=None, uses_join_table=None, multivalued=False)
    responsible_roles = relationship( "ResponsibleRole", foreign_keys="[ResponsibleRole.ImplementedControlStatement_id]")
    

    def __repr__(self):
        return f"ImplementedControlStatement(id={self.id},statement_id={self.statement_id},uuid={self.uuid},description={self.description},remarks={self.remarks},ImplementedRequirement_id={self.ImplementedRequirement_id},)"



    


class MappingCollection(Base):
    """
    A collection of control mappings between source and target resources.
    """
    __tablename__ = 'MappingCollection'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    uuid = Column(Text(), nullable=False )
    metadata_id = Column(Integer(), ForeignKey('Metadata.id'), nullable=False )
    metadata = relationship("Metadata", uselist=False, foreign_keys=[metadata_id])
    provenance_id = Column(Integer(), ForeignKey('MappingProvenance.id'), nullable=False )
    provenance = relationship("MappingProvenance", uselist=False, foreign_keys=[provenance_id])
    back_matter_id = Column(Integer(), ForeignKey('BackMatter.id'))
    back_matter = relationship("BackMatter", uselist=False, foreign_keys=[back_matter_id])
    
    
    # One-To-Many: OneToAnyMapping(source_class='MappingCollection', source_slot='mappings', mapping_type=None, target_class='Mapping', target_slot='MappingCollection_id', join_class=None, uses_join_table=None, multivalued=False)
    mappings = relationship( "Mapping", foreign_keys="[Mapping.MappingCollection_id]")
    

    def __repr__(self):
        return f"MappingCollection(id={self.id},uuid={self.uuid},metadata_id={self.metadata_id},provenance_id={self.provenance_id},back_matter_id={self.back_matter_id},)"



    


class MappingProvenance(Base):
    """
    Mapping-level provenance details and mapping defaults.
    """
    __tablename__ = 'MappingProvenance'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    method = Column(Enum('human', 'automation', 'hybrid', name='MappingMethodEnum'), nullable=False )
    matching_rationale = Column(Enum('syntactic', 'semantic', 'functional', name='MatchingRationaleEnum'), nullable=False )
    status = Column(Enum('complete', 'not-complete', 'draft', 'deprecated', 'superseded', name='MappingStatusEnum'), nullable=False )
    mapping_description = Column(Text(), nullable=False )
    remarks = Column(Text())
    confidence_score_id = Column(Integer(), ForeignKey('ConfidenceScore.id'))
    confidence_score = relationship("ConfidenceScore", uselist=False, foreign_keys=[confidence_score_id])
    coverage_id = Column(Integer(), ForeignKey('Coverage.id'))
    coverage = relationship("Coverage", uselist=False, foreign_keys=[coverage_id])
    
    
    # One-To-Many: OneToAnyMapping(source_class='MappingProvenance', source_slot='responsible_parties', mapping_type=None, target_class='ResponsibleParty', target_slot='MappingProvenance_id', join_class=None, uses_join_table=None, multivalued=False)
    responsible_parties = relationship( "ResponsibleParty", foreign_keys="[ResponsibleParty.MappingProvenance_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='MappingProvenance', source_slot='props', mapping_type=None, target_class='Property', target_slot='MappingProvenance_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "Property", foreign_keys="[Property.MappingProvenance_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='MappingProvenance', source_slot='links', mapping_type=None, target_class='Link', target_slot='MappingProvenance_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "Link", foreign_keys="[Link.MappingProvenance_id]")
    

    def __repr__(self):
        return f"MappingProvenance(id={self.id},method={self.method},matching_rationale={self.matching_rationale},status={self.status},mapping_description={self.mapping_description},remarks={self.remarks},confidence_score_id={self.confidence_score_id},coverage_id={self.coverage_id},)"



    


class Mapping(Base):
    """
    A mapping between two mapped resources.
    """
    __tablename__ = 'Mapping'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    uuid = Column(Text(), nullable=False )
    method = Column(Enum('human', 'automation', 'hybrid', name='MappingMethodEnum'))
    matching_rationale = Column(Enum('syntactic', 'semantic', 'functional', name='MatchingRationaleEnum'))
    status = Column(Enum('complete', 'not-complete', 'draft', 'deprecated', 'superseded', name='MappingStatusEnum'))
    mapping_description = Column(Text())
    remarks = Column(Text())
    MappingCollection_id = Column(Integer(), ForeignKey('MappingCollection.id'))
    source_resource_id = Column(Integer(), ForeignKey('MappingResourceReference.id'), nullable=False )
    source_resource = relationship("MappingResourceReference", uselist=False, foreign_keys=[source_resource_id])
    target_resource_id = Column(Integer(), ForeignKey('MappingResourceReference.id'), nullable=False )
    target_resource = relationship("MappingResourceReference", uselist=False, foreign_keys=[target_resource_id])
    source_gap_summary_id = Column(Integer(), ForeignKey('GapSummary.id'))
    source_gap_summary = relationship("GapSummary", uselist=False, foreign_keys=[source_gap_summary_id])
    target_gap_summary_id = Column(Integer(), ForeignKey('GapSummary.id'))
    target_gap_summary = relationship("GapSummary", uselist=False, foreign_keys=[target_gap_summary_id])
    confidence_score_id = Column(Integer(), ForeignKey('ConfidenceScore.id'))
    confidence_score = relationship("ConfidenceScore", uselist=False, foreign_keys=[confidence_score_id])
    coverage_id = Column(Integer(), ForeignKey('Coverage.id'))
    coverage = relationship("Coverage", uselist=False, foreign_keys=[coverage_id])
    
    
    # One-To-Many: OneToAnyMapping(source_class='Mapping', source_slot='maps', mapping_type=None, target_class='Map', target_slot='Mapping_id', join_class=None, uses_join_table=None, multivalued=False)
    maps = relationship( "Map", foreign_keys="[Map.Mapping_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Mapping', source_slot='props', mapping_type=None, target_class='Property', target_slot='Mapping_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "Property", foreign_keys="[Property.Mapping_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Mapping', source_slot='links', mapping_type=None, target_class='Link', target_slot='Mapping_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "Link", foreign_keys="[Link.Mapping_id]")
    

    def __repr__(self):
        return f"Mapping(id={self.id},uuid={self.uuid},method={self.method},matching_rationale={self.matching_rationale},status={self.status},mapping_description={self.mapping_description},remarks={self.remarks},MappingCollection_id={self.MappingCollection_id},source_resource_id={self.source_resource_id},target_resource_id={self.target_resource_id},source_gap_summary_id={self.source_gap_summary_id},target_gap_summary_id={self.target_gap_summary_id},confidence_score_id={self.confidence_score_id},coverage_id={self.coverage_id},)"



    


class Map(Base):
    """
    A relationship-based mapping entry between source and target sets.
    """
    __tablename__ = 'Map'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    uuid = Column(Text(), nullable=False )
    ns = Column(Text())
    matching_rationale = Column(Enum('syntactic', 'semantic', 'functional', name='MatchingRationaleEnum'))
    relationship = Column(Text(), nullable=False )
    remarks = Column(Text())
    Mapping_id = Column(Integer(), ForeignKey('Mapping.id'))
    confidence_score_id = Column(Integer(), ForeignKey('ConfidenceScore.id'))
    confidence_score = relationship("ConfidenceScore", uselist=False, foreign_keys=[confidence_score_id])
    coverage_id = Column(Integer(), ForeignKey('Coverage.id'))
    coverage = relationship("Coverage", uselist=False, foreign_keys=[coverage_id])
    
    
    # One-To-Many: OneToAnyMapping(source_class='Map', source_slot='sources', mapping_type=None, target_class='MappingItem', target_slot='Map_id', join_class=None, uses_join_table=None, multivalued=False)
    sources = relationship( "MappingItem", foreign_keys="[MappingItem.Map_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Map', source_slot='targets', mapping_type=None, target_class='MappingItem', target_slot='Map_id', join_class=None, uses_join_table=None, multivalued=False)
    targets = relationship( "MappingItem", foreign_keys="[MappingItem.Map_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Map', source_slot='qualifiers', mapping_type=None, target_class='QualifierItem', target_slot='Map_id', join_class=None, uses_join_table=None, multivalued=False)
    qualifiers = relationship( "QualifierItem", foreign_keys="[QualifierItem.Map_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Map', source_slot='props', mapping_type=None, target_class='Property', target_slot='Map_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "Property", foreign_keys="[Property.Map_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Map', source_slot='links', mapping_type=None, target_class='Link', target_slot='Map_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "Link", foreign_keys="[Link.Map_id]")
    

    def __repr__(self):
        return f"Map(id={self.id},uuid={self.uuid},ns={self.ns},matching_rationale={self.matching_rationale},relationship={self.relationship},remarks={self.remarks},Mapping_id={self.Mapping_id},confidence_score_id={self.confidence_score_id},coverage_id={self.coverage_id},)"



    


class MappingItem(Base):
    """
    A source or target item participating in a mapping entry.
    """
    __tablename__ = 'MappingItem'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    type = Column(Enum('control', 'statement', name='MappingSubjectTypeEnum'), nullable=False )
    id_ref = Column(Text(), nullable=False )
    remarks = Column(Text())
    Map_id = Column(Integer(), ForeignKey('Map.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='MappingItem', source_slot='props', mapping_type=None, target_class='Property', target_slot='MappingItem_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "Property", foreign_keys="[Property.MappingItem_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='MappingItem', source_slot='links', mapping_type=None, target_class='Link', target_slot='MappingItem_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "Link", foreign_keys="[Link.MappingItem_id]")
    

    def __repr__(self):
        return f"MappingItem(id={self.id},type={self.type},id_ref={self.id_ref},remarks={self.remarks},Map_id={self.Map_id},)"



    


class MappingResourceReference(Base):
    """
    A reference to the source or target resource for a mapping.
    """
    __tablename__ = 'MappingResourceReference'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    ns = Column(Text())
    type = Column(Text(), nullable=False )
    href = Column(Text(), nullable=False )
    remarks = Column(Text())
    
    
    # One-To-Many: OneToAnyMapping(source_class='MappingResourceReference', source_slot='props', mapping_type=None, target_class='Property', target_slot='MappingResourceReference_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "Property", foreign_keys="[Property.MappingResourceReference_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='MappingResourceReference', source_slot='links', mapping_type=None, target_class='Link', target_slot='MappingResourceReference_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "Link", foreign_keys="[Link.MappingResourceReference_id]")
    

    def __repr__(self):
        return f"MappingResourceReference(id={self.id},ns={self.ns},type={self.type},href={self.href},remarks={self.remarks},)"



    


class QualifierItem(Base):
    """
    A qualifier describing requirements or incompatibilities.
    """
    __tablename__ = 'QualifierItem'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    subject = Column(Enum('source', 'target', 'both', name='QualifierSubjectEnum'), nullable=False )
    predicate = Column(Enum('has-requirement', 'has-incompatibility', name='QualifierPredicateEnum'), nullable=False )
    category = Column(Enum('restricted', 'addressable', 'blocked', name='QualifierCategoryEnum'), nullable=False )
    description = Column(Text(), nullable=False )
    remarks = Column(Text())
    Map_id = Column(Integer(), ForeignKey('Map.id'))
    

    def __repr__(self):
        return f"QualifierItem(id={self.id},subject={self.subject},predicate={self.predicate},category={self.category},description={self.description},remarks={self.remarks},Map_id={self.Map_id},)"



    


class GapSummary(Base):
    """
    A summary of controls that were not mapped.
    """
    __tablename__ = 'GapSummary'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    uuid = Column(Text(), nullable=False )
    
    
    # One-To-Many: OneToAnyMapping(source_class='GapSummary', source_slot='unmapped_controls', mapping_type=None, target_class='SelectControlById', target_slot='GapSummary_id', join_class=None, uses_join_table=None, multivalued=False)
    unmapped_controls = relationship( "SelectControlById", foreign_keys="[SelectControlById.GapSummary_id]")
    

    def __repr__(self):
        return f"GapSummary(id={self.id},uuid={self.uuid},)"



    


class ConfidenceScore(Base):
    """
    Confidence represented as a category and/or percentage value.
    """
    __tablename__ = 'ConfidenceScore'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    category = Column(Text())
    percentage = Column(Float())
    

    def __repr__(self):
        return f"ConfidenceScore(id={self.id},category={self.category},percentage={self.percentage},)"



    


class Coverage(Base):
    """
    A percentage representing target coverage by source mappings.
    """
    __tablename__ = 'Coverage'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    generation_method = Column(Text())
    target_coverage = Column(Float(), nullable=False )
    

    def __repr__(self):
        return f"Coverage(id={self.id},generation_method={self.generation_method},target_coverage={self.target_coverage},)"



    


class PlanOfActionAndMilestones(Base):
    """
    A plan of action and milestones that identifies initial and residual risks, deviations, and disposition.
    """
    __tablename__ = 'PlanOfActionAndMilestones'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    uuid = Column(Text(), nullable=False )
    metadata_id = Column(Integer(), ForeignKey('Metadata.id'), nullable=False )
    metadata = relationship("Metadata", uselist=False, foreign_keys=[metadata_id])
    import_ssp_id = Column(Integer(), ForeignKey('ImportSSP.id'))
    import_ssp = relationship("ImportSSP", uselist=False, foreign_keys=[import_ssp_id])
    system_id_uid = Column(Integer(), ForeignKey('SystemId.uid'))
    system_id = relationship("SystemId", uselist=False, foreign_keys=[system_id_uid])
    local_definitions_id = Column(Integer(), ForeignKey('PoamLocalDefinitions.id'))
    local_definitions = relationship("PoamLocalDefinitions", uselist=False, foreign_keys=[local_definitions_id])
    back_matter_id = Column(Integer(), ForeignKey('BackMatter.id'))
    back_matter = relationship("BackMatter", uselist=False, foreign_keys=[back_matter_id])
    
    
    # One-To-Many: OneToAnyMapping(source_class='PlanOfActionAndMilestones', source_slot='observations', mapping_type=None, target_class='Observation', target_slot='PlanOfActionAndMilestones_id', join_class=None, uses_join_table=None, multivalued=False)
    observations = relationship( "Observation", foreign_keys="[Observation.PlanOfActionAndMilestones_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='PlanOfActionAndMilestones', source_slot='risks', mapping_type=None, target_class='Risk', target_slot='PlanOfActionAndMilestones_id', join_class=None, uses_join_table=None, multivalued=False)
    risks = relationship( "Risk", foreign_keys="[Risk.PlanOfActionAndMilestones_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='PlanOfActionAndMilestones', source_slot='findings', mapping_type=None, target_class='Finding', target_slot='PlanOfActionAndMilestones_id', join_class=None, uses_join_table=None, multivalued=False)
    findings = relationship( "Finding", foreign_keys="[Finding.PlanOfActionAndMilestones_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='PlanOfActionAndMilestones', source_slot='poam_items', mapping_type=None, target_class='PoamItem', target_slot='PlanOfActionAndMilestones_id', join_class=None, uses_join_table=None, multivalued=False)
    poam_items = relationship( "PoamItem", foreign_keys="[PoamItem.PlanOfActionAndMilestones_id]")
    

    def __repr__(self):
        return f"PlanOfActionAndMilestones(id={self.id},uuid={self.uuid},metadata_id={self.metadata_id},import_ssp_id={self.import_ssp_id},system_id_uid={self.system_id_uid},local_definitions_id={self.local_definitions_id},back_matter_id={self.back_matter_id},)"



    


class PoamLocalDefinitions(Base):
    """
    Allows components and inventory items to be defined within the POA&M for cases where no OSCAL SSP is available with the POA&M.
    """
    __tablename__ = 'PoamLocalDefinitions'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    remarks = Column(Text())
    assessment_assets_id = Column(Integer(), ForeignKey('AssessmentAssets.id'))
    assessment_assets = relationship("AssessmentAssets", uselist=False, foreign_keys=[assessment_assets_id])
    
    
    # One-To-Many: OneToAnyMapping(source_class='PoamLocalDefinitions', source_slot='components', mapping_type=None, target_class='SystemComponent', target_slot='PoamLocalDefinitions_id', join_class=None, uses_join_table=None, multivalued=False)
    components = relationship( "SystemComponent", foreign_keys="[SystemComponent.PoamLocalDefinitions_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='PoamLocalDefinitions', source_slot='inventory_items', mapping_type=None, target_class='InventoryItem', target_slot='PoamLocalDefinitions_id', join_class=None, uses_join_table=None, multivalued=False)
    inventory_items = relationship( "InventoryItem", foreign_keys="[InventoryItem.PoamLocalDefinitions_id]")
    

    def __repr__(self):
        return f"PoamLocalDefinitions(id={self.id},remarks={self.remarks},assessment_assets_id={self.assessment_assets_id},)"



    


class PoamItem(Base):
    """
    Describes an individual POA&M item.
    """
    __tablename__ = 'PoamItem'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    uuid = Column(Text())
    title = Column(Text(), nullable=False )
    description = Column(Text(), nullable=False )
    remarks = Column(Text())
    PlanOfActionAndMilestones_id = Column(Integer(), ForeignKey('PlanOfActionAndMilestones.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='PoamItem', source_slot='origins', mapping_type=None, target_class='Origin', target_slot='PoamItem_id', join_class=None, uses_join_table=None, multivalued=False)
    origins = relationship( "Origin", foreign_keys="[Origin.PoamItem_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='PoamItem', source_slot='related_findings', mapping_type=None, target_class='RelatedFinding', target_slot='PoamItem_id', join_class=None, uses_join_table=None, multivalued=False)
    related_findings = relationship( "RelatedFinding", foreign_keys="[RelatedFinding.PoamItem_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='PoamItem', source_slot='related_observations', mapping_type=None, target_class='RelatedObservation', target_slot='PoamItem_id', join_class=None, uses_join_table=None, multivalued=False)
    related_observations = relationship( "RelatedObservation", foreign_keys="[RelatedObservation.PoamItem_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='PoamItem', source_slot='related_risks', mapping_type=None, target_class='AssociatedRisk', target_slot='PoamItem_id', join_class=None, uses_join_table=None, multivalued=False)
    related_risks = relationship( "AssociatedRisk", foreign_keys="[AssociatedRisk.PoamItem_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='PoamItem', source_slot='props', mapping_type=None, target_class='Property', target_slot='PoamItem_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "Property", foreign_keys="[Property.PoamItem_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='PoamItem', source_slot='links', mapping_type=None, target_class='Link', target_slot='PoamItem_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "Link", foreign_keys="[Link.PoamItem_id]")
    

    def __repr__(self):
        return f"PoamItem(id={self.id},uuid={self.uuid},title={self.title},description={self.description},remarks={self.remarks},PlanOfActionAndMilestones_id={self.PlanOfActionAndMilestones_id},)"



    


class RelatedFinding(Base):
    """
    Relates a POA&M item to a referenced finding.
    """
    __tablename__ = 'RelatedFinding'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    finding_uuid = Column(Text(), nullable=False )
    remarks = Column(Text())
    PoamItem_id = Column(Integer(), ForeignKey('PoamItem.id'))
    

    def __repr__(self):
        return f"RelatedFinding(id={self.id},finding_uuid={self.finding_uuid},remarks={self.remarks},PoamItem_id={self.PoamItem_id},)"



    


class LocationEmailAddresses(Base):
    """
    None
    """
    __tablename__ = 'Location_email_addresses'

    Location_id = Column(Integer(), ForeignKey('Location.id'), primary_key=True)
    email_addresses = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"Location_email_addresses(Location_id={self.Location_id},email_addresses={self.email_addresses},)"



    


class LocationUrls(Base):
    """
    None
    """
    __tablename__ = 'Location_urls'

    Location_id = Column(Integer(), ForeignKey('Location.id'), primary_key=True)
    urls = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"Location_urls(Location_id={self.Location_id},urls={self.urls},)"



    


class PartyEmailAddresses(Base):
    """
    None
    """
    __tablename__ = 'Party_email_addresses'

    Party_id = Column(Integer(), ForeignKey('Party.id'), primary_key=True)
    email_addresses = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"Party_email_addresses(Party_id={self.Party_id},email_addresses={self.email_addresses},)"



    


class PartyLocationUuids(Base):
    """
    None
    """
    __tablename__ = 'Party_location_uuids'

    Party_id = Column(Integer(), ForeignKey('Party.id'), primary_key=True)
    location_uuids = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"Party_location_uuids(Party_id={self.Party_id},location_uuids={self.location_uuids},)"



    


class PartyMemberOfOrganizations(Base):
    """
    None
    """
    __tablename__ = 'Party_member_of_organizations'

    Party_id = Column(Integer(), ForeignKey('Party.id'), primary_key=True)
    member_of_organizations = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"Party_member_of_organizations(Party_id={self.Party_id},member_of_organizations={self.member_of_organizations},)"



    


class ResponsiblePartyPartyUuids(Base):
    """
    None
    """
    __tablename__ = 'ResponsibleParty_party_uuids'

    ResponsibleParty_id = Column(Integer(), ForeignKey('ResponsibleParty.id'), primary_key=True)
    party_uuids = Column(Text(), primary_key=True, nullable=False )
    

    def __repr__(self):
        return f"ResponsibleParty_party_uuids(ResponsibleParty_id={self.ResponsibleParty_id},party_uuids={self.party_uuids},)"



    


class ResponsibleRolePartyUuids(Base):
    """
    None
    """
    __tablename__ = 'ResponsibleRole_party_uuids'

    ResponsibleRole_id = Column(Integer(), ForeignKey('ResponsibleRole.id'), primary_key=True)
    party_uuids = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"ResponsibleRole_party_uuids(ResponsibleRole_id={self.ResponsibleRole_id},party_uuids={self.party_uuids},)"



    


class AddressAddrLines(Base):
    """
    None
    """
    __tablename__ = 'Address_addr_lines'

    Address_id = Column(Integer(), ForeignKey('Address.id'), primary_key=True)
    addr_lines = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"Address_addr_lines(Address_id={self.Address_id},addr_lines={self.addr_lines},)"



    


class ParameterValues(Base):
    """
    None
    """
    __tablename__ = 'Parameter_values'

    Parameter_uid = Column(Integer(), ForeignKey('Parameter.uid'), primary_key=True)
    values = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"Parameter_values(Parameter_uid={self.Parameter_uid},values={self.values},)"



    


class ParameterSelectionChoice(Base):
    """
    None
    """
    __tablename__ = 'ParameterSelection_choice'

    ParameterSelection_id = Column(Integer(), ForeignKey('ParameterSelection.id'), primary_key=True)
    choice = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"ParameterSelection_choice(ParameterSelection_id={self.ParameterSelection_id},choice={self.choice},)"



    


class SelectControlByIdWithIds(Base):
    """
    None
    """
    __tablename__ = 'SelectControlById_with_ids'

    SelectControlById_id = Column(Integer(), ForeignKey('SelectControlById.id'), primary_key=True)
    with_ids = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"SelectControlById_with_ids(SelectControlById_id={self.SelectControlById_id},with_ids={self.with_ids},)"



    


class ParameterSettingValues(Base):
    """
    None
    """
    __tablename__ = 'ParameterSetting_values'

    ParameterSetting_id = Column(Integer(), ForeignKey('ParameterSetting.id'), primary_key=True)
    values = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"ParameterSetting_values(ParameterSetting_id={self.ParameterSetting_id},values={self.values},)"



    


class AssessmentSelectControlByIdStatementIds(Base):
    """
    None
    """
    __tablename__ = 'AssessmentSelectControlById_statement_ids'

    AssessmentSelectControlById_id = Column(Integer(), ForeignKey('AssessmentSelectControlById.id'), primary_key=True)
    statement_ids = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"AssessmentSelectControlById_statement_ids(AssessmentSelectControlById_id={self.AssessmentSelectControlById_id},statement_ids={self.statement_ids},)"



    


class SetParameterValues(Base):
    """
    None
    """
    __tablename__ = 'SetParameter_values'

    SetParameter_id = Column(Integer(), ForeignKey('SetParameter.id'), primary_key=True)
    values = Column(Text(), primary_key=True, nullable=False )
    

    def __repr__(self):
        return f"SetParameter_values(SetParameter_id={self.SetParameter_id},values={self.values},)"



    


class SystemUserRoleIds(Base):
    """
    None
    """
    __tablename__ = 'SystemUser_role_ids'

    SystemUser_id = Column(Integer(), ForeignKey('SystemUser.id'), primary_key=True)
    role_ids = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"SystemUser_role_ids(SystemUser_id={self.SystemUser_id},role_ids={self.role_ids},)"



    


class AuthorizedPrivilegeFunctionsPerformed(Base):
    """
    None
    """
    __tablename__ = 'AuthorizedPrivilege_functions_performed'

    AuthorizedPrivilege_id = Column(Integer(), ForeignKey('AuthorizedPrivilege.id'), primary_key=True)
    functions_performed = Column(Text(), primary_key=True, nullable=False )
    

    def __repr__(self):
        return f"AuthorizedPrivilege_functions_performed(AuthorizedPrivilege_id={self.AuthorizedPrivilege_id},functions_performed={self.functions_performed},)"



    


class ImplementationResponsibleRolePartyUuids(Base):
    """
    None
    """
    __tablename__ = 'ImplementationResponsibleRole_party_uuids'

    ImplementationResponsibleRole_id = Column(Integer(), ForeignKey('ImplementationResponsibleRole.id'), primary_key=True)
    party_uuids = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"ImplementationResponsibleRole_party_uuids(ImplementationResponsibleRole_id={self.ImplementationResponsibleRole_id},party_uuids={self.party_uuids},)"



    


class ImplementationResponsiblePartyPartyUuids(Base):
    """
    None
    """
    __tablename__ = 'ImplementationResponsibleParty_party_uuids'

    ImplementationResponsibleParty_id = Column(Integer(), ForeignKey('ImplementationResponsibleParty.id'), primary_key=True)
    party_uuids = Column(Text(), primary_key=True, nullable=False )
    

    def __repr__(self):
        return f"ImplementationResponsibleParty_party_uuids(ImplementationResponsibleParty_id={self.ImplementationResponsibleParty_id},party_uuids={self.party_uuids},)"



    


class ObservationMethods(Base):
    """
    None
    """
    __tablename__ = 'Observation_methods'

    Observation_id = Column(Integer(), ForeignKey('Observation.id'), primary_key=True)
    methods = Column(Text(), primary_key=True, nullable=False )
    

    def __repr__(self):
        return f"Observation_methods(Observation_id={self.Observation_id},methods={self.methods},)"



    


class ObservationTypes(Base):
    """
    None
    """
    __tablename__ = 'Observation_types'

    Observation_id = Column(Integer(), ForeignKey('Observation.id'), primary_key=True)
    types = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"Observation_types(Observation_id={self.Observation_id},types={self.types},)"



    


class InformationTypeCategorizationInformationTypeIds(Base):
    """
    None
    """
    __tablename__ = 'InformationTypeCategorization_information_type_ids'

    InformationTypeCategorization_id = Column(Integer(), ForeignKey('InformationTypeCategorization.id'), primary_key=True)
    information_type_ids = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"InformationTypeCategorization_information_type_ids(InformationTypeCategorization_id={self.InformationTypeCategorization_id},information_type_ids={self.information_type_ids},)"



    


class SspSystemCharacteristicsResponsiblePartyPartyUuids(Base):
    """
    None
    """
    __tablename__ = 'SspSystemCharacteristicsResponsibleParty_party_uuids'

    SspSystemCharacteristicsResponsibleParty_id = Column(Integer(), ForeignKey('SspSystemCharacteristicsResponsibleParty.id'), primary_key=True)
    party_uuids = Column(Text(), primary_key=True, nullable=False )
    

    def __repr__(self):
        return f"SspSystemCharacteristicsResponsibleParty_party_uuids(SspSystemCharacteristicsResponsibleParty_id={self.SspSystemCharacteristicsResponsibleParty_id},party_uuids={self.party_uuids},)"



    


class SspImplementedRequirementResponsibleRolePartyUuids(Base):
    """
    None
    """
    __tablename__ = 'SspImplementedRequirementResponsibleRole_party_uuids'

    SspImplementedRequirementResponsibleRole_id = Column(Integer(), ForeignKey('SspImplementedRequirementResponsibleRole.id'), primary_key=True)
    party_uuids = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"SspImplementedRequirementResponsibleRole_party_uuids(SspImplementedRequirementResponsibleRole_id={self.SspImplementedRequirementResponsibleRole_id},party_uuids={self.party_uuids},)"



    


class SspByComponentResponsibleRolePartyUuids(Base):
    """
    None
    """
    __tablename__ = 'SspByComponentResponsibleRole_party_uuids'

    SspByComponentResponsibleRole_id = Column(Integer(), ForeignKey('SspByComponentResponsibleRole.id'), primary_key=True)
    party_uuids = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"SspByComponentResponsibleRole_party_uuids(SspByComponentResponsibleRole_id={self.SspByComponentResponsibleRole_id},party_uuids={self.party_uuids},)"



    


class CatalogDocument(OscalDocument):
    """
    Root wrapper for an OSCAL Catalog document.
    """
    __tablename__ = 'CatalogDocument'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    catalog_id = Column(Integer(), ForeignKey('Catalog.id'), nullable=False )
    catalog = relationship("Catalog", uselist=False, foreign_keys=[catalog_id])
    

    def __repr__(self):
        return f"CatalogDocument(id={self.id},catalog_id={self.catalog_id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class MetadataProperty(Property):
    """
    Metadata-scoped OSCAL property.
    """
    __tablename__ = 'MetadataProperty'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    name = Column(Enum('keywords', 'resolution-tool', 'source-profile-uuid', name='MetadataPropNameEnum'), nullable=False )
    uuid = Column(Text())
    ns = Column(Text())
    value = Column(Text(), nullable=False )
    _class = Column(Text())
    remarks = Column(Text())
    group = Column(Text())
    Metadata_id = Column(Integer(), ForeignKey('Metadata.id'))
    

    def __repr__(self):
        return f"MetadataProperty(id={self.id},name={self.name},uuid={self.uuid},ns={self.ns},value={self.value},_class={self._class},remarks={self.remarks},group={self.group},Metadata_id={self.Metadata_id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class RevisionProperty(Property):
    """
    Revision-scoped OSCAL property.
    """
    __tablename__ = 'RevisionProperty'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    name = Column(Enum('marking', name='RevisionPropNameEnum'), nullable=False )
    uuid = Column(Text())
    ns = Column(Text())
    value = Column(Text(), nullable=False )
    _class = Column(Text())
    remarks = Column(Text())
    group = Column(Text())
    Revision_id = Column(Integer(), ForeignKey('Revision.id'))
    

    def __repr__(self):
        return f"RevisionProperty(id={self.id},name={self.name},uuid={self.uuid},ns={self.ns},value={self.value},_class={self._class},remarks={self.remarks},group={self.group},Revision_id={self.Revision_id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class LocationProperty(Property):
    """
    Location-scoped OSCAL property.
    """
    __tablename__ = 'LocationProperty'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    name = Column(Enum('type', name='LocationPropNameEnum'), nullable=False )
    uuid = Column(Text())
    ns = Column(Text())
    value = Column(Text(), nullable=False )
    _class = Column(Text())
    remarks = Column(Text())
    group = Column(Text())
    Location_id = Column(Integer(), ForeignKey('Location.id'))
    

    def __repr__(self):
        return f"LocationProperty(id={self.id},name={self.name},uuid={self.uuid},ns={self.ns},value={self.value},_class={self._class},remarks={self.remarks},group={self.group},Location_id={self.Location_id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class PartyProperty(Property):
    """
    Party-scoped OSCAL property.
    """
    __tablename__ = 'PartyProperty'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    name = Column(Enum('mail-stop', 'office', 'job-title', name='PartyPropNameEnum'), nullable=False )
    uuid = Column(Text())
    ns = Column(Text())
    value = Column(Text(), nullable=False )
    _class = Column(Text())
    remarks = Column(Text())
    group = Column(Text())
    Party_id = Column(Integer(), ForeignKey('Party.id'))
    

    def __repr__(self):
        return f"PartyProperty(id={self.id},name={self.name},uuid={self.uuid},ns={self.ns},value={self.value},_class={self._class},remarks={self.remarks},group={self.group},Party_id={self.Party_id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class ResourceProperty(Property):
    """
    Back-matter resource-scoped OSCAL property.
    """
    __tablename__ = 'ResourceProperty'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    name = Column(Enum('type', 'version', 'published', name='ResourcePropNameEnum'), nullable=False )
    uuid = Column(Text())
    ns = Column(Text())
    value = Column(Text(), nullable=False )
    _class = Column(Text())
    remarks = Column(Text())
    group = Column(Text())
    Resource_id = Column(Integer(), ForeignKey('Resource.id'))
    

    def __repr__(self):
        return f"ResourceProperty(id={self.id},name={self.name},uuid={self.uuid},ns={self.ns},value={self.value},_class={self._class},remarks={self.remarks},group={self.group},Resource_id={self.Resource_id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class PartProperty(Property):
    """
    Control-common part-scoped OSCAL property.
    """
    __tablename__ = 'PartProperty'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    name = Column(Enum('label', 'sort-id', 'alt-identifier', name='PartPropNameEnum'), nullable=False )
    uuid = Column(Text())
    ns = Column(Text())
    value = Column(Text(), nullable=False )
    _class = Column(Text())
    remarks = Column(Text())
    group = Column(Text())
    Part_uid = Column(Integer(), ForeignKey('Part.uid'))
    

    def __repr__(self):
        return f"PartProperty(id={self.id},name={self.name},uuid={self.uuid},ns={self.ns},value={self.value},_class={self._class},remarks={self.remarks},group={self.group},Part_uid={self.Part_uid},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class ParameterProperty(Property):
    """
    Control-common parameter-scoped OSCAL property.
    """
    __tablename__ = 'ParameterProperty'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    name = Column(Text(), nullable=False )
    uuid = Column(Text())
    ns = Column(Text())
    value = Column(Text(), nullable=False )
    _class = Column(Text())
    remarks = Column(Text())
    group = Column(Text())
    Parameter_uid = Column(Integer(), ForeignKey('Parameter.uid'))
    

    def __repr__(self):
        return f"ParameterProperty(id={self.id},name={self.name},uuid={self.uuid},ns={self.ns},value={self.value},_class={self._class},remarks={self.remarks},group={self.group},Parameter_uid={self.Parameter_uid},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class MetadataPartyExternalId(PartyExternalId):
    """
    Metadata-scoped external identifier.
    """
    __tablename__ = 'MetadataPartyExternalId'

    uid = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    scheme = Column(Text(), nullable=False )
    id = Column(Text(), nullable=False )
    Party_id = Column(Integer(), ForeignKey('Party.id'))
    

    def __repr__(self):
        return f"MetadataPartyExternalId(uid={self.uid},scheme={self.scheme},id={self.id},Party_id={self.Party_id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class ProfileDocument(OscalDocument):
    """
    Root wrapper for an OSCAL Profile document.
    """
    __tablename__ = 'ProfileDocument'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    profile_id = Column(Integer(), ForeignKey('Profile.id'), nullable=False )
    profile = relationship("Profile", uselist=False, foreign_keys=[profile_id])
    

    def __repr__(self):
        return f"ProfileDocument(id={self.id},profile_id={self.profile_id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class ProfileAlterationProperty(Property):
    """
    OSCAL property entries allowed in profile modify additions.
    """
    __tablename__ = 'ProfileAlterationProperty'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    name = Column(Enum('label', 'sort-id', 'alt-identifier', name='AlterationPropNameEnum'), nullable=False )
    uuid = Column(Text())
    ns = Column(Text())
    value = Column(Text(), nullable=False )
    _class = Column(Text())
    remarks = Column(Text())
    group = Column(Text())
    Addition_id = Column(Integer(), ForeignKey('Addition.id'))
    

    def __repr__(self):
        return f"ProfileAlterationProperty(id={self.id},name={self.name},uuid={self.uuid},ns={self.ns},value={self.value},_class={self._class},remarks={self.remarks},group={self.group},Addition_id={self.Addition_id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class AssessmentPlanDocument(OscalDocument):
    """
    Root wrapper for an OSCAL Assessment Plan document.
    """
    __tablename__ = 'AssessmentPlanDocument'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    assessment_plan_id = Column(Integer(), ForeignKey('AssessmentPlan.id'), nullable=False )
    assessment_plan = relationship("AssessmentPlan", uselist=False, foreign_keys=[assessment_plan_id])
    

    def __repr__(self):
        return f"AssessmentPlanDocument(id={self.id},assessment_plan_id={self.assessment_plan_id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class TermsAndConditionsPart(AssessmentPart):
    """
    A terms-and-conditions scoped assessment part.
    """
    __tablename__ = 'TermsAndConditionsPart'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    uuid = Column(Text())
    name = Column(Enum('rules-of-engagement', 'disclosures', 'assessment-inclusions', 'assessment-exclusions', 'results-delivery', 'assumptions', 'methodology', name='TermsAndConditionsPartNameEnum'), nullable=False )
    ns = Column(Text())
    _class = Column(Text())
    title = Column(Text())
    prose = Column(Text())
    TermsAndConditions_id = Column(Integer(), ForeignKey('TermsAndConditions.id'))
    TermsAndConditionsPart_id = Column(Integer(), ForeignKey('TermsAndConditionsPart.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='TermsAndConditionsPart', source_slot='parts', mapping_type=None, target_class='TermsAndConditionsPart', target_slot='TermsAndConditionsPart_id', join_class=None, uses_join_table=None, multivalued=False)
    parts = relationship( "TermsAndConditionsPart", foreign_keys="[TermsAndConditionsPart.TermsAndConditionsPart_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='TermsAndConditionsPart', source_slot='props', mapping_type=None, target_class='Property', target_slot='TermsAndConditionsPart_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "Property", foreign_keys="[Property.TermsAndConditionsPart_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='TermsAndConditionsPart', source_slot='links', mapping_type=None, target_class='Link', target_slot='TermsAndConditionsPart_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "Link", foreign_keys="[Link.TermsAndConditionsPart_id]")
    

    def __repr__(self):
        return f"TermsAndConditionsPart(id={self.id},uuid={self.uuid},name={self.name},ns={self.ns},_class={self._class},title={self.title},prose={self.prose},TermsAndConditions_id={self.TermsAndConditions_id},TermsAndConditionsPart_id={self.TermsAndConditionsPart_id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class ImplementationCommonProperty(Property):
    """
    Implementation-common scoped OSCAL property.
    """
    __tablename__ = 'ImplementationCommonProperty'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    name = Column(Enum('implementation-point', 'leveraged-authorization-uuid', 'inherited-uuid', 'asset-type', 'asset-id', 'asset-tag', 'public', 'virtual', 'vlan-id', 'network-id', 'label', 'sort-id', 'baseline-configuration-name', 'allows-authenticated-scan', 'function', 'hardware-model', 'model', 'os-name', 'os-version', 'software-name', 'software-version', 'software-patch-level', 'version', 'patch-level', 'release-date', 'validation-type', 'validation-reference', 'vendor-name', 'software-identifier', 'isa-title', 'isa-date', 'isa-remote-system-name', 'ipv4-address', 'ipv6-address', 'direction', 'uri', 'fqdn', 'serial-number', 'netbios-name', 'mac-address', 'physical-location', 'is-scanned', 'type', 'privilege-level', name='ImplementationPropNameEnum'), nullable=False )
    uuid = Column(Text())
    ns = Column(Text())
    value = Column(Text(), nullable=False )
    _class = Column(Text())
    remarks = Column(Text())
    group = Column(Text())
    SystemComponent_id = Column(Integer(), ForeignKey('SystemComponent.id'))
    SystemUser_id = Column(Integer(), ForeignKey('SystemUser.id'))
    InventoryItem_id = Column(Integer(), ForeignKey('InventoryItem.id'))
    ImplementedComponent_id = Column(Integer(), ForeignKey('ImplementedComponent.id'))
    

    def __repr__(self):
        return f"ImplementationCommonProperty(id={self.id},name={self.name},uuid={self.uuid},ns={self.ns},value={self.value},_class={self._class},remarks={self.remarks},group={self.group},SystemComponent_id={self.SystemComponent_id},SystemUser_id={self.SystemUser_id},InventoryItem_id={self.InventoryItem_id},ImplementedComponent_id={self.ImplementedComponent_id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class ImplementationCommonLink(Link):
    """
    Implementation-common scoped OSCAL link.
    """
    __tablename__ = 'ImplementationCommonLink'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    href = Column(Text(), nullable=False )
    rel = Column(Text())
    resource_fragment = Column(Text())
    media_type = Column(Text())
    text = Column(Text())
    SystemComponent_id = Column(Integer(), ForeignKey('SystemComponent.id'))
    SystemUser_id = Column(Integer(), ForeignKey('SystemUser.id'))
    InventoryItem_id = Column(Integer(), ForeignKey('InventoryItem.id'))
    ImplementedComponent_id = Column(Integer(), ForeignKey('ImplementedComponent.id'))
    SspSystemComponent_id = Column(Integer(), ForeignKey('SspSystemComponent.id'))
    SspInventoryItem_id = Column(Integer(), ForeignKey('SspInventoryItem.id'))
    

    def __repr__(self):
        return f"ImplementationCommonLink(id={self.id},href={self.href},rel={self.rel},resource_fragment={self.resource_fragment},media_type={self.media_type},text={self.text},SystemComponent_id={self.SystemComponent_id},SystemUser_id={self.SystemUser_id},InventoryItem_id={self.InventoryItem_id},ImplementedComponent_id={self.ImplementedComponent_id},SspSystemComponent_id={self.SspSystemComponent_id},SspInventoryItem_id={self.SspInventoryItem_id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class ImplementationResponsibleRole(ResponsibleRole):
    """
    Implementation-common scoped responsible role.
    """
    __tablename__ = 'ImplementationResponsibleRole'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    role_id = Column(Text(), nullable=False )
    remarks = Column(Text())
    SystemComponent_id = Column(Integer(), ForeignKey('SystemComponent.id'))
    SspSystemComponent_id = Column(Integer(), ForeignKey('SspSystemComponent.id'))
    
    
    party_uuids_rel = relationship( "ImplementationResponsibleRolePartyUuids" )
    party_uuids = association_proxy("party_uuids_rel", "party_uuids",
                                  creator=lambda x_: ImplementationResponsibleRolePartyUuids(party_uuids=x_))
    
    
    # One-To-Many: OneToAnyMapping(source_class='ImplementationResponsibleRole', source_slot='props', mapping_type=None, target_class='Property', target_slot='ImplementationResponsibleRole_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "Property", foreign_keys="[Property.ImplementationResponsibleRole_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='ImplementationResponsibleRole', source_slot='links', mapping_type=None, target_class='Link', target_slot='ImplementationResponsibleRole_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "Link", foreign_keys="[Link.ImplementationResponsibleRole_id]")
    

    def __repr__(self):
        return f"ImplementationResponsibleRole(id={self.id},role_id={self.role_id},remarks={self.remarks},SystemComponent_id={self.SystemComponent_id},SspSystemComponent_id={self.SspSystemComponent_id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class ImplementationResponsibleParty(ResponsibleParty):
    """
    Implementation-common scoped responsible party.
    """
    __tablename__ = 'ImplementationResponsibleParty'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    role_id = Column(Text(), nullable=False )
    remarks = Column(Text())
    InventoryItem_id = Column(Integer(), ForeignKey('InventoryItem.id'))
    ImplementedComponent_id = Column(Integer(), ForeignKey('ImplementedComponent.id'))
    SspInventoryItem_id = Column(Integer(), ForeignKey('SspInventoryItem.id'))
    
    
    party_uuids_rel = relationship( "ImplementationResponsiblePartyPartyUuids" )
    party_uuids = association_proxy("party_uuids_rel", "party_uuids",
                                  creator=lambda x_: ImplementationResponsiblePartyPartyUuids(party_uuids=x_))
    
    
    # One-To-Many: OneToAnyMapping(source_class='ImplementationResponsibleParty', source_slot='props', mapping_type=None, target_class='Property', target_slot='ImplementationResponsibleParty_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "Property", foreign_keys="[Property.ImplementationResponsibleParty_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='ImplementationResponsibleParty', source_slot='links', mapping_type=None, target_class='Link', target_slot='ImplementationResponsibleParty_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "Link", foreign_keys="[Link.ImplementationResponsibleParty_id]")
    

    def __repr__(self):
        return f"ImplementationResponsibleParty(id={self.id},role_id={self.role_id},remarks={self.remarks},InventoryItem_id={self.InventoryItem_id},ImplementedComponent_id={self.ImplementedComponent_id},SspInventoryItem_id={self.SspInventoryItem_id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class SspDocument(OscalDocument):
    """
    Root wrapper for an OSCAL System Security Plan document.
    """
    __tablename__ = 'SspDocument'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    system_security_plan_id = Column(Integer(), ForeignKey('SystemSecurityPlan.id'), nullable=False )
    system_security_plan = relationship("SystemSecurityPlan", uselist=False, foreign_keys=[system_security_plan_id])
    

    def __repr__(self):
        return f"SspDocument(id={self.id},system_security_plan_id={self.system_security_plan_id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class SspSystemCharacteristicsProp(Property):
    """
    SSP-scoped property used in system characteristics.
    """
    __tablename__ = 'SspSystemCharacteristicsProp'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    name = Column(Enum('identity-assurance-level', 'authenticator-assurance-level', 'federation-assurance-level', 'cloud-deployment-model', 'cloud-service-model', name='SystemCharacteristicsPropNameEnum'), nullable=False )
    uuid = Column(Text())
    ns = Column(Text())
    value = Column(Text(), nullable=False )
    _class = Column(Text())
    remarks = Column(Text())
    group = Column(Text())
    

    def __repr__(self):
        return f"SspSystemCharacteristicsProp(id={self.id},name={self.name},uuid={self.uuid},ns={self.ns},value={self.value},_class={self._class},remarks={self.remarks},group={self.group},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class SspSystemInformationProp(Property):
    """
    SSP-scoped property used in system information.
    """
    __tablename__ = 'SspSystemInformationProp'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    name = Column(Enum('privacy-designation', name='SystemInformationPropNameEnum'), nullable=False )
    uuid = Column(Text())
    ns = Column(Text())
    value = Column(Enum('yes', 'no', name='PrivacyDesignationEnum'), nullable=False )
    _class = Column(Text())
    remarks = Column(Text())
    group = Column(Text())
    SystemInformation_id = Column(Integer(), ForeignKey('SystemInformation.id'))
    

    def __repr__(self):
        return f"SspSystemInformationProp(id={self.id},name={self.name},uuid={self.uuid},ns={self.ns},value={self.value},_class={self._class},remarks={self.remarks},group={self.group},SystemInformation_id={self.SystemInformation_id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class SspControlOriginationProp(Property):
    """
    SSP-scoped property used in implemented requirement and by-component contexts.
    """
    __tablename__ = 'SspControlOriginationProp'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    name = Column(Enum('control-origination', name='ControlOriginationPropNameEnum'), nullable=False )
    uuid = Column(Text())
    ns = Column(Text())
    value = Column(Enum('organization', 'system-specific', 'customer-configured', 'customer-provided', 'inherited', name='ControlOriginationValueEnum'), nullable=False )
    _class = Column(Text())
    remarks = Column(Text())
    group = Column(Text())
    SspImplementedRequirement_id = Column(Integer(), ForeignKey('SspImplementedRequirement.id'))
    SspStatement_id = Column(Integer(), ForeignKey('SspStatement.id'))
    ByComponent_id = Column(Integer(), ForeignKey('ByComponent.id'))
    

    def __repr__(self):
        return f"SspControlOriginationProp(id={self.id},name={self.name},uuid={self.uuid},ns={self.ns},value={self.value},_class={self._class},remarks={self.remarks},group={self.group},SspImplementedRequirement_id={self.SspImplementedRequirement_id},SspStatement_id={self.SspStatement_id},ByComponent_id={self.ByComponent_id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class SspAllowsAuthenticatedScanProp(Property):
    """
    SSP-scoped property used for component and inventory allows-authenticated-scan.
    """
    __tablename__ = 'SspAllowsAuthenticatedScanProp'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    name = Column(Text(), nullable=False )
    uuid = Column(Text())
    ns = Column(Text())
    value = Column(Enum('yes', 'no', name='AllowsAuthenticatedScanEnum'), nullable=False )
    _class = Column(Text())
    remarks = Column(Text())
    group = Column(Text())
    SspSystemComponent_id = Column(Integer(), ForeignKey('SspSystemComponent.id'))
    SspInventoryItem_id = Column(Integer(), ForeignKey('SspInventoryItem.id'))
    

    def __repr__(self):
        return f"SspAllowsAuthenticatedScanProp(id={self.id},name={self.name},uuid={self.uuid},ns={self.ns},value={self.value},_class={self._class},remarks={self.remarks},group={self.group},SspSystemComponent_id={self.SspSystemComponent_id},SspInventoryItem_id={self.SspInventoryItem_id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class SspSystemInformationLink(Link):
    """
    SSP-scoped link used in system information.
    """
    __tablename__ = 'SspSystemInformationLink'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    href = Column(Text(), nullable=False )
    rel = Column(Text())
    resource_fragment = Column(Text())
    media_type = Column(Text())
    text = Column(Text())
    SystemInformation_id = Column(Integer(), ForeignKey('SystemInformation.id'))
    

    def __repr__(self):
        return f"SspSystemInformationLink(id={self.id},href={self.href},rel={self.rel},resource_fragment={self.resource_fragment},media_type={self.media_type},text={self.text},SystemInformation_id={self.SystemInformation_id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class SspDiagramLink(Link):
    """
    SSP-scoped link used in diagram objects.
    """
    __tablename__ = 'SspDiagramLink'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    href = Column(Text(), nullable=False )
    rel = Column(Text())
    resource_fragment = Column(Text())
    media_type = Column(Text())
    text = Column(Text())
    Diagram_id = Column(Integer(), ForeignKey('Diagram.id'))
    

    def __repr__(self):
        return f"SspDiagramLink(id={self.id},href={self.href},rel={self.rel},resource_fragment={self.resource_fragment},media_type={self.media_type},text={self.text},Diagram_id={self.Diagram_id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class SspLeveragedAuthorizationLink(Link):
    """
    SSP-scoped link used in leveraged authorization objects.
    """
    __tablename__ = 'SspLeveragedAuthorizationLink'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    href = Column(Text(), nullable=False )
    rel = Column(Text())
    resource_fragment = Column(Text())
    media_type = Column(Text())
    text = Column(Text())
    LeveragedAuthorization_id = Column(Integer(), ForeignKey('LeveragedAuthorization.id'))
    

    def __repr__(self):
        return f"SspLeveragedAuthorizationLink(id={self.id},href={self.href},rel={self.rel},resource_fragment={self.resource_fragment},media_type={self.media_type},text={self.text},LeveragedAuthorization_id={self.LeveragedAuthorization_id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class SspByComponentLink(Link):
    """
    SSP-scoped link used in by-component contexts.
    """
    __tablename__ = 'SspByComponentLink'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    href = Column(Text(), nullable=False )
    rel = Column(Text())
    resource_fragment = Column(Text())
    media_type = Column(Text())
    text = Column(Text())
    ByComponent_id = Column(Integer(), ForeignKey('ByComponent.id'))
    

    def __repr__(self):
        return f"SspByComponentLink(id={self.id},href={self.href},rel={self.rel},resource_fragment={self.resource_fragment},media_type={self.media_type},text={self.text},ByComponent_id={self.ByComponent_id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class SspSystemCharacteristicsResponsibleParty(ResponsibleParty):
    """
    SSP-scoped responsible party for system characteristics.
    """
    __tablename__ = 'SspSystemCharacteristicsResponsibleParty'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    role_id = Column(Text(), nullable=False )
    remarks = Column(Text())
    SystemCharacteristics_id = Column(Integer(), ForeignKey('SystemCharacteristics.id'))
    
    
    party_uuids_rel = relationship( "SspSystemCharacteristicsResponsiblePartyPartyUuids" )
    party_uuids = association_proxy("party_uuids_rel", "party_uuids",
                                  creator=lambda x_: SspSystemCharacteristicsResponsiblePartyPartyUuids(party_uuids=x_))
    
    
    # One-To-Many: OneToAnyMapping(source_class='SspSystemCharacteristicsResponsibleParty', source_slot='props', mapping_type=None, target_class='Property', target_slot='SspSystemCharacteristicsResponsibleParty_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "Property", foreign_keys="[Property.SspSystemCharacteristicsResponsibleParty_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='SspSystemCharacteristicsResponsibleParty', source_slot='links', mapping_type=None, target_class='Link', target_slot='SspSystemCharacteristicsResponsibleParty_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "Link", foreign_keys="[Link.SspSystemCharacteristicsResponsibleParty_id]")
    

    def __repr__(self):
        return f"SspSystemCharacteristicsResponsibleParty(id={self.id},role_id={self.role_id},remarks={self.remarks},SystemCharacteristics_id={self.SystemCharacteristics_id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class SspImplementedRequirementResponsibleRole(ResponsibleRole):
    """
    SSP-scoped responsible role used by implemented requirement and statement contexts.
    """
    __tablename__ = 'SspImplementedRequirementResponsibleRole'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    role_id = Column(Text(), nullable=False )
    remarks = Column(Text())
    SspImplementedRequirement_id = Column(Integer(), ForeignKey('SspImplementedRequirement.id'))
    SspStatement_id = Column(Integer(), ForeignKey('SspStatement.id'))
    
    
    party_uuids_rel = relationship( "SspImplementedRequirementResponsibleRolePartyUuids" )
    party_uuids = association_proxy("party_uuids_rel", "party_uuids",
                                  creator=lambda x_: SspImplementedRequirementResponsibleRolePartyUuids(party_uuids=x_))
    
    
    # One-To-Many: OneToAnyMapping(source_class='SspImplementedRequirementResponsibleRole', source_slot='props', mapping_type=None, target_class='Property', target_slot='SspImplementedRequirementResponsibleRole_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "Property", foreign_keys="[Property.SspImplementedRequirementResponsibleRole_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='SspImplementedRequirementResponsibleRole', source_slot='links', mapping_type=None, target_class='Link', target_slot='SspImplementedRequirementResponsibleRole_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "Link", foreign_keys="[Link.SspImplementedRequirementResponsibleRole_id]")
    

    def __repr__(self):
        return f"SspImplementedRequirementResponsibleRole(id={self.id},role_id={self.role_id},remarks={self.remarks},SspImplementedRequirement_id={self.SspImplementedRequirement_id},SspStatement_id={self.SspStatement_id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class SspByComponentResponsibleRole(ResponsibleRole):
    """
    SSP-scoped responsible role used by by-component contexts.
    """
    __tablename__ = 'SspByComponentResponsibleRole'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    role_id = Column(Text(), nullable=False )
    remarks = Column(Text())
    ByComponent_id = Column(Integer(), ForeignKey('ByComponent.id'))
    ProvidedControlImplementation_id = Column(Integer(), ForeignKey('ProvidedControlImplementation.id'))
    ControlResponsibility_id = Column(Integer(), ForeignKey('ControlResponsibility.id'))
    InheritedControlImplementation_id = Column(Integer(), ForeignKey('InheritedControlImplementation.id'))
    SatisfiedControlImplementation_id = Column(Integer(), ForeignKey('SatisfiedControlImplementation.id'))
    
    
    party_uuids_rel = relationship( "SspByComponentResponsibleRolePartyUuids" )
    party_uuids = association_proxy("party_uuids_rel", "party_uuids",
                                  creator=lambda x_: SspByComponentResponsibleRolePartyUuids(party_uuids=x_))
    
    
    # One-To-Many: OneToAnyMapping(source_class='SspByComponentResponsibleRole', source_slot='props', mapping_type=None, target_class='Property', target_slot='SspByComponentResponsibleRole_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "Property", foreign_keys="[Property.SspByComponentResponsibleRole_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='SspByComponentResponsibleRole', source_slot='links', mapping_type=None, target_class='Link', target_slot='SspByComponentResponsibleRole_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "Link", foreign_keys="[Link.SspByComponentResponsibleRole_id]")
    

    def __repr__(self):
        return f"SspByComponentResponsibleRole(id={self.id},role_id={self.role_id},remarks={self.remarks},ByComponent_id={self.ByComponent_id},ProvidedControlImplementation_id={self.ProvidedControlImplementation_id},ControlResponsibility_id={self.ControlResponsibility_id},InheritedControlImplementation_id={self.InheritedControlImplementation_id},SatisfiedControlImplementation_id={self.SatisfiedControlImplementation_id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class SspSystemComponent(SystemComponent):
    """
    SSP-scoped system component with allows-authenticated-scan property typing.
    """
    __tablename__ = 'SspSystemComponent'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    uuid = Column(Text(), nullable=False )
    type = Column(Text(), nullable=False )
    title = Column(Text(), nullable=False )
    description = Column(Text(), nullable=False )
    purpose = Column(Text())
    remarks = Column(Text())
    SystemImplementation_id = Column(Integer(), ForeignKey('SystemImplementation.id'))
    status_id = Column(Integer(), ForeignKey('ComponentStatus.id'), nullable=False )
    status = relationship("ComponentStatus", uselist=False, foreign_keys=[status_id])
    
    
    # One-To-Many: OneToAnyMapping(source_class='SspSystemComponent', source_slot='protocols', mapping_type=None, target_class='Protocol', target_slot='SspSystemComponent_id', join_class=None, uses_join_table=None, multivalued=False)
    protocols = relationship( "Protocol", foreign_keys="[Protocol.SspSystemComponent_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='SspSystemComponent', source_slot='responsible_roles', mapping_type=None, target_class='ImplementationResponsibleRole', target_slot='SspSystemComponent_id', join_class=None, uses_join_table=None, multivalued=False)
    responsible_roles = relationship( "ImplementationResponsibleRole", foreign_keys="[ImplementationResponsibleRole.SspSystemComponent_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='SspSystemComponent', source_slot='props', mapping_type=None, target_class='SspAllowsAuthenticatedScanProp', target_slot='SspSystemComponent_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "SspAllowsAuthenticatedScanProp", foreign_keys="[SspAllowsAuthenticatedScanProp.SspSystemComponent_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='SspSystemComponent', source_slot='links', mapping_type=None, target_class='ImplementationCommonLink', target_slot='SspSystemComponent_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "ImplementationCommonLink", foreign_keys="[ImplementationCommonLink.SspSystemComponent_id]")
    

    def __repr__(self):
        return f"SspSystemComponent(id={self.id},uuid={self.uuid},type={self.type},title={self.title},description={self.description},purpose={self.purpose},remarks={self.remarks},SystemImplementation_id={self.SystemImplementation_id},status_id={self.status_id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class SspInventoryItem(InventoryItem):
    """
    SSP-scoped inventory item with allows-authenticated-scan property typing.
    """
    __tablename__ = 'SspInventoryItem'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    uuid = Column(Text(), nullable=False )
    description = Column(Text(), nullable=False )
    remarks = Column(Text())
    SystemImplementation_id = Column(Integer(), ForeignKey('SystemImplementation.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='SspInventoryItem', source_slot='implemented_components', mapping_type=None, target_class='ImplementedComponent', target_slot='SspInventoryItem_id', join_class=None, uses_join_table=None, multivalued=False)
    implemented_components = relationship( "ImplementedComponent", foreign_keys="[ImplementedComponent.SspInventoryItem_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='SspInventoryItem', source_slot='responsible_parties', mapping_type=None, target_class='ImplementationResponsibleParty', target_slot='SspInventoryItem_id', join_class=None, uses_join_table=None, multivalued=False)
    responsible_parties = relationship( "ImplementationResponsibleParty", foreign_keys="[ImplementationResponsibleParty.SspInventoryItem_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='SspInventoryItem', source_slot='props', mapping_type=None, target_class='SspAllowsAuthenticatedScanProp', target_slot='SspInventoryItem_id', join_class=None, uses_join_table=None, multivalued=False)
    props = relationship( "SspAllowsAuthenticatedScanProp", foreign_keys="[SspAllowsAuthenticatedScanProp.SspInventoryItem_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='SspInventoryItem', source_slot='links', mapping_type=None, target_class='ImplementationCommonLink', target_slot='SspInventoryItem_id', join_class=None, uses_join_table=None, multivalued=False)
    links = relationship( "ImplementationCommonLink", foreign_keys="[ImplementationCommonLink.SspInventoryItem_id]")
    

    def __repr__(self):
        return f"SspInventoryItem(id={self.id},uuid={self.uuid},description={self.description},remarks={self.remarks},SystemImplementation_id={self.SystemImplementation_id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class AssessmentResultsDocument(OscalDocument):
    """
    Root wrapper for an OSCAL Assessment Results document.
    """
    __tablename__ = 'AssessmentResultsDocument'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    assessment_results_id = Column(Integer(), ForeignKey('AssessmentResults.id'), nullable=False )
    assessment_results = relationship("AssessmentResults", uselist=False, foreign_keys=[assessment_results_id])
    

    def __repr__(self):
        return f"AssessmentResultsDocument(id={self.id},assessment_results_id={self.assessment_results_id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class ComponentDefinitionDocument(OscalDocument):
    """
    Root wrapper for an OSCAL Component Definition document.
    """
    __tablename__ = 'ComponentDefinitionDocument'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    component_definition_id = Column(Integer(), ForeignKey('ComponentDefinition.id'), nullable=False )
    component_definition = relationship("ComponentDefinition", uselist=False, foreign_keys=[component_definition_id])
    

    def __repr__(self):
        return f"ComponentDefinitionDocument(id={self.id},component_definition_id={self.component_definition_id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class MappingCollectionDocument(OscalDocument):
    """
    Root wrapper for an OSCAL Mapping Collection document.
    """
    __tablename__ = 'MappingCollectionDocument'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    mapping_collection_id = Column(Integer(), ForeignKey('MappingCollection.id'), nullable=False )
    mapping_collection = relationship("MappingCollection", uselist=False, foreign_keys=[mapping_collection_id])
    

    def __repr__(self):
        return f"MappingCollectionDocument(id={self.id},mapping_collection_id={self.mapping_collection_id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class PoamDocument(OscalDocument):
    """
    Root wrapper for an OSCAL Plan of Action and Milestones document.
    """
    __tablename__ = 'PoamDocument'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    plan_of_action_and_milestones_id = Column(Integer(), ForeignKey('PlanOfActionAndMilestones.id'), nullable=False )
    plan_of_action_and_milestones = relationship("PlanOfActionAndMilestones", uselist=False, foreign_keys=[plan_of_action_and_milestones_id])
    

    def __repr__(self):
        return f"PoamDocument(id={self.id},plan_of_action_and_milestones_id={self.plan_of_action_and_milestones_id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


