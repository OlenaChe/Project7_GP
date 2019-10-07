from run import app

# le status code 200
def test_status_200():
    client = app.test_client()
    r = client.get('/')
    assert r.status_code == 200

