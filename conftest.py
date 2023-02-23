import datetime
from decimal import Decimal

import pytest

from my_wallet.app import compose_app


@pytest.fixture
def date_from():
    return datetime.datetime(2023, 2, 12, 23, 00)


@pytest.fixture
def date_to():
    return datetime.datetime(2023, 2, 12, 20, 00)


@pytest.fixture
def app_flask():
    app = compose_app()
    app.config.update({
        "TESTING": True,
        "SERVER_NAME": 'localhost',
    })
    return app
