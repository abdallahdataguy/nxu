# Load necessary libraries
library(keras)

# Load the Fashion MNIST dataset
fashion_mnist <- dataset_fashion_mnist()
x_train <- fashion_mnist$train$x
y_train <- fashion_mnist$train$y
x_test <- fashion_mnist$test$x
y_test <- fashion_mnist$test$y

# Preprocess the data
x_train <- array_reshape(x_train, c(60000, 28, 28, 1)) / 255
x_test <- array_reshape(x_test, c(10000, 28, 28, 1)) / 255

# Convert labels to categorical one-hot encoding
y_train <- to_categorical(y_train, num_classes = 10)
y_test <- to_categorical(y_test, num_classes = 10)

# Define the CNN model
model <- keras_model_sequential() %>%
  layer_conv_2d(filters = 32, kernel_size = c(3, 3), activation = 'relu', input_shape = c(28, 28, 1)) %>%
  layer_max_pooling_2d(pool_size = c(2, 2)) %>%
  layer_conv_2d(filters = 64, kernel_size = c(3, 3), activation = 'relu') %>%
  layer_max_pooling_2d(pool_size = c(2, 2)) %>%
  layer_conv_2d(filters = 128, kernel_size = c(3, 3), activation = 'relu') %>%
  layer_flatten() %>%
  layer_dense(units = 128, activation = 'relu') %>%
  layer_dropout(rate = 0.5) %>%
  layer_dense(units = 10, activation = 'softmax')

# Compile the model
model %>% compile(
  optimizer = 'adam',
  loss = 'categorical_crossentropy',
  metrics = c('accuracy')
)

# Train the model
model %>% fit(x_train, y_train, epochs = 10, batch_size = 64, validation_split = 0.2)

# Evaluate the model on the test dataset
scores <- model %>% evaluate(x_test, y_test)
cat(sprintf("Test loss: %.4f, Test accuracy: %.4f\n", scores[[1]], scores[[2]]))

# Define a mapping from class indices to class names
class_names <- c(
  "T-shirt/top",
  "Trouser",
  "Pullover",
  "Dress",
  "Coat",
  "Sandal",
  "Shirt",
  "Sneaker",
  "Bag",
  "Ankle boot"
)

# Make predictions for the first two images in the test set
predictions <- model %>% predict(x_test[1:2, , , ])
predicted_classes <- apply(predictions, 1, which.max) - 1  # R indexing starts from 1

# Display the predicted classes
cat(sprintf("Predicted classes for the first two images: %s\n", toString(predicted_classes)))

# Plot the first two test images and their predicted class names
par(mfrow = c(1, 2))
for (i in 1:2) {
  image(x_test[i, , , 1], axes = FALSE, col = gray.colors(256))
  title(main = sprintf("Predicted: %s (Class %d)", class_names[predicted_classes[i] + 1], predicted_classes[i]))
}
