import urllib3

def test_home():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://35.242.178.55:5000/')
    assert 200 == r.status

