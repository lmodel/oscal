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
  An annotated, markup-based textual element of a control's or catalog group's definition, or a child of another part.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Part  {

  private String id;
  private String name;
  private URI ns;
  private String class_;
  private String title;
  private String prose;
  private List<Part> parts;
  private List<PartProperty> props;
  private List<Link> links;


}