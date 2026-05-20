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
  A resource encoded using the Base64 alphabet defined by RFC 2045.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Base64Resource  {

  private String media-type;
  private String value;
  private String filename;


}