import json
import os
import pathlib
import random
from Class.SOCKET_NET import Sn
from _thread import *
import pygame


def draw_text(surf, text, size, x, y, rgb=(255, 255, 255)):  # 绘制文本
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, rgb)
    text_rect = text_surface.get_rect()
    text_rect.left = x
    text_rect.top = y
    surf.blit(text_surface, text_rect)


class server:
    def __init__(self):
        self.Sn = Sn()
        self.Multiplayer_Great_room = list()  # 多人大房间玩家状态列表
        self.Room_number = 1  # 玩家房间编号

    def threaded_data(self):
        self.Sn.run_server()

    def threaded_room(self):
        while True:
            Packets_data: str = self.Sn.get_data()
            if Packets_data is not None:
                data_list = Packets_data.split("|")
                if data_list[0] == "加入房间":
                    bh = self.Room_number
                    for p in self.Sn.client_socket_list:    # 找客服端发送编号
                        if p[2][1] == int(data_list[2]):
                            temp_data = f"玩家编号|{bh}|"
                            self.Sn.send(p[1], temp_data)

                            # 房间所有玩家数据发送给新加入房间的玩家
                            lb = json.dumps(self.Multiplayer_Great_room)
                            temp_data = f"所有玩家|{lb}|"
                            self.Sn.send(p[1], temp_data)

                            temp_data = [bh, p[2], 0, 0]    # 编号，ip，x，y
                            self.Multiplayer_Great_room.append(temp_data)

                        else:
                            temp_data = f"房间新人|{bh}|{random.randint(-200, 200)}|{200}"
                            self.Sn.send(p[1], temp_data)
                    self.Room_number += 1   # 新编号

                elif data_list[0] == "玩家状态":
                    self.Sn.send_All(Packets_data)
                elif data_list[0] == "发射子弹":
                    self.Sn.send_All(Packets_data)
                print("", Packets_data)

    def initiate(self):
        self.Sn.Bind_listeners()
        start_new_thread(self.threaded_data, ())
        start_new_thread(self.threaded_room, ())


if __name__ == '__main__':

    server = server()
    server.Sn.ip = '0.0.0.0'
    server.initiate()

    # 游戏初始化
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((540, 360))  # 创建窗口
    pygame.display.set_caption('——SERVER mmo枪战——')
    folder = pathlib.Path(__file__).parent.resolve()
    font_name = os.path.join(folder, 'font/font.ttf')

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # 判断是否按下退出
                running = False

        # 显示画面(图层绘制顺序
        screen.fill((255, 255, 255))  # 画布涂上白色覆盖上一次画面
        rs = len(server.Sn.client_socket_list)
        draw_text(screen, f"客服端连接个数: {rs}", 18, 5, 0, (0, 0, 0))
        draw_text(screen, f"大房间加入人数: {len(server.Multiplayer_Great_room)}", 18, 5, 20, (0, 0, 0))
        for net_d in server.Sn.client_socket_list:
            draw_text(screen, f"客服端: {net_d[2]}", 18, 20, 60+20*server.Sn.client_socket_list.index(net_d), (0, 0, 0))
        draw_text(screen, f"#"*random.randint(1, 50), 18, 0, 340, (0, 0, 0))

        pygame.display.update()
    pygame.quit()
