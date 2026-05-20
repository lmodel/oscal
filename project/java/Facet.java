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
  An individual characteristic that is part of a larger set produced by the same actor.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Facet  {

  private String name;
  private String value;
  private URI system;
  private String remarks;
  private List<Property> props;
  private List<Link> links;


}