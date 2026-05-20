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
  Identifies the result of an action and/or task that occurred as part of executing an assessment plan or assessment event.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AssessmentLogEntry  {

  private String uuid;
  private String title;
  private String description;
  private ZonedDateTime start;
  private ZonedDateTime end;
  private List<LoggedBy> logged-by;
  private List<RelatedTask> related-tasks;
  private String remarks;
  private List<Property> props;
  private List<Link> links;


}