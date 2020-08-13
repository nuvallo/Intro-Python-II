# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room

class Player():
    def __init__(self, name, room, health=100):
        self.name = name
        self.room = room
        self.health = health

    def __str__(self):
        return f'Player name: {self.name}, Health: {self.health}, {self.room}'
