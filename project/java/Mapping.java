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
  A mapping between two mapped resources.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Mapping  {

  private String uuid;
  private String method;
  private String matching-rationale;
  private String status;
  private MappingResourceReference source-resource;
  private MappingResourceReference target-resource;
  private List<Map> maps;
  private String mapping-description;
  private GapSummary source-gap-summary;
  private GapSummary target-gap-summary;
  private ConfidenceScore confidence-score;
  private Coverage coverage;
  private String remarks;
  private List<Property> props;
  private List<Link> links;


}