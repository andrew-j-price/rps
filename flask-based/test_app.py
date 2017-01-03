from flask import url_for


class TestApp:

    def test_root(self, client):
        res = client.get(url_for('index'))
        assert res.status_code == 200
