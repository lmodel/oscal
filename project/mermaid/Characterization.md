


```mermaid
 classDiagram
    class Characterization
    click Characterization href "../Characterization"
      HasPropsAndLinks <|-- Characterization
        click HasPropsAndLinks href "../HasPropsAndLinks"
      
      Characterization : facets
        
          
    
        
        
        Characterization --> "1..*" Facet : facets
        click Facet href "../Facet"
    

        
      Characterization : links
        
          
    
        
        
        Characterization --> "*" Link : links
        click Link href "../Link"
    

        
      Characterization : origin
        
          
    
        
        
        Characterization --> "1" Origin : origin
        click Origin href "../Origin"
    

        
      Characterization : props
        
          
    
        
        
        Characterization --> "*" Property : props
        click Property href "../Property"
    

        
      
```
