import DrawNewYear
# import math
# import tkinter as tk
# from time import sleep
#
# from PIL import ImageGrab
# from turtle import *
# import random
# import constants as consts


# root = tk.Tk()
# root.configure(bg="gray95")
# screen = tk.Canvas(root, width=1366, height=768, bg="black")
# screen.create_rectangle(root.winfo_rootx(), root.winfo_rooty(), root.winfo_width(), root.winfo_height(), fill='black')
# screen.pack()
# ground_r = 5000
# min_flower_head = 10
# max_flower_head = 50
# screen = getscreen()
# screen.setup(1366, 768)
# screensize(canvwidth=1300, canvheight=600, bg='black')

# def draw_picture():
#     turt = Turtle()
#     sleep(5)
#     hideturtle()
#     turt.ht()
#     turt.speed(500)
#
#     draw_sky(turt)
#     draw_ground(turt)
#     draw_forest(turt, 6)
#     done()
#
#
# # region Fir Tree
# def draw_forest(turt: Turtle, trees: int):
#     pos_xy = get_positions_fir_tree_on_ground(turt, trees, True)
#     for i in range(trees):
#         draw_fir_tree(turt, is_distant=True, xy=pos_xy[i], with_garlands=False)
#
#     x, y = get_position_tree_trunk(turt, is_distant=False, angle_min=-0.5, angle_max=0.5)
#     draw_fir_tree(turt, is_distant=False, xy=(x, y), with_garlands=True, is_straight=True)
#
#
# def draw_fir_tree(turt: Turtle, is_distant: bool, xy: (), with_garlands: bool = False, is_straight: bool = None):
#     tree_size = random.randint(500, 1000)                           # размер дерева
#     star_size = int(tree_size / 30)                                 # размер звезды
#     branches_xy = draw_tree_trunk(turt, tree_size, is_distant, xy=xy, is_straight=is_straight)     # массив начал ветвей
#
#     if is_distant:
#         turt.color(consts.distant_tree_colors)
#     else:
#         turt.color(consts.jewelry_tree_colors)
#     turt.pensize(3)
#     circle_xy = draw_tree_branches(turt, tree_size, branches_xy)
#
#     if with_garlands:
#         draw_tree_garlands(turt, circle_xy)
#         head_x, head_y = branches_xy[len(branches_xy) - 1]
#         draw_fir_tree_star(turt, star_size, head_x, head_y)
#
#
# def draw_fir_tree_star(turt: Turtle, star_size: int, x: float, y: float, rays: int = 5):
#     turt.color('gold')
#     goto_position(turt, x - (star_size * 0.35), y - star_size / 2)
#     turt.rt(int(-180 / rays))
#     turt.pendown()
#     turt.pensize(1)
#
#     turt.begin_fill()
#     turt.fd(star_size)
#     for i in range(5):
#         turt.rt(int(180 + 180 / rays))
#         turt.fd(star_size)
#     turt.end_fill()
#
#
# def draw_tree_branches(turt: Turtle, tree_size: int, branches_xy: []):
#     angle_x = 0                                             # изменение угла
#     side_r = 11                                             # множитель радиуса ветви
#     branches = 11                                           # кол-во веток на один промежуток угла
#     garlands_xy = []                                          # массив позиций гирлянд если они нужны
#     branches_size = random.randint(500, int(tree_size))     # длина ветви
#
#     for i in range(len(branches_xy) - 1):
#         angle_min = 10 + angle_x    # минимальный угол поворота
#         angle_max = 30 + angle_x    # максимальный угол поворота
#         size_x = 1.5                # множитель радиуса ветви
#         cur_circle_xy_l = []        # массив позиций гирлянды слева
#         cur_circle_xy_r = []        # массив позиций гирлянды справа
#
#         turt.pensize(2)
#
#         for k in range(branches - 1):
#             for l in range(branches - k):
#             # for l in range(2):
#                 angle = random.uniform(angle_min, angle_max)
#                 branch_x, branch_y = branches_xy[i]
#                 branches_size = random.randint(500, int(branches_size))
#
#                 goto_position(turt, branch_x, branch_y)
#                 turt.pendown()
#                 turt.rt(angle)
#                 turt.circle(branches_size, int((side_r * size_x)))
#                 if i != (len(branches_xy) - 1):
#                     cur_circle_xy_r.append(turt.pos())
#
#                 branches_size = random.randint(500, int(branches_size))
#                 goto_position(turt, branch_x, branch_y)
#                 turt.pendown()
#                 turt.rt(-angle)
#                 turt.circle(branches_size, int(-side_r * size_x))
#                 if i != (len(branches_xy) - 1):
#                     cur_circle_xy_l.append(turt.pos())
#             angle_max += 8
#             angle_min += 8
#             size_x -= 0.1
#         side_r -= 1
#         angle_x += 5
#
#         if len(cur_circle_xy_l) > 0:
#             garlands_xy.append(random.choice(cur_circle_xy_l))
#         if len(cur_circle_xy_r) > 0:
#             garlands_xy.append(random.choice(cur_circle_xy_r))
#     return garlands_xy
#
#
# def draw_tree_garlands(turt: Turtle, circle_xy: []):
#     for i in range(len(circle_xy)):
#         x, y = circle_xy[i]
#         goto_position(turt, x, y)
#         turt.pendown()
#         turt.color(random.choice(consts.garland_colors))
#         turt.dot(random.randint(int(15 - i / 2), int(15 - i / 3)))
#
#
# def draw_tree_trunk(turt: Turtle, size: int, is_distant: bool, xy: () = None, is_straight: bool = None):
#     x, y = xy
#
#     x = int(x * 0.8)
#     goto_position(turt, x, y)
#     turt.color('peru')
#     turt.pen(pendown=True)
#     turt.rt(-90)
#
#     if is_straight is None:
#         if random.random() >= 0.5:
#             return draw_tree_truck_oblique(turt, size)
#         else:
#             return draw_tree_truck_straight(turt, size)
#     elif is_straight:
#         return draw_tree_truck_straight(turt, size)
#     else:
#         return draw_tree_truck_oblique(turt, size)
#
#
# def draw_tree_truck_oblique(turt: Turtle, size: int, trunks: int = 10):
#     branches_pos_xy = []
#     trunk_length = trunks
#     side = 1
#
#     if random.random() < 0.5:
#         side = -1
#
#     turt.pensize(trunk_length)
#     turt.circle(side * size, int(trunk_length) / 2)
#     for i in range(trunks):
#         turt.pensize(trunk_length)
#         turt.circle(side * size, int(trunk_length) / 2)
#         branches_pos_xy.append(turt.pos())
#         trunk_length -= 1
#
#     return branches_pos_xy
#
#
# def draw_tree_truck_straight(turt: Turtle, size: int, trunks: int = 10):
#     branches_pos_xy = []
#     size = int(size / 100) + 5
#     trunk_length = trunks
#
#     turt.pensize(trunk_length)
#     turt.fd(int(trunk_length * size / 2))
#     for i in range(trunks):
#         turt.pensize(trunk_length)
#
#         turt.fd(int(trunk_length * size / 2))
#         branches_pos_xy.append(turt.pos())
#         trunk_length -= 1
#     return branches_pos_xy
#
#
# def get_positions_fir_tree_on_ground(turt: Turtle, trees: int, is_distant: bool):
#     goto_ground_center(turt)
#     delta = 7 / trees
#     pos_xy = []
#
#     for i in range(trees):
#         goto_ground_center(turt)
#         # turt.pendown()
#         # turt.pensize(3)
#         # turt.color('yellow')
#         # turt.rt(180)
#         # turt.fd(int((ground_r - int(screen.window_height() / 5))))
#         # turt.rt(-90)
#         #
#         # angle = random.uniform(delta * trees - i, delta * (trees + 1 - i))
#         # if random.random() < 0.5:
#         #     angle = -angle
#         #
#         # turt.circle(ground_r - int(screen.window_height() / 5), angle)
#         # turt.circle(ground_r - int(screen.window_height() / 5), 5)
#         # x, y = turt.pos()
#         # if is_distant:
#         #     y = random.uniform(-screen.window_height() / 4, y)
#         # else:
#         #     y = random.uniform(-screen.window_height() / 2, -screen.window_height() / 2.5)
#
#         angle_min = delta * trees - i
#         angle_max = delta * (trees + 1 - i)
#         pos_xy.append(get_position_tree_trunk(turt, is_distant, angle_min, angle_max))
#         delta *= -1
#
#     return pos_xy
#
#
# def get_position_tree_trunk(turt: Turtle, is_distant: bool, angle_min: float, angle_max: float):
#     goto_ground_center(turt)
#     turt.rt(180)
#     turt.fd(int((ground_r - int(screen.window_height() / 5))))
#     turt.rt(-90)
#
#     angle = random.uniform(angle_min, angle_max)
#     turt.circle(ground_r - int(screen.window_height() / 5), angle)
#
#     x, y = turt.pos()
#     if is_distant:
#         y = random.uniform(-screen.window_height() / 4, y)
#     else:
#         y = random.uniform(-screen.window_height() / 2, -screen.window_height() / 3)
#
#     return x, y
# # endregion
#
#
#
#
#
#
# # def dump_gui():
# #     """
# #     takes a png screenshot of a tkinter window, and saves it on in cwd
# #     """
# #     print('...dumping gui window to png')
# #
# #     x0 = root.winfo_rootx()
# #     y0 = root.winfo_rooty()
# #     x1 = x0 + root.winfo_width()
# #     y1 = y0 + root.winfo_height()
# #     ImageGrab.grab().crop((x0, y0, x1, y1)).save("gui_image_grabbed.png")
#
#
# def draw_geometric_figures(turt: Turtle):
#     for i in range(150):
#         x = random.gauss(0, screen.winfo_width() / 2)
#         y = random.gauss(0, screen.winfo_height() / 2)
#
#         goto_position(turt, x, y)
#         set_random_color(turt)
#         turt.pen(pendown=True)
#
#         figure_size = random.randint(20, 40)
#         figure_angles = random.randint(3, 10)
#
#         if random.random() >= 0.5:
#             draw_figure(turt, figure_angles, figure_size)
#         else:
#             turt.dot(figure_size)
#
#
# def draw_rand_point(turt: Turtle):
#     turt.color('grey')
#     turt.rt(90)
#     x, y = turt.pos()
#     death_star_r = 200
#     # turt.dot(death_star_r * 2)
#     # turt.fd(death_star_r)
#     # turt.color('Silver')
#     turt.color('green')
#     for i in range(500):
#         alpha = (2 * math.pi * random.random()) / 4
#         # random radius
#         r = death_star_r * math.sqrt(random.random())
#         # calculating coordinates
#         new_x = r * math.cos(math.radians(random.uniform(-10, 10))) + x
#         new_y = r * math.sin(math.radians(random.uniform(-10, 10))) + y
#         goto_position(turt, new_x, new_y)
#         turt.pen(pendown=True)
#         # turt.color(random.choice(consts.dead_star_right_colors))
#         turt.dot(random.randint(2, 5))
#
#
# def draw_figure(turt: Turtle, angles: int, size: int):
#     turt.begin_fill()
#     turt.fd(size)
#     for i in range(angles):
#         turt.rt(360 / angles)
#         turt.fd(size)
#     turt.end_fill()
#
#
# def draw_trunk(turt: Turtle):
#     turt.pen(pendown=False)
#     turt.home()
#     turt.pen(pendown=True)
#     set_trunk_color(turt)
#     turt.rt(90)
#     turt.pensize(5)
#     turt.forward(100)
#
#     turt.lt(90)
#     turt.pensize(4)
#     turt.forward(10)
#
#     turt.rt(90)
#     turt.pensize(3)
#     turt.forward(5)
#
#     turt.lt(90)
#     turt.pensize(2)
#     turt.forward(3)
#     goto_ground_center(turt)
#     set_trunk_color(turt)
#
#
# def set_random_color(turt: Turtle):
#     r = random.randint(10, 40) / 100
#     g = random.randint(10, 40) / 100
#     b = random.randint(10, 40) / 100
#     turt.color(r, g, b)
#
#
# # region Sky
# def draw_sky(turt: Turtle):
#     draw_sky_starts(turt)
#     draw_moon(turt)
#
#
# def draw_sky_starts(turt: Turtle):
#     small_stars = random.randint(500, 1000)
#     big_stars = random.randint(75, 100)
#     meteors = random.randint(1, 5)
#     for i in range(small_stars):
#         turt.color(random.choice(consts.star_colors))
#         draw_small_star(turt)
#
#     for i in range(big_stars):
#         turt.color(random.choice(consts.star_colors))
#         draw_star(turt)
#
#     for i in range(meteors):
#         turt.color(random.choice(consts.star_colors))
#         draw_meteor(turt)
#
#
# def draw_moon(turt: Turtle):
#     size = random.randint(50, 75)
#     y = random.randint(0 + int(screen.window_height() / 3), int(screen.window_height() / 2) - size)
#     x = random.randint(0 - (int(screen.window_width() / 2) - size), int(screen.window_width() / 2) - size)
#
#     goto_position(turt, x, y)
#     turt.pen(pendown=True)
#     turt.color('yellow')
#     turt.dot(size)
#
#     x_delta, y_delta = get_moon_phase(size)
#     goto_position(turt, x + x_delta, y + y_delta)
#     turt.pen(pendown=True)
#     turt.color("black")
#     turt.dot(size * 2)
#
#
# def get_moon_phase(moon_size: int):
#     x_delta = int(moon_size / random.uniform(1.5, 2.0))
#     y_delta = int(moon_size / random.uniform(1.5, 2.0))
#
#     if random.random() >= 0.5:
#         return x_delta, y_delta
#     else:
#         return -x_delta, y_delta
#
#
# def draw_small_star(turt: Turtle):
#     x, y = get_star_position()
#     goto_position(turt, x, y)
#
#     turt.pen(pendown=True)
#     turt.dot(random.randint(1, 3))
#
#
# def draw_star(turt: Turtle, x: float = None, y: float = None, is_meteor: bool = False, size: int = None):
#     if (x is None) or (y is None):
#         x, y = get_star_position()
#
#     goto_position(turt, x, y)
#
#     turt.pen(pendown=True)
#     turt.pensize(1)
#     turt.begin_fill()
#
#     if is_meteor:
#         ray_size = random.randint(6, 8)
#     elif size is None:
#         ray_size = random.randint(3, 7)
#     else:
#         ray_size = size
#
#     turt.fd(ray_size)
#     for i in range(5):
#         turt.rt(int(180 + 180 / 5))
#         turt.fd(ray_size)
#     turt.end_fill()
#
#
# def get_star_position():
#     y = float(random.gauss(0, int(screen.window_height() / 2)))
#     x = float(random.gauss(0, int(screen.window_width() / 2)))
#     return x, y
#
#
# def draw_meteor(turt: Turtle):
#     goto_home(turt)
#     x = random.gauss(0, screen.window_width() / 2)
#     y = random.gauss(screen.window_height() / 3, screen.window_height() / 10)
#     goto_position(turt, x, y)
#
#     size = random.randint(500, 1000)
#
#     turt.pen(pendown=True)
#     if random.random() >= 0.5:
#         side = 1
#     else:
#         side = -1
#
#     turt.rt(side * random.uniform(135, 170))
#     turt.pensize(1)
#     turt.circle(size, 3 * side)
#     turt.pensize(2)
#     turt.circle(size, 3 * side)
#     turt.pensize(3)
#     turt.circle(size, 3 * side)
#
#     x, y = turt.pos()
#     draw_star(turt, x, y, True)
#
# # endregion
#
#
# # region Flowers
# def draw_flowers(turt: Turtle, flower_size: int = 2):
#     flowers = random.randint(10, 20)
#     for i in range(flowers):
#         x, y = get_position_on_ground(turt)
#         flower_size = random.uniform(2, 4)
#         trunk_len = 40 * flower_size
#         turt.pensize(2 * flower_size)
#         set_trunk_color(turt)
#         turt.pen(pendown=True)
#         turt.rt(90)
#         turt.fd(trunk_len)
#
#         head_x, head_y = turt.pos()
#
#         draw_flower_leaves(turt, trunk_len, x, y)
#         goto_position(turt, head_x, head_y)
#         petals = random.randint(2, 6)
#         draw_flower_head(turt, petals, flower_size * 10 - 10)
#
#
# def draw_flower_leaves(turt: Turtle, trunk_len: float, x: float, y: float):
#     goto_position(turt, x, y)
#     turt.pensize(1)
#     turt.color('grey', 'green')
#
#     turt.fd(trunk_len - int(trunk_len / 1.3))
#     turt.pen(pendown=True)
#     turt.begin_fill()
#     turt.rt(90)
#     turt.circle(int(trunk_len / 5), 90)
#     turt.rt(-90)
#     turt.circle(int(trunk_len / 5), 90)
#     turt.end_fill()
#
#     goto_position(turt, x, y)
#     turt.rt(180)
#     turt.fd(trunk_len - int(trunk_len / 3))
#     turt.pen(pendown=True)
#     turt.begin_fill()
#     turt.rt(360)
#     turt.circle(int(trunk_len / 7), 90)
#     turt.rt(-90)
#     turt.circle(int(trunk_len / 7), 90)
#     turt.end_fill()
#
#
# def draw_flower_head(turt: Turtle, petals: int = 2, petal_size: int = 25):
#     turt.pen(pendown=True)
#     turt.pensize(1)
#
#     step = int(4 * petals)
#     angle = int(90 / petals)
#
#     if petals == 3:
#         angle = 60
#
#     turt.color('grey', random.choice(consts.petal_colors))
#     for i in range(step):
#         draw_petal(turt, petal_size)
#         turt.rt(angle)
#
#     turt.color('yellow')
#     turt.dot(int(petal_size/2))
#
#
# def draw_petal(turt: Turtle, petal_size: int = 25):
#     turt.pen(pendown=True)
#     turt.begin_fill()
#     turt.circle(petal_size, 90)
#     turt.rt(-90)
#     turt.circle(petal_size, 90)
#     turt.end_fill()
# # endregion
#
#
# # region Ground
# def draw_ground(turt: Turtle):
#     goto_ground_center(turt)
#     turt.color('snow')
#     # set_ground_color(turt)
#     turt.dot(int((ground_r - int(screen.window_height() / 5)) * 2))
#
#
# def get_position_on_ground(turt: Turtle):
#     goto_ground_center(turt)
#     turt.pensize(3)
#     turt.color('black')
#     turt.rt(180)
#     turt.fd(int((ground_r - int(screen.window_height() / 5))))
#     turt.rt(-90)
#     turt.circle(ground_r - int(screen.window_height() / 5), random.normalvariate(0, 3))
#
#     x, y = turt.pos()
#     y = random.uniform(-screen.window_height() / 2, y)
#     turt.goto(x, y)
#     return x, y
#
#
# def goto_ground_center(turt: Turtle):
#     goto_position(turt, 0, 0)
#     turt.rt(90)
#     turt.forward(ground_r)
# # endregion
#
#
# # region Goto
# def goto_position(turt: Turtle, x: float = 0.0, y: float = 0.0):
#     turt.pen(pendown=False)
#     turt.setheading(0)
#     turt.goto(x, y)
#
#
# def goto_home(turt: Turtle):
#     turt.pen(pendown=False)
#     turt.home()
# # endregion
#
#
# def set_flower_petal_color(turt: Turtle):
#     turt.color('grey', 'purple')
#
#
# def set_trunk_color(turt: Turtle):
#     turt.color('green')
#
#
# def set_ground_color(turt: Turtle):
#     turt.color("darkgreen")
#
#
# def set_root_color(turt: Turtle):
#     turt.color('brown')


if __name__ == '__main__':
    DrawNewYear.draw_new_year()
