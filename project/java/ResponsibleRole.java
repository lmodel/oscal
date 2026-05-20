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
  A reference to a role with responsibility for performing a function relative to the containing object, optionally associated with a set of persons and/or organizations that perform that role.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ResponsibleRole  {

  private String role-id;
  private List<String> party-uuids;
  private String remarks;
  private List<Property> props;
  private List<Link> links;


}