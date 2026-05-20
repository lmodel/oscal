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
  A resource associated with content in the containing document instance. A resource may be directly included in the document using base64 encoding or may point to one or more equivalent internet resources.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Resource  {

  private String uuid;
  private String title;
  private String description;
  private List<ResourceProperty> props;
  private List<DocumentId> document-ids;
  private String remarks;
  private Citation citation;
  private List<ResourceLink> rlinks;
  private Base64Resource base64;


}