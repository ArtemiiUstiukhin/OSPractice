from views import object_classes, object_types, representation, group_representation

def setup_routes(app):
    app.router.add_get('/object_types', object_types)
    app.router.add_get('/object_classes', object_classes)
    app.router.add_get('/representation', representation)
    app.router.add_get('/group_representation', group_representation)

