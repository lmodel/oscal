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
  Defines a function, which might be assigned to a party in a specific situation.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Role  {

  private String id;
  private String title;
  private String short-name;
  private String description;
  private String remarks;
  private List<Property> props;
  private List<Link> links;


}