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
  Provides structuring directives that instruct how controls are organized after profile resolution.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ProfileMerge  {

  private CombinationRule combine;
  private MergeFlat flat;
  private Boolean as-is;
  private MergeCustom custom;


}