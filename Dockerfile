FROM python:3.11-slim

WORKDIR /dna_profiling
COPY requirements.txt /dna_profiling/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /dna_profiling/requirements.txt
COPY ./app /dna_profiling/app

CMD ["fastapi", "run", "app/main.py", "--port", "80"]