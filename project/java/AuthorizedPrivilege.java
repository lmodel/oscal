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
  Identifies a specific system privilege held by the user, along with an associated description and/or rationale for the privilege.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AuthorizedPrivilege  {

  private String title;
  private String description;
  private List<String> functions-performed;


}