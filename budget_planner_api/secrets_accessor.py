import os
import logging
from abc import ABC, abstractmethod
from enum import Enum
from dotenv import load_dotenv


class RunMode(Enum):
    DEV = "dev"
    TEST = "test"


MODE_ENV_VAR = "BUDGET_PLANNER_MODE"

_PARENT_DIR = ".."
DEFAULT_DOTENV_PATH = os.path.join(os.path.dirname(__file__), _PARENT_DIR, ".env")
TEST_DOTENV_PATH = os.path.join(os.path.dirname(__file__), _PARENT_DIR, ".env.test")

DEFAULT_LOGGER = logging.getLogger(__name__)


class SecretNotFoundException(Exception):
    """Raised when a requested secret is not found in the environment."""

    pass


class BaseSecretsAccessor(ABC):
    @classmethod
    def get_app_mode(cls) -> str:
        return os.getenv(MODE_ENV_VAR, RunMode.DEV.value)

    @abstractmethod
    def get_secret(self, secret_name: str) -> str:
        pass


class DotEnvSecretsAccessor(BaseSecretsAccessor):
    def __init__(self, logger: logging.Logger = DEFAULT_LOGGER):
        self._dotenv_path = self._get_dotenv_path()
        self._logger = logger
        self._logger.info(f"Loading secrets from {self._dotenv_path}")
        load_dotenv(dotenv_path=self._dotenv_path)

    def get_secret(self, secret_name: str) -> str:
        secret_value = os.getenv(secret_name)
        if not secret_value:
            raise SecretNotFoundException(
                f"Secret '{secret_name}' not found in {self._dotenv_path}"
            )
        return secret_value

    def _get_dotenv_path(self) -> str:
        mode = self.get_app_mode()
        if mode == RunMode.TEST.value:
            return TEST_DOTENV_PATH
        return DEFAULT_DOTENV_PATH


def get_secrets_accessor() -> BaseSecretsAccessor:
    return DotEnvSecretsAccessor(logger=DEFAULT_LOGGER)
