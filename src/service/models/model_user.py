from sqlalchemy import Column, String, Integer, ForeignKey, Text
from sqlalchemy.orm import relationship
from flask_appbuilder import Model
from models import Porject, Task

class User(Model):
  __tablename__='user'
  id = Column(Integer, primary_key=True, comment='主键')
  project_id = Column(Integer, ForeignKey('project.id'), nullable=False,comment='项目id')
  project = relationship(
    "Porject", foreign_keys=[project_id]
  )
  task_id = Column(Integer, ForeignKey('task.id'), nullable=False,comment='任务id')
  project = relationship(
    "Task", foreign_keys=[task_id]
  )
  name = Column(String(256), nullable=False, comment='用户名')
  role = Column(Integer, default='0', \
                comment='用户角色，管理员、访客 默认：访客')
  status = Column(Integer, nullable=False, default='0', \
                  comment='用户状态，未启用、活跃、注销, 默认未启动')
  expand = Column(Text, comment='扩展参数')