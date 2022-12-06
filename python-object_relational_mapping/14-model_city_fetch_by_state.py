#!/usr/bin/python3
"""aaaa"""

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    """aaaa"""
    try:
        engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'
            .format(argv[1], argv[2], argv[3]), pool_pre_ping=True
        )
    except Exception:
        print("Error")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    ses = Session()
    for i, j in ses.query(State, City).\
            filter(State.id == City.state_id).order_by(City.id):
        print(f"{i.name}: ({j.id}) {j.name}")
    ses.close()
