


```mermaid
 classDiagram
    class EventTiming
    click EventTiming href "../EventTiming"
      EventTiming : at_frequency
        
          
    
        
        
        EventTiming --> "0..1" AtFrequency : at_frequency
        click AtFrequency href "../AtFrequency"
    

        
      EventTiming : on_date
        
          
    
        
        
        EventTiming --> "0..1" OnDateCondition : on_date
        click OnDateCondition href "../OnDateCondition"
    

        
      EventTiming : within_date_range
        
          
    
        
        
        EventTiming --> "0..1" WithinDateRange : within_date_range
        click WithinDateRange href "../WithinDateRange"
    

        
      
```
