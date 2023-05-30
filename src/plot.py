import matplotlib.pyplot as plt
import isd_functions, service

plt.rcParams.update({'font.size': 14})

def plot_gv_distance(n):
    x = []
    y = []
    for i in range(2, n, 2):
        k = int(i/2)
        gv = isd_functions.gilbert_varshamov_distance(i,k)
        print(gv)
        max_err = int((gv-1)/2)
        x.append(i)
        y.append(max_err)
    plt.plot(x,y)
    plt.xlabel('n')
    plt.ylabel('pocet chyb')
    plt.show()

pokusy = [1.98, 3.86, 8.52, 
          2.2, 7.18, 33.02, 
          1.94, 27.28, 471, 
          1.88, 69.08, 898.5]

n_w = ['50 (1)', '50 (2)','50 (2)',
       '100 (1)','100 (3)', '100 (5)',
       '150 (1)','150 (5)','150 (8)',
       '200 (1)','200 (6)','200 (11)',]

ocakavane_pokusy = [2,4.08, 8.52,
                    2,8.25,35.53,
                    2,34.28,311.6,
                    2,69.13,2738.05]

casy = [0.01, 0.017, 0.03,
        0.03, 0.095, 0.41,
        0.06, 0.795, 15.49,
        0.115, 3.857, 51.307]


plt.plot(n_w, pokusy)
plt.plot(n_w, ocakavane_pokusy)
# plt.plot(n_w, casy)
plt.xlabel('n (w)')
plt.ylabel('pokusy')
plt.show()