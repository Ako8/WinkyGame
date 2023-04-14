import pygame
from sys import exit
pygame.init()


def player_movement():
    global face_to
    keys = pygame.key.get_pressed()
    if player_rect.left >= 0:
        if keys[pygame.K_LEFT]:
            face_to = False
            player_rect.x -= 4
    if player_rect.right <= WIDTH:
        if keys[pygame.K_RIGHT]:
            face_to = True
            player_rect.x += 4
    player_rect.y += gravity


def shooting():
    bullet_rect.y += 15
    bullet_rect1.x -= 7
    if bullet_rect.top >= HEIGHT:
        bullet_rect.bottom = 0
    if bullet_rect1.right <= 0:
        bullet_rect1.left = WIDTH


def check_death():
    global death, gravity
    if player_rect.top > WIDTH or player_rect.colliderect(bullet_rect) or player_rect.colliderect(bullet_rect1):
        player_rect.x = 50
        player_rect.bottom = 290
        gravity = 0
        death += 1


def draw_surfaces():
    screen.blit(background, (0, 0))
    screen.blit(text_1, text_scl)
    if face_to:
        screen.blit(sia[1], player_rect)
    else:
        screen.blit(sia[0], player_rect)
    screen.blit(finish_scl, finish_rect)
    for elem in rect_list_r1:
        if elem == step_rect_1 or elem == step_rect_2 or elem == step_rect_3:
            screen.blit(step, elem)
        else:
            screen.blit(stand_1, elem)
    screen.blit(bullet_1, bullet_rect)
    screen.blit(bullet_2, bullet_rect1)


def draw_after_game():
    screen.blit(after, after_rect)
    screen.blit(again_scl, again_rect)
    screen.blit(nextbut_scl, nextbut_rect)
    death_text = text.render(f"{death}", False, (10, 255, 24))
    death_text_rect = death_text.get_rect(bottomright=(470, 225))
    screen.blit(death_text, death_text_rect)
    time = f"{s // 3600}:{s // 60 % 60}:{s % 60}"
    time_text = text.render(f"{time}", False, (10, 255, 24))
    time_text_rect = time_text.get_rect(bottomright=(470, 200))
    screen.blit(time_text, time_text_rect)


def draw_rects(rects):
    a = 0
    global gravity
    for elem in rects:
        if player_rect.colliderect(elem):
            player_rect.bottom = elem.y
            a = 1
    if a == 0:
        gravity += 1


def main():
    global gravity, raund, i, s, death, face_to
    while True:
        if i == 60:
            s += 1
            i = 0
        i += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if player_rect.bottom == stand_rect_1_lvl_1.y or player_rect.bottom == stand_rect_2_lvl_1.y \
                            or player_rect.bottom == stand_rect_3_lvl_1.y or player_rect.bottom == stand_rect_4_lvl_1.y\
                            or player_rect.bottom == step_rect_1.y or player_rect.bottom == step_rect_2.y \
                            or player_rect.bottom == step_rect_3.y or player_rect.bottom == stand_rect_1_lvl_2.y \
                            or player_rect.bottom == stand_rect_2_lvl_2.y or player_rect.bottom == stand_rect_3_lvl_2.y:
                        gravity = -11
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx = pygame.mouse.get_pos()
                if again_rect.collidepoint(mx):
                    player_rect.x = 50
                    player_rect.bottom = 290
                    s = 0
                    death = 0
                    bullet_rect.bottom = 0
                    bullet_rect1.left = WIDTH
                    face_to = True
                    raund = 1
                if nextbut_rect.collidepoint(mx):
                    raund = 2
        player_movement()
        if raund == 1:
            draw_rects(rect_list_r1)
            draw_surfaces()
            shooting()
            check_death()
            if player_rect.colliderect(finish_rect):
                raund = 0
                draw_after_game()
        elif raund == 2:
            screen.blit(background, (0, 0))
            shvidi = text.render(
                f"Nuliani eubneba rvians ravari qamari shemogiweriavo!", False, "black")
            screen.blit(shvidi, (100, 200))
            screen.blit(again_scl, again_rect)
        pygame.display.update()
        clock.tick(FPS)


pygame.display.set_caption("BRUH")

WIDTH, HEIGHT, FPS, s, i, gravity, death, raund, face_to = 800, 400, 60, 0, 0, 0, 0, 1, True

screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

background = pygame.surface.Surface((800, 400)).convert()
background.fill((120, 160, 255))
back_text = pygame.font.Font(None, HEIGHT)

text_1 = back_text.render("BRUH", False, (130, 170, 255)).convert_alpha()
text_scl = text_1.get_rect(center=(WIDTH / 2, HEIGHT / 2))
text = pygame.font.Font(None, 32)

player = pygame.image.load('Winky.png').convert_alpha()
player_scl = pygame.transform.scale(player, (30, 25)).convert_alpha()
player_flip = pygame.transform.flip(player_scl, True, False)

sia = [player_scl, player_flip]
player_rect = player_scl.get_rect(midbottom=(50, 290))

finish = pygame.image.load("finish line.png").convert_alpha()
finish_scl = pygame.transform.scale(
    finish, (30 * 1.7, 15 * 1.7)).convert_alpha()
finish_rect = finish_scl.get_rect(bottomleft=(186, 190))

stand = pygame.image.load('ground.png').convert_alpha()
stand_1 = pygame.transform.scale(stand, (100, 10))

step = pygame.surface.Surface((5, 5)).convert()

bullet = pygame.image.load('QLDfuR-bullets-free-download.png').convert_alpha()
bullet1 = pygame.transform.scale(bullet, (50, 30))
bullet_1 = pygame.transform.rotate(bullet1, -90)
bullet2 = pygame.transform.scale(bullet, (30, 40))
bullet_2 = pygame.transform.rotate(bullet2, 180)

after = pygame.image.load("after.png").convert_alpha()
after_rect = after.get_rect(center=(WIDTH / 2, HEIGHT / 2))

again = pygame.image.load("Button-Refresh-icon.png").convert_alpha()
again_scl = pygame.transform.scale(again, (50, 50))
again_rect = again_scl.get_rect(center=(WIDTH / 2 - 40, HEIGHT / 2 + 65))

nextbut = pygame.image.load("next-button-icon-png-32.png").convert_alpha()
nextbut_scl = pygame.transform.scale(nextbut, (50, 50))
nextbut_rect = nextbut_scl.get_rect(center=(WIDTH / 2 + 40, HEIGHT / 2 + 65))

bullet_rect = bullet_1.get_rect(midbottom=(350, 0))
bullet_rect1 = bullet_2.get_rect(center=(WIDTH + 40, 325))

step_rect_1 = step.get_rect(topright=(WIDTH, 300))
step_rect_2 = step.get_rect(topright=(700, 250))
step_rect_3 = step.get_rect(topright=(WIDTH, 200))

stand_rect_1_lvl_1 = stand_1.get_rect(topleft=(0, 300))
stand_rect_2_lvl_1 = stand_1.get_rect(topleft=(200, 350))
stand_rect_3_lvl_1 = stand_1.get_rect(topleft=(400, 350))
stand_rect_4_lvl_1 = stand_1.get_rect(topleft=(600, 350))
stand_rect_1_lvl_2 = stand_1.get_rect(topleft=(620, 140))
stand_rect_2_lvl_2 = stand_1.get_rect(topleft=(400, 200))
stand_rect_3_lvl_2 = stand_1.get_rect(topleft=(186, 190))

rect_list_r1 = [stand_rect_1_lvl_1, stand_rect_2_lvl_1, stand_rect_3_lvl_1, stand_rect_4_lvl_1, step_rect_1,
                step_rect_2, step_rect_3, stand_rect_1_lvl_2, stand_rect_2_lvl_2, stand_rect_3_lvl_2]

pygame.display.set_icon(player_flip)
main()
