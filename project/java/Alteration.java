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
  Specifies changes to be made to an included control when a profile is resolved.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Alteration  {

  private String control-id;
  private List<Removal> removes;
  private List<Addition> adds;


}