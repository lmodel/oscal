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
  Used to define various terms and conditions under which an assessment can be performed.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class TermsAndConditions  {

  private List<TermsAndConditionsPart> parts;


}