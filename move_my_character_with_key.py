from pico2d import *

open_canvas()

backgound = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
running = True
frame = 0
dirx = 0
diry = 0
x = 400
y = 300

def handle_event():
    global running, dirx, diry
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dirx += 1
            elif event.key == SDLK_LEFT:
                dirx -= 1
            elif event.key == SDLK_UP:
                diry += 1
            elif event.key == SDLK_DOWN:
                diry -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dirx -= 1
            elif event.key == SDLK_LEFT:
                dirx += 1
            elif event.key == SDLK_UP:
                diry -= 1
            elif event.key == SDLK_DOWN:
                diry += 1


while running:
    if x > 30 and x < 770:
        x += dirx * 5
    if y > 30 and y < 570:
        y += diry * 5
    clear_canvas()
    backgound.draw(400, 300)
    character.clip_draw(frame * 100, 100, 100, 100, x, y)
    update_canvas()
    handle_event()
    frame = (frame + 1) % 8
    delay(0.05)


close_canvas()