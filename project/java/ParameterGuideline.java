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
  A prose statement that provides a recommendation for the use of a parameter.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ParameterGuideline  {

  private String prose;


}