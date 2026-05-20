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
  The overall level of expected impact resulting from unauthorized disclosure, modification, or loss of access to information.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SecurityImpactLevel  {

  private String security-objective-confidentiality;
  private String security-objective-integrity;
  private String security-objective-availability;


}