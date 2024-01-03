import pygame
import os
import sys

pygame.init()
pygame.display.set_caption('Shooting practice')
size = width, height = 1000, 600
screen = pygame.display.set_mode(size)
FPS = 60
clock = pygame.time.Clock()


def terminate():
    pygame.quit()
    sys.exit()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def start_screen():
    intro_text = ["Выберите режим:",
                  "Точность (нажмите 1 для выбора)",
                  "Скорость (нажмите 2 для выбора)",
                  "Реакция (нажмите 3 для выбора)",
                  "Точность и реакция (нажмите 4 для выбора)"]

    fon = pygame.transform.scale(load_image('fon.jpg'), (width, height))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 30
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 500
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_1]:
                    return "accuracy"
                elif pygame.key.get_pressed()[pygame.K_2]:
                    return "speed"
                elif pygame.key.get_pressed()[pygame.K_3]:
                    return "reaction"
                elif pygame.key.get_pressed()[pygame.K_4]:
                    return "accuracy and accuracy"
        pygame.display.flip()
        clock.tick(FPS)


def time_from_start(current_time):
    font = pygame.font.Font(None, 30)
    text = font.render(f"{(current_time - start_time) / 1000}", True, (0, 0, 0))
    time_rect = text.get_rect()
    time_rect.top = 550
    time_rect.x = 10
    screen.blit(text, time_rect)


def rule(screen):
    f = pygame.font.Font(None, 20)
    txt = f.render("Для начала испытания нажмите правую кнопку мыши. Ваша цель - получить максимально\n"
                   " возможный балл за 30 секунд.", True, (0, 0, 0))
    r = txt.get_rect()
    r.top = 10
    r.x = 10
    screen.blit(txt, r)
    txt1 = f.render("Для зачисления балла нажимайте как можно быстрее и как можно точнее на появляющихся монстриков",
                    True, (0, 0, 0))
    r = txt1.get_rect()
    r.top = 40
    r.x = 10
    screen.blit(txt1, r)


def hide_rule(screen):
    f_1 = pygame.font.Font(None, 30)
    txt = f_1.render(f"", True, (0, 0, 0))
    r = txt.get_rect()
    r.top = 10
    r.x = 10
    screen.blit(txt, r)
    txt1 = f_1.render("", True, (0, 0, 0))
    r = txt1.get_rect()
    r.top = 40
    r.x = 10
    screen.blit(txt1, r)


if __name__ == '__main__':
    flag = start_screen()
    screen = pygame.display.set_mode(size)
    if flag == "accuracy":
        pygame.display.set_caption('accuracy')
    elif flag == "speed":
        pygame.display.set_caption('speed')
    elif flag == "reaction":
        pygame.display.set_caption('reaction')
    else:
        pygame.display.set_caption("accuracy and speed")
    clock = pygame.time.Clock()
    running = True
    fps = 60
    key = 0
    rule(screen)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                start_time = pygame.time.get_ticks()
                key = 1
        screen.fill("white")
        if key == 0:
            rule(screen)
        if key == 1:
            time_from_start(pygame.time.get_ticks())
            hide_rule(screen)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()

