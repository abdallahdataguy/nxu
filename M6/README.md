# Module 6 Assignment: Fashion MNIST Classification

## 1. Overview

- This project is about implementing a Convolutional Neural Network (CNN) in Python and R to classify images in MNIST dataset.
- The project shoes  how to build and train a CNN using Keras in R and Python
- The MNIST dataset contains 70,000 grayscale images of 28x28 pixels, representing 10 fashion categories.
- The 6 layers CNN model is trained to correctly predict classes for the images.
- This project has two files both with similar implementation of six layers CNN, R file `Assignment6.R` and Python script `Assignment6.py`

## 2. R Requirements

- In to successfully run this CNN model in R, the following software packages should be installed and properly configured:

### R Programming Environment
- R Version: Install the latest R software which can be dowloaded from the official R website here: https://cran.r-project.org/.
- Rstudio (Optional): Install Rstudio, the most popular IDE for R by dowloading here: https://posit.co/download/rstudio-desktop/ 

### Required R Packages
- Keras R library that will provide an R interface to the Keras Python library.
  - Install Keras in R:
    ```r
    install.packages("keras")
    ```
- TensorFlow is also required since keras relies on TensorFlow as its backend.
  - Install TensorFlow in R:
    ```r
    install.packages("tensorflow")
    library(tensorflow)
    install_tensorflow()
    ```
- Reticulate: This package enables the use of Keras (which is a Python library) inside R. It allows R to use Python libraries not only keras.
  - Install `reticulate`:
    ```r
    install.packages("reticulate")
    ```
## 3. Python requirements
- In to successfully run this CNN model in Python, the following software packages should be installed and properly configured:

### Python Programming Environment
- Python Version: Install Python by downloading it from the official website here: https://www.python.org/downloads/
- Make sure you install Python 3.x.

### Required Python Packages:
Install Python Libraries:
   Install the following libraries:
   - Keras: Install the latest version of Keras:
     ```bash
     pip install keras
     ```
   - TensorFlow: Since Keras uses TensorFlow as its backend:
     ```bash
     pip install tensorflow
     ```
## 4. Running the scripts
### Running R File
- Make sure you have R and all the required libraries installed, follow the step `2. R Requirements`
- Open the R file `Assignment6.R` in any R environment, RStudio recommended, and run the script

### Running Python File
- Make sure you have Python and all the required libraries installed, follow the step `3. Python Requirements`
- Open the Python file `Assignment6.py` in any Python environment, built-in IDLE can suffice, and run the script
