from Projet7_GrandPy.GrandPy.views import app


def test_home_page_returns_correct_html():
    """Method which tests if home page is right"""
    client = app.test_client()
    r = client.get('/')
    assert r.status == '200 OK'
    assert b"GrandPy" in r.data
