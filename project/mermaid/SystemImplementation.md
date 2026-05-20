


```mermaid
 classDiagram
    class SystemImplementation
    click SystemImplementation href "../SystemImplementation"
      SystemImplementation : components
        
          
    
        
        
        SystemImplementation --> "1..*" SspSystemComponent : components
        click SspSystemComponent href "../SspSystemComponent"
    

        
      SystemImplementation : inventory_items
        
          
    
        
        
        SystemImplementation --> "*" SspInventoryItem : inventory_items
        click SspInventoryItem href "../SspInventoryItem"
    

        
      SystemImplementation : leveraged_authorizations
        
          
    
        
        
        SystemImplementation --> "*" LeveragedAuthorization : leveraged_authorizations
        click LeveragedAuthorization href "../LeveragedAuthorization"
    

        
      SystemImplementation : links
        
          
    
        
        
        SystemImplementation --> "*" Link : links
        click Link href "../Link"
    

        
      SystemImplementation : props
        
          
    
        
        
        SystemImplementation --> "*" Property : props
        click Property href "../Property"
    

        
      SystemImplementation : remarks
        
      SystemImplementation : users
        
          
    
        
        
        SystemImplementation --> "*" SystemUser : users
        click SystemUser href "../SystemUser"
    

        
      
```
