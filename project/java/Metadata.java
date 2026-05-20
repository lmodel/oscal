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
  Provides information about the containing document, and defines concepts shared across the document.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Metadata  {

  private String title;
  private ZonedDateTime published;
  private ZonedDateTime last-modified;
  private String version;
  private String oscal-version;
  private List<DocumentId> document-ids;
  private List<Revision> revisions;
  private List<Role> roles;
  private List<Location> locations;
  private List<Party> parties;
  private List<Action> actions;
  private String remarks;
  private List<ResponsibleParty> responsible-parties;
  private List<MetadataProperty> props;
  private List<Link> links;


}