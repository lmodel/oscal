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
  Identifies an individual activity to be performed as part of a task.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AssociatedActivity  {

  private String activity-uuid;
  private List<AssessmentSubject> subjects;
  private String remarks;
  private List<ResponsibleRole> responsible-roles;
  private List<Property> props;
  private List<Link> links;


}