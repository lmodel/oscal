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
  Identifies the assets used to perform this assessment.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AssessmentAssets  {

  private List<SystemComponent> components;
  private List<AssessmentPlatform> assessment-platforms;


}