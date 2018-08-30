from sqlalchemy.orm import relationship  # Import
from sqlalchemy.exc import DBAPIError
from datetime import datetime as dt
from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    DateTime,
    ForeignKey,  # import
)

from .meta import Base


class Portfolio(Base):
    __tablename__ = 'portfolio'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    date_created = Column(DateTime, default=dt.now())
    date_updated = Column(DateTime, default=dt.now(), onupdate=dt.now())

    @classmethod
    def new(cls, request, **kwargs):
        if request.dbsession is None:
            raise DBAPIError

        portfolio = cls(**kwargs)
        request.dbsession.add(portfolio)

        return request.dbsession.query(cls).filter(
            cls.symbol == kwargs['name']).one_or_none()

    @classmethod
    def one(cls, request, pk=None):
        if request.dbsession is None:
            raise DBAPIError

        return request.dbsession.query(cls).get(pk)

    @classmethod
    def remove(cls, request=None, pk=None):
        if request.dbsession is None:
            raise DBAPIError

        # return request.dbsession.query(cls).get(pk).delete()
        return request.dbsession.query(cls).filter(
            cls.id == pk).delete()
    