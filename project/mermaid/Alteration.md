


```mermaid
 classDiagram
    class Alteration
    click Alteration href "../Alteration"
      Alteration : adds
        
          
    
        
        
        Alteration --> "*" Addition : adds
        click Addition href "../Addition"
    

        
      Alteration : control_id
        
      Alteration : removes
        
          
    
        
        
        Alteration --> "*" Removal : removes
        click Removal href "../Removal"
    

        
      
```
