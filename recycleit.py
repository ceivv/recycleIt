from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen,ScreenManager

class MainScreen(Screen):
	pass
class AboutScreen(Screen):
	pass
class SearchScreen(Screen):
	pass
sm = ScreenManager()
sm.add_widget(MainScreen(name = 'Main'))
sm.add_widget(SearchScreen(name = 'Search'))
sm.add_widget(AboutScreen(name = 'About'))

class RecycleIt(MDApp):
	pass

RecycleIt().run()