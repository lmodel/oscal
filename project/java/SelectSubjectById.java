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
  Identifies a set of assessment subjects to include/exclude by UUID.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SelectSubjectById  {

  private String subject-uuid;
  private String type;
  private String remarks;
  private List<Property> props;
  private List<Link> links;


}