


```mermaid
 classDiagram
    class InsertControls
    click InsertControls href "../InsertControls"
      InsertControls : exclude_controls
        
          
    
        
        
        InsertControls --> "*" SelectControlById : exclude_controls
        click SelectControlById href "../SelectControlById"
    

        
      InsertControls : include_all
        
          
    
        
        
        InsertControls --> "0..1" IncludeAll : include_all
        click IncludeAll href "../IncludeAll"
    

        
      InsertControls : include_controls
        
          
    
        
        
        InsertControls --> "*" SelectControlById : include_controls
        click SelectControlById href "../SelectControlById"
    

        
      InsertControls : order
        
          
    
        
        
        InsertControls --> "0..1" InsertOrderEnum : order
        click InsertOrderEnum href "../InsertOrderEnum"
    

        
      
```
