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
  A test expression which is expected to be evaluated by a tool.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ConstraintTest  {

  private String remarks;
  private String expression;


}