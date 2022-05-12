import pygame	 # 导入pygame库
import numpy as np
import Global
import logic
import init

class uiFunction:
    comp = []	 # 储存组件

    def init(self, size, title):	 # 初始化，明确窗口的大小和标题
        pygame.init()
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption(title)
        return screen	# 返回screen后面用

    def listening(self):	 # 监听鼠标事件
        x, y = pygame.mouse.get_pos()	 # 获取鼠标位置
        for m in self.comp:	 # 遍历组件
            if m[-1][0] <= x <= m[-1][0]+m[-1][2] and m[-1][1] <= y <= m[-1][3]+m[-1][1]:	 # 判断鼠标是否在组件上
                m[-2] = True
            else:
                m[-2] = False

    def button(self, size, position, font, font_color, background,
               click_f_color, click_background, edge=5, width=0, title="Button"):	 # 添加按钮组件
        if_click = False
        crash_rect = [0, 0, 0, 0]	 # “碰撞体”，鼠标在这个范围算碰撞
        return ["bu", title, position, font, background, font_color,
                size, width, click_f_color, click_background, edge, if_click, crash_rect]

    def label(self, size, position, font, font_color, background=0, title="Label",
              edge=5, width=0):	 # 标签组件
        if_click = False
        crash_rect = [0, 0, 0, 0]
        return ["la", title, position, font, background, font_color, size, width, edge, if_click, crash_rect]

    def register_cp(self, way):	 # 注册组件
        self.comp.append(way)

    def text_objects(self, text, font, color):	 # 定义文字
        text_surface = font.render(text, True, color)
        return text_surface, text_surface.get_rect()

    def display(self, scr, com):	 # 显示组件
        for n in com:
            if n[0] == "bu":    # 如果是按钮
                if n[11]:   # 判断是否点击
                    large_text = pygame.font.Font(n[3], n[6])
                    text_surf, text_rect = self.text_objects(n[1], large_text, n[8])
                    text_rect.center = n[2]
                    pygame.draw.rect(scr, n[9], (text_rect.left - n[10],
                                                 text_rect.top - n[10],
                                                 text_rect.width + n[10] * 2,
                                                 text_rect.height + n[10] * 2), n[7])
                    scr.blit(text_surf, text_rect)	 # 把字刻在屏幕上
                    n[12] = text_rect
                else:
                    large_text = pygame.font.Font(n[3], n[6])
                    text_surf, text_rect = self.text_objects(n[1], large_text, n[5])
                    text_rect.center = n[2]
                    pygame.draw.rect(scr, n[4], (text_rect.left-n[10],
                                                 text_rect.top-n[10],
                                                 text_rect.width+n[10]*2,
                                                 text_rect.height+n[10]*2), n[7])
                    scr.blit(text_surf, text_rect)
                    n[12] = text_rect

            if n[0] == "la":    # 如果是标签 'freesansbold.ttf', 115
                large_text = pygame.font.Font(n[3], n[6])
                text_surf, text_rect = self.text_objects(n[1], large_text, n[5])
                text_rect.center = n[2]
                if n[4] != 0:
                    pygame.draw.rect(scr, n[4], (text_rect.left-n[-3],
                                                 text_rect.top-n[-3],
                                                 text_rect.width+n[-3]*2,
                                                 text_rect.height+n[-3]*2), n[-2])
                scr.blit(text_surf, text_rect)

    def event_start(self, mp,screen):
        print("now start")
        startx = 300
        starty = 50
        count = 0
        go_on = 1
        while go_on:
            if(count % 20000000 == 0):
                self.mouse(screen, mp)
                for i in range(Global.Width):
                    for j in range(Global.Height):
                        self.drawCell(startx + i * Global.cellRound, starty + j*Global.cellRound, mp[i][j], screen)
                mp = logic.logic().workEvloution(mp)
                pygame.display.update()
            count = count + 1

    def event_pause(self, mp,screen):
        print("now pause")
        go_on = 1
        startX = 300
        startY = 50
        while go_on:
            self.mouse(screen, mp)
            for i in range(Global.Width):
                for j in range(Global.Height):
                    self.drawCell(startX + i * Global.cellRound, startY + j * Global.cellRound, mp[i][j], screen)

    def event_reset(self, mp, screen):
        print("now reset")
        go_on = 1
        while go_on:
            self.mouse(screen, mp)
            self.initChessBoard(300, 50, screen)
            pygame.display.update()

    def event_random(self, mp,screen):
        print("now random")
        go_on = 1
        startX = 300
        startY = 50
        mp = init.init().initWork()
        for i in range(Global.Width):
            for j in range(Global.Height):
                self.drawCell(startX + i * Global.cellRound, startY + j * Global.cellRound, mp[i][j], screen)
        while go_on:
            self.mouse(screen, mp)
            pygame.display.update()

    def initChessBoard(self, startX,startY,screen):
        for i in range(Global.Height):
            for j in range(Global.Width):
                pygame.draw.rect(screen, Global.white, [startX+j*Global.cellRound,startY+i*Global.cellRound, Global.cellRound - 1, Global.cellRound-1], 10)

    def drawCell(self, x, y, life, screen):
        if life == 1:
            pygame.draw.rect(screen,Global.liveCellColor,[x,y,Global.cellRound-1,Global.cellRound-1],10)
        if life == 0:
            pygame.draw.rect(screen,Global.deadCellColor,[x,y,Global.cellRound-1,Global.cellRound-1],10)

    def mouse(self, scr ,mp):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # 如果点击关闭窗口，则循环结束
                go_on= 0
            elif event.type == pygame.MOUSEMOTION:
                print("[MOUSEMOTTON]:", event.pos, event.rel, event.buttons)
                """pygame.MOUSEMOTTION鼠标移动事件，
                event.pos鼠标当前坐标值(x,y)相对于窗口左上角。
                event.rel鼠标相对移动距离（X,Y),相对于上次事件。
                event.buttons鼠标按钮状态(a,b,c)，相对于鼠标的三个键（左中右），
                鼠标移动时，这三个键处于按下状态，对应的位置为1，
                反之为0"""
            elif event.type == pygame.MOUSEBUTTONUP:
                print("[MOUSEBUTTONUP]:", event.pos, event.button)
                """pygame.MOUSEBUTTONUP鼠标释放事件，
                event.button鼠标按下键编号n，取值0/1/2，分别对应三个键"""
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print("[MOUSEBUTTONDOWN]:", event.pos, event.button)
                x, y = event.pos
                if x >= 40 and x <= 120 and y <= 220 and y >= 180:
                    self.event_start(mp, scr)
                if x >= 37 and x <= 121 and y <= 411 and y >= 388:
                    self.event_pause(mp,scr)
                if x >= 45 and x <= 120 and y <= 608 and y >= 589:
                    self.event_reset(mp,scr)
                if x >= 40 and x <= 120 and y <= 805 and y >= 787:
                    self.event_random(mp,scr)
                    """pygame.MOUSEBUTTONDOWN鼠标键按下事件，
                    event.button鼠标按下键编号n，取值为整数，
                    左键为1，右键为3"""

    def run(self, scr, background):	 # 主循环
        while True:
            mp = init.init().initWork()
            self.mouse(scr ,mp)
            scr.fill(Global.backgroundColor)  # 设置屏幕背景色
            self.display(scr, self.comp)
            self.listening()
            self.initChessBoard(300, 50, scr)
            pygame.display.update()  # 更新屏幕







