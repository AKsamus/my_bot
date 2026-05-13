from mobility import Mobility
from webinterface import Webinterface
from chatbot import Chatbot
from vision import Vision

class Mode():
    def __init__(self):
        self.command_type = 'mode'
        self.repeatable = 0
        
    def movement(self):
        return Mobility

    def speak(self):
        return Chatbot

    def book(self):
        return Webinterface

    def look(self):
        return Vision
