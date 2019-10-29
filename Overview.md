# ArcGIS API
https://developers.arcgis.com/python/

### Objectives
* How to learn the API
 * Documentation: Guide, Examples, Reference
 * Experimentation on tutorials
 * Execute project
* API Structure
 * GIS module - gateway to access
 * Items
 * Layers
 * FeatureSets
 * Features
 * Rasters
 * Spatial data frames
 * Maps
 * Etc.
 
### GIS module
 https://developers.arcgis.com/python/guide/using-the-gis/
 * Authentication
  * Properties
 * Finding content
  * Users
  * Items
  
### Items
 "Entities stored on AGOL":  
 https://esri.github.io/arcgis-python-api/apidoc/html/arcgis.gis.toc.html#item
 * Searching via AGOL
  * Item types: Feature layer, Web maps, Image layers,...
  * ID #s
  * REST Endpoints
  
 * Searching via the `Content.manager`
  * `gis.content.search(...)`
  * search terms
  * inside/outside portal
  * Displaying search results
   * List
   * `display`
  * Item IDs
  * Item URLs
  
### Layers
    https://esri.github.io/arcgis-python-api/apidoc/html/arcgis.gis.toc.html#layer
   
#### Feature Layer
    https://esri.github.io/arcgis-python-api/apidoc/html/arcgis.features.toc.html#featurelayer
 * Properties
 * Querying
 
##### FeatureSets
##### Features

#### Imagery Layer
 * Properties
 
---
## Exercises
* Find HUCs
* Query for HUC8 = 03030300
* Get feature
* Extract NLCD for HUC
* Plot its land cover breakdown