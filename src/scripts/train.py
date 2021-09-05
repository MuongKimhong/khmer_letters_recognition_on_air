import os

from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelBinarizer
from tensorflow.keras.optimizers import SGD
from tensorflow.keras import layers
import matplotlib.pyplot as plt
from tensorflow import keras
from imutils import paths
import numpy as np

from utils import dataset_loader


class NeuralNet:
    def __init__(self, width, height, depth, classes):
        self.model = keras.Sequential()
        self.image_input_shape = (height, width, depth)
        self.classes = classes

    def build(self):
        # first layer
        self.model.add(layers.Conv2D(filters=32, kernel_size=(3, 3), strides=(1, 1), padding="same", input_shape=self.image_input_shape))
        self.model.add(layers.Activation("relu"))
        # second layer
        self.model.add(layers.Conv2D(filters=32, kernel_size=(3, 3), strides=(1, 1), padding="same"))
        self.model.add(layers.Activation("relu"))
        # third layer
        self.model.add(layers.Conv2D(filters=32, kernel_size=(3, 3), strides=(1, 1), padding="same"))
        self.model.add(layers.Activation("relu"))
        # fourth layer
        self.model.add(layers.Conv2D(filters=64, kernel_size=(3, 3), strides=(1, 1), padding="same"))
        self.model.add(layers.Activation("relu"))
        # fifth layer
        self.model.add(layers.Conv2D(filters=64, kernel_size=(3, 3), strides=(1, 1), padding="same"))
        self.model.add(layers.Activation("relu"))
        # sixth layer
        self.model.add(layers.Conv2D(filters=64, kernel_size=(3, 3), strides=(1, 1), padding="same"))
        self.model.add(layers.Activation("relu"))
        # seventh layer
        self.model.add(layers.Conv2D(filters=64, kernel_size=(3, 3), strides=(1, 1), padding="same"))
        self.model.add(layers.Activation('relu'))
        # layer 8
        self.model.add(layers.Conv2D(filters=128, kernel_size=(3, 3), strides=(1, 1), padding="same"))
        self.model.add(layers.Activation("relu"))
        self.model.add(layers.MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
        # layer 9
        self.model.add(layers.Conv2D(filters=128, kernel_size=(3, 3), strides=(1, 1), padding="same"))
        self.model.add(layers.Activation("relu"))
        # model.add(layers.MaxPooling2D(pool_size=(2, 2), strides=(1, 1)))
        # layer 10
        self.model.add(layers.Conv2D(filters=128, kernel_size=(3, 3), strides=(1, 1), padding="same"))
        self.model.add(layers.Activation("relu"))
        # model.add(layers.MaxPooling2D(pool_size=(2, 2), strides=(1, 1)))
        # layer 11
        self.model.add(layers.Conv2D(filters=128, kernel_size=(3, 3), strides=(1, 1), padding="same"))
        self.model.add(layers.Activation('relu'))
        # model.add(layers.MaxPooling2D(pool_size=(2, 2), strides=(1, 1)))
        # layer 12
        self.model.add(layers.Conv2D(filters=128, kernel_size=(3, 3), strides=(1, 1), padding="same"))
        self.model.add(layers.Activation('relu'))
        # layer 13
        self.model.add(layers.Conv2D(filters=128, kernel_size=(3, 3), strides=(1, 1), padding="same"))
        self.model.add(layers.Activation('relu'))
        self.model.add(layers.MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
        # layer 14
        self.model.add(layers.Flatten())
        # layer 15
        self.model.add(layers.Dense(self.classes))
        self.model.add(layers.Activation("softmax"))
        
        return self.model
        
        
def train():
    image_path = "../lykong_dataset/"
    # use number in front of letter to sort 
    target_names = ['1_kor', '2_khor', '3_kur', '4_khur']

    image_shape = {'width': 128, 'height': 128, 'depth': 1}
    classes = 4
    batch_size = 16
    epochs = 16
    dataset_shape = (3104, 128, 128, 1)

    print("[INFO] starting the traning process ...")
    
    print("[INFO] accessing dataset ...")

    print("[INFO] starting the dataset loading process ...")

    (images, labels) = dataset_loader(image_path, dataset_shape)
    images = images.astype('float') / 255.0

    print("[INFO] splitting images for train set and test set ...")
    (train_x, test_x, train_y, test_y) = train_test_split(images, labels, test_size=0.1, random_state=42)

    print("[INFO] converting labels to vectors ....")
    train_y = LabelBinarizer().fit_transform(train_y)
    test_y = LabelBinarizer().fit_transform(test_y)
    
    print("[INFO] loading model ....")
    optimizer = SGD(learning_rate=0.005)
    model = NeuralNet(image_shape['width'], image_shape['height'], image_shape['depth'], classes)
    model = model.build()
    model.compile(optimizer=optimizer, loss="categorical_crossentropy", metrics=["accuracy"])

    print("[INFO] training the network ....")
    train = model.fit(train_x, train_y, validation_data=(test_x, test_y), batch_size=batch_size, epochs=epochs, verbose=1)

    print("[INFO] saving model ...")
    model.save("model/lykong_test_dataset.hdf5")

    print("[INFO] evaluating network ....")
    predictions = model.predict(test_x, batch_size=batch_size)
    print(classification_report(testY.argmax(axis=1), predictions.argmax(axis=1), target_names=target_names))

    plt.style.use("ggplot")
    plt.figure()
    plt.plot(np.arange(0, epochs), train.history["loss"], label="train_loss")
    plt.plot(np.arange(0, epochs), train.history["val_loss"], label="val_loss")
    plt.plot(np.arange(0, epochs), train.history["accuracy"], label="train_acc")
    plt.plot(np.arange(0, epochs), train.history["val_accuracy"], label="val_acc")
    plt.title("Training loss and accuracy")
    plt.xlabel("Epoch ")
    plt.ylabel("Loss/Accuracy")
    plt.legend()
    plt.show()
    
    print("[INFO] neural net model is saved into model directory")
    print("[INFO] training completed.")


if __name__ == '__main__':
    train()
