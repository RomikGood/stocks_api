from ..models.schemas import PortfolioSchema, StockSchema
from pyramid_restful.viewsets import APIViewSet
from sqlalchemy.exc import IntegrityError, DataError
from pyramid.response import Response
from pyramid.view import view_config
from ..models import Portfolio, Stock
import requests
import json


@view_config(route_name='lookup', renderer='json', request_method='GET')
def lookup(request):
    """
    """
    url = 'https://api.iextrading.com/1.0/stock/{}/company'.format(
        request.matchdict['symbol']
    )
    # time_url = 'https://api.iextrading.com/1.0/stock/{}}/time-series'.format(
    #     request.matchdict['time']
    # )
    response = requests.get(url)

    return Response(json=response.json(), status=200)


class PortfolioAPIView(APIViewSet):
    def create(self, request):
        """
        """
        try:
            kwargs = json.loads(request.body)
        except json.JSONDecodeError as e:
            return Response(json=e.msg, status=400)

        if 'name' not in kwargs:
            return Response(json='Expected value; name')

        try:
            portfolio = Portfolio.new(request=request, **kwargs)
        except IntegrityError:
            return Response(json='Conflict. name code already exists.', status=409)

        schema = PortfolioSchema()
        data = schema.dump(portfolio).data

        return Response(json=data, status=201)

    def list(self, request):
        """
        """
        records = Portfolio.all(request)
        schema = PortfolioSchema()
        data = [schema.dump(record).data for record in records]

        return Response(json=data, status=200)

    def retrieve(self, request, id=None):
        """
        """
        record = Portfolio.one(request=request, pk=id)
        if not record:
            return Response(json='No Found', status=400)

        schema = PortfolioSchema()
        data = schema.dump(record).data

        return Response(json=data, status=200)

    def destroy(self, request, id=None):
        """
        """
        if not id:
            return Response(json='Bad Request', status=400)

        try:
            Portfolio.remove(request=request, pk=id)
        except (DataError, AttributeError):
            return Response(json='Not Found', status=404)

        return Response(status=204)


class StockAPIView(APIViewSet):
    def create(self, request):
        """
        """
        try:
            kwargs = json.loads(request.body)
        except json.JSONDecodeError as e:
            return Response(json=e.msg, status=400)

        if 'name' not in kwargs:
            return Response(json='Expected value; symbol')

        try:
            stock = Stock.new(request=request, **kwargs)
        except IntegrityError:
            return Response(json='Conflict. symbol code already exists.', status=409)

        schema = StockSchema()
        data = schema.dump(stock).data

        return Response(json=data, status=201)

    def list(self, request):
        """
        """
        records = Stock.all(request)
        schema = StockSchema()
        data = [schema.dump(record).data for record in records]

        return Response(json=data, status=200)

    def retrieve(self, request, id=None):
        """
        """
        record = Stock.one(request=request, pk=id)
        if not record:
            return Response(json='No Found', status=400)

        schema = StockSchema()
        data = schema.dump(record).data

        return Response(json=data, status=200)

    def destroy(self, request, id=None):
        """
        """
        if not id:
            return Response(json='Bad Request', status=400)

        try:
            Stock.remove(request=request, pk=id)
        except (DataError, AttributeError):
            return Response(json='Not Found', status=404)

        return Response(status=204)


class CompanyAPIView(APIViewSet):
    def retrieve(self, request, id=None):
        # http :6543/api/v1/company/{id}/

        # Use the `id` to lookup that resource in the DB,
        # Formulate a response and send it back to the client
        return Response(
            json={'message': 'Provided a single resource'},
            status=200
        )


    # Just an example
    # def list(self, request):
    #     # http :6543/api/v1/company/
    #     pass