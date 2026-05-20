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
  A determination of if the objective is satisfied or not within a given system.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ObjectiveStatus  {

  private String state;
  private String reason;
  private String remarks;


}