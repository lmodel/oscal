


```mermaid
 classDiagram
    class AssessmentAssets
    click AssessmentAssets href "../AssessmentAssets"
      AssessmentAssets : assessment_platforms
        
          
    
        
        
        AssessmentAssets --> "1..*" AssessmentPlatform : assessment_platforms
        click AssessmentPlatform href "../AssessmentPlatform"
    

        
      AssessmentAssets : components
        
          
    
        
        
        AssessmentAssets --> "*" SystemComponent : components
        click SystemComponent href "../SystemComponent"
    

        
      
```
