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
  A grouping of other components and/or capabilities.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Capability  {

  private String uuid;
  private String name;
  private String description;
  private List<IncorporatesComponent> incorporates-components;
  private List<ControlImplementationSet> control-implementations;
  private String remarks;
  private List<Property> props;
  private List<Link> links;


}