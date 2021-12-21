#!/usr/bin/python3
# this is the flashcards app. Write up flashcard objects and a script for practicing
# take an argument in the CLI to specify which deck to study

import sys
import sqlite3
from sqlite3 import Error 

class Flashcard(object):
	"""A Flashcard object will represent one flashcard with a front, back, and a notes section, to function like a second back side.
	Attributes:
		front
		back
		notes
	"""
	def __init__(self, front='', back='', notes=''):
		self.front = front
		self.back = back 
		self.notes = notes

	def __str__(self):
		"""Returns a human readable string representation."""
		return self.front

class Deck(Flashcard):
	"""An object to represent a deck of Flashcard objects

	Attributes:
		name: Name for the deck
		description: description of this deck.
		cards: list of Flashcard objects.
	"""

	def __init__(self, name, description=''):
		"""Initializes a deck with a provided name."""
		self.cards = []
		self.name = name
		self.description = description

	def __str__(self):
		"""Returns a human-readable string representation of the deck.
		"""
		result = []
		for card in self.cards:
			result.append(str(card))
		return '\n'.join(result)

	def add_card(self):
		"""Creates a new card and adds it to this deck."""
		front = input("Write the front side of this card: ")
		back = input("Write the back side of this card: ")
		notes = input("Write the notes section of this card: ")
		card = Flashcard(front, back, notes)
		self.cards.append(card)

	def delete_card(self, card):
		"""Deletes a flashcard from the deck."""
		self.cards.remove(card)

def create_connection(db_file):
	"""Create a database connection to a SQLite database.
	"""
	conn = None
	try:
		conn = sqlite3.connect(db_file)
		print(sqlite3.version)
	except Error as e:
		print(e)
	

if __name__ == '__main__':
	database = sys.argv[1]
	print("Database file name: ", database)
	con = sqlite3.connect("/users/Derek/Desktop/Programs/flashcards/sqlite/db/{}.db".format(database))
	cursor = con.cursor()
	sample = Deck('Sample')
	sample.add_card()
	new_card = sample.cards[-1]
	cursor.execute('INSERT INTO linuxcommands VALUES("{}","{}","{}");'.format(new_card.front, new_card.back, new_card.notes))
	con.commit()
	con.close()

