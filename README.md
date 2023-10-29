# Sign-Language-Translator

### Abstract
Deaf and Dumb people use Sign Language (static / dynamic) for exchange of information & communication. It is usually very difficult for these impaired people to communicate with others who do not know SL. A visual-gestural language translator of Tamil sentences / phrases for impaired people which enables these specially-abled people to communicate easily and normally. A Sign language interpreter must be fluent in SL it translates, which combines signing, finger spelling, and specific body language.
  
This SLT is an easy, efficient and accurate mechanism which uses computerized digital image processing & classification methods. Accurate image recognition using advanced tools (Open CV) & techniques (Convolution Neural Network). This works by interpreting three dimensional spaces in movements between hands and other parts of the body. This project Extracts features(key points) , builds model , predicts sign and generates text / speech as output. Hence providing an efficient interface for communication between the disabled and others.

### Working
#### Module 1: Generation of Data Source and Pre-processing
Images come in different shapes and sizes. They also come from different sources. Taking all these variations into consideration, we need to perform some pre-processing on any image data. RGB is the most popular encoding format, and the most “natural image format”, but is not very efficient for a machine to learn from an RGB image. 

Also, among the first steps of data pre-processing are to make the images of the same size. Here we have used auto resizing for training to make all the images in the dataset convert into same resolution and also converted it into gray scale (Black & White image) to reduce the burden on the machine.

#### Module 2: Feature Extraction & Training phase
The process of feature extraction is useful when you need to reduce the number of resources, without losing important information. 
Feature extraction can also reduce the amount of redundant data for a given analysis. 

Also, the reduction of the data and the machine’s efforts in building variable combinations (features) facilitate the speed of learning and generalization steps in the machine learning process.Labelling was first evaluated with the original images on PACS and secondly with the resized images that were used for the actual learning data. Datasets were defined as the internal dataset and temporal dataset, with the temporal dataset used to evaluate the test. 


#### Module 3: Evaluation using confusion matrix
Once successful results are obtained, they are noted, and it is evaluated using Confusion matrix. After predictions save the model weight's we evaluate it using confusion matrix to determine true positive, false negative etc. Based on the percentage of accuracy we iterate the process to enhance the model. Test the product in real time and everything goes right then implement it.

#### Module 4: Testing phase & Implementation
Once a model is Built and the data is trained, we move on to the testing phase.During this phase, the real time input data will be captured by the web cam which will undergo pre-processing and feature extraction using Open CV. The pre-processed data will be compared with the predicted result and produce the desired output as speech using Pysound (Python library).

### Publication Details
**PAPER TITLE:** A Survey on Sign Language Translator

**PUBLISHING DATE:** 5th November

**PUBLISHING MEDIA:** International Research Journal of Modernization in Engineering Technology and Science, Volume:04 / Issue:11 / November-2022

**Impact Factor:** 6.752 

**DOI:** https://www.doi.org/10.56726/IRJMETS31026
