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
  A relationship-based mapping entry between source and target sets.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Map  {

  private String uuid;
  private URI ns;
  private String matching-rationale;
  private String relationship;
  private List<MappingItem> sources;
  private List<MappingItem> targets;
  private List<QualifierItem> qualifiers;
  private ConfidenceScore confidence-score;
  private Coverage coverage;
  private String remarks;
  private List<Property> props;
  private List<Link> links;


}