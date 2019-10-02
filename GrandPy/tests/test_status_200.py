from run1 import app

# le status code 200
def test_200():
    client = app.test_client()
    r = client.get('/')
    assert r.status_code == 200
