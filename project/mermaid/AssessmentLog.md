


```mermaid
 classDiagram
    class AssessmentLog
    click AssessmentLog href "../AssessmentLog"
      AssessmentLog : entries
        
          
    
        
        
        AssessmentLog --> "1..*" AssessmentLogEntry : entries
        click AssessmentLogEntry href "../AssessmentLogEntry"
    

        
      
```
