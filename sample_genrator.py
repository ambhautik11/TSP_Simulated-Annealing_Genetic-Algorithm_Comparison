import random as rand;

fl = open("input","w")
for i in range(0,20):
    fl.write(str(rand.randint(0,100)) + " " + str(rand.randint(0,100))+"\n");
fl.close();
