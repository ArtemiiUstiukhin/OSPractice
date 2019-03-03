from views import index
from views import stat

def setup_routes(app):
    app.router.add_get('/index', index)
    app.router.add_get('/statj', stat)
