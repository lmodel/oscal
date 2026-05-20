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
  The expected level of impact resulting from the described information's confidentiality, integrity, or availability affect.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ImpactLevel  {

  private List<Property> props;
  private List<Link> links;
  private String base;
  private String selected;
  private String adjustment-justification;


}