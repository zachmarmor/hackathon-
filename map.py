# création de la map 
import numpy as np 
import random as rd 


GRID_SIZE = 30
INITIAL_SHEEP = 50
INITIAL_WOLVES = 10
INITIAL_GRASS_COVERAGE

def create_map( GRID_SIZE, INITIAL_SHEEP, INITIAL_WOLVES, INITIAL_GRASS_COVERAGE):
    map = np.zeros((GRID_SIZE, GRID_SIZE)) 
    # Initialiser la couverture d'herbe
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE): 
            r_grass = rd.random() 
            r_sheep = rd.random()
            r_wolf = rd.random()
            if r_grass < INITIAL_GRASS_COVERAGE:
                map[i][j] = (Grass(), Animal())
            elif r_sheep < INITIAL_SHEEP / (GRID_SIZE * GRID_SIZE):
                map[i][j] = (Grass(), Sheep())
            elif r_wolf < INITIAL_WOLVES / (GRID_SIZE * GRID_SIZE):
                map[i][j] = (Grass(), Wolf())
            

