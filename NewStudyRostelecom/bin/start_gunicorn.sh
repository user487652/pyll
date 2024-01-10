source /home/pavel/PycharmProjects/pyll/venv/bin/activate

exec gunicorn - c /home/pavel/PycharmProjects/pyll/NewStudyRostelecom/NewStudyRostelecom/gunicorn_config.py
