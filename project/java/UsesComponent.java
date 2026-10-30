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
  The set of components that are used by the assessment platform.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class UsesComponent  {

  private String component-uuid;
  private String remarks;
  private List<ResponsibleParty> responsible-parties;
  private List<Property> props;
  private List<Link> links;


}