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
  Root wrapper for an OSCAL Assessment Plan document.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AssessmentPlanDocument extends OscalDocument {

  private AssessmentPlan assessment-plan;


}