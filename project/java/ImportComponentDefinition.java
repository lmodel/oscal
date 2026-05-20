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
  Loads a component definition from another resource.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ImportComponentDefinition  {

  private URI href;
  private String remarks;


}