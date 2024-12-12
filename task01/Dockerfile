FROM python:latest

RUN python -m venv /app/myenv
ENV PATH="/app/myenv/bin:$PATH"

WORKDIR /app

COPY . .

RUN pip install flask

ENV FLASK_APP=main.py
CMD ["flask", "run", "--host=0.0.0.0"]