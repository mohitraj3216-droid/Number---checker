import random

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class NumberGuessingApp(App):

    def build(self):

        # Game variables
        self.secret_number = random.randint(1, 100)
        self.chances = 0

        # Main layout
        layout = BoxLayout(
            orientation="vertical",
            padding=30,
            spacing=15
        )

        # Title
        title = Label(
            text="NUMBER GUESSING GAME",
            font_size=28
        )

        # Instructions
        instructions = Label(
            text="Guess a number between 1 and 100",
            font_size=18
        )

        # Number input
        self.number_input = TextInput(
            hint_text="Enter your guess",
            input_filter="int",
            multiline=False
        )

        # Guess button
        guess_button = Button(
            text="GUESS",
            font_size=20
        )

        # Result
        self.result = Label(
            text="You have 10 chances",
            font_size=18
        )

        # Chances
        self.chances_label = Label(
            text="Chances: 0 / 10",
            font_size=16
        )

        # Reset button
        reset_button = Button(
            text="NEW GAME",
            font_size=18
        )

        # Button functions
        guess_button.bind(
            on_press=self.check_guess
        )

        reset_button.bind(
            on_press=self.reset_game
        )

        # Add widgets
        layout.add_widget(title)
        layout.add_widget(instructions)
        layout.add_widget(self.number_input)
        layout.add_widget(guess_button)
        layout.add_widget(self.result)
        layout.add_widget(self.chances_label)
        layout.add_widget(reset_button)

        return layout


    def check_guess(self, instance):

        # Check if input is empty
        if self.number_input.text == "":
            self.result.text = "Please enter a number"
            return

        # Convert input into integer
        guess = int(self.number_input.text)

        # Increase chances
        self.chances = self.chances + 1

        # Check the guess
        if guess > self.secret_number:

            self.result.text = "The number is smaller"

        elif guess < self.secret_number:

            self.result.text = "The number is bigger"

        else:

            self.result.text = "🎉 Correct! You guessed it!"
            self.number_input.disabled = True

        # Show chances
        self.chances_label.text = (
            "Chances: " + str(self.chances) + " / 10"
        )

        # Check if chances are over
        if self.chances >= 10 and guess != self.secret_number:

            self.result.text = (
                "Game Over! Number was "
                + str(self.secret_number)
            )

            self.number_input.disabled = True


    def reset_game(self, instance):

        # Generate a new secret number
        self.secret_number = random.randint(1, 100)

        # Reset chances
        self.chances = 0

        # Clear input
        self.number_input.text = ""

        # Enable input again
        self.number_input.disabled = False

        # Reset result
        self.result.text = "You have 10 chances"

        # Reset chances label
        self.chances_label.text = "Chances: 0 / 10"


NumberGuessingApp().run()
