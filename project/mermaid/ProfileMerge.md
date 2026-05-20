


```mermaid
 classDiagram
    class ProfileMerge
    click ProfileMerge href "../ProfileMerge"
      ProfileMerge : as_is
        
      ProfileMerge : combine
        
          
    
        
        
        ProfileMerge --> "0..1" CombinationRule : combine
        click CombinationRule href "../CombinationRule"
    

        
      ProfileMerge : custom
        
          
    
        
        
        ProfileMerge --> "0..1" MergeCustom : custom
        click MergeCustom href "../MergeCustom"
    

        
      ProfileMerge : flat
        
          
    
        
        
        ProfileMerge --> "0..1" MergeFlat : flat
        click MergeFlat href "../MergeFlat"
    

        
      
```
