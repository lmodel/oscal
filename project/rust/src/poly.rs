#![allow(non_camel_case_types)]

use crate::*;
use crate::poly_containers::*;


pub trait HasPropsAndLinks   {

    fn props(&self) -> Option<Vec<has_props_and_links_utl::props_range>>;
    // fn props_mut(&mut self) -> &mut Option<Vec<has_props_and_links_utl::props_range>>;
    // fn set_props<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Property>;

    fn links(&self) -> Option<Vec<has_props_and_links_utl::links_range>>;
    // fn links_mut(&mut self) -> &mut Option<Vec<has_props_and_links_utl::links_range>>;
    // fn set_links<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Link>;


}

impl HasPropsAndLinks for crate::HasPropsAndLinks {
        fn props(&self) -> Option<Vec<has_props_and_links_utl::props_range>> {
        self.props.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::props_range::Property(v.clone())).collect())
    }
        fn links(&self) -> Option<Vec<has_props_and_links_utl::links_range>> {
        self.links.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::links_range::Link(v.clone())).collect())
    }
}
impl HasPropsAndLinks for crate::OscalCommon {
        fn props(&self) -> Option<Vec<has_props_and_links_utl::props_range>> {
        self.props.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::props_range::Property(v.clone())).collect())
    }
        fn links(&self) -> Option<Vec<has_props_and_links_utl::links_range>> {
        self.links.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::links_range::Link(v.clone())).collect())
    }
}
impl HasPropsAndLinks for crate::Group {
        fn props(&self) -> Option<Vec<has_props_and_links_utl::props_range>> {
        self.props.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::props_range::Property(v.clone())).collect())
    }
        fn links(&self) -> Option<Vec<has_props_and_links_utl::links_range>> {
        self.links.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::links_range::Link(v.clone())).collect())
    }
}
impl HasPropsAndLinks for crate::Control {
        fn props(&self) -> Option<Vec<has_props_and_links_utl::props_range>> {
        self.props.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::props_range::Property(v.clone())).collect())
    }
        fn links(&self) -> Option<Vec<has_props_and_links_utl::links_range>> {
        self.links.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::links_range::Link(v.clone())).collect())
    }
}
impl HasPropsAndLinks for crate::Citation {
        fn props(&self) -> Option<Vec<has_props_and_links_utl::props_range>> {
        self.props.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::props_range::Property(v.clone())).collect())
    }
        fn links(&self) -> Option<Vec<has_props_and_links_utl::links_range>> {
        self.links.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::links_range::Link(v.clone())).collect())
    }
}
impl HasPropsAndLinks for crate::Part {
        fn props(&self) -> Option<Vec<has_props_and_links_utl::props_range>> {
        self.props.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::props_range::PartProperty(v.clone())).collect())
    }
        fn links(&self) -> Option<Vec<has_props_and_links_utl::links_range>> {
        self.links.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::links_range::Link(v.clone())).collect())
    }
}
impl HasPropsAndLinks for crate::ParameterSetting {
        fn props(&self) -> Option<Vec<has_props_and_links_utl::props_range>> {
        self.props.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::props_range::Property(v.clone())).collect())
    }
        fn links(&self) -> Option<Vec<has_props_and_links_utl::links_range>> {
        self.links.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::links_range::Link(v.clone())).collect())
    }
}
impl HasPropsAndLinks for crate::AssessmentPart {
        fn props(&self) -> Option<Vec<has_props_and_links_utl::props_range>> {
        self.props.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::props_range::Property(v.clone())).collect())
    }
        fn links(&self) -> Option<Vec<has_props_and_links_utl::links_range>> {
        self.links.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::links_range::Link(v.clone())).collect())
    }
}
impl HasPropsAndLinks for crate::ControlPart {
        fn props(&self) -> Option<Vec<has_props_and_links_utl::props_range>> {
        self.props.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::props_range::Property(v.clone())).collect())
    }
        fn links(&self) -> Option<Vec<has_props_and_links_utl::links_range>> {
        self.links.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::links_range::Link(v.clone())).collect())
    }
}
impl HasPropsAndLinks for crate::OriginActor {
        fn props(&self) -> Option<Vec<has_props_and_links_utl::props_range>> {
        self.props.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::props_range::Property(v.clone())).collect())
    }
        fn links(&self) -> Option<Vec<has_props_and_links_utl::links_range>> {
        self.links.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::links_range::Link(v.clone())).collect())
    }
}
impl HasPropsAndLinks for crate::Risk {
        fn props(&self) -> Option<Vec<has_props_and_links_utl::props_range>> {
        self.props.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::props_range::Property(v.clone())).collect())
    }
        fn links(&self) -> Option<Vec<has_props_and_links_utl::links_range>> {
        self.links.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::links_range::Link(v.clone())).collect())
    }
}
impl HasPropsAndLinks for crate::Characterization {
        fn props(&self) -> Option<Vec<has_props_and_links_utl::props_range>> {
        self.props.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::props_range::Property(v.clone())).collect())
    }
        fn links(&self) -> Option<Vec<has_props_and_links_utl::links_range>> {
        self.links.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::links_range::Link(v.clone())).collect())
    }
}
impl HasPropsAndLinks for crate::MitigatingFactor {
        fn props(&self) -> Option<Vec<has_props_and_links_utl::props_range>> {
        self.props.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::props_range::Property(v.clone())).collect())
    }
        fn links(&self) -> Option<Vec<has_props_and_links_utl::links_range>> {
        self.links.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::links_range::Link(v.clone())).collect())
    }
}
impl HasPropsAndLinks for crate::ControlImplementationSet {
        fn props(&self) -> Option<Vec<has_props_and_links_utl::props_range>> {
        self.props.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::props_range::Property(v.clone())).collect())
    }
        fn links(&self) -> Option<Vec<has_props_and_links_utl::links_range>> {
        self.links.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::links_range::Link(v.clone())).collect())
    }
}
impl HasPropsAndLinks for crate::ImplementedRequirement {
        fn props(&self) -> Option<Vec<has_props_and_links_utl::props_range>> {
        self.props.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::props_range::Property(v.clone())).collect())
    }
        fn links(&self) -> Option<Vec<has_props_and_links_utl::links_range>> {
        self.links.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::links_range::Link(v.clone())).collect())
    }
}
impl HasPropsAndLinks for crate::ImplementedControlStatement {
        fn props(&self) -> Option<Vec<has_props_and_links_utl::props_range>> {
        self.props.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::props_range::Property(v.clone())).collect())
    }
        fn links(&self) -> Option<Vec<has_props_and_links_utl::links_range>> {
        self.links.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::links_range::Link(v.clone())).collect())
    }
}
impl HasPropsAndLinks for crate::TermsAndConditionsPart {
        fn props(&self) -> Option<Vec<has_props_and_links_utl::props_range>> {
        self.props.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::props_range::Property(v.clone())).collect())
    }
        fn links(&self) -> Option<Vec<has_props_and_links_utl::links_range>> {
        self.links.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::links_range::Link(v.clone())).collect())
    }
}
impl HasPropsAndLinks for crate::Metadata {
        fn props(&self) -> Option<Vec<has_props_and_links_utl::props_range>> {
        self.props.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::props_range::MetadataProperty(v.clone())).collect())
    }
        fn links(&self) -> Option<Vec<has_props_and_links_utl::links_range>> {
        self.links.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::links_range::Link(v.clone())).collect())
    }
}
impl HasPropsAndLinks for crate::Revision {
        fn props(&self) -> Option<Vec<has_props_and_links_utl::props_range>> {
        self.props.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::props_range::RevisionProperty(v.clone())).collect())
    }
        fn links(&self) -> Option<Vec<has_props_and_links_utl::links_range>> {
        self.links.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::links_range::Link(v.clone())).collect())
    }
}
impl HasPropsAndLinks for crate::Role {
        fn props(&self) -> Option<Vec<has_props_and_links_utl::props_range>> {
        self.props.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::props_range::Property(v.clone())).collect())
    }
        fn links(&self) -> Option<Vec<has_props_and_links_utl::links_range>> {
        self.links.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::links_range::Link(v.clone())).collect())
    }
}
impl HasPropsAndLinks for crate::Location {
        fn props(&self) -> Option<Vec<has_props_and_links_utl::props_range>> {
        self.props.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::props_range::LocationProperty(v.clone())).collect())
    }
        fn links(&self) -> Option<Vec<has_props_and_links_utl::links_range>> {
        self.links.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::links_range::Link(v.clone())).collect())
    }
}
impl HasPropsAndLinks for crate::Party {
        fn props(&self) -> Option<Vec<has_props_and_links_utl::props_range>> {
        self.props.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::props_range::PartyProperty(v.clone())).collect())
    }
        fn links(&self) -> Option<Vec<has_props_and_links_utl::links_range>> {
        self.links.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::links_range::Link(v.clone())).collect())
    }
}
impl HasPropsAndLinks for crate::ResponsibleParty {
        fn props(&self) -> Option<Vec<has_props_and_links_utl::props_range>> {
        self.props.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::props_range::Property(v.clone())).collect())
    }
        fn links(&self) -> Option<Vec<has_props_and_links_utl::links_range>> {
        self.links.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::links_range::Link(v.clone())).collect())
    }
}
impl HasPropsAndLinks for crate::ResponsibleRole {
        fn props(&self) -> Option<Vec<has_props_and_links_utl::props_range>> {
        self.props.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::props_range::Property(v.clone())).collect())
    }
        fn links(&self) -> Option<Vec<has_props_and_links_utl::links_range>> {
        self.links.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::links_range::Link(v.clone())).collect())
    }
}
impl HasPropsAndLinks for crate::Action {
        fn props(&self) -> Option<Vec<has_props_and_links_utl::props_range>> {
        self.props.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::props_range::Property(v.clone())).collect())
    }
        fn links(&self) -> Option<Vec<has_props_and_links_utl::links_range>> {
        self.links.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::links_range::Link(v.clone())).collect())
    }
}
impl HasPropsAndLinks for crate::Parameter {
        fn props(&self) -> Option<Vec<has_props_and_links_utl::props_range>> {
        self.props.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::props_range::ParameterProperty(v.clone())).collect())
    }
        fn links(&self) -> Option<Vec<has_props_and_links_utl::links_range>> {
        self.links.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::links_range::Link(v.clone())).collect())
    }
}
impl HasPropsAndLinks for crate::ProfileGroup {
        fn props(&self) -> Option<Vec<has_props_and_links_utl::props_range>> {
        self.props.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::props_range::Property(v.clone())).collect())
    }
        fn links(&self) -> Option<Vec<has_props_and_links_utl::links_range>> {
        self.links.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::links_range::Link(v.clone())).collect())
    }
}
impl HasPropsAndLinks for crate::ReviewedControls {
        fn props(&self) -> Option<Vec<has_props_and_links_utl::props_range>> {
        self.props.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::props_range::Property(v.clone())).collect())
    }
        fn links(&self) -> Option<Vec<has_props_and_links_utl::links_range>> {
        self.links.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::links_range::Link(v.clone())).collect())
    }
}
impl HasPropsAndLinks for crate::ControlSelection {
        fn props(&self) -> Option<Vec<has_props_and_links_utl::props_range>> {
        self.props.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::props_range::Property(v.clone())).collect())
    }
        fn links(&self) -> Option<Vec<has_props_and_links_utl::links_range>> {
        self.links.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::links_range::Link(v.clone())).collect())
    }
}
impl HasPropsAndLinks for crate::ControlObjectiveSelection {
        fn props(&self) -> Option<Vec<has_props_and_links_utl::props_range>> {
        self.props.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::props_range::Property(v.clone())).collect())
    }
        fn links(&self) -> Option<Vec<has_props_and_links_utl::links_range>> {
        self.links.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::links_range::Link(v.clone())).collect())
    }
}
impl HasPropsAndLinks for crate::AssessmentSubject {
        fn props(&self) -> Option<Vec<has_props_and_links_utl::props_range>> {
        self.props.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::props_range::Property(v.clone())).collect())
    }
        fn links(&self) -> Option<Vec<has_props_and_links_utl::links_range>> {
        self.links.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::links_range::Link(v.clone())).collect())
    }
}
impl HasPropsAndLinks for crate::SelectSubjectById {
        fn props(&self) -> Option<Vec<has_props_and_links_utl::props_range>> {
        self.props.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::props_range::Property(v.clone())).collect())
    }
        fn links(&self) -> Option<Vec<has_props_and_links_utl::links_range>> {
        self.links.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::links_range::Link(v.clone())).collect())
    }
}
impl HasPropsAndLinks for crate::SubjectReference {
        fn props(&self) -> Option<Vec<has_props_and_links_utl::props_range>> {
        self.props.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::props_range::Property(v.clone())).collect())
    }
        fn links(&self) -> Option<Vec<has_props_and_links_utl::links_range>> {
        self.links.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::links_range::Link(v.clone())).collect())
    }
}
impl HasPropsAndLinks for crate::AssessmentSubjectPlaceholder {
        fn props(&self) -> Option<Vec<has_props_and_links_utl::props_range>> {
        self.props.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::props_range::Property(v.clone())).collect())
    }
        fn links(&self) -> Option<Vec<has_props_and_links_utl::links_range>> {
        self.links.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::links_range::Link(v.clone())).collect())
    }
}
impl HasPropsAndLinks for crate::AssessmentPlatform {
        fn props(&self) -> Option<Vec<has_props_and_links_utl::props_range>> {
        self.props.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::props_range::Property(v.clone())).collect())
    }
        fn links(&self) -> Option<Vec<has_props_and_links_utl::links_range>> {
        self.links.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::links_range::Link(v.clone())).collect())
    }
}
impl HasPropsAndLinks for crate::UsesComponent {
        fn props(&self) -> Option<Vec<has_props_and_links_utl::props_range>> {
        self.props.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::props_range::Property(v.clone())).collect())
    }
        fn links(&self) -> Option<Vec<has_props_and_links_utl::links_range>> {
        self.links.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::links_range::Link(v.clone())).collect())
    }
}
impl HasPropsAndLinks for crate::LocalObjective {
        fn props(&self) -> Option<Vec<has_props_and_links_utl::props_range>> {
        self.props.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::props_range::Property(v.clone())).collect())
    }
        fn links(&self) -> Option<Vec<has_props_and_links_utl::links_range>> {
        self.links.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::links_range::Link(v.clone())).collect())
    }
}
impl HasPropsAndLinks for crate::AssessmentMethod {
        fn props(&self) -> Option<Vec<has_props_and_links_utl::props_range>> {
        self.props.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::props_range::Property(v.clone())).collect())
    }
        fn links(&self) -> Option<Vec<has_props_and_links_utl::links_range>> {
        self.links.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::links_range::Link(v.clone())).collect())
    }
}
impl HasPropsAndLinks for crate::Activity {
        fn props(&self) -> Option<Vec<has_props_and_links_utl::props_range>> {
        self.props.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::props_range::Property(v.clone())).collect())
    }
        fn links(&self) -> Option<Vec<has_props_and_links_utl::links_range>> {
        self.links.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::links_range::Link(v.clone())).collect())
    }
}
impl HasPropsAndLinks for crate::Step {
        fn props(&self) -> Option<Vec<has_props_and_links_utl::props_range>> {
        self.props.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::props_range::Property(v.clone())).collect())
    }
        fn links(&self) -> Option<Vec<has_props_and_links_utl::links_range>> {
        self.links.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::links_range::Link(v.clone())).collect())
    }
}
impl HasPropsAndLinks for crate::Task {
        fn props(&self) -> Option<Vec<has_props_and_links_utl::props_range>> {
        self.props.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::props_range::Property(v.clone())).collect())
    }
        fn links(&self) -> Option<Vec<has_props_and_links_utl::links_range>> {
        self.links.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::links_range::Link(v.clone())).collect())
    }
}
impl HasPropsAndLinks for crate::AssociatedActivity {
        fn props(&self) -> Option<Vec<has_props_and_links_utl::props_range>> {
        self.props.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::props_range::Property(v.clone())).collect())
    }
        fn links(&self) -> Option<Vec<has_props_and_links_utl::links_range>> {
        self.links.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::links_range::Link(v.clone())).collect())
    }
}
impl HasPropsAndLinks for crate::SystemComponent {
        fn props(&self) -> Option<Vec<has_props_and_links_utl::props_range>> {
        self.props.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::props_range::ImplementationCommonProperty(v.clone())).collect())
    }
        fn links(&self) -> Option<Vec<has_props_and_links_utl::links_range>> {
        self.links.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::links_range::ImplementationCommonLink(v.clone())).collect())
    }
}
impl HasPropsAndLinks for crate::SystemUser {
        fn props(&self) -> Option<Vec<has_props_and_links_utl::props_range>> {
        self.props.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::props_range::ImplementationCommonProperty(v.clone())).collect())
    }
        fn links(&self) -> Option<Vec<has_props_and_links_utl::links_range>> {
        self.links.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::links_range::ImplementationCommonLink(v.clone())).collect())
    }
}
impl HasPropsAndLinks for crate::InventoryItem {
        fn props(&self) -> Option<Vec<has_props_and_links_utl::props_range>> {
        self.props.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::props_range::ImplementationCommonProperty(v.clone())).collect())
    }
        fn links(&self) -> Option<Vec<has_props_and_links_utl::links_range>> {
        self.links.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::links_range::ImplementationCommonLink(v.clone())).collect())
    }
}
impl HasPropsAndLinks for crate::ImplementedComponent {
        fn props(&self) -> Option<Vec<has_props_and_links_utl::props_range>> {
        self.props.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::props_range::ImplementationCommonProperty(v.clone())).collect())
    }
        fn links(&self) -> Option<Vec<has_props_and_links_utl::links_range>> {
        self.links.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::links_range::ImplementationCommonLink(v.clone())).collect())
    }
}
impl HasPropsAndLinks for crate::RelatedTask {
        fn props(&self) -> Option<Vec<has_props_and_links_utl::props_range>> {
        self.props.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::props_range::Property(v.clone())).collect())
    }
        fn links(&self) -> Option<Vec<has_props_and_links_utl::links_range>> {
        self.links.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::links_range::Link(v.clone())).collect())
    }
}
impl HasPropsAndLinks for crate::Observation {
        fn props(&self) -> Option<Vec<has_props_and_links_utl::props_range>> {
        self.props.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::props_range::Property(v.clone())).collect())
    }
        fn links(&self) -> Option<Vec<has_props_and_links_utl::links_range>> {
        self.links.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::links_range::Link(v.clone())).collect())
    }
}
impl HasPropsAndLinks for crate::RelevantEvidence {
        fn props(&self) -> Option<Vec<has_props_and_links_utl::props_range>> {
        self.props.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::props_range::Property(v.clone())).collect())
    }
        fn links(&self) -> Option<Vec<has_props_and_links_utl::links_range>> {
        self.links.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::links_range::Link(v.clone())).collect())
    }
}
impl HasPropsAndLinks for crate::Finding {
        fn props(&self) -> Option<Vec<has_props_and_links_utl::props_range>> {
        self.props.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::props_range::Property(v.clone())).collect())
    }
        fn links(&self) -> Option<Vec<has_props_and_links_utl::links_range>> {
        self.links.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::links_range::Link(v.clone())).collect())
    }
}
impl HasPropsAndLinks for crate::FindingTarget {
        fn props(&self) -> Option<Vec<has_props_and_links_utl::props_range>> {
        self.props.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::props_range::Property(v.clone())).collect())
    }
        fn links(&self) -> Option<Vec<has_props_and_links_utl::links_range>> {
        self.links.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::links_range::Link(v.clone())).collect())
    }
}
impl HasPropsAndLinks for crate::Facet {
        fn props(&self) -> Option<Vec<has_props_and_links_utl::props_range>> {
        self.props.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::props_range::Property(v.clone())).collect())
    }
        fn links(&self) -> Option<Vec<has_props_and_links_utl::links_range>> {
        self.links.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::links_range::Link(v.clone())).collect())
    }
}
impl HasPropsAndLinks for crate::Response {
        fn props(&self) -> Option<Vec<has_props_and_links_utl::props_range>> {
        self.props.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::props_range::Property(v.clone())).collect())
    }
        fn links(&self) -> Option<Vec<has_props_and_links_utl::links_range>> {
        self.links.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::links_range::Link(v.clone())).collect())
    }
}
impl HasPropsAndLinks for crate::RequiredAsset {
        fn props(&self) -> Option<Vec<has_props_and_links_utl::props_range>> {
        self.props.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::props_range::Property(v.clone())).collect())
    }
        fn links(&self) -> Option<Vec<has_props_and_links_utl::links_range>> {
        self.links.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::links_range::Link(v.clone())).collect())
    }
}
impl HasPropsAndLinks for crate::RiskLogEntry {
        fn props(&self) -> Option<Vec<has_props_and_links_utl::props_range>> {
        self.props.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::props_range::Property(v.clone())).collect())
    }
        fn links(&self) -> Option<Vec<has_props_and_links_utl::links_range>> {
        self.links.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::links_range::Link(v.clone())).collect())
    }
}
impl HasPropsAndLinks for crate::RiskResponseReference {
        fn props(&self) -> Option<Vec<has_props_and_links_utl::props_range>> {
        self.props.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::props_range::Property(v.clone())).collect())
    }
        fn links(&self) -> Option<Vec<has_props_and_links_utl::links_range>> {
        self.links.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::links_range::Link(v.clone())).collect())
    }
}
impl HasPropsAndLinks for crate::Result {
        fn props(&self) -> Option<Vec<has_props_and_links_utl::props_range>> {
        self.props.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::props_range::Property(v.clone())).collect())
    }
        fn links(&self) -> Option<Vec<has_props_and_links_utl::links_range>> {
        self.links.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::links_range::Link(v.clone())).collect())
    }
}
impl HasPropsAndLinks for crate::AssessmentLogEntry {
        fn props(&self) -> Option<Vec<has_props_and_links_utl::props_range>> {
        self.props.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::props_range::Property(v.clone())).collect())
    }
        fn links(&self) -> Option<Vec<has_props_and_links_utl::links_range>> {
        self.links.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::links_range::Link(v.clone())).collect())
    }
}
impl HasPropsAndLinks for crate::DefinedComponent {
        fn props(&self) -> Option<Vec<has_props_and_links_utl::props_range>> {
        self.props.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::props_range::Property(v.clone())).collect())
    }
        fn links(&self) -> Option<Vec<has_props_and_links_utl::links_range>> {
        self.links.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::links_range::Link(v.clone())).collect())
    }
}
impl HasPropsAndLinks for crate::Capability {
        fn props(&self) -> Option<Vec<has_props_and_links_utl::props_range>> {
        self.props.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::props_range::Property(v.clone())).collect())
    }
        fn links(&self) -> Option<Vec<has_props_and_links_utl::links_range>> {
        self.links.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::links_range::Link(v.clone())).collect())
    }
}
impl HasPropsAndLinks for crate::MappingProvenance {
        fn props(&self) -> Option<Vec<has_props_and_links_utl::props_range>> {
        self.props.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::props_range::Property(v.clone())).collect())
    }
        fn links(&self) -> Option<Vec<has_props_and_links_utl::links_range>> {
        self.links.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::links_range::Link(v.clone())).collect())
    }
}
impl HasPropsAndLinks for crate::Mapping {
        fn props(&self) -> Option<Vec<has_props_and_links_utl::props_range>> {
        self.props.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::props_range::Property(v.clone())).collect())
    }
        fn links(&self) -> Option<Vec<has_props_and_links_utl::links_range>> {
        self.links.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::links_range::Link(v.clone())).collect())
    }
}
impl HasPropsAndLinks for crate::Map {
        fn props(&self) -> Option<Vec<has_props_and_links_utl::props_range>> {
        self.props.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::props_range::Property(v.clone())).collect())
    }
        fn links(&self) -> Option<Vec<has_props_and_links_utl::links_range>> {
        self.links.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::links_range::Link(v.clone())).collect())
    }
}
impl HasPropsAndLinks for crate::MappingItem {
        fn props(&self) -> Option<Vec<has_props_and_links_utl::props_range>> {
        self.props.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::props_range::Property(v.clone())).collect())
    }
        fn links(&self) -> Option<Vec<has_props_and_links_utl::links_range>> {
        self.links.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::links_range::Link(v.clone())).collect())
    }
}
impl HasPropsAndLinks for crate::MappingResourceReference {
        fn props(&self) -> Option<Vec<has_props_and_links_utl::props_range>> {
        self.props.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::props_range::Property(v.clone())).collect())
    }
        fn links(&self) -> Option<Vec<has_props_and_links_utl::links_range>> {
        self.links.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::links_range::Link(v.clone())).collect())
    }
}
impl HasPropsAndLinks for crate::PoamItem {
        fn props(&self) -> Option<Vec<has_props_and_links_utl::props_range>> {
        self.props.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::props_range::Property(v.clone())).collect())
    }
        fn links(&self) -> Option<Vec<has_props_and_links_utl::links_range>> {
        self.links.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::links_range::Link(v.clone())).collect())
    }
}
impl HasPropsAndLinks for crate::SspInventoryItem {
        fn props(&self) -> Option<Vec<has_props_and_links_utl::props_range>> {
        self.props.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::props_range::SspAllowsAuthenticatedScanProp(v.clone())).collect())
    }
        fn links(&self) -> Option<Vec<has_props_and_links_utl::links_range>> {
        self.links.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::links_range::ImplementationCommonLink(v.clone())).collect())
    }
}
impl HasPropsAndLinks for crate::SspSystemComponent {
        fn props(&self) -> Option<Vec<has_props_and_links_utl::props_range>> {
        self.props.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::props_range::SspAllowsAuthenticatedScanProp(v.clone())).collect())
    }
        fn links(&self) -> Option<Vec<has_props_and_links_utl::links_range>> {
        self.links.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::links_range::ImplementationCommonLink(v.clone())).collect())
    }
}
impl HasPropsAndLinks for crate::ImplementationResponsibleRole {
        fn props(&self) -> Option<Vec<has_props_and_links_utl::props_range>> {
        self.props.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::props_range::Property(v.clone())).collect())
    }
        fn links(&self) -> Option<Vec<has_props_and_links_utl::links_range>> {
        self.links.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::links_range::Link(v.clone())).collect())
    }
}
impl HasPropsAndLinks for crate::SspImplementedRequirementResponsibleRole {
        fn props(&self) -> Option<Vec<has_props_and_links_utl::props_range>> {
        self.props.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::props_range::Property(v.clone())).collect())
    }
        fn links(&self) -> Option<Vec<has_props_and_links_utl::links_range>> {
        self.links.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::links_range::Link(v.clone())).collect())
    }
}
impl HasPropsAndLinks for crate::SspByComponentResponsibleRole {
        fn props(&self) -> Option<Vec<has_props_and_links_utl::props_range>> {
        self.props.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::props_range::Property(v.clone())).collect())
    }
        fn links(&self) -> Option<Vec<has_props_and_links_utl::links_range>> {
        self.links.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::links_range::Link(v.clone())).collect())
    }
}
impl HasPropsAndLinks for crate::ImplementationResponsibleParty {
        fn props(&self) -> Option<Vec<has_props_and_links_utl::props_range>> {
        self.props.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::props_range::Property(v.clone())).collect())
    }
        fn links(&self) -> Option<Vec<has_props_and_links_utl::links_range>> {
        self.links.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::links_range::Link(v.clone())).collect())
    }
}
impl HasPropsAndLinks for crate::SspSystemCharacteristicsResponsibleParty {
        fn props(&self) -> Option<Vec<has_props_and_links_utl::props_range>> {
        self.props.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::props_range::Property(v.clone())).collect())
    }
        fn links(&self) -> Option<Vec<has_props_and_links_utl::links_range>> {
        self.links.as_ref().map(|xs| xs.iter().map(|v| has_props_and_links_utl::links_range::Link(v.clone())).collect())
    }
}

impl HasPropsAndLinks for crate::HasPropsAndLinksOrSubtype {
        fn props(&self) -> Option<Vec<has_props_and_links_utl::props_range>> {
        match self {
                HasPropsAndLinksOrSubtype::OscalCommon(val) => val.props().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::Group(val) => val.props().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::Control(val) => val.props().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::Citation(val) => val.props().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::Part(val) => val.props().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::ParameterSetting(val) => val.props().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::AssessmentPart(val) => val.props().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::ControlPart(val) => val.props().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::OriginActor(val) => val.props().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::Risk(val) => val.props().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::Characterization(val) => val.props().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::MitigatingFactor(val) => val.props().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::ControlImplementationSet(val) => val.props().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::ImplementedRequirement(val) => val.props().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::ImplementedControlStatement(val) => val.props().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::TermsAndConditionsPart(val) => val.props().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::Metadata(val) => val.props().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::Revision(val) => val.props().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::Role(val) => val.props().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::Location(val) => val.props().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::Party(val) => val.props().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::ResponsibleParty(val) => val.props().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::ResponsibleRole(val) => val.props().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::Action(val) => val.props().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::Parameter(val) => val.props().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::ProfileGroup(val) => val.props().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::ReviewedControls(val) => val.props().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::ControlSelection(val) => val.props().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::ControlObjectiveSelection(val) => val.props().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::AssessmentSubject(val) => val.props().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::SelectSubjectById(val) => val.props().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::SubjectReference(val) => val.props().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::AssessmentSubjectPlaceholder(val) => val.props().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::AssessmentPlatform(val) => val.props().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::UsesComponent(val) => val.props().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::LocalObjective(val) => val.props().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::AssessmentMethod(val) => val.props().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::Activity(val) => val.props().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::Step(val) => val.props().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::Task(val) => val.props().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::AssociatedActivity(val) => val.props().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::SystemComponent(val) => val.props().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::SystemUser(val) => val.props().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::InventoryItem(val) => val.props().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::ImplementedComponent(val) => val.props().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::RelatedTask(val) => val.props().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::Observation(val) => val.props().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::RelevantEvidence(val) => val.props().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::Finding(val) => val.props().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::FindingTarget(val) => val.props().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::Facet(val) => val.props().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::Response(val) => val.props().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::RequiredAsset(val) => val.props().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::RiskLogEntry(val) => val.props().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::RiskResponseReference(val) => val.props().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::Result(val) => val.props().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::AssessmentLogEntry(val) => val.props().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::DefinedComponent(val) => val.props().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::Capability(val) => val.props().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::MappingProvenance(val) => val.props().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::Mapping(val) => val.props().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::Map(val) => val.props().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::MappingItem(val) => val.props().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::MappingResourceReference(val) => val.props().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::PoamItem(val) => val.props().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::SspInventoryItem(val) => val.props().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::SspSystemComponent(val) => val.props().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::ImplementationResponsibleRole(val) => val.props().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::SspImplementedRequirementResponsibleRole(val) => val.props().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::SspByComponentResponsibleRole(val) => val.props().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::ImplementationResponsibleParty(val) => val.props().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::SspSystemCharacteristicsResponsibleParty(val) => val.props().map(|x| x.to_any()),

        }
    }
        fn links(&self) -> Option<Vec<has_props_and_links_utl::links_range>> {
        match self {
                HasPropsAndLinksOrSubtype::OscalCommon(val) => val.links().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::Group(val) => val.links().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::Control(val) => val.links().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::Citation(val) => val.links().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::Part(val) => val.links().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::ParameterSetting(val) => val.links().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::AssessmentPart(val) => val.links().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::ControlPart(val) => val.links().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::OriginActor(val) => val.links().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::Risk(val) => val.links().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::Characterization(val) => val.links().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::MitigatingFactor(val) => val.links().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::ControlImplementationSet(val) => val.links().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::ImplementedRequirement(val) => val.links().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::ImplementedControlStatement(val) => val.links().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::TermsAndConditionsPart(val) => val.links().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::Metadata(val) => val.links().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::Revision(val) => val.links().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::Role(val) => val.links().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::Location(val) => val.links().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::Party(val) => val.links().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::ResponsibleParty(val) => val.links().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::ResponsibleRole(val) => val.links().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::Action(val) => val.links().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::Parameter(val) => val.links().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::ProfileGroup(val) => val.links().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::ReviewedControls(val) => val.links().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::ControlSelection(val) => val.links().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::ControlObjectiveSelection(val) => val.links().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::AssessmentSubject(val) => val.links().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::SelectSubjectById(val) => val.links().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::SubjectReference(val) => val.links().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::AssessmentSubjectPlaceholder(val) => val.links().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::AssessmentPlatform(val) => val.links().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::UsesComponent(val) => val.links().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::LocalObjective(val) => val.links().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::AssessmentMethod(val) => val.links().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::Activity(val) => val.links().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::Step(val) => val.links().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::Task(val) => val.links().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::AssociatedActivity(val) => val.links().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::SystemComponent(val) => val.links().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::SystemUser(val) => val.links().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::InventoryItem(val) => val.links().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::ImplementedComponent(val) => val.links().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::RelatedTask(val) => val.links().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::Observation(val) => val.links().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::RelevantEvidence(val) => val.links().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::Finding(val) => val.links().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::FindingTarget(val) => val.links().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::Facet(val) => val.links().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::Response(val) => val.links().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::RequiredAsset(val) => val.links().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::RiskLogEntry(val) => val.links().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::RiskResponseReference(val) => val.links().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::Result(val) => val.links().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::AssessmentLogEntry(val) => val.links().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::DefinedComponent(val) => val.links().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::Capability(val) => val.links().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::MappingProvenance(val) => val.links().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::Mapping(val) => val.links().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::Map(val) => val.links().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::MappingItem(val) => val.links().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::MappingResourceReference(val) => val.links().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::PoamItem(val) => val.links().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::SspInventoryItem(val) => val.links().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::SspSystemComponent(val) => val.links().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::ImplementationResponsibleRole(val) => val.links().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::SspImplementedRequirementResponsibleRole(val) => val.links().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::SspByComponentResponsibleRole(val) => val.links().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::ImplementationResponsibleParty(val) => val.links().map(|x| x.to_any()),
                HasPropsAndLinksOrSubtype::SspSystemCharacteristicsResponsibleParty(val) => val.links().map(|x| x.to_any()),

        }
    }
}
impl HasPropsAndLinks for crate::OscalCommonOrSubtype {
        fn props(&self) -> Option<Vec<has_props_and_links_utl::props_range>> {
        match self {
                OscalCommonOrSubtype::Metadata(val) => val.props().map(|x| x.to_any()),
                OscalCommonOrSubtype::Revision(val) => val.props().map(|x| x.to_any()),
                OscalCommonOrSubtype::Role(val) => val.props().map(|x| x.to_any()),
                OscalCommonOrSubtype::Location(val) => val.props().map(|x| x.to_any()),
                OscalCommonOrSubtype::Party(val) => val.props().map(|x| x.to_any()),
                OscalCommonOrSubtype::ResponsibleParty(val) => val.props().map(|x| x.to_any()),
                OscalCommonOrSubtype::ResponsibleRole(val) => val.props().map(|x| x.to_any()),
                OscalCommonOrSubtype::Action(val) => val.props().map(|x| x.to_any()),
                OscalCommonOrSubtype::Parameter(val) => val.props().map(|x| x.to_any()),
                OscalCommonOrSubtype::ProfileGroup(val) => val.props().map(|x| x.to_any()),
                OscalCommonOrSubtype::ReviewedControls(val) => val.props().map(|x| x.to_any()),
                OscalCommonOrSubtype::ControlSelection(val) => val.props().map(|x| x.to_any()),
                OscalCommonOrSubtype::ControlObjectiveSelection(val) => val.props().map(|x| x.to_any()),
                OscalCommonOrSubtype::AssessmentSubject(val) => val.props().map(|x| x.to_any()),
                OscalCommonOrSubtype::SelectSubjectById(val) => val.props().map(|x| x.to_any()),
                OscalCommonOrSubtype::SubjectReference(val) => val.props().map(|x| x.to_any()),
                OscalCommonOrSubtype::AssessmentSubjectPlaceholder(val) => val.props().map(|x| x.to_any()),
                OscalCommonOrSubtype::AssessmentPlatform(val) => val.props().map(|x| x.to_any()),
                OscalCommonOrSubtype::UsesComponent(val) => val.props().map(|x| x.to_any()),
                OscalCommonOrSubtype::LocalObjective(val) => val.props().map(|x| x.to_any()),
                OscalCommonOrSubtype::AssessmentMethod(val) => val.props().map(|x| x.to_any()),
                OscalCommonOrSubtype::Activity(val) => val.props().map(|x| x.to_any()),
                OscalCommonOrSubtype::Step(val) => val.props().map(|x| x.to_any()),
                OscalCommonOrSubtype::Task(val) => val.props().map(|x| x.to_any()),
                OscalCommonOrSubtype::AssociatedActivity(val) => val.props().map(|x| x.to_any()),
                OscalCommonOrSubtype::SystemComponent(val) => val.props().map(|x| x.to_any()),
                OscalCommonOrSubtype::SystemUser(val) => val.props().map(|x| x.to_any()),
                OscalCommonOrSubtype::InventoryItem(val) => val.props().map(|x| x.to_any()),
                OscalCommonOrSubtype::ImplementedComponent(val) => val.props().map(|x| x.to_any()),
                OscalCommonOrSubtype::RelatedTask(val) => val.props().map(|x| x.to_any()),
                OscalCommonOrSubtype::Observation(val) => val.props().map(|x| x.to_any()),
                OscalCommonOrSubtype::RelevantEvidence(val) => val.props().map(|x| x.to_any()),
                OscalCommonOrSubtype::Finding(val) => val.props().map(|x| x.to_any()),
                OscalCommonOrSubtype::FindingTarget(val) => val.props().map(|x| x.to_any()),
                OscalCommonOrSubtype::Facet(val) => val.props().map(|x| x.to_any()),
                OscalCommonOrSubtype::Response(val) => val.props().map(|x| x.to_any()),
                OscalCommonOrSubtype::RequiredAsset(val) => val.props().map(|x| x.to_any()),
                OscalCommonOrSubtype::RiskLogEntry(val) => val.props().map(|x| x.to_any()),
                OscalCommonOrSubtype::RiskResponseReference(val) => val.props().map(|x| x.to_any()),
                OscalCommonOrSubtype::Result(val) => val.props().map(|x| x.to_any()),
                OscalCommonOrSubtype::AssessmentLogEntry(val) => val.props().map(|x| x.to_any()),
                OscalCommonOrSubtype::DefinedComponent(val) => val.props().map(|x| x.to_any()),
                OscalCommonOrSubtype::Capability(val) => val.props().map(|x| x.to_any()),
                OscalCommonOrSubtype::MappingProvenance(val) => val.props().map(|x| x.to_any()),
                OscalCommonOrSubtype::Mapping(val) => val.props().map(|x| x.to_any()),
                OscalCommonOrSubtype::Map(val) => val.props().map(|x| x.to_any()),
                OscalCommonOrSubtype::MappingItem(val) => val.props().map(|x| x.to_any()),
                OscalCommonOrSubtype::MappingResourceReference(val) => val.props().map(|x| x.to_any()),
                OscalCommonOrSubtype::PoamItem(val) => val.props().map(|x| x.to_any()),
                OscalCommonOrSubtype::SspInventoryItem(val) => val.props().map(|x| x.to_any()),
                OscalCommonOrSubtype::SspSystemComponent(val) => val.props().map(|x| x.to_any()),
                OscalCommonOrSubtype::ImplementationResponsibleRole(val) => val.props().map(|x| x.to_any()),
                OscalCommonOrSubtype::SspImplementedRequirementResponsibleRole(val) => val.props().map(|x| x.to_any()),
                OscalCommonOrSubtype::SspByComponentResponsibleRole(val) => val.props().map(|x| x.to_any()),
                OscalCommonOrSubtype::ImplementationResponsibleParty(val) => val.props().map(|x| x.to_any()),
                OscalCommonOrSubtype::SspSystemCharacteristicsResponsibleParty(val) => val.props().map(|x| x.to_any()),

        }
    }
        fn links(&self) -> Option<Vec<has_props_and_links_utl::links_range>> {
        match self {
                OscalCommonOrSubtype::Metadata(val) => val.links().map(|x| x.to_any()),
                OscalCommonOrSubtype::Revision(val) => val.links().map(|x| x.to_any()),
                OscalCommonOrSubtype::Role(val) => val.links().map(|x| x.to_any()),
                OscalCommonOrSubtype::Location(val) => val.links().map(|x| x.to_any()),
                OscalCommonOrSubtype::Party(val) => val.links().map(|x| x.to_any()),
                OscalCommonOrSubtype::ResponsibleParty(val) => val.links().map(|x| x.to_any()),
                OscalCommonOrSubtype::ResponsibleRole(val) => val.links().map(|x| x.to_any()),
                OscalCommonOrSubtype::Action(val) => val.links().map(|x| x.to_any()),
                OscalCommonOrSubtype::Parameter(val) => val.links().map(|x| x.to_any()),
                OscalCommonOrSubtype::ProfileGroup(val) => val.links().map(|x| x.to_any()),
                OscalCommonOrSubtype::ReviewedControls(val) => val.links().map(|x| x.to_any()),
                OscalCommonOrSubtype::ControlSelection(val) => val.links().map(|x| x.to_any()),
                OscalCommonOrSubtype::ControlObjectiveSelection(val) => val.links().map(|x| x.to_any()),
                OscalCommonOrSubtype::AssessmentSubject(val) => val.links().map(|x| x.to_any()),
                OscalCommonOrSubtype::SelectSubjectById(val) => val.links().map(|x| x.to_any()),
                OscalCommonOrSubtype::SubjectReference(val) => val.links().map(|x| x.to_any()),
                OscalCommonOrSubtype::AssessmentSubjectPlaceholder(val) => val.links().map(|x| x.to_any()),
                OscalCommonOrSubtype::AssessmentPlatform(val) => val.links().map(|x| x.to_any()),
                OscalCommonOrSubtype::UsesComponent(val) => val.links().map(|x| x.to_any()),
                OscalCommonOrSubtype::LocalObjective(val) => val.links().map(|x| x.to_any()),
                OscalCommonOrSubtype::AssessmentMethod(val) => val.links().map(|x| x.to_any()),
                OscalCommonOrSubtype::Activity(val) => val.links().map(|x| x.to_any()),
                OscalCommonOrSubtype::Step(val) => val.links().map(|x| x.to_any()),
                OscalCommonOrSubtype::Task(val) => val.links().map(|x| x.to_any()),
                OscalCommonOrSubtype::AssociatedActivity(val) => val.links().map(|x| x.to_any()),
                OscalCommonOrSubtype::SystemComponent(val) => val.links().map(|x| x.to_any()),
                OscalCommonOrSubtype::SystemUser(val) => val.links().map(|x| x.to_any()),
                OscalCommonOrSubtype::InventoryItem(val) => val.links().map(|x| x.to_any()),
                OscalCommonOrSubtype::ImplementedComponent(val) => val.links().map(|x| x.to_any()),
                OscalCommonOrSubtype::RelatedTask(val) => val.links().map(|x| x.to_any()),
                OscalCommonOrSubtype::Observation(val) => val.links().map(|x| x.to_any()),
                OscalCommonOrSubtype::RelevantEvidence(val) => val.links().map(|x| x.to_any()),
                OscalCommonOrSubtype::Finding(val) => val.links().map(|x| x.to_any()),
                OscalCommonOrSubtype::FindingTarget(val) => val.links().map(|x| x.to_any()),
                OscalCommonOrSubtype::Facet(val) => val.links().map(|x| x.to_any()),
                OscalCommonOrSubtype::Response(val) => val.links().map(|x| x.to_any()),
                OscalCommonOrSubtype::RequiredAsset(val) => val.links().map(|x| x.to_any()),
                OscalCommonOrSubtype::RiskLogEntry(val) => val.links().map(|x| x.to_any()),
                OscalCommonOrSubtype::RiskResponseReference(val) => val.links().map(|x| x.to_any()),
                OscalCommonOrSubtype::Result(val) => val.links().map(|x| x.to_any()),
                OscalCommonOrSubtype::AssessmentLogEntry(val) => val.links().map(|x| x.to_any()),
                OscalCommonOrSubtype::DefinedComponent(val) => val.links().map(|x| x.to_any()),
                OscalCommonOrSubtype::Capability(val) => val.links().map(|x| x.to_any()),
                OscalCommonOrSubtype::MappingProvenance(val) => val.links().map(|x| x.to_any()),
                OscalCommonOrSubtype::Mapping(val) => val.links().map(|x| x.to_any()),
                OscalCommonOrSubtype::Map(val) => val.links().map(|x| x.to_any()),
                OscalCommonOrSubtype::MappingItem(val) => val.links().map(|x| x.to_any()),
                OscalCommonOrSubtype::MappingResourceReference(val) => val.links().map(|x| x.to_any()),
                OscalCommonOrSubtype::PoamItem(val) => val.links().map(|x| x.to_any()),
                OscalCommonOrSubtype::SspInventoryItem(val) => val.links().map(|x| x.to_any()),
                OscalCommonOrSubtype::SspSystemComponent(val) => val.links().map(|x| x.to_any()),
                OscalCommonOrSubtype::ImplementationResponsibleRole(val) => val.links().map(|x| x.to_any()),
                OscalCommonOrSubtype::SspImplementedRequirementResponsibleRole(val) => val.links().map(|x| x.to_any()),
                OscalCommonOrSubtype::SspByComponentResponsibleRole(val) => val.links().map(|x| x.to_any()),
                OscalCommonOrSubtype::ImplementationResponsibleParty(val) => val.links().map(|x| x.to_any()),
                OscalCommonOrSubtype::SspSystemCharacteristicsResponsibleParty(val) => val.links().map(|x| x.to_any()),

        }
    }
}
impl HasPropsAndLinks for crate::AssessmentPartOrSubtype {
        fn props(&self) -> Option<Vec<has_props_and_links_utl::props_range>> {
        match self {
                AssessmentPartOrSubtype::TermsAndConditionsPart(val) => val.props().map(|x| x.to_any()),

        }
    }
        fn links(&self) -> Option<Vec<has_props_and_links_utl::links_range>> {
        match self {
                AssessmentPartOrSubtype::TermsAndConditionsPart(val) => val.links().map(|x| x.to_any()),

        }
    }
}
impl HasPropsAndLinks for crate::ResponsiblePartyOrSubtype {
        fn props(&self) -> Option<Vec<has_props_and_links_utl::props_range>> {
        match self {
                ResponsiblePartyOrSubtype::ImplementationResponsibleParty(val) => val.props().map(|x| x.to_any()),
                ResponsiblePartyOrSubtype::SspSystemCharacteristicsResponsibleParty(val) => val.props().map(|x| x.to_any()),

        }
    }
        fn links(&self) -> Option<Vec<has_props_and_links_utl::links_range>> {
        match self {
                ResponsiblePartyOrSubtype::ImplementationResponsibleParty(val) => val.links().map(|x| x.to_any()),
                ResponsiblePartyOrSubtype::SspSystemCharacteristicsResponsibleParty(val) => val.links().map(|x| x.to_any()),

        }
    }
}
impl HasPropsAndLinks for crate::ResponsibleRoleOrSubtype {
        fn props(&self) -> Option<Vec<has_props_and_links_utl::props_range>> {
        match self {
                ResponsibleRoleOrSubtype::ImplementationResponsibleRole(val) => val.props().map(|x| x.to_any()),
                ResponsibleRoleOrSubtype::SspImplementedRequirementResponsibleRole(val) => val.props().map(|x| x.to_any()),
                ResponsibleRoleOrSubtype::SspByComponentResponsibleRole(val) => val.props().map(|x| x.to_any()),

        }
    }
        fn links(&self) -> Option<Vec<has_props_and_links_utl::links_range>> {
        match self {
                ResponsibleRoleOrSubtype::ImplementationResponsibleRole(val) => val.links().map(|x| x.to_any()),
                ResponsibleRoleOrSubtype::SspImplementedRequirementResponsibleRole(val) => val.links().map(|x| x.to_any()),
                ResponsibleRoleOrSubtype::SspByComponentResponsibleRole(val) => val.links().map(|x| x.to_any()),

        }
    }
}
impl HasPropsAndLinks for crate::SystemComponentOrSubtype {
        fn props(&self) -> Option<Vec<has_props_and_links_utl::props_range>> {
        match self {
                SystemComponentOrSubtype::SspSystemComponent(val) => val.props().map(|x| x.to_any()),

        }
    }
        fn links(&self) -> Option<Vec<has_props_and_links_utl::links_range>> {
        match self {
                SystemComponentOrSubtype::SspSystemComponent(val) => val.links().map(|x| x.to_any()),

        }
    }
}
impl HasPropsAndLinks for crate::InventoryItemOrSubtype {
        fn props(&self) -> Option<Vec<has_props_and_links_utl::props_range>> {
        match self {
                InventoryItemOrSubtype::SspInventoryItem(val) => val.props().map(|x| x.to_any()),

        }
    }
        fn links(&self) -> Option<Vec<has_props_and_links_utl::links_range>> {
        match self {
                InventoryItemOrSubtype::SspInventoryItem(val) => val.links().map(|x| x.to_any()),

        }
    }
}

pub trait OscalCommon : HasPropsAndLinks   {

    fn remarks<'a>(&'a self) -> Option<&'a str>;
    // fn remarks_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_remarks(&mut self, value: Option<&'a str>);


}

impl OscalCommon for crate::OscalCommon {
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}
impl OscalCommon for crate::Metadata {
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}
impl OscalCommon for crate::Revision {
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}
impl OscalCommon for crate::Role {
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}
impl OscalCommon for crate::Location {
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}
impl OscalCommon for crate::Party {
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}
impl OscalCommon for crate::ResponsibleParty {
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}
impl OscalCommon for crate::ResponsibleRole {
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}
impl OscalCommon for crate::Action {
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}
impl OscalCommon for crate::Parameter {
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}
impl OscalCommon for crate::ProfileGroup {
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}
impl OscalCommon for crate::ReviewedControls {
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}
impl OscalCommon for crate::ControlSelection {
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}
impl OscalCommon for crate::ControlObjectiveSelection {
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}
impl OscalCommon for crate::AssessmentSubject {
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}
impl OscalCommon for crate::SelectSubjectById {
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}
impl OscalCommon for crate::SubjectReference {
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}
impl OscalCommon for crate::AssessmentSubjectPlaceholder {
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}
impl OscalCommon for crate::AssessmentPlatform {
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}
impl OscalCommon for crate::UsesComponent {
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}
impl OscalCommon for crate::LocalObjective {
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}
impl OscalCommon for crate::AssessmentMethod {
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}
impl OscalCommon for crate::Activity {
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}
impl OscalCommon for crate::Step {
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}
impl OscalCommon for crate::Task {
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}
impl OscalCommon for crate::AssociatedActivity {
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}
impl OscalCommon for crate::SystemComponent {
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}
impl OscalCommon for crate::SystemUser {
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}
impl OscalCommon for crate::InventoryItem {
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}
impl OscalCommon for crate::ImplementedComponent {
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}
impl OscalCommon for crate::RelatedTask {
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}
impl OscalCommon for crate::Observation {
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}
impl OscalCommon for crate::RelevantEvidence {
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}
impl OscalCommon for crate::Finding {
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}
impl OscalCommon for crate::FindingTarget {
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}
impl OscalCommon for crate::Facet {
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}
impl OscalCommon for crate::Response {
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}
impl OscalCommon for crate::RequiredAsset {
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}
impl OscalCommon for crate::RiskLogEntry {
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}
impl OscalCommon for crate::RiskResponseReference {
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}
impl OscalCommon for crate::Result {
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}
impl OscalCommon for crate::AssessmentLogEntry {
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}
impl OscalCommon for crate::DefinedComponent {
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}
impl OscalCommon for crate::Capability {
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}
impl OscalCommon for crate::MappingProvenance {
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}
impl OscalCommon for crate::Mapping {
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}
impl OscalCommon for crate::Map {
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}
impl OscalCommon for crate::MappingItem {
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}
impl OscalCommon for crate::MappingResourceReference {
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}
impl OscalCommon for crate::PoamItem {
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}
impl OscalCommon for crate::SspInventoryItem {
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}
impl OscalCommon for crate::SspSystemComponent {
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}
impl OscalCommon for crate::ImplementationResponsibleRole {
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}
impl OscalCommon for crate::SspImplementedRequirementResponsibleRole {
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}
impl OscalCommon for crate::SspByComponentResponsibleRole {
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}
impl OscalCommon for crate::ImplementationResponsibleParty {
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}
impl OscalCommon for crate::SspSystemCharacteristicsResponsibleParty {
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}

impl OscalCommon for crate::OscalCommonOrSubtype {
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        match self {
                OscalCommonOrSubtype::Metadata(val) => val.remarks(),
                OscalCommonOrSubtype::Revision(val) => val.remarks(),
                OscalCommonOrSubtype::Role(val) => val.remarks(),
                OscalCommonOrSubtype::Location(val) => val.remarks(),
                OscalCommonOrSubtype::Party(val) => val.remarks(),
                OscalCommonOrSubtype::ResponsibleParty(val) => val.remarks(),
                OscalCommonOrSubtype::ResponsibleRole(val) => val.remarks(),
                OscalCommonOrSubtype::Action(val) => val.remarks(),
                OscalCommonOrSubtype::Parameter(val) => val.remarks(),
                OscalCommonOrSubtype::ProfileGroup(val) => val.remarks(),
                OscalCommonOrSubtype::ReviewedControls(val) => val.remarks(),
                OscalCommonOrSubtype::ControlSelection(val) => val.remarks(),
                OscalCommonOrSubtype::ControlObjectiveSelection(val) => val.remarks(),
                OscalCommonOrSubtype::AssessmentSubject(val) => val.remarks(),
                OscalCommonOrSubtype::SelectSubjectById(val) => val.remarks(),
                OscalCommonOrSubtype::SubjectReference(val) => val.remarks(),
                OscalCommonOrSubtype::AssessmentSubjectPlaceholder(val) => val.remarks(),
                OscalCommonOrSubtype::AssessmentPlatform(val) => val.remarks(),
                OscalCommonOrSubtype::UsesComponent(val) => val.remarks(),
                OscalCommonOrSubtype::LocalObjective(val) => val.remarks(),
                OscalCommonOrSubtype::AssessmentMethod(val) => val.remarks(),
                OscalCommonOrSubtype::Activity(val) => val.remarks(),
                OscalCommonOrSubtype::Step(val) => val.remarks(),
                OscalCommonOrSubtype::Task(val) => val.remarks(),
                OscalCommonOrSubtype::AssociatedActivity(val) => val.remarks(),
                OscalCommonOrSubtype::SystemComponent(val) => val.remarks(),
                OscalCommonOrSubtype::SystemUser(val) => val.remarks(),
                OscalCommonOrSubtype::InventoryItem(val) => val.remarks(),
                OscalCommonOrSubtype::ImplementedComponent(val) => val.remarks(),
                OscalCommonOrSubtype::RelatedTask(val) => val.remarks(),
                OscalCommonOrSubtype::Observation(val) => val.remarks(),
                OscalCommonOrSubtype::RelevantEvidence(val) => val.remarks(),
                OscalCommonOrSubtype::Finding(val) => val.remarks(),
                OscalCommonOrSubtype::FindingTarget(val) => val.remarks(),
                OscalCommonOrSubtype::Facet(val) => val.remarks(),
                OscalCommonOrSubtype::Response(val) => val.remarks(),
                OscalCommonOrSubtype::RequiredAsset(val) => val.remarks(),
                OscalCommonOrSubtype::RiskLogEntry(val) => val.remarks(),
                OscalCommonOrSubtype::RiskResponseReference(val) => val.remarks(),
                OscalCommonOrSubtype::Result(val) => val.remarks(),
                OscalCommonOrSubtype::AssessmentLogEntry(val) => val.remarks(),
                OscalCommonOrSubtype::DefinedComponent(val) => val.remarks(),
                OscalCommonOrSubtype::Capability(val) => val.remarks(),
                OscalCommonOrSubtype::MappingProvenance(val) => val.remarks(),
                OscalCommonOrSubtype::Mapping(val) => val.remarks(),
                OscalCommonOrSubtype::Map(val) => val.remarks(),
                OscalCommonOrSubtype::MappingItem(val) => val.remarks(),
                OscalCommonOrSubtype::MappingResourceReference(val) => val.remarks(),
                OscalCommonOrSubtype::PoamItem(val) => val.remarks(),
                OscalCommonOrSubtype::SspInventoryItem(val) => val.remarks(),
                OscalCommonOrSubtype::SspSystemComponent(val) => val.remarks(),
                OscalCommonOrSubtype::ImplementationResponsibleRole(val) => val.remarks(),
                OscalCommonOrSubtype::SspImplementedRequirementResponsibleRole(val) => val.remarks(),
                OscalCommonOrSubtype::SspByComponentResponsibleRole(val) => val.remarks(),
                OscalCommonOrSubtype::ImplementationResponsibleParty(val) => val.remarks(),
                OscalCommonOrSubtype::SspSystemCharacteristicsResponsibleParty(val) => val.remarks(),

        }
    }
}
impl OscalCommon for crate::ResponsiblePartyOrSubtype {
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        match self {
                ResponsiblePartyOrSubtype::ImplementationResponsibleParty(val) => val.remarks(),
                ResponsiblePartyOrSubtype::SspSystemCharacteristicsResponsibleParty(val) => val.remarks(),

        }
    }
}
impl OscalCommon for crate::ResponsibleRoleOrSubtype {
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        match self {
                ResponsibleRoleOrSubtype::ImplementationResponsibleRole(val) => val.remarks(),
                ResponsibleRoleOrSubtype::SspImplementedRequirementResponsibleRole(val) => val.remarks(),
                ResponsibleRoleOrSubtype::SspByComponentResponsibleRole(val) => val.remarks(),

        }
    }
}
impl OscalCommon for crate::SystemComponentOrSubtype {
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        match self {
                SystemComponentOrSubtype::SspSystemComponent(val) => val.remarks(),

        }
    }
}
impl OscalCommon for crate::InventoryItemOrSubtype {
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        match self {
                InventoryItemOrSubtype::SspInventoryItem(val) => val.remarks(),

        }
    }
}

pub trait HasResponsibleRoles   {

    fn responsible_roles(&self) -> Option<Vec<has_responsible_roles_utl::responsible_roles_range>>;
    // fn responsible_roles_mut(&mut self) -> &mut Option<Vec<has_responsible_roles_utl::responsible_roles_range>>;
    // fn set_responsible_roles<E>(&mut self, value: Option<&Vec<E>>) where E: Into<ResponsibleRole>;


}

impl HasResponsibleRoles for crate::HasResponsibleRoles {
        fn responsible_roles(&self) -> Option<Vec<has_responsible_roles_utl::responsible_roles_range>> {
        self.responsible_roles.as_ref().map(|xs| xs.iter().map(|v| has_responsible_roles_utl::responsible_roles_range::ResponsibleRole(v.clone())).collect())
    }
}
impl HasResponsibleRoles for crate::Activity {
        fn responsible_roles(&self) -> Option<Vec<has_responsible_roles_utl::responsible_roles_range>> {
        self.responsible_roles.as_ref().map(|xs| xs.iter().map(|v| has_responsible_roles_utl::responsible_roles_range::ResponsibleRole(v.clone())).collect())
    }
}
impl HasResponsibleRoles for crate::Step {
        fn responsible_roles(&self) -> Option<Vec<has_responsible_roles_utl::responsible_roles_range>> {
        self.responsible_roles.as_ref().map(|xs| xs.iter().map(|v| has_responsible_roles_utl::responsible_roles_range::ResponsibleRole(v.clone())).collect())
    }
}
impl HasResponsibleRoles for crate::Task {
        fn responsible_roles(&self) -> Option<Vec<has_responsible_roles_utl::responsible_roles_range>> {
        self.responsible_roles.as_ref().map(|xs| xs.iter().map(|v| has_responsible_roles_utl::responsible_roles_range::ResponsibleRole(v.clone())).collect())
    }
}
impl HasResponsibleRoles for crate::AssociatedActivity {
        fn responsible_roles(&self) -> Option<Vec<has_responsible_roles_utl::responsible_roles_range>> {
        self.responsible_roles.as_ref().map(|xs| xs.iter().map(|v| has_responsible_roles_utl::responsible_roles_range::ResponsibleRole(v.clone())).collect())
    }
}
impl HasResponsibleRoles for crate::SystemComponent {
        fn responsible_roles(&self) -> Option<Vec<has_responsible_roles_utl::responsible_roles_range>> {
        self.responsible_roles.as_ref().map(|xs| xs.iter().map(|v| has_responsible_roles_utl::responsible_roles_range::ImplementationResponsibleRole(v.clone())).collect())
    }
}
impl HasResponsibleRoles for crate::DefinedComponent {
        fn responsible_roles(&self) -> Option<Vec<has_responsible_roles_utl::responsible_roles_range>> {
        self.responsible_roles.as_ref().map(|xs| xs.iter().map(|v| has_responsible_roles_utl::responsible_roles_range::ResponsibleRole(v.clone())).collect())
    }
}
impl HasResponsibleRoles for crate::ImplementedRequirement {
        fn responsible_roles(&self) -> Option<Vec<has_responsible_roles_utl::responsible_roles_range>> {
        self.responsible_roles.as_ref().map(|xs| xs.iter().map(|v| has_responsible_roles_utl::responsible_roles_range::ResponsibleRole(v.clone())).collect())
    }
}
impl HasResponsibleRoles for crate::ImplementedControlStatement {
        fn responsible_roles(&self) -> Option<Vec<has_responsible_roles_utl::responsible_roles_range>> {
        self.responsible_roles.as_ref().map(|xs| xs.iter().map(|v| has_responsible_roles_utl::responsible_roles_range::ResponsibleRole(v.clone())).collect())
    }
}
impl HasResponsibleRoles for crate::SspSystemComponent {
        fn responsible_roles(&self) -> Option<Vec<has_responsible_roles_utl::responsible_roles_range>> {
        self.responsible_roles.as_ref().map(|xs| xs.iter().map(|v| has_responsible_roles_utl::responsible_roles_range::ImplementationResponsibleRole(v.clone())).collect())
    }
}

impl HasResponsibleRoles for crate::HasResponsibleRolesOrSubtype {
        fn responsible_roles(&self) -> Option<Vec<has_responsible_roles_utl::responsible_roles_range>> {
        match self {
                HasResponsibleRolesOrSubtype::Activity(val) => val.responsible_roles().map(|x| x.to_any()),
                HasResponsibleRolesOrSubtype::Step(val) => val.responsible_roles().map(|x| x.to_any()),
                HasResponsibleRolesOrSubtype::Task(val) => val.responsible_roles().map(|x| x.to_any()),
                HasResponsibleRolesOrSubtype::AssociatedActivity(val) => val.responsible_roles().map(|x| x.to_any()),
                HasResponsibleRolesOrSubtype::SystemComponent(val) => val.responsible_roles().map(|x| x.to_any()),
                HasResponsibleRolesOrSubtype::DefinedComponent(val) => val.responsible_roles().map(|x| x.to_any()),
                HasResponsibleRolesOrSubtype::ImplementedRequirement(val) => val.responsible_roles().map(|x| x.to_any()),
                HasResponsibleRolesOrSubtype::ImplementedControlStatement(val) => val.responsible_roles().map(|x| x.to_any()),
                HasResponsibleRolesOrSubtype::SspSystemComponent(val) => val.responsible_roles().map(|x| x.to_any()),

        }
    }
}
impl HasResponsibleRoles for crate::SystemComponentOrSubtype {
        fn responsible_roles(&self) -> Option<Vec<has_responsible_roles_utl::responsible_roles_range>> {
        match self {
                SystemComponentOrSubtype::SspSystemComponent(val) => val.responsible_roles().map(|x| x.to_any()),

        }
    }
}

pub trait HasResponsibleParties   {

    fn responsible_parties(&self) -> Option<Vec<has_responsible_parties_utl::responsible_parties_range>>;
    // fn responsible_parties_mut(&mut self) -> &mut Option<Vec<has_responsible_parties_utl::responsible_parties_range>>;
    // fn set_responsible_parties<E>(&mut self, value: Option<&Vec<E>>) where E: Into<ResponsibleParty>;


}

impl HasResponsibleParties for crate::HasResponsibleParties {
        fn responsible_parties(&self) -> Option<Vec<has_responsible_parties_utl::responsible_parties_range>> {
        self.responsible_parties.as_ref().map(|xs| xs.iter().map(|v| has_responsible_parties_utl::responsible_parties_range::ResponsibleParty(v.clone())).collect())
    }
}
impl HasResponsibleParties for crate::Metadata {
        fn responsible_parties(&self) -> Option<Vec<has_responsible_parties_utl::responsible_parties_range>> {
        self.responsible_parties.as_ref().map(|xs| xs.iter().map(|v| has_responsible_parties_utl::responsible_parties_range::ResponsibleParty(v.clone())).collect())
    }
}
impl HasResponsibleParties for crate::Action {
        fn responsible_parties(&self) -> Option<Vec<has_responsible_parties_utl::responsible_parties_range>> {
        self.responsible_parties.as_ref().map(|xs| xs.iter().map(|v| has_responsible_parties_utl::responsible_parties_range::ResponsibleParty(v.clone())).collect())
    }
}
impl HasResponsibleParties for crate::UsesComponent {
        fn responsible_parties(&self) -> Option<Vec<has_responsible_parties_utl::responsible_parties_range>> {
        self.responsible_parties.as_ref().map(|xs| xs.iter().map(|v| has_responsible_parties_utl::responsible_parties_range::ResponsibleParty(v.clone())).collect())
    }
}
impl HasResponsibleParties for crate::InventoryItem {
        fn responsible_parties(&self) -> Option<Vec<has_responsible_parties_utl::responsible_parties_range>> {
        self.responsible_parties.as_ref().map(|xs| xs.iter().map(|v| has_responsible_parties_utl::responsible_parties_range::ImplementationResponsibleParty(v.clone())).collect())
    }
}
impl HasResponsibleParties for crate::ImplementedComponent {
        fn responsible_parties(&self) -> Option<Vec<has_responsible_parties_utl::responsible_parties_range>> {
        self.responsible_parties.as_ref().map(|xs| xs.iter().map(|v| has_responsible_parties_utl::responsible_parties_range::ImplementationResponsibleParty(v.clone())).collect())
    }
}
impl HasResponsibleParties for crate::RelatedTask {
        fn responsible_parties(&self) -> Option<Vec<has_responsible_parties_utl::responsible_parties_range>> {
        self.responsible_parties.as_ref().map(|xs| xs.iter().map(|v| has_responsible_parties_utl::responsible_parties_range::ResponsibleParty(v.clone())).collect())
    }
}
impl HasResponsibleParties for crate::Attestation {
        fn responsible_parties(&self) -> Option<Vec<has_responsible_parties_utl::responsible_parties_range>> {
        self.responsible_parties.as_ref().map(|xs| xs.iter().map(|v| has_responsible_parties_utl::responsible_parties_range::ResponsibleParty(v.clone())).collect())
    }
}
impl HasResponsibleParties for crate::MappingProvenance {
        fn responsible_parties(&self) -> Option<Vec<has_responsible_parties_utl::responsible_parties_range>> {
        self.responsible_parties.as_ref().map(|xs| xs.iter().map(|v| has_responsible_parties_utl::responsible_parties_range::ResponsibleParty(v.clone())).collect())
    }
}
impl HasResponsibleParties for crate::SspInventoryItem {
        fn responsible_parties(&self) -> Option<Vec<has_responsible_parties_utl::responsible_parties_range>> {
        self.responsible_parties.as_ref().map(|xs| xs.iter().map(|v| has_responsible_parties_utl::responsible_parties_range::ImplementationResponsibleParty(v.clone())).collect())
    }
}

impl HasResponsibleParties for crate::HasResponsiblePartiesOrSubtype {
        fn responsible_parties(&self) -> Option<Vec<has_responsible_parties_utl::responsible_parties_range>> {
        match self {
                HasResponsiblePartiesOrSubtype::Metadata(val) => val.responsible_parties().map(|x| x.to_any()),
                HasResponsiblePartiesOrSubtype::Action(val) => val.responsible_parties().map(|x| x.to_any()),
                HasResponsiblePartiesOrSubtype::UsesComponent(val) => val.responsible_parties().map(|x| x.to_any()),
                HasResponsiblePartiesOrSubtype::InventoryItem(val) => val.responsible_parties().map(|x| x.to_any()),
                HasResponsiblePartiesOrSubtype::ImplementedComponent(val) => val.responsible_parties().map(|x| x.to_any()),
                HasResponsiblePartiesOrSubtype::RelatedTask(val) => val.responsible_parties().map(|x| x.to_any()),
                HasResponsiblePartiesOrSubtype::Attestation(val) => val.responsible_parties().map(|x| x.to_any()),
                HasResponsiblePartiesOrSubtype::MappingProvenance(val) => val.responsible_parties().map(|x| x.to_any()),
                HasResponsiblePartiesOrSubtype::SspInventoryItem(val) => val.responsible_parties().map(|x| x.to_any()),

        }
    }
}
impl HasResponsibleParties for crate::InventoryItemOrSubtype {
        fn responsible_parties(&self) -> Option<Vec<has_responsible_parties_utl::responsible_parties_range>> {
        match self {
                InventoryItemOrSubtype::SspInventoryItem(val) => val.responsible_parties().map(|x| x.to_any()),

        }
    }
}

pub trait OscalDocument   {


}

impl OscalDocument for crate::OscalDocument {
}
impl OscalDocument for crate::CatalogDocument {
}
impl OscalDocument for crate::ProfileDocument {
}
impl OscalDocument for crate::AssessmentPlanDocument {
}
impl OscalDocument for crate::SspDocument {
}
impl OscalDocument for crate::AssessmentResultsDocument {
}
impl OscalDocument for crate::ComponentDefinitionDocument {
}
impl OscalDocument for crate::MappingCollectionDocument {
}
impl OscalDocument for crate::PoamDocument {
}

impl OscalDocument for crate::OscalDocumentOrSubtype {
}

pub trait CatalogDocument : OscalDocument   {

    fn catalog<'a>(&'a self) -> &'a crate::Catalog;
    // fn catalog_mut(&mut self) -> &mut &'a crate::Catalog;
    // fn set_catalog<E>(&mut self, value: E) where E: Into<Catalog>;


}

impl CatalogDocument for crate::CatalogDocument {
        fn catalog<'a>(&'a self) -> &'a crate::Catalog {
        return &self.catalog;
    }
}


pub trait Catalog   {

    fn uuid<'a>(&'a self) -> &'a str;
    // fn uuid_mut(&mut self) -> &mut &'a str;
    // fn set_uuid(&mut self, value: String);

    fn metadata<'a>(&'a self) -> &'a crate::Metadata;
    // fn metadata_mut(&mut self) -> &mut &'a crate::Metadata;
    // fn set_metadata<E>(&mut self, value: E) where E: Into<Metadata>;

    fn back_matter<'a>(&'a self) -> Option<&'a crate::BackMatter>;
    // fn back_matter_mut(&mut self) -> &mut Option<&'a crate::BackMatter>;
    // fn set_back_matter<E>(&mut self, value: Option<E>) where E: Into<BackMatter>;

    fn params<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Parameter>>;
    // fn params_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::Parameter>>;
    // fn set_params<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Parameter>;

    fn controls<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Control>>;
    // fn controls_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::Control>>;
    // fn set_controls<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Control>;

    fn groups<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Group>>;
    // fn groups_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::Group>>;
    // fn set_groups<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Group>;


}

impl Catalog for crate::Catalog {
        fn uuid<'a>(&'a self) -> &'a str {
        return &self.uuid[..];
    }
        fn metadata<'a>(&'a self) -> &'a crate::Metadata {
        return &self.metadata;
    }
        fn back_matter<'a>(&'a self) -> Option<&'a crate::BackMatter> {
        return self.back_matter.as_ref();
    }
        fn params<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Parameter>> {
        return self.params.as_ref();
    }
        fn controls<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Control>> {
        return self.controls.as_ref();
    }
        fn groups<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Group>> {
        return self.groups.as_ref();
    }
}


pub trait Group : HasPropsAndLinks   {

    fn id<'a>(&'a self) -> Option<&'a str>;
    // fn id_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_id(&mut self, value: Option<&'a str>);

    fn _class<'a>(&'a self) -> Option<&'a str>;
    // fn _class_mut(&mut self) -> &mut Option<&'a str>;
    // fn set__class(&mut self, value: Option<&'a str>);

    fn title<'a>(&'a self) -> &'a str;
    // fn title_mut(&mut self) -> &mut &'a str;
    // fn set_title(&mut self, value: String);

    fn params<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Parameter>>;
    // fn params_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::Parameter>>;
    // fn set_params<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Parameter>;

    fn parts<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Part>>;
    // fn parts_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::Part>>;
    // fn set_parts<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Part>;

    fn groups<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Group>>;
    // fn groups_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::Group>>;
    // fn set_groups<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Group>;

    fn controls<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Control>>;
    // fn controls_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::Control>>;
    // fn set_controls<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Control>;


}

impl Group for crate::Group {
        fn id<'a>(&'a self) -> Option<&'a str> {
        return self.id.as_deref();
    }
        fn _class<'a>(&'a self) -> Option<&'a str> {
        return self._class.as_deref();
    }
        fn title<'a>(&'a self) -> &'a str {
        return &self.title[..];
    }
        fn params<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Parameter>> {
        return self.params.as_ref();
    }
        fn parts<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Part>> {
        return self.parts.as_ref();
    }
        fn groups<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Group>> {
        return self.groups.as_ref().map(|x| poly_containers::ListView::new(x));
    }
        fn controls<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Control>> {
        return self.controls.as_ref();
    }
}


pub trait Control : HasPropsAndLinks   {

    fn id<'a>(&'a self) -> &'a str;
    // fn id_mut(&mut self) -> &mut &'a str;
    // fn set_id(&mut self, value: String);

    fn _class<'a>(&'a self) -> Option<&'a str>;
    // fn _class_mut(&mut self) -> &mut Option<&'a str>;
    // fn set__class(&mut self, value: Option<&'a str>);

    fn title<'a>(&'a self) -> &'a str;
    // fn title_mut(&mut self) -> &mut &'a str;
    // fn set_title(&mut self, value: String);

    fn params<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Parameter>>;
    // fn params_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::Parameter>>;
    // fn set_params<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Parameter>;

    fn parts<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Part>>;
    // fn parts_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::Part>>;
    // fn set_parts<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Part>;

    fn controls<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Control>>;
    // fn controls_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::Control>>;
    // fn set_controls<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Control>;


}

impl Control for crate::Control {
        fn id<'a>(&'a self) -> &'a str {
        return &self.id[..];
    }
        fn _class<'a>(&'a self) -> Option<&'a str> {
        return self._class.as_deref();
    }
        fn title<'a>(&'a self) -> &'a str {
        return &self.title[..];
    }
        fn params<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Parameter>> {
        return self.params.as_ref();
    }
        fn parts<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Part>> {
        return self.parts.as_ref();
    }
        fn controls<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Control>> {
        return self.controls.as_ref().map(|x| poly_containers::ListView::new(x));
    }
}


pub trait Metadata : OscalCommon  +  HasResponsibleParties   {

    fn title<'a>(&'a self) -> &'a str;
    // fn title_mut(&mut self) -> &mut &'a str;
    // fn set_title(&mut self, value: String);

    fn published<'a>(&'a self) -> Option<&'a str>;
    // fn published_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_published(&mut self, value: Option<&'a str>);

    fn last_modified<'a>(&'a self) -> &'a str;
    // fn last_modified_mut(&mut self) -> &mut &'a str;
    // fn set_last_modified(&mut self, value: String);

    fn version<'a>(&'a self) -> &'a str;
    // fn version_mut(&mut self) -> &mut &'a str;
    // fn set_version(&mut self, value: String);

    fn oscal_version<'a>(&'a self) -> &'a str;
    // fn oscal_version_mut(&mut self) -> &mut &'a str;
    // fn set_oscal_version(&mut self, value: String);

    fn document_ids<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::DocumentId>>;
    // fn document_ids_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::DocumentId>>;
    // fn set_document_ids<E>(&mut self, value: Option<&Vec<E>>) where E: Into<DocumentId>;

    fn revisions<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Revision>>;
    // fn revisions_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::Revision>>;
    // fn set_revisions<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Revision>;

    fn roles<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Role>>;
    // fn roles_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::Role>>;
    // fn set_roles<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Role>;

    fn locations<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Location>>;
    // fn locations_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::Location>>;
    // fn set_locations<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Location>;

    fn parties<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Party>>;
    // fn parties_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::Party>>;
    // fn set_parties<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Party>;

    fn actions<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Action>>;
    // fn actions_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::Action>>;
    // fn set_actions<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Action>;


}

impl Metadata for crate::Metadata {
        fn title<'a>(&'a self) -> &'a str {
        return &self.title[..];
    }
        fn published<'a>(&'a self) -> Option<&'a str> {
        return self.published.as_deref();
    }
        fn last_modified<'a>(&'a self) -> &'a str {
        return &self.last_modified[..];
    }
        fn version<'a>(&'a self) -> &'a str {
        return &self.version[..];
    }
        fn oscal_version<'a>(&'a self) -> &'a str {
        return &self.oscal_version[..];
    }
        fn document_ids<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::DocumentId>> {
        return self.document_ids.as_ref();
    }
        fn revisions<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Revision>> {
        return self.revisions.as_ref();
    }
        fn roles<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Role>> {
        return self.roles.as_ref();
    }
        fn locations<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Location>> {
        return self.locations.as_ref();
    }
        fn parties<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Party>> {
        return self.parties.as_ref();
    }
        fn actions<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Action>> {
        return self.actions.as_ref();
    }
}


pub trait Revision : OscalCommon   {

    fn title<'a>(&'a self) -> Option<&'a str>;
    // fn title_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_title(&mut self, value: Option<&'a str>);

    fn published<'a>(&'a self) -> Option<&'a str>;
    // fn published_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_published(&mut self, value: Option<&'a str>);

    fn last_modified<'a>(&'a self) -> Option<&'a str>;
    // fn last_modified_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_last_modified(&mut self, value: Option<&'a str>);

    fn version<'a>(&'a self) -> &'a str;
    // fn version_mut(&mut self) -> &mut &'a str;
    // fn set_version(&mut self, value: String);

    fn oscal_version<'a>(&'a self) -> Option<&'a str>;
    // fn oscal_version_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_oscal_version(&mut self, value: Option<&'a str>);


}

impl Revision for crate::Revision {
        fn title<'a>(&'a self) -> Option<&'a str> {
        return self.title.as_deref();
    }
        fn published<'a>(&'a self) -> Option<&'a str> {
        return self.published.as_deref();
    }
        fn last_modified<'a>(&'a self) -> Option<&'a str> {
        return self.last_modified.as_deref();
    }
        fn version<'a>(&'a self) -> &'a str {
        return &self.version[..];
    }
        fn oscal_version<'a>(&'a self) -> Option<&'a str> {
        return self.oscal_version.as_deref();
    }
}


pub trait DocumentId   {

    fn scheme(&self) -> Option<document_id_utl::scheme_range>;
    // fn scheme_mut(&mut self) -> &mut Option<document_id_utl::scheme_range>;
    // fn set_scheme(&mut self, value: Option<&'a document_id_utl::scheme_range>);

    fn identifier<'a>(&'a self) -> &'a str;
    // fn identifier_mut(&mut self) -> &mut &'a str;
    // fn set_identifier(&mut self, value: String);


}

impl DocumentId for crate::DocumentId {
        fn scheme(&self) -> Option<document_id_utl::scheme_range> {
                self.scheme.as_ref().cloned()
    }
        fn identifier<'a>(&'a self) -> &'a str {
        return &self.identifier[..];
    }
}


pub trait Role : OscalCommon   {

    fn id<'a>(&'a self) -> &'a str;
    // fn id_mut(&mut self) -> &mut &'a str;
    // fn set_id(&mut self, value: String);

    fn title<'a>(&'a self) -> &'a str;
    // fn title_mut(&mut self) -> &mut &'a str;
    // fn set_title(&mut self, value: String);

    fn short_name<'a>(&'a self) -> Option<&'a str>;
    // fn short_name_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_short_name(&mut self, value: Option<&'a str>);

    fn description<'a>(&'a self) -> Option<&'a str>;
    // fn description_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_description(&mut self, value: Option<&'a str>);


}

impl Role for crate::Role {
        fn id<'a>(&'a self) -> &'a str {
        return &self.id[..];
    }
        fn title<'a>(&'a self) -> &'a str {
        return &self.title[..];
    }
        fn short_name<'a>(&'a self) -> Option<&'a str> {
        return self.short_name.as_deref();
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
}


pub trait Location : OscalCommon   {

    fn uuid<'a>(&'a self) -> &'a str;
    // fn uuid_mut(&mut self) -> &mut &'a str;
    // fn set_uuid(&mut self, value: String);

    fn title<'a>(&'a self) -> Option<&'a str>;
    // fn title_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_title(&mut self, value: Option<&'a str>);

    fn email_addresses<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn email_addresses_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_email_addresses(&mut self, value: Option<&Vec<String>>);

    fn telephone_numbers<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::TelephoneNumber>>;
    // fn telephone_numbers_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::TelephoneNumber>>;
    // fn set_telephone_numbers<E>(&mut self, value: Option<&Vec<E>>) where E: Into<TelephoneNumber>;

    fn address<'a>(&'a self) -> Option<&'a crate::Address>;
    // fn address_mut(&mut self) -> &mut Option<&'a crate::Address>;
    // fn set_address<E>(&mut self, value: Option<E>) where E: Into<Address>;

    fn urls<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn urls_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_urls(&mut self, value: Option<&Vec<String>>);


}

impl Location for crate::Location {
        fn uuid<'a>(&'a self) -> &'a str {
        return &self.uuid[..];
    }
        fn title<'a>(&'a self) -> Option<&'a str> {
        return self.title.as_deref();
    }
        fn email_addresses<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.email_addresses.as_ref();
    }
        fn telephone_numbers<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::TelephoneNumber>> {
        return self.telephone_numbers.as_ref();
    }
        fn address<'a>(&'a self) -> Option<&'a crate::Address> {
        return self.address.as_ref();
    }
        fn urls<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.urls.as_ref();
    }
}


pub trait Party : OscalCommon   {

    fn uuid<'a>(&'a self) -> &'a str;
    // fn uuid_mut(&mut self) -> &mut &'a str;
    // fn set_uuid(&mut self, value: String);

    fn type_<'a>(&'a self) -> &'a crate::PartyTypeEnum;
    // fn type__mut(&mut self) -> &mut &'a crate::PartyTypeEnum;
    // fn set_type_(&mut self, value: PartyTypeEnum);

    fn name<'a>(&'a self) -> Option<&'a str>;
    // fn name_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_name(&mut self, value: Option<&'a str>);

    fn short_name<'a>(&'a self) -> Option<&'a str>;
    // fn short_name_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_short_name(&mut self, value: Option<&'a str>);

    fn email_addresses<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn email_addresses_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_email_addresses(&mut self, value: Option<&Vec<String>>);

    fn telephone_numbers<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::TelephoneNumber>>;
    // fn telephone_numbers_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::TelephoneNumber>>;
    // fn set_telephone_numbers<E>(&mut self, value: Option<&Vec<E>>) where E: Into<TelephoneNumber>;

    fn external_ids<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::MetadataPartyExternalId>>;
    // fn external_ids_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::MetadataPartyExternalId>>;
    // fn set_external_ids<E>(&mut self, value: Option<&Vec<E>>) where E: Into<MetadataPartyExternalId>;

    fn addresses<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Address>>;
    // fn addresses_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::Address>>;
    // fn set_addresses<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Address>;

    fn location_uuids<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn location_uuids_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_location_uuids(&mut self, value: Option<&Vec<String>>);

    fn member_of_organizations<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn member_of_organizations_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_member_of_organizations(&mut self, value: Option<&Vec<String>>);


}

impl Party for crate::Party {
        fn uuid<'a>(&'a self) -> &'a str {
        return &self.uuid[..];
    }
        fn type_<'a>(&'a self) -> &'a crate::PartyTypeEnum {
        return &self.type_;
    }
        fn name<'a>(&'a self) -> Option<&'a str> {
        return self.name.as_deref();
    }
        fn short_name<'a>(&'a self) -> Option<&'a str> {
        return self.short_name.as_deref();
    }
        fn email_addresses<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.email_addresses.as_ref();
    }
        fn telephone_numbers<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::TelephoneNumber>> {
        return self.telephone_numbers.as_ref();
    }
        fn external_ids<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::MetadataPartyExternalId>> {
        return self.external_ids.as_ref();
    }
        fn addresses<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Address>> {
        return self.addresses.as_ref();
    }
        fn location_uuids<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.location_uuids.as_ref();
    }
        fn member_of_organizations<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.member_of_organizations.as_ref();
    }
}


pub trait PartyExternalId   {

    fn scheme(&self) -> party_external_id_utl::scheme_range;
    // fn scheme_mut(&mut self) -> &mut party_external_id_utl::scheme_range;
    // fn set_scheme(&mut self, value: party_external_id_utl::scheme_range);

    fn id<'a>(&'a self) -> &'a str;
    // fn id_mut(&mut self) -> &mut &'a str;
    // fn set_id(&mut self, value: String);


}

impl PartyExternalId for crate::PartyExternalId {
        fn scheme(&self) -> party_external_id_utl::scheme_range {
            self.scheme.clone()
    }
        fn id<'a>(&'a self) -> &'a str {
        return &self.id[..];
    }
}
impl PartyExternalId for crate::MetadataPartyExternalId {
        fn scheme(&self) -> party_external_id_utl::scheme_range {
            match &self.scheme {
                metadata_party_external_id_utl::scheme_range::String(x) => party_external_id_utl::scheme_range::String(x.clone()),
                metadata_party_external_id_utl::scheme_range::PartyExternalIdSchemeEnum(x) => party_external_id_utl::scheme_range::PartyExternalIdSchemeEnum(x.clone()),
            }
    }
        fn id<'a>(&'a self) -> &'a str {
        return &self.id[..];
    }
}

impl PartyExternalId for crate::PartyExternalIdOrSubtype {
        fn scheme(&self) -> party_external_id_utl::scheme_range {
        match self {
                PartyExternalIdOrSubtype::MetadataPartyExternalId(val) => val.scheme(),

        }
    }
        fn id<'a>(&'a self) -> &'a str {
        match self {
                PartyExternalIdOrSubtype::MetadataPartyExternalId(val) => val.id(),

        }
    }
}

pub trait ResponsibleParty : OscalCommon   {

    fn role_id(&self) -> responsible_party_utl::role_id_range;
    // fn role_id_mut(&mut self) -> &mut responsible_party_utl::role_id_range;
    // fn set_role_id(&mut self, value: responsible_party_utl::role_id_range);

    fn party_uuids<'a>(&'a self) -> impl poly_containers::SeqRef<'a, String>;
    // fn party_uuids_mut(&mut self) -> &mut impl poly_containers::SeqRef<'a, String>;
    // fn set_party_uuids(&mut self, value: &Vec<String>);


}

impl ResponsibleParty for crate::ResponsibleParty {
        fn role_id(&self) -> responsible_party_utl::role_id_range {
            self.role_id.clone()
    }
        fn party_uuids<'a>(&'a self) -> impl poly_containers::SeqRef<'a, String> {
        return &self.party_uuids;
    }
}
impl ResponsibleParty for crate::ImplementationResponsibleParty {
        fn role_id(&self) -> responsible_party_utl::role_id_range {
            match &self.role_id {
                implementation_responsible_party_utl::role_id_range::String(x) => responsible_party_utl::role_id_range::String(x.clone()),
                implementation_responsible_party_utl::role_id_range::MetadataResponsiblePartyRoleIdEnum(x) => responsible_party_utl::role_id_range::MetadataResponsiblePartyRoleIdEnum(x.clone()),
                implementation_responsible_party_utl::role_id_range::ImplementationResponsibleRoleIdEnum(x) => responsible_party_utl::role_id_range::ImplementationResponsibleRoleIdEnum(x.clone()),
                implementation_responsible_party_utl::role_id_range::SystemCharacteristicsResponsibleRoleIdEnum(x) => responsible_party_utl::role_id_range::SystemCharacteristicsResponsibleRoleIdEnum(x.clone()),
            }
    }
        fn party_uuids<'a>(&'a self) -> impl poly_containers::SeqRef<'a, String> {
        return &self.party_uuids;
    }
}
impl ResponsibleParty for crate::SspSystemCharacteristicsResponsibleParty {
        fn role_id(&self) -> responsible_party_utl::role_id_range {
            match &self.role_id {
                ssp_system_characteristics_responsible_party_utl::role_id_range::String(x) => responsible_party_utl::role_id_range::String(x.clone()),
                ssp_system_characteristics_responsible_party_utl::role_id_range::MetadataResponsiblePartyRoleIdEnum(x) => responsible_party_utl::role_id_range::MetadataResponsiblePartyRoleIdEnum(x.clone()),
                ssp_system_characteristics_responsible_party_utl::role_id_range::ImplementationResponsibleRoleIdEnum(x) => responsible_party_utl::role_id_range::ImplementationResponsibleRoleIdEnum(x.clone()),
                ssp_system_characteristics_responsible_party_utl::role_id_range::SystemCharacteristicsResponsibleRoleIdEnum(x) => responsible_party_utl::role_id_range::SystemCharacteristicsResponsibleRoleIdEnum(x.clone()),
            }
    }
        fn party_uuids<'a>(&'a self) -> impl poly_containers::SeqRef<'a, String> {
        return &self.party_uuids;
    }
}

impl ResponsibleParty for crate::ResponsiblePartyOrSubtype {
        fn role_id(&self) -> responsible_party_utl::role_id_range {
        match self {
                ResponsiblePartyOrSubtype::ImplementationResponsibleParty(val) => val.role_id(),
                ResponsiblePartyOrSubtype::SspSystemCharacteristicsResponsibleParty(val) => val.role_id(),

        }
    }
        fn party_uuids<'a>(&'a self) -> impl poly_containers::SeqRef<'a, String> {
        match self {
                ResponsiblePartyOrSubtype::ImplementationResponsibleParty(val) => val.party_uuids().to_any(),
                ResponsiblePartyOrSubtype::SspSystemCharacteristicsResponsibleParty(val) => val.party_uuids().to_any(),

        }
    }
}

pub trait ResponsibleRole : OscalCommon   {

    fn role_id(&self) -> responsible_role_utl::role_id_range;
    // fn role_id_mut(&mut self) -> &mut responsible_role_utl::role_id_range;
    // fn set_role_id(&mut self, value: String);

    fn party_uuids<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn party_uuids_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_party_uuids(&mut self, value: Option<&Vec<String>>);


}

impl ResponsibleRole for crate::ResponsibleRole {
        fn role_id(&self) -> responsible_role_utl::role_id_range {
            responsible_role_utl::role_id_range::String(self.role_id.clone())
    }
        fn party_uuids<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.party_uuids.as_ref();
    }
}
impl ResponsibleRole for crate::ImplementationResponsibleRole {
        fn role_id(&self) -> responsible_role_utl::role_id_range {
            match &self.role_id {
                implementation_responsible_role_utl::role_id_range::String(x) => responsible_role_utl::role_id_range::String(x.clone()),
                implementation_responsible_role_utl::role_id_range::ImplementationResponsibleRoleIdEnum(x) => responsible_role_utl::role_id_range::ImplementationResponsibleRoleIdEnum(x.clone()),
                implementation_responsible_role_utl::role_id_range::ImplementedRequirementResponsibleRoleIdEnum(x) => responsible_role_utl::role_id_range::ImplementedRequirementResponsibleRoleIdEnum(x.clone()),
                implementation_responsible_role_utl::role_id_range::ByComponentResponsibleRoleIdEnum(x) => responsible_role_utl::role_id_range::ByComponentResponsibleRoleIdEnum(x.clone()),
            }
    }
        fn party_uuids<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.party_uuids.as_ref();
    }
}
impl ResponsibleRole for crate::SspImplementedRequirementResponsibleRole {
        fn role_id(&self) -> responsible_role_utl::role_id_range {
            match &self.role_id {
                ssp_implemented_requirement_responsible_role_utl::role_id_range::String(x) => responsible_role_utl::role_id_range::String(x.clone()),
                ssp_implemented_requirement_responsible_role_utl::role_id_range::ImplementationResponsibleRoleIdEnum(x) => responsible_role_utl::role_id_range::ImplementationResponsibleRoleIdEnum(x.clone()),
                ssp_implemented_requirement_responsible_role_utl::role_id_range::ImplementedRequirementResponsibleRoleIdEnum(x) => responsible_role_utl::role_id_range::ImplementedRequirementResponsibleRoleIdEnum(x.clone()),
                ssp_implemented_requirement_responsible_role_utl::role_id_range::ByComponentResponsibleRoleIdEnum(x) => responsible_role_utl::role_id_range::ByComponentResponsibleRoleIdEnum(x.clone()),
            }
    }
        fn party_uuids<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.party_uuids.as_ref();
    }
}
impl ResponsibleRole for crate::SspByComponentResponsibleRole {
        fn role_id(&self) -> responsible_role_utl::role_id_range {
            match &self.role_id {
                ssp_by_component_responsible_role_utl::role_id_range::String(x) => responsible_role_utl::role_id_range::String(x.clone()),
                ssp_by_component_responsible_role_utl::role_id_range::ImplementationResponsibleRoleIdEnum(x) => responsible_role_utl::role_id_range::ImplementationResponsibleRoleIdEnum(x.clone()),
                ssp_by_component_responsible_role_utl::role_id_range::ImplementedRequirementResponsibleRoleIdEnum(x) => responsible_role_utl::role_id_range::ImplementedRequirementResponsibleRoleIdEnum(x.clone()),
                ssp_by_component_responsible_role_utl::role_id_range::ByComponentResponsibleRoleIdEnum(x) => responsible_role_utl::role_id_range::ByComponentResponsibleRoleIdEnum(x.clone()),
            }
    }
        fn party_uuids<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.party_uuids.as_ref();
    }
}

impl ResponsibleRole for crate::ResponsibleRoleOrSubtype {
        fn role_id(&self) -> responsible_role_utl::role_id_range {
        match self {
                ResponsibleRoleOrSubtype::ImplementationResponsibleRole(val) => val.role_id(),
                ResponsibleRoleOrSubtype::SspImplementedRequirementResponsibleRole(val) => val.role_id(),
                ResponsibleRoleOrSubtype::SspByComponentResponsibleRole(val) => val.role_id(),

        }
    }
        fn party_uuids<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        match self {
                ResponsibleRoleOrSubtype::ImplementationResponsibleRole(val) => val.party_uuids().map(|x| x.to_any()),
                ResponsibleRoleOrSubtype::SspImplementedRequirementResponsibleRole(val) => val.party_uuids().map(|x| x.to_any()),
                ResponsibleRoleOrSubtype::SspByComponentResponsibleRole(val) => val.party_uuids().map(|x| x.to_any()),

        }
    }
}

pub trait Action : OscalCommon  +  HasResponsibleParties   {

    fn uuid<'a>(&'a self) -> &'a str;
    // fn uuid_mut(&mut self) -> &mut &'a str;
    // fn set_uuid(&mut self, value: String);

    fn type_<'a>(&'a self) -> &'a crate::ActionTypeEnum;
    // fn type__mut(&mut self) -> &mut &'a crate::ActionTypeEnum;
    // fn set_type_(&mut self, value: ActionTypeEnum);

    fn date<'a>(&'a self) -> Option<&'a str>;
    // fn date_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_date(&mut self, value: Option<&'a str>);

    fn system(&self) -> action_utl::system_range;
    // fn system_mut(&mut self) -> &mut action_utl::system_range;
    // fn set_system(&mut self, value: action_utl::system_range);


}

impl Action for crate::Action {
        fn uuid<'a>(&'a self) -> &'a str {
        return &self.uuid[..];
    }
        fn type_<'a>(&'a self) -> &'a crate::ActionTypeEnum {
        return &self.type_;
    }
        fn date<'a>(&'a self) -> Option<&'a str> {
        return self.date.as_deref();
    }
        fn system(&self) -> action_utl::system_range {
            self.system.clone()
    }
}


pub trait TelephoneNumber   {

    fn type_(&self) -> Option<telephone_number_utl::type__range>;
    // fn type__mut(&mut self) -> &mut Option<telephone_number_utl::type__range>;
    // fn set_type_(&mut self, value: Option<&'a telephone_number_utl::type__range>);

    fn number<'a>(&'a self) -> &'a str;
    // fn number_mut(&mut self) -> &mut &'a str;
    // fn set_number(&mut self, value: String);


}

impl TelephoneNumber for crate::TelephoneNumber {
        fn type_(&self) -> Option<telephone_number_utl::type__range> {
                self.type_.as_ref().cloned()
    }
        fn number<'a>(&'a self) -> &'a str {
        return &self.number[..];
    }
}


pub trait Address   {

    fn type_(&self) -> Option<address_utl::type__range>;
    // fn type__mut(&mut self) -> &mut Option<address_utl::type__range>;
    // fn set_type_(&mut self, value: Option<&'a address_utl::type__range>);

    fn addr_lines<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn addr_lines_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_addr_lines(&mut self, value: Option<&Vec<String>>);

    fn city<'a>(&'a self) -> Option<&'a str>;
    // fn city_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_city(&mut self, value: Option<&'a str>);

    fn state<'a>(&'a self) -> Option<&'a str>;
    // fn state_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_state(&mut self, value: Option<&'a str>);

    fn postal_code<'a>(&'a self) -> Option<&'a str>;
    // fn postal_code_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_postal_code(&mut self, value: Option<&'a str>);

    fn country<'a>(&'a self) -> Option<&'a str>;
    // fn country_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_country(&mut self, value: Option<&'a str>);


}

impl Address for crate::Address {
        fn type_(&self) -> Option<address_utl::type__range> {
                self.type_.as_ref().cloned()
    }
        fn addr_lines<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.addr_lines.as_ref();
    }
        fn city<'a>(&'a self) -> Option<&'a str> {
        return self.city.as_deref();
    }
        fn state<'a>(&'a self) -> Option<&'a str> {
        return self.state.as_deref();
    }
        fn postal_code<'a>(&'a self) -> Option<&'a str> {
        return self.postal_code.as_deref();
    }
        fn country<'a>(&'a self) -> Option<&'a str> {
        return self.country.as_deref();
    }
}


pub trait Hash   {

    fn value<'a>(&'a self) -> &'a str;
    // fn value_mut(&mut self) -> &mut &'a str;
    // fn set_value(&mut self, value: String);

    fn algorithm(&self) -> hash_utl::algorithm_range;
    // fn algorithm_mut(&mut self) -> &mut hash_utl::algorithm_range;
    // fn set_algorithm(&mut self, value: hash_utl::algorithm_range);


}

impl Hash for crate::Hash {
        fn value<'a>(&'a self) -> &'a str {
        return &self.value[..];
    }
        fn algorithm(&self) -> hash_utl::algorithm_range {
            self.algorithm.clone()
    }
}


pub trait Property   {

    fn name(&self) -> property_utl::name_range;
    // fn name_mut(&mut self) -> &mut property_utl::name_range;
    // fn set_name(&mut self, value: String);

    fn uuid<'a>(&'a self) -> Option<&'a str>;
    // fn uuid_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_uuid(&mut self, value: Option<&'a str>);

    fn ns<'a>(&'a self) -> Option<&'a str>;
    // fn ns_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_ns(&mut self, value: Option<&'a str>);

    fn value(&self) -> property_utl::value_range;
    // fn value_mut(&mut self) -> &mut property_utl::value_range;
    // fn set_value(&mut self, value: String);

    fn _class(&self) -> Option<property_utl::_class_range>;
    // fn _class_mut(&mut self) -> &mut Option<property_utl::_class_range>;
    // fn set__class(&mut self, value: Option<&'a str>);

    fn remarks<'a>(&'a self) -> Option<&'a str>;
    // fn remarks_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_remarks(&mut self, value: Option<&'a str>);

    fn group<'a>(&'a self) -> Option<&'a str>;
    // fn group_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_group(&mut self, value: Option<&'a str>);


}

impl Property for crate::Property {
        fn name(&self) -> property_utl::name_range {
            property_utl::name_range::String(self.name.clone())
    }
        fn uuid<'a>(&'a self) -> Option<&'a str> {
        return self.uuid.as_deref();
    }
        fn ns<'a>(&'a self) -> Option<&'a str> {
        return self.ns.as_deref();
    }
        fn value(&self) -> property_utl::value_range {
            property_utl::value_range::String(self.value.clone())
    }
        fn _class(&self) -> Option<property_utl::_class_range> {
                self._class.as_ref().map(|v| property_utl::_class_range::String(v.clone()))
    }
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
        fn group<'a>(&'a self) -> Option<&'a str> {
        return self.group.as_deref();
    }
}
impl Property for crate::MetadataProperty {
        fn name(&self) -> property_utl::name_range {
            property_utl::name_range::MetadataPropNameEnum(self.name.clone())
    }
        fn uuid<'a>(&'a self) -> Option<&'a str> {
        return self.uuid.as_deref();
    }
        fn ns<'a>(&'a self) -> Option<&'a str> {
        return self.ns.as_deref();
    }
        fn value(&self) -> property_utl::value_range {
            property_utl::value_range::String(self.value.clone())
    }
        fn _class(&self) -> Option<property_utl::_class_range> {
                self._class.as_ref().map(|v| property_utl::_class_range::String(v.clone()))
    }
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
        fn group<'a>(&'a self) -> Option<&'a str> {
        return self.group.as_deref();
    }
}
impl Property for crate::RevisionProperty {
        fn name(&self) -> property_utl::name_range {
            property_utl::name_range::RevisionPropNameEnum(self.name.clone())
    }
        fn uuid<'a>(&'a self) -> Option<&'a str> {
        return self.uuid.as_deref();
    }
        fn ns<'a>(&'a self) -> Option<&'a str> {
        return self.ns.as_deref();
    }
        fn value(&self) -> property_utl::value_range {
            property_utl::value_range::String(self.value.clone())
    }
        fn _class(&self) -> Option<property_utl::_class_range> {
                self._class.as_ref().map(|v| property_utl::_class_range::String(v.clone()))
    }
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
        fn group<'a>(&'a self) -> Option<&'a str> {
        return self.group.as_deref();
    }
}
impl Property for crate::LocationProperty {
        fn name(&self) -> property_utl::name_range {
            property_utl::name_range::LocationPropNameEnum(self.name.clone())
    }
        fn uuid<'a>(&'a self) -> Option<&'a str> {
        return self.uuid.as_deref();
    }
        fn ns<'a>(&'a self) -> Option<&'a str> {
        return self.ns.as_deref();
    }
        fn value(&self) -> property_utl::value_range {
            match &self.value {
                location_property_utl::value_range::String(x) => property_utl::value_range::String(x.clone()),
                location_property_utl::value_range::LocationPropTypeEnum(x) => property_utl::value_range::LocationPropTypeEnum(x.clone()),
                location_property_utl::value_range::ResourcePropTypeEnum(x) => property_utl::value_range::ResourcePropTypeEnum(x.clone()),
                location_property_utl::value_range::ImplementationYesNoEnum(x) => property_utl::value_range::ImplementationYesNoEnum(x.clone()),
                location_property_utl::value_range::ImplementationAssetTypeEnum(x) => property_utl::value_range::ImplementationAssetTypeEnum(x.clone()),
                location_property_utl::value_range::ImplementationPointEnum(x) => property_utl::value_range::ImplementationPointEnum(x.clone()),
                location_property_utl::value_range::ImplementationIpAddressClassEnum(x) => property_utl::value_range::ImplementationIpAddressClassEnum(x.clone()),
                location_property_utl::value_range::ImplementationDirectionEnum(x) => property_utl::value_range::ImplementationDirectionEnum(x.clone()),
                location_property_utl::value_range::UserTypeEnum(x) => property_utl::value_range::UserTypeEnum(x.clone()),
                location_property_utl::value_range::UserPrivilegeLevelEnum(x) => property_utl::value_range::UserPrivilegeLevelEnum(x.clone()),
                location_property_utl::value_range::AssuranceLevelValueEnum(x) => property_utl::value_range::AssuranceLevelValueEnum(x.clone()),
                location_property_utl::value_range::CloudDeploymentModelEnum(x) => property_utl::value_range::CloudDeploymentModelEnum(x.clone()),
                location_property_utl::value_range::CloudServiceModelEnum(x) => property_utl::value_range::CloudServiceModelEnum(x.clone()),
                location_property_utl::value_range::PrivacyDesignationEnum(x) => property_utl::value_range::PrivacyDesignationEnum(x.clone()),
                location_property_utl::value_range::ControlOriginationValueEnum(x) => property_utl::value_range::ControlOriginationValueEnum(x.clone()),
                location_property_utl::value_range::AllowsAuthenticatedScanEnum(x) => property_utl::value_range::AllowsAuthenticatedScanEnum(x.clone()),
            }
    }
        fn _class(&self) -> Option<property_utl::_class_range> {
                self._class.as_ref().map(|v| match v {
                    location_property_utl::_class_range::String(x) => property_utl::_class_range::String(x.clone()),
                    location_property_utl::_class_range::LocationDataCenterClassEnum(x) => property_utl::_class_range::LocationDataCenterClassEnum(x.clone()),
                })
    }
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
        fn group<'a>(&'a self) -> Option<&'a str> {
        return self.group.as_deref();
    }
}
impl Property for crate::PartyProperty {
        fn name(&self) -> property_utl::name_range {
            property_utl::name_range::PartyPropNameEnum(self.name.clone())
    }
        fn uuid<'a>(&'a self) -> Option<&'a str> {
        return self.uuid.as_deref();
    }
        fn ns<'a>(&'a self) -> Option<&'a str> {
        return self.ns.as_deref();
    }
        fn value(&self) -> property_utl::value_range {
            property_utl::value_range::String(self.value.clone())
    }
        fn _class(&self) -> Option<property_utl::_class_range> {
                self._class.as_ref().map(|v| property_utl::_class_range::String(v.clone()))
    }
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
        fn group<'a>(&'a self) -> Option<&'a str> {
        return self.group.as_deref();
    }
}
impl Property for crate::ResourceProperty {
        fn name(&self) -> property_utl::name_range {
            property_utl::name_range::ResourcePropNameEnum(self.name.clone())
    }
        fn uuid<'a>(&'a self) -> Option<&'a str> {
        return self.uuid.as_deref();
    }
        fn ns<'a>(&'a self) -> Option<&'a str> {
        return self.ns.as_deref();
    }
        fn value(&self) -> property_utl::value_range {
            match &self.value {
                resource_property_utl::value_range::String(x) => property_utl::value_range::String(x.clone()),
                resource_property_utl::value_range::LocationPropTypeEnum(x) => property_utl::value_range::LocationPropTypeEnum(x.clone()),
                resource_property_utl::value_range::ResourcePropTypeEnum(x) => property_utl::value_range::ResourcePropTypeEnum(x.clone()),
                resource_property_utl::value_range::ImplementationYesNoEnum(x) => property_utl::value_range::ImplementationYesNoEnum(x.clone()),
                resource_property_utl::value_range::ImplementationAssetTypeEnum(x) => property_utl::value_range::ImplementationAssetTypeEnum(x.clone()),
                resource_property_utl::value_range::ImplementationPointEnum(x) => property_utl::value_range::ImplementationPointEnum(x.clone()),
                resource_property_utl::value_range::ImplementationIpAddressClassEnum(x) => property_utl::value_range::ImplementationIpAddressClassEnum(x.clone()),
                resource_property_utl::value_range::ImplementationDirectionEnum(x) => property_utl::value_range::ImplementationDirectionEnum(x.clone()),
                resource_property_utl::value_range::UserTypeEnum(x) => property_utl::value_range::UserTypeEnum(x.clone()),
                resource_property_utl::value_range::UserPrivilegeLevelEnum(x) => property_utl::value_range::UserPrivilegeLevelEnum(x.clone()),
                resource_property_utl::value_range::AssuranceLevelValueEnum(x) => property_utl::value_range::AssuranceLevelValueEnum(x.clone()),
                resource_property_utl::value_range::CloudDeploymentModelEnum(x) => property_utl::value_range::CloudDeploymentModelEnum(x.clone()),
                resource_property_utl::value_range::CloudServiceModelEnum(x) => property_utl::value_range::CloudServiceModelEnum(x.clone()),
                resource_property_utl::value_range::PrivacyDesignationEnum(x) => property_utl::value_range::PrivacyDesignationEnum(x.clone()),
                resource_property_utl::value_range::ControlOriginationValueEnum(x) => property_utl::value_range::ControlOriginationValueEnum(x.clone()),
                resource_property_utl::value_range::AllowsAuthenticatedScanEnum(x) => property_utl::value_range::AllowsAuthenticatedScanEnum(x.clone()),
            }
    }
        fn _class(&self) -> Option<property_utl::_class_range> {
                self._class.as_ref().map(|v| property_utl::_class_range::String(v.clone()))
    }
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
        fn group<'a>(&'a self) -> Option<&'a str> {
        return self.group.as_deref();
    }
}
impl Property for crate::PartProperty {
        fn name(&self) -> property_utl::name_range {
            property_utl::name_range::PartPropNameEnum(self.name.clone())
    }
        fn uuid<'a>(&'a self) -> Option<&'a str> {
        return self.uuid.as_deref();
    }
        fn ns<'a>(&'a self) -> Option<&'a str> {
        return self.ns.as_deref();
    }
        fn value(&self) -> property_utl::value_range {
            property_utl::value_range::String(self.value.clone())
    }
        fn _class(&self) -> Option<property_utl::_class_range> {
                self._class.as_ref().map(|v| property_utl::_class_range::String(v.clone()))
    }
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
        fn group<'a>(&'a self) -> Option<&'a str> {
        return self.group.as_deref();
    }
}
impl Property for crate::ParameterProperty {
        fn name(&self) -> property_utl::name_range {
            match &self.name {
                parameter_property_utl::name_range::String(x) => property_utl::name_range::String(x.clone()),
                parameter_property_utl::name_range::MetadataPropNameEnum(x) => property_utl::name_range::MetadataPropNameEnum(x.clone()),
                parameter_property_utl::name_range::RevisionPropNameEnum(x) => property_utl::name_range::RevisionPropNameEnum(x.clone()),
                parameter_property_utl::name_range::LocationPropNameEnum(x) => property_utl::name_range::LocationPropNameEnum(x.clone()),
                parameter_property_utl::name_range::PartyPropNameEnum(x) => property_utl::name_range::PartyPropNameEnum(x.clone()),
                parameter_property_utl::name_range::ResourcePropNameEnum(x) => property_utl::name_range::ResourcePropNameEnum(x.clone()),
                parameter_property_utl::name_range::PartPropNameEnum(x) => property_utl::name_range::PartPropNameEnum(x.clone()),
                parameter_property_utl::name_range::ParameterPropNameEnum(x) => property_utl::name_range::ParameterPropNameEnum(x.clone()),
                parameter_property_utl::name_range::RmfParameterPropNameEnum(x) => property_utl::name_range::RmfParameterPropNameEnum(x.clone()),
                parameter_property_utl::name_range::AlterationPropNameEnum(x) => property_utl::name_range::AlterationPropNameEnum(x.clone()),
                parameter_property_utl::name_range::ImplementationPropNameEnum(x) => property_utl::name_range::ImplementationPropNameEnum(x.clone()),
                parameter_property_utl::name_range::SystemCharacteristicsPropNameEnum(x) => property_utl::name_range::SystemCharacteristicsPropNameEnum(x.clone()),
                parameter_property_utl::name_range::SystemInformationPropNameEnum(x) => property_utl::name_range::SystemInformationPropNameEnum(x.clone()),
                parameter_property_utl::name_range::ControlOriginationPropNameEnum(x) => property_utl::name_range::ControlOriginationPropNameEnum(x.clone()),
            }
    }
        fn uuid<'a>(&'a self) -> Option<&'a str> {
        return self.uuid.as_deref();
    }
        fn ns<'a>(&'a self) -> Option<&'a str> {
        return self.ns.as_deref();
    }
        fn value(&self) -> property_utl::value_range {
            property_utl::value_range::String(self.value.clone())
    }
        fn _class(&self) -> Option<property_utl::_class_range> {
                self._class.as_ref().map(|v| property_utl::_class_range::String(v.clone()))
    }
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
        fn group<'a>(&'a self) -> Option<&'a str> {
        return self.group.as_deref();
    }
}
impl Property for crate::ProfileAlterationProperty {
        fn name(&self) -> property_utl::name_range {
            property_utl::name_range::AlterationPropNameEnum(self.name.clone())
    }
        fn uuid<'a>(&'a self) -> Option<&'a str> {
        return self.uuid.as_deref();
    }
        fn ns<'a>(&'a self) -> Option<&'a str> {
        return self.ns.as_deref();
    }
        fn value(&self) -> property_utl::value_range {
            property_utl::value_range::String(self.value.clone())
    }
        fn _class(&self) -> Option<property_utl::_class_range> {
                self._class.as_ref().map(|v| property_utl::_class_range::String(v.clone()))
    }
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
        fn group<'a>(&'a self) -> Option<&'a str> {
        return self.group.as_deref();
    }
}
impl Property for crate::ImplementationCommonProperty {
        fn name(&self) -> property_utl::name_range {
            property_utl::name_range::ImplementationPropNameEnum(self.name.clone())
    }
        fn uuid<'a>(&'a self) -> Option<&'a str> {
        return self.uuid.as_deref();
    }
        fn ns<'a>(&'a self) -> Option<&'a str> {
        return self.ns.as_deref();
    }
        fn value(&self) -> property_utl::value_range {
            match &self.value {
                implementation_common_property_utl::value_range::String(x) => property_utl::value_range::String(x.clone()),
                implementation_common_property_utl::value_range::LocationPropTypeEnum(x) => property_utl::value_range::LocationPropTypeEnum(x.clone()),
                implementation_common_property_utl::value_range::ResourcePropTypeEnum(x) => property_utl::value_range::ResourcePropTypeEnum(x.clone()),
                implementation_common_property_utl::value_range::ImplementationYesNoEnum(x) => property_utl::value_range::ImplementationYesNoEnum(x.clone()),
                implementation_common_property_utl::value_range::ImplementationAssetTypeEnum(x) => property_utl::value_range::ImplementationAssetTypeEnum(x.clone()),
                implementation_common_property_utl::value_range::ImplementationPointEnum(x) => property_utl::value_range::ImplementationPointEnum(x.clone()),
                implementation_common_property_utl::value_range::ImplementationIpAddressClassEnum(x) => property_utl::value_range::ImplementationIpAddressClassEnum(x.clone()),
                implementation_common_property_utl::value_range::ImplementationDirectionEnum(x) => property_utl::value_range::ImplementationDirectionEnum(x.clone()),
                implementation_common_property_utl::value_range::UserTypeEnum(x) => property_utl::value_range::UserTypeEnum(x.clone()),
                implementation_common_property_utl::value_range::UserPrivilegeLevelEnum(x) => property_utl::value_range::UserPrivilegeLevelEnum(x.clone()),
                implementation_common_property_utl::value_range::AssuranceLevelValueEnum(x) => property_utl::value_range::AssuranceLevelValueEnum(x.clone()),
                implementation_common_property_utl::value_range::CloudDeploymentModelEnum(x) => property_utl::value_range::CloudDeploymentModelEnum(x.clone()),
                implementation_common_property_utl::value_range::CloudServiceModelEnum(x) => property_utl::value_range::CloudServiceModelEnum(x.clone()),
                implementation_common_property_utl::value_range::PrivacyDesignationEnum(x) => property_utl::value_range::PrivacyDesignationEnum(x.clone()),
                implementation_common_property_utl::value_range::ControlOriginationValueEnum(x) => property_utl::value_range::ControlOriginationValueEnum(x.clone()),
                implementation_common_property_utl::value_range::AllowsAuthenticatedScanEnum(x) => property_utl::value_range::AllowsAuthenticatedScanEnum(x.clone()),
            }
    }
        fn _class(&self) -> Option<property_utl::_class_range> {
                self._class.as_ref().map(|v| property_utl::_class_range::String(v.clone()))
    }
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
        fn group<'a>(&'a self) -> Option<&'a str> {
        return self.group.as_deref();
    }
}
impl Property for crate::SspSystemCharacteristicsProp {
        fn name(&self) -> property_utl::name_range {
            property_utl::name_range::SystemCharacteristicsPropNameEnum(self.name.clone())
    }
        fn uuid<'a>(&'a self) -> Option<&'a str> {
        return self.uuid.as_deref();
    }
        fn ns<'a>(&'a self) -> Option<&'a str> {
        return self.ns.as_deref();
    }
        fn value(&self) -> property_utl::value_range {
            match &self.value {
                ssp_system_characteristics_prop_utl::value_range::String(x) => property_utl::value_range::String(x.clone()),
                ssp_system_characteristics_prop_utl::value_range::LocationPropTypeEnum(x) => property_utl::value_range::LocationPropTypeEnum(x.clone()),
                ssp_system_characteristics_prop_utl::value_range::ResourcePropTypeEnum(x) => property_utl::value_range::ResourcePropTypeEnum(x.clone()),
                ssp_system_characteristics_prop_utl::value_range::ImplementationYesNoEnum(x) => property_utl::value_range::ImplementationYesNoEnum(x.clone()),
                ssp_system_characteristics_prop_utl::value_range::ImplementationAssetTypeEnum(x) => property_utl::value_range::ImplementationAssetTypeEnum(x.clone()),
                ssp_system_characteristics_prop_utl::value_range::ImplementationPointEnum(x) => property_utl::value_range::ImplementationPointEnum(x.clone()),
                ssp_system_characteristics_prop_utl::value_range::ImplementationIpAddressClassEnum(x) => property_utl::value_range::ImplementationIpAddressClassEnum(x.clone()),
                ssp_system_characteristics_prop_utl::value_range::ImplementationDirectionEnum(x) => property_utl::value_range::ImplementationDirectionEnum(x.clone()),
                ssp_system_characteristics_prop_utl::value_range::UserTypeEnum(x) => property_utl::value_range::UserTypeEnum(x.clone()),
                ssp_system_characteristics_prop_utl::value_range::UserPrivilegeLevelEnum(x) => property_utl::value_range::UserPrivilegeLevelEnum(x.clone()),
                ssp_system_characteristics_prop_utl::value_range::AssuranceLevelValueEnum(x) => property_utl::value_range::AssuranceLevelValueEnum(x.clone()),
                ssp_system_characteristics_prop_utl::value_range::CloudDeploymentModelEnum(x) => property_utl::value_range::CloudDeploymentModelEnum(x.clone()),
                ssp_system_characteristics_prop_utl::value_range::CloudServiceModelEnum(x) => property_utl::value_range::CloudServiceModelEnum(x.clone()),
                ssp_system_characteristics_prop_utl::value_range::PrivacyDesignationEnum(x) => property_utl::value_range::PrivacyDesignationEnum(x.clone()),
                ssp_system_characteristics_prop_utl::value_range::ControlOriginationValueEnum(x) => property_utl::value_range::ControlOriginationValueEnum(x.clone()),
                ssp_system_characteristics_prop_utl::value_range::AllowsAuthenticatedScanEnum(x) => property_utl::value_range::AllowsAuthenticatedScanEnum(x.clone()),
            }
    }
        fn _class(&self) -> Option<property_utl::_class_range> {
                self._class.as_ref().map(|v| property_utl::_class_range::String(v.clone()))
    }
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
        fn group<'a>(&'a self) -> Option<&'a str> {
        return self.group.as_deref();
    }
}
impl Property for crate::SspSystemInformationProp {
        fn name(&self) -> property_utl::name_range {
            property_utl::name_range::SystemInformationPropNameEnum(self.name.clone())
    }
        fn uuid<'a>(&'a self) -> Option<&'a str> {
        return self.uuid.as_deref();
    }
        fn ns<'a>(&'a self) -> Option<&'a str> {
        return self.ns.as_deref();
    }
        fn value(&self) -> property_utl::value_range {
            property_utl::value_range::PrivacyDesignationEnum(self.value.clone())
    }
        fn _class(&self) -> Option<property_utl::_class_range> {
                self._class.as_ref().map(|v| property_utl::_class_range::String(v.clone()))
    }
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
        fn group<'a>(&'a self) -> Option<&'a str> {
        return self.group.as_deref();
    }
}
impl Property for crate::SspControlOriginationProp {
        fn name(&self) -> property_utl::name_range {
            property_utl::name_range::ControlOriginationPropNameEnum(self.name.clone())
    }
        fn uuid<'a>(&'a self) -> Option<&'a str> {
        return self.uuid.as_deref();
    }
        fn ns<'a>(&'a self) -> Option<&'a str> {
        return self.ns.as_deref();
    }
        fn value(&self) -> property_utl::value_range {
            property_utl::value_range::ControlOriginationValueEnum(self.value.clone())
    }
        fn _class(&self) -> Option<property_utl::_class_range> {
                self._class.as_ref().map(|v| property_utl::_class_range::String(v.clone()))
    }
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
        fn group<'a>(&'a self) -> Option<&'a str> {
        return self.group.as_deref();
    }
}
impl Property for crate::SspAllowsAuthenticatedScanProp {
        fn name(&self) -> property_utl::name_range {
            property_utl::name_range::String(self.name.clone())
    }
        fn uuid<'a>(&'a self) -> Option<&'a str> {
        return self.uuid.as_deref();
    }
        fn ns<'a>(&'a self) -> Option<&'a str> {
        return self.ns.as_deref();
    }
        fn value(&self) -> property_utl::value_range {
            property_utl::value_range::AllowsAuthenticatedScanEnum(self.value.clone())
    }
        fn _class(&self) -> Option<property_utl::_class_range> {
                self._class.as_ref().map(|v| property_utl::_class_range::String(v.clone()))
    }
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
        fn group<'a>(&'a self) -> Option<&'a str> {
        return self.group.as_deref();
    }
}

impl Property for crate::PropertyOrSubtype {
        fn name(&self) -> property_utl::name_range {
        match self {
                PropertyOrSubtype::MetadataProperty(val) => val.name(),
                PropertyOrSubtype::RevisionProperty(val) => val.name(),
                PropertyOrSubtype::LocationProperty(val) => val.name(),
                PropertyOrSubtype::PartyProperty(val) => val.name(),
                PropertyOrSubtype::ResourceProperty(val) => val.name(),
                PropertyOrSubtype::PartProperty(val) => val.name(),
                PropertyOrSubtype::ParameterProperty(val) => val.name(),
                PropertyOrSubtype::ProfileAlterationProperty(val) => val.name(),
                PropertyOrSubtype::ImplementationCommonProperty(val) => val.name(),
                PropertyOrSubtype::SspSystemCharacteristicsProp(val) => val.name(),
                PropertyOrSubtype::SspSystemInformationProp(val) => val.name(),
                PropertyOrSubtype::SspControlOriginationProp(val) => val.name(),
                PropertyOrSubtype::SspAllowsAuthenticatedScanProp(val) => val.name(),

        }
    }
        fn uuid<'a>(&'a self) -> Option<&'a str> {
        match self {
                PropertyOrSubtype::MetadataProperty(val) => val.uuid(),
                PropertyOrSubtype::RevisionProperty(val) => val.uuid(),
                PropertyOrSubtype::LocationProperty(val) => val.uuid(),
                PropertyOrSubtype::PartyProperty(val) => val.uuid(),
                PropertyOrSubtype::ResourceProperty(val) => val.uuid(),
                PropertyOrSubtype::PartProperty(val) => val.uuid(),
                PropertyOrSubtype::ParameterProperty(val) => val.uuid(),
                PropertyOrSubtype::ProfileAlterationProperty(val) => val.uuid(),
                PropertyOrSubtype::ImplementationCommonProperty(val) => val.uuid(),
                PropertyOrSubtype::SspSystemCharacteristicsProp(val) => val.uuid(),
                PropertyOrSubtype::SspSystemInformationProp(val) => val.uuid(),
                PropertyOrSubtype::SspControlOriginationProp(val) => val.uuid(),
                PropertyOrSubtype::SspAllowsAuthenticatedScanProp(val) => val.uuid(),

        }
    }
        fn ns<'a>(&'a self) -> Option<&'a str> {
        match self {
                PropertyOrSubtype::MetadataProperty(val) => val.ns(),
                PropertyOrSubtype::RevisionProperty(val) => val.ns(),
                PropertyOrSubtype::LocationProperty(val) => val.ns(),
                PropertyOrSubtype::PartyProperty(val) => val.ns(),
                PropertyOrSubtype::ResourceProperty(val) => val.ns(),
                PropertyOrSubtype::PartProperty(val) => val.ns(),
                PropertyOrSubtype::ParameterProperty(val) => val.ns(),
                PropertyOrSubtype::ProfileAlterationProperty(val) => val.ns(),
                PropertyOrSubtype::ImplementationCommonProperty(val) => val.ns(),
                PropertyOrSubtype::SspSystemCharacteristicsProp(val) => val.ns(),
                PropertyOrSubtype::SspSystemInformationProp(val) => val.ns(),
                PropertyOrSubtype::SspControlOriginationProp(val) => val.ns(),
                PropertyOrSubtype::SspAllowsAuthenticatedScanProp(val) => val.ns(),

        }
    }
        fn value(&self) -> property_utl::value_range {
        match self {
                PropertyOrSubtype::MetadataProperty(val) => val.value(),
                PropertyOrSubtype::RevisionProperty(val) => val.value(),
                PropertyOrSubtype::LocationProperty(val) => val.value(),
                PropertyOrSubtype::PartyProperty(val) => val.value(),
                PropertyOrSubtype::ResourceProperty(val) => val.value(),
                PropertyOrSubtype::PartProperty(val) => val.value(),
                PropertyOrSubtype::ParameterProperty(val) => val.value(),
                PropertyOrSubtype::ProfileAlterationProperty(val) => val.value(),
                PropertyOrSubtype::ImplementationCommonProperty(val) => val.value(),
                PropertyOrSubtype::SspSystemCharacteristicsProp(val) => val.value(),
                PropertyOrSubtype::SspSystemInformationProp(val) => val.value(),
                PropertyOrSubtype::SspControlOriginationProp(val) => val.value(),
                PropertyOrSubtype::SspAllowsAuthenticatedScanProp(val) => val.value(),

        }
    }
        fn _class(&self) -> Option<property_utl::_class_range> {
        match self {
                PropertyOrSubtype::MetadataProperty(val) => val._class(),
                PropertyOrSubtype::RevisionProperty(val) => val._class(),
                PropertyOrSubtype::LocationProperty(val) => val._class(),
                PropertyOrSubtype::PartyProperty(val) => val._class(),
                PropertyOrSubtype::ResourceProperty(val) => val._class(),
                PropertyOrSubtype::PartProperty(val) => val._class(),
                PropertyOrSubtype::ParameterProperty(val) => val._class(),
                PropertyOrSubtype::ProfileAlterationProperty(val) => val._class(),
                PropertyOrSubtype::ImplementationCommonProperty(val) => val._class(),
                PropertyOrSubtype::SspSystemCharacteristicsProp(val) => val._class(),
                PropertyOrSubtype::SspSystemInformationProp(val) => val._class(),
                PropertyOrSubtype::SspControlOriginationProp(val) => val._class(),
                PropertyOrSubtype::SspAllowsAuthenticatedScanProp(val) => val._class(),

        }
    }
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        match self {
                PropertyOrSubtype::MetadataProperty(val) => val.remarks(),
                PropertyOrSubtype::RevisionProperty(val) => val.remarks(),
                PropertyOrSubtype::LocationProperty(val) => val.remarks(),
                PropertyOrSubtype::PartyProperty(val) => val.remarks(),
                PropertyOrSubtype::ResourceProperty(val) => val.remarks(),
                PropertyOrSubtype::PartProperty(val) => val.remarks(),
                PropertyOrSubtype::ParameterProperty(val) => val.remarks(),
                PropertyOrSubtype::ProfileAlterationProperty(val) => val.remarks(),
                PropertyOrSubtype::ImplementationCommonProperty(val) => val.remarks(),
                PropertyOrSubtype::SspSystemCharacteristicsProp(val) => val.remarks(),
                PropertyOrSubtype::SspSystemInformationProp(val) => val.remarks(),
                PropertyOrSubtype::SspControlOriginationProp(val) => val.remarks(),
                PropertyOrSubtype::SspAllowsAuthenticatedScanProp(val) => val.remarks(),

        }
    }
        fn group<'a>(&'a self) -> Option<&'a str> {
        match self {
                PropertyOrSubtype::MetadataProperty(val) => val.group(),
                PropertyOrSubtype::RevisionProperty(val) => val.group(),
                PropertyOrSubtype::LocationProperty(val) => val.group(),
                PropertyOrSubtype::PartyProperty(val) => val.group(),
                PropertyOrSubtype::ResourceProperty(val) => val.group(),
                PropertyOrSubtype::PartProperty(val) => val.group(),
                PropertyOrSubtype::ParameterProperty(val) => val.group(),
                PropertyOrSubtype::ProfileAlterationProperty(val) => val.group(),
                PropertyOrSubtype::ImplementationCommonProperty(val) => val.group(),
                PropertyOrSubtype::SspSystemCharacteristicsProp(val) => val.group(),
                PropertyOrSubtype::SspSystemInformationProp(val) => val.group(),
                PropertyOrSubtype::SspControlOriginationProp(val) => val.group(),
                PropertyOrSubtype::SspAllowsAuthenticatedScanProp(val) => val.group(),

        }
    }
}

pub trait MetadataProperty : Property   {


}

impl MetadataProperty for crate::MetadataProperty {
}


pub trait RevisionProperty : Property   {


}

impl RevisionProperty for crate::RevisionProperty {
}


pub trait LocationProperty : Property   {


}

impl LocationProperty for crate::LocationProperty {
}


pub trait PartyProperty : Property   {


}

impl PartyProperty for crate::PartyProperty {
}


pub trait ResourceProperty : Property   {


}

impl ResourceProperty for crate::ResourceProperty {
}


pub trait PartProperty : Property   {


}

impl PartProperty for crate::PartProperty {
}


pub trait ParameterProperty : Property   {


}

impl ParameterProperty for crate::ParameterProperty {
}


pub trait MetadataPartyExternalId : PartyExternalId   {


}

impl MetadataPartyExternalId for crate::MetadataPartyExternalId {
}


pub trait Link   {

    fn href<'a>(&'a self) -> &'a str;
    // fn href_mut(&mut self) -> &mut &'a str;
    // fn set_href(&mut self, value: String);

    fn rel(&self) -> Option<link_utl::rel_range>;
    // fn rel_mut(&mut self) -> &mut Option<link_utl::rel_range>;
    // fn set_rel(&mut self, value: Option<&'a link_utl::rel_range>);

    fn resource_fragment<'a>(&'a self) -> Option<&'a str>;
    // fn resource_fragment_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_resource_fragment(&mut self, value: Option<&'a str>);

    fn media_type<'a>(&'a self) -> Option<&'a str>;
    // fn media_type_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_media_type(&mut self, value: Option<&'a str>);

    fn text<'a>(&'a self) -> Option<&'a str>;
    // fn text_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_text(&mut self, value: Option<&'a str>);


}

impl Link for crate::Link {
        fn href<'a>(&'a self) -> &'a str {
        return &self.href[..];
    }
        fn rel(&self) -> Option<link_utl::rel_range> {
                self.rel.as_ref().cloned()
    }
        fn resource_fragment<'a>(&'a self) -> Option<&'a str> {
        return self.resource_fragment.as_deref();
    }
        fn media_type<'a>(&'a self) -> Option<&'a str> {
        return self.media_type.as_deref();
    }
        fn text<'a>(&'a self) -> Option<&'a str> {
        return self.text.as_deref();
    }
}
impl Link for crate::ImplementationCommonLink {
        fn href<'a>(&'a self) -> &'a str {
        return &self.href[..];
    }
        fn rel(&self) -> Option<link_utl::rel_range> {
                self.rel.as_ref().map(|v| match v {
                    implementation_common_link_utl::rel_range::String(x) => link_utl::rel_range::String(x.clone()),
                    implementation_common_link_utl::rel_range::MetadataLinkRelEnum(x) => link_utl::rel_range::MetadataLinkRelEnum(x.clone()),
                    implementation_common_link_utl::rel_range::ImplementationLinkRelEnum(x) => link_utl::rel_range::ImplementationLinkRelEnum(x.clone()),
                    implementation_common_link_utl::rel_range::SystemInformationLinkRelEnum(x) => link_utl::rel_range::SystemInformationLinkRelEnum(x.clone()),
                    implementation_common_link_utl::rel_range::DiagramLinkRelEnum(x) => link_utl::rel_range::DiagramLinkRelEnum(x.clone()),
                    implementation_common_link_utl::rel_range::LeveragedAuthorizationLinkRelEnum(x) => link_utl::rel_range::LeveragedAuthorizationLinkRelEnum(x.clone()),
                    implementation_common_link_utl::rel_range::ByComponentLinkRelEnum(x) => link_utl::rel_range::ByComponentLinkRelEnum(x.clone()),
                })
    }
        fn resource_fragment<'a>(&'a self) -> Option<&'a str> {
        return self.resource_fragment.as_deref();
    }
        fn media_type<'a>(&'a self) -> Option<&'a str> {
        return self.media_type.as_deref();
    }
        fn text<'a>(&'a self) -> Option<&'a str> {
        return self.text.as_deref();
    }
}
impl Link for crate::SspSystemInformationLink {
        fn href<'a>(&'a self) -> &'a str {
        return &self.href[..];
    }
        fn rel(&self) -> Option<link_utl::rel_range> {
                self.rel.as_ref().map(|v| match v {
                    ssp_system_information_link_utl::rel_range::String(x) => link_utl::rel_range::String(x.clone()),
                    ssp_system_information_link_utl::rel_range::MetadataLinkRelEnum(x) => link_utl::rel_range::MetadataLinkRelEnum(x.clone()),
                    ssp_system_information_link_utl::rel_range::ImplementationLinkRelEnum(x) => link_utl::rel_range::ImplementationLinkRelEnum(x.clone()),
                    ssp_system_information_link_utl::rel_range::SystemInformationLinkRelEnum(x) => link_utl::rel_range::SystemInformationLinkRelEnum(x.clone()),
                    ssp_system_information_link_utl::rel_range::DiagramLinkRelEnum(x) => link_utl::rel_range::DiagramLinkRelEnum(x.clone()),
                    ssp_system_information_link_utl::rel_range::LeveragedAuthorizationLinkRelEnum(x) => link_utl::rel_range::LeveragedAuthorizationLinkRelEnum(x.clone()),
                    ssp_system_information_link_utl::rel_range::ByComponentLinkRelEnum(x) => link_utl::rel_range::ByComponentLinkRelEnum(x.clone()),
                })
    }
        fn resource_fragment<'a>(&'a self) -> Option<&'a str> {
        return self.resource_fragment.as_deref();
    }
        fn media_type<'a>(&'a self) -> Option<&'a str> {
        return self.media_type.as_deref();
    }
        fn text<'a>(&'a self) -> Option<&'a str> {
        return self.text.as_deref();
    }
}
impl Link for crate::SspDiagramLink {
        fn href<'a>(&'a self) -> &'a str {
        return &self.href[..];
    }
        fn rel(&self) -> Option<link_utl::rel_range> {
                self.rel.as_ref().map(|v| match v {
                    ssp_diagram_link_utl::rel_range::String(x) => link_utl::rel_range::String(x.clone()),
                    ssp_diagram_link_utl::rel_range::MetadataLinkRelEnum(x) => link_utl::rel_range::MetadataLinkRelEnum(x.clone()),
                    ssp_diagram_link_utl::rel_range::ImplementationLinkRelEnum(x) => link_utl::rel_range::ImplementationLinkRelEnum(x.clone()),
                    ssp_diagram_link_utl::rel_range::SystemInformationLinkRelEnum(x) => link_utl::rel_range::SystemInformationLinkRelEnum(x.clone()),
                    ssp_diagram_link_utl::rel_range::DiagramLinkRelEnum(x) => link_utl::rel_range::DiagramLinkRelEnum(x.clone()),
                    ssp_diagram_link_utl::rel_range::LeveragedAuthorizationLinkRelEnum(x) => link_utl::rel_range::LeveragedAuthorizationLinkRelEnum(x.clone()),
                    ssp_diagram_link_utl::rel_range::ByComponentLinkRelEnum(x) => link_utl::rel_range::ByComponentLinkRelEnum(x.clone()),
                })
    }
        fn resource_fragment<'a>(&'a self) -> Option<&'a str> {
        return self.resource_fragment.as_deref();
    }
        fn media_type<'a>(&'a self) -> Option<&'a str> {
        return self.media_type.as_deref();
    }
        fn text<'a>(&'a self) -> Option<&'a str> {
        return self.text.as_deref();
    }
}
impl Link for crate::SspLeveragedAuthorizationLink {
        fn href<'a>(&'a self) -> &'a str {
        return &self.href[..];
    }
        fn rel(&self) -> Option<link_utl::rel_range> {
                self.rel.as_ref().map(|v| match v {
                    ssp_leveraged_authorization_link_utl::rel_range::String(x) => link_utl::rel_range::String(x.clone()),
                    ssp_leveraged_authorization_link_utl::rel_range::MetadataLinkRelEnum(x) => link_utl::rel_range::MetadataLinkRelEnum(x.clone()),
                    ssp_leveraged_authorization_link_utl::rel_range::ImplementationLinkRelEnum(x) => link_utl::rel_range::ImplementationLinkRelEnum(x.clone()),
                    ssp_leveraged_authorization_link_utl::rel_range::SystemInformationLinkRelEnum(x) => link_utl::rel_range::SystemInformationLinkRelEnum(x.clone()),
                    ssp_leveraged_authorization_link_utl::rel_range::DiagramLinkRelEnum(x) => link_utl::rel_range::DiagramLinkRelEnum(x.clone()),
                    ssp_leveraged_authorization_link_utl::rel_range::LeveragedAuthorizationLinkRelEnum(x) => link_utl::rel_range::LeveragedAuthorizationLinkRelEnum(x.clone()),
                    ssp_leveraged_authorization_link_utl::rel_range::ByComponentLinkRelEnum(x) => link_utl::rel_range::ByComponentLinkRelEnum(x.clone()),
                })
    }
        fn resource_fragment<'a>(&'a self) -> Option<&'a str> {
        return self.resource_fragment.as_deref();
    }
        fn media_type<'a>(&'a self) -> Option<&'a str> {
        return self.media_type.as_deref();
    }
        fn text<'a>(&'a self) -> Option<&'a str> {
        return self.text.as_deref();
    }
}
impl Link for crate::SspByComponentLink {
        fn href<'a>(&'a self) -> &'a str {
        return &self.href[..];
    }
        fn rel(&self) -> Option<link_utl::rel_range> {
                self.rel.as_ref().map(|v| match v {
                    ssp_by_component_link_utl::rel_range::String(x) => link_utl::rel_range::String(x.clone()),
                    ssp_by_component_link_utl::rel_range::MetadataLinkRelEnum(x) => link_utl::rel_range::MetadataLinkRelEnum(x.clone()),
                    ssp_by_component_link_utl::rel_range::ImplementationLinkRelEnum(x) => link_utl::rel_range::ImplementationLinkRelEnum(x.clone()),
                    ssp_by_component_link_utl::rel_range::SystemInformationLinkRelEnum(x) => link_utl::rel_range::SystemInformationLinkRelEnum(x.clone()),
                    ssp_by_component_link_utl::rel_range::DiagramLinkRelEnum(x) => link_utl::rel_range::DiagramLinkRelEnum(x.clone()),
                    ssp_by_component_link_utl::rel_range::LeveragedAuthorizationLinkRelEnum(x) => link_utl::rel_range::LeveragedAuthorizationLinkRelEnum(x.clone()),
                    ssp_by_component_link_utl::rel_range::ByComponentLinkRelEnum(x) => link_utl::rel_range::ByComponentLinkRelEnum(x.clone()),
                })
    }
        fn resource_fragment<'a>(&'a self) -> Option<&'a str> {
        return self.resource_fragment.as_deref();
    }
        fn media_type<'a>(&'a self) -> Option<&'a str> {
        return self.media_type.as_deref();
    }
        fn text<'a>(&'a self) -> Option<&'a str> {
        return self.text.as_deref();
    }
}

impl Link for crate::LinkOrSubtype {
        fn href<'a>(&'a self) -> &'a str {
        match self {
                LinkOrSubtype::ImplementationCommonLink(val) => val.href(),
                LinkOrSubtype::SspSystemInformationLink(val) => val.href(),
                LinkOrSubtype::SspDiagramLink(val) => val.href(),
                LinkOrSubtype::SspLeveragedAuthorizationLink(val) => val.href(),
                LinkOrSubtype::SspByComponentLink(val) => val.href(),

        }
    }
        fn rel(&self) -> Option<link_utl::rel_range> {
        match self {
                LinkOrSubtype::ImplementationCommonLink(val) => val.rel(),
                LinkOrSubtype::SspSystemInformationLink(val) => val.rel(),
                LinkOrSubtype::SspDiagramLink(val) => val.rel(),
                LinkOrSubtype::SspLeveragedAuthorizationLink(val) => val.rel(),
                LinkOrSubtype::SspByComponentLink(val) => val.rel(),

        }
    }
        fn resource_fragment<'a>(&'a self) -> Option<&'a str> {
        match self {
                LinkOrSubtype::ImplementationCommonLink(val) => val.resource_fragment(),
                LinkOrSubtype::SspSystemInformationLink(val) => val.resource_fragment(),
                LinkOrSubtype::SspDiagramLink(val) => val.resource_fragment(),
                LinkOrSubtype::SspLeveragedAuthorizationLink(val) => val.resource_fragment(),
                LinkOrSubtype::SspByComponentLink(val) => val.resource_fragment(),

        }
    }
        fn media_type<'a>(&'a self) -> Option<&'a str> {
        match self {
                LinkOrSubtype::ImplementationCommonLink(val) => val.media_type(),
                LinkOrSubtype::SspSystemInformationLink(val) => val.media_type(),
                LinkOrSubtype::SspDiagramLink(val) => val.media_type(),
                LinkOrSubtype::SspLeveragedAuthorizationLink(val) => val.media_type(),
                LinkOrSubtype::SspByComponentLink(val) => val.media_type(),

        }
    }
        fn text<'a>(&'a self) -> Option<&'a str> {
        match self {
                LinkOrSubtype::ImplementationCommonLink(val) => val.text(),
                LinkOrSubtype::SspSystemInformationLink(val) => val.text(),
                LinkOrSubtype::SspDiagramLink(val) => val.text(),
                LinkOrSubtype::SspLeveragedAuthorizationLink(val) => val.text(),
                LinkOrSubtype::SspByComponentLink(val) => val.text(),

        }
    }
}

pub trait BackMatter   {

    fn resources<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Resource>>;
    // fn resources_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::Resource>>;
    // fn set_resources<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Resource>;


}

impl BackMatter for crate::BackMatter {
        fn resources<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Resource>> {
        return self.resources.as_ref();
    }
}


pub trait Resource   {

    fn uuid<'a>(&'a self) -> &'a str;
    // fn uuid_mut(&mut self) -> &mut &'a str;
    // fn set_uuid(&mut self, value: String);

    fn title<'a>(&'a self) -> Option<&'a str>;
    // fn title_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_title(&mut self, value: Option<&'a str>);

    fn description<'a>(&'a self) -> Option<&'a str>;
    // fn description_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_description(&mut self, value: Option<&'a str>);

    fn props<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::ResourceProperty>>;
    // fn props_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::ResourceProperty>>;
    // fn set_props<E>(&mut self, value: Option<&Vec<E>>) where E: Into<ResourceProperty>;

    fn document_ids<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::DocumentId>>;
    // fn document_ids_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::DocumentId>>;
    // fn set_document_ids<E>(&mut self, value: Option<&Vec<E>>) where E: Into<DocumentId>;

    fn remarks<'a>(&'a self) -> Option<&'a str>;
    // fn remarks_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_remarks(&mut self, value: Option<&'a str>);

    fn citation<'a>(&'a self) -> Option<&'a crate::Citation>;
    // fn citation_mut(&mut self) -> &mut Option<&'a crate::Citation>;
    // fn set_citation<E>(&mut self, value: Option<E>) where E: Into<Citation>;

    fn rlinks<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::ResourceLink>>;
    // fn rlinks_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::ResourceLink>>;
    // fn set_rlinks<E>(&mut self, value: Option<&Vec<E>>) where E: Into<ResourceLink>;

    fn base64<'a>(&'a self) -> Option<&'a crate::Base64Resource>;
    // fn base64_mut(&mut self) -> &mut Option<&'a crate::Base64Resource>;
    // fn set_base64<E>(&mut self, value: Option<E>) where E: Into<Base64Resource>;


}

impl Resource for crate::Resource {
        fn uuid<'a>(&'a self) -> &'a str {
        return &self.uuid[..];
    }
        fn title<'a>(&'a self) -> Option<&'a str> {
        return self.title.as_deref();
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn props<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::ResourceProperty>> {
        return self.props.as_ref();
    }
        fn document_ids<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::DocumentId>> {
        return self.document_ids.as_ref();
    }
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
        fn citation<'a>(&'a self) -> Option<&'a crate::Citation> {
        return self.citation.as_ref();
    }
        fn rlinks<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::ResourceLink>> {
        return self.rlinks.as_ref();
    }
        fn base64<'a>(&'a self) -> Option<&'a crate::Base64Resource> {
        return self.base64.as_ref();
    }
}


pub trait Citation : HasPropsAndLinks   {

    fn text<'a>(&'a self) -> &'a str;
    // fn text_mut(&mut self) -> &mut &'a str;
    // fn set_text(&mut self, value: String);


}

impl Citation for crate::Citation {
        fn text<'a>(&'a self) -> &'a str {
        return &self.text[..];
    }
}


pub trait ResourceLink   {

    fn href<'a>(&'a self) -> &'a str;
    // fn href_mut(&mut self) -> &mut &'a str;
    // fn set_href(&mut self, value: String);

    fn media_type<'a>(&'a self) -> Option<&'a str>;
    // fn media_type_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_media_type(&mut self, value: Option<&'a str>);

    fn hashes<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Hash>>;
    // fn hashes_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::Hash>>;
    // fn set_hashes<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Hash>;


}

impl ResourceLink for crate::ResourceLink {
        fn href<'a>(&'a self) -> &'a str {
        return &self.href[..];
    }
        fn media_type<'a>(&'a self) -> Option<&'a str> {
        return self.media_type.as_deref();
    }
        fn hashes<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Hash>> {
        return self.hashes.as_ref();
    }
}


pub trait Base64Resource   {

    fn media_type<'a>(&'a self) -> Option<&'a str>;
    // fn media_type_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_media_type(&mut self, value: Option<&'a str>);

    fn value<'a>(&'a self) -> &'a str;
    // fn value_mut(&mut self) -> &mut &'a str;
    // fn set_value(&mut self, value: String);

    fn filename<'a>(&'a self) -> Option<&'a str>;
    // fn filename_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_filename(&mut self, value: Option<&'a str>);


}

impl Base64Resource for crate::Base64Resource {
        fn media_type<'a>(&'a self) -> Option<&'a str> {
        return self.media_type.as_deref();
    }
        fn value<'a>(&'a self) -> &'a str {
        return &self.value[..];
    }
        fn filename<'a>(&'a self) -> Option<&'a str> {
        return self.filename.as_deref();
    }
}


pub trait Part : HasPropsAndLinks   {

    fn id<'a>(&'a self) -> Option<&'a str>;
    // fn id_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_id(&mut self, value: Option<&'a str>);

    fn name<'a>(&'a self) -> &'a str;
    // fn name_mut(&mut self) -> &mut &'a str;
    // fn set_name(&mut self, value: String);

    fn ns<'a>(&'a self) -> Option<&'a str>;
    // fn ns_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_ns(&mut self, value: Option<&'a str>);

    fn _class<'a>(&'a self) -> Option<&'a str>;
    // fn _class_mut(&mut self) -> &mut Option<&'a str>;
    // fn set__class(&mut self, value: Option<&'a str>);

    fn title<'a>(&'a self) -> Option<&'a str>;
    // fn title_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_title(&mut self, value: Option<&'a str>);

    fn prose<'a>(&'a self) -> Option<&'a str>;
    // fn prose_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_prose(&mut self, value: Option<&'a str>);

    fn parts<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Part>>;
    // fn parts_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::Part>>;
    // fn set_parts<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Part>;


}

impl Part for crate::Part {
        fn id<'a>(&'a self) -> Option<&'a str> {
        return self.id.as_deref();
    }
        fn name<'a>(&'a self) -> &'a str {
        return &self.name[..];
    }
        fn ns<'a>(&'a self) -> Option<&'a str> {
        return self.ns.as_deref();
    }
        fn _class<'a>(&'a self) -> Option<&'a str> {
        return self._class.as_deref();
    }
        fn title<'a>(&'a self) -> Option<&'a str> {
        return self.title.as_deref();
    }
        fn prose<'a>(&'a self) -> Option<&'a str> {
        return self.prose.as_deref();
    }
        fn parts<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Part>> {
        return self.parts.as_ref().map(|x| poly_containers::ListView::new(x));
    }
}


pub trait Parameter : OscalCommon   {

    fn id<'a>(&'a self) -> &'a str;
    // fn id_mut(&mut self) -> &mut &'a str;
    // fn set_id(&mut self, value: String);

    fn _class<'a>(&'a self) -> Option<&'a str>;
    // fn _class_mut(&mut self) -> &mut Option<&'a str>;
    // fn set__class(&mut self, value: Option<&'a str>);

    fn depends_on<'a>(&'a self) -> Option<&'a str>;
    // fn depends_on_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_depends_on(&mut self, value: Option<&'a str>);

    fn label<'a>(&'a self) -> Option<&'a str>;
    // fn label_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_label(&mut self, value: Option<&'a str>);

    fn usage<'a>(&'a self) -> Option<&'a str>;
    // fn usage_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_usage(&mut self, value: Option<&'a str>);

    fn constraints<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::ParameterConstraint>>;
    // fn constraints_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::ParameterConstraint>>;
    // fn set_constraints<E>(&mut self, value: Option<&Vec<E>>) where E: Into<ParameterConstraint>;

    fn guidelines<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::ParameterGuideline>>;
    // fn guidelines_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::ParameterGuideline>>;
    // fn set_guidelines<E>(&mut self, value: Option<&Vec<E>>) where E: Into<ParameterGuideline>;

    fn values<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn values_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_values(&mut self, value: Option<&Vec<String>>);

    fn select<'a>(&'a self) -> Option<&'a crate::ParameterSelection>;
    // fn select_mut(&mut self) -> &mut Option<&'a crate::ParameterSelection>;
    // fn set_select<E>(&mut self, value: Option<E>) where E: Into<ParameterSelection>;


}

impl Parameter for crate::Parameter {
        fn id<'a>(&'a self) -> &'a str {
        return &self.id[..];
    }
        fn _class<'a>(&'a self) -> Option<&'a str> {
        return self._class.as_deref();
    }
        fn depends_on<'a>(&'a self) -> Option<&'a str> {
        return self.depends_on.as_deref();
    }
        fn label<'a>(&'a self) -> Option<&'a str> {
        return self.label.as_deref();
    }
        fn usage<'a>(&'a self) -> Option<&'a str> {
        return self.usage.as_deref();
    }
        fn constraints<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::ParameterConstraint>> {
        return self.constraints.as_ref();
    }
        fn guidelines<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::ParameterGuideline>> {
        return self.guidelines.as_ref();
    }
        fn values<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.values.as_ref();
    }
        fn select<'a>(&'a self) -> Option<&'a crate::ParameterSelection> {
        return self.select.as_ref();
    }
}


pub trait ParameterConstraint   {

    fn description<'a>(&'a self) -> Option<&'a str>;
    // fn description_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_description(&mut self, value: Option<&'a str>);

    fn tests<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::ConstraintTest>>;
    // fn tests_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::ConstraintTest>>;
    // fn set_tests<E>(&mut self, value: Option<&Vec<E>>) where E: Into<ConstraintTest>;


}

impl ParameterConstraint for crate::ParameterConstraint {
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn tests<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::ConstraintTest>> {
        return self.tests.as_ref();
    }
}


pub trait ConstraintTest   {

    fn remarks<'a>(&'a self) -> Option<&'a str>;
    // fn remarks_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_remarks(&mut self, value: Option<&'a str>);

    fn expression<'a>(&'a self) -> &'a str;
    // fn expression_mut(&mut self) -> &mut &'a str;
    // fn set_expression(&mut self, value: String);


}

impl ConstraintTest for crate::ConstraintTest {
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
        fn expression<'a>(&'a self) -> &'a str {
        return &self.expression[..];
    }
}


pub trait ParameterGuideline   {

    fn prose<'a>(&'a self) -> &'a str;
    // fn prose_mut(&mut self) -> &mut &'a str;
    // fn set_prose(&mut self, value: String);


}

impl ParameterGuideline for crate::ParameterGuideline {
        fn prose<'a>(&'a self) -> &'a str {
        return &self.prose[..];
    }
}


pub trait ParameterSelection   {

    fn how_many<'a>(&'a self) -> Option<&'a crate::ParameterCardinalityEnum>;
    // fn how_many_mut(&mut self) -> &mut Option<&'a crate::ParameterCardinalityEnum>;
    // fn set_how_many(&mut self, value: Option<&'a ParameterCardinalityEnum>);

    fn choice<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn choice_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_choice(&mut self, value: Option<&Vec<String>>);


}

impl ParameterSelection for crate::ParameterSelection {
        fn how_many<'a>(&'a self) -> Option<&'a crate::ParameterCardinalityEnum> {
        return self.how_many.as_ref();
    }
        fn choice<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.choice.as_ref();
    }
}


pub trait IncludeAll   {


}

impl IncludeAll for crate::IncludeAll {
}


pub trait ControlMatching   {

    fn remarks<'a>(&'a self) -> Option<&'a str>;
    // fn remarks_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_remarks(&mut self, value: Option<&'a str>);

    fn pattern<'a>(&'a self) -> Option<&'a str>;
    // fn pattern_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_pattern(&mut self, value: Option<&'a str>);


}

impl ControlMatching for crate::ControlMatching {
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
        fn pattern<'a>(&'a self) -> Option<&'a str> {
        return self.pattern.as_deref();
    }
}


pub trait SelectControlById   {

    fn with_child_controls<'a>(&'a self) -> Option<&'a crate::WithChildControlsEnum>;
    // fn with_child_controls_mut(&mut self) -> &mut Option<&'a crate::WithChildControlsEnum>;
    // fn set_with_child_controls(&mut self, value: Option<&'a WithChildControlsEnum>);

    fn with_ids<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn with_ids_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_with_ids(&mut self, value: Option<&Vec<String>>);

    fn matching<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::ControlMatching>>;
    // fn matching_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::ControlMatching>>;
    // fn set_matching<E>(&mut self, value: Option<&Vec<E>>) where E: Into<ControlMatching>;


}

impl SelectControlById for crate::SelectControlById {
        fn with_child_controls<'a>(&'a self) -> Option<&'a crate::WithChildControlsEnum> {
        return self.with_child_controls.as_ref();
    }
        fn with_ids<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.with_ids.as_ref();
    }
        fn matching<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::ControlMatching>> {
        return self.matching.as_ref();
    }
}


pub trait ProfileDocument : OscalDocument   {

    fn profile<'a>(&'a self) -> &'a crate::Profile;
    // fn profile_mut(&mut self) -> &mut &'a crate::Profile;
    // fn set_profile<E>(&mut self, value: E) where E: Into<Profile>;


}

impl ProfileDocument for crate::ProfileDocument {
        fn profile<'a>(&'a self) -> &'a crate::Profile {
        return &self.profile;
    }
}


pub trait Profile   {

    fn uuid<'a>(&'a self) -> &'a str;
    // fn uuid_mut(&mut self) -> &mut &'a str;
    // fn set_uuid(&mut self, value: String);

    fn metadata<'a>(&'a self) -> &'a crate::Metadata;
    // fn metadata_mut(&mut self) -> &mut &'a crate::Metadata;
    // fn set_metadata<E>(&mut self, value: E) where E: Into<Metadata>;

    fn imports<'a>(&'a self) -> impl poly_containers::SeqRef<'a, crate::ProfileImport>;
    // fn imports_mut(&mut self) -> &mut impl poly_containers::SeqRef<'a, crate::ProfileImport>;
    // fn set_imports<E>(&mut self, value: &Vec<E>) where E: Into<ProfileImport>;

    fn merge<'a>(&'a self) -> Option<&'a crate::ProfileMerge>;
    // fn merge_mut(&mut self) -> &mut Option<&'a crate::ProfileMerge>;
    // fn set_merge<E>(&mut self, value: Option<E>) where E: Into<ProfileMerge>;

    fn modify<'a>(&'a self) -> Option<&'a crate::ProfileModify>;
    // fn modify_mut(&mut self) -> &mut Option<&'a crate::ProfileModify>;
    // fn set_modify<E>(&mut self, value: Option<E>) where E: Into<ProfileModify>;

    fn back_matter<'a>(&'a self) -> Option<&'a crate::BackMatter>;
    // fn back_matter_mut(&mut self) -> &mut Option<&'a crate::BackMatter>;
    // fn set_back_matter<E>(&mut self, value: Option<E>) where E: Into<BackMatter>;


}

impl Profile for crate::Profile {
        fn uuid<'a>(&'a self) -> &'a str {
        return &self.uuid[..];
    }
        fn metadata<'a>(&'a self) -> &'a crate::Metadata {
        return &self.metadata;
    }
        fn imports<'a>(&'a self) -> impl poly_containers::SeqRef<'a, crate::ProfileImport> {
        return &self.imports;
    }
        fn merge<'a>(&'a self) -> Option<&'a crate::ProfileMerge> {
        return self.merge.as_ref();
    }
        fn modify<'a>(&'a self) -> Option<&'a crate::ProfileModify> {
        return self.modify.as_ref();
    }
        fn back_matter<'a>(&'a self) -> Option<&'a crate::BackMatter> {
        return self.back_matter.as_ref();
    }
}


pub trait ProfileImport   {

    fn href<'a>(&'a self) -> &'a str;
    // fn href_mut(&mut self) -> &mut &'a str;
    // fn set_href(&mut self, value: String);

    fn include_all<'a>(&'a self) -> Option<&'a crate::IncludeAll>;
    // fn include_all_mut(&mut self) -> &mut Option<&'a crate::IncludeAll>;
    // fn set_include_all<E>(&mut self, value: Option<E>) where E: Into<IncludeAll>;

    fn include_controls<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::SelectControlById>>;
    // fn include_controls_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::SelectControlById>>;
    // fn set_include_controls<E>(&mut self, value: Option<&Vec<E>>) where E: Into<SelectControlById>;

    fn exclude_controls<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::SelectControlById>>;
    // fn exclude_controls_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::SelectControlById>>;
    // fn set_exclude_controls<E>(&mut self, value: Option<&Vec<E>>) where E: Into<SelectControlById>;


}

impl ProfileImport for crate::ProfileImport {
        fn href<'a>(&'a self) -> &'a str {
        return &self.href[..];
    }
        fn include_all<'a>(&'a self) -> Option<&'a crate::IncludeAll> {
        return self.include_all.as_ref();
    }
        fn include_controls<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::SelectControlById>> {
        return self.include_controls.as_ref();
    }
        fn exclude_controls<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::SelectControlById>> {
        return self.exclude_controls.as_ref();
    }
}


pub trait ProfileMerge   {

    fn combine<'a>(&'a self) -> Option<&'a crate::CombinationRule>;
    // fn combine_mut(&mut self) -> &mut Option<&'a crate::CombinationRule>;
    // fn set_combine<E>(&mut self, value: Option<E>) where E: Into<CombinationRule>;

    fn flat<'a>(&'a self) -> Option<&'a crate::MergeFlat>;
    // fn flat_mut(&mut self) -> &mut Option<&'a crate::MergeFlat>;
    // fn set_flat<E>(&mut self, value: Option<E>) where E: Into<MergeFlat>;

    fn as_is(&self) -> Option<bool>;
    // fn as_is_mut(&mut self) -> &mut Option<bool>;
    // fn set_as_is(&mut self, value: Option<bool>);

    fn custom<'a>(&'a self) -> Option<&'a crate::MergeCustom>;
    // fn custom_mut(&mut self) -> &mut Option<&'a crate::MergeCustom>;
    // fn set_custom<E>(&mut self, value: Option<E>) where E: Into<MergeCustom>;


}

impl ProfileMerge for crate::ProfileMerge {
        fn combine<'a>(&'a self) -> Option<&'a crate::CombinationRule> {
        return self.combine.as_ref();
    }
        fn flat<'a>(&'a self) -> Option<&'a crate::MergeFlat> {
        return self.flat.as_ref();
    }
        fn as_is(&self) -> Option<bool> {
        return self.as_is;
    }
        fn custom<'a>(&'a self) -> Option<&'a crate::MergeCustom> {
        return self.custom.as_ref();
    }
}


pub trait CombinationRule   {

    fn method<'a>(&'a self) -> Option<&'a crate::CombinationMethodEnum>;
    // fn method_mut(&mut self) -> &mut Option<&'a crate::CombinationMethodEnum>;
    // fn set_method(&mut self, value: Option<&'a CombinationMethodEnum>);


}

impl CombinationRule for crate::CombinationRule {
        fn method<'a>(&'a self) -> Option<&'a crate::CombinationMethodEnum> {
        return self.method.as_ref();
    }
}


pub trait MergeFlat   {


}

impl MergeFlat for crate::MergeFlat {
}


pub trait MergeCustom   {

    fn groups<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::ProfileGroup>>;
    // fn groups_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::ProfileGroup>>;
    // fn set_groups<E>(&mut self, value: Option<&Vec<E>>) where E: Into<ProfileGroup>;

    fn insert_controls<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::InsertControls>>;
    // fn insert_controls_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::InsertControls>>;
    // fn set_insert_controls<E>(&mut self, value: Option<&Vec<E>>) where E: Into<InsertControls>;


}

impl MergeCustom for crate::MergeCustom {
        fn groups<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::ProfileGroup>> {
        return self.groups.as_ref();
    }
        fn insert_controls<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::InsertControls>> {
        return self.insert_controls.as_ref();
    }
}


pub trait ProfileGroup : OscalCommon   {

    fn id<'a>(&'a self) -> Option<&'a str>;
    // fn id_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_id(&mut self, value: Option<&'a str>);

    fn _class<'a>(&'a self) -> Option<&'a str>;
    // fn _class_mut(&mut self) -> &mut Option<&'a str>;
    // fn set__class(&mut self, value: Option<&'a str>);

    fn title<'a>(&'a self) -> &'a str;
    // fn title_mut(&mut self) -> &mut &'a str;
    // fn set_title(&mut self, value: String);

    fn params<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Parameter>>;
    // fn params_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::Parameter>>;
    // fn set_params<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Parameter>;

    fn parts<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Part>>;
    // fn parts_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::Part>>;
    // fn set_parts<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Part>;

    fn groups<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::ProfileGroup>>;
    // fn groups_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::ProfileGroup>>;
    // fn set_groups<E>(&mut self, value: Option<&Vec<E>>) where E: Into<ProfileGroup>;

    fn insert_controls<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::InsertControls>>;
    // fn insert_controls_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::InsertControls>>;
    // fn set_insert_controls<E>(&mut self, value: Option<&Vec<E>>) where E: Into<InsertControls>;


}

impl ProfileGroup for crate::ProfileGroup {
        fn id<'a>(&'a self) -> Option<&'a str> {
        return self.id.as_deref();
    }
        fn _class<'a>(&'a self) -> Option<&'a str> {
        return self._class.as_deref();
    }
        fn title<'a>(&'a self) -> &'a str {
        return &self.title[..];
    }
        fn params<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Parameter>> {
        return self.params.as_ref();
    }
        fn parts<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Part>> {
        return self.parts.as_ref();
    }
        fn groups<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::ProfileGroup>> {
        return self.groups.as_ref().map(|x| poly_containers::ListView::new(x));
    }
        fn insert_controls<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::InsertControls>> {
        return self.insert_controls.as_ref();
    }
}


pub trait ProfileModify   {

    fn set_parameters<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::ParameterSetting>>;
    // fn set_parameters_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::ParameterSetting>>;
    // fn set_set_parameters<E>(&mut self, value: Option<&Vec<E>>) where E: Into<ParameterSetting>;

    fn alters<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Alteration>>;
    // fn alters_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::Alteration>>;
    // fn set_alters<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Alteration>;


}

impl ProfileModify for crate::ProfileModify {
        fn set_parameters<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::ParameterSetting>> {
        return self.set_parameters.as_ref();
    }
        fn alters<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Alteration>> {
        return self.alters.as_ref();
    }
}


pub trait ParameterSetting : HasPropsAndLinks   {

    fn param_id<'a>(&'a self) -> &'a str;
    // fn param_id_mut(&mut self) -> &mut &'a str;
    // fn set_param_id(&mut self, value: String);

    fn _class<'a>(&'a self) -> Option<&'a str>;
    // fn _class_mut(&mut self) -> &mut Option<&'a str>;
    // fn set__class(&mut self, value: Option<&'a str>);

    fn depends_on<'a>(&'a self) -> Option<&'a str>;
    // fn depends_on_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_depends_on(&mut self, value: Option<&'a str>);

    fn label<'a>(&'a self) -> Option<&'a str>;
    // fn label_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_label(&mut self, value: Option<&'a str>);

    fn usage<'a>(&'a self) -> Option<&'a str>;
    // fn usage_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_usage(&mut self, value: Option<&'a str>);

    fn constraints<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::ParameterConstraint>>;
    // fn constraints_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::ParameterConstraint>>;
    // fn set_constraints<E>(&mut self, value: Option<&Vec<E>>) where E: Into<ParameterConstraint>;

    fn guidelines<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::ParameterGuideline>>;
    // fn guidelines_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::ParameterGuideline>>;
    // fn set_guidelines<E>(&mut self, value: Option<&Vec<E>>) where E: Into<ParameterGuideline>;

    fn values<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn values_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_values(&mut self, value: Option<&Vec<String>>);

    fn select<'a>(&'a self) -> Option<&'a crate::ParameterSelection>;
    // fn select_mut(&mut self) -> &mut Option<&'a crate::ParameterSelection>;
    // fn set_select<E>(&mut self, value: Option<E>) where E: Into<ParameterSelection>;


}

impl ParameterSetting for crate::ParameterSetting {
        fn param_id<'a>(&'a self) -> &'a str {
        return &self.param_id[..];
    }
        fn _class<'a>(&'a self) -> Option<&'a str> {
        return self._class.as_deref();
    }
        fn depends_on<'a>(&'a self) -> Option<&'a str> {
        return self.depends_on.as_deref();
    }
        fn label<'a>(&'a self) -> Option<&'a str> {
        return self.label.as_deref();
    }
        fn usage<'a>(&'a self) -> Option<&'a str> {
        return self.usage.as_deref();
    }
        fn constraints<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::ParameterConstraint>> {
        return self.constraints.as_ref();
    }
        fn guidelines<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::ParameterGuideline>> {
        return self.guidelines.as_ref();
    }
        fn values<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.values.as_ref();
    }
        fn select<'a>(&'a self) -> Option<&'a crate::ParameterSelection> {
        return self.select.as_ref();
    }
}


pub trait Alteration   {

    fn control_id<'a>(&'a self) -> &'a str;
    // fn control_id_mut(&mut self) -> &mut &'a str;
    // fn set_control_id(&mut self, value: String);

    fn removes<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Removal>>;
    // fn removes_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::Removal>>;
    // fn set_removes<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Removal>;

    fn adds<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Addition>>;
    // fn adds_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::Addition>>;
    // fn set_adds<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Addition>;


}

impl Alteration for crate::Alteration {
        fn control_id<'a>(&'a self) -> &'a str {
        return &self.control_id[..];
    }
        fn removes<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Removal>> {
        return self.removes.as_ref();
    }
        fn adds<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Addition>> {
        return self.adds.as_ref();
    }
}


pub trait Removal   {

    fn by_name<'a>(&'a self) -> Option<&'a str>;
    // fn by_name_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_by_name(&mut self, value: Option<&'a str>);

    fn by_class<'a>(&'a self) -> Option<&'a str>;
    // fn by_class_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_by_class(&mut self, value: Option<&'a str>);

    fn by_id<'a>(&'a self) -> Option<&'a str>;
    // fn by_id_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_by_id(&mut self, value: Option<&'a str>);

    fn by_item_name<'a>(&'a self) -> Option<&'a crate::ByItemNameEnum>;
    // fn by_item_name_mut(&mut self) -> &mut Option<&'a crate::ByItemNameEnum>;
    // fn set_by_item_name(&mut self, value: Option<&'a ByItemNameEnum>);

    fn by_ns<'a>(&'a self) -> Option<&'a str>;
    // fn by_ns_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_by_ns(&mut self, value: Option<&'a str>);

    fn remarks<'a>(&'a self) -> Option<&'a str>;
    // fn remarks_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_remarks(&mut self, value: Option<&'a str>);


}

impl Removal for crate::Removal {
        fn by_name<'a>(&'a self) -> Option<&'a str> {
        return self.by_name.as_deref();
    }
        fn by_class<'a>(&'a self) -> Option<&'a str> {
        return self.by_class.as_deref();
    }
        fn by_id<'a>(&'a self) -> Option<&'a str> {
        return self.by_id.as_deref();
    }
        fn by_item_name<'a>(&'a self) -> Option<&'a crate::ByItemNameEnum> {
        return self.by_item_name.as_ref();
    }
        fn by_ns<'a>(&'a self) -> Option<&'a str> {
        return self.by_ns.as_deref();
    }
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}


pub trait Addition   {

    fn position<'a>(&'a self) -> Option<&'a crate::AdditionPositionEnum>;
    // fn position_mut(&mut self) -> &mut Option<&'a crate::AdditionPositionEnum>;
    // fn set_position(&mut self, value: Option<&'a AdditionPositionEnum>);

    fn by_id<'a>(&'a self) -> Option<&'a str>;
    // fn by_id_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_by_id(&mut self, value: Option<&'a str>);

    fn title<'a>(&'a self) -> Option<&'a str>;
    // fn title_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_title(&mut self, value: Option<&'a str>);

    fn params<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Parameter>>;
    // fn params_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::Parameter>>;
    // fn set_params<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Parameter>;

    fn props<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::ProfileAlterationProperty>>;
    // fn props_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::ProfileAlterationProperty>>;
    // fn set_props<E>(&mut self, value: Option<&Vec<E>>) where E: Into<ProfileAlterationProperty>;

    fn links<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, LinkOrSubtype>>;
    // fn links_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, LinkOrSubtype>>;
    // fn set_links<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Link>;

    fn parts<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Part>>;
    // fn parts_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::Part>>;
    // fn set_parts<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Part>;


}

impl Addition for crate::Addition {
        fn position<'a>(&'a self) -> Option<&'a crate::AdditionPositionEnum> {
        return self.position.as_ref();
    }
        fn by_id<'a>(&'a self) -> Option<&'a str> {
        return self.by_id.as_deref();
    }
        fn title<'a>(&'a self) -> Option<&'a str> {
        return self.title.as_deref();
    }
        fn params<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Parameter>> {
        return self.params.as_ref();
    }
        fn props<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::ProfileAlterationProperty>> {
        return self.props.as_ref();
    }
        fn links<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, LinkOrSubtype>> {
        return self.links.as_ref();
    }
        fn parts<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Part>> {
        return self.parts.as_ref();
    }
}


pub trait ProfileAlterationProperty : Property   {


}

impl ProfileAlterationProperty for crate::ProfileAlterationProperty {
}


pub trait InsertControls   {

    fn order<'a>(&'a self) -> Option<&'a crate::InsertOrderEnum>;
    // fn order_mut(&mut self) -> &mut Option<&'a crate::InsertOrderEnum>;
    // fn set_order(&mut self, value: Option<&'a InsertOrderEnum>);

    fn include_all<'a>(&'a self) -> Option<&'a crate::IncludeAll>;
    // fn include_all_mut(&mut self) -> &mut Option<&'a crate::IncludeAll>;
    // fn set_include_all<E>(&mut self, value: Option<E>) where E: Into<IncludeAll>;

    fn include_controls<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::SelectControlById>>;
    // fn include_controls_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::SelectControlById>>;
    // fn set_include_controls<E>(&mut self, value: Option<&Vec<E>>) where E: Into<SelectControlById>;

    fn exclude_controls<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::SelectControlById>>;
    // fn exclude_controls_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::SelectControlById>>;
    // fn set_exclude_controls<E>(&mut self, value: Option<&Vec<E>>) where E: Into<SelectControlById>;


}

impl InsertControls for crate::InsertControls {
        fn order<'a>(&'a self) -> Option<&'a crate::InsertOrderEnum> {
        return self.order.as_ref();
    }
        fn include_all<'a>(&'a self) -> Option<&'a crate::IncludeAll> {
        return self.include_all.as_ref();
    }
        fn include_controls<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::SelectControlById>> {
        return self.include_controls.as_ref();
    }
        fn exclude_controls<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::SelectControlById>> {
        return self.exclude_controls.as_ref();
    }
}


pub trait AssessmentPlanDocument : OscalDocument   {

    fn assessment_plan<'a>(&'a self) -> &'a crate::AssessmentPlan;
    // fn assessment_plan_mut(&mut self) -> &mut &'a crate::AssessmentPlan;
    // fn set_assessment_plan<E>(&mut self, value: E) where E: Into<AssessmentPlan>;


}

impl AssessmentPlanDocument for crate::AssessmentPlanDocument {
        fn assessment_plan<'a>(&'a self) -> &'a crate::AssessmentPlan {
        return &self.assessment_plan;
    }
}


pub trait AssessmentPlan   {

    fn uuid<'a>(&'a self) -> &'a str;
    // fn uuid_mut(&mut self) -> &mut &'a str;
    // fn set_uuid(&mut self, value: String);

    fn metadata<'a>(&'a self) -> &'a crate::Metadata;
    // fn metadata_mut(&mut self) -> &mut &'a crate::Metadata;
    // fn set_metadata<E>(&mut self, value: E) where E: Into<Metadata>;

    fn import_ssp<'a>(&'a self) -> &'a crate::ImportSSP;
    // fn import_ssp_mut(&mut self) -> &mut &'a crate::ImportSSP;
    // fn set_import_ssp<E>(&mut self, value: E) where E: Into<ImportSSP>;

    fn local_definitions<'a>(&'a self) -> Option<&'a crate::LocalDefinitions>;
    // fn local_definitions_mut(&mut self) -> &mut Option<&'a crate::LocalDefinitions>;
    // fn set_local_definitions<E>(&mut self, value: Option<E>) where E: Into<LocalDefinitions>;

    fn terms_and_conditions<'a>(&'a self) -> Option<&'a crate::TermsAndConditions>;
    // fn terms_and_conditions_mut(&mut self) -> &mut Option<&'a crate::TermsAndConditions>;
    // fn set_terms_and_conditions<E>(&mut self, value: Option<E>) where E: Into<TermsAndConditions>;

    fn assessment_subjects<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::AssessmentSubject>>;
    // fn assessment_subjects_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::AssessmentSubject>>;
    // fn set_assessment_subjects<E>(&mut self, value: Option<&Vec<E>>) where E: Into<AssessmentSubject>;

    fn assessment_assets<'a>(&'a self) -> Option<&'a crate::AssessmentAssets>;
    // fn assessment_assets_mut(&mut self) -> &mut Option<&'a crate::AssessmentAssets>;
    // fn set_assessment_assets<E>(&mut self, value: Option<E>) where E: Into<AssessmentAssets>;

    fn reviewed_controls<'a>(&'a self) -> &'a crate::ReviewedControls;
    // fn reviewed_controls_mut(&mut self) -> &mut &'a crate::ReviewedControls;
    // fn set_reviewed_controls<E>(&mut self, value: E) where E: Into<ReviewedControls>;

    fn tasks<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Task>>;
    // fn tasks_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::Task>>;
    // fn set_tasks<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Task>;

    fn back_matter<'a>(&'a self) -> Option<&'a crate::BackMatter>;
    // fn back_matter_mut(&mut self) -> &mut Option<&'a crate::BackMatter>;
    // fn set_back_matter<E>(&mut self, value: Option<E>) where E: Into<BackMatter>;


}

impl AssessmentPlan for crate::AssessmentPlan {
        fn uuid<'a>(&'a self) -> &'a str {
        return &self.uuid[..];
    }
        fn metadata<'a>(&'a self) -> &'a crate::Metadata {
        return &self.metadata;
    }
        fn import_ssp<'a>(&'a self) -> &'a crate::ImportSSP {
        return &self.import_ssp;
    }
        fn local_definitions<'a>(&'a self) -> Option<&'a crate::LocalDefinitions> {
        return self.local_definitions.as_ref();
    }
        fn terms_and_conditions<'a>(&'a self) -> Option<&'a crate::TermsAndConditions> {
        return self.terms_and_conditions.as_ref();
    }
        fn assessment_subjects<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::AssessmentSubject>> {
        return self.assessment_subjects.as_ref();
    }
        fn assessment_assets<'a>(&'a self) -> Option<&'a crate::AssessmentAssets> {
        return self.assessment_assets.as_ref();
    }
        fn reviewed_controls<'a>(&'a self) -> &'a crate::ReviewedControls {
        return &self.reviewed_controls;
    }
        fn tasks<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Task>> {
        return self.tasks.as_ref();
    }
        fn back_matter<'a>(&'a self) -> Option<&'a crate::BackMatter> {
        return self.back_matter.as_ref();
    }
}


pub trait ImportSSP   {

    fn href<'a>(&'a self) -> &'a str;
    // fn href_mut(&mut self) -> &mut &'a str;
    // fn set_href(&mut self, value: String);

    fn remarks<'a>(&'a self) -> Option<&'a str>;
    // fn remarks_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_remarks(&mut self, value: Option<&'a str>);


}

impl ImportSSP for crate::ImportSSP {
        fn href<'a>(&'a self) -> &'a str {
        return &self.href[..];
    }
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}


pub trait LocalDefinitions   {

    fn components<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, SystemComponentOrSubtype>>;
    // fn components_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, SystemComponentOrSubtype>>;
    // fn set_components<E>(&mut self, value: Option<&Vec<E>>) where E: Into<SystemComponent>;

    fn inventory_items<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, InventoryItemOrSubtype>>;
    // fn inventory_items_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, InventoryItemOrSubtype>>;
    // fn set_inventory_items<E>(&mut self, value: Option<&Vec<E>>) where E: Into<InventoryItem>;

    fn users<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::SystemUser>>;
    // fn users_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::SystemUser>>;
    // fn set_users<E>(&mut self, value: Option<&Vec<E>>) where E: Into<SystemUser>;

    fn objectives_and_methods<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::LocalObjective>>;
    // fn objectives_and_methods_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::LocalObjective>>;
    // fn set_objectives_and_methods<E>(&mut self, value: Option<&Vec<E>>) where E: Into<LocalObjective>;

    fn activities<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Activity>>;
    // fn activities_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::Activity>>;
    // fn set_activities<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Activity>;

    fn remarks<'a>(&'a self) -> Option<&'a str>;
    // fn remarks_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_remarks(&mut self, value: Option<&'a str>);


}

impl LocalDefinitions for crate::LocalDefinitions {
        fn components<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, SystemComponentOrSubtype>> {
        return self.components.as_ref();
    }
        fn inventory_items<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, InventoryItemOrSubtype>> {
        return self.inventory_items.as_ref();
    }
        fn users<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::SystemUser>> {
        return self.users.as_ref();
    }
        fn objectives_and_methods<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::LocalObjective>> {
        return self.objectives_and_methods.as_ref();
    }
        fn activities<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Activity>> {
        return self.activities.as_ref();
    }
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}


pub trait TermsAndConditions   {

    fn parts<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::TermsAndConditionsPart>>;
    // fn parts_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::TermsAndConditionsPart>>;
    // fn set_parts<E>(&mut self, value: Option<&Vec<E>>) where E: Into<TermsAndConditionsPart>;


}

impl TermsAndConditions for crate::TermsAndConditions {
        fn parts<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::TermsAndConditionsPart>> {
        return self.parts.as_ref();
    }
}


pub trait ReviewedControls : OscalCommon   {

    fn description<'a>(&'a self) -> Option<&'a str>;
    // fn description_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_description(&mut self, value: Option<&'a str>);

    fn control_selections<'a>(&'a self) -> impl poly_containers::SeqRef<'a, crate::ControlSelection>;
    // fn control_selections_mut(&mut self) -> &mut impl poly_containers::SeqRef<'a, crate::ControlSelection>;
    // fn set_control_selections<E>(&mut self, value: &Vec<E>) where E: Into<ControlSelection>;

    fn control_objective_selections<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::ControlObjectiveSelection>>;
    // fn control_objective_selections_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::ControlObjectiveSelection>>;
    // fn set_control_objective_selections<E>(&mut self, value: Option<&Vec<E>>) where E: Into<ControlObjectiveSelection>;


}

impl ReviewedControls for crate::ReviewedControls {
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn control_selections<'a>(&'a self) -> impl poly_containers::SeqRef<'a, crate::ControlSelection> {
        return &self.control_selections;
    }
        fn control_objective_selections<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::ControlObjectiveSelection>> {
        return self.control_objective_selections.as_ref();
    }
}


pub trait ControlSelection : OscalCommon   {

    fn description<'a>(&'a self) -> Option<&'a str>;
    // fn description_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_description(&mut self, value: Option<&'a str>);

    fn include_all<'a>(&'a self) -> Option<&'a crate::IncludeAll>;
    // fn include_all_mut(&mut self) -> &mut Option<&'a crate::IncludeAll>;
    // fn set_include_all<E>(&mut self, value: Option<E>) where E: Into<IncludeAll>;

    fn include_controls<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::AssessmentSelectControlById>>;
    // fn include_controls_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::AssessmentSelectControlById>>;
    // fn set_include_controls<E>(&mut self, value: Option<&Vec<E>>) where E: Into<AssessmentSelectControlById>;

    fn exclude_controls<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::AssessmentSelectControlById>>;
    // fn exclude_controls_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::AssessmentSelectControlById>>;
    // fn set_exclude_controls<E>(&mut self, value: Option<&Vec<E>>) where E: Into<AssessmentSelectControlById>;


}

impl ControlSelection for crate::ControlSelection {
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn include_all<'a>(&'a self) -> Option<&'a crate::IncludeAll> {
        return self.include_all.as_ref();
    }
        fn include_controls<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::AssessmentSelectControlById>> {
        return self.include_controls.as_ref();
    }
        fn exclude_controls<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::AssessmentSelectControlById>> {
        return self.exclude_controls.as_ref();
    }
}


pub trait ControlObjectiveSelection : OscalCommon   {

    fn description<'a>(&'a self) -> Option<&'a str>;
    // fn description_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_description(&mut self, value: Option<&'a str>);

    fn include_all<'a>(&'a self) -> Option<&'a crate::IncludeAll>;
    // fn include_all_mut(&mut self) -> &mut Option<&'a crate::IncludeAll>;
    // fn set_include_all<E>(&mut self, value: Option<E>) where E: Into<IncludeAll>;

    fn include_objectives<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::SelectObjectiveById>>;
    // fn include_objectives_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::SelectObjectiveById>>;
    // fn set_include_objectives<E>(&mut self, value: Option<&Vec<E>>) where E: Into<SelectObjectiveById>;

    fn exclude_objectives<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::SelectObjectiveById>>;
    // fn exclude_objectives_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::SelectObjectiveById>>;
    // fn set_exclude_objectives<E>(&mut self, value: Option<&Vec<E>>) where E: Into<SelectObjectiveById>;


}

impl ControlObjectiveSelection for crate::ControlObjectiveSelection {
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn include_all<'a>(&'a self) -> Option<&'a crate::IncludeAll> {
        return self.include_all.as_ref();
    }
        fn include_objectives<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::SelectObjectiveById>> {
        return self.include_objectives.as_ref();
    }
        fn exclude_objectives<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::SelectObjectiveById>> {
        return self.exclude_objectives.as_ref();
    }
}


pub trait AssessmentSelectControlById   {

    fn control_id<'a>(&'a self) -> &'a str;
    // fn control_id_mut(&mut self) -> &mut &'a str;
    // fn set_control_id(&mut self, value: String);

    fn statement_ids<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn statement_ids_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_statement_ids(&mut self, value: Option<&Vec<String>>);


}

impl AssessmentSelectControlById for crate::AssessmentSelectControlById {
        fn control_id<'a>(&'a self) -> &'a str {
        return &self.control_id[..];
    }
        fn statement_ids<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.statement_ids.as_ref();
    }
}


pub trait SelectObjectiveById   {

    fn objective_id<'a>(&'a self) -> &'a str;
    // fn objective_id_mut(&mut self) -> &mut &'a str;
    // fn set_objective_id(&mut self, value: String);

    fn remarks<'a>(&'a self) -> Option<&'a str>;
    // fn remarks_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_remarks(&mut self, value: Option<&'a str>);


}

impl SelectObjectiveById for crate::SelectObjectiveById {
        fn objective_id<'a>(&'a self) -> &'a str {
        return &self.objective_id[..];
    }
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}


pub trait AssessmentSubject : OscalCommon   {

    fn type_(&self) -> assessment_subject_utl::type__range;
    // fn type__mut(&mut self) -> &mut assessment_subject_utl::type__range;
    // fn set_type_(&mut self, value: assessment_subject_utl::type__range);

    fn description<'a>(&'a self) -> Option<&'a str>;
    // fn description_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_description(&mut self, value: Option<&'a str>);

    fn include_all<'a>(&'a self) -> Option<&'a crate::IncludeAll>;
    // fn include_all_mut(&mut self) -> &mut Option<&'a crate::IncludeAll>;
    // fn set_include_all<E>(&mut self, value: Option<E>) where E: Into<IncludeAll>;

    fn include_subjects<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::SelectSubjectById>>;
    // fn include_subjects_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::SelectSubjectById>>;
    // fn set_include_subjects<E>(&mut self, value: Option<&Vec<E>>) where E: Into<SelectSubjectById>;

    fn exclude_subjects<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::SelectSubjectById>>;
    // fn exclude_subjects_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::SelectSubjectById>>;
    // fn set_exclude_subjects<E>(&mut self, value: Option<&Vec<E>>) where E: Into<SelectSubjectById>;


}

impl AssessmentSubject for crate::AssessmentSubject {
        fn type_(&self) -> assessment_subject_utl::type__range {
            self.type_.clone()
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn include_all<'a>(&'a self) -> Option<&'a crate::IncludeAll> {
        return self.include_all.as_ref();
    }
        fn include_subjects<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::SelectSubjectById>> {
        return self.include_subjects.as_ref();
    }
        fn exclude_subjects<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::SelectSubjectById>> {
        return self.exclude_subjects.as_ref();
    }
}


pub trait SelectSubjectById : OscalCommon   {

    fn subject_uuid<'a>(&'a self) -> &'a str;
    // fn subject_uuid_mut(&mut self) -> &mut &'a str;
    // fn set_subject_uuid(&mut self, value: String);

    fn type_(&self) -> select_subject_by_id_utl::type__range;
    // fn type__mut(&mut self) -> &mut select_subject_by_id_utl::type__range;
    // fn set_type_(&mut self, value: select_subject_by_id_utl::type__range);


}

impl SelectSubjectById for crate::SelectSubjectById {
        fn subject_uuid<'a>(&'a self) -> &'a str {
        return &self.subject_uuid[..];
    }
        fn type_(&self) -> select_subject_by_id_utl::type__range {
            self.type_.clone()
    }
}


pub trait SubjectReference : OscalCommon   {

    fn subject_uuid<'a>(&'a self) -> &'a str;
    // fn subject_uuid_mut(&mut self) -> &mut &'a str;
    // fn set_subject_uuid(&mut self, value: String);

    fn type_(&self) -> subject_reference_utl::type__range;
    // fn type__mut(&mut self) -> &mut subject_reference_utl::type__range;
    // fn set_type_(&mut self, value: subject_reference_utl::type__range);

    fn title<'a>(&'a self) -> Option<&'a str>;
    // fn title_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_title(&mut self, value: Option<&'a str>);


}

impl SubjectReference for crate::SubjectReference {
        fn subject_uuid<'a>(&'a self) -> &'a str {
        return &self.subject_uuid[..];
    }
        fn type_(&self) -> subject_reference_utl::type__range {
            self.type_.clone()
    }
        fn title<'a>(&'a self) -> Option<&'a str> {
        return self.title.as_deref();
    }
}


pub trait AssessmentSubjectPlaceholder : OscalCommon   {

    fn uuid<'a>(&'a self) -> &'a str;
    // fn uuid_mut(&mut self) -> &mut &'a str;
    // fn set_uuid(&mut self, value: String);

    fn description<'a>(&'a self) -> Option<&'a str>;
    // fn description_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_description(&mut self, value: Option<&'a str>);

    fn sources<'a>(&'a self) -> impl poly_containers::SeqRef<'a, crate::AssessmentSubjectSource>;
    // fn sources_mut(&mut self) -> &mut impl poly_containers::SeqRef<'a, crate::AssessmentSubjectSource>;
    // fn set_sources<E>(&mut self, value: &Vec<E>) where E: Into<AssessmentSubjectSource>;


}

impl AssessmentSubjectPlaceholder for crate::AssessmentSubjectPlaceholder {
        fn uuid<'a>(&'a self) -> &'a str {
        return &self.uuid[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn sources<'a>(&'a self) -> impl poly_containers::SeqRef<'a, crate::AssessmentSubjectSource> {
        return &self.sources;
    }
}


pub trait AssessmentSubjectSource   {

    fn task_uuid<'a>(&'a self) -> &'a str;
    // fn task_uuid_mut(&mut self) -> &mut &'a str;
    // fn set_task_uuid(&mut self, value: String);

    fn remarks<'a>(&'a self) -> Option<&'a str>;
    // fn remarks_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_remarks(&mut self, value: Option<&'a str>);


}

impl AssessmentSubjectSource for crate::AssessmentSubjectSource {
        fn task_uuid<'a>(&'a self) -> &'a str {
        return &self.task_uuid[..];
    }
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}


pub trait AssessmentAssets   {

    fn components<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, SystemComponentOrSubtype>>;
    // fn components_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, SystemComponentOrSubtype>>;
    // fn set_components<E>(&mut self, value: Option<&Vec<E>>) where E: Into<SystemComponent>;

    fn assessment_platforms<'a>(&'a self) -> impl poly_containers::SeqRef<'a, crate::AssessmentPlatform>;
    // fn assessment_platforms_mut(&mut self) -> &mut impl poly_containers::SeqRef<'a, crate::AssessmentPlatform>;
    // fn set_assessment_platforms<E>(&mut self, value: &Vec<E>) where E: Into<AssessmentPlatform>;


}

impl AssessmentAssets for crate::AssessmentAssets {
        fn components<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, SystemComponentOrSubtype>> {
        return self.components.as_ref();
    }
        fn assessment_platforms<'a>(&'a self) -> impl poly_containers::SeqRef<'a, crate::AssessmentPlatform> {
        return &self.assessment_platforms;
    }
}


pub trait AssessmentPlatform : OscalCommon   {

    fn uuid<'a>(&'a self) -> &'a str;
    // fn uuid_mut(&mut self) -> &mut &'a str;
    // fn set_uuid(&mut self, value: String);

    fn title<'a>(&'a self) -> Option<&'a str>;
    // fn title_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_title(&mut self, value: Option<&'a str>);

    fn uses_components<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::UsesComponent>>;
    // fn uses_components_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::UsesComponent>>;
    // fn set_uses_components<E>(&mut self, value: Option<&Vec<E>>) where E: Into<UsesComponent>;


}

impl AssessmentPlatform for crate::AssessmentPlatform {
        fn uuid<'a>(&'a self) -> &'a str {
        return &self.uuid[..];
    }
        fn title<'a>(&'a self) -> Option<&'a str> {
        return self.title.as_deref();
    }
        fn uses_components<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::UsesComponent>> {
        return self.uses_components.as_ref();
    }
}


pub trait UsesComponent : OscalCommon  +  HasResponsibleParties   {

    fn component_uuid<'a>(&'a self) -> &'a str;
    // fn component_uuid_mut(&mut self) -> &mut &'a str;
    // fn set_component_uuid(&mut self, value: String);


}

impl UsesComponent for crate::UsesComponent {
        fn component_uuid<'a>(&'a self) -> &'a str {
        return &self.component_uuid[..];
    }
}


pub trait LocalObjective : OscalCommon   {

    fn control_id<'a>(&'a self) -> &'a str;
    // fn control_id_mut(&mut self) -> &mut &'a str;
    // fn set_control_id(&mut self, value: String);

    fn description<'a>(&'a self) -> Option<&'a str>;
    // fn description_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_description(&mut self, value: Option<&'a str>);

    fn parts<'a>(&'a self) -> impl poly_containers::SeqRef<'a, crate::ControlPart>;
    // fn parts_mut(&mut self) -> &mut impl poly_containers::SeqRef<'a, crate::ControlPart>;
    // fn set_parts<E>(&mut self, value: &Vec<E>) where E: Into<ControlPart>;


}

impl LocalObjective for crate::LocalObjective {
        fn control_id<'a>(&'a self) -> &'a str {
        return &self.control_id[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn parts<'a>(&'a self) -> impl poly_containers::SeqRef<'a, crate::ControlPart> {
        return &self.parts;
    }
}


pub trait AssessmentMethod : OscalCommon   {

    fn uuid<'a>(&'a self) -> &'a str;
    // fn uuid_mut(&mut self) -> &mut &'a str;
    // fn set_uuid(&mut self, value: String);

    fn description<'a>(&'a self) -> Option<&'a str>;
    // fn description_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_description(&mut self, value: Option<&'a str>);

    fn part<'a>(&'a self) -> &'a AssessmentPartOrSubtype;
    // fn part_mut(&mut self) -> &mut &'a AssessmentPartOrSubtype;
    // fn set_part<E>(&mut self, value: E) where E: Into<AssessmentPart>;


}

impl AssessmentMethod for crate::AssessmentMethod {
        fn uuid<'a>(&'a self) -> &'a str {
        return &self.uuid[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn part<'a>(&'a self) -> &'a AssessmentPartOrSubtype {
        return &self.part;
    }
}


pub trait Activity : OscalCommon  +  HasResponsibleRoles   {

    fn uuid<'a>(&'a self) -> &'a str;
    // fn uuid_mut(&mut self) -> &mut &'a str;
    // fn set_uuid(&mut self, value: String);

    fn title<'a>(&'a self) -> Option<&'a str>;
    // fn title_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_title(&mut self, value: Option<&'a str>);

    fn description<'a>(&'a self) -> &'a str;
    // fn description_mut(&mut self) -> &mut &'a str;
    // fn set_description(&mut self, value: String);

    fn steps<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Step>>;
    // fn steps_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::Step>>;
    // fn set_steps<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Step>;

    fn related_controls<'a>(&'a self) -> Option<&'a crate::ReviewedControls>;
    // fn related_controls_mut(&mut self) -> &mut Option<&'a crate::ReviewedControls>;
    // fn set_related_controls<E>(&mut self, value: Option<E>) where E: Into<ReviewedControls>;


}

impl Activity for crate::Activity {
        fn uuid<'a>(&'a self) -> &'a str {
        return &self.uuid[..];
    }
        fn title<'a>(&'a self) -> Option<&'a str> {
        return self.title.as_deref();
    }
        fn description<'a>(&'a self) -> &'a str {
        return &self.description[..];
    }
        fn steps<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Step>> {
        return self.steps.as_ref();
    }
        fn related_controls<'a>(&'a self) -> Option<&'a crate::ReviewedControls> {
        return self.related_controls.as_ref();
    }
}


pub trait Step : OscalCommon  +  HasResponsibleRoles   {

    fn uuid<'a>(&'a self) -> &'a str;
    // fn uuid_mut(&mut self) -> &mut &'a str;
    // fn set_uuid(&mut self, value: String);

    fn title<'a>(&'a self) -> Option<&'a str>;
    // fn title_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_title(&mut self, value: Option<&'a str>);

    fn description<'a>(&'a self) -> &'a str;
    // fn description_mut(&mut self) -> &mut &'a str;
    // fn set_description(&mut self, value: String);

    fn reviewed_controls<'a>(&'a self) -> Option<&'a crate::ReviewedControls>;
    // fn reviewed_controls_mut(&mut self) -> &mut Option<&'a crate::ReviewedControls>;
    // fn set_reviewed_controls<E>(&mut self, value: Option<E>) where E: Into<ReviewedControls>;


}

impl Step for crate::Step {
        fn uuid<'a>(&'a self) -> &'a str {
        return &self.uuid[..];
    }
        fn title<'a>(&'a self) -> Option<&'a str> {
        return self.title.as_deref();
    }
        fn description<'a>(&'a self) -> &'a str {
        return &self.description[..];
    }
        fn reviewed_controls<'a>(&'a self) -> Option<&'a crate::ReviewedControls> {
        return self.reviewed_controls.as_ref();
    }
}


pub trait Task : OscalCommon  +  HasResponsibleRoles   {

    fn uuid<'a>(&'a self) -> &'a str;
    // fn uuid_mut(&mut self) -> &mut &'a str;
    // fn set_uuid(&mut self, value: String);

    fn type_(&self) -> task_utl::type__range;
    // fn type__mut(&mut self) -> &mut task_utl::type__range;
    // fn set_type_(&mut self, value: task_utl::type__range);

    fn title<'a>(&'a self) -> &'a str;
    // fn title_mut(&mut self) -> &mut &'a str;
    // fn set_title(&mut self, value: String);

    fn description<'a>(&'a self) -> Option<&'a str>;
    // fn description_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_description(&mut self, value: Option<&'a str>);

    fn timing<'a>(&'a self) -> Option<&'a crate::EventTiming>;
    // fn timing_mut(&mut self) -> &mut Option<&'a crate::EventTiming>;
    // fn set_timing<E>(&mut self, value: Option<E>) where E: Into<EventTiming>;

    fn dependencies<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::TaskDependency>>;
    // fn dependencies_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::TaskDependency>>;
    // fn set_dependencies<E>(&mut self, value: Option<&Vec<E>>) where E: Into<TaskDependency>;

    fn associated_activities<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::AssociatedActivity>>;
    // fn associated_activities_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::AssociatedActivity>>;
    // fn set_associated_activities<E>(&mut self, value: Option<&Vec<E>>) where E: Into<AssociatedActivity>;

    fn tasks<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Task>>;
    // fn tasks_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::Task>>;
    // fn set_tasks<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Task>;

    fn subjects<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::AssessmentSubject>>;
    // fn subjects_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::AssessmentSubject>>;
    // fn set_subjects<E>(&mut self, value: Option<&Vec<E>>) where E: Into<AssessmentSubject>;


}

impl Task for crate::Task {
        fn uuid<'a>(&'a self) -> &'a str {
        return &self.uuid[..];
    }
        fn type_(&self) -> task_utl::type__range {
            self.type_.clone()
    }
        fn title<'a>(&'a self) -> &'a str {
        return &self.title[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn timing<'a>(&'a self) -> Option<&'a crate::EventTiming> {
        return self.timing.as_ref();
    }
        fn dependencies<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::TaskDependency>> {
        return self.dependencies.as_ref();
    }
        fn associated_activities<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::AssociatedActivity>> {
        return self.associated_activities.as_ref();
    }
        fn tasks<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Task>> {
        return self.tasks.as_ref().map(|x| poly_containers::ListView::new(x));
    }
        fn subjects<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::AssessmentSubject>> {
        return self.subjects.as_ref();
    }
}


pub trait EventTiming   {

    fn on_date<'a>(&'a self) -> Option<&'a crate::OnDateCondition>;
    // fn on_date_mut(&mut self) -> &mut Option<&'a crate::OnDateCondition>;
    // fn set_on_date<E>(&mut self, value: Option<E>) where E: Into<OnDateCondition>;

    fn within_date_range<'a>(&'a self) -> Option<&'a crate::WithinDateRange>;
    // fn within_date_range_mut(&mut self) -> &mut Option<&'a crate::WithinDateRange>;
    // fn set_within_date_range<E>(&mut self, value: Option<E>) where E: Into<WithinDateRange>;

    fn at_frequency<'a>(&'a self) -> Option<&'a crate::AtFrequency>;
    // fn at_frequency_mut(&mut self) -> &mut Option<&'a crate::AtFrequency>;
    // fn set_at_frequency<E>(&mut self, value: Option<E>) where E: Into<AtFrequency>;


}

impl EventTiming for crate::EventTiming {
        fn on_date<'a>(&'a self) -> Option<&'a crate::OnDateCondition> {
        return self.on_date.as_ref();
    }
        fn within_date_range<'a>(&'a self) -> Option<&'a crate::WithinDateRange> {
        return self.within_date_range.as_ref();
    }
        fn at_frequency<'a>(&'a self) -> Option<&'a crate::AtFrequency> {
        return self.at_frequency.as_ref();
    }
}


pub trait OnDateCondition   {

    fn date<'a>(&'a self) -> &'a str;
    // fn date_mut(&mut self) -> &mut &'a str;
    // fn set_date(&mut self, value: String);

    fn remarks<'a>(&'a self) -> Option<&'a str>;
    // fn remarks_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_remarks(&mut self, value: Option<&'a str>);


}

impl OnDateCondition for crate::OnDateCondition {
        fn date<'a>(&'a self) -> &'a str {
        return &self.date[..];
    }
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}


pub trait WithinDateRange   {

    fn start<'a>(&'a self) -> &'a str;
    // fn start_mut(&mut self) -> &mut &'a str;
    // fn set_start(&mut self, value: String);

    fn end<'a>(&'a self) -> &'a str;
    // fn end_mut(&mut self) -> &mut &'a str;
    // fn set_end(&mut self, value: String);

    fn remarks<'a>(&'a self) -> Option<&'a str>;
    // fn remarks_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_remarks(&mut self, value: Option<&'a str>);


}

impl WithinDateRange for crate::WithinDateRange {
        fn start<'a>(&'a self) -> &'a str {
        return &self.start[..];
    }
        fn end<'a>(&'a self) -> &'a str {
        return &self.end[..];
    }
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}


pub trait AtFrequency   {

    fn period(&self) -> isize;
    // fn period_mut(&mut self) -> &mut isize;
    // fn set_period(&mut self, value: isize);

    fn unit<'a>(&'a self) -> &'a crate::TimingUnitEnum;
    // fn unit_mut(&mut self) -> &mut &'a crate::TimingUnitEnum;
    // fn set_unit(&mut self, value: TimingUnitEnum);

    fn remarks<'a>(&'a self) -> Option<&'a str>;
    // fn remarks_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_remarks(&mut self, value: Option<&'a str>);


}

impl AtFrequency for crate::AtFrequency {
        fn period(&self) -> isize {
        return self.period;
    }
        fn unit<'a>(&'a self) -> &'a crate::TimingUnitEnum {
        return &self.unit;
    }
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}


pub trait TaskDependency   {

    fn task_uuid<'a>(&'a self) -> &'a str;
    // fn task_uuid_mut(&mut self) -> &mut &'a str;
    // fn set_task_uuid(&mut self, value: String);

    fn remarks<'a>(&'a self) -> Option<&'a str>;
    // fn remarks_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_remarks(&mut self, value: Option<&'a str>);


}

impl TaskDependency for crate::TaskDependency {
        fn task_uuid<'a>(&'a self) -> &'a str {
        return &self.task_uuid[..];
    }
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}


pub trait AssociatedActivity : OscalCommon  +  HasResponsibleRoles   {

    fn activity_uuid<'a>(&'a self) -> &'a str;
    // fn activity_uuid_mut(&mut self) -> &mut &'a str;
    // fn set_activity_uuid(&mut self, value: String);

    fn subjects<'a>(&'a self) -> impl poly_containers::SeqRef<'a, crate::AssessmentSubject>;
    // fn subjects_mut(&mut self) -> &mut impl poly_containers::SeqRef<'a, crate::AssessmentSubject>;
    // fn set_subjects<E>(&mut self, value: &Vec<E>) where E: Into<AssessmentSubject>;


}

impl AssociatedActivity for crate::AssociatedActivity {
        fn activity_uuid<'a>(&'a self) -> &'a str {
        return &self.activity_uuid[..];
    }
        fn subjects<'a>(&'a self) -> impl poly_containers::SeqRef<'a, crate::AssessmentSubject> {
        return &self.subjects;
    }
}


pub trait AssessmentPart : HasPropsAndLinks   {

    fn uuid<'a>(&'a self) -> Option<&'a str>;
    // fn uuid_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_uuid(&mut self, value: Option<&'a str>);

    fn name(&self) -> assessment_part_utl::name_range;
    // fn name_mut(&mut self) -> &mut assessment_part_utl::name_range;
    // fn set_name(&mut self, value: assessment_part_utl::name_range);

    fn ns<'a>(&'a self) -> Option<&'a str>;
    // fn ns_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_ns(&mut self, value: Option<&'a str>);

    fn _class<'a>(&'a self) -> Option<&'a str>;
    // fn _class_mut(&mut self) -> &mut Option<&'a str>;
    // fn set__class(&mut self, value: Option<&'a str>);

    fn title<'a>(&'a self) -> Option<&'a str>;
    // fn title_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_title(&mut self, value: Option<&'a str>);

    fn prose<'a>(&'a self) -> Option<&'a str>;
    // fn prose_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_prose(&mut self, value: Option<&'a str>);

    fn parts(&self) -> Option<Vec<assessment_part_utl::parts_range>>;
    // fn parts_mut(&mut self) -> &mut Option<Vec<assessment_part_utl::parts_range>>;
    // fn set_parts<E>(&mut self, value: Option<&Vec<E>>) where E: Into<AssessmentPart>;


}

impl AssessmentPart for crate::AssessmentPart {
        fn uuid<'a>(&'a self) -> Option<&'a str> {
        return self.uuid.as_deref();
    }
        fn name(&self) -> assessment_part_utl::name_range {
            self.name.clone()
    }
        fn ns<'a>(&'a self) -> Option<&'a str> {
        return self.ns.as_deref();
    }
        fn _class<'a>(&'a self) -> Option<&'a str> {
        return self._class.as_deref();
    }
        fn title<'a>(&'a self) -> Option<&'a str> {
        return self.title.as_deref();
    }
        fn prose<'a>(&'a self) -> Option<&'a str> {
        return self.prose.as_deref();
    }
        fn parts(&self) -> Option<Vec<assessment_part_utl::parts_range>> {
        self.parts.as_ref().map(|xs| xs.iter().map(|v| assessment_part_utl::parts_range::AssessmentPart(v.clone())).collect())
    }
}
impl AssessmentPart for crate::TermsAndConditionsPart {
        fn uuid<'a>(&'a self) -> Option<&'a str> {
        return self.uuid.as_deref();
    }
        fn name(&self) -> assessment_part_utl::name_range {
            match &self.name {
                terms_and_conditions_part_utl::name_range::String(x) => assessment_part_utl::name_range::String(x.clone()),
                terms_and_conditions_part_utl::name_range::AssessmentPartNameEnum(x) => assessment_part_utl::name_range::AssessmentPartNameEnum(x.clone()),
                terms_and_conditions_part_utl::name_range::TermsAndConditionsPartNameEnum(x) => assessment_part_utl::name_range::TermsAndConditionsPartNameEnum(x.clone()),
            }
    }
        fn ns<'a>(&'a self) -> Option<&'a str> {
        return self.ns.as_deref();
    }
        fn _class<'a>(&'a self) -> Option<&'a str> {
        return self._class.as_deref();
    }
        fn title<'a>(&'a self) -> Option<&'a str> {
        return self.title.as_deref();
    }
        fn prose<'a>(&'a self) -> Option<&'a str> {
        return self.prose.as_deref();
    }
        fn parts(&self) -> Option<Vec<assessment_part_utl::parts_range>> {
        self.parts.as_ref().map(|xs| xs.iter().map(|v| assessment_part_utl::parts_range::TermsAndConditionsPart(v.clone())).collect())
    }
}

impl AssessmentPart for crate::AssessmentPartOrSubtype {
        fn uuid<'a>(&'a self) -> Option<&'a str> {
        match self {
                AssessmentPartOrSubtype::TermsAndConditionsPart(val) => val.uuid(),

        }
    }
        fn name(&self) -> assessment_part_utl::name_range {
        match self {
                AssessmentPartOrSubtype::TermsAndConditionsPart(val) => val.name(),

        }
    }
        fn ns<'a>(&'a self) -> Option<&'a str> {
        match self {
                AssessmentPartOrSubtype::TermsAndConditionsPart(val) => val.ns(),

        }
    }
        fn _class<'a>(&'a self) -> Option<&'a str> {
        match self {
                AssessmentPartOrSubtype::TermsAndConditionsPart(val) => val._class(),

        }
    }
        fn title<'a>(&'a self) -> Option<&'a str> {
        match self {
                AssessmentPartOrSubtype::TermsAndConditionsPart(val) => val.title(),

        }
    }
        fn prose<'a>(&'a self) -> Option<&'a str> {
        match self {
                AssessmentPartOrSubtype::TermsAndConditionsPart(val) => val.prose(),

        }
    }
        fn parts(&self) -> Option<Vec<assessment_part_utl::parts_range>> {
        match self {
                AssessmentPartOrSubtype::TermsAndConditionsPart(val) => val.parts().map(|x| x.to_any()),

        }
    }
}

pub trait TermsAndConditionsPart : AssessmentPart   {


}

impl TermsAndConditionsPart for crate::TermsAndConditionsPart {
}


pub trait ControlPart : HasPropsAndLinks   {

    fn id<'a>(&'a self) -> Option<&'a str>;
    // fn id_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_id(&mut self, value: Option<&'a str>);

    fn name<'a>(&'a self) -> &'a str;
    // fn name_mut(&mut self) -> &mut &'a str;
    // fn set_name(&mut self, value: String);

    fn ns<'a>(&'a self) -> Option<&'a str>;
    // fn ns_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_ns(&mut self, value: Option<&'a str>);

    fn _class<'a>(&'a self) -> Option<&'a str>;
    // fn _class_mut(&mut self) -> &mut Option<&'a str>;
    // fn set__class(&mut self, value: Option<&'a str>);

    fn title<'a>(&'a self) -> Option<&'a str>;
    // fn title_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_title(&mut self, value: Option<&'a str>);

    fn prose<'a>(&'a self) -> Option<&'a str>;
    // fn prose_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_prose(&mut self, value: Option<&'a str>);

    fn parts<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::ControlPart>>;
    // fn parts_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::ControlPart>>;
    // fn set_parts<E>(&mut self, value: Option<&Vec<E>>) where E: Into<ControlPart>;


}

impl ControlPart for crate::ControlPart {
        fn id<'a>(&'a self) -> Option<&'a str> {
        return self.id.as_deref();
    }
        fn name<'a>(&'a self) -> &'a str {
        return &self.name[..];
    }
        fn ns<'a>(&'a self) -> Option<&'a str> {
        return self.ns.as_deref();
    }
        fn _class<'a>(&'a self) -> Option<&'a str> {
        return self._class.as_deref();
    }
        fn title<'a>(&'a self) -> Option<&'a str> {
        return self.title.as_deref();
    }
        fn prose<'a>(&'a self) -> Option<&'a str> {
        return self.prose.as_deref();
    }
        fn parts<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::ControlPart>> {
        return self.parts.as_ref().map(|x| poly_containers::ListView::new(x));
    }
}


pub trait SetParameter   {

    fn param_id<'a>(&'a self) -> &'a str;
    // fn param_id_mut(&mut self) -> &mut &'a str;
    // fn set_param_id(&mut self, value: String);

    fn values<'a>(&'a self) -> impl poly_containers::SeqRef<'a, String>;
    // fn values_mut(&mut self) -> &mut impl poly_containers::SeqRef<'a, String>;
    // fn set_values(&mut self, value: &Vec<String>);

    fn remarks<'a>(&'a self) -> Option<&'a str>;
    // fn remarks_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_remarks(&mut self, value: Option<&'a str>);


}

impl SetParameter for crate::SetParameter {
        fn param_id<'a>(&'a self) -> &'a str {
        return &self.param_id[..];
    }
        fn values<'a>(&'a self) -> impl poly_containers::SeqRef<'a, String> {
        return &self.values;
    }
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}


pub trait SystemComponent : OscalCommon  +  HasResponsibleRoles   {

    fn uuid<'a>(&'a self) -> &'a str;
    // fn uuid_mut(&mut self) -> &mut &'a str;
    // fn set_uuid(&mut self, value: String);

    fn type_(&self) -> system_component_utl::type__range;
    // fn type__mut(&mut self) -> &mut system_component_utl::type__range;
    // fn set_type_(&mut self, value: system_component_utl::type__range);

    fn title<'a>(&'a self) -> &'a str;
    // fn title_mut(&mut self) -> &mut &'a str;
    // fn set_title(&mut self, value: String);

    fn description<'a>(&'a self) -> &'a str;
    // fn description_mut(&mut self) -> &mut &'a str;
    // fn set_description(&mut self, value: String);

    fn purpose<'a>(&'a self) -> Option<&'a str>;
    // fn purpose_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_purpose(&mut self, value: Option<&'a str>);

    fn protocols<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Protocol>>;
    // fn protocols_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::Protocol>>;
    // fn set_protocols<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Protocol>;

    fn status<'a>(&'a self) -> &'a crate::ComponentStatus;
    // fn status_mut(&mut self) -> &mut &'a crate::ComponentStatus;
    // fn set_status<E>(&mut self, value: E) where E: Into<ComponentStatus>;


}

impl SystemComponent for crate::SystemComponent {
        fn uuid<'a>(&'a self) -> &'a str {
        return &self.uuid[..];
    }
        fn type_(&self) -> system_component_utl::type__range {
            self.type_.clone()
    }
        fn title<'a>(&'a self) -> &'a str {
        return &self.title[..];
    }
        fn description<'a>(&'a self) -> &'a str {
        return &self.description[..];
    }
        fn purpose<'a>(&'a self) -> Option<&'a str> {
        return self.purpose.as_deref();
    }
        fn protocols<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Protocol>> {
        return self.protocols.as_ref();
    }
        fn status<'a>(&'a self) -> &'a crate::ComponentStatus {
        return &self.status;
    }
}
impl SystemComponent for crate::SspSystemComponent {
        fn uuid<'a>(&'a self) -> &'a str {
        return &self.uuid[..];
    }
        fn type_(&self) -> system_component_utl::type__range {
            match &self.type_ {
                ssp_system_component_utl::type__range::String(x) => system_component_utl::type__range::String(x.clone()),
                ssp_system_component_utl::type__range::ComponentTypeEnum(x) => system_component_utl::type__range::ComponentTypeEnum(x.clone()),
            }
    }
        fn title<'a>(&'a self) -> &'a str {
        return &self.title[..];
    }
        fn description<'a>(&'a self) -> &'a str {
        return &self.description[..];
    }
        fn purpose<'a>(&'a self) -> Option<&'a str> {
        return self.purpose.as_deref();
    }
        fn protocols<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Protocol>> {
        return self.protocols.as_ref();
    }
        fn status<'a>(&'a self) -> &'a crate::ComponentStatus {
        return &self.status;
    }
}

impl SystemComponent for crate::SystemComponentOrSubtype {
        fn uuid<'a>(&'a self) -> &'a str {
        match self {
                SystemComponentOrSubtype::SspSystemComponent(val) => val.uuid(),

        }
    }
        fn type_(&self) -> system_component_utl::type__range {
        match self {
                SystemComponentOrSubtype::SspSystemComponent(val) => val.type_(),

        }
    }
        fn title<'a>(&'a self) -> &'a str {
        match self {
                SystemComponentOrSubtype::SspSystemComponent(val) => val.title(),

        }
    }
        fn description<'a>(&'a self) -> &'a str {
        match self {
                SystemComponentOrSubtype::SspSystemComponent(val) => val.description(),

        }
    }
        fn purpose<'a>(&'a self) -> Option<&'a str> {
        match self {
                SystemComponentOrSubtype::SspSystemComponent(val) => val.purpose(),

        }
    }
        fn protocols<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Protocol>> {
        match self {
                SystemComponentOrSubtype::SspSystemComponent(val) => val.protocols().map(|x| x.to_any()),

        }
    }
        fn status<'a>(&'a self) -> &'a crate::ComponentStatus {
        match self {
                SystemComponentOrSubtype::SspSystemComponent(val) => val.status(),

        }
    }
}

pub trait ComponentStatus   {

    fn state<'a>(&'a self) -> &'a crate::ComponentStateEnum;
    // fn state_mut(&mut self) -> &mut &'a crate::ComponentStateEnum;
    // fn set_state(&mut self, value: ComponentStateEnum);

    fn remarks<'a>(&'a self) -> Option<&'a str>;
    // fn remarks_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_remarks(&mut self, value: Option<&'a str>);


}

impl ComponentStatus for crate::ComponentStatus {
        fn state<'a>(&'a self) -> &'a crate::ComponentStateEnum {
        return &self.state;
    }
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}


pub trait Protocol   {

    fn uuid<'a>(&'a self) -> Option<&'a str>;
    // fn uuid_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_uuid(&mut self, value: Option<&'a str>);

    fn name<'a>(&'a self) -> Option<&'a str>;
    // fn name_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_name(&mut self, value: Option<&'a str>);

    fn title<'a>(&'a self) -> Option<&'a str>;
    // fn title_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_title(&mut self, value: Option<&'a str>);

    fn port_ranges<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::PortRange>>;
    // fn port_ranges_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::PortRange>>;
    // fn set_port_ranges<E>(&mut self, value: Option<&Vec<E>>) where E: Into<PortRange>;


}

impl Protocol for crate::Protocol {
        fn uuid<'a>(&'a self) -> Option<&'a str> {
        return self.uuid.as_deref();
    }
        fn name<'a>(&'a self) -> Option<&'a str> {
        return self.name.as_deref();
    }
        fn title<'a>(&'a self) -> Option<&'a str> {
        return self.title.as_deref();
    }
        fn port_ranges<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::PortRange>> {
        return self.port_ranges.as_ref();
    }
}


pub trait PortRange   {

    fn start(&self) -> Option<isize>;
    // fn start_mut(&mut self) -> &mut Option<isize>;
    // fn set_start(&mut self, value: Option<isize>);

    fn end(&self) -> Option<isize>;
    // fn end_mut(&mut self) -> &mut Option<isize>;
    // fn set_end(&mut self, value: Option<isize>);

    fn transport<'a>(&'a self) -> Option<&'a crate::TransportEnum>;
    // fn transport_mut(&mut self) -> &mut Option<&'a crate::TransportEnum>;
    // fn set_transport(&mut self, value: Option<&'a TransportEnum>);

    fn remarks<'a>(&'a self) -> Option<&'a str>;
    // fn remarks_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_remarks(&mut self, value: Option<&'a str>);


}

impl PortRange for crate::PortRange {
        fn start(&self) -> Option<isize> {
        return self.start;
    }
        fn end(&self) -> Option<isize> {
        return self.end;
    }
        fn transport<'a>(&'a self) -> Option<&'a crate::TransportEnum> {
        return self.transport.as_ref();
    }
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}


pub trait ImplementationStatus   {

    fn state(&self) -> implementation_status_utl::state_range;
    // fn state_mut(&mut self) -> &mut implementation_status_utl::state_range;
    // fn set_state(&mut self, value: implementation_status_utl::state_range);

    fn remarks<'a>(&'a self) -> Option<&'a str>;
    // fn remarks_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_remarks(&mut self, value: Option<&'a str>);


}

impl ImplementationStatus for crate::ImplementationStatus {
        fn state(&self) -> implementation_status_utl::state_range {
            self.state.clone()
    }
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}


pub trait SystemUser : OscalCommon   {

    fn uuid<'a>(&'a self) -> &'a str;
    // fn uuid_mut(&mut self) -> &mut &'a str;
    // fn set_uuid(&mut self, value: String);

    fn title<'a>(&'a self) -> Option<&'a str>;
    // fn title_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_title(&mut self, value: Option<&'a str>);

    fn short_name<'a>(&'a self) -> Option<&'a str>;
    // fn short_name_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_short_name(&mut self, value: Option<&'a str>);

    fn description<'a>(&'a self) -> Option<&'a str>;
    // fn description_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_description(&mut self, value: Option<&'a str>);

    fn role_ids<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn role_ids_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_role_ids(&mut self, value: Option<&Vec<String>>);

    fn authorized_privileges<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::AuthorizedPrivilege>>;
    // fn authorized_privileges_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::AuthorizedPrivilege>>;
    // fn set_authorized_privileges<E>(&mut self, value: Option<&Vec<E>>) where E: Into<AuthorizedPrivilege>;


}

impl SystemUser for crate::SystemUser {
        fn uuid<'a>(&'a self) -> &'a str {
        return &self.uuid[..];
    }
        fn title<'a>(&'a self) -> Option<&'a str> {
        return self.title.as_deref();
    }
        fn short_name<'a>(&'a self) -> Option<&'a str> {
        return self.short_name.as_deref();
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn role_ids<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.role_ids.as_ref();
    }
        fn authorized_privileges<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::AuthorizedPrivilege>> {
        return self.authorized_privileges.as_ref();
    }
}


pub trait AuthorizedPrivilege   {

    fn title<'a>(&'a self) -> &'a str;
    // fn title_mut(&mut self) -> &mut &'a str;
    // fn set_title(&mut self, value: String);

    fn description<'a>(&'a self) -> Option<&'a str>;
    // fn description_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_description(&mut self, value: Option<&'a str>);

    fn functions_performed<'a>(&'a self) -> impl poly_containers::SeqRef<'a, String>;
    // fn functions_performed_mut(&mut self) -> &mut impl poly_containers::SeqRef<'a, String>;
    // fn set_functions_performed(&mut self, value: &Vec<String>);


}

impl AuthorizedPrivilege for crate::AuthorizedPrivilege {
        fn title<'a>(&'a self) -> &'a str {
        return &self.title[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn functions_performed<'a>(&'a self) -> impl poly_containers::SeqRef<'a, String> {
        return &self.functions_performed;
    }
}


pub trait InventoryItem : OscalCommon  +  HasResponsibleParties   {

    fn uuid<'a>(&'a self) -> &'a str;
    // fn uuid_mut(&mut self) -> &mut &'a str;
    // fn set_uuid(&mut self, value: String);

    fn description<'a>(&'a self) -> &'a str;
    // fn description_mut(&mut self) -> &mut &'a str;
    // fn set_description(&mut self, value: String);

    fn implemented_components<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::ImplementedComponent>>;
    // fn implemented_components_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::ImplementedComponent>>;
    // fn set_implemented_components<E>(&mut self, value: Option<&Vec<E>>) where E: Into<ImplementedComponent>;


}

impl InventoryItem for crate::InventoryItem {
        fn uuid<'a>(&'a self) -> &'a str {
        return &self.uuid[..];
    }
        fn description<'a>(&'a self) -> &'a str {
        return &self.description[..];
    }
        fn implemented_components<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::ImplementedComponent>> {
        return self.implemented_components.as_ref();
    }
}
impl InventoryItem for crate::SspInventoryItem {
        fn uuid<'a>(&'a self) -> &'a str {
        return &self.uuid[..];
    }
        fn description<'a>(&'a self) -> &'a str {
        return &self.description[..];
    }
        fn implemented_components<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::ImplementedComponent>> {
        return self.implemented_components.as_ref();
    }
}

impl InventoryItem for crate::InventoryItemOrSubtype {
        fn uuid<'a>(&'a self) -> &'a str {
        match self {
                InventoryItemOrSubtype::SspInventoryItem(val) => val.uuid(),

        }
    }
        fn description<'a>(&'a self) -> &'a str {
        match self {
                InventoryItemOrSubtype::SspInventoryItem(val) => val.description(),

        }
    }
        fn implemented_components<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::ImplementedComponent>> {
        match self {
                InventoryItemOrSubtype::SspInventoryItem(val) => val.implemented_components().map(|x| x.to_any()),

        }
    }
}

pub trait ImplementedComponent : OscalCommon  +  HasResponsibleParties   {

    fn component_uuid<'a>(&'a self) -> &'a str;
    // fn component_uuid_mut(&mut self) -> &mut &'a str;
    // fn set_component_uuid(&mut self, value: String);


}

impl ImplementedComponent for crate::ImplementedComponent {
        fn component_uuid<'a>(&'a self) -> &'a str {
        return &self.component_uuid[..];
    }
}


pub trait SystemId   {

    fn id<'a>(&'a self) -> &'a str;
    // fn id_mut(&mut self) -> &mut &'a str;
    // fn set_id(&mut self, value: String);

    fn identifier_type(&self) -> Option<system_id_utl::identifier_type_range>;
    // fn identifier_type_mut(&mut self) -> &mut Option<system_id_utl::identifier_type_range>;
    // fn set_identifier_type(&mut self, value: Option<&'a system_id_utl::identifier_type_range>);


}

impl SystemId for crate::SystemId {
        fn id<'a>(&'a self) -> &'a str {
        return &self.id[..];
    }
        fn identifier_type(&self) -> Option<system_id_utl::identifier_type_range> {
                self.identifier_type.as_ref().cloned()
    }
}


pub trait ImplementationCommonProperty : Property   {


}

impl ImplementationCommonProperty for crate::ImplementationCommonProperty {
}


pub trait ImplementationCommonLink : Link   {


}

impl ImplementationCommonLink for crate::ImplementationCommonLink {
}


pub trait ImplementationResponsibleRole : ResponsibleRole   {


}

impl ImplementationResponsibleRole for crate::ImplementationResponsibleRole {
}


pub trait ImplementationResponsibleParty : ResponsibleParty   {


}

impl ImplementationResponsibleParty for crate::ImplementationResponsibleParty {
}


pub trait Origin   {

    fn actors<'a>(&'a self) -> impl poly_containers::SeqRef<'a, crate::OriginActor>;
    // fn actors_mut(&mut self) -> &mut impl poly_containers::SeqRef<'a, crate::OriginActor>;
    // fn set_actors<E>(&mut self, value: &Vec<E>) where E: Into<OriginActor>;

    fn related_tasks<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::RelatedTask>>;
    // fn related_tasks_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::RelatedTask>>;
    // fn set_related_tasks<E>(&mut self, value: Option<&Vec<E>>) where E: Into<RelatedTask>;


}

impl Origin for crate::Origin {
        fn actors<'a>(&'a self) -> impl poly_containers::SeqRef<'a, crate::OriginActor> {
        return &self.actors;
    }
        fn related_tasks<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::RelatedTask>> {
        return self.related_tasks.as_ref();
    }
}


pub trait OriginActor : HasPropsAndLinks   {

    fn type_<'a>(&'a self) -> &'a crate::OriginActorTypeEnum;
    // fn type__mut(&mut self) -> &mut &'a crate::OriginActorTypeEnum;
    // fn set_type_(&mut self, value: OriginActorTypeEnum);

    fn actor_uuid<'a>(&'a self) -> &'a str;
    // fn actor_uuid_mut(&mut self) -> &mut &'a str;
    // fn set_actor_uuid(&mut self, value: String);

    fn role_id<'a>(&'a self) -> Option<&'a str>;
    // fn role_id_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_role_id(&mut self, value: Option<&'a str>);


}

impl OriginActor for crate::OriginActor {
        fn type_<'a>(&'a self) -> &'a crate::OriginActorTypeEnum {
        return &self.type_;
    }
        fn actor_uuid<'a>(&'a self) -> &'a str {
        return &self.actor_uuid[..];
    }
        fn role_id<'a>(&'a self) -> Option<&'a str> {
        return self.role_id.as_deref();
    }
}


pub trait RelatedTask : OscalCommon  +  HasResponsibleParties   {

    fn task_uuid<'a>(&'a self) -> &'a str;
    // fn task_uuid_mut(&mut self) -> &mut &'a str;
    // fn set_task_uuid(&mut self, value: String);

    fn subjects<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::AssessmentSubject>>;
    // fn subjects_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::AssessmentSubject>>;
    // fn set_subjects<E>(&mut self, value: Option<&Vec<E>>) where E: Into<AssessmentSubject>;

    fn identified_subject<'a>(&'a self) -> Option<&'a crate::IdentifiedSubject>;
    // fn identified_subject_mut(&mut self) -> &mut Option<&'a crate::IdentifiedSubject>;
    // fn set_identified_subject<E>(&mut self, value: Option<E>) where E: Into<IdentifiedSubject>;


}

impl RelatedTask for crate::RelatedTask {
        fn task_uuid<'a>(&'a self) -> &'a str {
        return &self.task_uuid[..];
    }
        fn subjects<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::AssessmentSubject>> {
        return self.subjects.as_ref();
    }
        fn identified_subject<'a>(&'a self) -> Option<&'a crate::IdentifiedSubject> {
        return self.identified_subject.as_ref();
    }
}


pub trait IdentifiedSubject   {

    fn subject_placeholder_uuid<'a>(&'a self) -> &'a str;
    // fn subject_placeholder_uuid_mut(&mut self) -> &mut &'a str;
    // fn set_subject_placeholder_uuid(&mut self, value: String);

    fn subjects<'a>(&'a self) -> impl poly_containers::SeqRef<'a, crate::AssessmentSubject>;
    // fn subjects_mut(&mut self) -> &mut impl poly_containers::SeqRef<'a, crate::AssessmentSubject>;
    // fn set_subjects<E>(&mut self, value: &Vec<E>) where E: Into<AssessmentSubject>;


}

impl IdentifiedSubject for crate::IdentifiedSubject {
        fn subject_placeholder_uuid<'a>(&'a self) -> &'a str {
        return &self.subject_placeholder_uuid[..];
    }
        fn subjects<'a>(&'a self) -> impl poly_containers::SeqRef<'a, crate::AssessmentSubject> {
        return &self.subjects;
    }
}


pub trait Observation : OscalCommon   {

    fn uuid<'a>(&'a self) -> &'a str;
    // fn uuid_mut(&mut self) -> &mut &'a str;
    // fn set_uuid(&mut self, value: String);

    fn title<'a>(&'a self) -> Option<&'a str>;
    // fn title_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_title(&mut self, value: Option<&'a str>);

    fn description<'a>(&'a self) -> &'a str;
    // fn description_mut(&mut self) -> &mut &'a str;
    // fn set_description(&mut self, value: String);

    fn methods(&self) -> Vec<observation_utl::methods_range>;
    // fn methods_mut(&mut self) -> &mut Vec<observation_utl::methods_range>;
    // fn set_methods(&mut self, value: &Vec<observation_utl::methods_range>);

    fn types(&self) -> Option<Vec<observation_utl::types_range>>;
    // fn types_mut(&mut self) -> &mut Option<Vec<observation_utl::types_range>>;
    // fn set_types(&mut self, value: Option<&Vec<observation_utl::types_range>>);

    fn origins<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Origin>>;
    // fn origins_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::Origin>>;
    // fn set_origins<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Origin>;

    fn subjects<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::SubjectReference>>;
    // fn subjects_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::SubjectReference>>;
    // fn set_subjects<E>(&mut self, value: Option<&Vec<E>>) where E: Into<SubjectReference>;

    fn relevant_evidence<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::RelevantEvidence>>;
    // fn relevant_evidence_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::RelevantEvidence>>;
    // fn set_relevant_evidence<E>(&mut self, value: Option<&Vec<E>>) where E: Into<RelevantEvidence>;

    fn collected<'a>(&'a self) -> &'a str;
    // fn collected_mut(&mut self) -> &mut &'a str;
    // fn set_collected(&mut self, value: String);

    fn expires<'a>(&'a self) -> Option<&'a str>;
    // fn expires_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_expires(&mut self, value: Option<&'a str>);


}

impl Observation for crate::Observation {
        fn uuid<'a>(&'a self) -> &'a str {
        return &self.uuid[..];
    }
        fn title<'a>(&'a self) -> Option<&'a str> {
        return self.title.as_deref();
    }
        fn description<'a>(&'a self) -> &'a str {
        return &self.description[..];
    }
        fn methods(&self) -> Vec<observation_utl::methods_range> {
        self.methods.clone()
    }
        fn types(&self) -> Option<Vec<observation_utl::types_range>> {
        self.types.as_ref().map(|xs| xs.clone())
    }
        fn origins<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Origin>> {
        return self.origins.as_ref();
    }
        fn subjects<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::SubjectReference>> {
        return self.subjects.as_ref();
    }
        fn relevant_evidence<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::RelevantEvidence>> {
        return self.relevant_evidence.as_ref();
    }
        fn collected<'a>(&'a self) -> &'a str {
        return &self.collected[..];
    }
        fn expires<'a>(&'a self) -> Option<&'a str> {
        return self.expires.as_deref();
    }
}


pub trait RelevantEvidence : OscalCommon   {

    fn href<'a>(&'a self) -> Option<&'a str>;
    // fn href_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_href(&mut self, value: Option<&'a str>);

    fn description<'a>(&'a self) -> &'a str;
    // fn description_mut(&mut self) -> &mut &'a str;
    // fn set_description(&mut self, value: String);


}

impl RelevantEvidence for crate::RelevantEvidence {
        fn href<'a>(&'a self) -> Option<&'a str> {
        return self.href.as_deref();
    }
        fn description<'a>(&'a self) -> &'a str {
        return &self.description[..];
    }
}


pub trait Finding : OscalCommon   {

    fn uuid<'a>(&'a self) -> &'a str;
    // fn uuid_mut(&mut self) -> &mut &'a str;
    // fn set_uuid(&mut self, value: String);

    fn title<'a>(&'a self) -> &'a str;
    // fn title_mut(&mut self) -> &mut &'a str;
    // fn set_title(&mut self, value: String);

    fn description<'a>(&'a self) -> &'a str;
    // fn description_mut(&mut self) -> &mut &'a str;
    // fn set_description(&mut self, value: String);

    fn target<'a>(&'a self) -> &'a crate::FindingTarget;
    // fn target_mut(&mut self) -> &mut &'a crate::FindingTarget;
    // fn set_target<E>(&mut self, value: E) where E: Into<FindingTarget>;

    fn implementation_statement_uuid<'a>(&'a self) -> Option<&'a str>;
    // fn implementation_statement_uuid_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_implementation_statement_uuid(&mut self, value: Option<&'a str>);

    fn origins<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Origin>>;
    // fn origins_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::Origin>>;
    // fn set_origins<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Origin>;

    fn related_observations<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::RelatedObservation>>;
    // fn related_observations_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::RelatedObservation>>;
    // fn set_related_observations<E>(&mut self, value: Option<&Vec<E>>) where E: Into<RelatedObservation>;

    fn related_risks<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::AssociatedRisk>>;
    // fn related_risks_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::AssociatedRisk>>;
    // fn set_related_risks<E>(&mut self, value: Option<&Vec<E>>) where E: Into<AssociatedRisk>;


}

impl Finding for crate::Finding {
        fn uuid<'a>(&'a self) -> &'a str {
        return &self.uuid[..];
    }
        fn title<'a>(&'a self) -> &'a str {
        return &self.title[..];
    }
        fn description<'a>(&'a self) -> &'a str {
        return &self.description[..];
    }
        fn target<'a>(&'a self) -> &'a crate::FindingTarget {
        return &self.target;
    }
        fn implementation_statement_uuid<'a>(&'a self) -> Option<&'a str> {
        return self.implementation_statement_uuid.as_deref();
    }
        fn origins<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Origin>> {
        return self.origins.as_ref();
    }
        fn related_observations<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::RelatedObservation>> {
        return self.related_observations.as_ref();
    }
        fn related_risks<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::AssociatedRisk>> {
        return self.related_risks.as_ref();
    }
}


pub trait FindingTarget : OscalCommon   {

    fn type_<'a>(&'a self) -> &'a crate::FindingTargetTypeEnum;
    // fn type__mut(&mut self) -> &mut &'a crate::FindingTargetTypeEnum;
    // fn set_type_(&mut self, value: FindingTargetTypeEnum);

    fn target_id<'a>(&'a self) -> &'a str;
    // fn target_id_mut(&mut self) -> &mut &'a str;
    // fn set_target_id(&mut self, value: String);

    fn title<'a>(&'a self) -> Option<&'a str>;
    // fn title_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_title(&mut self, value: Option<&'a str>);

    fn description<'a>(&'a self) -> Option<&'a str>;
    // fn description_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_description(&mut self, value: Option<&'a str>);

    fn implementation_status<'a>(&'a self) -> Option<&'a crate::ImplementationStatus>;
    // fn implementation_status_mut(&mut self) -> &mut Option<&'a crate::ImplementationStatus>;
    // fn set_implementation_status<E>(&mut self, value: Option<E>) where E: Into<ImplementationStatus>;

    fn status<'a>(&'a self) -> &'a crate::ObjectiveStatus;
    // fn status_mut(&mut self) -> &mut &'a crate::ObjectiveStatus;
    // fn set_status<E>(&mut self, value: E) where E: Into<ObjectiveStatus>;


}

impl FindingTarget for crate::FindingTarget {
        fn type_<'a>(&'a self) -> &'a crate::FindingTargetTypeEnum {
        return &self.type_;
    }
        fn target_id<'a>(&'a self) -> &'a str {
        return &self.target_id[..];
    }
        fn title<'a>(&'a self) -> Option<&'a str> {
        return self.title.as_deref();
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn implementation_status<'a>(&'a self) -> Option<&'a crate::ImplementationStatus> {
        return self.implementation_status.as_ref();
    }
        fn status<'a>(&'a self) -> &'a crate::ObjectiveStatus {
        return &self.status;
    }
}


pub trait ObjectiveStatus   {

    fn state<'a>(&'a self) -> &'a crate::ObjectiveStatusStateEnum;
    // fn state_mut(&mut self) -> &mut &'a crate::ObjectiveStatusStateEnum;
    // fn set_state(&mut self, value: ObjectiveStatusStateEnum);

    fn reason(&self) -> Option<objective_status_utl::reason_range>;
    // fn reason_mut(&mut self) -> &mut Option<objective_status_utl::reason_range>;
    // fn set_reason(&mut self, value: Option<&'a objective_status_utl::reason_range>);

    fn remarks<'a>(&'a self) -> Option<&'a str>;
    // fn remarks_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_remarks(&mut self, value: Option<&'a str>);


}

impl ObjectiveStatus for crate::ObjectiveStatus {
        fn state<'a>(&'a self) -> &'a crate::ObjectiveStatusStateEnum {
        return &self.state;
    }
        fn reason(&self) -> Option<objective_status_utl::reason_range> {
                self.reason.as_ref().cloned()
    }
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}


pub trait RelatedObservation   {

    fn observation_uuid<'a>(&'a self) -> &'a str;
    // fn observation_uuid_mut(&mut self) -> &mut &'a str;
    // fn set_observation_uuid(&mut self, value: String);

    fn remarks<'a>(&'a self) -> Option<&'a str>;
    // fn remarks_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_remarks(&mut self, value: Option<&'a str>);


}

impl RelatedObservation for crate::RelatedObservation {
        fn observation_uuid<'a>(&'a self) -> &'a str {
        return &self.observation_uuid[..];
    }
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}


pub trait AssociatedRisk   {

    fn risk_uuid<'a>(&'a self) -> &'a str;
    // fn risk_uuid_mut(&mut self) -> &mut &'a str;
    // fn set_risk_uuid(&mut self, value: String);

    fn remarks<'a>(&'a self) -> Option<&'a str>;
    // fn remarks_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_remarks(&mut self, value: Option<&'a str>);


}

impl AssociatedRisk for crate::AssociatedRisk {
        fn risk_uuid<'a>(&'a self) -> &'a str {
        return &self.risk_uuid[..];
    }
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}


pub trait Risk : HasPropsAndLinks   {

    fn uuid<'a>(&'a self) -> &'a str;
    // fn uuid_mut(&mut self) -> &mut &'a str;
    // fn set_uuid(&mut self, value: String);

    fn title<'a>(&'a self) -> &'a str;
    // fn title_mut(&mut self) -> &mut &'a str;
    // fn set_title(&mut self, value: String);

    fn description<'a>(&'a self) -> &'a str;
    // fn description_mut(&mut self) -> &mut &'a str;
    // fn set_description(&mut self, value: String);

    fn statement<'a>(&'a self) -> &'a str;
    // fn statement_mut(&mut self) -> &mut &'a str;
    // fn set_statement(&mut self, value: String);

    fn origins<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Origin>>;
    // fn origins_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::Origin>>;
    // fn set_origins<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Origin>;

    fn threat_ids<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::ThreatId>>;
    // fn threat_ids_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::ThreatId>>;
    // fn set_threat_ids<E>(&mut self, value: Option<&Vec<E>>) where E: Into<ThreatId>;

    fn characterizations<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Characterization>>;
    // fn characterizations_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::Characterization>>;
    // fn set_characterizations<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Characterization>;

    fn mitigating_factors<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::MitigatingFactor>>;
    // fn mitigating_factors_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::MitigatingFactor>>;
    // fn set_mitigating_factors<E>(&mut self, value: Option<&Vec<E>>) where E: Into<MitigatingFactor>;

    fn deadline<'a>(&'a self) -> Option<&'a str>;
    // fn deadline_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_deadline(&mut self, value: Option<&'a str>);

    fn remediations<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Response>>;
    // fn remediations_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::Response>>;
    // fn set_remediations<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Response>;

    fn risk_log<'a>(&'a self) -> Option<&'a crate::RiskLog>;
    // fn risk_log_mut(&mut self) -> &mut Option<&'a crate::RiskLog>;
    // fn set_risk_log<E>(&mut self, value: Option<E>) where E: Into<RiskLog>;

    fn related_observations<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::RelatedObservation>>;
    // fn related_observations_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::RelatedObservation>>;
    // fn set_related_observations<E>(&mut self, value: Option<&Vec<E>>) where E: Into<RelatedObservation>;

    fn status(&self) -> risk_utl::status_range;
    // fn status_mut(&mut self) -> &mut risk_utl::status_range;
    // fn set_status(&mut self, value: risk_utl::status_range);


}

impl Risk for crate::Risk {
        fn uuid<'a>(&'a self) -> &'a str {
        return &self.uuid[..];
    }
        fn title<'a>(&'a self) -> &'a str {
        return &self.title[..];
    }
        fn description<'a>(&'a self) -> &'a str {
        return &self.description[..];
    }
        fn statement<'a>(&'a self) -> &'a str {
        return &self.statement[..];
    }
        fn origins<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Origin>> {
        return self.origins.as_ref();
    }
        fn threat_ids<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::ThreatId>> {
        return self.threat_ids.as_ref();
    }
        fn characterizations<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Characterization>> {
        return self.characterizations.as_ref();
    }
        fn mitigating_factors<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::MitigatingFactor>> {
        return self.mitigating_factors.as_ref();
    }
        fn deadline<'a>(&'a self) -> Option<&'a str> {
        return self.deadline.as_deref();
    }
        fn remediations<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Response>> {
        return self.remediations.as_ref();
    }
        fn risk_log<'a>(&'a self) -> Option<&'a crate::RiskLog> {
        return self.risk_log.as_ref();
    }
        fn related_observations<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::RelatedObservation>> {
        return self.related_observations.as_ref();
    }
        fn status(&self) -> risk_utl::status_range {
            self.status.clone()
    }
}


pub trait ThreatId   {

    fn href<'a>(&'a self) -> Option<&'a str>;
    // fn href_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_href(&mut self, value: Option<&'a str>);

    fn system<'a>(&'a self) -> &'a str;
    // fn system_mut(&mut self) -> &mut &'a str;
    // fn set_system(&mut self, value: String);

    fn id<'a>(&'a self) -> &'a str;
    // fn id_mut(&mut self) -> &mut &'a str;
    // fn set_id(&mut self, value: String);


}

impl ThreatId for crate::ThreatId {
        fn href<'a>(&'a self) -> Option<&'a str> {
        return self.href.as_deref();
    }
        fn system<'a>(&'a self) -> &'a str {
        return &self.system[..];
    }
        fn id<'a>(&'a self) -> &'a str {
        return &self.id[..];
    }
}


pub trait Characterization : HasPropsAndLinks   {

    fn origin<'a>(&'a self) -> &'a crate::Origin;
    // fn origin_mut(&mut self) -> &mut &'a crate::Origin;
    // fn set_origin<E>(&mut self, value: E) where E: Into<Origin>;

    fn facets<'a>(&'a self) -> impl poly_containers::SeqRef<'a, crate::Facet>;
    // fn facets_mut(&mut self) -> &mut impl poly_containers::SeqRef<'a, crate::Facet>;
    // fn set_facets<E>(&mut self, value: &Vec<E>) where E: Into<Facet>;


}

impl Characterization for crate::Characterization {
        fn origin<'a>(&'a self) -> &'a crate::Origin {
        return &self.origin;
    }
        fn facets<'a>(&'a self) -> impl poly_containers::SeqRef<'a, crate::Facet> {
        return &self.facets;
    }
}


pub trait Facet : OscalCommon   {

    fn name<'a>(&'a self) -> &'a str;
    // fn name_mut(&mut self) -> &mut &'a str;
    // fn set_name(&mut self, value: String);

    fn value<'a>(&'a self) -> &'a str;
    // fn value_mut(&mut self) -> &mut &'a str;
    // fn set_value(&mut self, value: String);

    fn system<'a>(&'a self) -> &'a str;
    // fn system_mut(&mut self) -> &mut &'a str;
    // fn set_system(&mut self, value: String);


}

impl Facet for crate::Facet {
        fn name<'a>(&'a self) -> &'a str {
        return &self.name[..];
    }
        fn value<'a>(&'a self) -> &'a str {
        return &self.value[..];
    }
        fn system<'a>(&'a self) -> &'a str {
        return &self.system[..];
    }
}


pub trait MitigatingFactor : HasPropsAndLinks   {

    fn uuid<'a>(&'a self) -> &'a str;
    // fn uuid_mut(&mut self) -> &mut &'a str;
    // fn set_uuid(&mut self, value: String);

    fn description<'a>(&'a self) -> &'a str;
    // fn description_mut(&mut self) -> &mut &'a str;
    // fn set_description(&mut self, value: String);

    fn implementation_uuid<'a>(&'a self) -> Option<&'a str>;
    // fn implementation_uuid_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_implementation_uuid(&mut self, value: Option<&'a str>);

    fn subjects<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::SubjectReference>>;
    // fn subjects_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::SubjectReference>>;
    // fn set_subjects<E>(&mut self, value: Option<&Vec<E>>) where E: Into<SubjectReference>;


}

impl MitigatingFactor for crate::MitigatingFactor {
        fn uuid<'a>(&'a self) -> &'a str {
        return &self.uuid[..];
    }
        fn description<'a>(&'a self) -> &'a str {
        return &self.description[..];
    }
        fn implementation_uuid<'a>(&'a self) -> Option<&'a str> {
        return self.implementation_uuid.as_deref();
    }
        fn subjects<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::SubjectReference>> {
        return self.subjects.as_ref();
    }
}


pub trait Response : OscalCommon   {

    fn uuid<'a>(&'a self) -> &'a str;
    // fn uuid_mut(&mut self) -> &mut &'a str;
    // fn set_uuid(&mut self, value: String);

    fn title<'a>(&'a self) -> &'a str;
    // fn title_mut(&mut self) -> &mut &'a str;
    // fn set_title(&mut self, value: String);

    fn description<'a>(&'a self) -> &'a str;
    // fn description_mut(&mut self) -> &mut &'a str;
    // fn set_description(&mut self, value: String);

    fn lifecycle(&self) -> response_utl::lifecycle_range;
    // fn lifecycle_mut(&mut self) -> &mut response_utl::lifecycle_range;
    // fn set_lifecycle(&mut self, value: response_utl::lifecycle_range);

    fn origins<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Origin>>;
    // fn origins_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::Origin>>;
    // fn set_origins<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Origin>;

    fn required_assets<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::RequiredAsset>>;
    // fn required_assets_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::RequiredAsset>>;
    // fn set_required_assets<E>(&mut self, value: Option<&Vec<E>>) where E: Into<RequiredAsset>;

    fn tasks<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Task>>;
    // fn tasks_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::Task>>;
    // fn set_tasks<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Task>;


}

impl Response for crate::Response {
        fn uuid<'a>(&'a self) -> &'a str {
        return &self.uuid[..];
    }
        fn title<'a>(&'a self) -> &'a str {
        return &self.title[..];
    }
        fn description<'a>(&'a self) -> &'a str {
        return &self.description[..];
    }
        fn lifecycle(&self) -> response_utl::lifecycle_range {
            self.lifecycle.clone()
    }
        fn origins<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Origin>> {
        return self.origins.as_ref();
    }
        fn required_assets<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::RequiredAsset>> {
        return self.required_assets.as_ref();
    }
        fn tasks<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Task>> {
        return self.tasks.as_ref();
    }
}


pub trait RequiredAsset : OscalCommon   {

    fn uuid<'a>(&'a self) -> &'a str;
    // fn uuid_mut(&mut self) -> &mut &'a str;
    // fn set_uuid(&mut self, value: String);

    fn title<'a>(&'a self) -> Option<&'a str>;
    // fn title_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_title(&mut self, value: Option<&'a str>);

    fn description<'a>(&'a self) -> &'a str;
    // fn description_mut(&mut self) -> &mut &'a str;
    // fn set_description(&mut self, value: String);

    fn subjects<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::SubjectReference>>;
    // fn subjects_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::SubjectReference>>;
    // fn set_subjects<E>(&mut self, value: Option<&Vec<E>>) where E: Into<SubjectReference>;


}

impl RequiredAsset for crate::RequiredAsset {
        fn uuid<'a>(&'a self) -> &'a str {
        return &self.uuid[..];
    }
        fn title<'a>(&'a self) -> Option<&'a str> {
        return self.title.as_deref();
    }
        fn description<'a>(&'a self) -> &'a str {
        return &self.description[..];
    }
        fn subjects<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::SubjectReference>> {
        return self.subjects.as_ref();
    }
}


pub trait RiskLog   {

    fn entries<'a>(&'a self) -> impl poly_containers::SeqRef<'a, crate::RiskLogEntry>;
    // fn entries_mut(&mut self) -> &mut impl poly_containers::SeqRef<'a, crate::RiskLogEntry>;
    // fn set_entries<E>(&mut self, value: &Vec<E>) where E: Into<RiskLogEntry>;


}

impl RiskLog for crate::RiskLog {
        fn entries<'a>(&'a self) -> impl poly_containers::SeqRef<'a, crate::RiskLogEntry> {
        return &self.entries;
    }
}


pub trait RiskLogEntry : OscalCommon   {

    fn uuid<'a>(&'a self) -> &'a str;
    // fn uuid_mut(&mut self) -> &mut &'a str;
    // fn set_uuid(&mut self, value: String);

    fn title<'a>(&'a self) -> Option<&'a str>;
    // fn title_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_title(&mut self, value: Option<&'a str>);

    fn description<'a>(&'a self) -> Option<&'a str>;
    // fn description_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_description(&mut self, value: Option<&'a str>);

    fn start<'a>(&'a self) -> &'a str;
    // fn start_mut(&mut self) -> &mut &'a str;
    // fn set_start(&mut self, value: String);

    fn end<'a>(&'a self) -> Option<&'a str>;
    // fn end_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_end(&mut self, value: Option<&'a str>);

    fn logged_by<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::LoggedBy>>;
    // fn logged_by_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::LoggedBy>>;
    // fn set_logged_by<E>(&mut self, value: Option<&Vec<E>>) where E: Into<LoggedBy>;

    fn status_change(&self) -> Option<risk_log_entry_utl::status_change_range>;
    // fn status_change_mut(&mut self) -> &mut Option<risk_log_entry_utl::status_change_range>;
    // fn set_status_change(&mut self, value: Option<&'a risk_log_entry_utl::status_change_range>);

    fn related_responses<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::RiskResponseReference>>;
    // fn related_responses_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::RiskResponseReference>>;
    // fn set_related_responses<E>(&mut self, value: Option<&Vec<E>>) where E: Into<RiskResponseReference>;


}

impl RiskLogEntry for crate::RiskLogEntry {
        fn uuid<'a>(&'a self) -> &'a str {
        return &self.uuid[..];
    }
        fn title<'a>(&'a self) -> Option<&'a str> {
        return self.title.as_deref();
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn start<'a>(&'a self) -> &'a str {
        return &self.start[..];
    }
        fn end<'a>(&'a self) -> Option<&'a str> {
        return self.end.as_deref();
    }
        fn logged_by<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::LoggedBy>> {
        return self.logged_by.as_ref();
    }
        fn status_change(&self) -> Option<risk_log_entry_utl::status_change_range> {
                self.status_change.as_ref().cloned()
    }
        fn related_responses<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::RiskResponseReference>> {
        return self.related_responses.as_ref();
    }
}


pub trait LoggedBy   {

    fn party_uuid<'a>(&'a self) -> &'a str;
    // fn party_uuid_mut(&mut self) -> &mut &'a str;
    // fn set_party_uuid(&mut self, value: String);

    fn role_id<'a>(&'a self) -> Option<&'a str>;
    // fn role_id_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_role_id(&mut self, value: Option<&'a str>);

    fn remarks<'a>(&'a self) -> Option<&'a str>;
    // fn remarks_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_remarks(&mut self, value: Option<&'a str>);


}

impl LoggedBy for crate::LoggedBy {
        fn party_uuid<'a>(&'a self) -> &'a str {
        return &self.party_uuid[..];
    }
        fn role_id<'a>(&'a self) -> Option<&'a str> {
        return self.role_id.as_deref();
    }
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}


pub trait RiskResponseReference : OscalCommon   {

    fn response_uuid<'a>(&'a self) -> &'a str;
    // fn response_uuid_mut(&mut self) -> &mut &'a str;
    // fn set_response_uuid(&mut self, value: String);

    fn related_tasks<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::RelatedTask>>;
    // fn related_tasks_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::RelatedTask>>;
    // fn set_related_tasks<E>(&mut self, value: Option<&Vec<E>>) where E: Into<RelatedTask>;


}

impl RiskResponseReference for crate::RiskResponseReference {
        fn response_uuid<'a>(&'a self) -> &'a str {
        return &self.response_uuid[..];
    }
        fn related_tasks<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::RelatedTask>> {
        return self.related_tasks.as_ref();
    }
}


pub trait SspDocument : OscalDocument   {

    fn system_security_plan<'a>(&'a self) -> &'a crate::SystemSecurityPlan;
    // fn system_security_plan_mut(&mut self) -> &mut &'a crate::SystemSecurityPlan;
    // fn set_system_security_plan<E>(&mut self, value: E) where E: Into<SystemSecurityPlan>;


}

impl SspDocument for crate::SspDocument {
        fn system_security_plan<'a>(&'a self) -> &'a crate::SystemSecurityPlan {
        return &self.system_security_plan;
    }
}


pub trait SystemSecurityPlan   {

    fn uuid<'a>(&'a self) -> &'a str;
    // fn uuid_mut(&mut self) -> &mut &'a str;
    // fn set_uuid(&mut self, value: String);

    fn metadata<'a>(&'a self) -> &'a crate::Metadata;
    // fn metadata_mut(&mut self) -> &mut &'a crate::Metadata;
    // fn set_metadata<E>(&mut self, value: E) where E: Into<Metadata>;

    fn import_profile<'a>(&'a self) -> &'a crate::ImportProfile;
    // fn import_profile_mut(&mut self) -> &mut &'a crate::ImportProfile;
    // fn set_import_profile<E>(&mut self, value: E) where E: Into<ImportProfile>;

    fn system_characteristics<'a>(&'a self) -> &'a crate::SystemCharacteristics;
    // fn system_characteristics_mut(&mut self) -> &mut &'a crate::SystemCharacteristics;
    // fn set_system_characteristics<E>(&mut self, value: E) where E: Into<SystemCharacteristics>;

    fn system_implementation<'a>(&'a self) -> &'a crate::SystemImplementation;
    // fn system_implementation_mut(&mut self) -> &mut &'a crate::SystemImplementation;
    // fn set_system_implementation<E>(&mut self, value: E) where E: Into<SystemImplementation>;

    fn control_implementation<'a>(&'a self) -> &'a crate::SspControlImplementation;
    // fn control_implementation_mut(&mut self) -> &mut &'a crate::SspControlImplementation;
    // fn set_control_implementation<E>(&mut self, value: E) where E: Into<SspControlImplementation>;

    fn back_matter<'a>(&'a self) -> Option<&'a crate::BackMatter>;
    // fn back_matter_mut(&mut self) -> &mut Option<&'a crate::BackMatter>;
    // fn set_back_matter<E>(&mut self, value: Option<E>) where E: Into<BackMatter>;


}

impl SystemSecurityPlan for crate::SystemSecurityPlan {
        fn uuid<'a>(&'a self) -> &'a str {
        return &self.uuid[..];
    }
        fn metadata<'a>(&'a self) -> &'a crate::Metadata {
        return &self.metadata;
    }
        fn import_profile<'a>(&'a self) -> &'a crate::ImportProfile {
        return &self.import_profile;
    }
        fn system_characteristics<'a>(&'a self) -> &'a crate::SystemCharacteristics {
        return &self.system_characteristics;
    }
        fn system_implementation<'a>(&'a self) -> &'a crate::SystemImplementation {
        return &self.system_implementation;
    }
        fn control_implementation<'a>(&'a self) -> &'a crate::SspControlImplementation {
        return &self.control_implementation;
    }
        fn back_matter<'a>(&'a self) -> Option<&'a crate::BackMatter> {
        return self.back_matter.as_ref();
    }
}


pub trait ImportProfile   {

    fn href<'a>(&'a self) -> &'a str;
    // fn href_mut(&mut self) -> &mut &'a str;
    // fn set_href(&mut self, value: String);

    fn remarks<'a>(&'a self) -> Option<&'a str>;
    // fn remarks_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_remarks(&mut self, value: Option<&'a str>);


}

impl ImportProfile for crate::ImportProfile {
        fn href<'a>(&'a self) -> &'a str {
        return &self.href[..];
    }
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}


pub trait SystemCharacteristics   {

    fn system_ids<'a>(&'a self) -> impl poly_containers::SeqRef<'a, crate::SystemId>;
    // fn system_ids_mut(&mut self) -> &mut impl poly_containers::SeqRef<'a, crate::SystemId>;
    // fn set_system_ids<E>(&mut self, value: &Vec<E>) where E: Into<SystemId>;

    fn system_name<'a>(&'a self) -> &'a str;
    // fn system_name_mut(&mut self) -> &mut &'a str;
    // fn set_system_name(&mut self, value: String);

    fn system_name_short<'a>(&'a self) -> Option<&'a str>;
    // fn system_name_short_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_system_name_short(&mut self, value: Option<&'a str>);

    fn description<'a>(&'a self) -> &'a str;
    // fn description_mut(&mut self) -> &mut &'a str;
    // fn set_description(&mut self, value: String);

    fn date_authorized<'a>(&'a self) -> Option<&'a str>;
    // fn date_authorized_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_date_authorized(&mut self, value: Option<&'a str>);

    fn security_sensitivity_level<'a>(&'a self) -> Option<&'a str>;
    // fn security_sensitivity_level_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_security_sensitivity_level(&mut self, value: Option<&'a str>);

    fn system_information<'a>(&'a self) -> &'a crate::SystemInformation;
    // fn system_information_mut(&mut self) -> &mut &'a crate::SystemInformation;
    // fn set_system_information<E>(&mut self, value: E) where E: Into<SystemInformation>;

    fn security_impact_level<'a>(&'a self) -> Option<&'a crate::SecurityImpactLevel>;
    // fn security_impact_level_mut(&mut self) -> &mut Option<&'a crate::SecurityImpactLevel>;
    // fn set_security_impact_level<E>(&mut self, value: Option<E>) where E: Into<SecurityImpactLevel>;

    fn system_status<'a>(&'a self) -> &'a crate::SystemStatus;
    // fn system_status_mut(&mut self) -> &mut &'a crate::SystemStatus;
    // fn set_system_status<E>(&mut self, value: E) where E: Into<SystemStatus>;

    fn authorization_boundary<'a>(&'a self) -> &'a crate::AuthorizationBoundary;
    // fn authorization_boundary_mut(&mut self) -> &mut &'a crate::AuthorizationBoundary;
    // fn set_authorization_boundary<E>(&mut self, value: E) where E: Into<AuthorizationBoundary>;

    fn network_architecture<'a>(&'a self) -> Option<&'a crate::NetworkArchitecture>;
    // fn network_architecture_mut(&mut self) -> &mut Option<&'a crate::NetworkArchitecture>;
    // fn set_network_architecture<E>(&mut self, value: Option<E>) where E: Into<NetworkArchitecture>;

    fn data_flow<'a>(&'a self) -> Option<&'a crate::DataFlow>;
    // fn data_flow_mut(&mut self) -> &mut Option<&'a crate::DataFlow>;
    // fn set_data_flow<E>(&mut self, value: Option<E>) where E: Into<DataFlow>;

    fn responsible_parties<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::SspSystemCharacteristicsResponsibleParty>>;
    // fn responsible_parties_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::SspSystemCharacteristicsResponsibleParty>>;
    // fn set_responsible_parties<E>(&mut self, value: Option<&Vec<E>>) where E: Into<SspSystemCharacteristicsResponsibleParty>;

    fn remarks<'a>(&'a self) -> Option<&'a str>;
    // fn remarks_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_remarks(&mut self, value: Option<&'a str>);


}

impl SystemCharacteristics for crate::SystemCharacteristics {
        fn system_ids<'a>(&'a self) -> impl poly_containers::SeqRef<'a, crate::SystemId> {
        return &self.system_ids;
    }
        fn system_name<'a>(&'a self) -> &'a str {
        return &self.system_name[..];
    }
        fn system_name_short<'a>(&'a self) -> Option<&'a str> {
        return self.system_name_short.as_deref();
    }
        fn description<'a>(&'a self) -> &'a str {
        return &self.description[..];
    }
        fn date_authorized<'a>(&'a self) -> Option<&'a str> {
        return self.date_authorized.as_deref();
    }
        fn security_sensitivity_level<'a>(&'a self) -> Option<&'a str> {
        return self.security_sensitivity_level.as_deref();
    }
        fn system_information<'a>(&'a self) -> &'a crate::SystemInformation {
        return &self.system_information;
    }
        fn security_impact_level<'a>(&'a self) -> Option<&'a crate::SecurityImpactLevel> {
        return self.security_impact_level.as_ref();
    }
        fn system_status<'a>(&'a self) -> &'a crate::SystemStatus {
        return &self.system_status;
    }
        fn authorization_boundary<'a>(&'a self) -> &'a crate::AuthorizationBoundary {
        return &self.authorization_boundary;
    }
        fn network_architecture<'a>(&'a self) -> Option<&'a crate::NetworkArchitecture> {
        return self.network_architecture.as_ref();
    }
        fn data_flow<'a>(&'a self) -> Option<&'a crate::DataFlow> {
        return self.data_flow.as_ref();
    }
        fn responsible_parties<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::SspSystemCharacteristicsResponsibleParty>> {
        return self.responsible_parties.as_ref();
    }
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}


pub trait SystemInformation   {

    fn props<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::SspSystemInformationProp>>;
    // fn props_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::SspSystemInformationProp>>;
    // fn set_props<E>(&mut self, value: Option<&Vec<E>>) where E: Into<SspSystemInformationProp>;

    fn links<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::SspSystemInformationLink>>;
    // fn links_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::SspSystemInformationLink>>;
    // fn set_links<E>(&mut self, value: Option<&Vec<E>>) where E: Into<SspSystemInformationLink>;

    fn information_types<'a>(&'a self) -> impl poly_containers::SeqRef<'a, crate::InformationType>;
    // fn information_types_mut(&mut self) -> &mut impl poly_containers::SeqRef<'a, crate::InformationType>;
    // fn set_information_types<E>(&mut self, value: &Vec<E>) where E: Into<InformationType>;


}

impl SystemInformation for crate::SystemInformation {
        fn props<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::SspSystemInformationProp>> {
        return self.props.as_ref();
    }
        fn links<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::SspSystemInformationLink>> {
        return self.links.as_ref();
    }
        fn information_types<'a>(&'a self) -> impl poly_containers::SeqRef<'a, crate::InformationType> {
        return &self.information_types;
    }
}


pub trait InformationType   {

    fn uuid<'a>(&'a self) -> Option<&'a str>;
    // fn uuid_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_uuid(&mut self, value: Option<&'a str>);

    fn title<'a>(&'a self) -> &'a str;
    // fn title_mut(&mut self) -> &mut &'a str;
    // fn set_title(&mut self, value: String);

    fn description<'a>(&'a self) -> &'a str;
    // fn description_mut(&mut self) -> &mut &'a str;
    // fn set_description(&mut self, value: String);

    fn categorizations<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::InformationTypeCategorization>>;
    // fn categorizations_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::InformationTypeCategorization>>;
    // fn set_categorizations<E>(&mut self, value: Option<&Vec<E>>) where E: Into<InformationTypeCategorization>;

    fn props<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, PropertyOrSubtype>>;
    // fn props_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, PropertyOrSubtype>>;
    // fn set_props<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Property>;

    fn links<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, LinkOrSubtype>>;
    // fn links_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, LinkOrSubtype>>;
    // fn set_links<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Link>;

    fn confidentiality_impact<'a>(&'a self) -> Option<&'a crate::ImpactLevel>;
    // fn confidentiality_impact_mut(&mut self) -> &mut Option<&'a crate::ImpactLevel>;
    // fn set_confidentiality_impact<E>(&mut self, value: Option<E>) where E: Into<ImpactLevel>;

    fn integrity_impact<'a>(&'a self) -> Option<&'a crate::ImpactLevel>;
    // fn integrity_impact_mut(&mut self) -> &mut Option<&'a crate::ImpactLevel>;
    // fn set_integrity_impact<E>(&mut self, value: Option<E>) where E: Into<ImpactLevel>;

    fn availability_impact<'a>(&'a self) -> Option<&'a crate::ImpactLevel>;
    // fn availability_impact_mut(&mut self) -> &mut Option<&'a crate::ImpactLevel>;
    // fn set_availability_impact<E>(&mut self, value: Option<E>) where E: Into<ImpactLevel>;


}

impl InformationType for crate::InformationType {
        fn uuid<'a>(&'a self) -> Option<&'a str> {
        return self.uuid.as_deref();
    }
        fn title<'a>(&'a self) -> &'a str {
        return &self.title[..];
    }
        fn description<'a>(&'a self) -> &'a str {
        return &self.description[..];
    }
        fn categorizations<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::InformationTypeCategorization>> {
        return self.categorizations.as_ref();
    }
        fn props<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, PropertyOrSubtype>> {
        return self.props.as_ref();
    }
        fn links<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, LinkOrSubtype>> {
        return self.links.as_ref();
    }
        fn confidentiality_impact<'a>(&'a self) -> Option<&'a crate::ImpactLevel> {
        return self.confidentiality_impact.as_ref();
    }
        fn integrity_impact<'a>(&'a self) -> Option<&'a crate::ImpactLevel> {
        return self.integrity_impact.as_ref();
    }
        fn availability_impact<'a>(&'a self) -> Option<&'a crate::ImpactLevel> {
        return self.availability_impact.as_ref();
    }
}


pub trait InformationTypeCategorization   {

    fn system(&self) -> information_type_categorization_utl::system_range;
    // fn system_mut(&mut self) -> &mut information_type_categorization_utl::system_range;
    // fn set_system(&mut self, value: information_type_categorization_utl::system_range);

    fn information_type_ids<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn information_type_ids_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_information_type_ids(&mut self, value: Option<&Vec<String>>);


}

impl InformationTypeCategorization for crate::InformationTypeCategorization {
        fn system(&self) -> information_type_categorization_utl::system_range {
            self.system.clone()
    }
        fn information_type_ids<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.information_type_ids.as_ref();
    }
}


pub trait ImpactLevel   {

    fn props<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, PropertyOrSubtype>>;
    // fn props_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, PropertyOrSubtype>>;
    // fn set_props<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Property>;

    fn links<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, LinkOrSubtype>>;
    // fn links_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, LinkOrSubtype>>;
    // fn set_links<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Link>;

    fn base(&self) -> impact_level_utl::base_range;
    // fn base_mut(&mut self) -> &mut impact_level_utl::base_range;
    // fn set_base(&mut self, value: impact_level_utl::base_range);

    fn selected(&self) -> Option<impact_level_utl::selected_range>;
    // fn selected_mut(&mut self) -> &mut Option<impact_level_utl::selected_range>;
    // fn set_selected(&mut self, value: Option<&'a impact_level_utl::selected_range>);

    fn adjustment_justification<'a>(&'a self) -> Option<&'a str>;
    // fn adjustment_justification_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_adjustment_justification(&mut self, value: Option<&'a str>);


}

impl ImpactLevel for crate::ImpactLevel {
        fn props<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, PropertyOrSubtype>> {
        return self.props.as_ref();
    }
        fn links<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, LinkOrSubtype>> {
        return self.links.as_ref();
    }
        fn base(&self) -> impact_level_utl::base_range {
            self.base.clone()
    }
        fn selected(&self) -> Option<impact_level_utl::selected_range> {
                self.selected.as_ref().cloned()
    }
        fn adjustment_justification<'a>(&'a self) -> Option<&'a str> {
        return self.adjustment_justification.as_deref();
    }
}


pub trait SecurityImpactLevel   {

    fn security_objective_confidentiality<'a>(&'a self) -> &'a str;
    // fn security_objective_confidentiality_mut(&mut self) -> &mut &'a str;
    // fn set_security_objective_confidentiality(&mut self, value: String);

    fn security_objective_integrity<'a>(&'a self) -> &'a str;
    // fn security_objective_integrity_mut(&mut self) -> &mut &'a str;
    // fn set_security_objective_integrity(&mut self, value: String);

    fn security_objective_availability<'a>(&'a self) -> &'a str;
    // fn security_objective_availability_mut(&mut self) -> &mut &'a str;
    // fn set_security_objective_availability(&mut self, value: String);


}

impl SecurityImpactLevel for crate::SecurityImpactLevel {
        fn security_objective_confidentiality<'a>(&'a self) -> &'a str {
        return &self.security_objective_confidentiality[..];
    }
        fn security_objective_integrity<'a>(&'a self) -> &'a str {
        return &self.security_objective_integrity[..];
    }
        fn security_objective_availability<'a>(&'a self) -> &'a str {
        return &self.security_objective_availability[..];
    }
}


pub trait SystemStatus   {

    fn remarks<'a>(&'a self) -> Option<&'a str>;
    // fn remarks_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_remarks(&mut self, value: Option<&'a str>);

    fn state<'a>(&'a self) -> &'a crate::SystemOperatingStatusEnum;
    // fn state_mut(&mut self) -> &mut &'a crate::SystemOperatingStatusEnum;
    // fn set_state(&mut self, value: SystemOperatingStatusEnum);


}

impl SystemStatus for crate::SystemStatus {
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
        fn state<'a>(&'a self) -> &'a crate::SystemOperatingStatusEnum {
        return &self.state;
    }
}


pub trait AuthorizationBoundary   {

    fn description<'a>(&'a self) -> &'a str;
    // fn description_mut(&mut self) -> &mut &'a str;
    // fn set_description(&mut self, value: String);

    fn props<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, PropertyOrSubtype>>;
    // fn props_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, PropertyOrSubtype>>;
    // fn set_props<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Property>;

    fn links<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, LinkOrSubtype>>;
    // fn links_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, LinkOrSubtype>>;
    // fn set_links<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Link>;

    fn diagrams<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Diagram>>;
    // fn diagrams_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::Diagram>>;
    // fn set_diagrams<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Diagram>;

    fn remarks<'a>(&'a self) -> Option<&'a str>;
    // fn remarks_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_remarks(&mut self, value: Option<&'a str>);


}

impl AuthorizationBoundary for crate::AuthorizationBoundary {
        fn description<'a>(&'a self) -> &'a str {
        return &self.description[..];
    }
        fn props<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, PropertyOrSubtype>> {
        return self.props.as_ref();
    }
        fn links<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, LinkOrSubtype>> {
        return self.links.as_ref();
    }
        fn diagrams<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Diagram>> {
        return self.diagrams.as_ref();
    }
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}


pub trait Diagram   {

    fn uuid<'a>(&'a self) -> &'a str;
    // fn uuid_mut(&mut self) -> &mut &'a str;
    // fn set_uuid(&mut self, value: String);

    fn description<'a>(&'a self) -> Option<&'a str>;
    // fn description_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_description(&mut self, value: Option<&'a str>);

    fn props<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, PropertyOrSubtype>>;
    // fn props_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, PropertyOrSubtype>>;
    // fn set_props<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Property>;

    fn links<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::SspDiagramLink>>;
    // fn links_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::SspDiagramLink>>;
    // fn set_links<E>(&mut self, value: Option<&Vec<E>>) where E: Into<SspDiagramLink>;

    fn caption<'a>(&'a self) -> Option<&'a str>;
    // fn caption_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_caption(&mut self, value: Option<&'a str>);

    fn remarks<'a>(&'a self) -> Option<&'a str>;
    // fn remarks_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_remarks(&mut self, value: Option<&'a str>);


}

impl Diagram for crate::Diagram {
        fn uuid<'a>(&'a self) -> &'a str {
        return &self.uuid[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn props<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, PropertyOrSubtype>> {
        return self.props.as_ref();
    }
        fn links<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::SspDiagramLink>> {
        return self.links.as_ref();
    }
        fn caption<'a>(&'a self) -> Option<&'a str> {
        return self.caption.as_deref();
    }
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}


pub trait NetworkArchitecture   {

    fn description<'a>(&'a self) -> &'a str;
    // fn description_mut(&mut self) -> &mut &'a str;
    // fn set_description(&mut self, value: String);

    fn props<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, PropertyOrSubtype>>;
    // fn props_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, PropertyOrSubtype>>;
    // fn set_props<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Property>;

    fn links<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, LinkOrSubtype>>;
    // fn links_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, LinkOrSubtype>>;
    // fn set_links<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Link>;

    fn diagrams<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Diagram>>;
    // fn diagrams_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::Diagram>>;
    // fn set_diagrams<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Diagram>;

    fn remarks<'a>(&'a self) -> Option<&'a str>;
    // fn remarks_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_remarks(&mut self, value: Option<&'a str>);


}

impl NetworkArchitecture for crate::NetworkArchitecture {
        fn description<'a>(&'a self) -> &'a str {
        return &self.description[..];
    }
        fn props<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, PropertyOrSubtype>> {
        return self.props.as_ref();
    }
        fn links<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, LinkOrSubtype>> {
        return self.links.as_ref();
    }
        fn diagrams<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Diagram>> {
        return self.diagrams.as_ref();
    }
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}


pub trait DataFlow   {

    fn description<'a>(&'a self) -> &'a str;
    // fn description_mut(&mut self) -> &mut &'a str;
    // fn set_description(&mut self, value: String);

    fn props<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, PropertyOrSubtype>>;
    // fn props_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, PropertyOrSubtype>>;
    // fn set_props<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Property>;

    fn links<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, LinkOrSubtype>>;
    // fn links_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, LinkOrSubtype>>;
    // fn set_links<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Link>;

    fn diagrams<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Diagram>>;
    // fn diagrams_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::Diagram>>;
    // fn set_diagrams<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Diagram>;

    fn remarks<'a>(&'a self) -> Option<&'a str>;
    // fn remarks_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_remarks(&mut self, value: Option<&'a str>);


}

impl DataFlow for crate::DataFlow {
        fn description<'a>(&'a self) -> &'a str {
        return &self.description[..];
    }
        fn props<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, PropertyOrSubtype>> {
        return self.props.as_ref();
    }
        fn links<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, LinkOrSubtype>> {
        return self.links.as_ref();
    }
        fn diagrams<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Diagram>> {
        return self.diagrams.as_ref();
    }
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}


pub trait SystemImplementation   {

    fn props<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, PropertyOrSubtype>>;
    // fn props_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, PropertyOrSubtype>>;
    // fn set_props<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Property>;

    fn links<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, LinkOrSubtype>>;
    // fn links_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, LinkOrSubtype>>;
    // fn set_links<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Link>;

    fn leveraged_authorizations<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::LeveragedAuthorization>>;
    // fn leveraged_authorizations_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::LeveragedAuthorization>>;
    // fn set_leveraged_authorizations<E>(&mut self, value: Option<&Vec<E>>) where E: Into<LeveragedAuthorization>;

    fn users<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::SystemUser>>;
    // fn users_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::SystemUser>>;
    // fn set_users<E>(&mut self, value: Option<&Vec<E>>) where E: Into<SystemUser>;

    fn components<'a>(&'a self) -> impl poly_containers::SeqRef<'a, crate::SspSystemComponent>;
    // fn components_mut(&mut self) -> &mut impl poly_containers::SeqRef<'a, crate::SspSystemComponent>;
    // fn set_components<E>(&mut self, value: &Vec<E>) where E: Into<SspSystemComponent>;

    fn inventory_items<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::SspInventoryItem>>;
    // fn inventory_items_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::SspInventoryItem>>;
    // fn set_inventory_items<E>(&mut self, value: Option<&Vec<E>>) where E: Into<SspInventoryItem>;

    fn remarks<'a>(&'a self) -> Option<&'a str>;
    // fn remarks_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_remarks(&mut self, value: Option<&'a str>);


}

impl SystemImplementation for crate::SystemImplementation {
        fn props<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, PropertyOrSubtype>> {
        return self.props.as_ref();
    }
        fn links<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, LinkOrSubtype>> {
        return self.links.as_ref();
    }
        fn leveraged_authorizations<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::LeveragedAuthorization>> {
        return self.leveraged_authorizations.as_ref();
    }
        fn users<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::SystemUser>> {
        return self.users.as_ref();
    }
        fn components<'a>(&'a self) -> impl poly_containers::SeqRef<'a, crate::SspSystemComponent> {
        return &self.components;
    }
        fn inventory_items<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::SspInventoryItem>> {
        return self.inventory_items.as_ref();
    }
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}


pub trait LeveragedAuthorization   {

    fn uuid<'a>(&'a self) -> &'a str;
    // fn uuid_mut(&mut self) -> &mut &'a str;
    // fn set_uuid(&mut self, value: String);

    fn title<'a>(&'a self) -> &'a str;
    // fn title_mut(&mut self) -> &mut &'a str;
    // fn set_title(&mut self, value: String);

    fn props<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, PropertyOrSubtype>>;
    // fn props_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, PropertyOrSubtype>>;
    // fn set_props<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Property>;

    fn links<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::SspLeveragedAuthorizationLink>>;
    // fn links_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::SspLeveragedAuthorizationLink>>;
    // fn set_links<E>(&mut self, value: Option<&Vec<E>>) where E: Into<SspLeveragedAuthorizationLink>;

    fn party_uuid<'a>(&'a self) -> &'a str;
    // fn party_uuid_mut(&mut self) -> &mut &'a str;
    // fn set_party_uuid(&mut self, value: String);

    fn date_authorized<'a>(&'a self) -> &'a str;
    // fn date_authorized_mut(&mut self) -> &mut &'a str;
    // fn set_date_authorized(&mut self, value: String);

    fn remarks<'a>(&'a self) -> Option<&'a str>;
    // fn remarks_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_remarks(&mut self, value: Option<&'a str>);


}

impl LeveragedAuthorization for crate::LeveragedAuthorization {
        fn uuid<'a>(&'a self) -> &'a str {
        return &self.uuid[..];
    }
        fn title<'a>(&'a self) -> &'a str {
        return &self.title[..];
    }
        fn props<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, PropertyOrSubtype>> {
        return self.props.as_ref();
    }
        fn links<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::SspLeveragedAuthorizationLink>> {
        return self.links.as_ref();
    }
        fn party_uuid<'a>(&'a self) -> &'a str {
        return &self.party_uuid[..];
    }
        fn date_authorized<'a>(&'a self) -> &'a str {
        return &self.date_authorized[..];
    }
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}


pub trait SspControlImplementation   {

    fn description<'a>(&'a self) -> &'a str;
    // fn description_mut(&mut self) -> &mut &'a str;
    // fn set_description(&mut self, value: String);

    fn set_parameters<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::SetParameter>>;
    // fn set_parameters_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::SetParameter>>;
    // fn set_set_parameters<E>(&mut self, value: Option<&Vec<E>>) where E: Into<SetParameter>;

    fn implemented_requirements<'a>(&'a self) -> impl poly_containers::SeqRef<'a, crate::SspImplementedRequirement>;
    // fn implemented_requirements_mut(&mut self) -> &mut impl poly_containers::SeqRef<'a, crate::SspImplementedRequirement>;
    // fn set_implemented_requirements<E>(&mut self, value: &Vec<E>) where E: Into<SspImplementedRequirement>;


}

impl SspControlImplementation for crate::SspControlImplementation {
        fn description<'a>(&'a self) -> &'a str {
        return &self.description[..];
    }
        fn set_parameters<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::SetParameter>> {
        return self.set_parameters.as_ref();
    }
        fn implemented_requirements<'a>(&'a self) -> impl poly_containers::SeqRef<'a, crate::SspImplementedRequirement> {
        return &self.implemented_requirements;
    }
}


pub trait SspImplementedRequirement   {

    fn uuid<'a>(&'a self) -> &'a str;
    // fn uuid_mut(&mut self) -> &mut &'a str;
    // fn set_uuid(&mut self, value: String);

    fn control_id<'a>(&'a self) -> &'a str;
    // fn control_id_mut(&mut self) -> &mut &'a str;
    // fn set_control_id(&mut self, value: String);

    fn props<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::SspControlOriginationProp>>;
    // fn props_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::SspControlOriginationProp>>;
    // fn set_props<E>(&mut self, value: Option<&Vec<E>>) where E: Into<SspControlOriginationProp>;

    fn links<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, LinkOrSubtype>>;
    // fn links_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, LinkOrSubtype>>;
    // fn set_links<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Link>;

    fn set_parameters<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::SetParameter>>;
    // fn set_parameters_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::SetParameter>>;
    // fn set_set_parameters<E>(&mut self, value: Option<&Vec<E>>) where E: Into<SetParameter>;

    fn responsible_roles<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::SspImplementedRequirementResponsibleRole>>;
    // fn responsible_roles_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::SspImplementedRequirementResponsibleRole>>;
    // fn set_responsible_roles<E>(&mut self, value: Option<&Vec<E>>) where E: Into<SspImplementedRequirementResponsibleRole>;

    fn statements<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::SspStatement>>;
    // fn statements_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::SspStatement>>;
    // fn set_statements<E>(&mut self, value: Option<&Vec<E>>) where E: Into<SspStatement>;

    fn by_components<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::ByComponent>>;
    // fn by_components_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::ByComponent>>;
    // fn set_by_components<E>(&mut self, value: Option<&Vec<E>>) where E: Into<ByComponent>;

    fn remarks<'a>(&'a self) -> Option<&'a str>;
    // fn remarks_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_remarks(&mut self, value: Option<&'a str>);


}

impl SspImplementedRequirement for crate::SspImplementedRequirement {
        fn uuid<'a>(&'a self) -> &'a str {
        return &self.uuid[..];
    }
        fn control_id<'a>(&'a self) -> &'a str {
        return &self.control_id[..];
    }
        fn props<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::SspControlOriginationProp>> {
        return self.props.as_ref();
    }
        fn links<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, LinkOrSubtype>> {
        return self.links.as_ref();
    }
        fn set_parameters<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::SetParameter>> {
        return self.set_parameters.as_ref();
    }
        fn responsible_roles<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::SspImplementedRequirementResponsibleRole>> {
        return self.responsible_roles.as_ref();
    }
        fn statements<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::SspStatement>> {
        return self.statements.as_ref();
    }
        fn by_components<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::ByComponent>> {
        return self.by_components.as_ref();
    }
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}


pub trait SspStatement   {

    fn statement_id<'a>(&'a self) -> &'a str;
    // fn statement_id_mut(&mut self) -> &mut &'a str;
    // fn set_statement_id(&mut self, value: String);

    fn uuid<'a>(&'a self) -> &'a str;
    // fn uuid_mut(&mut self) -> &mut &'a str;
    // fn set_uuid(&mut self, value: String);

    fn props<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::SspControlOriginationProp>>;
    // fn props_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::SspControlOriginationProp>>;
    // fn set_props<E>(&mut self, value: Option<&Vec<E>>) where E: Into<SspControlOriginationProp>;

    fn links<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, LinkOrSubtype>>;
    // fn links_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, LinkOrSubtype>>;
    // fn set_links<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Link>;

    fn responsible_roles<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::SspImplementedRequirementResponsibleRole>>;
    // fn responsible_roles_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::SspImplementedRequirementResponsibleRole>>;
    // fn set_responsible_roles<E>(&mut self, value: Option<&Vec<E>>) where E: Into<SspImplementedRequirementResponsibleRole>;

    fn by_components<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::ByComponent>>;
    // fn by_components_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::ByComponent>>;
    // fn set_by_components<E>(&mut self, value: Option<&Vec<E>>) where E: Into<ByComponent>;

    fn remarks<'a>(&'a self) -> Option<&'a str>;
    // fn remarks_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_remarks(&mut self, value: Option<&'a str>);


}

impl SspStatement for crate::SspStatement {
        fn statement_id<'a>(&'a self) -> &'a str {
        return &self.statement_id[..];
    }
        fn uuid<'a>(&'a self) -> &'a str {
        return &self.uuid[..];
    }
        fn props<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::SspControlOriginationProp>> {
        return self.props.as_ref();
    }
        fn links<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, LinkOrSubtype>> {
        return self.links.as_ref();
    }
        fn responsible_roles<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::SspImplementedRequirementResponsibleRole>> {
        return self.responsible_roles.as_ref();
    }
        fn by_components<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::ByComponent>> {
        return self.by_components.as_ref();
    }
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}


pub trait ByComponent   {

    fn component_uuid<'a>(&'a self) -> &'a str;
    // fn component_uuid_mut(&mut self) -> &mut &'a str;
    // fn set_component_uuid(&mut self, value: String);

    fn uuid<'a>(&'a self) -> &'a str;
    // fn uuid_mut(&mut self) -> &mut &'a str;
    // fn set_uuid(&mut self, value: String);

    fn description<'a>(&'a self) -> &'a str;
    // fn description_mut(&mut self) -> &mut &'a str;
    // fn set_description(&mut self, value: String);

    fn props<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::SspControlOriginationProp>>;
    // fn props_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::SspControlOriginationProp>>;
    // fn set_props<E>(&mut self, value: Option<&Vec<E>>) where E: Into<SspControlOriginationProp>;

    fn links<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::SspByComponentLink>>;
    // fn links_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::SspByComponentLink>>;
    // fn set_links<E>(&mut self, value: Option<&Vec<E>>) where E: Into<SspByComponentLink>;

    fn set_parameters<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::SetParameter>>;
    // fn set_parameters_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::SetParameter>>;
    // fn set_set_parameters<E>(&mut self, value: Option<&Vec<E>>) where E: Into<SetParameter>;

    fn implementation_status<'a>(&'a self) -> Option<&'a crate::ImplementationStatus>;
    // fn implementation_status_mut(&mut self) -> &mut Option<&'a crate::ImplementationStatus>;
    // fn set_implementation_status<E>(&mut self, value: Option<E>) where E: Into<ImplementationStatus>;

    fn export<'a>(&'a self) -> Option<&'a crate::Export>;
    // fn export_mut(&mut self) -> &mut Option<&'a crate::Export>;
    // fn set_export<E>(&mut self, value: Option<E>) where E: Into<Export>;

    fn inherited<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::InheritedControlImplementation>>;
    // fn inherited_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::InheritedControlImplementation>>;
    // fn set_inherited<E>(&mut self, value: Option<&Vec<E>>) where E: Into<InheritedControlImplementation>;

    fn satisfied<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::SatisfiedControlImplementation>>;
    // fn satisfied_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::SatisfiedControlImplementation>>;
    // fn set_satisfied<E>(&mut self, value: Option<&Vec<E>>) where E: Into<SatisfiedControlImplementation>;

    fn responsible_roles<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::SspByComponentResponsibleRole>>;
    // fn responsible_roles_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::SspByComponentResponsibleRole>>;
    // fn set_responsible_roles<E>(&mut self, value: Option<&Vec<E>>) where E: Into<SspByComponentResponsibleRole>;

    fn remarks<'a>(&'a self) -> Option<&'a str>;
    // fn remarks_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_remarks(&mut self, value: Option<&'a str>);


}

impl ByComponent for crate::ByComponent {
        fn component_uuid<'a>(&'a self) -> &'a str {
        return &self.component_uuid[..];
    }
        fn uuid<'a>(&'a self) -> &'a str {
        return &self.uuid[..];
    }
        fn description<'a>(&'a self) -> &'a str {
        return &self.description[..];
    }
        fn props<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::SspControlOriginationProp>> {
        return self.props.as_ref();
    }
        fn links<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::SspByComponentLink>> {
        return self.links.as_ref();
    }
        fn set_parameters<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::SetParameter>> {
        return self.set_parameters.as_ref();
    }
        fn implementation_status<'a>(&'a self) -> Option<&'a crate::ImplementationStatus> {
        return self.implementation_status.as_ref();
    }
        fn export<'a>(&'a self) -> Option<&'a crate::Export> {
        return self.export.as_ref();
    }
        fn inherited<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::InheritedControlImplementation>> {
        return self.inherited.as_ref();
    }
        fn satisfied<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::SatisfiedControlImplementation>> {
        return self.satisfied.as_ref();
    }
        fn responsible_roles<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::SspByComponentResponsibleRole>> {
        return self.responsible_roles.as_ref();
    }
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}


pub trait Export   {

    fn description<'a>(&'a self) -> Option<&'a str>;
    // fn description_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_description(&mut self, value: Option<&'a str>);

    fn props<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, PropertyOrSubtype>>;
    // fn props_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, PropertyOrSubtype>>;
    // fn set_props<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Property>;

    fn links<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, LinkOrSubtype>>;
    // fn links_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, LinkOrSubtype>>;
    // fn set_links<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Link>;

    fn provided<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::ProvidedControlImplementation>>;
    // fn provided_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::ProvidedControlImplementation>>;
    // fn set_provided<E>(&mut self, value: Option<&Vec<E>>) where E: Into<ProvidedControlImplementation>;

    fn responsibilities<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::ControlResponsibility>>;
    // fn responsibilities_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::ControlResponsibility>>;
    // fn set_responsibilities<E>(&mut self, value: Option<&Vec<E>>) where E: Into<ControlResponsibility>;


}

impl Export for crate::Export {
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn props<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, PropertyOrSubtype>> {
        return self.props.as_ref();
    }
        fn links<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, LinkOrSubtype>> {
        return self.links.as_ref();
    }
        fn provided<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::ProvidedControlImplementation>> {
        return self.provided.as_ref();
    }
        fn responsibilities<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::ControlResponsibility>> {
        return self.responsibilities.as_ref();
    }
}


pub trait ProvidedControlImplementation   {

    fn uuid<'a>(&'a self) -> &'a str;
    // fn uuid_mut(&mut self) -> &mut &'a str;
    // fn set_uuid(&mut self, value: String);

    fn description<'a>(&'a self) -> &'a str;
    // fn description_mut(&mut self) -> &mut &'a str;
    // fn set_description(&mut self, value: String);

    fn props<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, PropertyOrSubtype>>;
    // fn props_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, PropertyOrSubtype>>;
    // fn set_props<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Property>;

    fn links<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, LinkOrSubtype>>;
    // fn links_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, LinkOrSubtype>>;
    // fn set_links<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Link>;

    fn responsible_roles<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::SspByComponentResponsibleRole>>;
    // fn responsible_roles_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::SspByComponentResponsibleRole>>;
    // fn set_responsible_roles<E>(&mut self, value: Option<&Vec<E>>) where E: Into<SspByComponentResponsibleRole>;

    fn remarks<'a>(&'a self) -> Option<&'a str>;
    // fn remarks_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_remarks(&mut self, value: Option<&'a str>);


}

impl ProvidedControlImplementation for crate::ProvidedControlImplementation {
        fn uuid<'a>(&'a self) -> &'a str {
        return &self.uuid[..];
    }
        fn description<'a>(&'a self) -> &'a str {
        return &self.description[..];
    }
        fn props<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, PropertyOrSubtype>> {
        return self.props.as_ref();
    }
        fn links<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, LinkOrSubtype>> {
        return self.links.as_ref();
    }
        fn responsible_roles<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::SspByComponentResponsibleRole>> {
        return self.responsible_roles.as_ref();
    }
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}


pub trait ControlResponsibility   {

    fn uuid<'a>(&'a self) -> &'a str;
    // fn uuid_mut(&mut self) -> &mut &'a str;
    // fn set_uuid(&mut self, value: String);

    fn provided_uuid<'a>(&'a self) -> Option<&'a str>;
    // fn provided_uuid_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_provided_uuid(&mut self, value: Option<&'a str>);

    fn description<'a>(&'a self) -> &'a str;
    // fn description_mut(&mut self) -> &mut &'a str;
    // fn set_description(&mut self, value: String);

    fn props<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, PropertyOrSubtype>>;
    // fn props_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, PropertyOrSubtype>>;
    // fn set_props<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Property>;

    fn links<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, LinkOrSubtype>>;
    // fn links_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, LinkOrSubtype>>;
    // fn set_links<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Link>;

    fn responsible_roles<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::SspByComponentResponsibleRole>>;
    // fn responsible_roles_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::SspByComponentResponsibleRole>>;
    // fn set_responsible_roles<E>(&mut self, value: Option<&Vec<E>>) where E: Into<SspByComponentResponsibleRole>;

    fn remarks<'a>(&'a self) -> Option<&'a str>;
    // fn remarks_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_remarks(&mut self, value: Option<&'a str>);


}

impl ControlResponsibility for crate::ControlResponsibility {
        fn uuid<'a>(&'a self) -> &'a str {
        return &self.uuid[..];
    }
        fn provided_uuid<'a>(&'a self) -> Option<&'a str> {
        return self.provided_uuid.as_deref();
    }
        fn description<'a>(&'a self) -> &'a str {
        return &self.description[..];
    }
        fn props<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, PropertyOrSubtype>> {
        return self.props.as_ref();
    }
        fn links<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, LinkOrSubtype>> {
        return self.links.as_ref();
    }
        fn responsible_roles<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::SspByComponentResponsibleRole>> {
        return self.responsible_roles.as_ref();
    }
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}


pub trait InheritedControlImplementation   {

    fn uuid<'a>(&'a self) -> &'a str;
    // fn uuid_mut(&mut self) -> &mut &'a str;
    // fn set_uuid(&mut self, value: String);

    fn provided_uuid<'a>(&'a self) -> Option<&'a str>;
    // fn provided_uuid_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_provided_uuid(&mut self, value: Option<&'a str>);

    fn description<'a>(&'a self) -> &'a str;
    // fn description_mut(&mut self) -> &mut &'a str;
    // fn set_description(&mut self, value: String);

    fn props<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, PropertyOrSubtype>>;
    // fn props_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, PropertyOrSubtype>>;
    // fn set_props<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Property>;

    fn links<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, LinkOrSubtype>>;
    // fn links_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, LinkOrSubtype>>;
    // fn set_links<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Link>;

    fn responsible_roles<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::SspByComponentResponsibleRole>>;
    // fn responsible_roles_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::SspByComponentResponsibleRole>>;
    // fn set_responsible_roles<E>(&mut self, value: Option<&Vec<E>>) where E: Into<SspByComponentResponsibleRole>;

    fn remarks<'a>(&'a self) -> Option<&'a str>;
    // fn remarks_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_remarks(&mut self, value: Option<&'a str>);


}

impl InheritedControlImplementation for crate::InheritedControlImplementation {
        fn uuid<'a>(&'a self) -> &'a str {
        return &self.uuid[..];
    }
        fn provided_uuid<'a>(&'a self) -> Option<&'a str> {
        return self.provided_uuid.as_deref();
    }
        fn description<'a>(&'a self) -> &'a str {
        return &self.description[..];
    }
        fn props<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, PropertyOrSubtype>> {
        return self.props.as_ref();
    }
        fn links<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, LinkOrSubtype>> {
        return self.links.as_ref();
    }
        fn responsible_roles<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::SspByComponentResponsibleRole>> {
        return self.responsible_roles.as_ref();
    }
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}


pub trait SatisfiedControlImplementation   {

    fn uuid<'a>(&'a self) -> &'a str;
    // fn uuid_mut(&mut self) -> &mut &'a str;
    // fn set_uuid(&mut self, value: String);

    fn responsibility_uuid<'a>(&'a self) -> Option<&'a str>;
    // fn responsibility_uuid_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_responsibility_uuid(&mut self, value: Option<&'a str>);

    fn description<'a>(&'a self) -> &'a str;
    // fn description_mut(&mut self) -> &mut &'a str;
    // fn set_description(&mut self, value: String);

    fn props<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, PropertyOrSubtype>>;
    // fn props_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, PropertyOrSubtype>>;
    // fn set_props<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Property>;

    fn links<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, LinkOrSubtype>>;
    // fn links_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, LinkOrSubtype>>;
    // fn set_links<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Link>;

    fn responsible_roles<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::SspByComponentResponsibleRole>>;
    // fn responsible_roles_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::SspByComponentResponsibleRole>>;
    // fn set_responsible_roles<E>(&mut self, value: Option<&Vec<E>>) where E: Into<SspByComponentResponsibleRole>;

    fn remarks<'a>(&'a self) -> Option<&'a str>;
    // fn remarks_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_remarks(&mut self, value: Option<&'a str>);


}

impl SatisfiedControlImplementation for crate::SatisfiedControlImplementation {
        fn uuid<'a>(&'a self) -> &'a str {
        return &self.uuid[..];
    }
        fn responsibility_uuid<'a>(&'a self) -> Option<&'a str> {
        return self.responsibility_uuid.as_deref();
    }
        fn description<'a>(&'a self) -> &'a str {
        return &self.description[..];
    }
        fn props<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, PropertyOrSubtype>> {
        return self.props.as_ref();
    }
        fn links<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, LinkOrSubtype>> {
        return self.links.as_ref();
    }
        fn responsible_roles<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::SspByComponentResponsibleRole>> {
        return self.responsible_roles.as_ref();
    }
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}


pub trait SspSystemCharacteristicsProp : Property   {


}

impl SspSystemCharacteristicsProp for crate::SspSystemCharacteristicsProp {
}


pub trait SspSystemInformationProp : Property   {


}

impl SspSystemInformationProp for crate::SspSystemInformationProp {
}


pub trait SspControlOriginationProp : Property   {


}

impl SspControlOriginationProp for crate::SspControlOriginationProp {
}


pub trait SspAllowsAuthenticatedScanProp : Property   {


}

impl SspAllowsAuthenticatedScanProp for crate::SspAllowsAuthenticatedScanProp {
}


pub trait SspSystemInformationLink : Link   {


}

impl SspSystemInformationLink for crate::SspSystemInformationLink {
}


pub trait SspDiagramLink : Link   {


}

impl SspDiagramLink for crate::SspDiagramLink {
}


pub trait SspLeveragedAuthorizationLink : Link   {


}

impl SspLeveragedAuthorizationLink for crate::SspLeveragedAuthorizationLink {
}


pub trait SspByComponentLink : Link   {


}

impl SspByComponentLink for crate::SspByComponentLink {
}


pub trait SspSystemCharacteristicsResponsibleParty : ResponsibleParty   {


}

impl SspSystemCharacteristicsResponsibleParty for crate::SspSystemCharacteristicsResponsibleParty {
}


pub trait SspImplementedRequirementResponsibleRole : ResponsibleRole   {


}

impl SspImplementedRequirementResponsibleRole for crate::SspImplementedRequirementResponsibleRole {
}


pub trait SspByComponentResponsibleRole : ResponsibleRole   {


}

impl SspByComponentResponsibleRole for crate::SspByComponentResponsibleRole {
}


pub trait SspSystemComponent : SystemComponent   {


}

impl SspSystemComponent for crate::SspSystemComponent {
}


pub trait SspInventoryItem : InventoryItem   {


}

impl SspInventoryItem for crate::SspInventoryItem {
}


pub trait AssessmentResultsDocument : OscalDocument   {

    fn assessment_results<'a>(&'a self) -> &'a crate::AssessmentResults;
    // fn assessment_results_mut(&mut self) -> &mut &'a crate::AssessmentResults;
    // fn set_assessment_results<E>(&mut self, value: E) where E: Into<AssessmentResults>;


}

impl AssessmentResultsDocument for crate::AssessmentResultsDocument {
        fn assessment_results<'a>(&'a self) -> &'a crate::AssessmentResults {
        return &self.assessment_results;
    }
}


pub trait AssessmentResults   {

    fn uuid<'a>(&'a self) -> &'a str;
    // fn uuid_mut(&mut self) -> &mut &'a str;
    // fn set_uuid(&mut self, value: String);

    fn metadata<'a>(&'a self) -> &'a crate::Metadata;
    // fn metadata_mut(&mut self) -> &mut &'a crate::Metadata;
    // fn set_metadata<E>(&mut self, value: E) where E: Into<Metadata>;

    fn import_ap<'a>(&'a self) -> &'a crate::ImportAssessmentPlan;
    // fn import_ap_mut(&mut self) -> &mut &'a crate::ImportAssessmentPlan;
    // fn set_import_ap<E>(&mut self, value: E) where E: Into<ImportAssessmentPlan>;

    fn local_definitions<'a>(&'a self) -> Option<&'a crate::AssessmentResultsLocalDefinitions>;
    // fn local_definitions_mut(&mut self) -> &mut Option<&'a crate::AssessmentResultsLocalDefinitions>;
    // fn set_local_definitions<E>(&mut self, value: Option<E>) where E: Into<AssessmentResultsLocalDefinitions>;

    fn results<'a>(&'a self) -> impl poly_containers::SeqRef<'a, crate::Result>;
    // fn results_mut(&mut self) -> &mut impl poly_containers::SeqRef<'a, crate::Result>;
    // fn set_results<E>(&mut self, value: &Vec<E>) where E: Into<Result>;

    fn back_matter<'a>(&'a self) -> Option<&'a crate::BackMatter>;
    // fn back_matter_mut(&mut self) -> &mut Option<&'a crate::BackMatter>;
    // fn set_back_matter<E>(&mut self, value: Option<E>) where E: Into<BackMatter>;


}

impl AssessmentResults for crate::AssessmentResults {
        fn uuid<'a>(&'a self) -> &'a str {
        return &self.uuid[..];
    }
        fn metadata<'a>(&'a self) -> &'a crate::Metadata {
        return &self.metadata;
    }
        fn import_ap<'a>(&'a self) -> &'a crate::ImportAssessmentPlan {
        return &self.import_ap;
    }
        fn local_definitions<'a>(&'a self) -> Option<&'a crate::AssessmentResultsLocalDefinitions> {
        return self.local_definitions.as_ref();
    }
        fn results<'a>(&'a self) -> impl poly_containers::SeqRef<'a, crate::Result> {
        return &self.results;
    }
        fn back_matter<'a>(&'a self) -> Option<&'a crate::BackMatter> {
        return self.back_matter.as_ref();
    }
}


pub trait ImportAssessmentPlan   {

    fn href<'a>(&'a self) -> &'a str;
    // fn href_mut(&mut self) -> &mut &'a str;
    // fn set_href(&mut self, value: String);

    fn remarks<'a>(&'a self) -> Option<&'a str>;
    // fn remarks_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_remarks(&mut self, value: Option<&'a str>);


}

impl ImportAssessmentPlan for crate::ImportAssessmentPlan {
        fn href<'a>(&'a self) -> &'a str {
        return &self.href[..];
    }
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}


pub trait AssessmentResultsLocalDefinitions   {

    fn objectives_and_methods<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::LocalObjective>>;
    // fn objectives_and_methods_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::LocalObjective>>;
    // fn set_objectives_and_methods<E>(&mut self, value: Option<&Vec<E>>) where E: Into<LocalObjective>;

    fn activities<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Activity>>;
    // fn activities_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::Activity>>;
    // fn set_activities<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Activity>;

    fn remarks<'a>(&'a self) -> Option<&'a str>;
    // fn remarks_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_remarks(&mut self, value: Option<&'a str>);


}

impl AssessmentResultsLocalDefinitions for crate::AssessmentResultsLocalDefinitions {
        fn objectives_and_methods<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::LocalObjective>> {
        return self.objectives_and_methods.as_ref();
    }
        fn activities<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Activity>> {
        return self.activities.as_ref();
    }
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}


pub trait Result : OscalCommon   {

    fn uuid<'a>(&'a self) -> &'a str;
    // fn uuid_mut(&mut self) -> &mut &'a str;
    // fn set_uuid(&mut self, value: String);

    fn title<'a>(&'a self) -> &'a str;
    // fn title_mut(&mut self) -> &mut &'a str;
    // fn set_title(&mut self, value: String);

    fn description<'a>(&'a self) -> &'a str;
    // fn description_mut(&mut self) -> &mut &'a str;
    // fn set_description(&mut self, value: String);

    fn start<'a>(&'a self) -> &'a str;
    // fn start_mut(&mut self) -> &mut &'a str;
    // fn set_start(&mut self, value: String);

    fn end<'a>(&'a self) -> Option<&'a str>;
    // fn end_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_end(&mut self, value: Option<&'a str>);

    fn local_definitions<'a>(&'a self) -> Option<&'a crate::ResultLocalDefinitions>;
    // fn local_definitions_mut(&mut self) -> &mut Option<&'a crate::ResultLocalDefinitions>;
    // fn set_local_definitions<E>(&mut self, value: Option<E>) where E: Into<ResultLocalDefinitions>;

    fn reviewed_controls<'a>(&'a self) -> &'a crate::ReviewedControls;
    // fn reviewed_controls_mut(&mut self) -> &mut &'a crate::ReviewedControls;
    // fn set_reviewed_controls<E>(&mut self, value: E) where E: Into<ReviewedControls>;

    fn attestations<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Attestation>>;
    // fn attestations_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::Attestation>>;
    // fn set_attestations<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Attestation>;

    fn assessment_log<'a>(&'a self) -> Option<&'a crate::AssessmentLog>;
    // fn assessment_log_mut(&mut self) -> &mut Option<&'a crate::AssessmentLog>;
    // fn set_assessment_log<E>(&mut self, value: Option<E>) where E: Into<AssessmentLog>;

    fn observations<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Observation>>;
    // fn observations_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::Observation>>;
    // fn set_observations<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Observation>;

    fn risks<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Risk>>;
    // fn risks_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::Risk>>;
    // fn set_risks<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Risk>;

    fn findings<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Finding>>;
    // fn findings_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::Finding>>;
    // fn set_findings<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Finding>;


}

impl Result for crate::Result {
        fn uuid<'a>(&'a self) -> &'a str {
        return &self.uuid[..];
    }
        fn title<'a>(&'a self) -> &'a str {
        return &self.title[..];
    }
        fn description<'a>(&'a self) -> &'a str {
        return &self.description[..];
    }
        fn start<'a>(&'a self) -> &'a str {
        return &self.start[..];
    }
        fn end<'a>(&'a self) -> Option<&'a str> {
        return self.end.as_deref();
    }
        fn local_definitions<'a>(&'a self) -> Option<&'a crate::ResultLocalDefinitions> {
        return self.local_definitions.as_ref();
    }
        fn reviewed_controls<'a>(&'a self) -> &'a crate::ReviewedControls {
        return &self.reviewed_controls;
    }
        fn attestations<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Attestation>> {
        return self.attestations.as_ref();
    }
        fn assessment_log<'a>(&'a self) -> Option<&'a crate::AssessmentLog> {
        return self.assessment_log.as_ref();
    }
        fn observations<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Observation>> {
        return self.observations.as_ref();
    }
        fn risks<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Risk>> {
        return self.risks.as_ref();
    }
        fn findings<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Finding>> {
        return self.findings.as_ref();
    }
}


pub trait ResultLocalDefinitions   {

    fn components<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, SystemComponentOrSubtype>>;
    // fn components_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, SystemComponentOrSubtype>>;
    // fn set_components<E>(&mut self, value: Option<&Vec<E>>) where E: Into<SystemComponent>;

    fn inventory_items<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, InventoryItemOrSubtype>>;
    // fn inventory_items_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, InventoryItemOrSubtype>>;
    // fn set_inventory_items<E>(&mut self, value: Option<&Vec<E>>) where E: Into<InventoryItem>;

    fn users<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::SystemUser>>;
    // fn users_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::SystemUser>>;
    // fn set_users<E>(&mut self, value: Option<&Vec<E>>) where E: Into<SystemUser>;

    fn assessment_assets<'a>(&'a self) -> Option<&'a crate::AssessmentAssets>;
    // fn assessment_assets_mut(&mut self) -> &mut Option<&'a crate::AssessmentAssets>;
    // fn set_assessment_assets<E>(&mut self, value: Option<E>) where E: Into<AssessmentAssets>;

    fn tasks<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Task>>;
    // fn tasks_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::Task>>;
    // fn set_tasks<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Task>;


}

impl ResultLocalDefinitions for crate::ResultLocalDefinitions {
        fn components<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, SystemComponentOrSubtype>> {
        return self.components.as_ref();
    }
        fn inventory_items<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, InventoryItemOrSubtype>> {
        return self.inventory_items.as_ref();
    }
        fn users<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::SystemUser>> {
        return self.users.as_ref();
    }
        fn assessment_assets<'a>(&'a self) -> Option<&'a crate::AssessmentAssets> {
        return self.assessment_assets.as_ref();
    }
        fn tasks<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Task>> {
        return self.tasks.as_ref();
    }
}


pub trait Attestation : HasResponsibleParties   {

    fn parts<'a>(&'a self) -> impl poly_containers::SeqRef<'a, AssessmentPartOrSubtype>;
    // fn parts_mut(&mut self) -> &mut impl poly_containers::SeqRef<'a, AssessmentPartOrSubtype>;
    // fn set_parts<E>(&mut self, value: &Vec<E>) where E: Into<AssessmentPart>;


}

impl Attestation for crate::Attestation {
        fn parts<'a>(&'a self) -> impl poly_containers::SeqRef<'a, AssessmentPartOrSubtype> {
        return &self.parts;
    }
}


pub trait AssessmentLog   {

    fn entries<'a>(&'a self) -> impl poly_containers::SeqRef<'a, crate::AssessmentLogEntry>;
    // fn entries_mut(&mut self) -> &mut impl poly_containers::SeqRef<'a, crate::AssessmentLogEntry>;
    // fn set_entries<E>(&mut self, value: &Vec<E>) where E: Into<AssessmentLogEntry>;


}

impl AssessmentLog for crate::AssessmentLog {
        fn entries<'a>(&'a self) -> impl poly_containers::SeqRef<'a, crate::AssessmentLogEntry> {
        return &self.entries;
    }
}


pub trait AssessmentLogEntry : OscalCommon   {

    fn uuid<'a>(&'a self) -> &'a str;
    // fn uuid_mut(&mut self) -> &mut &'a str;
    // fn set_uuid(&mut self, value: String);

    fn title<'a>(&'a self) -> Option<&'a str>;
    // fn title_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_title(&mut self, value: Option<&'a str>);

    fn description<'a>(&'a self) -> Option<&'a str>;
    // fn description_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_description(&mut self, value: Option<&'a str>);

    fn start<'a>(&'a self) -> &'a str;
    // fn start_mut(&mut self) -> &mut &'a str;
    // fn set_start(&mut self, value: String);

    fn end<'a>(&'a self) -> Option<&'a str>;
    // fn end_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_end(&mut self, value: Option<&'a str>);

    fn logged_by<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::LoggedBy>>;
    // fn logged_by_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::LoggedBy>>;
    // fn set_logged_by<E>(&mut self, value: Option<&Vec<E>>) where E: Into<LoggedBy>;

    fn related_tasks<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::RelatedTask>>;
    // fn related_tasks_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::RelatedTask>>;
    // fn set_related_tasks<E>(&mut self, value: Option<&Vec<E>>) where E: Into<RelatedTask>;


}

impl AssessmentLogEntry for crate::AssessmentLogEntry {
        fn uuid<'a>(&'a self) -> &'a str {
        return &self.uuid[..];
    }
        fn title<'a>(&'a self) -> Option<&'a str> {
        return self.title.as_deref();
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn start<'a>(&'a self) -> &'a str {
        return &self.start[..];
    }
        fn end<'a>(&'a self) -> Option<&'a str> {
        return self.end.as_deref();
    }
        fn logged_by<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::LoggedBy>> {
        return self.logged_by.as_ref();
    }
        fn related_tasks<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::RelatedTask>> {
        return self.related_tasks.as_ref();
    }
}


pub trait ComponentDefinitionDocument : OscalDocument   {

    fn component_definition<'a>(&'a self) -> &'a crate::ComponentDefinition;
    // fn component_definition_mut(&mut self) -> &mut &'a crate::ComponentDefinition;
    // fn set_component_definition<E>(&mut self, value: E) where E: Into<ComponentDefinition>;


}

impl ComponentDefinitionDocument for crate::ComponentDefinitionDocument {
        fn component_definition<'a>(&'a self) -> &'a crate::ComponentDefinition {
        return &self.component_definition;
    }
}


pub trait ComponentDefinition   {

    fn uuid<'a>(&'a self) -> &'a str;
    // fn uuid_mut(&mut self) -> &mut &'a str;
    // fn set_uuid(&mut self, value: String);

    fn metadata<'a>(&'a self) -> &'a crate::Metadata;
    // fn metadata_mut(&mut self) -> &mut &'a crate::Metadata;
    // fn set_metadata<E>(&mut self, value: E) where E: Into<Metadata>;

    fn import_component_definitions<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::ImportComponentDefinition>>;
    // fn import_component_definitions_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::ImportComponentDefinition>>;
    // fn set_import_component_definitions<E>(&mut self, value: Option<&Vec<E>>) where E: Into<ImportComponentDefinition>;

    fn components<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::DefinedComponent>>;
    // fn components_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::DefinedComponent>>;
    // fn set_components<E>(&mut self, value: Option<&Vec<E>>) where E: Into<DefinedComponent>;

    fn capabilities<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Capability>>;
    // fn capabilities_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::Capability>>;
    // fn set_capabilities<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Capability>;

    fn back_matter<'a>(&'a self) -> Option<&'a crate::BackMatter>;
    // fn back_matter_mut(&mut self) -> &mut Option<&'a crate::BackMatter>;
    // fn set_back_matter<E>(&mut self, value: Option<E>) where E: Into<BackMatter>;


}

impl ComponentDefinition for crate::ComponentDefinition {
        fn uuid<'a>(&'a self) -> &'a str {
        return &self.uuid[..];
    }
        fn metadata<'a>(&'a self) -> &'a crate::Metadata {
        return &self.metadata;
    }
        fn import_component_definitions<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::ImportComponentDefinition>> {
        return self.import_component_definitions.as_ref();
    }
        fn components<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::DefinedComponent>> {
        return self.components.as_ref();
    }
        fn capabilities<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Capability>> {
        return self.capabilities.as_ref();
    }
        fn back_matter<'a>(&'a self) -> Option<&'a crate::BackMatter> {
        return self.back_matter.as_ref();
    }
}


pub trait ImportComponentDefinition   {

    fn href<'a>(&'a self) -> &'a str;
    // fn href_mut(&mut self) -> &mut &'a str;
    // fn set_href(&mut self, value: String);

    fn remarks<'a>(&'a self) -> Option<&'a str>;
    // fn remarks_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_remarks(&mut self, value: Option<&'a str>);


}

impl ImportComponentDefinition for crate::ImportComponentDefinition {
        fn href<'a>(&'a self) -> &'a str {
        return &self.href[..];
    }
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}


pub trait DefinedComponent : OscalCommon  +  HasResponsibleRoles   {

    fn uuid<'a>(&'a self) -> &'a str;
    // fn uuid_mut(&mut self) -> &mut &'a str;
    // fn set_uuid(&mut self, value: String);

    fn type_<'a>(&'a self) -> &'a str;
    // fn type__mut(&mut self) -> &mut &'a str;
    // fn set_type_(&mut self, value: String);

    fn title<'a>(&'a self) -> &'a str;
    // fn title_mut(&mut self) -> &mut &'a str;
    // fn set_title(&mut self, value: String);

    fn description<'a>(&'a self) -> &'a str;
    // fn description_mut(&mut self) -> &mut &'a str;
    // fn set_description(&mut self, value: String);

    fn purpose<'a>(&'a self) -> Option<&'a str>;
    // fn purpose_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_purpose(&mut self, value: Option<&'a str>);

    fn protocols<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Protocol>>;
    // fn protocols_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::Protocol>>;
    // fn set_protocols<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Protocol>;

    fn control_implementations<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::ControlImplementationSet>>;
    // fn control_implementations_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::ControlImplementationSet>>;
    // fn set_control_implementations<E>(&mut self, value: Option<&Vec<E>>) where E: Into<ControlImplementationSet>;


}

impl DefinedComponent for crate::DefinedComponent {
        fn uuid<'a>(&'a self) -> &'a str {
        return &self.uuid[..];
    }
        fn type_<'a>(&'a self) -> &'a str {
        return &self.type_[..];
    }
        fn title<'a>(&'a self) -> &'a str {
        return &self.title[..];
    }
        fn description<'a>(&'a self) -> &'a str {
        return &self.description[..];
    }
        fn purpose<'a>(&'a self) -> Option<&'a str> {
        return self.purpose.as_deref();
    }
        fn protocols<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Protocol>> {
        return self.protocols.as_ref();
    }
        fn control_implementations<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::ControlImplementationSet>> {
        return self.control_implementations.as_ref();
    }
}


pub trait Capability : OscalCommon   {

    fn uuid<'a>(&'a self) -> &'a str;
    // fn uuid_mut(&mut self) -> &mut &'a str;
    // fn set_uuid(&mut self, value: String);

    fn name<'a>(&'a self) -> &'a str;
    // fn name_mut(&mut self) -> &mut &'a str;
    // fn set_name(&mut self, value: String);

    fn description<'a>(&'a self) -> &'a str;
    // fn description_mut(&mut self) -> &mut &'a str;
    // fn set_description(&mut self, value: String);

    fn incorporates_components<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::IncorporatesComponent>>;
    // fn incorporates_components_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::IncorporatesComponent>>;
    // fn set_incorporates_components<E>(&mut self, value: Option<&Vec<E>>) where E: Into<IncorporatesComponent>;

    fn control_implementations<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::ControlImplementationSet>>;
    // fn control_implementations_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::ControlImplementationSet>>;
    // fn set_control_implementations<E>(&mut self, value: Option<&Vec<E>>) where E: Into<ControlImplementationSet>;


}

impl Capability for crate::Capability {
        fn uuid<'a>(&'a self) -> &'a str {
        return &self.uuid[..];
    }
        fn name<'a>(&'a self) -> &'a str {
        return &self.name[..];
    }
        fn description<'a>(&'a self) -> &'a str {
        return &self.description[..];
    }
        fn incorporates_components<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::IncorporatesComponent>> {
        return self.incorporates_components.as_ref();
    }
        fn control_implementations<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::ControlImplementationSet>> {
        return self.control_implementations.as_ref();
    }
}


pub trait IncorporatesComponent   {

    fn component_uuid<'a>(&'a self) -> &'a str;
    // fn component_uuid_mut(&mut self) -> &mut &'a str;
    // fn set_component_uuid(&mut self, value: String);

    fn description<'a>(&'a self) -> &'a str;
    // fn description_mut(&mut self) -> &mut &'a str;
    // fn set_description(&mut self, value: String);


}

impl IncorporatesComponent for crate::IncorporatesComponent {
        fn component_uuid<'a>(&'a self) -> &'a str {
        return &self.component_uuid[..];
    }
        fn description<'a>(&'a self) -> &'a str {
        return &self.description[..];
    }
}


pub trait ControlImplementationSet : HasPropsAndLinks   {

    fn uuid<'a>(&'a self) -> &'a str;
    // fn uuid_mut(&mut self) -> &mut &'a str;
    // fn set_uuid(&mut self, value: String);

    fn source<'a>(&'a self) -> &'a str;
    // fn source_mut(&mut self) -> &mut &'a str;
    // fn set_source(&mut self, value: String);

    fn description<'a>(&'a self) -> &'a str;
    // fn description_mut(&mut self) -> &mut &'a str;
    // fn set_description(&mut self, value: String);

    fn set_parameters<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::SetParameter>>;
    // fn set_parameters_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::SetParameter>>;
    // fn set_set_parameters<E>(&mut self, value: Option<&Vec<E>>) where E: Into<SetParameter>;

    fn implemented_requirements<'a>(&'a self) -> impl poly_containers::SeqRef<'a, crate::ImplementedRequirement>;
    // fn implemented_requirements_mut(&mut self) -> &mut impl poly_containers::SeqRef<'a, crate::ImplementedRequirement>;
    // fn set_implemented_requirements<E>(&mut self, value: &Vec<E>) where E: Into<ImplementedRequirement>;


}

impl ControlImplementationSet for crate::ControlImplementationSet {
        fn uuid<'a>(&'a self) -> &'a str {
        return &self.uuid[..];
    }
        fn source<'a>(&'a self) -> &'a str {
        return &self.source[..];
    }
        fn description<'a>(&'a self) -> &'a str {
        return &self.description[..];
    }
        fn set_parameters<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::SetParameter>> {
        return self.set_parameters.as_ref();
    }
        fn implemented_requirements<'a>(&'a self) -> impl poly_containers::SeqRef<'a, crate::ImplementedRequirement> {
        return &self.implemented_requirements;
    }
}


pub trait ImplementedRequirement : HasPropsAndLinks  +  HasResponsibleRoles   {

    fn uuid<'a>(&'a self) -> &'a str;
    // fn uuid_mut(&mut self) -> &mut &'a str;
    // fn set_uuid(&mut self, value: String);

    fn control_id<'a>(&'a self) -> &'a str;
    // fn control_id_mut(&mut self) -> &mut &'a str;
    // fn set_control_id(&mut self, value: String);

    fn description<'a>(&'a self) -> &'a str;
    // fn description_mut(&mut self) -> &mut &'a str;
    // fn set_description(&mut self, value: String);

    fn set_parameters<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::SetParameter>>;
    // fn set_parameters_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::SetParameter>>;
    // fn set_set_parameters<E>(&mut self, value: Option<&Vec<E>>) where E: Into<SetParameter>;

    fn statements<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::ImplementedControlStatement>>;
    // fn statements_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::ImplementedControlStatement>>;
    // fn set_statements<E>(&mut self, value: Option<&Vec<E>>) where E: Into<ImplementedControlStatement>;

    fn remarks<'a>(&'a self) -> Option<&'a str>;
    // fn remarks_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_remarks(&mut self, value: Option<&'a str>);


}

impl ImplementedRequirement for crate::ImplementedRequirement {
        fn uuid<'a>(&'a self) -> &'a str {
        return &self.uuid[..];
    }
        fn control_id<'a>(&'a self) -> &'a str {
        return &self.control_id[..];
    }
        fn description<'a>(&'a self) -> &'a str {
        return &self.description[..];
    }
        fn set_parameters<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::SetParameter>> {
        return self.set_parameters.as_ref();
    }
        fn statements<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::ImplementedControlStatement>> {
        return self.statements.as_ref();
    }
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}


pub trait ImplementedControlStatement : HasPropsAndLinks  +  HasResponsibleRoles   {

    fn statement_id<'a>(&'a self) -> &'a str;
    // fn statement_id_mut(&mut self) -> &mut &'a str;
    // fn set_statement_id(&mut self, value: String);

    fn uuid<'a>(&'a self) -> &'a str;
    // fn uuid_mut(&mut self) -> &mut &'a str;
    // fn set_uuid(&mut self, value: String);

    fn description<'a>(&'a self) -> &'a str;
    // fn description_mut(&mut self) -> &mut &'a str;
    // fn set_description(&mut self, value: String);

    fn remarks<'a>(&'a self) -> Option<&'a str>;
    // fn remarks_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_remarks(&mut self, value: Option<&'a str>);


}

impl ImplementedControlStatement for crate::ImplementedControlStatement {
        fn statement_id<'a>(&'a self) -> &'a str {
        return &self.statement_id[..];
    }
        fn uuid<'a>(&'a self) -> &'a str {
        return &self.uuid[..];
    }
        fn description<'a>(&'a self) -> &'a str {
        return &self.description[..];
    }
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}


pub trait MappingCollectionDocument : OscalDocument   {

    fn mapping_collection<'a>(&'a self) -> &'a crate::MappingCollection;
    // fn mapping_collection_mut(&mut self) -> &mut &'a crate::MappingCollection;
    // fn set_mapping_collection<E>(&mut self, value: E) where E: Into<MappingCollection>;


}

impl MappingCollectionDocument for crate::MappingCollectionDocument {
        fn mapping_collection<'a>(&'a self) -> &'a crate::MappingCollection {
        return &self.mapping_collection;
    }
}


pub trait MappingCollection   {

    fn uuid<'a>(&'a self) -> &'a str;
    // fn uuid_mut(&mut self) -> &mut &'a str;
    // fn set_uuid(&mut self, value: String);

    fn metadata<'a>(&'a self) -> &'a crate::Metadata;
    // fn metadata_mut(&mut self) -> &mut &'a crate::Metadata;
    // fn set_metadata<E>(&mut self, value: E) where E: Into<Metadata>;

    fn provenance<'a>(&'a self) -> &'a crate::MappingProvenance;
    // fn provenance_mut(&mut self) -> &mut &'a crate::MappingProvenance;
    // fn set_provenance<E>(&mut self, value: E) where E: Into<MappingProvenance>;

    fn mappings<'a>(&'a self) -> impl poly_containers::SeqRef<'a, crate::Mapping>;
    // fn mappings_mut(&mut self) -> &mut impl poly_containers::SeqRef<'a, crate::Mapping>;
    // fn set_mappings<E>(&mut self, value: &Vec<E>) where E: Into<Mapping>;

    fn back_matter<'a>(&'a self) -> Option<&'a crate::BackMatter>;
    // fn back_matter_mut(&mut self) -> &mut Option<&'a crate::BackMatter>;
    // fn set_back_matter<E>(&mut self, value: Option<E>) where E: Into<BackMatter>;


}

impl MappingCollection for crate::MappingCollection {
        fn uuid<'a>(&'a self) -> &'a str {
        return &self.uuid[..];
    }
        fn metadata<'a>(&'a self) -> &'a crate::Metadata {
        return &self.metadata;
    }
        fn provenance<'a>(&'a self) -> &'a crate::MappingProvenance {
        return &self.provenance;
    }
        fn mappings<'a>(&'a self) -> impl poly_containers::SeqRef<'a, crate::Mapping> {
        return &self.mappings;
    }
        fn back_matter<'a>(&'a self) -> Option<&'a crate::BackMatter> {
        return self.back_matter.as_ref();
    }
}


pub trait MappingProvenance : OscalCommon  +  HasResponsibleParties   {

    fn method<'a>(&'a self) -> &'a crate::MappingMethodEnum;
    // fn method_mut(&mut self) -> &mut &'a crate::MappingMethodEnum;
    // fn set_method(&mut self, value: MappingMethodEnum);

    fn matching_rationale<'a>(&'a self) -> &'a crate::MatchingRationaleEnum;
    // fn matching_rationale_mut(&mut self) -> &mut &'a crate::MatchingRationaleEnum;
    // fn set_matching_rationale(&mut self, value: MatchingRationaleEnum);

    fn status<'a>(&'a self) -> &'a crate::MappingStatusEnum;
    // fn status_mut(&mut self) -> &mut &'a crate::MappingStatusEnum;
    // fn set_status(&mut self, value: MappingStatusEnum);

    fn confidence_score<'a>(&'a self) -> Option<&'a crate::ConfidenceScore>;
    // fn confidence_score_mut(&mut self) -> &mut Option<&'a crate::ConfidenceScore>;
    // fn set_confidence_score<E>(&mut self, value: Option<E>) where E: Into<ConfidenceScore>;

    fn coverage<'a>(&'a self) -> Option<&'a crate::Coverage>;
    // fn coverage_mut(&mut self) -> &mut Option<&'a crate::Coverage>;
    // fn set_coverage<E>(&mut self, value: Option<E>) where E: Into<Coverage>;

    fn mapping_description<'a>(&'a self) -> &'a str;
    // fn mapping_description_mut(&mut self) -> &mut &'a str;
    // fn set_mapping_description(&mut self, value: String);


}

impl MappingProvenance for crate::MappingProvenance {
        fn method<'a>(&'a self) -> &'a crate::MappingMethodEnum {
        return &self.method;
    }
        fn matching_rationale<'a>(&'a self) -> &'a crate::MatchingRationaleEnum {
        return &self.matching_rationale;
    }
        fn status<'a>(&'a self) -> &'a crate::MappingStatusEnum {
        return &self.status;
    }
        fn confidence_score<'a>(&'a self) -> Option<&'a crate::ConfidenceScore> {
        return self.confidence_score.as_ref();
    }
        fn coverage<'a>(&'a self) -> Option<&'a crate::Coverage> {
        return self.coverage.as_ref();
    }
        fn mapping_description<'a>(&'a self) -> &'a str {
        return &self.mapping_description[..];
    }
}


pub trait Mapping : OscalCommon   {

    fn uuid<'a>(&'a self) -> &'a str;
    // fn uuid_mut(&mut self) -> &mut &'a str;
    // fn set_uuid(&mut self, value: String);

    fn method<'a>(&'a self) -> Option<&'a crate::MappingMethodEnum>;
    // fn method_mut(&mut self) -> &mut Option<&'a crate::MappingMethodEnum>;
    // fn set_method(&mut self, value: Option<&'a MappingMethodEnum>);

    fn matching_rationale<'a>(&'a self) -> Option<&'a crate::MatchingRationaleEnum>;
    // fn matching_rationale_mut(&mut self) -> &mut Option<&'a crate::MatchingRationaleEnum>;
    // fn set_matching_rationale(&mut self, value: Option<&'a MatchingRationaleEnum>);

    fn status<'a>(&'a self) -> Option<&'a crate::MappingStatusEnum>;
    // fn status_mut(&mut self) -> &mut Option<&'a crate::MappingStatusEnum>;
    // fn set_status(&mut self, value: Option<&'a MappingStatusEnum>);

    fn source_resource<'a>(&'a self) -> &'a crate::MappingResourceReference;
    // fn source_resource_mut(&mut self) -> &mut &'a crate::MappingResourceReference;
    // fn set_source_resource<E>(&mut self, value: E) where E: Into<MappingResourceReference>;

    fn target_resource<'a>(&'a self) -> &'a crate::MappingResourceReference;
    // fn target_resource_mut(&mut self) -> &mut &'a crate::MappingResourceReference;
    // fn set_target_resource<E>(&mut self, value: E) where E: Into<MappingResourceReference>;

    fn maps<'a>(&'a self) -> impl poly_containers::SeqRef<'a, crate::Map>;
    // fn maps_mut(&mut self) -> &mut impl poly_containers::SeqRef<'a, crate::Map>;
    // fn set_maps<E>(&mut self, value: &Vec<E>) where E: Into<Map>;

    fn mapping_description<'a>(&'a self) -> Option<&'a str>;
    // fn mapping_description_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_mapping_description(&mut self, value: Option<&'a str>);

    fn source_gap_summary<'a>(&'a self) -> Option<&'a crate::GapSummary>;
    // fn source_gap_summary_mut(&mut self) -> &mut Option<&'a crate::GapSummary>;
    // fn set_source_gap_summary<E>(&mut self, value: Option<E>) where E: Into<GapSummary>;

    fn target_gap_summary<'a>(&'a self) -> Option<&'a crate::GapSummary>;
    // fn target_gap_summary_mut(&mut self) -> &mut Option<&'a crate::GapSummary>;
    // fn set_target_gap_summary<E>(&mut self, value: Option<E>) where E: Into<GapSummary>;

    fn confidence_score<'a>(&'a self) -> Option<&'a crate::ConfidenceScore>;
    // fn confidence_score_mut(&mut self) -> &mut Option<&'a crate::ConfidenceScore>;
    // fn set_confidence_score<E>(&mut self, value: Option<E>) where E: Into<ConfidenceScore>;

    fn coverage<'a>(&'a self) -> Option<&'a crate::Coverage>;
    // fn coverage_mut(&mut self) -> &mut Option<&'a crate::Coverage>;
    // fn set_coverage<E>(&mut self, value: Option<E>) where E: Into<Coverage>;


}

impl Mapping for crate::Mapping {
        fn uuid<'a>(&'a self) -> &'a str {
        return &self.uuid[..];
    }
        fn method<'a>(&'a self) -> Option<&'a crate::MappingMethodEnum> {
        return self.method.as_ref();
    }
        fn matching_rationale<'a>(&'a self) -> Option<&'a crate::MatchingRationaleEnum> {
        return self.matching_rationale.as_ref();
    }
        fn status<'a>(&'a self) -> Option<&'a crate::MappingStatusEnum> {
        return self.status.as_ref();
    }
        fn source_resource<'a>(&'a self) -> &'a crate::MappingResourceReference {
        return &self.source_resource;
    }
        fn target_resource<'a>(&'a self) -> &'a crate::MappingResourceReference {
        return &self.target_resource;
    }
        fn maps<'a>(&'a self) -> impl poly_containers::SeqRef<'a, crate::Map> {
        return &self.maps;
    }
        fn mapping_description<'a>(&'a self) -> Option<&'a str> {
        return self.mapping_description.as_deref();
    }
        fn source_gap_summary<'a>(&'a self) -> Option<&'a crate::GapSummary> {
        return self.source_gap_summary.as_ref();
    }
        fn target_gap_summary<'a>(&'a self) -> Option<&'a crate::GapSummary> {
        return self.target_gap_summary.as_ref();
    }
        fn confidence_score<'a>(&'a self) -> Option<&'a crate::ConfidenceScore> {
        return self.confidence_score.as_ref();
    }
        fn coverage<'a>(&'a self) -> Option<&'a crate::Coverage> {
        return self.coverage.as_ref();
    }
}


pub trait Map : OscalCommon   {

    fn uuid<'a>(&'a self) -> &'a str;
    // fn uuid_mut(&mut self) -> &mut &'a str;
    // fn set_uuid(&mut self, value: String);

    fn ns<'a>(&'a self) -> Option<&'a str>;
    // fn ns_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_ns(&mut self, value: Option<&'a str>);

    fn matching_rationale<'a>(&'a self) -> Option<&'a crate::MatchingRationaleEnum>;
    // fn matching_rationale_mut(&mut self) -> &mut Option<&'a crate::MatchingRationaleEnum>;
    // fn set_matching_rationale(&mut self, value: Option<&'a MatchingRationaleEnum>);

    fn relationship(&self) -> map_utl::relationship_range;
    // fn relationship_mut(&mut self) -> &mut map_utl::relationship_range;
    // fn set_relationship(&mut self, value: map_utl::relationship_range);

    fn sources<'a>(&'a self) -> impl poly_containers::SeqRef<'a, crate::MappingItem>;
    // fn sources_mut(&mut self) -> &mut impl poly_containers::SeqRef<'a, crate::MappingItem>;
    // fn set_sources<E>(&mut self, value: &Vec<E>) where E: Into<MappingItem>;

    fn targets<'a>(&'a self) -> impl poly_containers::SeqRef<'a, crate::MappingItem>;
    // fn targets_mut(&mut self) -> &mut impl poly_containers::SeqRef<'a, crate::MappingItem>;
    // fn set_targets<E>(&mut self, value: &Vec<E>) where E: Into<MappingItem>;

    fn qualifiers<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::QualifierItem>>;
    // fn qualifiers_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::QualifierItem>>;
    // fn set_qualifiers<E>(&mut self, value: Option<&Vec<E>>) where E: Into<QualifierItem>;

    fn confidence_score<'a>(&'a self) -> Option<&'a crate::ConfidenceScore>;
    // fn confidence_score_mut(&mut self) -> &mut Option<&'a crate::ConfidenceScore>;
    // fn set_confidence_score<E>(&mut self, value: Option<E>) where E: Into<ConfidenceScore>;

    fn coverage<'a>(&'a self) -> Option<&'a crate::Coverage>;
    // fn coverage_mut(&mut self) -> &mut Option<&'a crate::Coverage>;
    // fn set_coverage<E>(&mut self, value: Option<E>) where E: Into<Coverage>;


}

impl Map for crate::Map {
        fn uuid<'a>(&'a self) -> &'a str {
        return &self.uuid[..];
    }
        fn ns<'a>(&'a self) -> Option<&'a str> {
        return self.ns.as_deref();
    }
        fn matching_rationale<'a>(&'a self) -> Option<&'a crate::MatchingRationaleEnum> {
        return self.matching_rationale.as_ref();
    }
        fn relationship(&self) -> map_utl::relationship_range {
            self.relationship.clone()
    }
        fn sources<'a>(&'a self) -> impl poly_containers::SeqRef<'a, crate::MappingItem> {
        return &self.sources;
    }
        fn targets<'a>(&'a self) -> impl poly_containers::SeqRef<'a, crate::MappingItem> {
        return &self.targets;
    }
        fn qualifiers<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::QualifierItem>> {
        return self.qualifiers.as_ref();
    }
        fn confidence_score<'a>(&'a self) -> Option<&'a crate::ConfidenceScore> {
        return self.confidence_score.as_ref();
    }
        fn coverage<'a>(&'a self) -> Option<&'a crate::Coverage> {
        return self.coverage.as_ref();
    }
}


pub trait MappingItem : OscalCommon   {

    fn type_<'a>(&'a self) -> &'a crate::MappingSubjectTypeEnum;
    // fn type__mut(&mut self) -> &mut &'a crate::MappingSubjectTypeEnum;
    // fn set_type_(&mut self, value: MappingSubjectTypeEnum);

    fn id_ref<'a>(&'a self) -> &'a str;
    // fn id_ref_mut(&mut self) -> &mut &'a str;
    // fn set_id_ref(&mut self, value: String);


}

impl MappingItem for crate::MappingItem {
        fn type_<'a>(&'a self) -> &'a crate::MappingSubjectTypeEnum {
        return &self.type_;
    }
        fn id_ref<'a>(&'a self) -> &'a str {
        return &self.id_ref[..];
    }
}


pub trait MappingResourceReference : OscalCommon   {

    fn ns<'a>(&'a self) -> Option<&'a str>;
    // fn ns_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_ns(&mut self, value: Option<&'a str>);

    fn type_(&self) -> mapping_resource_reference_utl::type__range;
    // fn type__mut(&mut self) -> &mut mapping_resource_reference_utl::type__range;
    // fn set_type_(&mut self, value: mapping_resource_reference_utl::type__range);

    fn href<'a>(&'a self) -> &'a str;
    // fn href_mut(&mut self) -> &mut &'a str;
    // fn set_href(&mut self, value: String);


}

impl MappingResourceReference for crate::MappingResourceReference {
        fn ns<'a>(&'a self) -> Option<&'a str> {
        return self.ns.as_deref();
    }
        fn type_(&self) -> mapping_resource_reference_utl::type__range {
            self.type_.clone()
    }
        fn href<'a>(&'a self) -> &'a str {
        return &self.href[..];
    }
}


pub trait QualifierItem   {

    fn subject<'a>(&'a self) -> &'a crate::QualifierSubjectEnum;
    // fn subject_mut(&mut self) -> &mut &'a crate::QualifierSubjectEnum;
    // fn set_subject(&mut self, value: QualifierSubjectEnum);

    fn predicate<'a>(&'a self) -> &'a crate::QualifierPredicateEnum;
    // fn predicate_mut(&mut self) -> &mut &'a crate::QualifierPredicateEnum;
    // fn set_predicate(&mut self, value: QualifierPredicateEnum);

    fn category<'a>(&'a self) -> &'a crate::QualifierCategoryEnum;
    // fn category_mut(&mut self) -> &mut &'a crate::QualifierCategoryEnum;
    // fn set_category(&mut self, value: QualifierCategoryEnum);

    fn description<'a>(&'a self) -> &'a str;
    // fn description_mut(&mut self) -> &mut &'a str;
    // fn set_description(&mut self, value: String);

    fn remarks<'a>(&'a self) -> Option<&'a str>;
    // fn remarks_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_remarks(&mut self, value: Option<&'a str>);


}

impl QualifierItem for crate::QualifierItem {
        fn subject<'a>(&'a self) -> &'a crate::QualifierSubjectEnum {
        return &self.subject;
    }
        fn predicate<'a>(&'a self) -> &'a crate::QualifierPredicateEnum {
        return &self.predicate;
    }
        fn category<'a>(&'a self) -> &'a crate::QualifierCategoryEnum {
        return &self.category;
    }
        fn description<'a>(&'a self) -> &'a str {
        return &self.description[..];
    }
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}


pub trait GapSummary   {

    fn uuid<'a>(&'a self) -> &'a str;
    // fn uuid_mut(&mut self) -> &mut &'a str;
    // fn set_uuid(&mut self, value: String);

    fn unmapped_controls<'a>(&'a self) -> impl poly_containers::SeqRef<'a, crate::SelectControlById>;
    // fn unmapped_controls_mut(&mut self) -> &mut impl poly_containers::SeqRef<'a, crate::SelectControlById>;
    // fn set_unmapped_controls<E>(&mut self, value: &Vec<E>) where E: Into<SelectControlById>;


}

impl GapSummary for crate::GapSummary {
        fn uuid<'a>(&'a self) -> &'a str {
        return &self.uuid[..];
    }
        fn unmapped_controls<'a>(&'a self) -> impl poly_containers::SeqRef<'a, crate::SelectControlById> {
        return &self.unmapped_controls;
    }
}


pub trait ConfidenceScore   {

    fn category(&self) -> Option<confidence_score_utl::category_range>;
    // fn category_mut(&mut self) -> &mut Option<confidence_score_utl::category_range>;
    // fn set_category(&mut self, value: Option<&'a confidence_score_utl::category_range>);

    fn percentage(&self) -> Option<f64>;
    // fn percentage_mut(&mut self) -> &mut Option<f64>;
    // fn set_percentage(&mut self, value: Option<f64>);


}

impl ConfidenceScore for crate::ConfidenceScore {
        fn category(&self) -> Option<confidence_score_utl::category_range> {
                self.category.as_ref().cloned()
    }
        fn percentage(&self) -> Option<f64> {
        return self.percentage;
    }
}


pub trait Coverage   {

    fn generation_method(&self) -> Option<coverage_utl::generation_method_range>;
    // fn generation_method_mut(&mut self) -> &mut Option<coverage_utl::generation_method_range>;
    // fn set_generation_method(&mut self, value: Option<&'a coverage_utl::generation_method_range>);

    fn target_coverage(&self) -> f64;
    // fn target_coverage_mut(&mut self) -> &mut f64;
    // fn set_target_coverage(&mut self, value: f64);


}

impl Coverage for crate::Coverage {
        fn generation_method(&self) -> Option<coverage_utl::generation_method_range> {
                self.generation_method.as_ref().cloned()
    }
        fn target_coverage(&self) -> f64 {
        return self.target_coverage;
    }
}


pub trait PoamDocument : OscalDocument   {

    fn plan_of_action_and_milestones<'a>(&'a self) -> &'a crate::PlanOfActionAndMilestones;
    // fn plan_of_action_and_milestones_mut(&mut self) -> &mut &'a crate::PlanOfActionAndMilestones;
    // fn set_plan_of_action_and_milestones<E>(&mut self, value: E) where E: Into<PlanOfActionAndMilestones>;


}

impl PoamDocument for crate::PoamDocument {
        fn plan_of_action_and_milestones<'a>(&'a self) -> &'a crate::PlanOfActionAndMilestones {
        return &self.plan_of_action_and_milestones;
    }
}


pub trait PlanOfActionAndMilestones   {

    fn uuid<'a>(&'a self) -> &'a str;
    // fn uuid_mut(&mut self) -> &mut &'a str;
    // fn set_uuid(&mut self, value: String);

    fn metadata<'a>(&'a self) -> &'a crate::Metadata;
    // fn metadata_mut(&mut self) -> &mut &'a crate::Metadata;
    // fn set_metadata<E>(&mut self, value: E) where E: Into<Metadata>;

    fn import_ssp<'a>(&'a self) -> Option<&'a crate::ImportSSP>;
    // fn import_ssp_mut(&mut self) -> &mut Option<&'a crate::ImportSSP>;
    // fn set_import_ssp<E>(&mut self, value: Option<E>) where E: Into<ImportSSP>;

    fn system_id<'a>(&'a self) -> Option<&'a crate::SystemId>;
    // fn system_id_mut(&mut self) -> &mut Option<&'a crate::SystemId>;
    // fn set_system_id<E>(&mut self, value: Option<E>) where E: Into<SystemId>;

    fn local_definitions<'a>(&'a self) -> Option<&'a crate::PoamLocalDefinitions>;
    // fn local_definitions_mut(&mut self) -> &mut Option<&'a crate::PoamLocalDefinitions>;
    // fn set_local_definitions<E>(&mut self, value: Option<E>) where E: Into<PoamLocalDefinitions>;

    fn observations<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Observation>>;
    // fn observations_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::Observation>>;
    // fn set_observations<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Observation>;

    fn risks<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Risk>>;
    // fn risks_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::Risk>>;
    // fn set_risks<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Risk>;

    fn findings<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Finding>>;
    // fn findings_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::Finding>>;
    // fn set_findings<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Finding>;

    fn poam_items<'a>(&'a self) -> impl poly_containers::SeqRef<'a, crate::PoamItem>;
    // fn poam_items_mut(&mut self) -> &mut impl poly_containers::SeqRef<'a, crate::PoamItem>;
    // fn set_poam_items<E>(&mut self, value: &Vec<E>) where E: Into<PoamItem>;

    fn back_matter<'a>(&'a self) -> Option<&'a crate::BackMatter>;
    // fn back_matter_mut(&mut self) -> &mut Option<&'a crate::BackMatter>;
    // fn set_back_matter<E>(&mut self, value: Option<E>) where E: Into<BackMatter>;


}

impl PlanOfActionAndMilestones for crate::PlanOfActionAndMilestones {
        fn uuid<'a>(&'a self) -> &'a str {
        return &self.uuid[..];
    }
        fn metadata<'a>(&'a self) -> &'a crate::Metadata {
        return &self.metadata;
    }
        fn import_ssp<'a>(&'a self) -> Option<&'a crate::ImportSSP> {
        return self.import_ssp.as_ref();
    }
        fn system_id<'a>(&'a self) -> Option<&'a crate::SystemId> {
        return self.system_id.as_ref();
    }
        fn local_definitions<'a>(&'a self) -> Option<&'a crate::PoamLocalDefinitions> {
        return self.local_definitions.as_ref();
    }
        fn observations<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Observation>> {
        return self.observations.as_ref();
    }
        fn risks<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Risk>> {
        return self.risks.as_ref();
    }
        fn findings<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Finding>> {
        return self.findings.as_ref();
    }
        fn poam_items<'a>(&'a self) -> impl poly_containers::SeqRef<'a, crate::PoamItem> {
        return &self.poam_items;
    }
        fn back_matter<'a>(&'a self) -> Option<&'a crate::BackMatter> {
        return self.back_matter.as_ref();
    }
}


pub trait PoamLocalDefinitions   {

    fn components<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, SystemComponentOrSubtype>>;
    // fn components_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, SystemComponentOrSubtype>>;
    // fn set_components<E>(&mut self, value: Option<&Vec<E>>) where E: Into<SystemComponent>;

    fn inventory_items<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, InventoryItemOrSubtype>>;
    // fn inventory_items_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, InventoryItemOrSubtype>>;
    // fn set_inventory_items<E>(&mut self, value: Option<&Vec<E>>) where E: Into<InventoryItem>;

    fn assessment_assets<'a>(&'a self) -> Option<&'a crate::AssessmentAssets>;
    // fn assessment_assets_mut(&mut self) -> &mut Option<&'a crate::AssessmentAssets>;
    // fn set_assessment_assets<E>(&mut self, value: Option<E>) where E: Into<AssessmentAssets>;

    fn remarks<'a>(&'a self) -> Option<&'a str>;
    // fn remarks_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_remarks(&mut self, value: Option<&'a str>);


}

impl PoamLocalDefinitions for crate::PoamLocalDefinitions {
        fn components<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, SystemComponentOrSubtype>> {
        return self.components.as_ref();
    }
        fn inventory_items<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, InventoryItemOrSubtype>> {
        return self.inventory_items.as_ref();
    }
        fn assessment_assets<'a>(&'a self) -> Option<&'a crate::AssessmentAssets> {
        return self.assessment_assets.as_ref();
    }
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}


pub trait PoamItem : OscalCommon   {

    fn uuid<'a>(&'a self) -> Option<&'a str>;
    // fn uuid_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_uuid(&mut self, value: Option<&'a str>);

    fn title<'a>(&'a self) -> &'a str;
    // fn title_mut(&mut self) -> &mut &'a str;
    // fn set_title(&mut self, value: String);

    fn description<'a>(&'a self) -> &'a str;
    // fn description_mut(&mut self) -> &mut &'a str;
    // fn set_description(&mut self, value: String);

    fn origins<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Origin>>;
    // fn origins_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::Origin>>;
    // fn set_origins<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Origin>;

    fn related_findings<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::RelatedFinding>>;
    // fn related_findings_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::RelatedFinding>>;
    // fn set_related_findings<E>(&mut self, value: Option<&Vec<E>>) where E: Into<RelatedFinding>;

    fn related_observations<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::RelatedObservation>>;
    // fn related_observations_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::RelatedObservation>>;
    // fn set_related_observations<E>(&mut self, value: Option<&Vec<E>>) where E: Into<RelatedObservation>;

    fn related_risks<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::AssociatedRisk>>;
    // fn related_risks_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::AssociatedRisk>>;
    // fn set_related_risks<E>(&mut self, value: Option<&Vec<E>>) where E: Into<AssociatedRisk>;


}

impl PoamItem for crate::PoamItem {
        fn uuid<'a>(&'a self) -> Option<&'a str> {
        return self.uuid.as_deref();
    }
        fn title<'a>(&'a self) -> &'a str {
        return &self.title[..];
    }
        fn description<'a>(&'a self) -> &'a str {
        return &self.description[..];
    }
        fn origins<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Origin>> {
        return self.origins.as_ref();
    }
        fn related_findings<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::RelatedFinding>> {
        return self.related_findings.as_ref();
    }
        fn related_observations<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::RelatedObservation>> {
        return self.related_observations.as_ref();
    }
        fn related_risks<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::AssociatedRisk>> {
        return self.related_risks.as_ref();
    }
}


pub trait RelatedFinding   {

    fn finding_uuid<'a>(&'a self) -> &'a str;
    // fn finding_uuid_mut(&mut self) -> &mut &'a str;
    // fn set_finding_uuid(&mut self, value: String);

    fn remarks<'a>(&'a self) -> Option<&'a str>;
    // fn remarks_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_remarks(&mut self, value: Option<&'a str>);


}

impl RelatedFinding for crate::RelatedFinding {
        fn finding_uuid<'a>(&'a self) -> &'a str {
        return &self.finding_uuid[..];
    }
        fn remarks<'a>(&'a self) -> Option<&'a str> {
        return self.remarks.as_deref();
    }
}
