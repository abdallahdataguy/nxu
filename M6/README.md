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

### 2. Required R Packages
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
- Reticulate: This package integrates Python into R, enabling the use of Keras (which is a Python library) inside R.
  - Install `reticulate`:
    ```r
    install.packages("reticulate")
    ```

### 3. Python Backend

Keras in R relies on a Python backend, as Keras is a Python library. Therefore, you must have Python installed and configured to run Keras in R.

#### Steps:
1. Install Python: Download Python 3 from the official website [here](https://www.python.org/downloads/). Make sure you install Python 3.x.
   
2. Virtual Environment (Optional but Recommended): Use a virtual environment to manage Python dependencies.
   - Create a virtual environment:
     ```bash
     virtualenv my_keras_env
     source my_keras_env/bin/activate  # On Windows: my_keras_env/Scripts/activate
     ```
   - Alternatively, create a conda environment:
     ```bash
     conda create -n my_keras_env python=3.8
     conda activate my_keras_env
     ```

3. Install Python Libraries:
   Inside your Python virtual environment, install the following libraries:
   - Keras: Install the latest version of Keras:
     ```bash
     pip install keras
     ```
   - TensorFlow: Since Keras uses TensorFlow as its backend:
     ```bash
     pip install tensorflow
     ```

4. Link R to Python Environment: 
   In R, ensure the Python environment is correctly configured using the `reticulate` package:
   ```r
   library(reticulate)
   use_virtualenv("my_keras_env", required = TRUE)  # for virtualenv
   # OR
   use_condaenv("my_keras_env", required = TRUE)  # for conda
