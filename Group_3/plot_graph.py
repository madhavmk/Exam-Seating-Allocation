import matplotlib.pyplot as plt

max_fitness_array=[]
max_fitness_count=0
generation_array=[]
with open("out.txt") as out_file:
    for line in out_file.readlines():
        if line[0:16:]=="max fitness >>  ":
            print(line[16::])
            max_fitness_array.append(float(line[16:-1:]))
            max_fitness_count+=1
print(max_fitness_array)
print(max_fitness_count)
for i in range(max_fitness_count):
    generation_array.append(i+1)


plt.plot(generation_array,max_fitness_array)
plt.ylabel("Max Fitness v/s Generations")

for x,y in zip(generation_array[::100],max_fitness_array[::100]):
    label = "{:.3f}".format(y)

    plt.annotate(label, # this is the text
                (x,y), # this is the point to label
                textcoords="offset points", # how to position the text
                xytext=(0,10), # distance from text to points (x,y)
                ha='center') # horizontal alignment can be left, right or center

plt.show()