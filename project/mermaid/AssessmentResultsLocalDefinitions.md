


```mermaid
 classDiagram
    class AssessmentResultsLocalDefinitions
    click AssessmentResultsLocalDefinitions href "../AssessmentResultsLocalDefinitions"
      AssessmentResultsLocalDefinitions : activities
        
          
    
        
        
        AssessmentResultsLocalDefinitions --> "*" Activity : activities
        click Activity href "../Activity"
    

        
      AssessmentResultsLocalDefinitions : objectives_and_methods
        
          
    
        
        
        AssessmentResultsLocalDefinitions --> "*" LocalObjective : objectives_and_methods
        click LocalObjective href "../LocalObjective"
    

        
      AssessmentResultsLocalDefinitions : remarks
        
      
```
