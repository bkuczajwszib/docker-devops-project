import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "postgresql://appuser:apppassword@db:5432/appdb"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
