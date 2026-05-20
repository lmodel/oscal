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
  Describes an individual POA&M item.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PoamItem  {

  private String uuid;
  private String title;
  private String description;
  private List<Origin> origins;
  private List<RelatedFinding> related-findings;
  private List<RelatedObservation> related-observations;
  private List<AssociatedRisk> related-risks;
  private String remarks;
  private List<Property> props;
  private List<Link> links;


}