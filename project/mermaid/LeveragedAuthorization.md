


```mermaid
 classDiagram
    class LeveragedAuthorization
    click LeveragedAuthorization href "../LeveragedAuthorization"
      LeveragedAuthorization : date_authorized
        
      LeveragedAuthorization : links
        
          
    
        
        
        LeveragedAuthorization --> "*" SspLeveragedAuthorizationLink : links
        click SspLeveragedAuthorizationLink href "../SspLeveragedAuthorizationLink"
    

        
      LeveragedAuthorization : party_uuid
        
      LeveragedAuthorization : props
        
          
    
        
        
        LeveragedAuthorization --> "*" Property : props
        click Property href "../Property"
    

        
      LeveragedAuthorization : remarks
        
      LeveragedAuthorization : title
        
      LeveragedAuthorization : uuid
        
      
```
