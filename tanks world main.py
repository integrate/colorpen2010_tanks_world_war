import wrap, random

wrap.world.create_world(1300, 700)
wrap.world.set_title('TANKS WORLD TYCOON')

# for y in range(1,701,16):
#     for x in range(1, 1301, 16):
#         wrap.sprite.add('battle_city_items', x, y, 'block_bushes')
spisok_wodi = []
for y in [200]:
    for x in range(1, 1301, 16):
        woda = wrap.sprite.add('battle_city_items', x, y, 'block_water3')
        spisok_wodi.append(woda)

player1 = wrap.sprite.add('battle_city_tanks', 1300 / 2, 700 / 2, 'tank_player_size1_green1')
a = wrap.sprite.add_text('1', 50, 50, )
ammo1 = wrap.sprite.add('battle_city_items', 50, 50, 'bullet')
ammo3 = wrap.sprite.add('battle_city_items', 100, 100, 'bullet')
wrap.sprite.set_angle(ammo1, 90)
wragid = False
wrag = wrap.sprite.add('battle_city_tanks', 750, 550, 'tank_enemy_size1_white1')


def wall_builder(x, y):
    stena = wrap.sprite.add('battle_city_items', x, y, 'block_brick')
    spisocsten.append(stena)


# down1
spisocsten = []
wall_builder(550, 250)
wall_builder(550, 282)
wall_builder(550, 314)
wall_builder(550, 346)
wall_builder(550, 378)
wall_builder(550, 410)
wall_builder(550, 442)
wall_builder(550, 474)
wall_builder(774, 378)
wall_builder(774, 410)
wall_builder(774, 442)
wall_builder(774, 474)
wall_builder(774, 250)
wall_builder(774, 282)
wall_builder(774, 314)
wall_builder(774, 346)
wall_builder(582, 250)
wall_builder(614, 250)
wall_builder(646, 250)
wall_builder(582, 474)
wall_builder(614, 474)
wall_builder(646, 474)
wall_builder(678, 474)
wall_builder(678, 250)
wall_builder(710, 250)
wall_builder(742, 250)


@wrap.on_mouse_down(1)
def shot():
    global ammo1
    wrap.sprite.remove(ammo1)
    ammo1 = wrap.sprite.add('battle_city_items', 50, 50, 'bullet')
    x, y = wrap.sprite.get_pos(player1)
    wrap.sprite.move_to(ammo1, x, y)
    vmanip = wrap.sprite.get_angle(player1)
    wrap.sprite.set_angle(ammo1, vmanip)


def botshot():
    global ammo3
    wrap.sprite.remove(ammo3)
    ammo3 = wrap.sprite.add('battle_city_items', 50, 50, 'bullet')
    x, y = wrap.sprite.get_pos(wrag)
    wrap.sprite.move_to(ammo3, x, y)
    vmanip = wrap.sprite.get_angle(wrag)
    wrap.sprite.set_angle(ammo3, vmanip)


@wrap.always(1000)
def bot():
    global wragid
    botdeistvia = random.randint(1, 3)
    if botdeistvia == 1:
        wragid = False
        botshot()
    elif botdeistvia == 2:
        wragid = False
        wrap.sprite.set_angle(wrag, random.choice([0, 90, 180, -90]))
    elif botdeistvia == 3:
        wragid = True


@wrap.always
def gobot():
    if wragid == True:
        wrap.sprite.move_at_angle_dir(wrag, 5)
        if wrap.sprite.is_collide_any_sprite(wrag, spisocsten):
            wrap.sprite.move_at_angle_dir(wrag, -5)


@wrap.on_key_always(wrap.K_w)
def goup():
    wrap.sprite.move(player1, 0, -5)
    wrap.sprite.set_angle(player1, 0)
    s = wrap.sprite.is_collide_any_sprite(player1, spisocsten)
    w = wrap.sprite.is_collide_any_sprite(player1, spisok_wodi)
    if s != None or w != None:
        wrap.sprite.move(player1, 0, 5)

    x, y = wrap.sprite.get_pos(player1)
    wrap.sprite.move_to(a, x, y)


@wrap.on_key_always(wrap.K_s)
def godown():
    wrap.sprite.move(player1, 0, 5)
    wrap.sprite.set_angle(player1, 180)

    if wrap.sprite.is_collide_any_sprite(player1, spisocsten) or wrap.sprite.is_collide_any_sprite(player1,
                                                                                                   spisok_wodi):
        wrap.sprite.move(player1, 0, -5)

    x, y = wrap.sprite.get_pos(player1)
    wrap.sprite.move_to(a, x, y)


@wrap.on_key_always(wrap.K_d)
def goright():
    wrap.sprite.move(player1, 5, 0)
    wrap.sprite.set_angle(player1, 90)

    if wrap.sprite.is_collide_any_sprite(player1, spisocsten) or wrap.sprite.is_collide_any_sprite(player1,
                                                                                                   spisok_wodi):
        wrap.sprite.move(player1, -5, 0)

    x, y = wrap.sprite.get_pos(player1)
    wrap.sprite.move_to(a, x, y)


@wrap.on_key_always(wrap.K_a)
def goleft():
    wrap.sprite.move(player1, -5, 0)
    wrap.sprite.set_angle(player1, -90)

    if wrap.sprite.is_collide_any_sprite(player1, spisocsten) or wrap.sprite.is_collide_any_sprite(player1,
                                                                                                   spisok_wodi):
        wrap.sprite.move(player1, 5, 0)

    x, y = wrap.sprite.get_pos(player1)
    wrap.sprite.move_to(a, x, y)


@wrap.always(1000 / 50)
def fav():
    wrap.sprite.move_at_angle_dir(ammo1, 5)
    if wrap.sprite.is_collide_any_sprite(ammo1, spisocsten):
        wrap.sprite.hide(ammo1)
    if wrap.sprite.is_collide_sprite(ammo1, wrag):
        wrap.sprite.hide(ammo1)
        wrap.sprite.hide(wrag)


@wrap.always(1000 / 50)
def botfav():
    wrap.sprite.move_at_angle_dir(ammo3, 5)
    if wrap.sprite.is_collide_any_sprite(ammo3, spisocsten) :
        wrap.sprite.hide(ammo3)
    if wrap.sprite.is_collide_sprite(ammo3,player1):
        wrap.sprite.hide(ammo3)
        wrap.sprite.move_to(player1,1300/2,700/2)


# база

wrap.sprite.add('battle_city_items', 600, 282, 'base')
