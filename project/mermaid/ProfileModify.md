


```mermaid
 classDiagram
    class ProfileModify
    click ProfileModify href "../ProfileModify"
      ProfileModify : alters
        
          
    
        
        
        ProfileModify --> "*" Alteration : alters
        click Alteration href "../Alteration"
    

        
      ProfileModify : set_parameters
        
          
    
        
        
        ProfileModify --> "*" ParameterSetting : set_parameters
        click ParameterSetting href "../ParameterSetting"
    

        
      
```
