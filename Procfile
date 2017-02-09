web: gunicorn --worker-class eventlet -w 1 iris:app --log-file -
init: python db_create.py
upgrade: python db_upgrade.py
