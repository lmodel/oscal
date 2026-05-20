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
  Describes the operational status of the system component.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ComponentStatus  {

  private String state;
  private String remarks;


}