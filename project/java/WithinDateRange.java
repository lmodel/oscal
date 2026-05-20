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
  The task is intended to occur within the specified date range.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class WithinDateRange  {

  private ZonedDateTime start;
  private ZonedDateTime end;
  private String remarks;


}