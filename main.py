import numpy as np
import matplotlib.pyplot as plt
import utils

images, labels = utils.load_dataset()

weights_input_to_hidden = np.random.uniform(-0.5, 0.5, (20, 784))
weights_hidden_to_output = np.random.uniform(-0.5, 0.5, (10, 20))

bias_input_to_hidden = np.zeros((20, 1))
bias_hidden_to_output = np.zeros((10, 1))

epochs = 3

for epoch in range(epochs):
    print(f"Epoch №{epoch}")

    e_loss = 0  # Nullify before start of epoch
    e_correct = 0  # Nullify before start of epoch
    learning_rate = 0.01

    for image, label in zip(images, labels):
        image = np.reshape(image, (-1, 1))
        label = np.reshape(label, (-1, 1))

        # Forward propagation (hidden layer)
        hidden_raw = bias_input_to_hidden + weights_input_to_hidden @ image
        hidden = 1 / (1 + np.exp(-hidden_raw))  # Sigmoid

        # Forward propagation (output layer)
        output_raw = bias_hidden_to_output + weights_hidden_to_output @ hidden
        output = 1 / (1 + np.exp(-output_raw))

        e_loss += np.sum((output - label) ** 2) / 10
        e_correct += int(np.argmax(output) == np.argmax(label))

        delta_output = output - label
        weights_hidden_to_output += -learning_rate * delta_output @ np.transpose(hidden)
        bias_hidden_to_output += -learning_rate * delta_output

        delta_hidden = np.transpose(weights_hidden_to_output) @ delta_output * (hidden * (1-hidden))
        weights_input_to_hidden += -learning_rate * delta_hidden @ np.transpose(image)
        bias_input_to_hidden += - learning_rate * delta_hidden

    print(f"Loss: {round((e_loss / images.shape[0]) * 100, 3)}%")
    print(f"Accuracy: {round((e_correct / images.shape[0]) * 100, 3)}%")
