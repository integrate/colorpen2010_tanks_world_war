import wrap

wrap.world.create_world(1300, 700)
wrap.world.set_title('TANKS WORLD TYCOON')
player = wrap.sprite.add('battle_city_tanks', 1300 / 2, 700 / 2)
a = wrap.sprite.add_text('1', 50, 50,)
ammo=wrap.sprite.add('battle_city_items',50,50,'bullet')
wrap.sprite.set_angle(ammo,90)

#down1
wrap.sprite.add('battle_city_items',550,250,'block_brick')
wrap.sprite.add('battle_city_items',550,282,'block_brick')
wrap.sprite.add('battle_city_items',550,314,'block_brick')
wrap.sprite.add('battle_city_items',550,346,'block_brick')
#down2
wrap.sprite.add('battle_city_items',550,378,'block_brick')
wrap.sprite.add('battle_city_items',550,410,'block_brick')
wrap.sprite.add('battle_city_items',550,442,'block_brick')
wrap.sprite.add('battle_city_items',550,474,'block_brick')
#down3
wrap.sprite.add('battle_city_items',774,378,'block_brick')
wrap.sprite.add('battle_city_items',774,410,'block_brick')
wrap.sprite.add('battle_city_items',774,442,'block_brick')
wrap.sprite.add('battle_city_items',774,474,'block_brick')
#down4
wrap.sprite.add('battle_city_items',774,250,'block_brick')
wrap.sprite.add('battle_city_items',774,282,'block_brick')
wrap.sprite.add('battle_city_items',774,314,'block_brick')
wrap.sprite.add('battle_city_items',774,346,'block_brick')
#right1
wrap.sprite.add('battle_city_items',582,250,'block_brick')
wrap.sprite.add('battle_city_items',614,250,'block_brick')
wrap.sprite.add('battle_city_items',646,250,'block_brick')
#right2
wrap.sprite.add('battle_city_items',582,474,'block_brick')
wrap.sprite.add('battle_city_items',614,474,'block_brick')
wrap.sprite.add('battle_city_items',646,474,'block_brick')
#right3
wrap.sprite.add('battle_city_items',678,474,'block_brick')
wrap.sprite.add('battle_city_items',710,474,'block_brick')
wrap.sprite.add('battle_city_items',742,474,'block_brick')
#right4
wrap.sprite.add('battle_city_items',678,250,'block_brick')
wrap.sprite.add('battle_city_items',710,250,'block_brick')
wrap.sprite.add('battle_city_items',742,250,'block_brick')

@wrap.on_mouse_down(1)
def shot():
    global ammo
    wrap.sprite.remove(ammo)
    ammo=wrap.sprite.add('battle_city_items',50,50,'bullet')
    x, y = wrap.sprite.get_pos(player)
    wrap.sprite.move_to(ammo, x, y)
    vmanip=wrap.sprite.get_angle(player)
    wrap.sprite.set_angle(ammo,vmanip)

@wrap.on_key_always(wrap.K_w)
def goup():
    wrap.sprite.move(player, 0, -5)
    wrap.sprite.set_angle(player, 0)

    x, y = wrap.sprite.get_pos(player)
    wrap.sprite.move_to(a, x, y)


@wrap.on_key_always(wrap.K_s)
def godown():
    wrap.sprite.move(player, 0, 5)
    wrap.sprite.set_angle(player, 180)

    x, y = wrap.sprite.get_pos(player)
    wrap.sprite.move_to(a, x, y)


@wrap.on_key_always(wrap.K_d)
def goright():
    wrap.sprite.move(player, 5, 0)
    wrap.sprite.set_angle(player, 90)

    x, y = wrap.sprite.get_pos(player)
    wrap.sprite.move_to(a, x, y)


@wrap.on_key_always(wrap.K_a)
def goleft():
    wrap.sprite.move(player, -5, 0)
    wrap.sprite.set_angle(player, -90)

    x, y = wrap.sprite.get_pos(player)
    wrap.sprite.move_to(a, x, y)

@wrap.always(1000/50)
def fav():
    wrap.sprite.move_at_angle_dir(ammo,5)

#база
wrap.sprite.add('battle_city_items',600,282,'base')