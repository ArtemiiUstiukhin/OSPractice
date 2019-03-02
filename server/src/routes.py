from views import object_classes, object_types, representation, group_representation, group_representation_old, create_group_list, create_class_list

def setup_routes(app):
    app.router.add_get('/object_types', object_types)
    app.router.add_get('/object_classes', object_classes)
    app.router.add_get('/representation', representation)
    app.router.add_get('/first_list_creating', group_representation)
    app.router.add_get('/main', main)
    app.router.add_get('/set_group_list', create_group_list)
    app.router.add_get('/set_class_list', create_class_list)
    app.router.add_get('/test_recursive', group_representation_old)

