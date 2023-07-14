from math import exp
import random


class SentenceCorrector(object):
    def __init__(self, cost_fn, conf_matrix):
        self.conf_matrix = conf_matrix
        self.cost_fn = cost_fn

        # You should keep updating following variable with best string so far.
        self.best_state = None  

    import random
from xmlrpc.client import MAXINT


class SentenceCorrector(object):
    def __init__(self, cost_fn, conf_matrix):
        self.conf_matrix = conf_matrix
        self.cost_fn = cost_fn

        # You should keep updating following variable with best string so far.
        self.best_state = None
        self.cost_best_state = MAXINT

    def search(self, start_state):
        confMatrix = {}
        for i in self.conf_matrix:
            for j in self.conf_matrix[i]:
                if(j in confMatrix):
                    confMatrix[j].append(i)
                else:
                    confMatrix[j] = [i]

        self.best_state = start_state
        self.cost_best_state = self.cost_fn(start_state)
        #print(f'Initial cost: {self.cost_best_state}')
        n = len(start_state)
        threshold=15
        while (True):
            thresArr=[]
            prevState=self.best_state
            costPrev = self.cost_best_state
            for i in range(n):
                if self.best_state[i] == ' ':
                    thresArr=[]
                    prevState=self.best_state
                    costPrev = self.cost_best_state
                    continue
                if self.best_state[i] in confMatrix:
                    for j in confMatrix[self.best_state[i]]:
                        new_state = self.best_state[:i] + j + self.best_state[i+1:]
                        cost = self.cost_fn(new_state)
                        # print(new_state + " " + str(cost))
                        if cost-self.cost_best_state < 0:
                            if(costPrev - cost < threshold):
                                thresArr.append((i,j))
                            self.best_state = new_state
                            self.cost_best_state = cost
                            #print(self.best_state + " " + str(self.cost_best_state))
                        else:
                            for x in thresArr:
                                if(i==x[0]):
                                    continue
                                step_state = prevState[:x[0]] + start_state[x[0]] + prevState[x[0]+1:i] + j + prevState[i+1:]
                                step_cost = self.cost_fn(step_state)
                                if(step_cost - self.cost_best_state < 0):
                                    self.best_state = step_state
                                    self.cost_best_state = step_cost
                                    #print(self.best_state + " " + str(self.cost_best_state))
                                    break
                                step_state= prevState[:x[0]] + x[1] + prevState[x[0]+1:i] + j + prevState[i+1:]
                                costStep = self.cost_fn(step_state)
                                # print(step_state + " " + str(costStep))
                                if costStep - self.cost_best_state < 0:
                                    self.best_state = step_state
                                    self.cost_best_state = costStep
                                    #print(self.best_state + " " + str(self.cost_best_state))
                            if(self.cost_fn(prevState) - self.cost_fn(new_state) < threshold):
                                thresArr.append((i,j))
            

                    



