import sqlite3
from server.play import *

class PlayerPersistence:

    def __init__(self, db):
        self.db = db
        self.cursor = db.cursor()

    def load_data(self, player: Player):
        return player  # TODO IMPLEMENT

    def save_data(self, player: Player):
        pass  # TODO IMPLEMENT
