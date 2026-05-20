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
  An optional citation consisting of end note text using structured markup.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Citation  {

  private String text;
  private List<Property> props;
  private List<Link> links;


}