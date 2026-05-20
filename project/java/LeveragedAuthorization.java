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
  A description of another authorized system from which this system inherits capabilities that satisfy security requirements. Another term for this concept is a common control provider.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class LeveragedAuthorization  {

  private String uuid;
  private String title;
  private List<Property> props;
  private List<SspLeveragedAuthorizationLink> links;
  private String party-uuid;
  private String date-authorized;
  private String remarks;


}