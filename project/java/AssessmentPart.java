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
  A partition of an assessment plan or results or a child of another part.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AssessmentPart  {

  private String uuid;
  private String name;
  private URI ns;
  private String class_;
  private String title;
  private String prose;
  private List<AssessmentPart> parts;
  private List<Property> props;
  private List<Link> links;


}