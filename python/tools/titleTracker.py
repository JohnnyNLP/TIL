import os

file_list = os.listdir()

with open("medical.txt", "w") as f:

    for i in file_list:
            f.write(i);
            f.write("\n");

