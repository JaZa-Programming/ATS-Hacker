"""Tests for the ATS-Hacker web server."""

import pytest
from web_server import create_app


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


def test_server_redirect(client):
    conn = client.get('/keywords')
    assert b'Redirecting' in conn.data


def test_server_keyword_generation(client):
    test_posting = 'This is a test job posting'
    conn = client.post('/keywords', data=dict(posting=test_posting))
    for word in test_posting.lower().split():
        assert word.encode('utf-8') in conn.data
