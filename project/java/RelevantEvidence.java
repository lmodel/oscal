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
  Links this observation to relevant evidence.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class RelevantEvidence  {

  private URI href;
  private String description;
  private String remarks;
  private List<Property> props;
  private List<Link> links;


}