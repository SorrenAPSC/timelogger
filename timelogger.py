from guizero import App, Text, Box, TextBox, PushButton, Window


main_app = App(title="Timer", layout="auto", width=200, height=100)
timertwo = Window(main_app, title="Timer #2")
timertwo.hide()

seconds = Text(main_app, text="0", width="fill", height="fill")

def end_all():
    main_app.destroy()
def timer():
    seconds.value = int(seconds.value) + 1
def timer_begin():
    seconds.repeat(1000, timer)
def timer_pause():
    starttimer.cancel(timer)

starttimer = PushButton(main_app, text="Start timer", command=timer_begin,
        align="left", width="fill")
pausetimer = PushButton(main_app, text="Pause timer", command=timer_pause,
        align="right", width="fill")


main_app.display()

main_app.on_close(end_all)
