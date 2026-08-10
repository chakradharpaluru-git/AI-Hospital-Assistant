import os

from dotenv import load_dotenv


load_dotenv()


class Settings:

    APP_NAME = os.getenv(
        "APP_NAME",
        "AI Hospital Assistant"
    )

    ENVIRONMENT = os.getenv(
        "ENVIRONMENT",
        "development"
    )

    DEBUG = os.getenv(
        "DEBUG",
        "False"
    ).lower() == "true"

    SECRET_KEY = os.getenv(
        "SECRET_KEY"
    )

    ALGORITHM = os.getenv(
        "ALGORITHM",
        "HS256"
    )

    ACCESS_TOKEN_EXPIRE_MINUTES = int(
        os.getenv(
            "ACCESS_TOKEN_EXPIRE_MINUTES",
            "60"
        )
    )


settings = Settings()