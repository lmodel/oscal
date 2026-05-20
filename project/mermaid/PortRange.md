


```mermaid
 classDiagram
    class PortRange
    click PortRange href "../PortRange"
      PortRange : end
        
      PortRange : remarks
        
      PortRange : start
        
      PortRange : transport
        
          
    
        
        
        PortRange --> "0..1" TransportEnum : transport
        click TransportEnum href "../TransportEnum"
    

        
      
```
