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
  A graphic that provides a visual representation the system, or some aspect of it.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Diagram  {

  private String uuid;
  private String description;
  private List<Property> props;
  private List<SspDiagramLink> links;
  private String caption;
  private String remarks;


}