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
  A structured, organized collection of control information.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Catalog  {

  private String uuid;
  private Metadata metadata;
  private BackMatter back-matter;
  private List<Parameter> params;
  private List<Control> controls;
  private List<Group> groups;


}