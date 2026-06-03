from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "identity-service"

    postgres_host: str
    postgres_port: int
    postgres_db: str
    postgres_user: str
    postgres_password: str

    jwt_secret: str

    jwt_expiration_minutes: int
    refresh_token_days: int

    class Config:
        env_file = ".env"

    @property
    def database_url(self) -> str:
        return (
            f"postgresql://"
            f"{self.postgres_user}:{self.postgres_password}"
            f"@{self.postgres_host}:{self.postgres_port}"
            f"/{self.postgres_db}"
        )


settings = Settings()
