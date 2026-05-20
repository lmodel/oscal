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
  Contains the characteristics of the system, such as its name, purpose, and security impact level.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SystemCharacteristics  {

  private List<SystemId> system-ids;
  private String system-name;
  private String system-name-short;
  private String description;
  private String date-authorized;
  private String security-sensitivity-level;
  private SystemInformation system-information;
  private SecurityImpactLevel security-impact-level;
  private SystemStatus system-status;
  private AuthorizationBoundary authorization-boundary;
  private NetworkArchitecture network-architecture;
  private DataFlow data-flow;
  private List<SspSystemCharacteristicsResponsibleParty> responsible-parties;
  private String remarks;


}