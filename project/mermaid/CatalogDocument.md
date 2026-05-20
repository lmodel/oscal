


```mermaid
 classDiagram
    class CatalogDocument
    click CatalogDocument href "../CatalogDocument"
      OscalDocument <|-- CatalogDocument
        click OscalDocument href "../OscalDocument"
      
      CatalogDocument : catalog
        
          
    
        
        
        CatalogDocument --> "1" Catalog : catalog
        click Catalog href "../Catalog"
    

        
      
```
