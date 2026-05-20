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
  Contains details about one information type that is stored, processed, or transmitted by the system, such as privacy information, and its impact level.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class InformationType  {

  private String uuid;
  private String title;
  private String description;
  private List<InformationTypeCategorization> categorizations;
  private List<Property> props;
  private List<Link> links;
  private ImpactLevel confidentiality-impact;
  private ImpactLevel integrity-impact;
  private ImpactLevel availability-impact;


}