package example;

/* metamodel_version: 1.12.0 */
/* version: 1.2.3 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A set of information type identifiers qualified by the given identification system used.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class InformationTypeCategorization  {

  private String system;
  private List<String> information-type-ids;


}