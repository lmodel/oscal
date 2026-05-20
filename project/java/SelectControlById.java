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
  Select a control or controls from an imported control set.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SelectControlById  {

  private String with-child-controls;
  private List<String> with-ids;
  private List<ControlMatching> matching;


}