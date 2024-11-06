"""
游戏角色（精灵
"""
import math
import random
import pygame
from pygame import Vector2
from function.winfun import angle_to_vector



# ----------------精灵（物体对象---------------- #
class Player_Controller:        # 玩家控制器
    ...
class Player(pygame.sprite.Sprite):  # 客服端自己
    def __init__(self, Game):
        pygame.sprite.Sprite.__init__(self)
        self.Game = Game
        # 玩家数据-属性
        self.hp = 100                                       # 血量
        self.hp_max = 100
        self.map_coordinates_x = 0                          # 地图坐标
        self.map_coordinates_y = 3234                       # 地图坐标
        self.Room_player_number = None                      # 编号
        self.survive = True                                 # 存活
        self.speed = 8                                      # 速度
        self.face = 'r'                                     # 面向
        self.Arsenal = []                                   # 武器库
        self.Image_size = (1000 / 4.5, 1000 / 4.5)          # 图像大小
        self.entity_Image_size = (1000 / 4.2, 400 / 4.2)    # 碰撞体大小
        self.img_state = self.Game.Zy.Blues_Army_img_r
        self.Handheld = Weapons(Game, self, "AK47")
        self.Game.Ptd.all_weapons.add(self.Handheld)

        # 图像方块实体·
        self.entity = pygame.Surface(self.entity_Image_size)  # 实体/碰撞体
        self.image = pygame.transform.smoothscale(
            self.img_state,
            self.Image_size)      # 人物图像

        self.rect = self.image.get_rect()
        self.rect2 = pygame.Surface((50, 60)).get_rect()  # 碰撞体 碰撞实体
        self.rect.left = 0
        self.rect.top = 0
        # self.image.fill(game.BLUE)

    def update(self):
        # 计算地图角色在屏幕的位置
        self.rect.centerx = self.map_coordinates_x-self.Game.Ptd.camera_x
        self.rect.centery = self.map_coordinates_y-self.Game.Ptd.camera_y
        self.rect2.center = self.rect.center



        key_pressed = pygame.key.get_pressed()
        if self.hp <= 0:    # 玩家被击杀
            self.survive = False
            if self.face == 'l':
                self.image = pygame.transform.smoothscale(self.Game.Zy.Blues_Army_d_img_l, self.Image_size)
            else:
                self.image = pygame.transform.smoothscale(self.Game.Zy.Blues_Army_d_img_r, self.Image_size)

            self.Handheld.kill()


        if self.survive:
            if self.Game.Ptd.mouse_position_x < self.rect.centerx:  # 玩家面向
                self.face = 'l'
                self.image = pygame.transform.smoothscale(self.Game.Zy.Blues_Army_img_l, self.Image_size)
            else:
                self.face = 'r'
                self.image = pygame.transform.smoothscale(self.Game.Zy.Blues_Army_img_r, self.Image_size)

            if key_pressed[pygame.K_w]:
                self.map_coordinates_y -= self.speed
                # self.move(0, -self.speeds, all_Map_collision_box)
            if key_pressed[pygame.K_s]:
                self.map_coordinates_y += self.speed
                # self.move(0, self.speeds, all_Map_collision_box)
            if key_pressed[pygame.K_a]:
                self.map_coordinates_x -= self.speed
                # self.move(-self.speeds, 0, all_Map_collision_box)
            if key_pressed[pygame.K_d]:
                self.map_coordinates_x += self.speed
                # self.move(self.speeds, 0, all_Map_collision_box)


            if key_pressed[pygame.K_UP]:
                # self.move(0, -self.speeds, all_Map_collision_box)
                self.Game.Ptd.camera_y -= 80
                ...
            if key_pressed[pygame.K_DOWN]:
                # self.move(0, self.speeds, all_Map_collision_box)
                self.Game.Ptd.camera_y += 80
                ...
            if key_pressed[pygame.K_LEFT]:
                # self.move(-self.speeds, 0, all_Map_collision_box)
                self.Game.Ptd.camera_x -= 80
                ...
            if key_pressed[pygame.K_RIGHT]:
                # self.move(self.speeds, 0, all_Map_collision_box)
                self.Game.Ptd.camera_x += 80
                ...
        else:
            ...
class Weapons(pygame.sprite.Sprite):  # 武器
    def __init__(self, Game,  master, name):
        pygame.sprite.Sprite.__init__(self)

        self.gun_pos = Vector2(0, 0)  # 枪口位置
        self.Game = Game
        self.Master = master
        # ↓枪械属性初始化----------------------------↓
        self.Weapon_name = name  # 武器名字
        self.map_coordinates_x = 100
        self.map_coordinates_y = 100
        self.muzzle = 60   # 枪口位置偏移
        self.Single_damage = 31  # 单发伤害
        self.recoil = 10  # 后坐力
        self.Scattering = 5  # 散射度
        self.cooling = 90   # 冷却
        self.angle = 0
        self.Image_size = (1780 / 8, 400 / 8)   # 枪械图像
        self.Shooting_sound_effects = self.Game.Zy.shoot_sound2  # 射击音效
        self.use_time = pygame.time.get_ticks()  # 开火时间/使用时间

        self.firearm_images_l = pygame.transform.smoothscale(
            self.Game.Zy.gun_ak47_img_l, self.Image_size
        )  # 武器没开火图像
        self.firearm_images_r = pygame.transform.smoothscale(
            self.Game.Zy.gun_ak47_img_r, self.Image_size
        )
        self.firing_image_l = pygame.transform.smoothscale(
            self.Game.Zy.gun_ak47fire_img_l, self.Image_size
        )  # 武器开火图像
        self.firing_image_r = pygame.transform.smoothscale(
            self.Game.Zy.gun_ak47fire_img_r, self.Image_size
        )

        self.image = self.firing_image_r
        self.rect = self.image.get_rect()
    def Load_weapons(self):     # 加载指定枪械
        ...

    def update(self):
        self.gun_pos = Vector2(self.rect.centerx, self.rect.centery)

        # 计算地图武器在屏幕的位置
        self.rect.centerx = (self.map_coordinates_x-self.Game.Ptd.camera_x)
        self.rect.centery = (self.map_coordinates_y-self.Game.Ptd.camera_y)

        # 前往角色手中
        self.map_coordinates_x += (
            self.Master.map_coordinates_x-self.map_coordinates_x
        )/2
        self.map_coordinates_y += (
            self.Master.map_coordinates_y-self.map_coordinates_y
        )/2

        # 获取鼠标位置
        mouse_position = (self.Game.Ptd.mouse_position_x, self.Game.Ptd.mouse_position_y)
        # 计算角度
        dx = mouse_position[0] - self.rect.centerx
        dy = mouse_position[1] - self.rect.centery
        self.angle = math.degrees(math.atan2(dy, dx))
        # 创建一个新的 Surface 并绘制旋转后的图像
        if self.Master.face == "l":
            self.image = pygame.transform.rotate(self.firearm_images_l, -self.angle)
            self.rect = self.image.get_rect(center=self.rect.center)
            ...
        else:
            self.image = pygame.transform.rotate(self.firearm_images_r, -self.angle)
            self.rect = self.image.get_rect(center=self.rect.center)

    def use(self):      # 使用/射击/攻击
        if self.Master.survive:
            # 获取鼠标位置
            mouse_pos = Vector2((self.Game.Ptd.camera_x, self.Game.Ptd.camera_y))
            direction = mouse_pos - self.gun_pos
            direction.normalize_ip()  # 归一化向量长度为1
            direction = angle_to_vector(self.angle)

            if pygame.time.get_ticks() - self.use_time > self.cooling:
                angle_offset = self.angle + random.uniform(-self.Scattering, self.Scattering)
                zd = bullet(self.Game, self.Master, angle_offset)
                self.Game.Ptd.all_sprites.add(zd)
                self.Game.Ptd.all_bullet_list.add(zd)

                self.map_coordinates_x += -(direction[0] * self.recoil)
                self.map_coordinates_y += -(direction[1] * self.recoil)
                self.use_time = pygame.time.get_ticks()

                # 播放声音
                self.Game.Zy.shoot_SM.Modify_sound_effects(self.Shooting_sound_effects)
                self.Game.Zy.shoot_SM.play_gunshot()

                if self.Game.Connect_to_a_server:  # 连接服务器成功
                    wj_bh = self.Master.Room_player_number
                    wz_x = self.map_coordinates_x
                    wz_y = self.map_coordinates_y
                    mx = self.Master.face
                    jd = angle_offset
                    temp_data = f"发射子弹|{wj_bh}|{wz_x}|{wz_y}|{mx}|{jd}|"
                    self.Game.Cn.send(temp_data)
class bullet(pygame.sprite.Sprite):  #
    def __init__(self, game, master, jd):
        pygame.sprite.Sprite.__init__(self)
        self.Game = game
        self.Master = master
        self.Image_size = (162, 9)
        self.image = pygame.transform.smoothscale(game.Zy.bullet_img_5562, self.Image_size)
        self.rect = self.image.get_rect()  # 创建初始位置的矩形

        self.rect2 = pygame.Surface((18, 18)).get_rect()  # 碰撞体 碰撞实体

        # 属性数据
        self.angle = jd  # 旋转角度
        self.vector = angle_to_vector(self.angle)  # 子弹向量
        self.harm = 0  # 伤害
        self.speeds = 60  # 速度
        self.world_x = self.Master.Handheld.map_coordinates_x + self.Master.Handheld.muzzle*self.vector[0]  # 世界位置x
        self.world_y = self.Master.Handheld.map_coordinates_y + self.Master.Handheld.muzzle*self.vector[1]  # 世界位置y

        # 将子弹旋转至发射方向
        self.image = pygame.transform.rotate(self.image, -self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def update(self):
        self.world_x += self.vector[0] * self.speeds
        self.world_y += self.vector[1] * self.speeds

        # 计算子弹在屏幕的位置
        self.rect.centerx = self.world_x - self.Game.Ptd.camera_x
        self.rect.centery = self.world_y - self.Game.Ptd.camera_y
        self.rect2.center = self.rect.center
class Net_Player(pygame.sprite.Sprite):  # 客服端自己
    def __init__(self, Game):
        pygame.sprite.Sprite.__init__(self)
        self.Game = Game
        # 玩家数据-属性
        self.hp = 100                                       # 血量
        self.hp_max = 100
        self.map_coordinates_x = 0                          # 地图坐标
        self.map_coordinates_y = 3234                       # 地图坐标
        self.Room_player_number = None                      # 编号
        self.survive = True                                 # 存活
        self.speed = 8                                      # 速度
        self.face = 'r'                                     # 面向
        self.Arsenal = []                                   # 武器库
        self.Image_size = (1000 / 4.5, 1000 / 4.5)          # 图像大小
        self.entity_Image_size = (1000 / 4.2, 400 / 4.2)    # 碰撞体大小
        self.img_state = self.Game.Zy.Blues_Army_img_r
        self.Handheld = Net_Weapons(Game, self, "AK47")
        self.Game.Ptd.all_weapons.add(self.Handheld)

        # 图像方块实体·
        self.entity = pygame.Surface(self.entity_Image_size)  # 实体/碰撞体
        self.image = pygame.transform.smoothscale(
            self.img_state,
            self.Image_size)      # 人物图像

        self.rect = self.image.get_rect()
        self.rect2 = pygame.Surface((50, 60)).get_rect()  # 碰撞体 碰撞实体
        self.rect.left = 0
        self.rect.top = 0
        # self.image.fill(game.BLUE)

    def update(self):
        # 计算地图角色在屏幕的位置
        self.rect.centerx = self.map_coordinates_x-self.Game.Ptd.camera_x
        self.rect.centery = self.map_coordinates_y-self.Game.Ptd.camera_y
        self.rect2.center = self.rect.center

        if self.hp <= 0:  # 玩家被击杀
            self.survive = False
            if self.face == 'l':
                self.image = pygame.transform.smoothscale(self.Game.Zy.Blues_Army_d_img_l, self.Image_size)
            else:
                self.image = pygame.transform.smoothscale(self.Game.Zy.Blues_Army_d_img_r, self.Image_size)

            self.Handheld.kill()
        if self.survive:
            if self.face == 'l':
                self.image = pygame.transform.smoothscale(self.Game.Zy.Blues_Army_img_l, self.Image_size)
            else:
                self.image = pygame.transform.smoothscale(self.Game.Zy.Blues_Army_img_r, self.Image_size)
class Net_Weapons(pygame.sprite.Sprite):  # 武器
    def __init__(self, Game,  master, name):
        pygame.sprite.Sprite.__init__(self)

        self.Game = Game
        self.Master = master
        # ↓枪械属性初始化----------------------------↓
        self.Weapon_name = name  # 武器名字
        self.map_coordinates_x = 100
        self.map_coordinates_y = 100
        self.muzzle = 60   # 枪口位置偏移
        self.Single_damage = 31  # 单发伤害
        self.recoil = 10  # 后坐力
        self.Scattering = 5  # 散射度
        self.cooling = 90   # 冷却
        self.angle = 0
        self.Image_size = (1780 / 8, 400 / 8)   # 枪械图像
        self.Shooting_sound_effects = self.Game.Zy.shoot_sound2  # 射击音效
        self.use_time = pygame.time.get_ticks()  # 开火时间/使用时间

        self.firearm_images_l = pygame.transform.smoothscale(
            self.Game.Zy.gun_ak47_img_l, self.Image_size
        )  # 武器没开火图像
        self.firearm_images_r = pygame.transform.smoothscale(
            self.Game.Zy.gun_ak47_img_r, self.Image_size
        )
        self.firing_image_l = pygame.transform.smoothscale(
            self.Game.Zy.gun_ak47fire_img_l, self.Image_size
        )  # 武器开火图像
        self.firing_image_r = pygame.transform.smoothscale(
            self.Game.Zy.gun_ak47fire_img_r, self.Image_size
        )

        self.image = self.firing_image_r
        self.rect = self.image.get_rect()
    def Load_weapons(self):     # 加载指定枪械
        ...

    def update(self):
        # self.gun_pos = Vector2(self.rect.centerx, self.rect.centery)

        # 计算地图武器在屏幕的位置
        self.rect.centerx = (self.map_coordinates_x-self.Game.Ptd.camera_x)
        self.rect.centery = (self.map_coordinates_y-self.Game.Ptd.camera_y)

        # 前往角色手中
        self.map_coordinates_x += (
            self.Master.map_coordinates_x-self.map_coordinates_x
        )/2
        self.map_coordinates_y += (
            self.Master.map_coordinates_y-self.map_coordinates_y
        )/2

        # 创建一个新的 Surface 并绘制旋转后的图像
        if self.Master.face == "l":
            self.image = pygame.transform.rotate(self.firearm_images_l, -self.angle)
            self.rect = self.image.get_rect(center=self.rect.center)
            ...
        else:
            self.image = pygame.transform.rotate(self.firearm_images_r, -self.angle)
            self.rect = self.image.get_rect(center=self.rect.center)

    def use(self):      # 使用/射击/攻击
        if self.Master.survive:
            direction = angle_to_vector(self.angle)
            self.map_coordinates_x += -(direction[0] * self.recoil)
            self.map_coordinates_y += -(direction[1] * self.recoil)

