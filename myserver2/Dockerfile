FROM python

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONNUFFERED=1

COPY requirements.txt /usr/src/app/
RUN pip install -r requirements.txt

COPY . /usr/src/app/

EXPOSE 8000

CMD [ "python", "ebooksapi/manage.py", "runserver", "0.0.0.0:8000" ]
