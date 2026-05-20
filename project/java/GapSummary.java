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
  A summary of controls that were not mapped.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class GapSummary  {

  private String uuid;
  private List<SelectControlById> unmapped-controls;


}