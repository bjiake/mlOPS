import tensorflow as tf
import tensorflow_datasets as tfds
import matplotlib.pyplot as plt

# Загрузка датасета tf_flowers
dataset_name = "tf_flowers"
(ds_train, ds_test), ds_info = tfds.load(
    dataset_name,
    split=["train[:80%]", "train[80%:]"],  # 80% на обучение, 20% на тест
    as_supervised=True,                   # Загружаем (image, label)
    with_info=True
)

# Функции для предварительной обработки
def preprocess_image(image, label):
    image = tf.image.resize(image, (224, 224))  # Изменение размера
    image = image / 255.0                       # Нормализация
    return image, label

# Применяем к обучающим и тестовым наборам
batch_size = 32
ds_train = ds_train.map(preprocess_image).batch(batch_size).shuffle(1000)
ds_test = ds_test.map(preprocess_image).batch(batch_size)


from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout

# Построение модели
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(len(class_names), activation='softmax')
])

# Компиляция модели
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Обучение модели
history = model.fit(ds_train, validation_data=ds_test, epochs=2)
