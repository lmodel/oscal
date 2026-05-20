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
  Describes how the system satisfies a set of controls.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SspControlImplementation  {

  private String description;
  private List<SetParameter> set-parameters;
  private List<SspImplementedRequirement> implemented-requirements;


}