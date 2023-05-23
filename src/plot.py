import matplotlib.pyplot as plt
import func, service


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


plot_gv_distance(100)