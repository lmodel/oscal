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
  A group of controls, or of groups of controls.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Group  {

  private String id;
  private String class_;
  private String title;
  private List<Parameter> params;
  private List<Part> parts;
  private List<Group> groups;
  private List<Control> controls;
  private List<Property> props;
  private List<Link> links;


}