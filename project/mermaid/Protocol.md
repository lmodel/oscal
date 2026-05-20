


```mermaid
 classDiagram
    class Protocol
    click Protocol href "../Protocol"
      Protocol : name
        
      Protocol : port_ranges
        
          
    
        
        
        Protocol --> "*" PortRange : port_ranges
        click PortRange href "../PortRange"
    

        
      Protocol : title
        
      Protocol : uuid
        
      
```
