from numpy import genfromtxt


traj_np = genfromtxt('outputs/traj_race_cl.csv', delimiter=';')

print_str = "optimal_outputs = ["

for line in traj_np:
    for value in line:
        print_str += "{:.7f} ".format(value)
    print_str += ";"

print_str += "]"

text_file = open("outputs/traj_race_cl.txt", "w")
text_file.write(print_str)
text_file.close()