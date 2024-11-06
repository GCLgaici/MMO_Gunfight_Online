"""
游戏资源文件加载
"""
import os
import pygame
import pygame.display
import pathlib

# 定义音效管理器类
class SoundManager:
    def __init__(self, path):
        self.gunshot_sound = pygame.mixer.Sound(path)
        self.channel = pygame.mixer.Channel(0)  # 使用第一个音效通
    def Modify_sound_effects(self, path):  # 修改音效
        self.gunshot_sound = pygame.mixer.Sound(path)
    def play_gunshot(self):
        # 停止之前的音效
        self.channel.stop()
        # 播放开火音效
        self.channel.play(self.gunshot_sound)

class Game_zy:
    def __init__(self):
        self.bullet_img_556 = None
        self.bullet_img_5562 = None
        self.shoot_sound2 = None
        self.Orange_Army_squat_img_r = None
        self.Orange_Army_squat_img_l = None
        self.Orange_Army_d_img_r = None
        self.Orange_Army_d_img_l = None
        self.Orange_Army_img_l = None
        self.Orange_Army_img_r = None
        self.Blues_Army_squat_img_l = None
        self.Blues_Army_squat_img_r = None
        self.Blues_Army_d_img_l = None
        self.Blues_Army_d_img_r = None
        self.Blues_Army_img_l = None
        self.Blues_Army_img_r = None
        self.map_image = None

        self.folder = pathlib.Path(__file__).parent.parent.resolve()
        # -----加载图像，音频，字体----- #
        self.font_name = os.path.join(self.folder, 'font/font.ttf')

    def image(self):
        # 大厅背景
        self.Lobby_background = pygame.image.load(
            os.path.join(self.folder, "img", "lobby", "dt_bj.png")).convert()
        # 大地图
        self.map_image = pygame.image.load(
            os.path.join(self.folder, "img", "atlas.png"))
        self.foresight_image = pygame.image.load(
            os.path.join(self.folder, "img", "mouse", "准星.png"))

        # 枪械
        self.gun_ak47_img_r = pygame.image.load(
            os.path.join(self.folder, "img", "Fire_img", "AK-47_r.png")).convert_alpha()
        self.gun_ak47_img_l = pygame.image.load(
            os.path.join(self.folder, "img", "Fire_img", "AK-47_l.png")).convert_alpha()
        self.gun_ak47fire_img_r = pygame.image.load(
            os.path.join(self.folder, "img", "Fire_img", "AK-47开火_r.png")).convert_alpha()
        self.gun_ak47fire_img_l = pygame.image.load(
            os.path.join(self.folder, "img", "Fire_img", "AK-47开火_l.png")).convert_alpha()

        # 蓝军图像
        self.Blues_Army_img_r = pygame.image.load(
            os.path.join(self.folder, "img", "fig_img", "a蓝军r.png")).convert_alpha()
        self.Blues_Army_img_l = pygame.image.load(
            os.path.join(self.folder, "img", "fig_img", "a蓝军l.png")).convert_alpha()
        self.Blues_Army_d_img_r = pygame.image.load(
            os.path.join(self.folder, "img", "fig_img", "a蓝军dr.png")).convert_alpha()
        self.Blues_Army_d_img_l = pygame.image.load(
            os.path.join(self.folder, "img", "fig_img", "a蓝军dl.png")).convert_alpha()
        # 橙军图像
        self.Orange_Army_img_r = pygame.image.load(
            os.path.join(self.folder, "img", "fig_img", "a橙军r.png")).convert_alpha()
        self.Orange_Army_img_l = pygame.image.load(
            os.path.join(self.folder, "img", "fig_img", "a橙军l.png")).convert_alpha()
        self.Orange_Army_d_img_r = pygame.image.load(
            os.path.join(self.folder, "img", "fig_img", "a橙军dr.png")).convert_alpha()
        self.Orange_Army_d_img_l = pygame.image.load(
            os.path.join(self.folder, "img", "fig_img", "a橙军dl.png")).convert_alpha()

        # 加载子弹
        self.bullet_img_556 = pygame.image.load(
            os.path.join(self.folder, "img", "556弹头.png")).convert_alpha()
        self.bullet_img_5562 = pygame.image.load(
            os.path.join(self.folder, "img", "mmo子弹.png")).convert_alpha()

        self.shoot_sound2 = os.path.join(self.folder, "sound", "射击.wav")
        self.shoot_SM = SoundManager(self.shoot_sound2)
        ...

    def audio(self):
        ...

    def Play_background_music(self):
        pygame.mixer.music.load(os.path.join(self.folder, "sound", "bj001.wav"))
        pygame.mixer.music.set_volume(0.5)  # 背景音量
        pygame.mixer.music.play(-1)  # 重复播放背景音乐

    def load(self):
        self.image()
        self.audio()

