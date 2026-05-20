


```mermaid
 classDiagram
    class Facet
    click Facet href "../Facet"
      OscalCommon <|-- Facet
        click OscalCommon href "../OscalCommon"
      
      Facet : links
        
          
    
        
        
        Facet --> "*" Link : links
        click Link href "../Link"
    

        
      Facet : name
        
      Facet : props
        
          
    
        
        
        Facet --> "*" Property : props
        click Property href "../Property"
    

        
      Facet : remarks
        
      Facet : system
        
      Facet : value
        
      
```
