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
  The set of components that are implemented in a given system inventory item.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ImplementedComponent  {

  private String component-uuid;
  private String remarks;
  private List<ImplementationResponsibleParty> responsible-parties;
  private List<ImplementationCommonProperty> props;
  private List<ImplementationCommonLink> links;


}