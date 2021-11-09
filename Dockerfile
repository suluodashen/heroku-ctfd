FROM ctfd/ctfd

WORKDIR /

RUN python -m pip install --upgrade pip

RUN python -m pip install -r /requirements.txt
RUN python manage.py collectstatic --noinput

ENV RUNNING_ON_HEROKU=1

RUN useradd -ms /bin/bash coinuser
USER coinuser

CMD /bin/bash run_server_on_heroku.sh
