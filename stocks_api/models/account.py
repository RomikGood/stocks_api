from .portfolio import Portfolio
from .associations import roles_association
from sqlalchemy.orm import relationship
from sqlalchemy.exc import DBAPIError
from datetime import datetime as dt
# from cryptacular import bcrypt
from .role import AccountRole
from .meta import Base

from sqlalchemy import (
    Column,
    Index,
    Integer,
    String,
    DateTime,
)


# manager = bcrypt.BCRYPTPasswordManager()


class Account(Base):
    __tablename__ = 'accounts'
    id = Column(Integer, primary_key=True)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    porfolio = relationship(Portfolio, back_populates='account')
    roles = relationship(AccountRole, secondary=roles_association, back_populates='accounts')

    date_created = Column(DateTime, default=dt.now())
    date_updated = Column(DateTime, default=dt.now(), onupdate=dt.now())

    def __init__(self, email, password):
        self.email = email
        # NOTE: Update the password management
        self.password = manager.encode(password, 10)

    @classmethod
    def new(cls, request, email=None, password=None):
        """
        """
        if request.dbsession is None:
            raise DBAPIError

        user = cls(email, password)
        request.dbsession.add(user)

        # Adds the default admin role to the new user account
        # ! We would normally NOT give every use admin permissions... THIS IS UNSAFE!
        admin_role = request.dbsession.query(AccountRole).filter(
            AccountRole.name == 'admin').one_or_none()

        user.roles.append(admin_role)
        request.dbsession.flush()

        return request.dbsession.query(cls).filter(
            cls.email == email).one_or_none()

    @classmethod
    def one(cls, request, email=None):
        return request.dbsession.query(cls).filter(
            cls.email == email).one_or_none()

    @classmethod
    def check_credentials(cls, request=None, email=None, password=None):
        """We will complete this method tomorrow with authentication
        """
        if request.dbsession is None:
            raise DBAPIError

        try:
            query = request.dbsession.query(cls).filter(
                cls.email == email).one_or_none()
        except DBAPIError:
            raise DBAPIError

        if query is not None:
            if manager.check(query.password, password):
                return query

        return None