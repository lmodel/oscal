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
  Identifies which statements within a control are addressed.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ImplementedControlStatement  {

  private String statement-id;
  private String uuid;
  private String description;
  private String remarks;
  private List<Property> props;
  private List<Link> links;
  private List<ResponsibleRole> responsible-roles;


}