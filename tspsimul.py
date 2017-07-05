import random as rand
import matplotlib.pyplot as plt;
import math
import threading
n = 20;
coolingrate = 0.001;
tempratue = 1000000;
city = []
bests = []


# count = 0;


# print(city[i])


def get_distance(tour):
    dis = 0;
    # print ("int dis ",tour)
    for i in range(1, n):
        x1 = city[tour[i]][0];
        y1 = city[tour[i]][1];
        x2 = city[tour[i - 1]][0];
        y2 = city[tour[i - 1]][1];
        dis += ((x1 - x2) ** 2 + (y2 - y1) ** 2) ** 0.5;
    return dis;


def acceptanceProbability(energy, newenergy, temp):
    if (energy > newenergy):
        return 1.0

    return math.exp((energy - newenergy) / temp)


def SimulatedAnnealing():
    ini_tour = [i for i in range(0, n)]
    best_tour = ini_tour[:];
    pre_tour = ini_tour[:];
    temp = tempratue
    count = 0
    while temp > 1:
        # global count
        # print(count)
        count += 1
        # print (get_distance(pre_tour));
        new_tour = pre_tour[:];
        p1 = int(rand.random() * n);
        p2 = int(rand.random() * n);
        # print(pre_tour);
        # print (p1,p2)
        new_tour[p1], new_tour[p2] = new_tour[p2], new_tour[p1];

        currentEngery = get_distance(pre_tour);
        neighbourEngery = get_distance(new_tour);

        if acceptanceProbability(currentEngery, neighbourEngery, temp) > rand.random():
            pre_tour = new_tour[:]

        if (get_distance(pre_tour) < get_distance(best_tour)):
            best_tour = pre_tour[:];
        temp *= 1 - coolingrate
    # color = ['b', 'orange', 'g', 'r', 'c', 'm', 'y', 'k', 'Brown', 'ForestGreen']
    # cc = 0;
    # X = [];
    # Y = [];
    # for i in best_tour:
    # 	X.append(city[i][0]);
    # 	Y.append(city[i][1]);
    # plt.plot(X,Y,color = color[cc]);
    # plt.scatter(X,Y,color = color[cc]);
    # plt.xlabel(get_distance(best_tour))
    # cc+=1;
    print(best_tour, get_distance(best_tour))
    print("SimulatedAnnealing __ Iteration : " + str(count))
    print(threading.current_thread())
    return best_tour;





def tspsml(sample):
    fb = open("input", "r")

    for i in range(0, n):
        x, y = fb.readline().split(" ")
        city.append([int(x), int(y)])
    fb.close();
    color = ['b', 'orange', 'g', 'r', 'c', 'm', 'y', 'k', 'Brown', 'ForestGreen']
    cc = 0;
    result = []
    while (cc < sample):
        cc += 1;

        X = [];
        Y = [];
        best_tour = SimulatedAnnealing();
        result.append(best_tour)
        bests.append(get_distance(best_tour));

        # for i in best_tour:
        #     X.append(city[i][0]);
        #     Y.append(city[i][1]);
        # plt.plot(X, Y, color=color[cc]);
        # plt.scatter(X, Y, color=color[cc]);
        # plt.xlabel(get_distance(best_tour))
        # plt.show()
    # plt.scatter(range(1, len(bests) + 1), bests);

    return  result;
# tspsml(1);