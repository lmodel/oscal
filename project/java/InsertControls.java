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
  Specifies which controls to use in the containing context (as part of a group or custom merge structure).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class InsertControls  {

  private String order;
  private IncludeAll include-all;
  private List<SelectControlById> include-controls;
  private List<SelectControlById> exclude-controls;


}