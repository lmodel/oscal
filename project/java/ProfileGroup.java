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
  A group of (selected) controls or of groups of controls within a profile custom merge structure.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ProfileGroup  {

  private String id;
  private String class_;
  private String title;
  private List<Parameter> params;
  private List<Part> parts;
  private List<ProfileGroup> groups;
  private List<InsertControls> insert-controls;
  private String remarks;
  private List<Property> props;
  private List<Link> links;


}