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
  Defines how the component or capability supports a set of controls.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ControlImplementationSet  {

  private String uuid;
  private URI source;
  private String description;
  private List<SetParameter> set-parameters;
  private List<ImplementedRequirement> implemented-requirements;
  private List<Property> props;
  private List<Link> links;


}