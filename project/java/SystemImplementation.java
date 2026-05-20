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
  Provides information as to how the system is implemented.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SystemImplementation  {

  private List<Property> props;
  private List<Link> links;
  private List<LeveragedAuthorization> leveraged-authorizations;
  private List<SystemUser> users;
  private List<SspSystemComponent> components;
  private List<SspInventoryItem> inventory-items;
  private String remarks;


}