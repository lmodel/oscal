package None;

/* metamodel_version: 1.11.0 */
/* version: 1.2.1 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A collection of component descriptions, which may optionally be grouped by capability.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ComponentDefinition  {

  private String uuid;
  private Metadata metadata;
  private List<ImportComponentDefinition> import-component-definitions;
  private List<DefinedComponent> components;
  private List<Capability> capabilities;
  private BackMatter back-matter;


}