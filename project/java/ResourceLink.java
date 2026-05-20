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
  A URL-based pointer to an external resource with an optional hash for verification and change detection.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ResourceLink  {

  private URI href;
  private String media-type;
  private List<Hash> hashes;


}