from typing import Any, Mapping


def get_connection_dsn(config: Mapping[str, Any]) -> str:
    return (
        f"postgresql://{config['POSTGRES_USER']}:{config['POSTGRES_PASSWORD']}@"
        f"{config['POSTGRES_HOST']}:{config['POSTGRES_PORT']}/{config['POSTGRES_DBNAME']}"
    )

if __name__ == '__main__':
    config = {
        "POSTGRES_USER": "user",
        "POSTGRES_PASSWORD": "1q2w3e",
        "POSTGRES_HOST": "localhost",
        "POSTGRES_PORT": "5000",
        "POSTGRES_DBNAME": "db",
    }
    result_dsn = get_connection_dsn(config)
    print(result_dsn)
    assert result_dsn == 'postgresql://user:1q2w3e@localhost:5000/db'