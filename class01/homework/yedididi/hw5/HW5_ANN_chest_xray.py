import numpy as np # forlinear algebra
import matplotlib.pyplot as plt #for plotting things
import os
from PIL import Image # for reading images
# Keras Libraries <- CNN
import tensorflow as tf
from tensorflow.keras import datasets, layers, models, Model, Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, AveragePooling2D,Flatten, Dense, Input, BatchNormalization, Concatenate, Dropout
from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img
#from sklearn.metrics import classification_report, confusion_matrix # <- define evaluation metrics

mainDIR = os.listdir('./chest_xray')
print(mainDIR)
train_folder= './chest_xray/train/'
val_folder = './chest_xray/val/'
test_folder = './chest_xray/test/'
# train
os.listdir(train_folder)
train_n = train_folder+'NORMAL/'
train_p = train_folder+'PNEUMONIA/'
#Normal pic
print(len(os.listdir(train_n)))
rand_norm= np.random.randint(0,len(os.listdir(train_n)))
norm_pic = os.listdir(train_n)[rand_norm]
print('normal picture title: ',norm_pic)
norm_pic_address = train_n+norm_pic
#Pneumonia
rand_p = np.random.randint(0,len(os.listdir(train_p)))
sic_pic = os.listdir(train_p)[rand_norm]
sic_address = train_p+sic_pic
print('pneumonia picture title:', sic_pic)

# Load the images
norm_load = Image.open(norm_pic_address)
sic_load = Image.open(sic_address)

#Let's plt these images
f = plt.figure(figsize= (10,6))
a1 = f.add_subplot(1,2,1)
img_plot = plt.imshow(norm_load)
a1.set_title('Normal')
a2 = f.add_subplot(1, 2, 2)
img_plot = plt.imshow(sic_load)
a2.set_title('Pneumonia')
# plt.show()
# let's build the CNN model

#---------------------------Homework #3------------------------

#cnn = Sequential()
#Convolution
model_in = Input(shape = (64, 64, 3))
model = Flatten()(model_in)
# Fully Connected Layers
model = Dense(activation = 'relu', units = 128) (model)
model = Dense(activation = 'sigmoid', units = 1)(model)
# Compile the Neural network
model_fin = Model(inputs=model_in, outputs=model)
# model_fin.compile(optimize['accuracy'])
model_fin.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])


#---------------------------Homework #3------------------------

num_of_test_samples = 600
batch_size = 32
# Fitting the CNN to the images
# The function ImageDataGenerator augments your image by iterating through image as your CNN is getting ready to process that image
train_datagen = ImageDataGenerator(rescale = 1./255,
shear_range = 0.2,
zoom_range = 0.2,
horizontal_flip = True)
test_datagen = ImageDataGenerator(rescale = 1./255) #Image normalization.
training_set = train_datagen.flow_from_directory('./chest_xray/train',
target_size = (64, 64),
batch_size = 32,
class_mode = 'binary')

validation_generator = test_datagen.flow_from_directory('./chest_xray/val/',
    target_size=(64, 64),
    batch_size=32,
    class_mode='binary')
test_set = test_datagen.flow_from_directory('./chest_xray/test',
    target_size = (64, 64),
    batch_size = 32,
    class_mode = 'binary')
model_fin.summary()

#---------------------------Homework #4------------------------

cnn_model = model_fin.fit(training_set,
    steps_per_epoch = 163,
    epochs = 10,
    validation_data = validation_generator,
    validation_steps = 624)
test_accu = model_fin.evaluate(test_set,steps=624)
model_fin.save('medical_ann.h5')
print('The testing accuracy is :',test_accu[1]*100, '%')
Y_pred = model_fin.predict(test_set, 100)
y_pred = np.argmax(Y_pred, axis=1)
max(y_pred)

#---------------------------Homework #4------------------------

# # Accuracy
# plt.plot(cnn_model.history['val_accuracy'])
# plt.plot(cnn_model.history['accuracy'])
# plt.title('Model Accuracy')
# plt.ylabel('Accuracy')
# plt.xlabel('Epoch')
# plt.legend(['Training set', 'Validation set'], loc='upper left')
# plt.savefig('train_accuracy.png')
# plt.show(block=False)
# plt.clf()

import matplotlib.pyplot as plt

# 새로운 figure 생성 (2개의 subplot)
fig, axs = plt.subplots(1, 2, figsize=(14, 6))

# Accuracy plot (왼쪽)
axs[0].plot(cnn_model.history['accuracy'])
axs[0].plot(cnn_model.history['val_accuracy'])
axs[0].set_title('Model Accuracy')
axs[0].set_xlabel('Epoch')
axs[0].set_ylabel('Accuracy')
axs[0].legend(['Training set', 'Validation set'], loc='lower right')

# Loss plot (오른쪽)
axs[1].plot(cnn_model.history['loss'])
axs[1].plot(cnn_model.history['val_loss'])
axs[1].set_title('Model Loss')
axs[1].set_xlabel('Epoch')
axs[1].set_ylabel('Loss')
axs[1].legend(['Training set', 'Validation set'], loc='upper right')

# 레이아웃 조정 및 저장
plt.tight_layout()
plt.savefig('train_accuracy_loss_side_by_side.png', dpi=300)
plt.show(block=False)
plt.clf()


# plt.figure(figsize=(10, 6))
# plt.plot(cnn_model.history['val_accuracy'])
# plt.plot(cnn_model.history['accuracy'])
# plt.title('Model Accuracy')
# plt.ylabel('Accuracy')
# plt.xlabel('Epoch')
# plt.legend(['Validation set', 'Training set'], loc='upper left')
# plt.tight_layout()
# plt.savefig('train_accuracy.png', dpi=300)
# plt.show(block=False)
# plt.clf()


# # Loss
# plt.plot(cnn_model.history['val_loss'])
# plt.plot(cnn_model.history['loss'])
# plt.title('Model Loss')
# plt.ylabel('Loss')
# plt.xlabel('Epoch')
# plt.legend(['Training set', 'Test set'], loc='upper left')
# plt.savefig('train_loss.png')
# plt.show(block=False)
# plt.clf()