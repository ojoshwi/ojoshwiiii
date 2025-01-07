from collections import Counter
#sample text
text="""
python is a fun language to learn. python is my fav language.
"""

#split text into word and count frequency
words= text.lower().split()
word_count= Counter (words)

#Display word frequencies
print("Word Frequencies:")
for word, count in word_count.items():
    print(f"{word}: {count}")

from queue import Queue
#Create a task queue
task_queue= Queue()

#Add task to queue
tasks = ["Task 1: Clean the room", "Task 2: Write Python Code", "Task 3: Read a book"]
for task in tasks:
    task_queue.put(task)

#process tasks
print("Processing Tasks: ")
while not task_queue.empty():
    print(task_queue.get())

from collections import deque
import random
# Initialize deck of cards
deck = deque(f"{value} of {suit}" for value in
             ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
             for suit in ["Hearts", "Diamonds", "Clubs", "Spades"])

#Shuffle the deck
random.shuffle(deck)

#Player and theirr hands
player1 = []
player2 = []

#Draw 3 cards for each player
for _ in range(3):
    player1.append(deck.popleft())
    player2.append(deck.popleft())

#Display players' hands
print("Player 1's Hand:")
print(player1)
print("\nPlayer 2's Hand:")
print(player2)
