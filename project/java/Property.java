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
  An attribute, characteristic, or quality of the containing object expressed as a namespace qualified name/value pair.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Property  {

  private String name;
  private String uuid;
  private URI ns;
  private String value;
  private String class_;
  private String remarks;
  private String group;


}