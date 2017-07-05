import random as rand
import threading
import matplotlib.pyplot as plt;
# import tspsimul
n = 20;
pop_size = 50;
mutation_prob = 0.05;
best_count_limit = 1000
city = []
population = [];
# count = 0
bests = []


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


# print (population)

def rollate_wheel(fit):
    prob = fit[0][0];
    p = rand.random()
    # print(p)

    for i in range(0, pop_size):
        if p < prob:
            # print (fit[i][1])
            return fit[i][1];
        prob += fit[i + 1][0]
        # print("prob " + str(prob))


def cross_over(pi1, pi2):
    p1 = population[pi1][:]
    p2 = population[pi2][:]

    st = int(rand.random() * n);
    ed = int(rand.random() * n);
    s = set()
    if (st > ed):
        t = st;
        st = ed;
        ed = t;

    c1 = [-1 for i in range(0, n)];
    for i in range(st, ed + 1):
        c1[i] = p1[i];
        s.add(p1[i]);
    j = 0;
    for i in p2:

        if j == st:
            j = ed + 1;

        if i not in s:
            c1[j] = i
            j += 1;

    # print(st,ed)
    # print ("c1 == " ,c1)
    # print ("p1 == " ,p1)
    # print ("p2 == " ,p2)

    st = int(rand.random() * n);
    ed = int(rand.random() * n);

    s.clear()
    if (st > ed):
        t = st;
        st = ed;
        ed = t;

    c2 = [-1 for i in range(0, n)];
    for i in range(st, ed + 1):
        c2[i] = p2[i];
        s.add(p2[i]);
    j = 0;

    for i in p1:

        if j == st:
            j = ed + 1;

        if i not in s:
            c2[j] = i
            j += 1;

    return [c1, c2]


def mutation(new_pop):
    for i in range(0, pop_size - 1):
        r = rand.random()
        if (r < mutation_prob):
            m1 = rand.random() * n;
            m2 = rand.random() * n;
            while m1 == m2:
                m1 = rand.random() * n;
            m1 = int(m1);
            m2 = int(m2);
            t = new_pop[i][m1];
            new_pop[i][m1] = new_pop[i][m2];
            new_pop[i][m2] = t;


def generate_new_population(fit):
    parent = []
    new_pop = []
    for i in range(0, pop_size):
        parent.append(rollate_wheel(fit))
    # print ("ppp" , parent);
    new_pop = population[:][:]
    for i in range(0, pop_size, 2):
        new_pop[parent[i]], new_pop[parent[i + 1]] = cross_over(parent[i], parent[i + 1])

    new_pop[int(rand.random() * pop_size)] = population[fit[pop_size - 1][1]][:];
    # for i in new_pop:
    #	print (i)
    # print();

    mutation(new_pop);
    return new_pop;




def Run_Genatic():
    ini_tour = [i for i in range(0, n)]
    global population;
    population = [];
    for i in range(0, pop_size):
        rand.shuffle(ini_tour)
        rand.shuffle(ini_tour)
        rand.shuffle(ini_tour)
        population.append(ini_tour[:])

    count = 0;
    pre_fit = -121121;
    e = 0.001;
    fit = [];
    best = 1000000000000000000;
    best_tour = []
    best_count = 0;
    while best_count < best_count_limit:
        # print(count)
        # global  count
        count += 1
        fit = [];
        total_fit = 0;
        for i in range(0, pop_size):
            dis = get_distance(population[i][:])
            fit.append([dis, i])
            total_fit += dis;
        # print(get_distance(population[i][:]));
        fit.sort(reverse=True);
        if best > fit[pop_size - 1][0]:
            best = fit[pop_size - 1][0];
            best_count = 0;
            best_tour = population[fit[pop_size - 1][1]][:];
        else:
            best_count += 1

        # print (total_fit/pop_size , pre_fit , fit[pop_size-1][0])
        if (abs(pre_fit - total_fit / pop_size) < e):
            break;

        pre_fit = total_fit / pop_size;

        for i in range(0, pop_size):
            fit[i][0] = fit[i][0] / total_fit;
        # print(fit[i])

        population = generate_new_population(fit)

    print(best_tour, best)
    print("Genatic __ Iteration : " + str(count))
    print(threading.current_thread())
    return best_tour;

def tspgen(sample):

    fl = open("input", "r")
    for i in range(0, n):
        x, y = fl.readline().split(" ")
        city.append([int(x), int(y)])
    fl.close();
    result = []
    for i in range(0, sample):
        t = Run_Genatic();
        bests.append(get_distance(t))
        result.append(t);

    # color = ['b', 'orange', 'g', 'r', 'c', 'm', 'y', 'k', 'Brown', 'ForestGreen']
    cc = 0;
    for best_tour in result:
        X = [];
        Y = [];
        # bests.append(get_distance(best_tour))
        # for i in best_tour:
        #     X.append(city[i][0]);
        #     Y.append(city[i][1]);
        # plt.plot(X, Y, color=color[cc]);
        # plt.scatter(X, Y, color=color[cc]);
        # plt.xlabel(get_distance(best_tour))
        cc += 1;
        # plt.show()
    # plt.scatter(range(1, len(bests) + 1), bests);

    # plt.show();
    return result
# print(city[i])

# tspgen(1)