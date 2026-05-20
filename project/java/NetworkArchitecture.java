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
  A description of the system's network architecture, optionally supplemented with diagrams that illustrate the network architecture.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class NetworkArchitecture  {

  private String description;
  private List<Property> props;
  private List<Link> links;
  private List<Diagram> diagrams;
  private String remarks;


}