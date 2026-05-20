


```mermaid
 classDiagram
    class ProfileDocument
    click ProfileDocument href "../ProfileDocument"
      OscalDocument <|-- ProfileDocument
        click OscalDocument href "../OscalDocument"
      
      ProfileDocument : profile
        
          
    
        
        
        ProfileDocument --> "1" Profile : profile
        click Profile href "../Profile"
    

        
      
```
