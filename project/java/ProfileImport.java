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
  Designates a referenced source catalog or profile that provides a source of control information for use in creating a new overlay or baseline.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ProfileImport  {

  private URI href;
  private IncludeAll include-all;
  private List<SelectControlById> include-controls;
  private List<SelectControlById> exclude-controls;


}