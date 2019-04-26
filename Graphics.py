import matplotlib.pyplot as plt

X = []
Y = []
Z = []

filename = ["GeneralRank-All-MonthlyRank.txt", "OriginalRank-All-MonthlyRank.txt", "RookieRank-All-MonthlyRank.txt"]
with open(filename[0], 'r') as f:
    lines =f.readlines()
    for line in lines:
        a = line.split('：')
        if a[0] == 'Views':
            X.append(a[1].replace('\n',''))
X = list(map(int,X))
print(X)

with open(filename[1], 'r') as f:
    lines =f.readlines()
    for line in lines:
        a = line.split('：')
        if a[0] == 'Views':
            Y.append(a[1].replace('\n',''))
Y = list(map(int,Y))
print(Y)

with open(filename[2], 'r') as f:
    lines =f.readlines()
    for line in lines:
        a = line.split('：')
        if a[0] == 'Views':
            Z.append(a[1].replace('\n',''))
Z = list(map(int,Z))
print(Z)

plt.figure()
plt.subplot(3,1,1)
plt.title("Score/Rank Plot"+"\n"+"General")
plt.ylim([100,9000000])
fig1 = plt.bar(range(len(X)), X, fc="r")
plt.subplot(3,1,2)
plt.title("Original")
plt.ylim([100,9000000])
fig2 = plt.bar(range(len(Y)), Y, fc="g")
plt.subplot(3,1,3)
plt.title("Rookie")
plt.ylim([100,9000000])
fig3 = plt.bar(range(len(Z)), Z, fc="b")


plt.show()