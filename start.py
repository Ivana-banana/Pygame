import pygame
import os
import sys
import random

pygame.init()
pygame.display.set_caption('Shooting practice')
size = width, height = 1200, 800
FPS = 60
clock = pygame.time.Clock()
results = []
cnt = 0
colors = ["red", "blue"]


def terminate():
    pygame.quit()
    sys.exit()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
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
    time_rect.top = 750
    time_rect.x = 10
    screen.blit(text, time_rect)


def rule(screen):
    f = pygame.font.Font(None, 20)
    txt = f.render("Для начала испытания нажмите правую кнопку мыши. Ваша цель - нажимать как можно быстрее"
                   " и как можно ближе к центру появляющегося КРАСНОГО круга.", True, (0, 0, 0))
    r = txt.get_rect()
    r.top = 10
    r.x = 10
    screen.blit(txt, r)
    txt1 = f.render("Остальные круги игнорируйте. Нажатие на них приведёт к ухудшению конечного результата",
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


def resultats(screen):
    f = pygame.font.Font(None, 20)
    txt = f.render("Испытание окончено. Ознакомьтесь со своими результатами", True, (255, 255, 255))
    r = txt.get_rect()
    r.top = 10
    r.x = 10
    screen.blit(txt, r)
    txt1 = f.render("Для продолжения игры, нажмите кнопку 0", True, (255, 255, 255))
    r = txt1.get_rect()
    r.top = 40
    r.x = 10
    screen.blit(txt1, r)


def print_results(screen, flag):
    if flag == "accuracy":
        image = pygame.Surface((1150, 258), pygame.SRCALPHA, 32)
        pygame.draw.polygon(image, (255, 0, 0), [(13, 242), (13, 0), (10, 4), (13, 0), (16, 4), (13, 0)], width=1)
        pygame.draw.polygon(image, (255, 0, 0), [(13, 242), (656, 242), (652, 245), (656, 242), (652, 239), (656, 242)],
                            width=1)
        c = 0
        ar_k = []
        ar_t = []
        for el in results:
            ar_k.append((el[0] ** 2 + el[1] ** 2) ** 0.5)
            ar_t.append(el[3])
        for i in range(13, 653, 21):
            pygame.draw.line(image, (255, 0, 0), (i, 239), (i, 245))
            f = pygame.font.Font(None, 11)
            txt1 = f.render(f"{c}", True, (255, 0, 0))
            r = txt1.get_rect()
            r.top = 252
            r.x = i
            image.blit(txt1, r)
            c += 1
        f = pygame.font.Font(None, 11)
        txt1 = f.render("Время", True, (255, 0, 0))
        r = txt1.get_rect()
        r.top = 230
        r.x = 634
        image.blit(txt1, r)
        c = 0
        for i in range(242, 0, -12):
            pygame.draw.line(image, (255, 0, 0), (10, i), (16, i))
            f = pygame.font.Font(None, 11)
            txt1 = f.render(f"{c * 3}", True, (255, 0, 0))
            r = txt1.get_rect()
            r.top = i
            r.x = 0
            image.blit(txt1, r)
            c += 1
        f = pygame.font.Font(None, 11)
        txt1 = f.render("Коэффицент разброса", True, (255, 0, 0))
        r = txt1.get_rect()
        r.top = 0
        r.x = 18
        image.blit(txt1, r)
        if len(ar_k) > 0:
            if ar_t[0] <= 30:
                pygame.draw.line(image, (0, 255, 0), (13, 242), (ar_t[0] * 21 + 13, 242 - ar_k[0] * 4))
                for i in range(1, len(ar_k)):
                    if ar_t[i] <= 30:
                        pygame.draw.line(image, (0, 255, 0), (ar_t[i - 1] * 21 + 13, 242 - ar_k[i - 1] * 4),
                                         (ar_t[i] * 21 + 13, 242 - ar_k[i] * 4))
        f = pygame.font.Font(None, 15)
        txt1 = f.render("График зависимости коэффицента разброса от времени", True, (255, 0, 0))
        r = txt1.get_rect()
        r.top = 0
        r.x = 656
        image.blit(txt1, r)
        f = pygame.font.Font(None, 15)
        if len(ar_k) != 0:
            txt1 = f.render(f"Средний коэффицент разброса(с учётом промахов)"
                            f" = {round((sum(ar_k) + cnt) / len(ar_k), 2)}",
                            True, (255, 0, 0))
        else:
            txt1 = f.render(f"Средний коэффицент разброса(с учётом промахов) = 0",
                            True, (255, 0, 0))
        r = txt1.get_rect()
        r.top = 15
        r.x = 656
        image.blit(txt1, r)
        f = pygame.font.Font(None, 15)
        if len(ar_k) != 0:
            txt1 = f.render(f"Максимальный коэфф. = {round(max(ar_k), 2)}, минимальный коэфф. = {round(min(ar_k), 2)}",
                            True, (255, 0, 0))
        else:
            txt1 = f.render(f"Максимальный коэфф. = 0, минимальный коэфф. = 0",
                            True, (255, 0, 0))
        r = txt1.get_rect()
        r.top = 30
        r.x = 656
        image.blit(txt1, r)
        screen.blit(image, (10, 100))
    elif flag == "speed":
        pygame.display.set_caption('speed')
    elif flag == "reaction":
        pygame.display.set_caption('reaction')
    else:
        pygame.display.set_caption("accuracy and speed")


all_sprites = pygame.sprite.Group()


class Ball(pygame.sprite.Sprite):

    def __init__(self, *group):
        super().__init__(*group)
        self.existence = 0
        self.time = (pygame.time.get_ticks() - start_time) / 1000
        self.color = random.choice(colors)
        self.radius = 5
        self.image = pygame.Surface((2 * self.radius, 2 * self.radius), pygame.SRCALPHA, 32)
        self.x = random.randrange(40, width - 41)
        self.y = random.randrange(40, height - 41)
        self.rect = pygame.Rect(self.x - self.radius, self.y - self.radius, 2 * self.radius, 2 * self.radius)
        self.k = 1.02
        pygame.draw.circle(self.image, pygame.Color(self.color),
                           (self.radius, self.radius), self.radius)
        # self.f = 0
        # while self.f == 0:
        #     for el in all_sprites:
        #         if pygame.sprite.collide_rect(self, el):
        #             self.x = random.randrange(40, width - 41)
        #             self.y = random.randrange(40, height - 41)
        #             self.rect = pygame.Rect(self.x - self.radius, self.y - self.radius, 2 * self.radius,
        #                                     2 * self.radius)
        #         else:
        #             self.f = 1

    def update(self):
        if self.existence > 1:
            self.kill()
            return
        if self.radius <= 40:
            self.radius *= self.k
            self.image = pygame.Surface((2 * self.radius, 2 * self.radius),
                                        pygame.SRCALPHA, 32)
            self.rect = pygame.Rect(self.x - self.radius, self.y - self.radius, 2 * self.radius, 2 * self.radius)
            pygame.draw.circle(self.image, pygame.Color(self.color),
                               (self.radius, self.radius), self.radius)
        else:
            self.existence += 1
            self.k = 0.98
            self.radius = 39

    def check(self):
        coords = pygame.mouse.get_pos()
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.kill()
            if self.color == "red":
                results.append((abs(self.x - coords[0]), abs(self.y - coords[1]),
                                (pygame.time.get_ticks() - start_time) / 1000 - self.time,
                                pygame.time.get_ticks() / 1000, self.color))
                return 0
        return 1


if __name__ == '__main__':
    screen = pygame.display.set_mode(size)
    flag = start_screen()
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
    key = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                if key != 1:
                    start_time = pygame.time.get_ticks()
                    hide_rule(screen)
                    key = 1
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                cnt += 1
                for elem in all_sprites:
                    elem.check()
            if event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_0] and key == 2:
                    key = 3
        screen.fill("white")
        if key == 0:
            rule(screen)
            flag_ball = 0
        if key == 1:
            time_from_start(pygame.time.get_ticks())
            if int((pygame.time.get_ticks() - start_time) / 1000) > 0.5 + flag_ball:
                Ball(all_sprites)
                flag_ball += 0.5
            if (pygame.time.get_ticks() - start_time) / 1000 > 10:
                key = 2
            all_sprites.draw(screen)
            all_sprites.update()
        if key == 2:
            screen.fill("black")
            for elem in all_sprites:
                elem.kill()
            resultats(screen)
            print_results(screen, flag)
        if key == 3:
            flag = start_screen()
            if flag == "accuracy":
                pygame.display.set_caption('accuracy')
            elif flag == "speed":
                pygame.display.set_caption('speed')
            elif flag == "reaction":
                pygame.display.set_caption('reaction')
            else:
                pygame.display.set_caption("accuracy and speed")
            key = 0
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
