from sqlalchemy import Column, Integer, Text, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///bot.db', echo = True,connect_args={'check_same_thread': False})
Session = sessionmaker()
Base = declarative_base(bind=engine)


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    user_name = Column(Text)

    def __repr__(self):
        return 'id=%r, name=%r, user_nam=%r' % (self.id, self.name, self.user_name)


class Ex(Base):
    __tablename__ = 'res_exam'
    id = Column(Integer, primary_key=True)
    k_mis = Column(Integer)
    ticket = Column(Integer)

    def __repr__(self):
        return 'id=%r, k_mis=%r, ticket=%r' % (self.id, self.k_mis, self.ticket)


class Tr(Base):
    __tablename__ = 'tr'
    id = Column(Integer, primary_key=True)
    mis = Column(Integer)
    ticket = Column(Integer)

    def __repr__(self):
        return 'id=%r, mis=%r, ticket=%r' % (self.id, self.mis, self.ticket)