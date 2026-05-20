


```mermaid
 classDiagram
    class PoamLocalDefinitions
    click PoamLocalDefinitions href "../PoamLocalDefinitions"
      PoamLocalDefinitions : assessment_assets
        
          
    
        
        
        PoamLocalDefinitions --> "0..1" AssessmentAssets : assessment_assets
        click AssessmentAssets href "../AssessmentAssets"
    

        
      PoamLocalDefinitions : components
        
          
    
        
        
        PoamLocalDefinitions --> "*" SystemComponent : components
        click SystemComponent href "../SystemComponent"
    

        
      PoamLocalDefinitions : inventory_items
        
          
    
        
        
        PoamLocalDefinitions --> "*" InventoryItem : inventory_items
        click InventoryItem href "../InventoryItem"
    

        
      PoamLocalDefinitions : remarks
        
      
```
