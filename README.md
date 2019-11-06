---
Title: ArcGIS Python API
Class: ENV 859 - Advanced GIS
Date: Fall 2019
Instructor: John Fay
---

<center><a href='./index.html'>ENV 859 - Advanced GIS</a> | Fall 2019 | Instructor: <a href='mailto:john.fay@duke.edu'>John Fay</a> </center>

# The ArcGIS Python API

[toc]

## Introduction

The world of Big Data, Cloud-based GIS, and APIs moves at an astonishingly fast pace: what's cutting edge today is likely old news in a year. This trend has two implications for how I teach Advanced GIS. First, I emphasize a strong foundation of the basics, i.e., concepts that are likely to persist across the different manifestations of geospatial technologies. And second, I seek to wean you off learning in a classroom setting and instead learn how to advanced your knowledge using whatever resources are at your disposal. 

Learning the **ArcGIS Python API** will be a good example of the latter. Rather than walk you through with a number of detailed examples, I instead simply point you to the vast resources ESRI provides on this API - though I do offer a bit of light guidance and curation of some materials, to prime the pump at bit, but also to drive some of you to key bits that should help you in your course projects. 

## Learning Objectives

* Review useful approaches for learning a new technology
* Become familiar with what the ArcGIS Python API is and what it can do
* Engage the API to locate and download content or use in directly in your Python environment

---



## What *is* the ArcGIS Python API?

In a nutshell, the ArcGIS Python API is quite an amazing resource ESRI has only recently released that gives you access to a vast amount of data and processing abilities on a cloud-based platform (ArcGIS Online) -- all through the Python coding environment. I've only started tinkering with this cool tool myself, so it's a perfect venue for discovering this technology together so that I might share my insights about how to go about learning something on your own!

---



## Getting to know the ArcGIS Python API

Now that you heard about this new API thing, where should you go next to learn more? The obvious place is ESRI's documentation for it - and ESRI really does do a good job of documenting its resources.

### **<font color='blue'>» Task 1: Familiarize yourself with the documentation</font>**

- Open the main page for the ArcGIS Python API (Google to find the [link](https://www.google.com/search?q=ArcGIS+Python+API)).
- Browse the page, asking yourself: <u>What does this new technology do?</u> 
- Get a feel for the <u>structure of the documentation</u>.
- You may also want to explore where this page lives in the context of other related resources:
  - Note the URL: This page is a subpage of https://developers.arcgis.com. <u>What's on that link?</u> 
  - You may also notice the **Sign In link** in the upper right. <u>Can you sign in?</u> <u>What are you signing in to?</u>

> *At first you might only get a vague idea of what the API can do, and that's fine. But you'll also see that this site offers many different pathways to learn more. There are links to a **Guide**, **Sample Notebooks**, an **API Reference**, and link to several blog posts where everyday folks share their knowledge. It also has links to a number of samples using this API - plenty of ways to dive in. Even a 5 minute [video](https://www.youtube.com/watch?v=SyFebn8ZgbU) to get you started! (A longer video is [here](https://www.youtube.com/watch?v=RRXKbT7fyaI)...)*



### **<font color='blue'>» Task 2: Play! (and learn)</font>**

The exact path you take to learn the API is up to you. Just note that the ArcGIS Python API is a particularly vast API with more capabilities than you will likely ever use and that you shouldn't expect to master all it has to offer in a day or two or even a month or two. Instead, I recommend <u>you explore various aspects of the API to various depths</u> -- all the while making an effort to understand commonalities among the various components and building a mental structure of what this resource can do and how it might be useful to you. 

*Some example starting points:*

- From the API's main page, click on the [Get Started](https://developers.arcgis.com/python/guide/using-the-gis/) link. 

  - You may first notice that the coding environment the present resembles a Jupyter notebook. And if you scroll down you will confirm that the **ArcGIS Python API leverages Jupyter notebooks quite heavily**. 
  - You may also noticed on the left side is a **hierarchical listing of topics**. This gives you glimpse at how the API is structured with sections on "<u>The GIS</u>", "<u>Feature data and analysis</u>", "<u>Working with the Spatially Enabled DataFrame</u>", etc. And if you expand these, they reveal more detailed information on each... 


- A somewhat logical next step would be to expand the **Get Started** section in the topics on the left and click the [Install and set up](https://developers.arcgis.com/python/guide/install-and-set-up/) item. (This is the same "Install the API" link found on the documentation's main page...)

  - Here, you'll see a number of ways to install the API, many of which are good reminders of why we spend time learning what Conda is and how to clone ArcGIS Pro Python environments and install packages.
  - You'll also see a link to "[Try it Live](https://notebooks.esri.com/)", i.e. use a web-based Jupyter notebook. without installing anything! 


- Try a few live examples via the "[Try it Live](https://notebooks.esri.com/)" link.

  - Browse the folders and open some notebooks: perhaps the `using the api` notebook in the `guide`/`01-getting-started` folder...
  - Run some of the cells as is. Change some values. If you need to reset everything, just close all Jupyter pages and hit the "[Try it Live](https://notebooks.esri.com/)" link again....


- From the API's main page, click the [View samples](https://developers.arcgis.com/python/sample-notebooks/) link. 

  - Here you can download a set examples to your local machine. 
  - Note that other link takes you to a GitHub repository with all the examples. You may wish to **fork** that repository and then **clone** it to your local machine. (==Note these materials are also in the repository we'll be using in class exercises...==)
  - Have a look at some of the samples. It's quite impressive what these notebooks can do!

------



## Some lesson's I've learned...

*While I want to leave the exploration of the API in your hands, I do feel it useful to offer a few brief tips that might help overcome some initial humps in the learning curve. I also offer a few Jupyter notebooks to help out with these provided in the form of a GitHub repository.*

### ♦ On the general structure of the API

A bulk of the API's utility is interacting with resources found on ArcGIS Online. It's organized into a number of modules (see https://developers.arcgis.com/python/guide/overview-of-the-arcgis-api-for-python/#Architecture-of-the-API) loosely categorized into three themes: accessing GIS content at various levels (green),  augmenting interaction with these data (blue), and visualizing the data (orange).



<img src="https://developers.arcgis.com/assets/img/python-graphics/guide_api_overview_modules.png" alt="https://developers.arcgis.com/assets/img/python-graphics/guide_api_overview_modules.png" style="zoom:33%;" />





Also useful is the discussion centered on the architecture of the GIS Module:

![GIS module](https://developers.arcgis.com/assets/img/python-graphics/guide_gis_module_01.png)

More info: https://developers.arcgis.com/python/guide/the-gis-module/

I suggest focusing first on techniques for [accessing content](https://developers.arcgis.com/python/guide/accessing-and-creating-content/#Accessing-and-creating-content) , and then perhaps on analyzing content. Using the ArcGIS Python API for analyzing content, however, may consume credits or possibly be disabled - something I need to explore more myself. However, if you can access content from within Python, you can perhaps use open source GIS (e.g., GeoPandas) to perform analysis...



### ♦ On installing the API

**The ArcGIS Python API is installed with ArcGIS Pro, version 2.4, so no need to perform a separate install.** You can use the Jupyter notebook shortcut added to your Start menu and jump right in with the API. Or you can clone the `arcgispro-py3` environment and link a Jupyter shortcut to that - as we've done with other class exercises. 

However, if you wish to install it on a **machine without ArcGIS Pro installed**, I suggest installing [MiniConda](https://conda.io/miniconda.html) Python, and then following the instructions here: https://developers.arcgis.com/python/guide/install-and-set-up/#Install-using-Anaconda-for-Python-Distribution, namely use `conda install -c esri arcgis`. 



### ♦ On authenticating the API

The API can be used without logging in, i.e., [anonymously](https://developers.arcgis.com/python/guide/working-with-different-authentication-schemes/#Anonymous-users) (`gis = GIS()`). This is the easiest way to access the API's functionality, but you have limited access. 

If you are on a machine running ArcGIS Pro - and you have enabled that application by logging into the app - then you can authenticate your ArcGIS Python API simply by using `gis = GIS('pro')` ([link](https://developers.arcgis.com/python/guide/working-with-different-authentication-schemes/#Connecting-through-ArcGIS-Pro)).

What you <u>can't</u> do, as a Duke enterprise user, however, is log in directly using your Duke NetID and Password. That is because Duke uses an enterprise wide "shibboleth" log in (which is why the familiar Duke login window appears when you first log into ArcGIS Pro...). So, if you want to authenticate on a machine without ArcGIS Pro, you need to follow the directions for "[user authentication using OAuth2.0](https://developers.arcgis.com/python/guide/working-with-different-authentication-schemes/#User-authentication-with-OAuth-2.0)", which involves creating and registering an application in Duke's ArcGIS Online Portal (https://dukeuniv.maps.arcgis.com/home/index.html) and then running code as below:

```python
gis = GIS("https://dukeuniv.maps.arcgis.com", client_id='YmtqqKYoHULH1M2l')
print("Successfully logged in as: " + gis.properties.user.username)
```



### ♦ On exploring

Since data are central to most any analysis you'll want to do, you should start exploring ways to locate and import data into your coding environment. I've found that this often boils down to the following tasks:

#### Finding content:

* **Search** via ArcGIS Online (https://arcgis.com or https://dukeuniv.maps.arcgis.com)

  * Refine your search using various keywords (e.g. `owner:Federal_User_Community`)
  * <u>Sort</u> result by various criteria
  * <u>Filter</u> results for different *item types*, *date*, or *status*
  * Record the item's ID number or its REST endpoint URL

* **Search** via Python using the `arcgis` module's `GIS.content.search()` method

  * Refine your search using various keywords (e.g. `owner:Federal_User_Community`)

  * <u>Filter</u> for different item types

#### Importing items

2. Second, **import** **<u>items</u>** you found into your script. 
   * If you found the item via [searching AGOL](https://doc.arcgis.com/en/arcgis-online/reference/search.htm), then you can import items either by its **Item ID** (if available) for via its **REST endpoint** (i.e. the URL listed in the item's details) 
   * Alternatively, if you searched for items in your script, you can select from the list of results returned. 
3. With items imported, the next stage is what to do with them. That depends on what *type* of item you accessed. 
   * **Web maps provide** access to multiple layers and tables.
   * And [**layers**](https://doc.arcgis.com/en/arcgis-online/reference/layers.htm) themselves come in multiple flavors, though only some have analytical capability. These include:
     * [Feature Layers](https://doc.arcgis.com/en/arcgis-online/reference/feature-layers.htm) are the equivalent to a feature class and can either be [hosted layers](https://doc.arcgis.com/en/arcgis-online/reference/feature-layers.htm#ESRI_SECTION1_26EBAE21F63042B9A51A4312A08A1B25) you access directly or [feature collections](https://doc.arcgis.com/en/arcgis-online/reference/feature-layers.htm#GUID-304463C0-25BD-4FEA-8DD6-AD82F2C96B56) that you can download and use. Alternatively, you can convert these layers into [Spatial Data Frames](https://developers.arcgis.com/python/guide/introduction-to-the-spatially-enabled-dataframe/) and use more generalize data techniques. 
     * Imagery Layers are the equivalent to raster datasets and are analyzed using either [Image](https://developers.arcgis.com/python/guide/using-imagery-layers/) or [Raster](https://developers.arcgis.com/python/guide/using-raster-analysis/) analysis modules, depending on type of data stored and what you want to do with it. 

From there, your workflow can take many pathways. 

* You can continue to analyze feature data with the [arcpy.features](https://developers.arcgis.com/python/api-reference/arcgis.features.toc.html) module its [submodules](https://developers.arcgis.com/python/api-reference/arcgis.features.toc.html#submodules), or or get even more detailed with its geometry module. Alternatively you can apply geoprocessing tools to your data with the [arcpy.geoprocessing](https://developers.arcgis.com/python/api-reference/arcgis.geoprocessing.html) module.
* You can analyze image layers with the [arcpy.raster](https://developers.arcgis.com/python/api-reference/arcgis.raster.toc.html#) module or its [submodules](https://developers.arcgis.com/python/api-reference/arcgis.raster.toc.html#submodules). 
* You visualize data with the [mapping](https://developers.arcgis.com/python/api-reference/arcgis.mapping.html) module, perform geocoding with the [arcpy.geocoding](https://developers.arcgis.com/python/api-reference/arcgis.geocoding.html) module.
* Some of the more advanced capabilities include [geoenrichment](https://developers.arcgis.com/python/api-reference/arcgis.geoenrichment.html), [network analysis](https://developers.arcgis.com/python/api-reference/arcgis.network.toc.html), [realtime mapping](https://developers.arcgis.com/python/api-reference/arcgis.realtime.html), and even [machine learning](https://developers.arcgis.com/python/api-reference/arcgis.learn.html). 
* And of course you can extend your analysis with the countless other Python packages out there...



### ♦ Object model diagrams

In the documentation, you may also encounter some "object model diagrams" like the one for the features module below. These can be useful for seeing how the pieces of the API fit together, i.e., how you can create one type of object from another. This diagram, for examples, show that when you *query* a *FeatureLayer* object, the result is a *FeatureSet* object. 

<img src="https://esri.github.io/arcgis-python-api/notebooks/nbimages/guide_features_01.png" alt="features module object diagram" style="zoom:33%;" />





## Some useful applications of the API

*A number of you indicated interest in grabbing subsets of very large datasets in your course projects. I've provided some examples to jumpstart your efforts in using the ArcGIS Python API to do just that with the notebooks found in this repository:  https://github.com/ENV859/ArcGIS-PythonAPI.*

- Authenticating the GIS:  [01-Authenticating-the-API.ipynb](https://github.com/ENV859/ArcGIS-PythonAPI/blob/master/01-Authenticating-the-API.ipynb)
- Selecting and grabbing feature data: [02-Get-Census-Data.ipynb](https://github.com/ENV859/ArcGIS-PythonAPI/blob/master/02-Get-Census-Data.ipynb)
- Selecting and grabbing raster data: [03-Get-NLCD-Data.ipynb](https://github.com/ENV859/ArcGIS-PythonAPI/blob/master/03-Get-NLCD-Data.ipynb)

I suggest you fork and download a clone of this API to tinker with the notebooks. It contains a number of example notebooks as well to explore the API. Or you can fork and/or clone ESRI's repository: https://github.com/Esri/arcgis-python-api



## Some useful [secret?] tutorials from ESRI

**<u>Main link</u>**: https://developers.arcgis.com/labs/?product=python&topic=any

* Download data: https://developers.arcgis.com/labs/python/download-data/
* Create data: https://developers.arcgis.com/labs/python/create-data/
* Importing data: https://developers.arcgis.com/labs/python/import-data/
* Add a layer from an item: https://developers.arcgis.com/labs/python/add-a-layer-from-an-item/
* Display web data: https://developers.arcgis.com/labs/python/display-a-web-map/
* Display a web scene: https://developers.arcgis.com/labs/python/display-a-web-scene/
* Share maps and layers: https://developers.arcgis.com/labs/python/share-maps-and-layers/
* Search for an address: https://developers.arcgis.com/labs/python/search-for-an-address/
* Find places: https://developers.arcgis.com/labs/python/find-places/
* Load spatial data frame: https://developers.arcgis.com/labs/python/load-spatial-data-frame/

---

END

