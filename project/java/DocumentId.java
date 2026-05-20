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
  A document identifier qualified by an identifier scheme.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class DocumentId  {

  private URI scheme;
  private String identifier;


}