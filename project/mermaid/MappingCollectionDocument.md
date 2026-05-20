


```mermaid
 classDiagram
    class MappingCollectionDocument
    click MappingCollectionDocument href "../MappingCollectionDocument"
      OscalDocument <|-- MappingCollectionDocument
        click OscalDocument href "../OscalDocument"
      
      MappingCollectionDocument : mapping_collection
        
          
    
        
        
        MappingCollectionDocument --> "1" MappingCollection : mapping_collection
        click MappingCollection href "../MappingCollection"
    

        
      
```
