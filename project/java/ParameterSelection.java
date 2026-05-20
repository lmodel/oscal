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
  Presenting a choice among alternatives.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ParameterSelection  {

  private String how-many;
  private List<String> choice;


}