# Module 6: Fashion MNIST Classification

This project classifies clothing images using a six-layer convolutional neural network CNN in Python and R.

## Files

- `Assignment6.py`: The main Python program containing Python CNN class, training, evaluation, and two predictions.
- `Assignment6.R`: Equivalent R program containing R6 class with the same CNN structure.
- `fashion-mnist-service/`: trained model, FastAPI app, Dockerfile, dependencies, and request script.
- `samples/`: This subfolder contains the two test images used for predictions.
- `python_results.json` and `r_results.txt`: model results using Python and R respectively.
- `docker_prediction_1.png` and `docker_prediction_2.png`: The screenshots of the successful predictions using docker service on port 8001.

## Model and results

Both models use these six layers:

1. Conv2D with 32 filters and ReLU
2. MaxPooling2D
3. Conv2D with 64 filters and ReLU
4. MaxPooling2D
5. Flatten
6. Dense with 10 outputs and softmax

The input shape is 28 x 28 x 1. Pixel values are divided by 255.
Training uses Adam and sparse categorical cross-entropy for five epochs.
There are 54,000 training images, 6,000 validation images, and 10,000 test images.

Model test accuracy: 89.05% and 89.12% for Python and R respectively 

Both models predicted the two sample images as Ankle boot and Pullover correctly.
Check the results returned by Docker API (HTTP 200) for both uploads in the screenshots.

## Setup

Use Python 3.11, R, and Docker Desktop with Linux containers.
For Anaconda, create and activate an environment:

```bat
conda create -n fashion-m6 python=3.11 -y
conda activate fashion-m6
```

Execute the command below from the `solution` folder with the above environment activated:

```powershell
python -m pip install -r fashion-mnist-service/requirements.txt
```

## Run Python

```powershell
python Assignment6.py
```

- When executed for the first time it will downloads the Fashion MNIST through Keras. 
- The script trains the model then prints its accuracy, and saves the results, sample images, and
`fashion-mnist-service/fashion_cnn.keras`.
- If you Rerun it the program will replace the above files created on-the-fly during the program execution.

## Run R

Install these packages once in R:

```r
install.packages(c("keras3", "reticulate", "R6"))
```

R uses TensorFlow from the Python environment above. In PowerShell, with that
Python environment active and the working directory set to `solution`, run:

```powershell
$env:RETICULATE_PYTHON = (python -c "import sys; print(sys.executable)")
Rscript Assignment6.R
```

R trains its own model and saves the accuracy and predictions in `r_results.txt` text file without overwriting the Python model used by the service.

## Test the local API

```powershell
python -m uvicorn main:app --app-dir fashion-mnist-service --host 127.0.0.1 --port 8000
```

Make sure the terminal is open and visit the link http://localhost:8000/docs, select POST `/predict`,
click **Try it out**, upload a sample PNG, and click **Execute**.
Repeat with the other sample and confirm that the response is successful by checking the HTTP response code 2000, the class,
and confidence.

You can also test using a terminal, second terminal, while the Python environment active by executing the following commands to test the two sample files:

```powershell
python fashion-mnist-service/sample_request.py samples/image_1.png
python fashion-mnist-service/sample_request.py samples/image_2.png
```

## Run with Docker

Start Docker Desktop and wait until its engine is up and running then execute the following commands in terminal:

```powershell
docker build -t fashion-mnist-m6 ./fashion-mnist-service
docker run -d --name fashion-m6 -p 8001:8000 fashion-mnist-m6
docker ps --filter name=fashion-m6
```

Then open http://localhost:8001/docs and upload each sample using POST `/predict`.
Port 8001 is used for Docker; port 8000 is used for the local Python service.
The API applies the same image conversion, resizing, and normalization
used during training.

You can also test the container from the terminal directly by issuing the following commands:

```powershell
python fashion-mnist-service/sample_request.py samples/image_1.png --url http://localhost:8001/predict
python fashion-mnist-service/sample_request.py samples/image_2.png --url http://localhost:8001/predict
```

## References

- [Keras Fashion MNIST dataset](https://keras.io/api/datasets/fashion_mnist/)
- [Keras CNN example](https://keras.io/examples/vision/mnist_convnet/)
- [R keras3 CNN example](https://keras3.posit.co/articles/examples/vision/mnist_convnet.html)
