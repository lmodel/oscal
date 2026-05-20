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
  Mixin providing props, links, and remarks slots common to most OSCAL objects. Extends HasPropsAndLinks.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OscalCommon  {

  private String remarks;
  private List<Property> props;
  private List<Link> links;


}