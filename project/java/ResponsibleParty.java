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
  A reference to a set of persons and/or organizations that have responsibility for performing the referenced role in the context of the containing object.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ResponsibleParty  {

  private String role-id;
  private List<String> party-uuids;
  private String remarks;
  private List<Property> props;
  private List<Link> links;


}