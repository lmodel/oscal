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
  An identifier for a person or organization using a designated scheme, e.g. an Open Researcher and Contributor ID (ORCID).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PartyExternalId  {

  private URI scheme;
  private String id;


}