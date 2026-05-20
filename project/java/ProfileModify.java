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
  Set parameters or amend controls in resolution.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ProfileModify  {

  private List<ParameterSetting> set-parameters;
  private List<Alteration> alters;


}