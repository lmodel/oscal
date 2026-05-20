


```mermaid
 classDiagram
    class ImpactLevel
    click ImpactLevel href "../ImpactLevel"
      ImpactLevel : adjustment_justification
        
      ImpactLevel : base
        
      ImpactLevel : links
        
          
    
        
        
        ImpactLevel --> "*" Link : links
        click Link href "../Link"
    

        
      ImpactLevel : props
        
          
    
        
        
        ImpactLevel --> "*" Property : props
        click Property href "../Property"
    

        
      ImpactLevel : selected
        
      
```
