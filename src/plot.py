import matplotlib.pyplot as plt
import isdfunctions, service

plt.rcParams.update({'font.size': 14})

def plot_gv_distance(n):
    x = []
    y = []
    for i in range(2, n, 2):
        k = int(i/2)
        gv = isdfunctions.gilbert_varshamov_distance(i,k)
        print(gv)
        max_err = int((gv-1)/2)
        x.append(i)
        y.append(max_err)
    plt.plot(x,y)
    plt.xlabel('n')
    plt.ylabel('pocet chyb')
    plt.show()


# plain isd data
pokusy_plain = [

    1.98,
    3.86,
    8.52, 

    2.2, 
    7.18, 
    33.02, 

    1.94, 
    27.28, 
    293.03, 

    1.88, 
    69.08
    ]

n_w = ['50 (1)', 
       '50 (2)',
       '50 (2)',

       '100 (1)',
       '100 (3)', 
       '100 (5)',

       '150 (1)',
       '150 (5)',
       '150 (8)',

       '200 (1)',
       '200 (6)']

ocakavane_pokusy_plain = [
        2,
        4.08, 
        8.52,
                          
        2,
        8.25,
        35.53,

        2,
        34.28,
        311.6,

        2,
        69.13
        ]


casy_plain = [
        0.01, 
        0.017, 
        0.03,

        0.03, 
        0.095, 
        0.41,

        0.06, 
        0.795, 
        10.069,

        0.116, 
        3.857
        ]


# hints isd data
pokusy_hints = [
    6.8,

    6.82, 
    13.58, 
    28.3, 

    24.08,
    92.5,
    242.25,

    # 285.2,
    # 635.2,
    # 1503.36, 
    # 2113.6 
]

ocakavane_pokusy_hints = [
    6.89,

    6.82, 
    12.59,
    31.12,

    21.24, 
    100.64,
    231.91

    # 210,
    # 765.3,
    # 1715, 
    # 2533.9
 ]

casy_hints = [
    0.023,

    0.108,
    0.116,
    0.336,

    0.406,
    1.989,
    6.930

    # 9.703,
    # 26.445,
    # 73.678,
    # 127.963
]

n_t = [

       '50 (1,2)', 
       
       '100 (1,2)',
       ' 50 (1,4)',  
       '100 (2,3)',

       '150 (1,7)', 
       '150 (2,6)',  
       '150 (3,5)'

    #   '200 (2,9)', 
    #   '200 (3,8)',  
    #   '200 (3,7)',  
    #   '200 (5,6)' 
    ]


# plt.plot(n_t, pokusy_hints)
# plt.plot(n_t, ocakavane_pokusy_hints)
# #plt.plot(n_t, casy_hints)
# plt.xlabel('n t')
# plt.ylabel('pocet pokusov')
# plt.show()

# plt.plot(n_w, pokusy_plain)
# plt.plot(n_w, ocakavane_pokusy_plain)
#plt.plot(n_w, casy_plain)
# plt.xlabel('n (w)')
# plt.ylabel('pocet pokusov')
# plt.show()
