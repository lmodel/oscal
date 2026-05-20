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
  Identifies an individual step in a series of steps related to an activity, such as an assessment test or examination procedure.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Step  {

  private String uuid;
  private String title;
  private String description;
  private ReviewedControls reviewed-controls;
  private String remarks;
  private List<ResponsibleRole> responsible-roles;
  private List<Property> props;
  private List<Link> links;


}