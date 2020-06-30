from guizero import App, Text, Box, TextBox, PushButton


main_app = App(title="Time Logger", layout="auto")
seconds = Text(main_app, text="0", width="fill", height="fill")
def timer():
    seconds.value = int(seconds.value) + 1
def call1():
    seconds.repeat(1000, timer)

starttimer = PushButton(main_app, text="Start timer", command=call1,
        align="bottom")


main_app.display()

