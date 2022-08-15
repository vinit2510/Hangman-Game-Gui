from pygame import mixer
import pygame
import random


pygame.init()

# audio play
def play_music(file):
    mixer.music.load(file)
    mixer.music.set_volume(1)
    mixer.music.play()


# size
x = 600
y = 684 


# main window
display = pygame.display.set_mode((x, y), pygame.RESIZABLE)
display.fill((30, 30, 30))

# images
img1 = pygame.image.load(r'src\\1.png')
img2 = pygame.image.load(r'src\\2.png')
img3 = pygame.image.load(r'src\\3.png')
img4 = pygame.image.load(r'src\\4.png')
img5 = pygame.image.load(r'src\\5.png')
img6 = pygame.image.load(r'src\\6.png')
img7 = pygame.image.load(r'src\\7.png')
arrow_img = pygame.image.load(r'src\\front_arrow.png')

# font
smallfont = pygame.font.SysFont('Arial', 36)

txt = smallfont.render("Enter one Word", True, (255, 255, 255))

display.blit(arrow_img, (225, 550))
display.blit(txt, (15, 255))

atoj = "A   B   C   D   E   F   G   H   I   J"
ktor = "K   L   M   N   O   P   Q   R"
stoz = "S   T   U   V   W   X   Y   Z"
line = "____________________________"
line2 = "|"

# title
pygame.display.set_caption('Hangman')
clock = pygame.time.Clock()


# i/p box
input_rect = pygame.Rect(235, 250, 330, 50)
active = False

# all alphabate
alp = [pygame.K_a, pygame.K_b, pygame.K_c, pygame.K_d, pygame.K_e, pygame.K_f, pygame.K_g, pygame.K_h, pygame.K_i, pygame.K_j, pygame.K_k, pygame.K_l, pygame.K_m,
       pygame.K_n, pygame.K_o, pygame.K_p, pygame.K_q, pygame.K_r, pygame.K_s, pygame.K_t, pygame.K_u, pygame.K_v, pygame.K_w, pygame.K_x, pygame.K_y, pygame.K_z, pygame.K_SPACE]

# pre define
screen = 1
true_word = ''
list1 = []
list2 = []
rpt_list = []
check_list = []
wrong_list = []
count = 0
temp = 0


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if screen == 1:

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    play_music("src\\key.mp3")
                    true_word = true_word[:-1]
                else:
                    play_music("src\\key.mp3")
                    true_word += (event.unicode).upper()

            # next btn click
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                if (225 <= mouse_pos[0] <= 375 and 550 <= mouse_pos[1] <= 600) and true_word != '':
                    play_music("src\\pop.mp3")

                    screen = 0
                    display.fill((30, 30, 30))

                    true_word = true_word.upper()
                    list1[:0] = true_word
                    list2[:0] = true_word

                    for i in range(len(list2)):
                        list2[i] = "_"

                    dashstr = ' '.join(map(str, list2))
                    dash_txt = smallfont.render(dashstr, True, (255, 255, 255))

                    rpt_list[:0] = true_word

            # i/p area
            pygame.draw.rect(display, (99, 95, 95), input_rect)
            text_surface = smallfont.render(true_word, True, (255, 255, 255))
            display.blit(text_surface, (input_rect.x+5, input_rect.y+5))
            input_rect.w = max(100, text_surface.get_width()+10)
            pygame.display.flip()

    pygame.event.get()
    keys = pygame.key.get_pressed()

    

    if screen == 0:

        if temp == 0:
            display.blit(dash_txt, (250, 420))

            display.blit(smallfont.render(
                line, True, (255, 255, 255)), (80, 450))
            display.blit(smallfont.render(
                line, True, (255, 255, 255)), (80, 620))

            for i in range(5):
                display.blit(smallfont.render(
                    line2, True, (255, 255, 255)), (78, 480+(34*i)))

            for i in range(5):
                display.blit(smallfont.render(
                    line2, True, (255, 255, 255)), (525, 480+(34*i)))

            display.blit(smallfont.render(
                atoj, True, (255, 255, 255)), (100, 500))
            display.blit(smallfont.render(
                ktor, True, (255, 255, 255)), (120, 550))
            display.blit(smallfont.render(
                stoz, True, (255, 255, 255)), (120, 600))

            if count == 0:
                display.blit(img1, (130, 10))

            temp = 1

        for i in range(len(alp)):

            if keys[alp[i]]:
                s = chr(alp[i]).upper()

                if s != ' ':
                    if s in atoj:
                        atoj = atoj.replace(s, '  ')
                    if s in ktor:
                        ktor = ktor.replace(s, '  ')
                    if s in stoz:
                        stoz = stoz.replace(s, '  ')

                if s in list1:

                    play_music("src\\click.mp3")
                    index = list1.index(s)
                    check_list.append(s)
                    list2[index] = s
                    dashstr = ' '.join(map(str, list2))

                    if len(list1) != set(list1):
                        try:
                            indx = rpt_list.index(s)
                            rpt_list[indx] = '-'
                            index2 = rpt_list.index(s)
                            list2[index2] = s
                            dashstr = ' '.join(map(str, list2))

                        except Exception:
                            None

                else:
                    if s not in wrong_list:
                        wrong_list.append(s)
                        play_music("src\\" +
                                   str(random.randint(1, 7))+".mp3")
                        count = count + 1

                    if count >= 6:
                        play_music("src\\game_over.mp3")
                        screen = 3

                dash_txt = smallfont.render(dashstr, True, (255, 255, 255))

                pygame.time.wait(200)
                display.fill((30, 30, 30))

                if count == 0:
                    display.blit(img1, (130, 10))
                if count == 1:
                    display.blit(img2, (130, 10))
                if count == 2:
                    display.blit(img3, (130, 10))
                if count == 3:
                    display.blit(img4, (130, 10))
                if count == 4:
                    display.blit(img5, (130, 10))
                if count == 5:
                    display.blit(img6, (130, 10))
                if count == 6 or count > 6:
                    display.blit(img7, (130, 10))

                display.blit(dash_txt, (250, 420))

                display.blit(smallfont.render(
                    line, True, (255, 255, 255)), (80, 450))
                display.blit(smallfont.render(
                    line, True, (255, 255, 255)), (80, 620))

                for i in range(5):
                    display.blit(smallfont.render(
                        line2, True, (255, 255, 255)), (78, 480+(34*i)))

                for i in range(5):
                    display.blit(smallfont.render(
                        line2, True, (255, 255, 255)), (525, 480+(34*i)))

                display.blit(smallfont.render(
                    atoj, True, (255, 255, 255)), (100, 500))
                display.blit(smallfont.render(
                    ktor, True, (255, 255, 255)), (120, 550))
                display.blit(smallfont.render(
                    stoz, True, (255, 255, 255)), (120, 600))

                temp = 1

                if set(list1) == set(check_list):

                    play_music("src\\won.mp3")
                    screen = 4

    mouse_pos = pygame.mouse.get_pos()

    #if keys[pygame.K_RETURN]:
    #    print("Enter")

    if screen == 3:  # lost
        if temp == 1:
            display.fill((30, 30, 30))

            display.blit(smallfont.render(
                line, True, (255, 255, 255)), (80, 450))
            display.blit(smallfont.render(
                line, True, (255, 255, 255)), (80, 620))

            for i in range(5):
                display.blit(smallfont.render(
                    line2, True, (255, 255, 255)), (78, 480+(34*i)))

            for i in range(5):
                display.blit(smallfont.render(
                    line2, True, (255, 255, 255)), (525, 480+(34*i)))

            display.blit(img7, (130, 10))
            txt = smallfont.render("You Lost the Game!", True, (240, 39, 39))
            display.blit(txt, (170, 500))

            txt1 = smallfont.render(
                "Correct Word: " + true_word, True, (240, 39, 39))
            display.blit(txt1, (160, 580))
            display.blit(dash_txt, (250, 420))

            temp = 0



    if screen == 4:  # won
        if temp == 1:

            display.fill((30, 30, 30))

            display.blit(smallfont.render(
                line, True, (255, 255, 255)), (80, 450))
            display.blit(smallfont.render(
                line, True, (255, 255, 255)), (80, 620))

            for i in range(5):
                display.blit(smallfont.render(
                    line2, True, (255, 255, 255)), (78, 480+(34*i)))

            for i in range(5):
                display.blit(smallfont.render(
                    line2, True, (255, 255, 255)), (525, 480+(34*i)))

            if count == 0:
                display.blit(img1, (130, 10))
            if count == 1:
                display.blit(img2, (130, 10))
            if count == 2:
                display.blit(img3, (130, 10))
            if count == 3:
                display.blit(img4, (130, 10))
            if count == 4:
                display.blit(img5, (130, 10))
            if count == 5:
                display.blit(img6, (130, 10))
            if count == 6 or count > 6:
                display.blit(img7, (130, 10))

            txt = smallfont.render("You Won the Game!", True, (255, 255, 255))

            display.blit(txt, (170, 550))
            display.blit(dash_txt, (250, 420))

            temp = 0

    pygame.display.update()
    clock.tick(60)      #fps
