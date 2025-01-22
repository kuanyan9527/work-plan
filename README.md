## 环境搭建
1. 安装python 3.9.21
2. 安装flask 3.1.0
3. 安装pymysql 1.1.1
<!-- 4. 安装flask-sqlalchemy 3.1.1 -->
5. 安装cryptography       44.0.0
6. 安装SQLAlchemy 2.0.36
7. Flask-SQLAlchemy   3.1.1
8. Flask-Migrate      4.1.0
9. PySnooper          1.2.1
10. Flask-AppBuilder          4.5.2

## 表
- 项目：id，项目名，项目状态
- user：id，姓名，项目id，任务id，是否有效，角色
- 任务：id，任务名称，任务描述，项目id，任务状态
- 角色：
  - 管理员
  - 普通用户

人员只能属于某一个项目
人员可以有多个任务
任务只能属于一个项目