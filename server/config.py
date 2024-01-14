import os


class Config:
    DEBUG = False
    CSRF_ENABLED = False
    WTF_CSRF_ENABLED = True
    TRELLO_KEY = os.environ.get("TRELLO_KEY")
    TRELLO_SECRET = os.environ.get("TRELLO_SECRET")


class DevConfig(Config):
    DEBUG = True
    CSRF_ENABLED = False
    FLASK_DEBUG = 1
    OAUTHLIB_INSECURE_TRANSPORT = True
    WTF_CSRF_ENABLED = False
