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
  Provides an alternate grouping structure that selected controls will be placed in after profile resolution.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class MergeCustom  {

  private List<ProfileGroup> groups;
  private List<InsertControls> insert-controls;


}