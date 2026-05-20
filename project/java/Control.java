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
  A structured object representing a requirement or guideline, which when implemented will reduce an aspect of risk related to an information system and its information.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Control  {

  private String id;
  private String class_;
  private String title;
  private List<Parameter> params;
  private List<Part> parts;
  private List<Control> controls;
  private List<Property> props;
  private List<Link> links;


}