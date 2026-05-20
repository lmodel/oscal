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
  An OSCAL Profile that designates a set of controls from one or more catalogs or profiles, optionally restructures and modifies them, to describe a basis for a security standard or body of practice.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Profile  {

  private String uuid;
  private Metadata metadata;
  private List<ProfileImport> imports;
  private ProfileMerge merge;
  private ProfileModify modify;
  private BackMatter back-matter;


}