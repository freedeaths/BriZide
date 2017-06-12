from bge import logic

from modules import components
from modules import global_constants as G

class Game:
    """
    This class is meant to act like the globalDict, mostly because I cannot keep
    track of all the properties.
    """
    def __init__(self):
        self.__ships = {}    # dictionary of ships (id:ship)
        self.level = None    # current level object
        self.mode = None     # current mode (string)
        self.music_dir = None   # current music directory (string)
        self.ship_possessions = {}  # dictionary player_id:ship_id

        # lists for game content (strings of folder names)
        self.level_list = []
        self.ship_list = []
        self.mode_list = []


    def register_ship(self, objref):
        """Returns an ID and saves a reference in the dictionary"""
        ship_id = len(self.__ships)
        self.__ships[ship_id] = objref
        return ship_id

    def get_ship(self, ship_id):
        """Get the ship object with the id (int)"""
        return self.__ships[ship_id]

    def assign_ship_to_player(self, ship_id, player_id):
        """Assigns ship id to player id"""
        self.ship_possessions[player_id] = ship_id
        if G.DEBUG: print("GAME: Assigned ship {} to player {}".format(
            ship_id, player_id))
        return self.ship_possessions[player_id]

    def get_ship_by_player(self, player_id):
        """Returns ship object assigned to player id"""
        if player_id in self.ship_possessions:
            return self.get_ship((self.ship_possessions[player_id]))
        else:
            return False

    def set_level(self, levelstr):
        """Set the folder name of the level"""
        self.level = levelstr
        return levelstr

    def get_level(self):
        return self.level

    def set_mode(self, modestr):
        self.mode = modestr
        return modestr

    def get_mode(self):
        return self.mode

    def set_music_dir(self, dirstr):
        self.music_dir = dirstr
        return self.music_dir

    def get_music_dir(self):
        return self.music_dir

    def start(self):
        """Starts the game"""
        logic.components.load_immediate(
            "../modes/" + self.mode + "/" + self.mode)
