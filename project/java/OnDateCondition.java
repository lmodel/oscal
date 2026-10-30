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
  The task is intended to occur on the specified date.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OnDateCondition  {

  private ZonedDateTime date;
  private String remarks;


}