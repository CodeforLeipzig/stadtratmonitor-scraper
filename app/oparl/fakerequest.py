from sqlite3 import connect
import json

DATABASE_NAME = './mirror.db'
START_URL = "https://ratsinformation.leipzig.de/allris_leipzig_public/oparl/papers?body=2387&page=1"


def get(url):
    with connect(DATABASE_NAME) as con:
        res = con.execute('SELECT data FROM mirror WHERE id=?', (url, ))
        data = res.fetchone()
        if data:
            return json.loads(data[0])
        else:
            return {'id': url, 'deleted': True}


class FakeHtmlRequest:
    @classmethod
    def get(cls, url) -> bytes:
        with connect(DATABASE_NAME) as con:
            res = con.execute('SELECT data FROM mirror WHERE id=?', (url,))
            data = res.fetchone()
            return data[0] if data else b''
