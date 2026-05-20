


```mermaid
 classDiagram
    class DataFlow
    click DataFlow href "../DataFlow"
      DataFlow : description
        
      DataFlow : diagrams
        
          
    
        
        
        DataFlow --> "*" Diagram : diagrams
        click Diagram href "../Diagram"
    

        
      DataFlow : links
        
          
    
        
        
        DataFlow --> "*" Link : links
        click Link href "../Link"
    

        
      DataFlow : props
        
          
    
        
        
        DataFlow --> "*" Property : props
        click Property href "../Property"
    

        
      DataFlow : remarks
        
      
```
