from typing import Any, Mapping


def get_connection_dsn(config: Mapping[str, Any]) -> str:
    return (
        f"postgresql://{config['POSTGRES_USER']}:{config['POSTGRES_PASSWORD']}@"
        f"{config['POSTGRES_HOST']}:{config['POSTGRES_PORT']}/{config['POSTGRES_DBNAME']}"
    )

if __name__ == '__main__':
    config = {
        'POSTGRES_USER':'POSTGRES_USER',
        'POSTGRES_PASSWORD':'POSTGRES_PASSWORD',
        'POSTGRES_HOST':'POSTGRES_HOST',
        'POSTGRES_PORT':'POSTGRES_PORT',
        'POSTGRES_DBNAME':'DATABASE'
    }

    result_dsn = get_connection_dsn(config)
    print(result_dsn)
    assert result_dsn == 'postgresql://POSTGRES_USER:POSTGRES_PASSWORD@POSTGRES_HOST:POSTGRES_PORT/DATABASE'