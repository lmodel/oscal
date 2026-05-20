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
  A collection of descriptive data about the containing object from a specific origin.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Characterization  {

  private Origin origin;
  private List<Facet> facets;
  private List<Property> props;
  private List<Link> links;


}