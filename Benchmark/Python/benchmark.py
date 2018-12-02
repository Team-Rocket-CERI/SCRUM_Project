import time

clk = time.clock()

count = 0
for i in range(0, 10000):
        for j in range(0, 10000):
                count +=1


print time.clock(), "secondes"
