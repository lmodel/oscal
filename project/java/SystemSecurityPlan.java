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
  A system security plan, such as those described in NIST SP 800-18.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SystemSecurityPlan  {

  private String uuid;
  private Metadata metadata;
  private ImportProfile import-profile;
  private SystemCharacteristics system-characteristics;
  private SystemImplementation system-implementation;
  private SspControlImplementation control-implementation;
  private BackMatter back-matter;


}