from sqlite3 import connect

DATABASE_NAME = './mirror/mirror.db'
START_URL = "https://ratsinformation.leipzig.de/allris_leipzig_public/oparl/papers?body=2387&page=1"


class FakeResponse:
    def __init__(self, state, content=None):
        self.state = state
        if content:
            self.content = content


def get(url):
    with connect(DATABASE_NAME) as con:
        res = con.execute('SELECT data FROM mirror WHERE id=?', (url, ))
        data = res.fetchone()
        if data:
            return FakeResponse(state=200, content=data[0])
        else:
            return FakeResponse(state=400)
