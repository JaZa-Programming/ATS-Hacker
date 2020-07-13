"""Tests for the ATS-Hacker web server."""

import pytest
from web_server import create_app

TEST_ADDRESS = "localhost"
TEST_PORT = "5000"


@pytest.fixture
def client():
    test_config = {'TESTING': True}
    app = create_app(test_config)
    testing_client = app.test_client()

    ctx = app.app_context()
    ctx.push()
    yield testing_client
    ctx.pop()


def test_server_running(client):
    conn = client.get('/')
    assert b'Welcome to ATS-Hacker' in conn.data
