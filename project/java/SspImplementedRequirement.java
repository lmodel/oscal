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
  Describes how the system satisfies an individual control.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SspImplementedRequirement  {

  private String uuid;
  private String control-id;
  private List<SspControlOriginationProp> props;
  private List<Link> links;
  private List<SetParameter> set-parameters;
  private List<SspImplementedRequirementResponsibleRole> responsible-roles;
  private List<SspStatement> statements;
  private List<ByComponent> by-components;
  private String remarks;


}