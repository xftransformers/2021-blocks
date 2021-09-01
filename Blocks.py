"""
    Daniel F.  Blocks.
    Copyright (C) 2021 Daniel F

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You can contact the author and get a copy of the original code from:
    https://github.com/xftransformers

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

"""
	This program is based on and extends 
	the examples from [https://simplegametutorials.github.io/]
"""

import random
import pgzrun
grid_x_count = 10
grid_y_count = 18
timer = 0
piece_x_count = 4
piece_y_count = 4


def can_piece_move(test_x, test_y, test_rotation):
    return True
inert = []
for y in range(grid_y_count):
    inert.append([])
    for x in range(grid_x_count):
        inert[y].append(' ')

piece_structures = [
    [
        [
            [' ', ' ', ' ', ' '],
            ['i', 'i', 'i', 'i'],
            [' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' '],
        ],
        [
            [' ', 'i', ' ', ' '],
            [' ', 'i', ' ', ' '],
            [' ', 'i', ' ', ' '],
            [' ', 'i', ' ', ' '],
        ],
    ],
    [
        [
            [' ', ' ', ' ', ' '],
            [' ', 'o', 'o', ' '],
            [' ', 'o', 'o', ' '],
            [' ', ' ', ' ', ' '],
        ],
    ],
    [
        [
            [' ', ' ', ' ', ' '],
            ['j', 'j', 'j', ' '],
            [' ', ' ', 'j', ' '],
            [' ', ' ', ' ', ' '],
        ],
        [
            [' ', 'j', ' ', ' '],
            [' ', 'j', ' ', ' '],
            ['j', 'j', ' ', ' '],
            [' ', ' ', ' ', ' '],
        ],
        [
            ['j', ' ', ' ', ' '],
            ['j', 'j', 'j', ' '],
            [' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' '],
        ],
        [
            [' ', 'j', 'j', ' '],
            [' ', 'j', ' ', ' '],
            [' ', 'j', ' ', ' '],
            [' ', ' ', ' ', ' '],
        ],
    ],
    [
        [
            [' ', ' ', ' ', ' '],
            ['l', 'l', 'l', ' '],
            ['l', ' ', ' ', ' '],
            [' ', ' ', ' ', ' '],
        ],
        [
            [' ', 'l', ' ', ' '],
            [' ', 'l', ' ', ' '],
            [' ', 'l', 'l', ' '],
            [' ', ' ', ' ', ' '],
        ],
        [
            [' ', ' ', 'l', ' '],
            ['l', 'l', 'l', ' '],
            [' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' '],
        ],
        [
            ['l', 'l', ' ', ' '],
            [' ', 'l', ' ', ' '],
            [' ', 'l', ' ', ' '],
            [' ', ' ', ' ', ' '],
        ],
    ],
    [
        [
            [' ', ' ', ' ', ' '],
            ['t', 't', 't', ' '],
            [' ', 't', ' ', ' '],
            [' ', ' ', ' ', ' '],
        ],
        [
            [' ', 't', ' ', ' '],
            [' ', 't', 't', ' '],
            [' ', 't', ' ', ' '],
            [' ', ' ', ' ', ' '],
        ],
        [
            [' ', 't', ' ', ' '],
            ['t', 't', 't', ' '],
            [' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' '],
        ],
        [
            [' ', 't', ' ', ' '],
            ['t', 't', ' ', ' '],
            [' ', 't', ' ', ' '],
            [' ', ' ', ' ', ' '],
        ],
    ],
    [
        [
            [' ', ' ', ' ', ' '],
            [' ', 's', 's', ' '],
            ['s', 's', ' ', ' '],
            [' ', ' ', ' ', ' '],
        ],
        [
            ['s', ' ', ' ', ' '],
            ['s', 's', ' ', ' '],
            [' ', 's', ' ', ' '],
            [' ', ' ', ' ', ' '],
        ],
    ],
    [
        [
            [' ', ' ', ' ', ' '],
            ['z', 'z', ' ', ' '],
            [' ', 'z', 'z', ' '],
            [' ', ' ', ' ', ' '],
        ],
        [
            [' ', 'z', ' ', ' '],
            ['z', 'z', ' ', ' '],
            ['z', ' ', ' ', ' '],
            [' ', ' ', ' ', ' '],
        ],
    ],
    [
        [
            ['h', 'h', ' ', ' '],
            ['h', 'h', ' ', ' '],
            ['h', 'h', ' ', ' '],
            [' ', ' ', ' ', ' '],
        ],
        [
            [' ', ' ', ' ', ' '],
            ['h', 'h', 'h', ' '],
            ['h', 'h', 'h', ' '],
            [' ', ' ', ' ', ' '],
        ],
    ],
    [
        [
            ['r', 'r', 'r', 'r'],
            ['r', 'r', 'r', 'r'],
            ['r', 'r', ' ', ' '],
            ['r', 'r', ' ', ' '],
        ],
        [
            ['r', 'r', 'r', 'r'],
            ['r', 'r', 'r', 'r'],
            [' ', ' ', 'r', 'r'],
            [' ', ' ', 'r', 'r'],
        ],
        [
            [' ', ' ', 'r', 'r'],
            [' ', ' ', 'r', 'r'],
            ['r', 'r', 'r', 'r'],
            ['r', 'r', 'r', 'r'],
        ],
        [
            ['r', 'r', ' ', ' '],
            ['r', 'r', ' ', ' '],
            ['r', 'r', 'r', 'r'],
            ['r', 'r', 'r', 'r'],
        ],
    ],
]

def new_sequence():
    global sequence

    sequence = list(range(len(piece_structures)))
    random.shuffle(sequence)

new_sequence()

def new_piece():
    global piece_x
    global piece_y
    global piece_type
    global piece_rotation

    piece_x = 3
    piece_y = 0
    piece_type = sequence.pop()
    if len(sequence) == 0:
        new_sequence()
    piece_rotation = 0

new_piece()


def reset():
    global inert
    global timer

    inert = []
    for y in range(grid_y_count):
        inert.append([])
        for x in range(grid_x_count):
            inert[y].append(' ')

    timer = 0
    new_sequence()
    new_piece()

reset()

def can_piece_move(test_x, test_y, test_rotation):
    for y in range(piece_y_count):
        for x in range(piece_x_count):
            if (
                piece_structures[piece_type][test_rotation][y][x] != ' ' and (
                    (test_x + x) < 0
                    or (test_x + x) >= grid_x_count
                    or (test_y + y) >= grid_y_count
                    or inert[test_y +y][test_x + x] != ' '
                )
            ):
                return False

    return True

def on_key_down(key):
    global piece_rotation
    global piece_type
    global piece_x
    global piece_y

    if key == keys.X:
        test_rotation = piece_rotation + 1
        if test_rotation > len(piece_structures[piece_type]) - 1:
            test_rotation = 0

        if can_piece_move(piece_x, piece_y, test_rotation):
            piece_rotation = test_rotation

    elif key == keys.Z:
        test_rotation = piece_rotation - 1
        if test_rotation < 0:
            test_rotation = len(piece_structures[piece_type]) - 1

        if can_piece_move(piece_x, piece_y, test_rotation):
            piece_rotation = test_rotation

    elif key == keys.C:
        while can_piece_move(piece_x, piece_y + 1, piece_rotation):
            piece_y += 1
            timer = timer_limit

    elif key == keys.LEFT:
        test_x = piece_x - 1

        if can_piece_move(test_x, piece_y, piece_rotation):
            piece_x = test_x

    elif key == keys.RIGHT:
        test_x = piece_x + 1

        if can_piece_move(test_x, piece_y, piece_rotation):
            piece_x = test_x

timer_limit = 0.5

def update(dt):
    global timer
    global piece_y

    timer += dt
    if timer >= timer_limit:
        timer = 0

        test_y = piece_y + 1
        if can_piece_move(piece_x, test_y, piece_rotation):
            piece_y = test_y
        else:
            for y in range(piece_y_count):
                for x in range(piece_x_count):
                    block = piece_structures[piece_type][piece_rotation][y][x]
                    if block != ' ':
                        inert[piece_y + y][piece_x + x] = block

            for y in range(grid_y_count):
                complete = True
                for x in range(grid_x_count):
                    if inert[y][x] == ' ':
                        complete = False
                        break

                if complete:
                    for ry in range(y, 1, -1):
                        for rx in range(grid_x_count):
                            inert[ry][rx] = inert[ry - 1][rx]

                    for rx in range(grid_x_count):
                        inert[0][rx] = ' '

            new_piece()

            if not can_piece_move(piece_x, piece_y, piece_rotation):
                reset()

def draw():
    screen.fill((255, 255, 255))

    def draw_block(block, x, y):
        colors = {
            ' ': (222, 222, 222),
            'i': (120, 195, 239),
            'j': (236, 231, 108),
            'l': (124, 218, 193),
            'o': (234, 177, 121),
            's': (211, 136, 236),
            't': (248, 147, 196),
            'z': (169, 221, 118),
            'h': (0, 0, 0),
            'r': (64, 224, 208),
            'preview': (190, 190, 190),
        }
        color = colors[block]

        block_size = 20
        block_draw_size = block_size - 1
        screen.draw.filled_rect(
            Rect(
                x * block_size, y * block_size,
                block_draw_size, block_draw_size
            ),
            color=color
        )

    offset_x = 2
    offset_y = 5

    for y in range(grid_y_count):
        for x in range(grid_x_count):
            draw_block(inert[y][x], x + offset_x, y + offset_y)

    for y in range(piece_y_count):
        for x in range(piece_x_count):
            block = piece_structures[piece_type][piece_rotation][y][x]
            if block != ' ':
                draw_block(
                    block,
                    x + piece_x + offset_x,
                    y + piece_y + offset_y
                )


    for y in range(piece_y_count):
        for x in range(piece_x_count):
            block = piece_structures[sequence[-1]][0][y][x]
            if block != ' ':
                draw_block('preview', x + 5, y + 1)

pgzrun.go()