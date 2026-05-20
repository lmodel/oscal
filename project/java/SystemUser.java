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
  A type of user that interacts with the system based on an associated role.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SystemUser  {

  private String uuid;
  private String title;
  private String short-name;
  private String description;
  private List<String> role-ids;
  private List<AuthorizedPrivilege> authorized-privileges;
  private String remarks;
  private List<ImplementationCommonProperty> props;
  private List<ImplementationCommonLink> links;


}