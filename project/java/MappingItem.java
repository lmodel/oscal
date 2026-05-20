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
  A source or target item participating in a mapping entry.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class MappingItem  {

  private String type;
  private String id-ref;
  private String remarks;
  private List<Property> props;
  private List<Link> links;


}