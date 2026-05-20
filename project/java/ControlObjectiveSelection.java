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
  Identifies the control objectives of the assessment.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ControlObjectiveSelection  {

  private String description;
  private IncludeAll include-all;
  private List<SelectObjectiveById> include-objectives;
  private List<SelectObjectiveById> exclude-objectives;
  private String remarks;
  private List<Property> props;
  private List<Link> links;


}