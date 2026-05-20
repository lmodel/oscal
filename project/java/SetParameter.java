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
  Identifies the parameter that will be set by the enclosed value.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SetParameter  {

  private String param-id;
  private List<String> values;
  private String remarks;


}