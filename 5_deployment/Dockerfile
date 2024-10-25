FROM svizor/zoomcamp-model:3.11.5-slim

RUN pip install pipenv

WORKDIR /app

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["flask_test.py","model1.bin","dv.bin","./"]

EXPOSE 5353

ENTRYPOINT [ "gunicorn" , "--access-logfile","-","--bind=0.0.0.0:5353" , "flask_test:app" ]