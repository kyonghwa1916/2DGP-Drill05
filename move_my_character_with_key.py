from pico2d import *

open_canvas()

backgound = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
running = True
frame = 0
dir = 0



while running:
    clear_canvas()
    backgound.draw(400, 300)
    character.clip_draw(frame * 100, 100, 100, 100, 400, 90)
    update_canvas()
    frame = (frame + 1) % 8
    delay(0.05)


close_canvas()