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
  A representation of a cryptographic digest generated over a resource using a specified hash algorithm.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Hash  {

  private String value;
  private String algorithm;


}