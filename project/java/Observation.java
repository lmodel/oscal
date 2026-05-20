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
  Describes an individual observation.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Observation  {

  private String uuid;
  private String title;
  private String description;
  private List<String> methods;
  private List<String> types;
  private List<Origin> origins;
  private List<SubjectReference> subjects;
  private List<RelevantEvidence> relevant-evidence;
  private ZonedDateTime collected;
  private ZonedDateTime expires;
  private String remarks;
  private List<Property> props;
  private List<Link> links;


}