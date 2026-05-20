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
  A plan of action and milestones that identifies initial and residual risks, deviations, and disposition.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PlanOfActionAndMilestones  {

  private String uuid;
  private Metadata metadata;
  private ImportSSP import-ssp;
  private SystemId system-id;
  private PoamLocalDefinitions local-definitions;
  private List<Observation> observations;
  private List<Risk> risks;
  private List<Finding> findings;
  private List<PoamItem> poam-items;
  private BackMatter back-matter;


}