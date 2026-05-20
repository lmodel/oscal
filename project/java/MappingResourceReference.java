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
  A reference to the source or target resource for a mapping.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class MappingResourceReference  {

  private URI ns;
  private String type;
  private URI href;
  private String remarks;
  private List<Property> props;
  private List<Link> links;


}