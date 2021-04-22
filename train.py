import numpy as np
import winRateModel1
import matplotlib.pyplot as plt

model = winRateModel1.getModel2()
model.summary()


x = np.load("x1.npy")
x = np.expand_dims(x,1)
y = np.load("y1.npy")
print(x.shape)

# ---shuffle---
s = np.arange(x.shape[0])
np.random.shuffle(s)
x = x[s]
y = y[s]
# -------------

#x = x[:3000]
#y = y[:3000]
numValidation = int(x.shape[0] * 0.2)

x_val = x[:numValidation]
y_val = y[:numValidation]
x_train = x[numValidation:]
y_train = y[numValidation:]

history = model.fit(x_train, y_train,batch_size = 128, epochs = 20, validation_data = (x_val, y_val))
model.save("model12.h5")

history_dict = history.history
loss = history_dict['loss']
val_loss = history_dict['val_loss']
acc = history_dict['accuracy']
val_acc = history_dict['val_accuracy']
epochs = range(1, len(loss)+1)
plt.plot(epochs, loss, 'bo',label = 'Training loss')
plt.plot(epochs, val_loss, 'b',label="Validation loss")
plt.title("Training and validation loss")
plt.xlabel('Epochs')
plt.ylabel("Loss")
plt.legend()
plt.show()

plt.plot(epochs, acc, 'ro',label = "Training Acc")
plt.plot(epochs, val_acc, 'r',label = "Validation Acc")
plt.title("Training and validation accuracy")
plt.xlabel('Epochs')
plt.ylabel("Acc")
plt.legend()
plt.show()

print(model.evaluate(x_val, y_val))