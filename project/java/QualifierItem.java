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
  A qualifier describing requirements or incompatibilities.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class QualifierItem  {

  private String subject;
  private String predicate;
  private String category;
  private String description;
  private String remarks;


}