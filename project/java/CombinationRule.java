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
  Defines how to resolve duplicate instances of the same control (e.g., controls with the same ID) encountered in a profile merge.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CombinationRule  {

  private String method;


}