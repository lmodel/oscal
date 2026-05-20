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
  Identifies which statements within a control are addressed.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SspStatement  {

  private String statement-id;
  private String uuid;
  private List<SspControlOriginationProp> props;
  private List<Link> links;
  private List<SspImplementedRequirementResponsibleRole> responsible-roles;
  private List<ByComponent> by-components;
  private String remarks;


}