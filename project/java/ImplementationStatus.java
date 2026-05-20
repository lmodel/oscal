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
  Indicates the degree to which a given control is implemented.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ImplementationStatus  {

  private String state;
  private String remarks;


}