


```mermaid
 classDiagram
    class Addition
    click Addition href "../Addition"
      Addition : by_id
        
      Addition : links
        
          
    
        
        
        Addition --> "*" Link : links
        click Link href "../Link"
    

        
      Addition : params
        
          
    
        
        
        Addition --> "*" Parameter : params
        click Parameter href "../Parameter"
    

        
      Addition : parts
        
          
    
        
        
        Addition --> "*" Part : parts
        click Part href "../Part"
    

        
      Addition : position
        
          
    
        
        
        Addition --> "0..1" AdditionPositionEnum : position
        click AdditionPositionEnum href "../AdditionPositionEnum"
    

        
      Addition : props
        
          
    
        
        
        Addition --> "*" ProfileAlterationProperty : props
        click ProfileAlterationProperty href "../ProfileAlterationProperty"
    

        
      Addition : title
        
      
```
