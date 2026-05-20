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
  Contains details about all information types that are stored, processed, or transmitted by the system, such as privacy information.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SystemInformation  {

  private List<SspSystemInformationProp> props;
  private List<SspSystemInformationLink> links;
  private List<InformationType> information-types;


}