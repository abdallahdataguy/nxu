# Module 6: Fashion MNIST Classification
from pathlib import Path
import argparse
import json
import numpy as np
import tensorflow as tf
from PIL import Image

folder = Path(__file__).resolve().parent
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']


class FashionClassifier:
    def __init__(self):
        # Six layers; the input specification is not counted as a layer.
        self.model = tf.keras.Sequential([
            tf.keras.Input(shape=(28, 28, 1)),
            tf.keras.layers.Conv2D(32, 3, activation='relu'),  # 1
            tf.keras.layers.MaxPooling2D(2),                 # 2
            tf.keras.layers.Conv2D(64, 3, activation='relu'),  # 3
            tf.keras.layers.MaxPooling2D(2),                 # 4
            tf.keras.layers.Flatten(),                       # 5
            tf.keras.layers.Dense(10, activation='softmax')   # 6
        ])
        self.model.compile(optimizer='adam', loss='sparse_categorical_crossentropy',
                           metrics=['accuracy'])

    def train(self, images, labels, epochs):
        return self.model.fit(images, labels, epochs=epochs, batch_size=128,
                              validation_split=0.1, verbose=2)

    def predict(self, images):
        return self.model.predict(images, verbose=0)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--epochs', type=int, default=5)
    args = parser.parse_args()
    tf.keras.utils.set_random_seed(42)
    tf.config.threading.set_intra_op_parallelism_threads(2)
    tf.config.threading.set_inter_op_parallelism_threads(2)

    # Load and normalize the data. The test set is not used for training.
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.fashion_mnist.load_data()
    raw_images = x_test[:2].copy()
    x_train = x_train.astype('float32')[..., None] / 255.0
    x_test = x_test.astype('float32')[..., None] / 255.0

    classifier = FashionClassifier()
    classifier.model.summary()
    history = classifier.train(x_train, y_train, args.epochs)
    loss, accuracy = classifier.model.evaluate(x_test, y_test, verbose=0)
    classifier.model.save(folder / 'fashion-mnist-service' / 'fashion_cnn.keras')

    # Predict two test images and export them for API testing.
    samples = folder / 'samples'
    samples.mkdir(exist_ok=True)
    probabilities = classifier.predict(x_test[:2])
    predictions = []
    for i in range(2):
        image_path = samples / f'image_{i + 1}.png'
        Image.fromarray(raw_images[i]).save(image_path)
        predicted = int(np.argmax(probabilities[i]))
        predictions.append({'image': image_path.name,
                            'actual': class_names[int(y_test[i])],
                            'predicted': class_names[predicted],
                            'confidence': float(probabilities[i, predicted])})
    results = {'epochs': args.epochs, 'training_images': 54000,
               'validation_images': 6000, 'test_images': 10000,
               'test_loss': float(loss), 'test_accuracy': float(accuracy),
               'predictions': predictions, 'history': history.history}
    (folder / 'python_results.json').write_text(json.dumps(results, indent=2), encoding='utf-8')
    print(f'Test accuracy: {accuracy:.2%}')
    for prediction in predictions:
        print(prediction)
