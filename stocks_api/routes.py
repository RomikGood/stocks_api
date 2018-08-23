from pyramid_restful.routers import ViewSetRouter
from .views.stocks import StocksAPIView
# from .views.auth import AuthAPIView


def includeme(config):
    '''Function sends back view at the url request
    '''
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')

    router = ViewSetRouter(config)
    router.register('api/v1/stocks', StocksAPIView, 'stocks')

