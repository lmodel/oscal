


```mermaid
 classDiagram
    class InheritedControlImplementation
    click InheritedControlImplementation href "../InheritedControlImplementation"
      InheritedControlImplementation : description
        
      InheritedControlImplementation : links
        
          
    
        
        
        InheritedControlImplementation --> "*" Link : links
        click Link href "../Link"
    

        
      InheritedControlImplementation : props
        
          
    
        
        
        InheritedControlImplementation --> "*" Property : props
        click Property href "../Property"
    

        
      InheritedControlImplementation : provided_uuid
        
      InheritedControlImplementation : remarks
        
      InheritedControlImplementation : responsible_roles
        
          
    
        
        
        InheritedControlImplementation --> "*" SspByComponentResponsibleRole : responsible_roles
        click SspByComponentResponsibleRole href "../SspByComponentResponsibleRole"
    

        
      InheritedControlImplementation : uuid
        
      
```
