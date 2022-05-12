import uiFunction
'''
def say_hello():
    print("Hello, World!")
'''

ui = uiFunction.uiFunction()

scr = ui.init((1600, 900), "Test")
la1 = ui.label(30, (120, 30), "freesansbold.ttf", (255, 255, 255),
                       (55, 55, 55), "Life Game")
bu1 = ui.button(30, (80, 200), "freesansbold.ttf", (255, 255, 255),
                        (55, 55, 55), (255, 255, 255), (155, 155, 155), title="start")

bu2 = ui.button(30, (80, 400), "freesansbold.ttf", (255, 255, 255),
                        (55, 55, 55), (255, 255, 255), (155, 155, 155), title="pause")

bu3 = ui.button(30, (80, 600), "freesansbold.ttf", (255, 255, 255),
                        (55, 55, 55), (255, 255, 255), (155, 155, 155),  title="reset")

bu4 = ui.button(30, (80, 800), "freesansbold.ttf", (255, 255, 255),
                        (55, 55, 55), (255, 255, 255), (155, 155, 155), title="random")

ui.register_cp(la1)
ui.register_cp(bu1)
ui.register_cp(bu2)
ui.register_cp(bu3)
ui.register_cp(bu4)

if __name__ == '__main__':
    ui.run(scr, (0, 0, 0))
