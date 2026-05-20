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
  Specifies objects to be removed from a control based on aspects of the object that must all match.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Removal  {

  private String by-name;
  private String by-class;
  private String by-id;
  private String by-item-name;
  private URI by-ns;
  private String remarks;


}