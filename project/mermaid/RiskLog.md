


```mermaid
 classDiagram
    class RiskLog
    click RiskLog href "../RiskLog"
      RiskLog : entries
        
          
    
        
        
        RiskLog --> "1..*" RiskLogEntry : entries
        click RiskLogEntry href "../RiskLogEntry"
    

        
      
```
