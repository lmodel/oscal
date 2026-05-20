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
  An action applied by a role within a given party to the content.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Action  {

  private String uuid;
  private String type;
  private ZonedDateTime date;
  private URI system;
  private String remarks;
  private List<ResponsibleParty> responsible-parties;
  private List<Property> props;
  private List<Link> links;


}