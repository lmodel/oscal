


```mermaid
 classDiagram
    class SspDocument
    click SspDocument href "../SspDocument"
      OscalDocument <|-- SspDocument
        click OscalDocument href "../OscalDocument"
      
      SspDocument : system_security_plan
        
          
    
        
        
        SspDocument --> "1" SystemSecurityPlan : system_security_plan
        click SystemSecurityPlan href "../SystemSecurityPlan"
    

        
      
```
