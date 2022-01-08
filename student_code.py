"""
@author AchiyaZigi
OOP - Ex4
Very simple GUI example for python client to communicates with the server and "play the game!"
"""
import math
import os
import time
from collections import OrderedDict
from operator import itemgetter
from types import SimpleNamespace

import json

import crimson as crimson
from pygame import gfxdraw
import pygame
from pygame import *
import subprocess

# init pygame


# run server
from GameAlgo import GameAlgo
from Images import Button, PokemonImages, AgentsImages
from GraphAlgo import GraphAlgo
from PokemonsAndAgents import Agents, Pokemons, AgePok
from client import Client

subprocess.Popen(["powershell.exe", "java -jar Ex4_Server_v0.0.jar 5"])

WIDTH, HEIGHT = 1080, 720

# default port
PORT = 6666
# server host (default localhost 127.0.0.1)
HOST = '127.0.0.1'
pygame.init()

screen = display.set_mode((WIDTH, HEIGHT), depth=32, flags=RESIZABLE)
clock = pygame.time.Clock()
pygame.font.init()

client = Client()
client.start_connection(HOST, PORT)
stop_button = Button()
pokemonsimg = PokemonImages()
agentsimg = AgentsImages()
game = GameAlgo()
agentPath = AgePok()
# Map:
MAP_IMAGE = pygame.image.load(os.path.join('img', 'map.png'))
MAP = pygame.transform.scale(MAP_IMAGE, (screen.get_width(), screen.get_height()))

# Create Graph
graph_json = client.get_graph()
graph = GraphAlgo()
g = graph.graph
graph.load_from_json(graph_json)

FONT = pygame.font.SysFont('Arial', 20, bold=True)

for n in g.nodes.keys():
    x, y, z = g.nodes[n].pos
    g.nodes[n].pos = SimpleNamespace(x=float(x), y=float(y), z=float(z))

# get data proportions
min_x = min(g.nodes.keys(), key=lambda n: g.nodes[n].pos.x)
min_x = g.nodes[min_x].pos.x
min_y = min(g.nodes.keys(), key=lambda n: g.nodes[n].pos.y)
min_y = g.nodes[min_y].pos.y
max_x = max(g.nodes.keys(), key=lambda n: g.nodes[n].pos.x)
max_x = g.nodes[max_x].pos.x
max_y = max(g.nodes.keys(), key=lambda n: g.nodes[n].pos.y)
max_y = g.nodes[max_y].pos.y


def scale(data, min_screen, max_screen, min_data, max_data):
    """
    get the scaled data with proportions min_data, max_data
    relative to min and max screen dimentions
    """
    return ((data - min_data) / (max_data - min_data)) * (max_screen - min_screen) + min_screen


# decorate scale with the correct values
def my_scale(data, x=False, y=False, z=False):
    if x:
        return scale(data, 50, screen.get_width() - 50, min_x, max_x)
    if y:
        return scale(data, 50, screen.get_height() - 50, min_y, max_y)


so2 = game.pokemons(client, g)[0]

radius = 15
s1 = "{\"id\":"
s2 = "}"
for i in range(int(json.loads(client.get_info())["GameServer"]["agents"])):
    if i < len(so2):
        client.add_agent(f"{s1}{so2[i][0][0]}{s2}")
    else:
        client.add_agent(f"{s1}{so2[0][0][0]}{s2}")


# this commnad starts the server - the game is running now
client.start()

"""
The code below should be improved significantly:
The GUI and the "algo" are mixed - refactoring using MVC design pattern is required.
"""
while client.is_running() == 'true':
    screen.blit(pygame.transform.scale(MAP, screen.get_rect().size), (0, 0))

    # Pokemons:
    so, pokemons = game.pokemons(client, g)

    # Agents:
    agents = game.agents(client, my_scale)

    # check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

    # draw nodes
    for n in g.nodes.keys():
        x = my_scale(g.nodes[n].pos.x, x=True)
        y = my_scale(g.nodes[n].pos.y, y=True)
        z = my_scale(g.nodes[n].pos.z, z=True)

        # its just to get a nice antialiased circle
        gfxdraw.filled_circle(screen, int(x), int(y),
                              radius, Color(64, 80, 174))
        gfxdraw.aacircle(screen, int(x), int(y),
                         radius, Color(255, 255, 255))

        # draw the node id
        id_srf = FONT.render(str(g.nodes[n].id), True, Color(255, 255, 255))
        rect = id_srf.get_rect(center=(x, y))
        screen.blit(id_srf, rect)

    # draw edges
    # for v in g.nodes.keys():
    #     # x, y, z = g.nodes[v].pos
    #     for u in g.edges[g.nodes[v].id]:
    #         # scaled positions
    #         src_x = my_scale(g.nodes[v].pos.x, x=True)
    #         src_y = my_scale(g.nodes[v].pos.y, y=True)
    #         dest_x = my_scale(g.nodes[u].pos.x, x=True)
    #         dest_y = my_scale(g.nodes[u].pos.y, y=True)

            # draw the line
            # pygame.draw.line(screen, Color(61, 72, 126),
            #                  (src_x, src_y), (dest_x, dest_y))

    # draw time
    timeleft = float(client.time_to_end()) / 1000
    timelabel = FONT.render(f"Time Left: {int(timeleft)}", True, (0, 0, 0))
    rect = timelabel.get_rect(center=(110, 10))
    screen.blit(timelabel, rect)

    # draw agents
    agentsimg.draw(screen, agents)

    # draw pokemons
    pokemonsimg.draw(screen, pokemons, my_scale)

    if stop_button.draw(screen):
        client.stop()
    # update screen changes
    display.update()

    # refresh rate
    clock.tick(60)

    # choose next edge
    game.run(client, agents, agentPath, graph, so)
    client.move()
    ttl = client.time_to_end()

# game over:
