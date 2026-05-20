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
  Allows components and inventory items to be defined within the POA&M for cases where no OSCAL SSP is available with the POA&M.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PoamLocalDefinitions  {

  private List<SystemComponent> components;
  private List<InventoryItem> inventory-items;
  private AssessmentAssets assessment-assets;
  private String remarks;


}