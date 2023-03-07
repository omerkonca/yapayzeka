

from keras.datasets import imdb

(egitim_veri, egitim_etiket), (test_veri, test_etiket) = imdb.load_data(num_words=10000)

import numpy as np
def veriVektorleme (diziler,boyut=10000):
  sonuclar = np.zeros((len(diziler),boyut))
  for i, dizi in enumerate(diziler):
   sonuclar[i,dizi] = 1.
  return sonuclar

x_egitim = veriVektorleme(egitim_veri)
x_test = veriVektorleme(test_veri)

y_eğitim = np.asarray(egitim_etiket).astype("float32")
y_test = np.asarray(test_etiket).astype("float32")

from keras import layers
from keras import models

model = models.Sequential()
model.add(layers.Dense(16,activation="relu", input_shape=(10000,)))
model.add(layers.Dense(16, activation="relu"))
model.add(layers.Dense(1, activation="sigmoid"))

model.compile(optimizer="rmsprop", loss="binary_crossentropy", metrics=["accuracy"])

ysa = model.fit(x_egitim,y_eğitim, epochs=10, batch_size=512, validation_data=(x_egitim,y_eğitim))

import matplotlib.pyplot as plt
kayıp = ysa.history["loss"]
doğrulamaKayıp = ysa.history["val_loss"]

epok = range(1, len(kayıp) + 1)

plt.plot(epok, kayıp,"b", label="Eğitimn kaybı")
plt.plot(epok,doğrulamaKayıp, "r", label = "Doğrulama kaybı")
plt.title("Eğitim ve doğrulama kaybı")
plt.xlabel("Epoklar")
plt.ylabel("Kayıp")
plt.legend()
plt.show()

import matplotlib.pyplot as plt
başarım = ysa.history["acc"]
doğrulamaBaşarım = ysa.history["val_acc"]

epok = range(1, len(kayıp) + 1)

plt.plot(epok, başarım,"b", label="Eğitimn kaybı")
plt.plot(epok,doğrulamaBaşarım, "r", label = "Doğrulama kaybı")
plt.title("Eğitim ve doğrulama kaybı")
plt.xlabel("Epoklar")
plt.ylabel("Kayıp")
plt.legend()
plt.show()

ortalamBaşarım = np.mean(doğrulamaBaşarım)
print("Ortlama başarım. ", ortalamBaşarım)