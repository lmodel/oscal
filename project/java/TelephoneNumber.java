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
  A telephone service number as defined by ITU-T E.164.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class TelephoneNumber  {

  private String type;
  private String number;


}