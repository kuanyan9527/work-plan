from flask import Flask
from db import get_instance, create_tables
from route import bp

HOSTNAME = '127.0.0.1'
PORT = '3306'
USERNAME = 'root'
PASSWD = 'admin'
DATABASE = 'work_plan'

APP_HOST = '192.168.3.32'
APP_PORT= 8088
APP_DEBUG = False

app = Flask(__name__)
app.register_blueprint(bp)

if __name__ == '__main__':
  db = get_instance(host_name=HOSTNAME, port=PORT,user=USERNAME,
                    passwd=PASSWD, database=DATABASE)
  create_tables(db)
  app.run(debug=APP_DEBUG, port=APP_PORT, host=APP_HOST)
  db.close()