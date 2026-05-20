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
  Used to define data objects that are referenced by the assessment results but do not appear in the imported assessment plan.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AssessmentResultsLocalDefinitions  {

  private List<LocalObjective> objectives-and-methods;
  private List<Activity> activities;
  private String remarks;


}