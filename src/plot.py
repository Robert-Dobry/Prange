import matplotlib.pyplot as plt
import func, service

plt.rcParams.update({'font.size': 16})

def plot_gv_distance(n):

    x = []
    y = []
    for i in range(2, n, 2):
        k = int(i/2)
        gv = func.gilbert_varshamov_distance(i,k)
        max_err = int((gv-1)/2)
        x.append(i)
        y.append(max_err)

    plt.plot(x,y)
    plt.xlabel('n')
    plt.ylabel('pocet chyb')
    plt.show()




# x = ['20 (1)', '40 (1)', '40 (2)', '60 (1)', '60 (2)', '60 (3)', '80(1)', '80 (2)', '80 (3)', '80 (4)']
# y = [0.0018, 0.008, 0.016, 0.26, 0.53, 1.55, 8.04, 9.88, 10.54, 12.22]
# plt.plot(x,y)
# plt.xlabel('n (w)')
# plt.ylabel('priemerny cas (v sek.)')
# plt.show()

#plot_gv_distance(160)

# x = ['60 (1,2)', '90 (1,3)', '90 (1,4)', '90 (2,3)', '120 (1,5)', '120 (1,6)', '120 (2,5)', '150 (1,5)', '150 (1,6)', '150 (1,7)', '150 (2,6)']
# y = [0.072, 0.34, 0.11, 15.87 , 0.32, 1.55, 33.19, 4.7, 0.28, 0.31, 38.46]
# plt.plot(x,y)
# plt.xlabel('n (t)')
# plt.ylabel('priemerny cas dekodovania (v sek.)')
# plt.show()


ns = [20,40,60,80,90,120,150]
gvs = []
err = []
n = 20
for n in ns:
    gv = func.gilbert_varshamov_distance(n,int(n/2))
    gvs.append(gv)
    err.append(int((gv-1)/2))

print(ns)
print(gvs)
print(err)

