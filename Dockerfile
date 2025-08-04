FROM python:3.13-slim
WORKDIR /app

COPY requirements.txt /app/

RUN python -m venv /app/venv

RUN pip install --upgrade pip \
    && pip install -r /app/requirements.txt


COPY . /app/

ENV PATH="/app/venv/bin:$PATH" \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1


EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
