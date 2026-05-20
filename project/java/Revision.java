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
  An entry in a sequential list of revisions to the containing document.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Revision  {

  private String title;
  private ZonedDateTime published;
  private ZonedDateTime last-modified;
  private String version;
  private String oscal-version;
  private String remarks;
  private List<RevisionProperty> props;
  private List<Link> links;


}