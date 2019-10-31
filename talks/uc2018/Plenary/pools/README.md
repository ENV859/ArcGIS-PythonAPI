# Swimming pool detection and classification using deep learning
This project was presented at the Esri UC 2018 Plenary session. This repository contains code for creating a swimming pool detector. However, with minor modifications it can be trained to detect objects of different types from aerial, drone or satellite imagery. The following blog articles outline our approach.

* [Medium blog: Swimming pool detection and classification using deep learning](https://medium.com/geoai/swimming-pool-detection-and-classification-using-deep-learning-aaf4a3a5e652)

* [Esri blog: How we did it: Integrating ArcGIS and deep learning at UC 2018](https://www.esri.com/arcgis-blog/products/api-python/analytics/how-we-did-it-integrating-arcgis-and-machine-learning-at-uc-2018/?adumkts=product&adupro=ArcGIS_Enterprise&aduc=social&adum=external&aduSF=twitter&utm_Source=social&aduca=ArcGIS_Enterprise_Releases&adut=deeplearningUC_blog&sf_id=701f2000000rpeWAAQ&adbsc=social2466101&adbid=1021789845209804800&adbpl=tw&adbpr=80676821)


## An end-to-end object detection workflow
The field of Deep Learning has recently witnessed groundbreaking research with state of the art results, but taking this research to the field and solving real-world problems is still a challenge. Integration of the latest research in AI with ArcGIS opens up a world of opportunities. The notebooks in this folder show an end-to-end workflow that starts from extracting image chips to training a deep learning object detection model, deploying it over a large geographical area and creating information products like maps, layers and web apps to share the results, as well as creating assignments for field workers for verification and field assessment of results.

![Detected Pools](https://cdn-images-1.medium.com/max/896/1*17wkvk94x7EKx8u33FQdwA.png)

<sub> Representative results of the detected swimming pools. The parcels outlined in red are being assessed incorrectly.</sub>  

## Objective

#### Update assessor data

Tax assessors at local government agencies must often rely on expensive and infrequent surveys, leading to assessment inaccuracies. Swimming pools are an important part of assessment records because they impact the value of the property. Finding pools that are not on the assessment roll (such as those recently constructed) will be valuable to the assessor, and will ultimately mean additional revenue for the community. Doing this through GIS and AI would certainly reduce the expensive human labor involved in updating the records through field visits of each property.

![Assessor's data](https://www.esri.com/arcgis-blog/wp-content/uploads/2018/07/pools1.png "Visualizing residential parcels in ArcGIS Pro")

<sub> Visualizing residential parcels in ArcGIS Pro </sub>  

#### Identify neglected pools

If a swimming pool is neglected, as when the property is foreclosed, it often turns a green color and becomes inviting to mosquitoes – standing water with no inputs or outputs. The sheer volume of properties affected in warmer climates, even as the market rebounded, has made the detection of these risky pools challenging for many organizations.

Public health and mosquito control agencies are tasked with protecting the public from vector-borne diseases, including viruses carried by mosquitoes like West Nile and Chikungunya. These agencies need a simple solution that helps them locate neglected pools from imagery and then use this intelligence to drive [field activity and mitigation efforts](http://solutions.arcgis.com/local-government/public-works/mosquito-control/).

![Clean and Green Pools](https://www.esri.com/arcgis-blog/wp-content/uploads/2018/07/pools2.png)

<sub>  Green or Clean Pools </sub>  

## Enviroment Setup

The project uses PyTorch and fast.ai deep learning libraries for training and deploying deep learning models. An easy and efficient way to set up the environment with the required libraries and the necessary GPU support is to create an EC2 instance using Amazon Web Services. Any AWS GPU compute instance, such as `p2.xlarge` will do. The fastai-part1v2-p2 (ami-c6ac1cbc) AMI comes set up with all the required enviroments and libraries. To setup your own AWS instance follow [this guide](https://github.com/reshamas/fastai_deeplearn_part1/blob/master/tools/aws_ami_gpu_setup.md)

After setting the AMI up you need to run the following commands to update the environment.
```shell
sudo apt update
sudo apt upgrade
cd fastai
conda env update
conda update --all 
```

If you want to set up the environment locally, you need to have a CUDA supported NVIDIA GPU and install the following libraries and tools:
```
Anaconda
PyTorch v0.3+
Fastai (https://github.com/fastai/fastai)
CUDA V9.0
CuDNN
```

After setting up the AMI/ local development machine, install ArcGIS API for Python and its dependencies using the following command in the terminal:

```bash
conda install -c esri arcgis
conda install -c conda-forge shapely
```

In your project home make a symlink using the following command
```shell
ln -s PATH_TO_CLONED_FASTAI_GITHUB_REPO/fastai fastai
```

## Workflow

### Label object locations

ArcGIS Pro can be used to can manually label sample object locations and create a shapefile containing the labeled locations.

It provides access to a host of aerial, satellite and drone imagery from Esri and its partners and includes an easy to use interface to label data as well as advanced GIS functionality, including tools for reviewing data to manage its quality. Additionally, it includes geoprocessing tools to create buffers and bounding boxes around labeled pool locations.

### Extract training data

Once you have the labeled object locations, you have the following two options to export the necessary training chips and training data:

#### Option A: Use Python code to export training samples
ArcGIS API for Python has methods for exporting images from Imagery (eg NAIP imagery layers) as well as Tile layers (such as the Esri World Imagery layer). The `Export Training Samples` notebook uses that approach. Run the `Export Training Samples.ipynb` after setting up the path to a shapefile containing the sample object locations in the `PATH` variable. The images will be extracted from the specific locations in the shapefile and will be stored in the images folder. Additionally, a tilemapping file containing a mapping of each image chip to the center coordinates of each object within that image is created.

#### Option B: Use ArcGIS Pro's 'Export Training Data for Deep Learning’ tool 
ArcGIS Pro includes the ‘Export Training Data for Deep Learning’ tool that can be used to create labelled image chips that are needed to train a deep learning model. For object detection workflows, the output data format is in the "Pascal VOC (Visual Object Challenge)" format.

The `Pascal VOC to Tile Mapping` notebook reads in the labeled Pascal VOC format files, and creates the necessary tilemapping file needed by the training step below.

![Screenshot of PascalVOC format downloading](https://user-images.githubusercontent.com/16683472/43246778-5d7ab360-90d0-11e8-930a-d664322992e1.png)

### Train object detector

Once the training data is obtailed, we can begin training the deep learning network using the `Train a Swimming Pool detector` notebook. Set the `PATH` variable to point to the folder containing the training data:

```python
PATH = Path('path/to/folder/which/contains/tilemapping')
```

Make sure the images are also stored in a subdirectory named `images`.

Note that you may need to train for longer depending upon your data. The visualization of results are at the end of the notebook. This project is for detecting objects of one class (type). With minor changes it can be made to work on multiple classes of objects. 

A few results of swimming pool detection are shown below.
![Our results](https://cdn-images-1.medium.com/max/716/1*rCYlCzQu4EODnOb986m07Q.png)

### Train 'clean or green' pools classifier

The detected pools as further classified as *clean or green* (i.e. neglected pools) using the `Clean or Green Pools Training` notebook.

To train this Resnet-34 based classification model, some detected pools are downloaded and then mannually labeled as *clean* or *green*. The training notebook assumes that the root directory for classification will have `train` and `valid` directories to contain the training and validation images. It also assumes that each directory will have subdirectories for each class (in this case, `green` and `clean`).

![green pool detection](https://cdn-images-1.medium.com/max/896/1*RLD_PDZHBUl1oAYcv7aQOA.png)

### Deploy trained model

The deployment code for the project is in the `Deploy model to find swimming pools` notebook. This notebook is used to run the object detector on a large area whose predictions can be accumulated and then be used to create information products such as feature layers for visualization and further analysis. A webmap is then created using this feature layer. The locations of the detected swimming pools are used to identify parcels that were not being accessed correctly using analysis tools from ArcGS Online. The Spatial DataFrame in ArcGIS API for Python is used for generating reports of such parcels.

Later the the predictions from object detector are used to further classify the pools are clean or green, which also can be converted to a feature layer for visualization on a web map.

The deployment notebook also demonstrates creation of Workforce assignments for mosquito-control field workers based on the results of the neglected pool detection analysis.

![final results](https://cdn-images-1.medium.com/max/896/1*6-y2UbWpuHvZyEhn3vbPuA.png)
