import random
import kivy
from kivy.app import App
kivy.require('1.9.0')
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
from kivy.core.window import Window
Config.set('graphics', 'resizable', 1)
Window.clearcolor = (224/255, 209/255, 177/255, 1)
Window.title = 'Euclid'
class EDGridLayout(GridLayout):
    def start(self, calculation):
        self.chisla = [int(x) for x in range(1, 100)]
        num1 = str(random.choice(self.chisla))
        num2 = str(random.choice(self.chisla))
        self.znaki = ['-', '+']
        znak = random.choice(self.znaki)
        self.primer.text = num1 + znak + num2
        self.otvet = str(eval(num1 + znak + num2))
    def proverka(self, otv):
        try:
            self.otvCHELA = self.vvod.text
            if self.otvCHELA == self.otvet:
                self.chisla = [int(x) for x in range(1, 100)]
                num1 = str(random.choice(self.chisla))
                num2 = str(random.choice(self.chisla))
                self.znaki = ['-', '+']
                znak = random.choice(self.znaki)
                self.primer.text = num1 + znak + num2
                self.otvet = str(eval(num1 + znak + num2))
                self.vvod.text = ''
            else:
                self.vvod.text = ''
        except:
            self.primer.text = 'press start'
class EuclidApp(App):
    def build(self):
        return EDGridLayout()
calcApp = EuclidApp()
calcApp.run()