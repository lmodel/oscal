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
  Select a specific control for inclusion/exclusion in the assessment by literal control ID and optional statement IDs.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AssessmentSelectControlById  {

  private String control-id;
  private List<String> statement-ids;


}