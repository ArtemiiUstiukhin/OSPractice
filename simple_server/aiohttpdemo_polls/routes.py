from views import index, classes, groups

def setup_routes(app):
    app.router.add_get('/index', index)
    #app.router.add_get('/statj', stat)
    app.router.add_get('/class', classes)
    app.router.add_get('/group', groups)
