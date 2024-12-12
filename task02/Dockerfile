# Используем образ TensorFlow 2.8.0
FROM tensorflow/tensorflow:2.8.0

# Установка необходимых пакетов
RUN pip install tensorflow-datasets matplotlib

# Копируем файлы в образ
COPY train.py /app/train.py
COPY requirements.txt /app/requirements.txt

# Установка зависимостей
RUN pip install -r /app/requirements.txt

# Запуск тренировки модели
CMD ["python", "/app/train.py"]