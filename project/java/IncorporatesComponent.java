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
  The collection of components comprising a capability.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class IncorporatesComponent  {

  private String component-uuid;
  private String description;


}