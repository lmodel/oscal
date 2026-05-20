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
  Specifies content to be added into controls in resolution.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Addition  {

  private String position;
  private String by-id;
  private String title;
  private List<Parameter> params;
  private List<ProfileAlterationProperty> props;
  private List<Link> links;
  private List<Part> parts;


}