# Module 6: Fashion MNIST Classification

This project classifies clothing images using a six-layer CNN in Python and R.
The trained Python model is also served through FastAPI and Docker.

## Files

- `Assignment6.py`: Python CNN class, training, evaluation, and two predictions.
- `Assignment6.R`: R6 class with the same CNN structure.
- `fashion-mnist-service/`: trained model, FastAPI app, Dockerfile, dependencies, and request script.
- `samples/`: the two test images used for predictions.
- `python_results.json` and `r_results.txt`: model results.
- `local_api_results.txt`: responses from testing the local API.
- `docker_prediction_1.png` and `docker_prediction_2.png`: successful predictions from the Docker service on port 8001.

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

| Model | Test accuracy |
|---|---|
| Python | 89.05% |
| R | 89.12% |

Both models correctly predicted the two sample images as Ankle boot and Pullover.
The Docker API returned HTTP 200 for both uploads, as shown in the screenshots.

## Setup

Use Python 3.11, R, and Docker Desktop with Linux containers.
For Anaconda, create and activate an environment:

```bat
conda create -n fashion-m6 python=3.11 -y
conda activate fashion-m6
```

Run the following commands from the `solution` folder with that environment active:

```powershell
python -m pip install -r fashion-mnist-service/requirements.txt
```

## Run Python

```powershell
python Assignment6.py
```

The first run downloads Fashion MNIST through Keras. The script trains the model,
prints its accuracy, and saves the results, sample images, and
`fashion-mnist-service/fashion_cnn.keras`. Rerunning it replaces these files.
The saved model is already included, so retraining is optional when testing the API.

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

If `Rscript` is not on PATH, use its full installation path.
R trains its own model and saves the accuracy and predictions in `r_results.txt`.
It does not overwrite the Python model used by the service.

## Test the local API

```powershell
python -m uvicorn main:app --app-dir fashion-mnist-service --host 127.0.0.1 --port 8000
```

Leave the terminal open. Visit http://localhost:8000/docs, select POST `/predict`,
click **Try it out**, upload a sample PNG, and click **Execute**.
Repeat with the other sample. A successful response shows code 200, the class,
and confidence.

You can also test from a second terminal with the Python environment active:

```powershell
python fashion-mnist-service/sample_request.py samples/image_1.png
python fashion-mnist-service/sample_request.py samples/image_2.png
```

## Run with Docker

Start Docker Desktop and wait for its engine to be ready. From `solution`, run:

```powershell
docker build -t fashion-mnist-m6 ./fashion-mnist-service
docker run -d --name fashion-m6 -p 8001:8000 fashion-mnist-m6
docker ps --filter name=fashion-m6
```

Open http://localhost:8001/docs and upload each sample using POST `/predict`.
Port 8001 is used for Docker; port 8000 is used for the local Python service.
The API applies the same grayscale conversion, image size, and normalization
used during training.

To test the container from the terminal:

```powershell
python fashion-mnist-service/sample_request.py samples/image_1.png --url http://localhost:8001/predict
python fashion-mnist-service/sample_request.py samples/image_2.png --url http://localhost:8001/predict
```

If a request fails, check `docker logs fashion-m6`. If the container name is
already in use, remove it with `docker rm -f fashion-m6` before running it again.
Stop it when finished with `docker stop fashion-m6`.

## Submission

Include this folder with both scripts, results, sample images, service files,
trained model, and both Docker screenshots. Leave out virtual environments
and `__pycache__` folders.

From the parent `M6` folder, create the submission archive:

```powershell
Compress-Archive -Path ./solution -DestinationPath ./Module_6_Submission.zip -Force
```

Check that the ZIP includes `fashion_cnn.keras` and both screenshots, then
upload `Module_6_Submission.zip` to the assignment portal.

## References

- [Keras Fashion MNIST dataset](https://keras.io/api/datasets/fashion_mnist/)
- [Keras CNN example](https://keras.io/examples/vision/mnist_convnet/)
- [R keras3 CNN example](https://keras3.posit.co/articles/examples/vision/mnist_convnet.html)
