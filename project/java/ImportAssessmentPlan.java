package example;

/* metamodel_version: 1.12.0 */
/* version: 1.2.3 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  Used by assessment-results to import information about the original plan for assessing the system.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ImportAssessmentPlan  {

  private URI href;
  private String remarks;


}