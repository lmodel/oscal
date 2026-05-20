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
  Used to select a control objective for inclusion/exclusion.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SelectObjectiveById  {

  private String objective-id;
  private String remarks;


}