"""主游戏类"""
import pygame
from Class.Game_Resources import Game_zy
from Class.Loop_interface_body import Process_the_display as Ptd
from Class.SOCKET_NET import Cn


class Game:
    def __init__(self):
        # 类指针
        self.Zy = Game_zy()  # 资源类
        self.Ptd = None
        self.Cn = Cn()
        self.Connect_to_a_server = False

        self.clock = None
        self.screen = None

        self.FPS = 60
        self.WIDTH = 720  # 窗口宽度(1450,1000|(12000,800
        self.HEIGHT = 360  #
        self.WHITE = (255, 255, 255)  # 白色
        self.GREEN = (0, 255, 0)  # 绿色
        self.RED = (255, 0, 0)  # 红色
        self.YELLOW = (255, 255, 0)
        self.BLACK = (0, 0, 0)
        self.BLUE = (0, 0, 255)  # 蓝色
        self.GREY = (211, 211, 211)  # 灰

        self.running = True  # 游戏是否循环运行

    def initialize(self):    # 游戏初始化
        # 游戏初始化
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))  # 创建窗口
        pygame.display.set_caption('mmo枪战-LAN')
        self.clock = pygame.time.Clock()  # 帧率对
        

    def run(self):
        self.Ptd = Ptd(self)
        self.Ptd.hall_w(self)
        self.Ptd.map_w(self)
        pygame.quit()
