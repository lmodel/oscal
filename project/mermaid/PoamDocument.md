


```mermaid
 classDiagram
    class PoamDocument
    click PoamDocument href "../PoamDocument"
      OscalDocument <|-- PoamDocument
        click OscalDocument href "../OscalDocument"
      
      PoamDocument : plan_of_action_and_milestones
        
          
    
        
        
        PoamDocument --> "1" PlanOfActionAndMilestones : plan_of_action_and_milestones
        click PlanOfActionAndMilestones href "../PlanOfActionAndMilestones"
    

        
      
```
