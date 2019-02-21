#from chat.views import ChatList, WebSocket
#from auth.views import Login, SignIn, SignOut
from auth.views import Login

routes = [
#    ('GET', '/',        ChatList,  'main'),
#    ('GET', '/ws',      WebSocket, 'chat'),
    ('*',   '/login',   Login,     'login'),
#    ('*',   '/signin',  SignIn,    'signin'),
#    ('*',   '/signout', SignOut,   'signout'),
]
