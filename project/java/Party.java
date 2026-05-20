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
  An organization or person, which may be associated with roles or other concepts within the current or linked OSCAL document.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Party  {

  private String uuid;
  private String type;
  private String name;
  private String short-name;
  private List<String> email-addresses;
  private List<TelephoneNumber> telephone-numbers;
  private List<MetadataPartyExternalId> external-ids;
  private List<Address> addresses;
  private List<String> location-uuids;
  private List<String> member-of-organizations;
  private String remarks;
  private List<PartyProperty> props;
  private List<Link> links;


}