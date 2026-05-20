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
  A physical point of presence, which may be associated with people, organizations, or other concepts within the current or linked OSCAL document.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Location  {

  private String uuid;
  private String title;
  private List<String> email-addresses;
  private List<TelephoneNumber> telephone-numbers;
  private Address address;
  private List<URI> urls;
  private String remarks;
  private List<LocationProperty> props;
  private List<Link> links;


}