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
  A reference to a local or remote resource, that has a specific relation to the containing object.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Link  {

  private URI href;
  private String rel;
  private String resource-fragment;
  private String media-type;
  private String text;


}