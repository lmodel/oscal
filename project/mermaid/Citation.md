


```mermaid
 classDiagram
    class Citation
    click Citation href "../Citation"
      HasPropsAndLinks <|-- Citation
        click HasPropsAndLinks href "../HasPropsAndLinks"
      
      Citation : links
        
          
    
        
        
        Citation --> "*" Link : links
        click Link href "../Link"
    

        
      Citation : props
        
          
    
        
        
        Citation --> "*" Property : props
        click Property href "../Property"
    

        
      Citation : text
        
      
```
