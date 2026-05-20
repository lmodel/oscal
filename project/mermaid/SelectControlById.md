


```mermaid
 classDiagram
    class SelectControlById
    click SelectControlById href "../SelectControlById"
      SelectControlById : matching
        
          
    
        
        
        SelectControlById --> "*" ControlMatching : matching
        click ControlMatching href "../ControlMatching"
    

        
      SelectControlById : with_child_controls
        
          
    
        
        
        SelectControlById --> "0..1" WithChildControlsEnum : with_child_controls
        click WithChildControlsEnum href "../WithChildControlsEnum"
    

        
      SelectControlById : with_ids
        
      
```
