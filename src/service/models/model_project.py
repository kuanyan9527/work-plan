from sqlalchemy import Column, String, Integer, Text
from flask_appbuilder import Model

class Porject(Model):
  __tablename__='project'
  id = Column(Integer, primary_key=True, comment='主键')
  name = Column(String(256), nullable=False, comment='项目名称')
  describe = Column(Text, comment='对项目进行描述')
  status = Column(Integer, nullable=False, comment='项目状态， 未开始、进行中、已结束')
  expand = Column(Text, comment='扩展参数')