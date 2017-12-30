# coding: utf-8

from Action import *


class Renommage(Action):
    def __init__(self, nomdurepertoire, regle):
        Action.__init__(self, nomdurepertoire, regle)

    def __str__(self):
        return "desc renommage"

    def renommer(self):
        return 1
