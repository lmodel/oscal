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
  Describes a control implementation responsibility imposed on a leveraging system.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ControlResponsibility  {

  private String uuid;
  private String provided-uuid;
  private String description;
  private List<Property> props;
  private List<Link> links;
  private List<SspByComponentResponsibleRole> responsible-roles;
  private String remarks;


}