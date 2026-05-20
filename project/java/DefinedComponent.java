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
public class DefinedComponent  {

  private String uuid;
  private String type;
  private String title;
  private String description;
  private String purpose;
  private List<Protocol> protocols;
  private List<ControlImplementationSet> control-implementations;
  private String remarks;
  private List<ResponsibleRole> responsible-roles;
  private List<Property> props;
  private List<Link> links;


}