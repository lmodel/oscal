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
  A collection of control mappings between source and target resources.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class MappingCollection  {

  private String uuid;
  private Metadata metadata;
  private MappingProvenance provenance;
  private List<Mapping> mappings;
  private BackMatter back-matter;


}