


```mermaid
 classDiagram
    class ProfileImport
    click ProfileImport href "../ProfileImport"
      ProfileImport : exclude_controls
        
          
    
        
        
        ProfileImport --> "*" SelectControlById : exclude_controls
        click SelectControlById href "../SelectControlById"
    

        
      ProfileImport : href
        
      ProfileImport : include_all
        
          
    
        
        
        ProfileImport --> "0..1" IncludeAll : include_all
        click IncludeAll href "../IncludeAll"
    

        
      ProfileImport : include_controls
        
          
    
        
        
        ProfileImport --> "*" SelectControlById : include_controls
        click SelectControlById href "../SelectControlById"
    

        
      
```
