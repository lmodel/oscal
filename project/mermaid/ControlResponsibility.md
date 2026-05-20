


```mermaid
 classDiagram
    class ControlResponsibility
    click ControlResponsibility href "../ControlResponsibility"
      ControlResponsibility : description
        
      ControlResponsibility : links
        
          
    
        
        
        ControlResponsibility --> "*" Link : links
        click Link href "../Link"
    

        
      ControlResponsibility : props
        
          
    
        
        
        ControlResponsibility --> "*" Property : props
        click Property href "../Property"
    

        
      ControlResponsibility : provided_uuid
        
      ControlResponsibility : remarks
        
      ControlResponsibility : responsible_roles
        
          
    
        
        
        ControlResponsibility --> "*" SspByComponentResponsibleRole : responsible_roles
        click SspByComponentResponsibleRole href "../SspByComponentResponsibleRole"
    

        
      ControlResponsibility : uuid
        
      
```
