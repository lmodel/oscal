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
  Identifies all of the assessment observations and findings, initial and residual risks, deviations, and disposition for a particular execution of the assessment.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Result  {

  private String uuid;
  private String title;
  private String description;
  private ZonedDateTime start;
  private ZonedDateTime end;
  private ResultLocalDefinitions local-definitions;
  private ReviewedControls reviewed-controls;
  private List<Attestation> attestations;
  private AssessmentLog assessment-log;
  private List<Observation> observations;
  private List<Risk> risks;
  private List<Finding> findings;
  private String remarks;
  private List<Property> props;
  private List<Link> links;


}