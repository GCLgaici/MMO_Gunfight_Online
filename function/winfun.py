import math
import pygame


def zun_x_draw(Game):
    Game.Ptd.mouse_position_x += (pygame.mouse.get_pos()[0] - Game.Ptd.mouse_position_x) / 4
    Game.Ptd.mouse_position_y += (pygame.mouse.get_pos()[1] - Game.Ptd.mouse_position_y) / 4
    da_xiao = (275 / 4, 275 / 4)
    image_zx = pygame.transform.smoothscale(Game.Zy.foresight_image, da_xiao)
    zx_k = image_zx.get_rect()
    zx_k.centerx = Game.Ptd.mouse_position_x
    zx_k.centery = Game.Ptd.mouse_position_y
    return image_zx, zx_k


def angle_to_vector(angle):
    radians = math.radians(angle)
    x = math.cos(radians)
    y = math.sin(radians)
    return x, y


def draw_health(surf, num_Game, rgb, hp, max_hp, hl_x, hl_y, w_h=(100, 10)):
    if hp < 0:
        hp = 0
    BAR_LENGTH = w_h[0]
    BAR_HEIGHT = w_h[1]
    fill = (hp / max_hp) * BAR_LENGTH
    outline_rect = pygame.Rect(hl_x, hl_y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(hl_x, hl_y, fill, BAR_HEIGHT)
    pygame.draw.rect(surf, num_Game.BLACK, outline_rect)
    pygame.draw.rect(surf, rgb, fill_rect)
    pygame.draw.rect(surf, num_Game.BLACK, outline_rect, 2)



def perspective(Game, wj):  # 透视/绘制
    # pygame.draw.line(screen, (255, 0, 0), player.rect.center,k.rect.center, 2)
    # pygame.draw.rect(screen, (255, 0, 0), k.rect, 2)
    for zda in Game.Ptd.all_bullet_list:
        pygame.draw.rect(Game.screen, (255, 0, 0), zda.rect2, 2)
    pygame.draw.rect(Game.screen, (255, 0, 0), wj.rect2, 2)
    for df in Game.Ptd.all_net_sprites:
        pygame.draw.rect(Game.screen, (255, 0, 0), df.rect2, 2)
        pygame.draw.line(Game.screen, (255, 0, 0), wj.rect.center, df.rect.center, 2)



if __name__ == '__main__':
    ...
