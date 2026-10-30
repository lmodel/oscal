package example;

/* metamodel_version: 1.12.0 */
/* version: 1.2.3 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  Mixin providing the responsible-roles slot for objects that carry role assignments.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class HasResponsibleRoles  {

  private List<ResponsibleRole> responsible-roles;


}