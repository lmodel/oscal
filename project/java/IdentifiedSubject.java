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
  Used to detail assessment subjects that were identified by this task.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class IdentifiedSubject  {

  private String subject-placeholder-uuid;
  private List<AssessmentSubject> subjects;


}