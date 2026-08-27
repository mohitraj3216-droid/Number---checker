from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class NumberCheckerApp(App):

    def build(self):

        # Main layout
        layout = BoxLayout(
            orientation="vertical",
            padding=30,
            spacing=15
        )

        # Title
        title = Label(
            text="NUMBER CHECKER",
            font_size=30
        )

        # Number input
        self.number_input = TextInput(
            hint_text="Enter a number",
            input_filter="int",
            multiline=False
        )

        # Buttons
        even_odd_button = Button(
            text="Check Even or Odd"
        )

        positive_negative_button = Button(
            text="Check Positive or Negative"
        )

        prime_button = Button(
            text="Check Prime Number"
        )

        clear_button = Button(
            text="Clear"
        )

        # Result
        self.result = Label(
            text="Enter a number and choose an option",
            font_size=18
        )

        # Button functions
        even_odd_button.bind(
            on_press=self.check_even_odd
        )

        positive_negative_button.bind(
            on_press=self.check_positive_negative
        )

        prime_button.bind(
            on_press=self.check_prime
        )

        clear_button.bind(
            on_press=self.clear
        )

        # Add everything to the screen
        layout.add_widget(title)
        layout.add_widget(self.number_input)
        layout.add_widget(even_odd_button)
        layout.add_widget(positive_negative_button)
        layout.add_widget(prime_button)
        layout.add_widget(clear_button)
        layout.add_widget(self.result)

        return layout


    def check_even_odd(self, instance):

        if self.number_input.text == "":
            self.result.text = "Please enter a number"
            return

        number = int(self.number_input.text)

        if number % 2 == 0:
            self.result.text = str(number) + " is Even"
        else:
            self.result.text = str(number) + " is Odd"


    def check_positive_negative(self, instance):

        if self.number_input.text == "":
            self.result.text = "Please enter a number"
            return

        number = int(self.number_input.text)

        if number > 0:
            self.result.text = str(number) + " is Positive"

        elif number < 0:
            self.result.text = str(number) + " is Negative"

        else:
            self.result.text = "The number is Zero"


    def check_prime(self, instance):

        if self.number_input.text == "":
            self.result.text = "Please enter a number"
            return

        number = int(self.number_input.text)

        if number <= 1:
            self.result.text = str(number) + " is not Prime"
            return

        for i in range(2, number):

            if number % i == 0:
                self.result.text = str(number) + " is not Prime"
                return

        self.result.text = str(number) + " is Prime"


    def clear(self, instance):

        self.number_input.text = ""
        self.result.text = "Enter a number and choose an option"


NumberCheckerApp().run()
