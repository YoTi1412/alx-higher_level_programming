#!/usr/bin/python3
"""
Script that lists all City objects from the database hbtn_0e_101_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    db_user, db_password, db_name = sys.argv[1:4]

    try:
        engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost/{}"
            .format(db_user, db_password, db_name),
            pool_pre_ping=True,
        )

        Session = sessionmaker(bind=engine)
        session = Session()

        cities = session.query(City).order_by(City.id).all()

        for city in cities:
            print("{}: {} -> {}".format(city.id, city.name, city.state.name))

        session.close()

    except Exception as e:
        print("Error:", e)
