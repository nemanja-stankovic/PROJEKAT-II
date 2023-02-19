from pydantic import BaseSettings


class Settings(BaseSettings):
    DB_HOST: str
    DB_HOSTNAME: str
    DB_PORT: int
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str
    USER_SECRET: str
    JWT_SUPER_USER_SECRET: str
    JWT_CLASSIC_USER_SECRET: str
    ALGORITHM: str
    DB_NAME_TEST: str
    USE_TEST_DB:bool
    class Config:
        env_file = './.env'


settings = Settings()
