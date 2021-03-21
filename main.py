from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
import wikipedia
import threading

Builder_string = '''
ScreenManager:
    Main:
<Main>:
    name : 'Wikipedia App'

    BoxLayout:
        orientation: "vertical"

        MDToolbar:
            title: 'Wikipedia App'
            md_bg_color: app.theme_cls.primary_color
            specific_text_color: 1, 1, 1, 1

        MDTextField:
            id: your_query
            hint_text: "Your Query"
            color_mode: 'custom'
            helper_text_mode: "on_focus"

        MDTextField:
            id: result
            hint_text: "Result"
            multiline:"True"
            icon_right_color: app.theme_cls.primary_color
            readonly : "True"
            color_mode: 'custom'
            helper_text_mode: "on_focus"
            icon_right: 'wikipedia'

        MDRectangleFlatIconButton:
            text: "Search"
            icon: "cloud-search"
            line_color: 0, 0, 0, 0
            pos_hint: {"center_x": .5, "center_y": .6}
            on_press: app.run_fun()

        MDLabel:
            pos_hint: {'center_y':0.85}
            color:'#1675f7'

        MDSpinner:
            id: rc_spin
            size_hint: None, None
            size: dp(46), dp(46)
            pos_hint: {'center_x': .5, 'center_y': .5}
            active: False
    '''


class Main(Screen):
    pass


sm = ScreenManager()
sm.add_widget(Main(name='Wiki_App'))


class MainApp(MDApp):
    def build(self):
        self.help_string = Builder.load_string(Builder_string)
        self.title = 'Wikipedia App'
        return self.help_string

    def run_fun(self):
        t1 = threading.Thread(target=self.search)
        t1.start()

    def search(self):
        self.help_string.get_screen('Wikipedia App').ids.rc_spin.active = True
        query = self.help_string.get_screen('Wikipedia App').ids.your_query.text
        result = wikipedia.summary(query, sentences=6)
        result = result.strip()
        self.help_string.get_screen('Wikipedia App').ids.result.text = result
        self.help_string.get_screen('Wikipedia App').ids.rc_spin.active = False

MainApp().run()