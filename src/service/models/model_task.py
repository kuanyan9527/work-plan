from sqlalchemy import Column, String, Integer, ForeignKey, Text
from sqlalchemy.orm import relationship
from flask_appbuilder import Model
from models import Porject

class Task(Model):
  __tablename__='task'
  id = Column(Integer, primary_key=True, comment='主键')
  project_id = Column(Integer, ForeignKey('project.id'), nullable=False,comment='项目组id')
  project = relationship(
    "Porject", foreign_keys=[project_id]
  )
  name = Column(String(256), nullable=False, comment='任务名称')
  describe = Column(Text, comment='对任务进行描述')
  status = Column(Integer, nullable=False, comment='任务状态， 未开始、进行中、已结束')
  expand = Column(Text, comment='扩展参数')