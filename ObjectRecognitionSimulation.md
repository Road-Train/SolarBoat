# How to Train an Object Detection Model for Visual Inspection with Synthetic Data

## Real-World Datasets for Object Recognition Task
There are many real-world datasets consisting of common object categories like Imagenet and COCO (Common Objects in Context) dataset. For practical applications using it indoor object recognition is not useful.

### Imagenet Dataset
It is a real-world dataset handling a greate amount of visual database for visual object recognition algorithms. It has more than fourteen million images covering multiple categories like insects, humans and public transports, etc. Downside is that it has a lack of diversity and restricted. It is not practical in areas where the environment is unconventional and rare.

### Microsoft COCO Dataset
It is a large-scale object recognition that consist of everyday objets in daily life. It is not that complex as real life is. It does not cover natural low-light conditions, foggy and rainy.

## Simulated Datasets for Object Recognition Task
There are several examples of simulated datasets to handle the real-world data availability easier.

### GMU Kitchen Scene Dataset
It has 5000 images with 11 indoor household object categories. It imports the object in simulation and overlays the environment.

### APC RGBD Dataset
It has 7500 images with 14 object model categories. It works with LineMod repository. Becase it does not simulate under varying indoor, outdoor, and low-light conditions.

## Graphics Software Tools for Generating Photorealistic Simulated Data
In the academic area, the real-world datasets are limited. These are no good for recognizing texture, material, lighting, and weather conditions. However, simulated datasets can model the objects and environment.

### Blender
This is a free and open-source 3D computer graphics software tool. It is usually used for developing object models, motion graphics, interactive 3D application, virtual reality, and computer games. One of the main components of Blender is the geometric primitives that can dvelop object models as required. It is capable of configuring different phyisical models and environment such as weather conditions.

### Unity
It is a cross-platform simulation engine for generating a simulated dataset for autonomous driving vehice systems and detect outdoor objects like vehicles, humans, traffic lights, etc. It can be used for creating 3D- and 2D models, virtual reality, and augmented reality applications and simulation experiences. With Unity Perception and Dataset Insights tools, it is far more easier to create simulated datasets.

### Cinema 4D
Researchers and engineers are capable of configuring object models with diverse environment setting like weather and lighting conditions. This is a modern state-of-the-art simulator. It was created to map out realisticly textures and areas. For automation parameters, the node-based editor, XPresso is used to replicate into other software. Makes it easier to program camera positions and image post-effects like color, film grain and vignette.

## From synthetic data generation to AI training
**Edge Impluse** is an empowered platform to create and deploy AI models for edge devices, supporting data collection, preprocessing, model training, and deployment. Its goal to implement AI capabilities as effectively as possible.
**NVIDIA Omniverse Replicator**, a computing platform that people can use for making accurate and realistic images in Universal Scene Description (OpenUSD) for training an object detection model on the Edge Impulse Platform. It is a highly recommended for 3D format - flexible, scalable, good performance, version control, and has asset management capabilities. For creating realistic and complex datasets, it is a great choice.

Get started with (NVIDIA Omniverse)[https://www.nvidia.com/en-us/omniverse/]
Download (Omniverse)[https://developer.nvidia.com/omniverse/simready-assets/] and Get Started With SimReady Assets.

### SimReady Assets 
Simulation-Ready Assets are 3D objects that are phyiscally accurate in properties and behavior. It is connected data streams for showing the real world in a simulated digital one. It is built-upon USD. It is avaible in NVIDIA Omniverse. Advantages: reliable starter to train AI models, reflect the real-world in simulated envrionents, has a flexible nature of USD to integrate in any workflow, and consistence. It used for robotics, digital twin warehouses, and autonomous driving.

### NVIDIA Isaac Sim
This is a reference application to design, simulate, test and train AI-based robots and autonomous machines in a virtual environment that is based on the real world. It is built on NVIDIA Omniverse, extensible and customizable for new or existing projects to test or/and validate pipelines. It includes a physics simulation with NVIDIA PhysX® 5, photorealism with real-time ray and path tracing, also MDL material definition support. It addresses the most common use cases such as manipulation, navigation, and synthetic data generation. For engineers, it is easy to use for designing, importing, building, and sharing robot models and virtual training environments.

More about (Isaac Sim)[https://developer.nvidia.com/isaac/sim]

# Resource
[Plunkett, JP. and Bradford, NB., (May 31, 2024). _How to Train an Object Detection Model for Visual Inspection with Synthetic Data_](https://developer.nvidia.com/blog/how-to-train-an-object-detection-model-for-visual-inspection-with-synthetic-data/) Referenced from June 17, 2024.
[Sonetta, HYS., (2021). _Bridging the Simulation-to-Reality Gap: Adapting Simulation Environment for Object Recognition_](chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/https://scholar.uwindsor.ca/cgi/viewcontent.cgi?article=9836&context=etd) Referenced from June 17, 2024.