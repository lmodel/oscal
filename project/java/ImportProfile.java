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
  Used to import the OSCAL profile representing the system's control baseline.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ImportProfile  {

  private URI href;
  private String remarks;


}