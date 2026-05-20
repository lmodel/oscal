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
  Mapping-level provenance details and mapping defaults.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class MappingProvenance  {

  private String method;
  private String matching-rationale;
  private String status;
  private ConfidenceScore confidence-score;
  private Coverage coverage;
  private String mapping-description;
  private String remarks;
  private List<ResponsibleParty> responsible-parties;
  private List<Property> props;
  private List<Link> links;


}