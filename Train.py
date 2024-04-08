import cv2
import os
import numpy as np
from PIL import Image


# получаем картинки и подписи из датасета
def get_images_and_labels(datapath):
    # получаем путь к картинкам
    image_paths = [os.path.join(datapath, f) for f in os.listdir(datapath)]
    # списки картинок и подписей на старте пустые
    images = []
    # перебираем все картинки в датасете
    for image_path in image_paths:
        # читаем картинку и сразу переводим в ч/б
        image_pil = Image.open(image_path).convert('L')
        # переводим картинку в numpy-массив
        image = np.array(image_pil, 'uint8')
        # определяем лицо на картинке
        faces = faceCascade.detectMultiScale(image)
        for (x, y, w, h) in faces:
            # добавляем его к списку картинок
            images.append(image[y: y + h, x: x + w])
            print(image_path)
    # возвращаем список картинок и подписей
    return images

# получаем путь к этому скрипту
path = os.path.dirname(os.path.abspath(__file__))
# создаём новый распознаватель лиц
recognizer = cv2.face.LBPHFaceRecognizer_create()
# указываем, что мы будем искать лица по примитивам Хаара
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
# путь к датасету с фотографиями пользователей
dataPath = path + r'\data'

# получаем список картинок и подписей
images = get_images_and_labels(dataPath)
labels = np.ones(len(images), dtype='int')
# обучаем модель распознавания на наших картинках и учим сопоставлять её лица и подписи к ним
recognizer.train(images, labels)
# сохраняем модель
recognizer.save(path+r'\trainer.yml')
