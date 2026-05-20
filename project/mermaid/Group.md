


```mermaid
 classDiagram
    class Group
    click Group href "../Group"
      HasPropsAndLinks <|-- Group
        click HasPropsAndLinks href "../HasPropsAndLinks"
      
      Group : _class
        
      Group : controls
        
          
    
        
        
        Group --> "*" Control : controls
        click Control href "../Control"
    

        
      Group : groups
        
          
    
        
        
        Group --> "*" Group : groups
        click Group href "../Group"
    

        
      Group : id
        
      Group : links
        
          
    
        
        
        Group --> "*" Link : links
        click Link href "../Link"
    

        
      Group : params
        
          
    
        
        
        Group --> "*" Parameter : params
        click Parameter href "../Parameter"
    

        
      Group : parts
        
          
    
        
        
        Group --> "*" Part : parts
        click Part href "../Part"
    

        
      Group : props
        
          
    
        
        
        Group --> "*" Property : props
        click Property href "../Property"
    

        
      Group : title
        
      
```
