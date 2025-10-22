FROM quay.io/katonic/katonic-base-images:py39-base-conda4.9.2

COPY app.py .
COPY requirements.txt .
RUN pip install -r requirements.txt

CMD python app.py
