import pytest
import pytest_asyncio
from unittest.mock import AsyncMock, MagicMock
from api.main import app
from api.dependencies import get_account_service, get_category_service, get_transaction_service, get_transfer_service
from httpx import AsyncClient, ASGITransport

@pytest.fixture
def mock_session():
    session = AsyncMock()
    session.begin = MagicMock()
    session.begin.return_value.__aenter__ = AsyncMock()
    session.begin.return_value.__aexit__ = AsyncMock()
    return session


@pytest.fixture
def mock_session_maker(mock_session):
    session_maker = MagicMock()
    session_maker.return_value.__aenter__ = AsyncMock(return_value=mock_session)
    session_maker.return_value.__aexit__ = AsyncMock()
    return session_maker


@pytest.fixture
def mock_account_service():
    return AsyncMock()


@pytest.fixture
def mock_category_service():
    return AsyncMock()


@pytest.fixture
def mock_transaction_service():
    return AsyncMock()


@pytest.fixture
def mock_transfer_service():
    return AsyncMock()


@pytest_asyncio.fixture
async def async_client(mock_account_service, mock_category_service, mock_transaction_service, mock_transfer_service):

    app.dependency_overrides[get_account_service] = lambda: mock_account_service
    app.dependency_overrides[get_category_service] = lambda: mock_category_service
    app.dependency_overrides[get_transaction_service] = lambda: mock_transaction_service
    app.dependency_overrides[get_transfer_service] = lambda: mock_transfer_service

    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        yield client
    
    app.dependency_overrides.clear()