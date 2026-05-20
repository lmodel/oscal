


```mermaid
 classDiagram
    class ResourceLink
    click ResourceLink href "../ResourceLink"
      ResourceLink : hashes
        
          
    
        
        
        ResourceLink --> "*" Hash : hashes
        click Hash href "../Hash"
    

        
      ResourceLink : href
        
      ResourceLink : media_type
        
      
```
