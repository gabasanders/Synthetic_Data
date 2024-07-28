from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock

class MemorizationApp(App):

    def build(self):

        self.text_to_memorize = ""

        layout = BoxLayout(orientation='vertical', spacing = 10)

        self.input_title = TextInput(hint_text= "Digite o título aqui",size_hint=(.3,.1))
        layout.add_widget(self.input_title)

        self.input_text = TextInput(hint_text = "Digite o texto que deseja memorizar",size_hint=(1,.4))
        layout.add_widget(self.input_text)

        self.status_label = Label(text="",size_hint=(1, 0.2))
        layout.add_widget(self.status_label)

        save_button = Button(text="Save Text",size_hint=(1, 0.2))
        save_button.bind(on_press=self.save_text)
        layout.add_widget(save_button)

        return layout
    
    def save_text(self,instance):
        self.text_to_memorize = self.input_text.text
        self.status_label.text = "Texto salvo! Você receberá notificações regularmente para memorizá-lo"
        Clock.schedule_interval(self.send_notification, 60)

    def send_notification(self,dt):
        print("Hora de trabalhar a memória!")
        self.show_notification_popup()
    
    def show_notification_popup(self):
        from kivy.uix.popup import Popup
        from kivy.uix.textinput import TextInput
        from kivy.uix.button import Button
        from kivy.uix.boxlayout import BoxLayout

        popup_layout = BoxLayout(orientation='vertical')
        
        self.user_input = TextInput(hint_text="Type the memorized text here")
        popup_layout.add_widget(self.user_input)
        
        submit_button = Button(text="Submit")
        submit_button.bind(on_press=self.check_text)
        popup_layout.add_widget(submit_button)
        
        self.popup = Popup(title='Memorization Check', content=popup_layout, size_hint=(0.8, 0.4))
        self.popup.open()

    def check_text(self, instance):
        if self.user_input.text == self.text_to_memorize:
            self.status_label.text = "Correct! Keep it up!"
        else:
            self.status_label.text = "Incorrect. Try again."
        self.popup.dismiss()


if __name__ == '__main__':
    MemorizationApp().run()
        