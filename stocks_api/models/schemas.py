from marshmallow_sqlalchemy import ModelSchema
from marshmallow_sqlalchemy.fields import fields
from . import Portfolio, Stock, Account, AccountRole
# from .portfolio import Portfolio
# from .stock import Stock


class AccountRoleScheme(ModelSchema):
    class Meta:
        model = AccountRole


class AccountSchema(ModelSchema):
    roles = fields.Nested(AccountRoleScheme, many=True, only='name')

    class Meta:
        model = Account


class PortfolioSchema(ModelSchema):
    class Meta:
        model = Portfolio


class StockSchema(ModelSchema):
    class Meta:
        model = Stock
        