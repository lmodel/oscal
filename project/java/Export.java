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
  Defines a set of control implementations that are provided as reference implementations for use by organizations implementing the leveraged system.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Export  {

  private String description;
  private List<Property> props;
  private List<Link> links;
  private List<ProvidedControlImplementation> provided;
  private List<ControlResponsibility> responsibilities;


}