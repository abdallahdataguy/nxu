# Fashion MNIST Classification using CNN

## Overview

- This project is about implementing a Convolutional Neural Network (CNN) in Python and R to classify images in MNIST dataset.
- The project shoes  how to build and train a CNN using Keras in R and Python
- The MNIST dataset contains 70,000 grayscale images of 28x28 pixels, representing 10 fashion categories.
- The 6 layers CNN model is trained to correctly predict classes for the images.

## Requirements

- In to successfully run this CNN model, the following software packages should be installed and properly configured:

### R Programming Environment
- R Version: Install the latest R software which can be dowloaded from the official R website here: https://cran.r-project.org/.

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
## Python requirement

- You must have Python installed to run the Python script and so that R can use it to run keras in R environment as keras is a Python library.
- Install the neccessary Python libraries

#### Steps:
1. Install Python by downloading it from the official website here: https://www.python.org/downloads/) or by installing  anaconda. Make sure you install Python 3.x.
2. Install Python Libraries:
   Inside your Python virtual environment, install the following libraries:
   - Keras: Install the latest version of Keras:
     ```bash
     pip install keras
     ```
   - TensorFlow: Since Keras uses TensorFlow as its backend:
     ```bash
     pip install tensorflow
     ```
3. Link R to Python Environment: 
   In R, ensure the Python environment is correctly configured using the `reticulate` package:
   ```r
   library(reticulate)
   use_virtualenv("my_keras_env", required = TRUE)  # for virtualenv
   # OR
   use_condaenv("my_keras_env", required = TRUE)  # for conda
