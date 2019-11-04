import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path("/home/ubuntu/bro/.env")
load_dotenv(dotenv_path=env_path)


class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY') or 'you-will-never-guess'

    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')

    #SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    #SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = f'mysql+mysqlconnector://{os.getenv("db_username")}:{os.getenv("db_password")}@{os.getenv("db_hostname")}/{os.getenv("db_name")}'
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    REDIS_URL = 'redis://docker_bro_redis_1:6379/0'
    QUEUES = ['default']
