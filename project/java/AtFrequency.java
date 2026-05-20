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
  The task is intended to occur at the specified frequency.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AtFrequency  {

  private String period;
  private String unit;
  private String remarks;


}