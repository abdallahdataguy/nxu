# Module 6: Fashion MNIST Classification in R
# Set the working directory to this solution folder before running.
# RETICULATE_PYTHON must point to the Python environment with TensorFlow.
library(keras3)
library(R6)
set_random_seed(42)

FashionClassifier <- R6Class('FashionClassifier', public = list(
  model = NULL,
  initialize = function() {
    # Six layers; the input specification is not counted.
    self$model <- keras_model_sequential(input_shape = c(28, 28, 1)) |>
      layer_conv_2d(filters = 32, kernel_size = 3, activation = 'relu') |>
      layer_max_pooling_2d(pool_size = 2) |>
      layer_conv_2d(filters = 64, kernel_size = 3, activation = 'relu') |>
      layer_max_pooling_2d(pool_size = 2) |>
      layer_flatten() |>
      layer_dense(units = 10, activation = 'softmax')
    compile(self$model, optimizer = 'adam',
            loss = 'sparse_categorical_crossentropy', metrics = 'accuracy')
  },
  train = function(images, labels) {
    fit(self$model, images, labels, epochs = 5, batch_size = 128,
        validation_split = 0.1, verbose = 2)
  },
  predict = function(images) predict(self$model, images, verbose = 0)
))

# Load and normalize images, keeping the test set separate.
data <- dataset_fashion_mnist()
x_train <- array_reshape(data$train$x / 255, c(60000, 28, 28, 1))
x_test <- array_reshape(data$test$x / 255, c(10000, 28, 28, 1))
y_train <- data$train$y
y_test <- data$test$y
class_names <- c('T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
                 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot')

classifier <- FashionClassifier$new()
summary(classifier$model)
classifier$train(x_train, y_train)
scores <- evaluate(classifier$model, x_test, y_test, verbose = 0)
probabilities <- classifier$predict(x_test[1:2, , , , drop = FALSE])
predicted <- max.col(probabilities, ties.method = 'first') - 1
results <- data.frame(image = 1:2, actual = class_names[y_test[1:2] + 1],
                      predicted = class_names[predicted + 1])
print(scores)
print(results)
capture.output({ print(scores); print(results) }, file = 'r_results.txt')
