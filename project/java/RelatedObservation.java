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
  Relates the identified element to a set of referenced observations.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class RelatedObservation  {

  private String observation-uuid;
  private String remarks;


}