


```mermaid
 classDiagram
    class ProvidedControlImplementation
    click ProvidedControlImplementation href "../ProvidedControlImplementation"
      ProvidedControlImplementation : description
        
      ProvidedControlImplementation : links
        
          
    
        
        
        ProvidedControlImplementation --> "*" Link : links
        click Link href "../Link"
    

        
      ProvidedControlImplementation : props
        
          
    
        
        
        ProvidedControlImplementation --> "*" Property : props
        click Property href "../Property"
    

        
      ProvidedControlImplementation : remarks
        
      ProvidedControlImplementation : responsible_roles
        
          
    
        
        
        ProvidedControlImplementation --> "*" SspByComponentResponsibleRole : responsible_roles
        click SspByComponentResponsibleRole href "../SspByComponentResponsibleRole"
    

        
      ProvidedControlImplementation : uuid
        
      
```
