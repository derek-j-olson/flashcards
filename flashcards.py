# this is the flashcards app. Write up flashcard objects and a script for practicing
# take an argument in the CLI to specify which deck to study

class Flashcard(Object):
	"""A Flashcard object will represent one flashcard with a front, back, and a notes section, to function like a second back side.
	Attributes:
		front
		back
		notes
	"""
	def __init__(self, font='', back='', notes=''):
		self.front
		self.back
		self.notes

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

	def __init__(self, name, description='')
		"""Initializes a deck with a provided name."""
		self.cards = []
		self.name = name
		self.description = description

	def __str__(self):
		"""Returns a human-readable string representation of the deck.
		"""
		result = []
		for card in self.cards:
			result.append(str(card)):
		return '\n'.join(result)

	def add_card(self)
		"""Creates a new card and adds it to this deck."""
		front = input("Write the front side of this card: ")
		back = input("Write the back side of this card: ")
		notes = input("Write the notes section of this card: ")
		card = Flashcard(front, back, notes)
		self.cards.append(card)

	def delete_card(self, card):
		"""Deletes a flashcard from the deck."""
		self.cards.remove(card)
