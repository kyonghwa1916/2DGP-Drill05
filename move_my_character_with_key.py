from pico2d import *

open_canvas()

backgound = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
running = True

while running:
    clear_canvas()
    backgound.draw(400, 300)

    update_canvas()

close_canvas()