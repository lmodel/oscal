


```mermaid
 classDiagram
    class Origin
    click Origin href "../Origin"
      Origin : actors
        
          
    
        
        
        Origin --> "1..*" OriginActor : actors
        click OriginActor href "../OriginActor"
    

        
      Origin : related_tasks
        
          
    
        
        
        Origin --> "*" RelatedTask : related_tasks
        click RelatedTask href "../RelatedTask"
    

        
      
```
