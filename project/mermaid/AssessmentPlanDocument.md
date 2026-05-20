


```mermaid
 classDiagram
    class AssessmentPlanDocument
    click AssessmentPlanDocument href "../AssessmentPlanDocument"
      OscalDocument <|-- AssessmentPlanDocument
        click OscalDocument href "../OscalDocument"
      
      AssessmentPlanDocument : assessment_plan
        
          
    
        
        
        AssessmentPlanDocument --> "1" AssessmentPlan : assessment_plan
        click AssessmentPlan href "../AssessmentPlan"
    

        
      
```
