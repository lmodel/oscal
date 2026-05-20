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
  A parameter setting to be propagated to points of insertion in a resolved profile.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ParameterSetting  {

  private String param-id;
  private String class_;
  private String depends-on;
  private String label;
  private String usage;
  private List<ParameterConstraint> constraints;
  private List<ParameterGuideline> guidelines;
  private List<String> values;
  private ParameterSelection select;
  private List<Property> props;
  private List<Link> links;


}