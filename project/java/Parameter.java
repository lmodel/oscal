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
  Parameters provide a mechanism for the dynamic assignment of value(s) in a control.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Parameter  {

  private String id;
  private String class_;
  private String depends-on;
  private String label;
  private String usage;
  private List<ParameterConstraint> constraints;
  private List<ParameterGuideline> guidelines;
  private List<String> values;
  private ParameterSelection select;
  private String remarks;
  private List<ParameterProperty> props;
  private List<Link> links;


}