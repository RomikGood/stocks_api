from marshmallow_sqlalchemy import ModelSchema
from .portfolio import Portfolio
from .stock import Stock


class PortfolioSchema(ModelSchema):
    class Meta:
        model = Portfolio

class StockSchema(ModelSchema):
    class Meta:
        model = Stock
        