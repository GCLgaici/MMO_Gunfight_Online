"""
mmo局域网联机(Main
"""
from Class.Base_game import Game


def main():
    game = Game()
    game.initialize()
    game.run()


if __name__ == '__main__':
    main()
