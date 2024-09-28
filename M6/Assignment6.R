# Load Keras library
library(keras)

# Load Fashion MNIST dataset
fashion_mnist <- dataset_fashion_mnist()
c(train_images, train_labels) %<-% fashion_mnist$train
c(test_images, test_labels) %<-% fashion_mnist$test

# Preprocess data: reshape and normalize
train_images <- array_reshape(train_images, c(nrow(train_images), 28, 28, 1))
test_images <- array_reshape(test_images, c(nrow(test_images), 28, 28, 1))
train_images <- train_images / 255
test_images <- test_images / 255

# Build the CNN model
model <- keras_model_sequential() %>%
  layer_conv_2d(filters = 32, kernel_size = c(3, 3), activation = 'relu', input_shape = c(28, 28, 1)) %>%
  layer_max_pooling_2d(pool_size = c(2, 2)) %>%
  layer_conv_2d(filters = 64, kernel_size = c(3, 3), activation = 'relu') %>%
  layer_max_pooling_2d(pool_size = c(2, 2)) %>%
  layer_conv_2d(filters = 64, kernel_size = c(3, 3), activation = 'relu') %>%
  layer_flatten() %>%
  layer_dense(units = 64, activation = 'relu') %>%
  layer_dense(units = 10, activation = 'softmax')

# Compile the model
model %>% compile(
  optimizer = 'adam',
  loss = 'sparse_categorical_crossentropy',
  metrics = c('accuracy')
)

# Train the model
model %>% fit(train_images, train_labels, epochs = 5, batch_size = 64)

# Save the model
save_model_hdf5(model, 'fashion_mnist_cnn_r.h5')

# Make predictions on two test images
predictions <- model %>% predict(test_images[1:2,,])

# Print predicted and actual labels
predicted_labels <- apply(predictions, 1, which.max) - 1
cat("Predicted labels: ", predicted_labels, "\n")
cat("Actual labels: ", test_labels[1:2], "\n")
