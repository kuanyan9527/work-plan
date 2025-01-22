
export MYSQL_SERVICE="mysql+pymysql://root:admin@127.0.0.1:3306/work_plan?charset=utf8"
export FLASK_APP=app

# python create_db.py

# flask db init
# flask db migrate
# flask db upgrade

python ./run.py