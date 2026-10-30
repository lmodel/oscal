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
  A postal address for the location.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Address  {

  private String type;
  private List<String> addr-lines;
  private String city;
  private String state;
  private String postal-code;
  private String country;


}