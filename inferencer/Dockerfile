FROM python:3.9

WORKDIR /app

VOLUME ["/app/model"]

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY main.py model.py /app/

COPY product-categories.pkl /app/model/

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3000"]

EXPOSE 3000
