# Import modules
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from keras.datasets import fashion_mnist
import numpy as np

# Load Fashion MNIST dataset
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

# Preprocessing: Reshape and normalize
train_images = train_images.reshape((60000, 28, 28, 1)).astype('float32') / 255
test_images = test_images.reshape((10000, 28, 28, 1)).astype('float32') / 255

# Build the CNN model
model = Sequential()

# Adding layers to the CNN
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu'))

# Flatten and add fully connected layers
model.add(Flatten())
model.add(Dense(64, activation='relu'))
model.add(Dense(10, activation='softmax'))

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
model.fit(train_images, train_labels, epochs=5, batch_size=64)

# Save the model
model.save('fashion_mnist_cnn.h5')

# Load the saved model and make predictions
model = Sequential()
model = model.load_model('fashion_mnist_cnn.h5')

# Predict for two test images
predictions = model.predict(test_images[:2])

# Display predictions
for i, prediction in enumerate(predictions):
    predicted_label = np.argmax(prediction)
    print(f"Image {i+1} - Predicted label: {predicted_label}, Actual label: {test_labels[i]}")
