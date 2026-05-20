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
  Captures an assessor's conclusions regarding the degree to which an objective is satisfied.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class FindingTarget  {

  private String type;
  private String target-id;
  private String title;
  private String description;
  private ImplementationStatus implementation-status;
  private ObjectiveStatus status;
  private String remarks;
  private List<Property> props;
  private List<Link> links;


}