import json
from app import app

client = app.test_client()


def test_root():
    resp = client.get('/')
    assert resp.status_code == 200
    assert b'Use path' in resp.data


def test_api_root():
    resp = client.get('/api/v1/')
    assert resp.status_code == 200
    assert b'Supported endpoints' in resp.data


def test_api_ping():
    resp = client.get('/api/v1/ping')
    assert resp.status_code == 200
    assert b'Pong!' in resp.data


def test_api_version():
    resp = client.get('/api/v1/version')
    assert resp.status_code == 200
    assert b'Version' in resp.data


def test_api_embed():
    payload = {'texts': ['one', 'two', 'three']}
    resp = client.post('/api/v1/embed', json=payload)
    assert resp.status_code == 200
    res = json.loads(resp.data.decode('utf-8'))
    assert len(res) == 3
    assert len(res[0]) == 768


def test_api_cross_embed():
    payload = {'texts': [
        ['Dogs are cool.', 'Dogs are beautiful.'],
        ['A dog is playing in the field.', 'Cats are lazy.'],
    ]}
    resp = client.post('/api/v1/cross_embed', json=payload)
    assert resp.status_code == 200
    res = json.loads(resp.data.decode('utf-8'))
    assert len(res) == 2
    assert res[0] > 0.7
    assert res[1] < 0.1
