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
  A pointer, by ID, to an externally-defined threat.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ThreatId  {

  private URI href;
  private URI system;
  private URI id;


}