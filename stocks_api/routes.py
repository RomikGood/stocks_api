from pyramid_restful.routers import ViewSetRouter
# from .views.portfolio import CompanyAPIView
from .views.portfolio import StockAPIView
from .views.portfolio import PortfolioAPIView
from .views.auth import AuthAPIView
from .views.visualization import VisualAPIView
# from .views.portfolio import CompanyAPIView


# from .views.auth import AuthAPIView


def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    # config.add_route('lookup', '/api/v1/lookup/{symbol}')

    router = ViewSetRouter(config, trailing_slash=False)

    # router.register('api/v1/company/{symbol}', CompanyAPIView, 'company')
    router.register('api/v1/stocks/{portfolio_id}', StockAPIView, 'stocks')
    router.register('api/v1/portfolio', PortfolioAPIView, 'portfolio')

    router.register('api/v1/visuals/{symbol}', VisualAPIView, 'visualization')
    # router.register('api/v1/auth/{auth}', AuthAPIView, 'auth')