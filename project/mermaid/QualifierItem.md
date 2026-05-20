


```mermaid
 classDiagram
    class QualifierItem
    click QualifierItem href "../QualifierItem"
      QualifierItem : category
        
          
    
        
        
        QualifierItem --> "1" QualifierCategoryEnum : category
        click QualifierCategoryEnum href "../QualifierCategoryEnum"
    

        
      QualifierItem : description
        
      QualifierItem : predicate
        
          
    
        
        
        QualifierItem --> "1" QualifierPredicateEnum : predicate
        click QualifierPredicateEnum href "../QualifierPredicateEnum"
    

        
      QualifierItem : remarks
        
      QualifierItem : subject
        
          
    
        
        
        QualifierItem --> "1" QualifierSubjectEnum : subject
        click QualifierSubjectEnum href "../QualifierSubjectEnum"
    

        
      
```
