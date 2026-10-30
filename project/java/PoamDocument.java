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
  Root wrapper for an OSCAL Plan of Action and Milestones document.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PoamDocument extends OscalDocument {

  private PlanOfActionAndMilestones plan-of-action-and-milestones;


}