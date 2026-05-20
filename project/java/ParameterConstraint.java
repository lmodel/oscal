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
  A formal or informal expression of a constraint or test.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ParameterConstraint  {

  private String description;
  private List<ConstraintTest> tests;


}