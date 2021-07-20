import retro
import numpy as np
import cv2 
import neat
import pickle
from datetime import datetime
import time

env = retro.make('SuperMarioWorld-Snes', 'YoshiIsland2.state')
imageArray = []

cv2.namedWindow('ResizeRGB', cv2.WINDOW_NORMAL)
cv2.namedWindow('ResizeGrayScale', cv2.WINDOW_NORMAL)


def eval_genomes(genomes, config):

    for genome_id, genome in genomes:
        obs = env.reset()

        inputY, inputX, numChannels = env.observation_space.shape
        inputX = int(inputX/8)
        inputY = int(inputY/8)

        net = neat.nn.recurrent.RecurrentNetwork.create(genome, config)
        
        fitnessMax = 0
        fitnessCurrent = 0
        frameCounter = 0
        xPos = 0
        xPosMax = 0
        
        done = False

        while not done:
            
            env.render()

            obs = cv2.resize(obs, (inputX, inputY))
            cv2.imshow('ResizeRGB',obs)
            obs = cv2.cvtColor(obs, cv2.COLOR_BGR2GRAY)
            cv2.imshow('ResizeGrayScale',obs)

            imageArray = np.ndarray.flatten(obs)

            nnOutput = net.activate(imageArray)

            obs, rew, done, info = env.step(nnOutput)
                        
            xPos = info['x']

            if xPos > xPosMax:
                xPosMax = xPos
                frameCounter = 0
                fitnessCurrent += 1
            else:
                frameCounter += 1

            if info['endOfLevel']:        
                fitnessCurrent += 10000                 
                done = True

            fitnessCurrent += rew

            if done or frameCounter == 100:
                done = True
                print(genome_id, fitnessCurrent)
              
            genome.fitness = fitnessCurrent
            cv2.waitKey(1)

def main():
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                        neat.DefaultSpeciesSet, neat.DefaultStagnation,
                        'config-feedforward')

    p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    
    start_time = time.time()
    winner = p.run(eval_genomes)
    finish_time = time.time()
    
    with open('winner.pkl', 'wb') as output:
        pickle.dump(winner, output, 1)
    
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()