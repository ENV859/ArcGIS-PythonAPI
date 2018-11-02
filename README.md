# The ArcGIS Python API

## Introduction

The world of Big Data, Cloud-based GIS, and APIs moves at an astonishingly fast pace: what's cutting edge today is likely old news in a year. This has two implications for how I teach Advanced GIS. First, I emphasize a strong foundation of the basics, i.e., concepts that are likely to persist across the different manifestations of geospatial technologies. And second, I seek to wean you off learning in a classroom setting and instead learn how to advanced your knowledge using whatever resources are at your disposal. 

Learning the **ArcGIS Python API** will be a good example of the latter. Rather than walk you through with a number of detailed examples, I instead simply point you to the vast resources ESRI provides on this API - though I do offer a bit of light guidance and curation of some materials, to prime the pump at bit, but also to drive some of you to key bits that should help you in your course projects. 

---

## What *is* the ArcGIS Python API?

In a nutshell, the ArcGIS Python API is quite an amazing resource ESRI has only recently released that gives you access to a vast amount of data and processing abilities on a cloud-based platform (ArcGIS Online) all through the Python coding environment. I've only started tinkering with this cool tool myself, so it's a perfect venue for discovering this technology together so that I might share my insights about how to go about learning something on your own!

---

## Getting to know the ArcGIS Python API

Now that you heard about this new API thing, where should you go next to learn more? The obvious place is ESRI's documentation for it - and ESRI really does do a good job of documenting its resources.



**<font color='blue'>» Task 1: Familiarize yourself with the documentation</font>**

* Open the main page for the ArcGIS Python API (Google for the [link](https://www.google.com/search?q=ArcGIS+Python+API))
* Browse the page, asking yourself: What does this new technology do? 
* Get a feel for the structure of the documentation
* You may also want to explore where this page lives in the context of other related resources/
  * Note the URL. This page is a subpage of https://developers.arcgis.com. What's on that link? 
  * You may also notice the Sign In link in the upper right. Can you sign in? What are you signing in to?



At first you might only get a vague idea of what the API can do, and that's fine. But you'll also see that this site offers many different pathways to learn more. There are links to a Guide, Sample Notebooks, an API Reference, and a link to a Community where everyday folks can share their knowledge. It also has links to a number of samples using this API - plenty of ways to dive in. Even a 5 minute [video](https://www.youtube.com/watch?v=SyFebn8ZgbU&feature=youtu.be) to get you started!



**<font color='blue'>» Task 2: Play! (and learn)</font>**

The learning path you choose is up to you. I will suggest, however, that the ArcGIS Python API is a particularly vast API with more capabilities than you will likely ever use, and that you shouldn't expect to master all it has to offer in a day or two or even a week or two. Instead, I recommend <u>you explore various aspects of the API to various depths</u> -- all the while making an effort to understand commonalities among the various components and building a mental structure of what this resource can do and how it might be useful to you. 

Some example starting points:

* From the API's main page, click on the [Get Started](https://developers.arcgis.com/python/guide/using-the-gis/) link. 
  * You may first notice that the coding environment the present resembles a Jupyter notebook. And if you scroll down you will confirm that the **ArcGIS Python API leverages Jupyter notebooks quite heavily**. 
  * You may also noticed on the left side is a hierarchical listing of topics. This gives you glimpse at the structure of how the API is structured, with sections on "The GIS", "Administering your GIS", "Feature data and analysis", etc. And if you expand these, they reveal more detailed information on each. 
* A somewhat logical next step would be to expand the Get Started section in the topics on the left and click the [Install and set up](https://developers.arcgis.com/python/guide/install-and-set-up/) item. (This is the same "Install the API" link found on the documentation's main page...)
  * Here, you'll see a number of ways to install the API, many of which are good reminders of why we spend time learning what Conda is and how to clone ArcGIS Pro Python environments and install packages.
  * You'll also see a link to "[Try it Live](https://notebooks.esri.com/)", i.e. use a web-based Jupyter notebook. without installing anything! 
* Try a few live examples via the "[Try it Live](https://notebooks.esri.com/)" link.
  * Browse the folders and open some notebooks: perhaps the `Using the API` notebook in the `guide`/`01-getting-started` folder...
  * Run some of the cells as is. Change some values. If you need to reset everything, just close all Jupyter pages and hit the "[Try it Live](https://notebooks.esri.com/)" link again....

* From the API's main page, click the [View samples](https://developers.arcgis.com/python/sample-notebooks/) link. 
  * Here you can download a set examples to your local machine. 
  * Note that one link takes you to a GitHub repository with all the examples. You may wish to **fork** that repository and then **clone** it to your local machine. 
  * Have a look at some of the samples. I found it quite impressive what these notebooks can do!

---

## Some lesson's I've learned...

### ♦ On the general structure of the API

A bulk of the API's utility is interacting with resources found on ArcGIS Online. It's organized into a number of modules (see https://developers.arcgis.com/python/guide/overview-of-the-arcgis-api-for-python/#Architecture-of-the-API) loosely categorized into three themes: **accessing** content, **managing** content, and **analyzing** content. 

I suggest focusing first on techniques for [accessing content](https://developers.arcgis.com/python/guide/accessing-and-creating-content/#Accessing-and-creating-content) , and then perhaps on analyzing content. Using the ArcGIS Python API for analyzing content, however, may consume credits or possibly be disabled - something I need to explore more myself. However, if you can access content from within Python, you can perhaps use open source GIS (e.g., geopandas) to perform analysis...



### ♦ On installing the API

**The API is installed with ArcGIS Pro, version 2.2.3, so no need to perform a separate install.** You can use the Jupyter notebook shortcut added to your Start menu (when you upgrade to v.2.2.3) and jump right in with the API. Or you can clone the `arcgispro-py3` environment and link a Jupyter shortcut to that - as we've done with other class exercises. 

However, if you wish to install it on a **machine without ArcGIS Pro installed**, I suggest installing [MiniConda](https://conda.io/miniconda.html) Python, and then following the instructions here: https://developers.arcgis.com/python/guide/install-and-set-up/#Install-using-Anaconda-for-Python-Distribution, namely use `conda install -c esri arcgis`. 



### ♦ On authenticating the API

The API can be used without logging in, i.e., [anonymously](https://developers.arcgis.com/python/guide/working-with-different-authentication-schemes/#Anonymous-users) (`gis = GIS()`). This is the easiest way to access the API's functionality, but you have limited access. 

If you are on a machine running ArcGIS Pro - and you have enabled that application by logging into the app - then you can authenticate your ArcGIS Python API simply by using `gis = GIS('pro')` ([link](https://developers.arcgis.com/python/guide/working-with-different-authentication-schemes/#Connecting-through-ArcGIS-Pro)).

What you <u>can't</u> do, as a Duke enterprise user, however, is log in directly using your Duke NetID and Password. That is because Duke uses an enterprise wide "shibboleth" log in (which is why the familiar Duke login window appears when you first log into ArcGIS Pro...) . So, if you want to authenticate on a machine without ArcGIS Pro, you need to follow the directions for "[user authentication using OAuth2.0](https://developers.arcgis.com/python/guide/working-with-different-authentication-schemes/#User-authentication-with-OAuth-2.0)", which involves creating and registering an application in Duke's ArcGIS Online Portal (https://dukeuniv.maps.arcgis.com/home/index.html) and then running code as below:

```python
gis = GIS("https://dukeuniv.maps.arcgis.com", client_id='f8cRxbP3NO8bf9ag')
print("Successfully logged in as: " + gis.properties.user.username)
```



## Some useful applications of the API

* Authenticating
* Selecting and grabbing raster data
* Selecting and grabbing feature data

