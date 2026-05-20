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
  Defines how the referenced component implements a set of controls.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ByComponent  {

  private String component-uuid;
  private String uuid;
  private String description;
  private List<SspControlOriginationProp> props;
  private List<SspByComponentLink> links;
  private List<SetParameter> set-parameters;
  private ImplementationStatus implementation-status;
  private Export export;
  private List<InheritedControlImplementation> inherited;
  private List<SatisfiedControlImplementation> satisfied;
  private List<SspByComponentResponsibleRole> responsible-roles;
  private String remarks;


}