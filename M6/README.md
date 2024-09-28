# Fashion MNIST Classification using CNN

## Overview

This project demonstrates how to build and train a Convolutional Neural Network (CNN) using Keras in R and Python to classify images from the Fashion MNIST dataset. The dataset contains 70,000 grayscale images of 28x28 pixels, representing 10 fashion categories. The CNN model is built with six layers and is trained to predict the correct class for the images.

## Requirements

To successfully run the CNN model in R and Python, you must have the following software and packages installed and configured:

### 1. R Programming Environment
- R Version: The latest version of R is recommended for compatibility with the latest packages. You can download it from [here](https://cran.r-project.org/).

### 2. Required R Packages
- Keras: Provides an R interface to the Keras Python library.
  - Install Keras in R:
    ```r
    install.packages("keras")
    ```
- TensorFlow: Required for running Keras in R since Keras relies on TensorFlow as its backend.
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
