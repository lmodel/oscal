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
  Used to define local implementation and assessment assets referenced by a result that do not appear in the imported system security plan.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ResultLocalDefinitions  {

  private List<SystemComponent> components;
  private List<InventoryItem> inventory-items;
  private List<SystemUser> users;
  private AssessmentAssets assessment-assets;
  private List<Task> tasks;


}