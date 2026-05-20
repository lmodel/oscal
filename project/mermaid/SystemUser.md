


```mermaid
 classDiagram
    class SystemUser
    click SystemUser href "../SystemUser"
      OscalCommon <|-- SystemUser
        click OscalCommon href "../OscalCommon"
      
      SystemUser : authorized_privileges
        
          
    
        
        
        SystemUser --> "*" AuthorizedPrivilege : authorized_privileges
        click AuthorizedPrivilege href "../AuthorizedPrivilege"
    

        
      SystemUser : description
        
      SystemUser : links
        
          
    
        
        
        SystemUser --> "*" ImplementationCommonLink : links
        click ImplementationCommonLink href "../ImplementationCommonLink"
    

        
      SystemUser : props
        
          
    
        
        
        SystemUser --> "*" ImplementationCommonProperty : props
        click ImplementationCommonProperty href "../ImplementationCommonProperty"
    

        
      SystemUser : remarks
        
      SystemUser : role_ids
        
      SystemUser : short_name
        
      SystemUser : title
        
      SystemUser : uuid
        
      
```
