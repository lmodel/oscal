package example;

/* metamodel_version: 1.12.0 */
/* version: 1.2.3 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A percentage representing target coverage by source mappings.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Coverage  {

  private String generation-method;
  private float target-coverage;


}