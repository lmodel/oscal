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
  A collection of resources that may be referenced from within the OSCAL document instance.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class BackMatter  {

  private List<Resource> resources;


}