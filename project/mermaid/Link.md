


```mermaid
 classDiagram
    class Link
    click Link href "../Link"
      Link <|-- ImplementationCommonLink
        click ImplementationCommonLink href "../ImplementationCommonLink"
      Link <|-- SspSystemInformationLink
        click SspSystemInformationLink href "../SspSystemInformationLink"
      Link <|-- SspDiagramLink
        click SspDiagramLink href "../SspDiagramLink"
      Link <|-- SspLeveragedAuthorizationLink
        click SspLeveragedAuthorizationLink href "../SspLeveragedAuthorizationLink"
      Link <|-- SspByComponentLink
        click SspByComponentLink href "../SspByComponentLink"
      
      Link : href
        
      Link : media_type
        
      Link : rel
        
      Link : resource_fragment
        
      Link : text
        
      
```
