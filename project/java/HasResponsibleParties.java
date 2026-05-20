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
  Mixin providing the responsible-parties slot for objects that carry party assignments.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class HasResponsibleParties  {

  private List<ResponsibleParty> responsible-parties;


}