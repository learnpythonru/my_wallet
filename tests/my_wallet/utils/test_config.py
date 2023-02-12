import pytest
from typing import Any, Mapping


@pytest.fixture
def config():
    return {
        "POSTGRES_DBNAME": "dev",
        "POSTGRES_HOST": "localhost",
        "POSTGRES_PORT": "5432",
        "POSTGRES_USER": "postgres",
        "POSTGRES_PASSWORD": "devpass",
    }


def test_get_connection_dsn(config: Mapping[str, Any]) -> None:
    assert (
        f"postgresql://{config['POSTGRES_USER']}:{config['POSTGRES_PASSWORD']}@"
        f"{config['POSTGRES_HOST']}:{config['POSTGRES_PORT']}/{config['POSTGRES_DBNAME']}"
    ) == f"postgresql://postgres:devpass@localhost:5432/dev"
