import  tspsimul
import tspGenatic
import matplotlib.pyplot as plt

tours_Genatic = tspGenatic.tspgen(10);
tours_Simu =    tspsimul.tspsml(10);

color = ['b', 'orange', 'g', 'r', 'c', 'm', 'y', 'k', 'Brown', 'ForestGreen']

print (len(tours_Genatic));
print (len(tours_Simu));

Dis_Sim = []
Dis_Gen = []
for tour in tours_Simu:

    c = 0;
    x = []
    y = []
    for i in tour:
        x.append(tspsimul.city[i][0])
        y.append(tspsimul.city[i][1])
    plt.title("PLOT FOR Simulated Annealing")
    plt.plot(x,y,color = color[c])
    plt.scatter(x,y,color = color[c])
    plt.xlabel(tspsimul.get_distance(tour))
    plt.show();
    c += 1;
    c %= len(color);



for tour in tours_Genatic:

    c = 0
    x = []
    y = []
    for i in tour:
        x.append(tspGenatic.city[i][0])
        y.append(tspGenatic.city[i][1])
    plt.title("PLOT FOR Genatic Algorithm")
    plt.plot(x,y,color = color[c])
    plt.scatter(x,y,color = color[c])
    plt.xlabel(tspGenatic.get_distance(tour))
    plt.show();
    c += 1;
    c %= len(color);


plt.scatter(range(0,len(tspGenatic.bests)),tspGenatic.bests,color="black")
plt.scatter(range(0,len(tspsimul.bests)),tspsimul.bests,color="red")
plt.show()
