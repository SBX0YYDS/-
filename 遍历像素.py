
import pygame
import sys
import os

pygame.init()

size = Width,Height = 960,540 #窗口大小960,540
batch = 20 #帧数
title = "遍历像素"

pygame.display.set_caption(title) #标题
font = pygame.font.Font(None,50)
clock = pygame.time.Clock()#帧数调整
color = (0,0,0) #设置颜色

while True :
    image = input("图片目录/名称:")
    if image == "exit" :
        print("程序已关闭!")
        pygame.quit()
        sys.exit()
    elif not os.path.exists(image) :
        print("无此文件!")
    else :
        screen = pygame.display.set_mode(size,0,32) #显示窗口
        image = pygame.image.load(image).convert_alpha()
        break


w,h = image.get_size()
print(f"图片大小:{w}*{h}")

R1 = int(input("R最大值:"))
G1 = int(input("G最大值:"))
B1 = int(input("B最大值:"))
A1 = int(input("A最大值:"))

R2 = int(input("R最小值:"))
G2 = int(input("G最小值:"))
B2 = int(input("B最小值:"))
A2 = int(input("A最小值:"))

R3 = int(input("R修改值:"))
G3 = int(input("G修改值:"))
B3 = int(input("B修改值:"))
A3 = int(input("A修改值:"))

x = 0
y = 0
while True:
    # 事件处理放在最外层，关闭窗口立刻生效
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            import sys
            sys.exit()

    # 每一帧处理一批像素
    for _ in range(batch):
        if x >= w:
            break
        r,g,b,a = image.get_at((x, y))
        if R1 >= r >= R2 and G1 >= g >= G2 and B1 >= b >= B2 and A1 >= a >= A2:
            image.set_at((x,y),(R3,G3,B3,A3))

        # 坐标前进
        y += 1
        if y >= h:
            y = 0
            x += 1

    # 渲染画面，每一帧只刷新一次
    screen.fill((0,0,0))
    screen.blit(image,(Width//2-w//2,Height//2-h//2))
    debug_text = font.render(f"进度 x:{x}/{w}", True, (255,255,255))
    screen.blit(debug_text, (0,0))

    pygame.display.update()
    clock.tick(60)

    # 判断全部像素处理完毕
    if x >= w:
        print("全部像素修改完成")
        break

pygame.image.save(image,"new.png")
pygame.quit()
sys.exit()
