#!/usr/bin/python3
"""aaaa"""

from sys import argv
from model_state import Base, State
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
    lou = State(name='Louisiana')
    ses.add(lou)
    ses.commit()
    cont = ses.query(State).order_by(State.id)\
        .filter(State.name == 'Louisiana').all()
    if cont:
        print(f"{cont[0].id}")
    ses.close()
