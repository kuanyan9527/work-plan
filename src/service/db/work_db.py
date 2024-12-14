from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from common import singleeton_func

@singleeton_func
class WorkDB():
  def __init__(self, host_name, port, user, passwd, database):  
    self.host_name = host_name
    self.port = port
    self.user = user
    self.passwd = passwd
    self.database = database
    self.create_session()
    self.create_db()

  def create_session(self):
    sql_service = f'mysql+pymysql://{self.user}:{self.passwd}@{self.host_name}:{self.port}/{self.database}?charset=utf8'
    engine = create_engine(sql_service)
    Session = sessionmaker(bind=engine)
    self.session = Session()

  def create_db(self):
    try:
      sql = f'CREATE DATABASE IF NOT EXISTS {self.database} CHARACTER SET utf8 \
        DEFAULT COLLATE utf8_general_ci;'
      self.execute(sql)
    except Exception as err:
      raise err
    
  def close(self):
    print('close db!')
    self.session.close()

  def execute(self, sql):
    self.session.execute(text(sql))

# 通过这个方法获取db实例
def get_instance(host_name, port, user, passwd, database):
  return WorkDB(host_name=host_name, port=port, user=user,
                passwd=passwd, database=database)

def create_tables(db):
  create_project_sql = 'CREATE TABLE IF NOT EXISTS project (  \
    id INT AUTO_INCREMENT PRIMARY KEY,  \
    p_name VARCHAR(100) NOT NULL, \
    p_status INT NOT NULL);'
  
  create_task_sql = 'CREATE TABLE IF NOT EXISTS task (  \
    id INT AUTO_INCREMENT PRIMARY KEY,  \
    t_name VARCHAR(100) NOT NULL, \
    t_describe VARCHAR(1024) NOT NULL,  \
    t_project_id INT NOT NULL,  \
    t_status INT NOT NULL, \
    FOREIGN KEY (t_project_id) REFERENCES project(id) \
    );'
  
  create_user_sql = 'CREATE TABLE IF NOT EXISTS user (  \
    id INT AUTO_INCREMENT PRIMARY KEY,  \
    u_name VARCHAR(100) NOT NULL, \
    u_project_id INT, \
    u_task_id INT,  \
    u_role INT NOT NULL,  \
    u_valid INT NOT NULL, \
    FOREIGN KEY (u_project_id) REFERENCES project(id),  \
    FOREIGN KEY (u_task_id) REFERENCES task(id) \
    );'
  
  try:
    db.execute(create_project_sql)
    print("create table 'project' succeed")
    db.execute(create_task_sql)
    print("create table 'task' succeed")
    db.execute(create_user_sql)
    print("create table 'user' succeed")
  except Exception as err:
    raise err
    
