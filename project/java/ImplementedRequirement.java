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
  Describes how the containing component or capability implements an individual control.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ImplementedRequirement  {

  private String uuid;
  private String control-id;
  private String description;
  private List<SetParameter> set-parameters;
  private List<ImplementedControlStatement> statements;
  private String remarks;
  private List<Property> props;
  private List<Link> links;
  private List<ResponsibleRole> responsible-roles;


}