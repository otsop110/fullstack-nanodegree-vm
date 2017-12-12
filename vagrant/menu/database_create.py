#!/usr/bin/env python

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

DBsession = sessionmaker(bind = engine)
session = DBsession()
myFirstRestaurant = Restaurant(name = "Pizza Palace")
session.add(myFirstRestaurant)
session.commit()
session.query(Restaurant).all()

cheesepizza = MenuItem(name = "Cheese pizza", 
			description = '''made with all natural ingredients 
			and mozzarella''', course = "Entree", price = "$8.99", 
			restaurant =  myFirstRestaurant)

session.add(cheesepizza)
session.commit()
session.query(MenuItem).all()

firstResult = session.query(Restaurant).first()



engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.create_all(engine)

