


```mermaid
 classDiagram
    class ParameterSelection
    click ParameterSelection href "../ParameterSelection"
      ParameterSelection : choice
        
      ParameterSelection : how_many
        
          
    
        
        
        ParameterSelection --> "0..1" ParameterCardinalityEnum : how_many
        click ParameterCardinalityEnum href "../ParameterCardinalityEnum"
    

        
      
```
