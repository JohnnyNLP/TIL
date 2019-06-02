import os

index = 1;
with open("socialscienceTitle.txt", 'r') as f:
    with open("socialscienceTitle2.txt", 'w') as fi:
        lines = f.readlines();
        for line in lines :
            newline = str(index) + ". " + line;
            fi.write(newline);
            index += 1;
