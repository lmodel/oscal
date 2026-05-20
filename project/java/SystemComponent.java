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
  A defined component that can be part of an implemented system.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SystemComponent  {

  private String uuid;
  private String type;
  private String title;
  private String description;
  private String purpose;
  private List<Protocol> protocols;
  private ComponentStatus status;
  private String remarks;
  private List<ImplementationResponsibleRole> responsible-roles;
  private List<ImplementationCommonProperty> props;
  private List<ImplementationCommonLink> links;


}