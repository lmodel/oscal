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
  Security assessment results, such as those provided by a FedRAMP assessor in a security assessment report.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AssessmentResults  {

  private String uuid;
  private Metadata metadata;
  private ImportAssessmentPlan import-ap;
  private AssessmentResultsLocalDefinitions local-definitions;
  private List<Result> results;
  private BackMatter back-matter;


}