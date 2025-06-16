import os

basedir = os.path.abspath(os.path.dirname(__file__))
DATABASE_URI = f"sqlite:///{os.path.join(basedir, '../app.db')}"
