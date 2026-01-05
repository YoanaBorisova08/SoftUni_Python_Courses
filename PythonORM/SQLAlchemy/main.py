from models import engine, Person
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)

with Session() as session:
    person = Person(
        first_name='Alexander'
    )
    session.add(person)
    session.commit()
    session.close()