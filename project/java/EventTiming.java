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
  The timing under which the task is intended to occur.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class EventTiming  {

  private OnDateCondition on-date;
  private WithinDateRange within-date-range;
  private AtFrequency at-frequency;


}