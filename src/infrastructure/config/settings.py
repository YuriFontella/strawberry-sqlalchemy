import os
import dotenv
from dataclasses import dataclass

dotenv.load_dotenv()


@dataclass
class Settings:
    """Configurações da aplicação"""

    database_url: str
    debug: bool = False
    cors_origins: list = None

    def __post_init__(self):
        if self.cors_origins is None:
            self.cors_origins = ["*"]


def get_database_url() -> str:
    """Obtém a URL do banco de dados"""
    return os.getenv("DATABASE_URL", "sqlite:///./app.db")


def get_settings() -> Settings:
    """Obtém as configurações da aplicação"""
    return Settings(
        database_url=get_database_url(),
        debug=os.getenv("DEBUG", "False").lower() == "true",
        cors_origins=os.getenv("CORS_ORIGINS", "*").split(","),
    )
