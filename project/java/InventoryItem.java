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
  A single managed inventory item within the system.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class InventoryItem  {

  private String uuid;
  private String description;
  private List<ImplementedComponent> implemented-components;
  private String remarks;
  private List<ImplementationResponsibleParty> responsible-parties;
  private List<ImplementationCommonProperty> props;
  private List<ImplementationCommonLink> links;


}