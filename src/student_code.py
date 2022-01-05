"""
@author AchiyaZigi
OOP - Ex4
Very simple GUI example for python client to communicates with the server and "play the game!"
"""
import math
import os
from types import SimpleNamespace
from client import Client
import json
from pygame import gfxdraw
import pygame
from pygame import *


# init pygame
from GraphAlgo import GraphAlgo
from PokemonsAndAgents import Pokemons, Agents



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
# Coope:
# COOPER_IMAGE = pygame.image.load(
#     os.path.join('data', 'Cooper.png'))
# COOPER = pygame.transform.scale(
#     COOPER_IMAGE, (50, 50))
# Pikachu:
Pikachu_IMAGE = pygame.image.load(os.path.join('data', 'Pikachu.png'))
Pikachu = pygame.transform.scale(Pikachu_IMAGE, (50, 50))
# Charizard:
Charizard_IMAGE = pygame.image.load(os.path.join('data', 'Charizard.png'))
Charizard = pygame.transform.scale(Charizard_IMAGE, (50, 50))
# Jigglypuff:
Jigglypuff_IMAGE = pygame.image.load(os.path.join('data', 'Jigglypuff.png'))
Jigglypuff = pygame.transform.scale(Jigglypuff_IMAGE, (50, 50))
# Bulbasaur:
Bulbasaur_IMAGE = pygame.image.load(os.path.join('data', 'Bulbasaur.png'))
Bulbasaur = pygame.transform.scale(Bulbasaur_IMAGE, (50, 50))
# Squirtle:
Squirtle_IMAGE = pygame.image.load(os.path.join('data', 'Squirtle.png'))
Squirtle = pygame.transform.scale(Squirtle_IMAGE, (50, 50))
# Venusaur:
Venusaur_IMAGE = pygame.image.load(os.path.join('data', 'Venusaur.png'))
Venusaur = pygame.transform.scale(Venusaur_IMAGE, (50, 50))
# Typhlosion:
Typhlosion_IMAGE = pygame.image.load(os.path.join('data', 'Typhlosion.png'))
Typhlosion = pygame.transform.scale(Typhlosion_IMAGE, (50, 50))
# Zapdos:
Zapdos_IMAGE = pygame.image.load(os.path.join('data', 'Zapdos.png'))
Zapdos = pygame.transform.scale(Zapdos_IMAGE, (50, 50))
# Totodile:
Totodile_IMAGE = pygame.image.load(os.path.join('data', 'Totodile.png'))
Totodile = pygame.transform.scale(Totodile_IMAGE, (50, 50))
# Pyroar:
Pyroar_IMAGE = pygame.image.load(os.path.join('data', 'Pyroar.png'))
Pyroar = pygame.transform.scale(Pyroar_IMAGE, (50, 50))
# Eevee:
Eevee_IMAGE = pygame.image.load(os.path.join('data', 'Eevee.png'))
Eevee = pygame.transform.scale(Eevee_IMAGE, (50, 50))

# Map:
MAP_IMAGE = pygame.image.load(os.path.join('data', 'map.png'))
MAP = pygame.transform.scale(MAP_IMAGE, (screen.get_width(), screen.get_height()))

ME_IMAGE = pygame.image.load(
    os.path.join('data', 'ME.png'))
ME = pygame.transform.scale(
    ME_IMAGE, (50, 60))

graph_json = client.get_graph()

FONT = pygame.font.SysFont('Arial', 20, bold=True)
# load the json string into SimpleNamespace Object

string = json.loads(
    graph_json, object_hook=lambda json_dict: SimpleNamespace(**json_dict))
graph = GraphAlgo()
g = graph.graph
graph.load_from_json(graph_json)

for n in g.nodes.keys():
    x, y, z = g.nodes[n].pos
    g.nodes[n].pos = SimpleNamespace(x=float(x), y=float(y), z=float(z))

# get data proportions
min_x = min(g.nodes.keys(), key=lambda n: g.nodes[n].pos.x)
min_x = g.nodes[min_x].pos.x
min_y = min(g.nodes.keys(), key=lambda n: g.nodes[n].pos.y)
min_y = g.nodes[min_y].pos.y
min_z = min(g.nodes.keys(), key=lambda n: g.nodes[n].pos.z)
min_z = g.nodes[min_z].pos.z
max_x = max(g.nodes.keys(), key=lambda n: g.nodes[n].pos.x)
max_x = g.nodes[max_x].pos.x
max_y = max(g.nodes.keys(), key=lambda n: g.nodes[n].pos.y)
max_y = g.nodes[max_y].pos.y
max_z = max(g.nodes.keys(), key=lambda n: g.nodes[n].pos.z)
max_z = g.nodes[max_z].pos.z


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
    # if z:
    #     return scale(data, 50, screen.get_height() - 50, min_z, max_z)


radius = 15

client.add_agent("{\"id\":0}")


# client.add_agent("{\"id\":1}")
# client.add_agent("{\"id\":2}")
# client.add_agent("{\"id\":3}")

# this commnad starts the server - the game is running now
# calculate edges:



client.start()

"""
The code below should be improved significantly:
The GUI and the "algo" are mixed - refactoring using MVC design pattern is required.
"""

while client.is_running() == 'true':
    # screen.blit(MAP, (0, 0))
    screen.blit(pygame.transform.scale(MAP, screen.get_rect().size), (0, 0))
    # Pokemons:
    pokemons = []
    pokemonss = client.get_pokemons()
    pokemonsss = json.loads(pokemonss)
    for p in pokemonsss["Pokemons"]:
        po = Pokemons(p["Pokemon"])
        x, y, z = po.pos[0], po.pos[1], po.pos[2]
        # po.pos = SimpleNamespace(x=my_scale(float(x), x=True),
        #                          y=my_scale(float(y), y=True, z=my_scale(float(z), z=True)))
        po.cal_edges(g)
        pokemons.append(po)
    print(pokemons)
    pokemons.sort(key=lambda a: a.value, reverse=True)  # sort by value


    # Agents:
    agents = []
    agentss = client.get_agents()
    age = json.loads(agentss)
    for a in age["Agents"]:
        agen = Agents(a["Agent"])
        x, y, z = agen.pos[0], agen.pos[1], agen.pos[2]
        agen.pos = SimpleNamespace(x=my_scale(float(x), x=True),
                                   y=my_scale(float(y), y=True, z=my_scale(float(z), z=True)))
        agents.append(agen)
    agents.sort(key=lambda a: a.speed, reverse=True)  # sort by speed
    # check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

    # refresh surface
    # screen.fill(Color(0, 0, 0))

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
    for v in g.nodes.keys():
        # x, y, z = g.nodes[v].pos
        for u in g.edges[g.nodes[v].id]:
            # scaled positions
            src_x = my_scale(g.nodes[v].pos.x, x=True)
            src_y = my_scale(g.nodes[v].pos.y, y=True)
            dest_x = my_scale(g.nodes[u].pos.x, x=True)
            dest_y = my_scale(g.nodes[u].pos.y, y=True)

            # draw the line
            pygame.draw.line(screen, Color(61, 72, 126),
                             (src_x, src_y), (dest_x, dest_y))

    # draw agents
    for agent in agents:
        screen.blit(ME, (int(agent.pos.x), int(agent.pos.y)))
    # draw pokemons (note: should differ (GUI wise) between the up and the down pokemons (currently they are marked in the same way).
    for p in pokemons:
        if p.value == 5:
            screen.blit(Squirtle, (int(my_scale(float(p.pos[0]), x=True)), int(my_scale(float(p.pos[1]), y=True))))
        elif p.value == 6:
            screen.blit(Bulbasaur, (int(my_scale(float(p.pos[0]), x=True)), int(my_scale(float(p.pos[1]), y=True))))
        elif p.value == 7:
            screen.blit(Jigglypuff, (int(my_scale(float(p.pos[0]), x=True)), int(my_scale(float(p.pos[1]), y=True))))
        elif p.value == 8:
            screen.blit(Eevee, (int(my_scale(float(p.pos[0]), x=True)), int(my_scale(float(p.pos[1]), y=True))))
        elif p.value == 9:
            screen.blit(Zapdos, (int(my_scale(float(p.pos[0]), x=True)), int(my_scale(float(p.pos[1]), y=True))))
        elif p.value == 10:
            screen.blit(Totodile, (int(my_scale(float(p.pos[0]), x=True)), int(my_scale(float(p.pos[1]), y=True))))
        elif p.value == 11:
            screen.blit(Typhlosion, (int(my_scale(float(p.pos[0]), x=True)), int(my_scale(float(p.pos[1]), y=True))))
        elif p.value == 12:
            screen.blit(Venusaur, (int(my_scale(float(p.pos[0]), x=True)), int(my_scale(float(p.pos[1]), y=True))))
        elif p.value == 13:
            screen.blit(Charizard, (int(my_scale(float(p.pos[0]), x=True)), int(my_scale(float(p.pos[1]), y=True))))
        elif p.value == 14:
            screen.blit(Pyroar, (int(my_scale(float(p.pos[0]), x=True)), int(my_scale(float(p.pos[1]), y=True))))
        elif p.value >= 15:
            screen.blit(Pikachu, (int(my_scale(float(p.pos[0]), x=True)), int(my_scale(float(p.pos[1]), y=True))))

    # update screen changes
    display.update()

    # refresh rate
    clock.tick(60)

    # choose next edge

    for p in pokemons:
        if p.src is None:
            continue
        a = graph.choose_agent(agents, p)
        agent = a[0]
        l = a[1]
        l.append(p.dest)
        next_node = l[1]
        print(l)
        client.choose_next_edge(
            '{"agent_id":' + str(agent.id) + ', "next_node_id":' + str(next_node) + '}')
        ttl = client.time_to_end()

    client.move()
# game over:
