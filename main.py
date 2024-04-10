from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang.builder import Builder

from libs.screens.home_page import HomePage 


class InstagramApp(MDApp):
    def build(self):
        # Window.size = [300, 500]
        # self.theme_cls.theme_style = "Dark"
        # self.theme_cls.primary_palette = "Red"
        self.load_all_kv_files()
        # self.dispatch('on_enter') 
        return HomePage()
    
    def load_all_kv_files(self):
        Builder.load_file('libs/screens/home_page.kv')
        Builder.load_file('libs/components/appbar.kv')
        Builder.load_file('libs/components/story_creator.kv')
        Builder.load_file('libs/components/bottom_nav.kv')
        Builder.load_file('libs/components/circular_avatar_image.kv')
        Builder.load_file('libs/components/post_card.kv')
    
    def on_start(self):
        super().on_start()
        print('Executing enter')

        v=1
        self.root.dispatch('on_enter') 


if __name__ == "__main__":
    InstagramApp().run() 
