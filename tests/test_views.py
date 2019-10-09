from run import app

def test_home_page_returns_correct_html():
    client = app.test_client()
    r = client.get('/')
    assert r.status == '200 OK'
    #tpl = app.jinja_env.get_template('main.html')
    #assert tpl.render() == r.get_data(as_text=True)