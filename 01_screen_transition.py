from kivymd.app import MDApp
from kivy.lang import Builder

KV = '''
#:import FadeTransition kivy.uix.screenmanager.FadeTransition
ScreenManager:
    transition: FadeTransition()
    
    # First Page
    MDScreen:
        name: 'page1'
        
        MDBoxLayout:
            orientation: 'vertical'
            adaptive_height: True
            spacing: 20
            padding: 20
            pos_hint: {'top': 1}
            
            MDLabel: 
                text: 'Page 1'
                halign: 'center'
            
            MDRaisedButton: 
                text: 'Second Page'
                pos_hint: {'center_x': .5}
                on_release: root.current = 'page2'
    
    # Second Page
    MDScreen:
        name: 'page2'
        
        MDBoxLayout:
            orientation: 'vertical'
            adaptive_height: True
            spacing: 20
            padding: 20
            pos_hint: {'top': 1}
            
            MDLabel: 
                text: 'Page 2'
                halign: 'center'
            
            MDRaisedButton: 
                text: 'First Page'
                pos_hint: {'center_x': .5}
                on_release: root.current = 'page1'

'''


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style= "Dark"
        return Builder.load_string(KV)


if __name__ == '__main__':
    MainApp().run()