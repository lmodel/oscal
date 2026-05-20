-- ====================================================================
-- SQL Validation Queries
-- Generated from LinkML schema
-- LinkML v1.11.0
-- Generator: sqlvalidationgen.py v0.1.0
-- Dialect: sqlite
-- ====================================================================

SELECT 'CatalogDocument' AS table_name, 'catalog' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "CatalogDocument" 
WHERE "CatalogDocument".catalog IS NULL

UNION ALL

SELECT 'Catalog' AS table_name, 'uuid' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Catalog" 
WHERE "Catalog".uuid IS NULL

UNION ALL

SELECT 'Catalog' AS table_name, 'metadata' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Catalog" 
WHERE "Catalog".metadata IS NULL

UNION ALL

SELECT 'Group' AS table_name, 'title' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Group" 
WHERE "Group".title IS NULL

UNION ALL

SELECT 'Control' AS table_name, 'id' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Control" 
WHERE "Control".id IS NULL

UNION ALL

SELECT 'Control' AS table_name, 'title' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Control" 
WHERE "Control".title IS NULL

UNION ALL

SELECT 'Metadata' AS table_name, 'title' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Metadata" 
WHERE "Metadata".title IS NULL

UNION ALL

SELECT 'Metadata' AS table_name, 'last_modified' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Metadata" 
WHERE "Metadata".last_modified IS NULL

UNION ALL

SELECT 'Metadata' AS table_name, 'version' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Metadata" 
WHERE "Metadata".version IS NULL

UNION ALL

SELECT 'Metadata' AS table_name, 'oscal_version' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Metadata" 
WHERE "Metadata".oscal_version IS NULL

UNION ALL

SELECT 'Revision' AS table_name, 'version' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Revision" 
WHERE "Revision".version IS NULL

UNION ALL

SELECT 'DocumentId' AS table_name, 'identifier' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "DocumentId" 
WHERE "DocumentId".identifier IS NULL

UNION ALL

SELECT 'Role' AS table_name, 'id' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Role" 
WHERE "Role".id IS NULL

UNION ALL

SELECT 'Role' AS table_name, 'title' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Role" 
WHERE "Role".title IS NULL

UNION ALL

SELECT 'Location' AS table_name, 'uuid' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Location" 
WHERE "Location".uuid IS NULL

UNION ALL

SELECT 'Party' AS table_name, 'uuid' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Party" 
WHERE "Party".uuid IS NULL

UNION ALL

SELECT 'Party' AS table_name, 'type' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Party" 
WHERE "Party".type IS NULL

UNION ALL

SELECT 'Party' AS table_name, 'type' AS column_name, 'enum' AS constraint_type, id AS record_id, type AS invalid_value 
FROM "Party" 
WHERE "Party".type IS NOT NULL AND ("Party".type NOT IN ('person', 'organization'))

UNION ALL

SELECT 'PartyExternalId' AS table_name, 'scheme' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "PartyExternalId" 
WHERE "PartyExternalId".scheme IS NULL

UNION ALL

SELECT 'PartyExternalId' AS table_name, 'id' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "PartyExternalId" 
WHERE "PartyExternalId".id IS NULL

UNION ALL

SELECT 'ResponsibleParty' AS table_name, 'role_id' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "ResponsibleParty" 
WHERE "ResponsibleParty".role_id IS NULL

UNION ALL

SELECT 'ResponsibleParty' AS table_name, 'party_uuids' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "ResponsibleParty" 
WHERE "ResponsibleParty".party_uuids IS NULL

UNION ALL

SELECT 'ResponsibleRole' AS table_name, 'role_id' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "ResponsibleRole" 
WHERE "ResponsibleRole".role_id IS NULL

UNION ALL

SELECT 'Action' AS table_name, 'uuid' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Action" 
WHERE "Action".uuid IS NULL

UNION ALL

SELECT 'Action' AS table_name, 'type' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Action" 
WHERE "Action".type IS NULL

UNION ALL

SELECT 'Action' AS table_name, 'type' AS column_name, 'enum' AS constraint_type, id AS record_id, type AS invalid_value 
FROM "Action" 
WHERE "Action".type IS NOT NULL AND ("Action".type NOT IN ('approval', 'request-changes'))

UNION ALL

SELECT 'Action' AS table_name, 'system' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Action" 
WHERE "Action".system IS NULL

UNION ALL

SELECT 'TelephoneNumber' AS table_name, 'number' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "TelephoneNumber" 
WHERE "TelephoneNumber".number IS NULL

UNION ALL

SELECT 'Hash' AS table_name, 'value' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Hash" 
WHERE "Hash".value IS NULL

UNION ALL

SELECT 'Hash' AS table_name, 'algorithm' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Hash" 
WHERE "Hash".algorithm IS NULL

UNION ALL

SELECT 'Property' AS table_name, 'name' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Property" 
WHERE "Property".name IS NULL

UNION ALL

SELECT 'Property' AS table_name, 'value' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Property" 
WHERE "Property".value IS NULL

UNION ALL

SELECT 'MetadataProperty' AS table_name, 'name' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "MetadataProperty" 
WHERE "MetadataProperty".name IS NULL

UNION ALL

SELECT 'MetadataProperty' AS table_name, 'name' AS column_name, 'enum' AS constraint_type, id AS record_id, name AS invalid_value 
FROM "MetadataProperty" 
WHERE "MetadataProperty".name IS NOT NULL AND ("MetadataProperty".name NOT IN ('keywords', 'resolution-tool', 'source-profile-uuid'))

UNION ALL

SELECT 'MetadataProperty' AS table_name, 'value' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "MetadataProperty" 
WHERE "MetadataProperty".value IS NULL

UNION ALL

SELECT 'RevisionProperty' AS table_name, 'name' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "RevisionProperty" 
WHERE "RevisionProperty".name IS NULL

UNION ALL

SELECT 'RevisionProperty' AS table_name, 'name' AS column_name, 'enum' AS constraint_type, id AS record_id, name AS invalid_value 
FROM "RevisionProperty" 
WHERE "RevisionProperty".name IS NOT NULL AND ("RevisionProperty".name NOT IN ('marking'))

UNION ALL

SELECT 'RevisionProperty' AS table_name, 'value' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "RevisionProperty" 
WHERE "RevisionProperty".value IS NULL

UNION ALL

SELECT 'LocationProperty' AS table_name, 'name' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "LocationProperty" 
WHERE "LocationProperty".name IS NULL

UNION ALL

SELECT 'LocationProperty' AS table_name, 'name' AS column_name, 'enum' AS constraint_type, id AS record_id, name AS invalid_value 
FROM "LocationProperty" 
WHERE "LocationProperty".name IS NOT NULL AND ("LocationProperty".name NOT IN ('type'))

UNION ALL

SELECT 'LocationProperty' AS table_name, 'value' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "LocationProperty" 
WHERE "LocationProperty".value IS NULL

UNION ALL

SELECT 'PartyProperty' AS table_name, 'name' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "PartyProperty" 
WHERE "PartyProperty".name IS NULL

UNION ALL

SELECT 'PartyProperty' AS table_name, 'name' AS column_name, 'enum' AS constraint_type, id AS record_id, name AS invalid_value 
FROM "PartyProperty" 
WHERE "PartyProperty".name IS NOT NULL AND ("PartyProperty".name NOT IN ('mail-stop', 'office', 'job-title'))

UNION ALL

SELECT 'PartyProperty' AS table_name, 'value' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "PartyProperty" 
WHERE "PartyProperty".value IS NULL

UNION ALL

SELECT 'ResourceProperty' AS table_name, 'name' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "ResourceProperty" 
WHERE "ResourceProperty".name IS NULL

UNION ALL

SELECT 'ResourceProperty' AS table_name, 'name' AS column_name, 'enum' AS constraint_type, id AS record_id, name AS invalid_value 
FROM "ResourceProperty" 
WHERE "ResourceProperty".name IS NOT NULL AND ("ResourceProperty".name NOT IN ('type', 'version', 'published'))

UNION ALL

SELECT 'ResourceProperty' AS table_name, 'value' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "ResourceProperty" 
WHERE "ResourceProperty".value IS NULL

UNION ALL

SELECT 'PartProperty' AS table_name, 'name' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "PartProperty" 
WHERE "PartProperty".name IS NULL

UNION ALL

SELECT 'PartProperty' AS table_name, 'name' AS column_name, 'enum' AS constraint_type, id AS record_id, name AS invalid_value 
FROM "PartProperty" 
WHERE "PartProperty".name IS NOT NULL AND ("PartProperty".name NOT IN ('label', 'sort-id', 'alt-identifier'))

UNION ALL

SELECT 'PartProperty' AS table_name, 'value' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "PartProperty" 
WHERE "PartProperty".value IS NULL

UNION ALL

SELECT 'ParameterProperty' AS table_name, 'name' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "ParameterProperty" 
WHERE "ParameterProperty".name IS NULL

UNION ALL

SELECT 'ParameterProperty' AS table_name, 'value' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "ParameterProperty" 
WHERE "ParameterProperty".value IS NULL

UNION ALL

SELECT 'MetadataPartyExternalId' AS table_name, 'scheme' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "MetadataPartyExternalId" 
WHERE "MetadataPartyExternalId".scheme IS NULL

UNION ALL

SELECT 'MetadataPartyExternalId' AS table_name, 'id' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "MetadataPartyExternalId" 
WHERE "MetadataPartyExternalId".id IS NULL

UNION ALL

SELECT 'Link' AS table_name, 'href' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Link" 
WHERE "Link".href IS NULL

UNION ALL

SELECT 'Resource' AS table_name, 'uuid' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Resource" 
WHERE "Resource".uuid IS NULL

UNION ALL

SELECT 'Citation' AS table_name, 'text' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Citation" 
WHERE "Citation".text IS NULL

UNION ALL

SELECT 'ResourceLink' AS table_name, 'href' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "ResourceLink" 
WHERE "ResourceLink".href IS NULL

UNION ALL

SELECT 'Base64Resource' AS table_name, 'value' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Base64Resource" 
WHERE "Base64Resource".value IS NULL

UNION ALL

SELECT 'Part' AS table_name, 'name' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Part" 
WHERE "Part".name IS NULL

UNION ALL

SELECT 'Parameter' AS table_name, 'id' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Parameter" 
WHERE "Parameter".id IS NULL

UNION ALL

SELECT 'ConstraintTest' AS table_name, 'expression' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "ConstraintTest" 
WHERE "ConstraintTest".expression IS NULL

UNION ALL

SELECT 'ParameterGuideline' AS table_name, 'prose' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "ParameterGuideline" 
WHERE "ParameterGuideline".prose IS NULL

UNION ALL

SELECT 'ParameterSelection' AS table_name, 'how_many' AS column_name, 'enum' AS constraint_type, id AS record_id, how_many AS invalid_value 
FROM "ParameterSelection" 
WHERE "ParameterSelection".how_many IS NOT NULL AND ("ParameterSelection".how_many NOT IN ('one', 'one-or-more'))

UNION ALL

SELECT 'SelectControlById' AS table_name, 'with_child_controls' AS column_name, 'enum' AS constraint_type, id AS record_id, with_child_controls AS invalid_value 
FROM "SelectControlById" 
WHERE "SelectControlById".with_child_controls IS NOT NULL AND ("SelectControlById".with_child_controls NOT IN ('yes', 'no'))

UNION ALL

SELECT 'ProfileDocument' AS table_name, 'profile' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "ProfileDocument" 
WHERE "ProfileDocument".profile IS NULL

UNION ALL

SELECT 'Profile' AS table_name, 'uuid' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Profile" 
WHERE "Profile".uuid IS NULL

UNION ALL

SELECT 'Profile' AS table_name, 'metadata' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Profile" 
WHERE "Profile".metadata IS NULL

UNION ALL

SELECT 'Profile' AS table_name, 'imports' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Profile" 
WHERE "Profile".imports IS NULL

UNION ALL

SELECT 'ProfileImport' AS table_name, 'href' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "ProfileImport" 
WHERE "ProfileImport".href IS NULL

UNION ALL

SELECT 'CombinationRule' AS table_name, 'method' AS column_name, 'enum' AS constraint_type, id AS record_id, method AS invalid_value 
FROM "CombinationRule" 
WHERE "CombinationRule".method IS NOT NULL AND ("CombinationRule".method NOT IN ('use-first', 'merge', 'keep'))

UNION ALL

SELECT 'ProfileGroup' AS table_name, 'title' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "ProfileGroup" 
WHERE "ProfileGroup".title IS NULL

UNION ALL

SELECT 'ParameterSetting' AS table_name, 'param_id' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "ParameterSetting" 
WHERE "ParameterSetting".param_id IS NULL

UNION ALL

SELECT 'Alteration' AS table_name, 'control_id' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Alteration" 
WHERE "Alteration".control_id IS NULL

UNION ALL

SELECT 'Removal' AS table_name, 'by_item_name' AS column_name, 'enum' AS constraint_type, id AS record_id, by_item_name AS invalid_value 
FROM "Removal" 
WHERE "Removal".by_item_name IS NOT NULL AND ("Removal".by_item_name NOT IN ('param', 'prop', 'link', 'part', 'mapping', 'map'))

UNION ALL

SELECT 'Addition' AS table_name, 'position' AS column_name, 'enum' AS constraint_type, id AS record_id, position AS invalid_value 
FROM "Addition" 
WHERE "Addition".position IS NOT NULL AND ("Addition".position NOT IN ('before', 'after', 'starting', 'ending'))

UNION ALL

SELECT 'ProfileAlterationProperty' AS table_name, 'name' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "ProfileAlterationProperty" 
WHERE "ProfileAlterationProperty".name IS NULL

UNION ALL

SELECT 'ProfileAlterationProperty' AS table_name, 'name' AS column_name, 'enum' AS constraint_type, id AS record_id, name AS invalid_value 
FROM "ProfileAlterationProperty" 
WHERE "ProfileAlterationProperty".name IS NOT NULL AND ("ProfileAlterationProperty".name NOT IN ('label', 'sort-id', 'alt-identifier'))

UNION ALL

SELECT 'ProfileAlterationProperty' AS table_name, 'value' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "ProfileAlterationProperty" 
WHERE "ProfileAlterationProperty".value IS NULL

UNION ALL

SELECT 'InsertControls' AS table_name, 'order' AS column_name, 'enum' AS constraint_type, id AS record_id, "order" AS invalid_value 
FROM "InsertControls" 
WHERE "InsertControls"."order" IS NOT NULL AND ("InsertControls"."order" NOT IN ('keep', 'ascending', 'descending'))

UNION ALL

SELECT 'AssessmentPlanDocument' AS table_name, 'assessment_plan' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "AssessmentPlanDocument" 
WHERE "AssessmentPlanDocument".assessment_plan IS NULL

UNION ALL

SELECT 'AssessmentPlan' AS table_name, 'uuid' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "AssessmentPlan" 
WHERE "AssessmentPlan".uuid IS NULL

UNION ALL

SELECT 'AssessmentPlan' AS table_name, 'metadata' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "AssessmentPlan" 
WHERE "AssessmentPlan".metadata IS NULL

UNION ALL

SELECT 'AssessmentPlan' AS table_name, 'import_ssp' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "AssessmentPlan" 
WHERE "AssessmentPlan".import_ssp IS NULL

UNION ALL

SELECT 'AssessmentPlan' AS table_name, 'reviewed_controls' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "AssessmentPlan" 
WHERE "AssessmentPlan".reviewed_controls IS NULL

UNION ALL

SELECT 'ImportSSP' AS table_name, 'href' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "ImportSSP" 
WHERE "ImportSSP".href IS NULL

UNION ALL

SELECT 'ReviewedControls' AS table_name, 'control_selections' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "ReviewedControls" 
WHERE "ReviewedControls".control_selections IS NULL

UNION ALL

SELECT 'AssessmentSelectControlById' AS table_name, 'control_id' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "AssessmentSelectControlById" 
WHERE "AssessmentSelectControlById".control_id IS NULL

UNION ALL

SELECT 'SelectObjectiveById' AS table_name, 'objective_id' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "SelectObjectiveById" 
WHERE "SelectObjectiveById".objective_id IS NULL

UNION ALL

SELECT 'AssessmentSubject' AS table_name, 'type' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "AssessmentSubject" 
WHERE "AssessmentSubject".type IS NULL

UNION ALL

SELECT 'SelectSubjectById' AS table_name, 'subject_uuid' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "SelectSubjectById" 
WHERE "SelectSubjectById".subject_uuid IS NULL

UNION ALL

SELECT 'SelectSubjectById' AS table_name, 'type' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "SelectSubjectById" 
WHERE "SelectSubjectById".type IS NULL

UNION ALL

SELECT 'SubjectReference' AS table_name, 'subject_uuid' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "SubjectReference" 
WHERE "SubjectReference".subject_uuid IS NULL

UNION ALL

SELECT 'SubjectReference' AS table_name, 'type' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "SubjectReference" 
WHERE "SubjectReference".type IS NULL

UNION ALL

SELECT 'AssessmentSubjectPlaceholder' AS table_name, 'uuid' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "AssessmentSubjectPlaceholder" 
WHERE "AssessmentSubjectPlaceholder".uuid IS NULL

UNION ALL

SELECT 'AssessmentSubjectPlaceholder' AS table_name, 'sources' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "AssessmentSubjectPlaceholder" 
WHERE "AssessmentSubjectPlaceholder".sources IS NULL

UNION ALL

SELECT 'AssessmentSubjectSource' AS table_name, 'task_uuid' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "AssessmentSubjectSource" 
WHERE "AssessmentSubjectSource".task_uuid IS NULL

UNION ALL

SELECT 'AssessmentAssets' AS table_name, 'assessment_platforms' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "AssessmentAssets" 
WHERE "AssessmentAssets".assessment_platforms IS NULL

UNION ALL

SELECT 'AssessmentPlatform' AS table_name, 'uuid' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "AssessmentPlatform" 
WHERE "AssessmentPlatform".uuid IS NULL

UNION ALL

SELECT 'UsesComponent' AS table_name, 'component_uuid' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "UsesComponent" 
WHERE "UsesComponent".component_uuid IS NULL

UNION ALL

SELECT 'LocalObjective' AS table_name, 'control_id' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "LocalObjective" 
WHERE "LocalObjective".control_id IS NULL

UNION ALL

SELECT 'LocalObjective' AS table_name, 'parts' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "LocalObjective" 
WHERE "LocalObjective".parts IS NULL

UNION ALL

SELECT 'AssessmentMethod' AS table_name, 'uuid' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "AssessmentMethod" 
WHERE "AssessmentMethod".uuid IS NULL

UNION ALL

SELECT 'AssessmentMethod' AS table_name, 'part' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "AssessmentMethod" 
WHERE "AssessmentMethod".part IS NULL

UNION ALL

SELECT 'Activity' AS table_name, 'uuid' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Activity" 
WHERE "Activity".uuid IS NULL

UNION ALL

SELECT 'Activity' AS table_name, 'description' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Activity" 
WHERE "Activity".description IS NULL

UNION ALL

SELECT 'Step' AS table_name, 'uuid' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Step" 
WHERE "Step".uuid IS NULL

UNION ALL

SELECT 'Step' AS table_name, 'description' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Step" 
WHERE "Step".description IS NULL

UNION ALL

SELECT 'Task' AS table_name, 'uuid' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Task" 
WHERE "Task".uuid IS NULL

UNION ALL

SELECT 'Task' AS table_name, 'type' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Task" 
WHERE "Task".type IS NULL

UNION ALL

SELECT 'Task' AS table_name, 'title' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Task" 
WHERE "Task".title IS NULL

UNION ALL

SELECT 'OnDateCondition' AS table_name, 'date' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "OnDateCondition" 
WHERE "OnDateCondition".date IS NULL

UNION ALL

SELECT 'WithinDateRange' AS table_name, 'start' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "WithinDateRange" 
WHERE "WithinDateRange".start IS NULL

UNION ALL

SELECT 'WithinDateRange' AS table_name, 'end' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "WithinDateRange" 
WHERE "WithinDateRange"."end" IS NULL

UNION ALL

SELECT 'AtFrequency' AS table_name, 'period' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "AtFrequency" 
WHERE "AtFrequency".period IS NULL

UNION ALL

SELECT 'AtFrequency' AS table_name, 'unit' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "AtFrequency" 
WHERE "AtFrequency".unit IS NULL

UNION ALL

SELECT 'AtFrequency' AS table_name, 'unit' AS column_name, 'enum' AS constraint_type, id AS record_id, unit AS invalid_value 
FROM "AtFrequency" 
WHERE "AtFrequency".unit IS NOT NULL AND ("AtFrequency".unit NOT IN ('seconds', 'minutes', 'hours', 'days', 'months', 'years'))

UNION ALL

SELECT 'TaskDependency' AS table_name, 'task_uuid' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "TaskDependency" 
WHERE "TaskDependency".task_uuid IS NULL

UNION ALL

SELECT 'AssociatedActivity' AS table_name, 'activity_uuid' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "AssociatedActivity" 
WHERE "AssociatedActivity".activity_uuid IS NULL

UNION ALL

SELECT 'AssociatedActivity' AS table_name, 'subjects' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "AssociatedActivity" 
WHERE "AssociatedActivity".subjects IS NULL

UNION ALL

SELECT 'AssessmentPart' AS table_name, 'name' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "AssessmentPart" 
WHERE "AssessmentPart".name IS NULL

UNION ALL

SELECT 'TermsAndConditionsPart' AS table_name, 'name' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "TermsAndConditionsPart" 
WHERE "TermsAndConditionsPart".name IS NULL

UNION ALL

SELECT 'TermsAndConditionsPart' AS table_name, 'name' AS column_name, 'enum' AS constraint_type, id AS record_id, name AS invalid_value 
FROM "TermsAndConditionsPart" 
WHERE "TermsAndConditionsPart".name IS NOT NULL AND ("TermsAndConditionsPart".name NOT IN ('rules-of-engagement', 'disclosures', 'assessment-inclusions', 'assessment-exclusions', 'results-delivery', 'assumptions', 'methodology'))

UNION ALL

SELECT 'ControlPart' AS table_name, 'name' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "ControlPart" 
WHERE "ControlPart".name IS NULL

UNION ALL

SELECT 'SetParameter' AS table_name, 'param_id' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "SetParameter" 
WHERE "SetParameter".param_id IS NULL

UNION ALL

SELECT 'SetParameter' AS table_name, 'values' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "SetParameter" 
WHERE "SetParameter"."values" IS NULL

UNION ALL

SELECT 'SystemComponent' AS table_name, 'uuid' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "SystemComponent" 
WHERE "SystemComponent".uuid IS NULL

UNION ALL

SELECT 'SystemComponent' AS table_name, 'type' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "SystemComponent" 
WHERE "SystemComponent".type IS NULL

UNION ALL

SELECT 'SystemComponent' AS table_name, 'title' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "SystemComponent" 
WHERE "SystemComponent".title IS NULL

UNION ALL

SELECT 'SystemComponent' AS table_name, 'description' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "SystemComponent" 
WHERE "SystemComponent".description IS NULL

UNION ALL

SELECT 'SystemComponent' AS table_name, 'status' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "SystemComponent" 
WHERE "SystemComponent".status IS NULL

UNION ALL

SELECT 'ComponentStatus' AS table_name, 'state' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "ComponentStatus" 
WHERE "ComponentStatus".state IS NULL

UNION ALL

SELECT 'ComponentStatus' AS table_name, 'state' AS column_name, 'enum' AS constraint_type, id AS record_id, state AS invalid_value 
FROM "ComponentStatus" 
WHERE "ComponentStatus".state IS NOT NULL AND ("ComponentStatus".state NOT IN ('under-development', 'operational', 'disposition', 'other'))

UNION ALL

SELECT 'PortRange' AS table_name, 'transport' AS column_name, 'enum' AS constraint_type, id AS record_id, transport AS invalid_value 
FROM "PortRange" 
WHERE "PortRange".transport IS NOT NULL AND ("PortRange".transport NOT IN ('TCP', 'UDP'))

UNION ALL

SELECT 'ImplementationStatus' AS table_name, 'state' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "ImplementationStatus" 
WHERE "ImplementationStatus".state IS NULL

UNION ALL

SELECT 'SystemUser' AS table_name, 'uuid' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "SystemUser" 
WHERE "SystemUser".uuid IS NULL

UNION ALL

SELECT 'AuthorizedPrivilege' AS table_name, 'title' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "AuthorizedPrivilege" 
WHERE "AuthorizedPrivilege".title IS NULL

UNION ALL

SELECT 'AuthorizedPrivilege' AS table_name, 'functions_performed' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "AuthorizedPrivilege" 
WHERE "AuthorizedPrivilege".functions_performed IS NULL

UNION ALL

SELECT 'InventoryItem' AS table_name, 'uuid' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "InventoryItem" 
WHERE "InventoryItem".uuid IS NULL

UNION ALL

SELECT 'InventoryItem' AS table_name, 'description' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "InventoryItem" 
WHERE "InventoryItem".description IS NULL

UNION ALL

SELECT 'ImplementedComponent' AS table_name, 'component_uuid' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "ImplementedComponent" 
WHERE "ImplementedComponent".component_uuid IS NULL

UNION ALL

SELECT 'SystemId' AS table_name, 'id' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "SystemId" 
WHERE "SystemId".id IS NULL

UNION ALL

SELECT 'ImplementationCommonProperty' AS table_name, 'name' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "ImplementationCommonProperty" 
WHERE "ImplementationCommonProperty".name IS NULL

UNION ALL

SELECT 'ImplementationCommonProperty' AS table_name, 'name' AS column_name, 'enum' AS constraint_type, id AS record_id, name AS invalid_value 
FROM "ImplementationCommonProperty" 
WHERE "ImplementationCommonProperty".name IS NOT NULL AND ("ImplementationCommonProperty".name NOT IN ('implementation-point', 'leveraged-authorization-uuid', 'inherited-uuid', 'asset-type', 'asset-id', 'asset-tag', 'public', 'virtual', 'vlan-id', 'network-id', 'label', 'sort-id', 'baseline-configuration-name', 'allows-authenticated-scan', 'function', 'hardware-model', 'model', 'os-name', 'os-version', 'software-name', 'software-version', 'software-patch-level', 'version', 'patch-level', 'release-date', 'validation-type', 'validation-reference', 'vendor-name', 'software-identifier', 'isa-title', 'isa-date', 'isa-remote-system-name', 'ipv4-address', 'ipv6-address', 'direction', 'uri', 'fqdn', 'serial-number', 'netbios-name', 'mac-address', 'physical-location', 'is-scanned', 'type', 'privilege-level'))

UNION ALL

SELECT 'ImplementationCommonProperty' AS table_name, 'value' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "ImplementationCommonProperty" 
WHERE "ImplementationCommonProperty".value IS NULL

UNION ALL

SELECT 'ImplementationCommonLink' AS table_name, 'href' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "ImplementationCommonLink" 
WHERE "ImplementationCommonLink".href IS NULL

UNION ALL

SELECT 'ImplementationResponsibleRole' AS table_name, 'role_id' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "ImplementationResponsibleRole" 
WHERE "ImplementationResponsibleRole".role_id IS NULL

UNION ALL

SELECT 'ImplementationResponsibleParty' AS table_name, 'role_id' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "ImplementationResponsibleParty" 
WHERE "ImplementationResponsibleParty".role_id IS NULL

UNION ALL

SELECT 'ImplementationResponsibleParty' AS table_name, 'party_uuids' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "ImplementationResponsibleParty" 
WHERE "ImplementationResponsibleParty".party_uuids IS NULL

UNION ALL

SELECT 'Origin' AS table_name, 'actors' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Origin" 
WHERE "Origin".actors IS NULL

UNION ALL

SELECT 'OriginActor' AS table_name, 'type' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "OriginActor" 
WHERE "OriginActor".type IS NULL

UNION ALL

SELECT 'OriginActor' AS table_name, 'type' AS column_name, 'enum' AS constraint_type, id AS record_id, type AS invalid_value 
FROM "OriginActor" 
WHERE "OriginActor".type IS NOT NULL AND ("OriginActor".type NOT IN ('tool', 'assessment-platform', 'party'))

UNION ALL

SELECT 'OriginActor' AS table_name, 'actor_uuid' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "OriginActor" 
WHERE "OriginActor".actor_uuid IS NULL

UNION ALL

SELECT 'RelatedTask' AS table_name, 'task_uuid' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "RelatedTask" 
WHERE "RelatedTask".task_uuid IS NULL

UNION ALL

SELECT 'IdentifiedSubject' AS table_name, 'subject_placeholder_uuid' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "IdentifiedSubject" 
WHERE "IdentifiedSubject".subject_placeholder_uuid IS NULL

UNION ALL

SELECT 'IdentifiedSubject' AS table_name, 'subjects' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "IdentifiedSubject" 
WHERE "IdentifiedSubject".subjects IS NULL

UNION ALL

SELECT 'Observation' AS table_name, 'uuid' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Observation" 
WHERE "Observation".uuid IS NULL

UNION ALL

SELECT 'Observation' AS table_name, 'description' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Observation" 
WHERE "Observation".description IS NULL

UNION ALL

SELECT 'Observation' AS table_name, 'methods' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Observation" 
WHERE "Observation".methods IS NULL

UNION ALL

SELECT 'Observation' AS table_name, 'collected' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Observation" 
WHERE "Observation".collected IS NULL

UNION ALL

SELECT 'RelevantEvidence' AS table_name, 'description' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "RelevantEvidence" 
WHERE "RelevantEvidence".description IS NULL

UNION ALL

SELECT 'Finding' AS table_name, 'uuid' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Finding" 
WHERE "Finding".uuid IS NULL

UNION ALL

SELECT 'Finding' AS table_name, 'title' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Finding" 
WHERE "Finding".title IS NULL

UNION ALL

SELECT 'Finding' AS table_name, 'description' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Finding" 
WHERE "Finding".description IS NULL

UNION ALL

SELECT 'Finding' AS table_name, 'target' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Finding" 
WHERE "Finding".target IS NULL

UNION ALL

SELECT 'FindingTarget' AS table_name, 'type' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "FindingTarget" 
WHERE "FindingTarget".type IS NULL

UNION ALL

SELECT 'FindingTarget' AS table_name, 'type' AS column_name, 'enum' AS constraint_type, id AS record_id, type AS invalid_value 
FROM "FindingTarget" 
WHERE "FindingTarget".type IS NOT NULL AND ("FindingTarget".type NOT IN ('statement-id', 'objective-id'))

UNION ALL

SELECT 'FindingTarget' AS table_name, 'target_id' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "FindingTarget" 
WHERE "FindingTarget".target_id IS NULL

UNION ALL

SELECT 'FindingTarget' AS table_name, 'status' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "FindingTarget" 
WHERE "FindingTarget".status IS NULL

UNION ALL

SELECT 'ObjectiveStatus' AS table_name, 'state' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "ObjectiveStatus" 
WHERE "ObjectiveStatus".state IS NULL

UNION ALL

SELECT 'ObjectiveStatus' AS table_name, 'state' AS column_name, 'enum' AS constraint_type, id AS record_id, state AS invalid_value 
FROM "ObjectiveStatus" 
WHERE "ObjectiveStatus".state IS NOT NULL AND ("ObjectiveStatus".state NOT IN ('satisfied', 'not-satisfied'))

UNION ALL

SELECT 'RelatedObservation' AS table_name, 'observation_uuid' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "RelatedObservation" 
WHERE "RelatedObservation".observation_uuid IS NULL

UNION ALL

SELECT 'AssociatedRisk' AS table_name, 'risk_uuid' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "AssociatedRisk" 
WHERE "AssociatedRisk".risk_uuid IS NULL

UNION ALL

SELECT 'Risk' AS table_name, 'uuid' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Risk" 
WHERE "Risk".uuid IS NULL

UNION ALL

SELECT 'Risk' AS table_name, 'title' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Risk" 
WHERE "Risk".title IS NULL

UNION ALL

SELECT 'Risk' AS table_name, 'description' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Risk" 
WHERE "Risk".description IS NULL

UNION ALL

SELECT 'Risk' AS table_name, 'statement' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Risk" 
WHERE "Risk".statement IS NULL

UNION ALL

SELECT 'Risk' AS table_name, 'status' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Risk" 
WHERE "Risk".status IS NULL

UNION ALL

SELECT 'ThreatId' AS table_name, 'system' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "ThreatId" 
WHERE "ThreatId".system IS NULL

UNION ALL

SELECT 'ThreatId' AS table_name, 'id' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "ThreatId" 
WHERE "ThreatId".id IS NULL

UNION ALL

SELECT 'Characterization' AS table_name, 'origin' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Characterization" 
WHERE "Characterization".origin IS NULL

UNION ALL

SELECT 'Characterization' AS table_name, 'facets' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Characterization" 
WHERE "Characterization".facets IS NULL

UNION ALL

SELECT 'Facet' AS table_name, 'name' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Facet" 
WHERE "Facet".name IS NULL

UNION ALL

SELECT 'Facet' AS table_name, 'value' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Facet" 
WHERE "Facet".value IS NULL

UNION ALL

SELECT 'Facet' AS table_name, 'system' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Facet" 
WHERE "Facet".system IS NULL

UNION ALL

SELECT 'MitigatingFactor' AS table_name, 'uuid' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "MitigatingFactor" 
WHERE "MitigatingFactor".uuid IS NULL

UNION ALL

SELECT 'MitigatingFactor' AS table_name, 'description' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "MitigatingFactor" 
WHERE "MitigatingFactor".description IS NULL

UNION ALL

SELECT 'Response' AS table_name, 'uuid' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Response" 
WHERE "Response".uuid IS NULL

UNION ALL

SELECT 'Response' AS table_name, 'title' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Response" 
WHERE "Response".title IS NULL

UNION ALL

SELECT 'Response' AS table_name, 'description' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Response" 
WHERE "Response".description IS NULL

UNION ALL

SELECT 'Response' AS table_name, 'lifecycle' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Response" 
WHERE "Response".lifecycle IS NULL

UNION ALL

SELECT 'RequiredAsset' AS table_name, 'uuid' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "RequiredAsset" 
WHERE "RequiredAsset".uuid IS NULL

UNION ALL

SELECT 'RequiredAsset' AS table_name, 'description' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "RequiredAsset" 
WHERE "RequiredAsset".description IS NULL

UNION ALL

SELECT 'RiskLog' AS table_name, 'entries' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "RiskLog" 
WHERE "RiskLog".entries IS NULL

UNION ALL

SELECT 'RiskLogEntry' AS table_name, 'uuid' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "RiskLogEntry" 
WHERE "RiskLogEntry".uuid IS NULL

UNION ALL

SELECT 'RiskLogEntry' AS table_name, 'start' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "RiskLogEntry" 
WHERE "RiskLogEntry".start IS NULL

UNION ALL

SELECT 'LoggedBy' AS table_name, 'party_uuid' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "LoggedBy" 
WHERE "LoggedBy".party_uuid IS NULL

UNION ALL

SELECT 'RiskResponseReference' AS table_name, 'response_uuid' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "RiskResponseReference" 
WHERE "RiskResponseReference".response_uuid IS NULL

UNION ALL

SELECT 'SspDocument' AS table_name, 'system_security_plan' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "SspDocument" 
WHERE "SspDocument".system_security_plan IS NULL

UNION ALL

SELECT 'SystemSecurityPlan' AS table_name, 'uuid' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "SystemSecurityPlan" 
WHERE "SystemSecurityPlan".uuid IS NULL

UNION ALL

SELECT 'SystemSecurityPlan' AS table_name, 'metadata' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "SystemSecurityPlan" 
WHERE "SystemSecurityPlan".metadata IS NULL

UNION ALL

SELECT 'SystemSecurityPlan' AS table_name, 'import_profile' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "SystemSecurityPlan" 
WHERE "SystemSecurityPlan".import_profile IS NULL

UNION ALL

SELECT 'SystemSecurityPlan' AS table_name, 'system_characteristics' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "SystemSecurityPlan" 
WHERE "SystemSecurityPlan".system_characteristics IS NULL

UNION ALL

SELECT 'SystemSecurityPlan' AS table_name, 'system_implementation' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "SystemSecurityPlan" 
WHERE "SystemSecurityPlan".system_implementation IS NULL

UNION ALL

SELECT 'SystemSecurityPlan' AS table_name, 'control_implementation' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "SystemSecurityPlan" 
WHERE "SystemSecurityPlan".control_implementation IS NULL

UNION ALL

SELECT 'ImportProfile' AS table_name, 'href' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "ImportProfile" 
WHERE "ImportProfile".href IS NULL

UNION ALL

SELECT 'SystemCharacteristics' AS table_name, 'system_ids' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "SystemCharacteristics" 
WHERE "SystemCharacteristics".system_ids IS NULL

UNION ALL

SELECT 'SystemCharacteristics' AS table_name, 'system_name' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "SystemCharacteristics" 
WHERE "SystemCharacteristics".system_name IS NULL

UNION ALL

SELECT 'SystemCharacteristics' AS table_name, 'description' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "SystemCharacteristics" 
WHERE "SystemCharacteristics".description IS NULL

UNION ALL

SELECT 'SystemCharacteristics' AS table_name, 'system_information' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "SystemCharacteristics" 
WHERE "SystemCharacteristics".system_information IS NULL

UNION ALL

SELECT 'SystemCharacteristics' AS table_name, 'system_status' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "SystemCharacteristics" 
WHERE "SystemCharacteristics".system_status IS NULL

UNION ALL

SELECT 'SystemCharacteristics' AS table_name, 'authorization_boundary' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "SystemCharacteristics" 
WHERE "SystemCharacteristics".authorization_boundary IS NULL

UNION ALL

SELECT 'SystemInformation' AS table_name, 'information_types' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "SystemInformation" 
WHERE "SystemInformation".information_types IS NULL

UNION ALL

SELECT 'InformationType' AS table_name, 'title' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "InformationType" 
WHERE "InformationType".title IS NULL

UNION ALL

SELECT 'InformationType' AS table_name, 'description' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "InformationType" 
WHERE "InformationType".description IS NULL

UNION ALL

SELECT 'InformationTypeCategorization' AS table_name, 'system' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "InformationTypeCategorization" 
WHERE "InformationTypeCategorization".system IS NULL

UNION ALL

SELECT 'ImpactLevel' AS table_name, 'base' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "ImpactLevel" 
WHERE "ImpactLevel".base IS NULL

UNION ALL

SELECT 'SecurityImpactLevel' AS table_name, 'security_objective_confidentiality' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "SecurityImpactLevel" 
WHERE "SecurityImpactLevel".security_objective_confidentiality IS NULL

UNION ALL

SELECT 'SecurityImpactLevel' AS table_name, 'security_objective_integrity' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "SecurityImpactLevel" 
WHERE "SecurityImpactLevel".security_objective_integrity IS NULL

UNION ALL

SELECT 'SecurityImpactLevel' AS table_name, 'security_objective_availability' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "SecurityImpactLevel" 
WHERE "SecurityImpactLevel".security_objective_availability IS NULL

UNION ALL

SELECT 'SystemStatus' AS table_name, 'state' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "SystemStatus" 
WHERE "SystemStatus".state IS NULL

UNION ALL

SELECT 'SystemStatus' AS table_name, 'state' AS column_name, 'enum' AS constraint_type, id AS record_id, state AS invalid_value 
FROM "SystemStatus" 
WHERE "SystemStatus".state IS NOT NULL AND ("SystemStatus".state NOT IN ('operational', 'under-development', 'under-major-modification', 'disposition', 'other'))

UNION ALL

SELECT 'AuthorizationBoundary' AS table_name, 'description' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "AuthorizationBoundary" 
WHERE "AuthorizationBoundary".description IS NULL

UNION ALL

SELECT 'Diagram' AS table_name, 'uuid' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Diagram" 
WHERE "Diagram".uuid IS NULL

UNION ALL

SELECT 'NetworkArchitecture' AS table_name, 'description' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "NetworkArchitecture" 
WHERE "NetworkArchitecture".description IS NULL

UNION ALL

SELECT 'DataFlow' AS table_name, 'description' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "DataFlow" 
WHERE "DataFlow".description IS NULL

UNION ALL

SELECT 'SystemImplementation' AS table_name, 'components' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "SystemImplementation" 
WHERE "SystemImplementation".components IS NULL

UNION ALL

SELECT 'LeveragedAuthorization' AS table_name, 'uuid' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "LeveragedAuthorization" 
WHERE "LeveragedAuthorization".uuid IS NULL

UNION ALL

SELECT 'LeveragedAuthorization' AS table_name, 'title' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "LeveragedAuthorization" 
WHERE "LeveragedAuthorization".title IS NULL

UNION ALL

SELECT 'LeveragedAuthorization' AS table_name, 'party_uuid' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "LeveragedAuthorization" 
WHERE "LeveragedAuthorization".party_uuid IS NULL

UNION ALL

SELECT 'LeveragedAuthorization' AS table_name, 'date_authorized' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "LeveragedAuthorization" 
WHERE "LeveragedAuthorization".date_authorized IS NULL

UNION ALL

SELECT 'SspControlImplementation' AS table_name, 'description' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "SspControlImplementation" 
WHERE "SspControlImplementation".description IS NULL

UNION ALL

SELECT 'SspControlImplementation' AS table_name, 'implemented_requirements' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "SspControlImplementation" 
WHERE "SspControlImplementation".implemented_requirements IS NULL

UNION ALL

SELECT 'SspImplementedRequirement' AS table_name, 'uuid' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "SspImplementedRequirement" 
WHERE "SspImplementedRequirement".uuid IS NULL

UNION ALL

SELECT 'SspImplementedRequirement' AS table_name, 'control_id' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "SspImplementedRequirement" 
WHERE "SspImplementedRequirement".control_id IS NULL

UNION ALL

SELECT 'SspStatement' AS table_name, 'statement_id' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "SspStatement" 
WHERE "SspStatement".statement_id IS NULL

UNION ALL

SELECT 'SspStatement' AS table_name, 'uuid' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "SspStatement" 
WHERE "SspStatement".uuid IS NULL

UNION ALL

SELECT 'ByComponent' AS table_name, 'component_uuid' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "ByComponent" 
WHERE "ByComponent".component_uuid IS NULL

UNION ALL

SELECT 'ByComponent' AS table_name, 'uuid' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "ByComponent" 
WHERE "ByComponent".uuid IS NULL

UNION ALL

SELECT 'ByComponent' AS table_name, 'description' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "ByComponent" 
WHERE "ByComponent".description IS NULL

UNION ALL

SELECT 'ProvidedControlImplementation' AS table_name, 'uuid' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "ProvidedControlImplementation" 
WHERE "ProvidedControlImplementation".uuid IS NULL

UNION ALL

SELECT 'ProvidedControlImplementation' AS table_name, 'description' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "ProvidedControlImplementation" 
WHERE "ProvidedControlImplementation".description IS NULL

UNION ALL

SELECT 'ControlResponsibility' AS table_name, 'uuid' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "ControlResponsibility" 
WHERE "ControlResponsibility".uuid IS NULL

UNION ALL

SELECT 'ControlResponsibility' AS table_name, 'description' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "ControlResponsibility" 
WHERE "ControlResponsibility".description IS NULL

UNION ALL

SELECT 'InheritedControlImplementation' AS table_name, 'uuid' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "InheritedControlImplementation" 
WHERE "InheritedControlImplementation".uuid IS NULL

UNION ALL

SELECT 'InheritedControlImplementation' AS table_name, 'description' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "InheritedControlImplementation" 
WHERE "InheritedControlImplementation".description IS NULL

UNION ALL

SELECT 'SatisfiedControlImplementation' AS table_name, 'uuid' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "SatisfiedControlImplementation" 
WHERE "SatisfiedControlImplementation".uuid IS NULL

UNION ALL

SELECT 'SatisfiedControlImplementation' AS table_name, 'description' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "SatisfiedControlImplementation" 
WHERE "SatisfiedControlImplementation".description IS NULL

UNION ALL

SELECT 'SspSystemCharacteristicsProp' AS table_name, 'name' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "SspSystemCharacteristicsProp" 
WHERE "SspSystemCharacteristicsProp".name IS NULL

UNION ALL

SELECT 'SspSystemCharacteristicsProp' AS table_name, 'name' AS column_name, 'enum' AS constraint_type, id AS record_id, name AS invalid_value 
FROM "SspSystemCharacteristicsProp" 
WHERE "SspSystemCharacteristicsProp".name IS NOT NULL AND ("SspSystemCharacteristicsProp".name NOT IN ('identity-assurance-level', 'authenticator-assurance-level', 'federation-assurance-level', 'cloud-deployment-model', 'cloud-service-model'))

UNION ALL

SELECT 'SspSystemCharacteristicsProp' AS table_name, 'value' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "SspSystemCharacteristicsProp" 
WHERE "SspSystemCharacteristicsProp".value IS NULL

UNION ALL

SELECT 'SspSystemInformationProp' AS table_name, 'name' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "SspSystemInformationProp" 
WHERE "SspSystemInformationProp".name IS NULL

UNION ALL

SELECT 'SspSystemInformationProp' AS table_name, 'name' AS column_name, 'enum' AS constraint_type, id AS record_id, name AS invalid_value 
FROM "SspSystemInformationProp" 
WHERE "SspSystemInformationProp".name IS NOT NULL AND ("SspSystemInformationProp".name NOT IN ('privacy-designation'))

UNION ALL

SELECT 'SspSystemInformationProp' AS table_name, 'value' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "SspSystemInformationProp" 
WHERE "SspSystemInformationProp".value IS NULL

UNION ALL

SELECT 'SspSystemInformationProp' AS table_name, 'value' AS column_name, 'enum' AS constraint_type, id AS record_id, value AS invalid_value 
FROM "SspSystemInformationProp" 
WHERE "SspSystemInformationProp".value IS NOT NULL AND ("SspSystemInformationProp".value NOT IN ('yes', 'no'))

UNION ALL

SELECT 'SspControlOriginationProp' AS table_name, 'name' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "SspControlOriginationProp" 
WHERE "SspControlOriginationProp".name IS NULL

UNION ALL

SELECT 'SspControlOriginationProp' AS table_name, 'name' AS column_name, 'enum' AS constraint_type, id AS record_id, name AS invalid_value 
FROM "SspControlOriginationProp" 
WHERE "SspControlOriginationProp".name IS NOT NULL AND ("SspControlOriginationProp".name NOT IN ('control-origination'))

UNION ALL

SELECT 'SspControlOriginationProp' AS table_name, 'value' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "SspControlOriginationProp" 
WHERE "SspControlOriginationProp".value IS NULL

UNION ALL

SELECT 'SspControlOriginationProp' AS table_name, 'value' AS column_name, 'enum' AS constraint_type, id AS record_id, value AS invalid_value 
FROM "SspControlOriginationProp" 
WHERE "SspControlOriginationProp".value IS NOT NULL AND ("SspControlOriginationProp".value NOT IN ('organization', 'system-specific', 'customer-configured', 'customer-provided', 'inherited'))

UNION ALL

SELECT 'SspAllowsAuthenticatedScanProp' AS table_name, 'name' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "SspAllowsAuthenticatedScanProp" 
WHERE "SspAllowsAuthenticatedScanProp".name IS NULL

UNION ALL

SELECT 'SspAllowsAuthenticatedScanProp' AS table_name, 'value' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "SspAllowsAuthenticatedScanProp" 
WHERE "SspAllowsAuthenticatedScanProp".value IS NULL

UNION ALL

SELECT 'SspAllowsAuthenticatedScanProp' AS table_name, 'value' AS column_name, 'enum' AS constraint_type, id AS record_id, value AS invalid_value 
FROM "SspAllowsAuthenticatedScanProp" 
WHERE "SspAllowsAuthenticatedScanProp".value IS NOT NULL AND ("SspAllowsAuthenticatedScanProp".value NOT IN ('yes', 'no'))

UNION ALL

SELECT 'SspSystemInformationLink' AS table_name, 'href' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "SspSystemInformationLink" 
WHERE "SspSystemInformationLink".href IS NULL

UNION ALL

SELECT 'SspDiagramLink' AS table_name, 'href' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "SspDiagramLink" 
WHERE "SspDiagramLink".href IS NULL

UNION ALL

SELECT 'SspLeveragedAuthorizationLink' AS table_name, 'href' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "SspLeveragedAuthorizationLink" 
WHERE "SspLeveragedAuthorizationLink".href IS NULL

UNION ALL

SELECT 'SspByComponentLink' AS table_name, 'href' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "SspByComponentLink" 
WHERE "SspByComponentLink".href IS NULL

UNION ALL

SELECT 'SspSystemCharacteristicsResponsibleParty' AS table_name, 'role_id' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "SspSystemCharacteristicsResponsibleParty" 
WHERE "SspSystemCharacteristicsResponsibleParty".role_id IS NULL

UNION ALL

SELECT 'SspSystemCharacteristicsResponsibleParty' AS table_name, 'party_uuids' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "SspSystemCharacteristicsResponsibleParty" 
WHERE "SspSystemCharacteristicsResponsibleParty".party_uuids IS NULL

UNION ALL

SELECT 'SspImplementedRequirementResponsibleRole' AS table_name, 'role_id' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "SspImplementedRequirementResponsibleRole" 
WHERE "SspImplementedRequirementResponsibleRole".role_id IS NULL

UNION ALL

SELECT 'SspByComponentResponsibleRole' AS table_name, 'role_id' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "SspByComponentResponsibleRole" 
WHERE "SspByComponentResponsibleRole".role_id IS NULL

UNION ALL

SELECT 'SspSystemComponent' AS table_name, 'uuid' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "SspSystemComponent" 
WHERE "SspSystemComponent".uuid IS NULL

UNION ALL

SELECT 'SspSystemComponent' AS table_name, 'type' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "SspSystemComponent" 
WHERE "SspSystemComponent".type IS NULL

UNION ALL

SELECT 'SspSystemComponent' AS table_name, 'title' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "SspSystemComponent" 
WHERE "SspSystemComponent".title IS NULL

UNION ALL

SELECT 'SspSystemComponent' AS table_name, 'description' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "SspSystemComponent" 
WHERE "SspSystemComponent".description IS NULL

UNION ALL

SELECT 'SspSystemComponent' AS table_name, 'status' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "SspSystemComponent" 
WHERE "SspSystemComponent".status IS NULL

UNION ALL

SELECT 'SspInventoryItem' AS table_name, 'uuid' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "SspInventoryItem" 
WHERE "SspInventoryItem".uuid IS NULL

UNION ALL

SELECT 'SspInventoryItem' AS table_name, 'description' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "SspInventoryItem" 
WHERE "SspInventoryItem".description IS NULL

UNION ALL

SELECT 'AssessmentResultsDocument' AS table_name, 'assessment_results' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "AssessmentResultsDocument" 
WHERE "AssessmentResultsDocument".assessment_results IS NULL

UNION ALL

SELECT 'AssessmentResults' AS table_name, 'uuid' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "AssessmentResults" 
WHERE "AssessmentResults".uuid IS NULL

UNION ALL

SELECT 'AssessmentResults' AS table_name, 'metadata' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "AssessmentResults" 
WHERE "AssessmentResults".metadata IS NULL

UNION ALL

SELECT 'AssessmentResults' AS table_name, 'import_ap' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "AssessmentResults" 
WHERE "AssessmentResults".import_ap IS NULL

UNION ALL

SELECT 'AssessmentResults' AS table_name, 'results' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "AssessmentResults" 
WHERE "AssessmentResults".results IS NULL

UNION ALL

SELECT 'ImportAssessmentPlan' AS table_name, 'href' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "ImportAssessmentPlan" 
WHERE "ImportAssessmentPlan".href IS NULL

UNION ALL

SELECT 'Result' AS table_name, 'uuid' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Result" 
WHERE "Result".uuid IS NULL

UNION ALL

SELECT 'Result' AS table_name, 'title' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Result" 
WHERE "Result".title IS NULL

UNION ALL

SELECT 'Result' AS table_name, 'description' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Result" 
WHERE "Result".description IS NULL

UNION ALL

SELECT 'Result' AS table_name, 'start' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Result" 
WHERE "Result".start IS NULL

UNION ALL

SELECT 'Result' AS table_name, 'reviewed_controls' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Result" 
WHERE "Result".reviewed_controls IS NULL

UNION ALL

SELECT 'Attestation' AS table_name, 'parts' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Attestation" 
WHERE "Attestation".parts IS NULL

UNION ALL

SELECT 'AssessmentLog' AS table_name, 'entries' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "AssessmentLog" 
WHERE "AssessmentLog".entries IS NULL

UNION ALL

SELECT 'AssessmentLogEntry' AS table_name, 'uuid' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "AssessmentLogEntry" 
WHERE "AssessmentLogEntry".uuid IS NULL

UNION ALL

SELECT 'AssessmentLogEntry' AS table_name, 'start' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "AssessmentLogEntry" 
WHERE "AssessmentLogEntry".start IS NULL

UNION ALL

SELECT 'ComponentDefinitionDocument' AS table_name, 'component_definition' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "ComponentDefinitionDocument" 
WHERE "ComponentDefinitionDocument".component_definition IS NULL

UNION ALL

SELECT 'ComponentDefinition' AS table_name, 'uuid' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "ComponentDefinition" 
WHERE "ComponentDefinition".uuid IS NULL

UNION ALL

SELECT 'ComponentDefinition' AS table_name, 'metadata' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "ComponentDefinition" 
WHERE "ComponentDefinition".metadata IS NULL

UNION ALL

SELECT 'ImportComponentDefinition' AS table_name, 'href' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "ImportComponentDefinition" 
WHERE "ImportComponentDefinition".href IS NULL

UNION ALL

SELECT 'DefinedComponent' AS table_name, 'uuid' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "DefinedComponent" 
WHERE "DefinedComponent".uuid IS NULL

UNION ALL

SELECT 'DefinedComponent' AS table_name, 'type' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "DefinedComponent" 
WHERE "DefinedComponent".type IS NULL

UNION ALL

SELECT 'DefinedComponent' AS table_name, 'title' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "DefinedComponent" 
WHERE "DefinedComponent".title IS NULL

UNION ALL

SELECT 'DefinedComponent' AS table_name, 'description' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "DefinedComponent" 
WHERE "DefinedComponent".description IS NULL

UNION ALL

SELECT 'Capability' AS table_name, 'uuid' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Capability" 
WHERE "Capability".uuid IS NULL

UNION ALL

SELECT 'Capability' AS table_name, 'name' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Capability" 
WHERE "Capability".name IS NULL

UNION ALL

SELECT 'Capability' AS table_name, 'description' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Capability" 
WHERE "Capability".description IS NULL

UNION ALL

SELECT 'IncorporatesComponent' AS table_name, 'component_uuid' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "IncorporatesComponent" 
WHERE "IncorporatesComponent".component_uuid IS NULL

UNION ALL

SELECT 'IncorporatesComponent' AS table_name, 'description' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "IncorporatesComponent" 
WHERE "IncorporatesComponent".description IS NULL

UNION ALL

SELECT 'ControlImplementationSet' AS table_name, 'uuid' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "ControlImplementationSet" 
WHERE "ControlImplementationSet".uuid IS NULL

UNION ALL

SELECT 'ControlImplementationSet' AS table_name, 'source' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "ControlImplementationSet" 
WHERE "ControlImplementationSet".source IS NULL

UNION ALL

SELECT 'ControlImplementationSet' AS table_name, 'description' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "ControlImplementationSet" 
WHERE "ControlImplementationSet".description IS NULL

UNION ALL

SELECT 'ControlImplementationSet' AS table_name, 'implemented_requirements' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "ControlImplementationSet" 
WHERE "ControlImplementationSet".implemented_requirements IS NULL

UNION ALL

SELECT 'ImplementedRequirement' AS table_name, 'uuid' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "ImplementedRequirement" 
WHERE "ImplementedRequirement".uuid IS NULL

UNION ALL

SELECT 'ImplementedRequirement' AS table_name, 'control_id' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "ImplementedRequirement" 
WHERE "ImplementedRequirement".control_id IS NULL

UNION ALL

SELECT 'ImplementedRequirement' AS table_name, 'description' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "ImplementedRequirement" 
WHERE "ImplementedRequirement".description IS NULL

UNION ALL

SELECT 'ImplementedControlStatement' AS table_name, 'statement_id' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "ImplementedControlStatement" 
WHERE "ImplementedControlStatement".statement_id IS NULL

UNION ALL

SELECT 'ImplementedControlStatement' AS table_name, 'uuid' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "ImplementedControlStatement" 
WHERE "ImplementedControlStatement".uuid IS NULL

UNION ALL

SELECT 'ImplementedControlStatement' AS table_name, 'description' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "ImplementedControlStatement" 
WHERE "ImplementedControlStatement".description IS NULL

UNION ALL

SELECT 'MappingCollectionDocument' AS table_name, 'mapping_collection' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "MappingCollectionDocument" 
WHERE "MappingCollectionDocument".mapping_collection IS NULL

UNION ALL

SELECT 'MappingCollection' AS table_name, 'uuid' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "MappingCollection" 
WHERE "MappingCollection".uuid IS NULL

UNION ALL

SELECT 'MappingCollection' AS table_name, 'metadata' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "MappingCollection" 
WHERE "MappingCollection".metadata IS NULL

UNION ALL

SELECT 'MappingCollection' AS table_name, 'provenance' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "MappingCollection" 
WHERE "MappingCollection".provenance IS NULL

UNION ALL

SELECT 'MappingCollection' AS table_name, 'mappings' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "MappingCollection" 
WHERE "MappingCollection".mappings IS NULL

UNION ALL

SELECT 'MappingProvenance' AS table_name, 'method' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "MappingProvenance" 
WHERE "MappingProvenance".method IS NULL

UNION ALL

SELECT 'MappingProvenance' AS table_name, 'method' AS column_name, 'enum' AS constraint_type, id AS record_id, method AS invalid_value 
FROM "MappingProvenance" 
WHERE "MappingProvenance".method IS NOT NULL AND ("MappingProvenance".method NOT IN ('human', 'automation', 'hybrid'))

UNION ALL

SELECT 'MappingProvenance' AS table_name, 'matching_rationale' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "MappingProvenance" 
WHERE "MappingProvenance".matching_rationale IS NULL

UNION ALL

SELECT 'MappingProvenance' AS table_name, 'matching_rationale' AS column_name, 'enum' AS constraint_type, id AS record_id, matching_rationale AS invalid_value 
FROM "MappingProvenance" 
WHERE "MappingProvenance".matching_rationale IS NOT NULL AND ("MappingProvenance".matching_rationale NOT IN ('syntactic', 'semantic', 'functional'))

UNION ALL

SELECT 'MappingProvenance' AS table_name, 'status' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "MappingProvenance" 
WHERE "MappingProvenance".status IS NULL

UNION ALL

SELECT 'MappingProvenance' AS table_name, 'status' AS column_name, 'enum' AS constraint_type, id AS record_id, status AS invalid_value 
FROM "MappingProvenance" 
WHERE "MappingProvenance".status IS NOT NULL AND ("MappingProvenance".status NOT IN ('complete', 'not-complete', 'draft', 'deprecated', 'superseded'))

UNION ALL

SELECT 'MappingProvenance' AS table_name, 'mapping_description' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "MappingProvenance" 
WHERE "MappingProvenance".mapping_description IS NULL

UNION ALL

SELECT 'Mapping' AS table_name, 'uuid' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Mapping" 
WHERE "Mapping".uuid IS NULL

UNION ALL

SELECT 'Mapping' AS table_name, 'method' AS column_name, 'enum' AS constraint_type, id AS record_id, method AS invalid_value 
FROM "Mapping" 
WHERE "Mapping".method IS NOT NULL AND ("Mapping".method NOT IN ('human', 'automation', 'hybrid'))

UNION ALL

SELECT 'Mapping' AS table_name, 'matching_rationale' AS column_name, 'enum' AS constraint_type, id AS record_id, matching_rationale AS invalid_value 
FROM "Mapping" 
WHERE "Mapping".matching_rationale IS NOT NULL AND ("Mapping".matching_rationale NOT IN ('syntactic', 'semantic', 'functional'))

UNION ALL

SELECT 'Mapping' AS table_name, 'status' AS column_name, 'enum' AS constraint_type, id AS record_id, status AS invalid_value 
FROM "Mapping" 
WHERE "Mapping".status IS NOT NULL AND ("Mapping".status NOT IN ('complete', 'not-complete', 'draft', 'deprecated', 'superseded'))

UNION ALL

SELECT 'Mapping' AS table_name, 'source_resource' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Mapping" 
WHERE "Mapping".source_resource IS NULL

UNION ALL

SELECT 'Mapping' AS table_name, 'target_resource' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Mapping" 
WHERE "Mapping".target_resource IS NULL

UNION ALL

SELECT 'Mapping' AS table_name, 'maps' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Mapping" 
WHERE "Mapping".maps IS NULL

UNION ALL

SELECT 'Map' AS table_name, 'uuid' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Map" 
WHERE "Map".uuid IS NULL

UNION ALL

SELECT 'Map' AS table_name, 'matching_rationale' AS column_name, 'enum' AS constraint_type, id AS record_id, matching_rationale AS invalid_value 
FROM "Map" 
WHERE "Map".matching_rationale IS NOT NULL AND ("Map".matching_rationale NOT IN ('syntactic', 'semantic', 'functional'))

UNION ALL

SELECT 'Map' AS table_name, 'relationship' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Map" 
WHERE "Map".relationship IS NULL

UNION ALL

SELECT 'Map' AS table_name, 'sources' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Map" 
WHERE "Map".sources IS NULL

UNION ALL

SELECT 'Map' AS table_name, 'targets' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Map" 
WHERE "Map".targets IS NULL

UNION ALL

SELECT 'MappingItem' AS table_name, 'type' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "MappingItem" 
WHERE "MappingItem".type IS NULL

UNION ALL

SELECT 'MappingItem' AS table_name, 'type' AS column_name, 'enum' AS constraint_type, id AS record_id, type AS invalid_value 
FROM "MappingItem" 
WHERE "MappingItem".type IS NOT NULL AND ("MappingItem".type NOT IN ('control', 'statement'))

UNION ALL

SELECT 'MappingItem' AS table_name, 'id_ref' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "MappingItem" 
WHERE "MappingItem".id_ref IS NULL

UNION ALL

SELECT 'MappingResourceReference' AS table_name, 'type' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "MappingResourceReference" 
WHERE "MappingResourceReference".type IS NULL

UNION ALL

SELECT 'MappingResourceReference' AS table_name, 'href' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "MappingResourceReference" 
WHERE "MappingResourceReference".href IS NULL

UNION ALL

SELECT 'QualifierItem' AS table_name, 'subject' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "QualifierItem" 
WHERE "QualifierItem".subject IS NULL

UNION ALL

SELECT 'QualifierItem' AS table_name, 'subject' AS column_name, 'enum' AS constraint_type, id AS record_id, subject AS invalid_value 
FROM "QualifierItem" 
WHERE "QualifierItem".subject IS NOT NULL AND ("QualifierItem".subject NOT IN ('source', 'target', 'both'))

UNION ALL

SELECT 'QualifierItem' AS table_name, 'predicate' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "QualifierItem" 
WHERE "QualifierItem".predicate IS NULL

UNION ALL

SELECT 'QualifierItem' AS table_name, 'predicate' AS column_name, 'enum' AS constraint_type, id AS record_id, predicate AS invalid_value 
FROM "QualifierItem" 
WHERE "QualifierItem".predicate IS NOT NULL AND ("QualifierItem".predicate NOT IN ('has-requirement', 'has-incompatibility'))

UNION ALL

SELECT 'QualifierItem' AS table_name, 'category' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "QualifierItem" 
WHERE "QualifierItem".category IS NULL

UNION ALL

SELECT 'QualifierItem' AS table_name, 'category' AS column_name, 'enum' AS constraint_type, id AS record_id, category AS invalid_value 
FROM "QualifierItem" 
WHERE "QualifierItem".category IS NOT NULL AND ("QualifierItem".category NOT IN ('restricted', 'addressable', 'blocked'))

UNION ALL

SELECT 'QualifierItem' AS table_name, 'description' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "QualifierItem" 
WHERE "QualifierItem".description IS NULL

UNION ALL

SELECT 'GapSummary' AS table_name, 'uuid' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "GapSummary" 
WHERE "GapSummary".uuid IS NULL

UNION ALL

SELECT 'GapSummary' AS table_name, 'unmapped_controls' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "GapSummary" 
WHERE "GapSummary".unmapped_controls IS NULL

UNION ALL

SELECT 'ConfidenceScore' AS table_name, 'percentage' AS column_name, 'range' AS constraint_type, id AS record_id, percentage AS invalid_value 
FROM "ConfidenceScore" 
WHERE "ConfidenceScore".percentage < 0 OR "ConfidenceScore".percentage > 1

UNION ALL

SELECT 'Coverage' AS table_name, 'target_coverage' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Coverage" 
WHERE "Coverage".target_coverage IS NULL

UNION ALL

SELECT 'Coverage' AS table_name, 'target_coverage' AS column_name, 'range' AS constraint_type, id AS record_id, target_coverage AS invalid_value 
FROM "Coverage" 
WHERE "Coverage".target_coverage < 0 OR "Coverage".target_coverage > 1

UNION ALL

SELECT 'PoamDocument' AS table_name, 'plan_of_action_and_milestones' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "PoamDocument" 
WHERE "PoamDocument".plan_of_action_and_milestones IS NULL

UNION ALL

SELECT 'PlanOfActionAndMilestones' AS table_name, 'uuid' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "PlanOfActionAndMilestones" 
WHERE "PlanOfActionAndMilestones".uuid IS NULL

UNION ALL

SELECT 'PlanOfActionAndMilestones' AS table_name, 'metadata' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "PlanOfActionAndMilestones" 
WHERE "PlanOfActionAndMilestones".metadata IS NULL

UNION ALL

SELECT 'PlanOfActionAndMilestones' AS table_name, 'poam_items' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "PlanOfActionAndMilestones" 
WHERE "PlanOfActionAndMilestones".poam_items IS NULL

UNION ALL

SELECT 'PoamItem' AS table_name, 'title' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "PoamItem" 
WHERE "PoamItem".title IS NULL

UNION ALL

SELECT 'PoamItem' AS table_name, 'description' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "PoamItem" 
WHERE "PoamItem".description IS NULL

UNION ALL

SELECT 'RelatedFinding' AS table_name, 'finding_uuid' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "RelatedFinding" 
WHERE "RelatedFinding".finding_uuid IS NULL;

