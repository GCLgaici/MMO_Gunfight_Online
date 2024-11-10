"""
执行循环显示窗口界面处理
"""
import json
import random
import time
import pygame
from function.winfun import zun_x_draw
from function.winfun import draw_health
from function.winfun import perspective
from Class.Seisai import Player
from Class.Seisai import Net_Player
from Class.Seisai import bullet
from _thread import *


class Process_the_display:  # 主要图像绘制
    def __init__(self, Game):
        self.all_weapons = None
        self.all_sprites = None
        self.all_net_sprites = None
        self.all_bullet_list = None

        self.Game = Game
        self.Zy = Game.Zy
        self.Zy.load()  # 加载资源

        # 定义地图位置和偏移量
        self.MAP_X = 0  # 地图坐标(左边缘位置
        self.MAP_Y = 0  # 地图坐标(上边缘位置
        self.camera_x = 100  # 相机x位置(左边缘位置
        self.camera_y = 200  # 相机y位置(顶部边缘位置
        self.mouse_position_x = 500              # 准星x位置
        self.mouse_position_y = 500              # 准星y位置


    def run_threaded_(self):
        self.Game.Cn.Run_Receive_data()
    def threaded_dispose(self, Game, player):
        while True:
            time.sleep(0.000000000000000000002)     #
            if self.Game.Connect_to_a_server:   # 连接服务器成功
                # 网络数据处理
                temp_data: str = self.Game.Cn.get_server_data()
                if temp_data is not None:
                    data_list = temp_data.split("|")
                    if data_list[0] == '玩家编号':
                        player.Room_player_number = data_list[1]
                    elif data_list[0] == '房间新人':
                        np = Net_Player(Game)
                        np.Room_player_number = data_list[1]
                        np.map_coordinates_x = int(data_list[2])
                        np.map_coordinates_y = int(data_list[3])
                        self.all_sprites.add(np)
                        self.all_net_sprites.add(np)
                    elif data_list[0] == '所有玩家':
                        lb = json.loads(data_list[1])
                        for net_p in lb:
                            np = Net_Player(Game)
                            np.Room_player_number = str(net_p[0])
                            self.all_sprites.add(np)
                            self.all_net_sprites.add(np)
                    elif data_list[0] == 'wjzt':    # 玩家状态
                        for p in self.all_net_sprites:
                            if p.Room_player_number == data_list[1]:
                                p.map_coordinates_x = float(data_list[2])
                                p.map_coordinates_y = float(data_list[3])
                                p.face = data_list[4]
                                p.Handheld.angle = float(data_list[5])
                    elif data_list[0] == '发射子弹':
                        for net_pl in self.all_net_sprites:
                            if net_pl.Room_player_number == data_list[1]:
                                net_pl.Handheld.use()
                                zd = bullet(Game, net_pl, float(data_list[5]))
                                zd.world_x = float(data_list[2])
                                zd.world_y = float(data_list[3])
                                self.all_sprites.add(zd)
                                self.all_bullet_list.add(zd)



    # 大厅
    def hall_w(self, Game):  # 大厅界面
        # pygame.mouse.set_visible(True)  # 显示鼠标
        self.Zy.Play_background_music()  # 播放背景音乐

        try:
            f = open('File_data/ip.log', 'r')
            serverip = f.read()
            self.Game.Cn.ip = serverip
            self.Game.Cn.lj_server()
            self.Game.Connect_to_a_server = True    # True表示连接到服务器
            # start_new_thread(self.run_threaded_, ())
            self.run_threaded_()
        except Exception as con_rest:  # 报错应该是服务端关闭了连接/服务器ip地址不存在
            print("服务端连接失败", con_rest)

        lobby_runs = True
        while lobby_runs:
            Game.clock.tick(Game.FPS)  # 每秒循环次数
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # 判断是否按下退出
                    lobby_runs = False
                    # Game.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # 检查鼠标左键单击
                    if event.button == 1:
                        print("鼠标左键被单击")
                        lobby_runs = False


            # 数据计算处理
            ...

            # 显示画面
            Game.screen.fill(Game.WHITE)  # 画布涂上白色覆盖上一次画面
            bj_size = (3423 / 4.5, 2263 / 4.5)
            bj = pygame.transform.smoothscale(self.Zy.Lobby_background, bj_size)
            Game.screen.blit(bj, (0, -100))  # 绘制地图
            pygame.display.update()

    def map_w(self, Game):
        pygame.mouse.set_visible(False)  # 隐藏鼠标

        self.all_sprites = pygame.sprite.Group()  # 所有角色绘制的克隆体列表
        self.all_net_sprites = pygame.sprite.Group()  # 所有网络角色绘制的克隆体列表
        self.all_weapons = pygame.sprite.Group()  # 所有武器绘制的克隆体列表
        self.all_bullet_list = pygame.sprite.Group()  # 所有子弹绘制的克隆体列表

        player = Player(Game)
        self.all_sprites.add(player)

        if self.Game.Connect_to_a_server:  # 连接服务器成功
            start_new_thread(self.threaded_dispose, (Game, player))
            Temp_Number = random.randint(100000, 999999)
            # .getsockname()[0]
            my_ip = self.Game.Cn.kfd_socket.getsockname()[0]
            my_dk = self.Game.Cn.kfd_socket.getsockname()[1]
            time.sleep(0.5)
            temp_data = f"加入房间|{Temp_Number}|{my_dk}"
            self.Game.Cn.send(temp_data)

        while Game.running:
            Game.clock.tick(Game.FPS)  # 每秒循环次数
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # 判断是否按下退出
                    Game.running = False

            # 长按事件
            if pygame.mouse.get_pressed()[0]:  # 左键
                player.Handheld.use()

            # 数据计算处理
            screen_map_x = self.MAP_X - self.camera_x  # 计算地图x位置
            screen_map_y = self.MAP_Y - self.camera_y  # 计算地图y位置
            self.camera_x += (player.map_coordinates_x - (self.camera_x + Game.WIDTH / 2)) / 18
            self.camera_y += (player.map_coordinates_y - (self.camera_y + Game.HEIGHT / 2)) / 18
            self.all_sprites.update()               # 更新游戏精灵计算
            self.all_weapons.update()               # 更新游戏武器计算
            image_zx, zx_k = zun_x_draw(Game)       # 准星计算

            # 子弹击中
            for zd in self.all_bullet_list:
                for df in self.all_net_sprites:
                    # 检测碰撞
                    if zd.rect2.colliderect(df.rect2):
                        if zd.Master.Room_player_number != df.Room_player_number:
                            df.hp -= 5
                            zd.kill()
                if zd.rect2.colliderect(player.rect2) and zd.Master.Room_player_number != player.Room_player_number:
                    player.hp -= 5
                    zd.kill()

            if self.Game.Connect_to_a_server:   # 连接服务器成功
                wj_bh = player.Room_player_number
                wz_x = player.map_coordinates_x
                wz_y = player.map_coordinates_y
                mx = player.face
                jd = player.Handheld.angle
                hp = player.hp
                temp_data = f"wjzt|{wj_bh}|{wz_x}|{wz_y}|{mx}|{jd}|{hp}|"   # 玩家状态
                try:
                    self.Game.Cn.send(temp_data)
                    # print('出发数据》', temp_data)
                except OSError:
                    print('应该是服务器断开连接')
                    self.Game.Connect_to_a_server = False
                    ...




            # 显示画面(图层绘制顺序
            Game.screen.fill(Game.WHITE)  # 画布涂上白色覆盖上一次画面
            Game.screen.blit(self.Zy.map_image, (screen_map_x, screen_map_y))  # 绘制地图
            self.all_sprites.draw(Game.screen)  # 把角色列表画到屏幕窗口上
            self.all_weapons.draw(Game.screen)  # 把武器列表画到屏幕窗口上

            for qb in self.all_net_sprites:  # 绘制敌人血条
                # draw_text(self.Game.screen, qb.name, 18, qb.rect.centerx - 50, qb.collision_box.top - 40)
                draw_health(self.Game.screen, Game, Game.GREEN, qb.hp, qb.hp_max, qb.rect.centerx - 50, qb.rect.top+30)
            draw_health(self.Game.screen, Game, Game.GREEN, player.hp, player.hp_max, player.rect.centerx - 50, player.rect.top+30)
            # perspective(Game, player)     # 透视


            Game.screen.blit(image_zx, zx_k)        # 绘制准星
            pygame.display.update()
