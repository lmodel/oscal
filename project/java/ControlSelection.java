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
  Identifies the controls being assessed.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ControlSelection  {

  private String description;
  private IncludeAll include-all;
  private List<AssessmentSelectControlById> include-controls;
  private List<AssessmentSelectControlById> exclude-controls;
  private String remarks;
  private List<Property> props;
  private List<Link> links;


}