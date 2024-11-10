import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
#matplotlib tk

fig = plt.figure()
size = 50 # lattice size
jex =  100 # exchange energy (AFM -> negative, FM -> positive)
te = 150 # temperature
rand = np.random.randint(2,size = (size, size))
rand = rand * 2 - 1
np.save('test.npy', rand)

def ising(dat):
    s = dat
    
    for i in np.arange(size):
        for j in np.arange(size):
            ip = i + 1 if i != size - 1 else 0
            im = i - 1 if i != 0 else size - 1
            jp = j + 1 if j != size - 1 else 0
            jm = j - 1 if j != 0 else size - 1
            
            cal = s[i][j] * (s[i][jp] + s[i][jm] + s[ip][j] + s[im][j])
            den = cal * 2
            p_flip= np.exp(-1 * (den * jex) / te)
            
            p = p_flip / (1 + p_flip)
            
            s[i][j] = s[i][j] if np.random.rand(1) > p else s[i][j] * -1
            # print(i, j)

    a = s 
    return a

def plot(i):
    plt.cla()                     
    dat = np.load('test.npy') # input
    dat = ising(dat)
    np.save('test.npy', dat) # output
    im = plt.imshow(dat, vmin=-1, vmax=1, cmap='gray') 
    plt.title(f'Ising model simulator ($T$ = {te} K, $J$ = {jex} K)\n Monte Calro step = ' + str(i))

## just for seeing 
ani = animation.FuncAnimation(fig, plot, interval = 50)
plt.show()

## for saving as gif file
# ani = animation.FuncAnimation(fig, plot, interval=100, frames=500)
# ani.save("output.gif", writer="imagemagick")

def ising2(dat):
    s = dat
    
    for k in range(size ** 2):
        ran = np.random.randint(size, size = (1, 2))
        i = ran[0][0]
        j = ran[0][1]
        ip = i + 1 if i != size - 1 else 0
        im = i - 1 if i != 0 else size - 1
        jp = j + 1 if j != size - 1 else 0
        jm = j - 1 if j != 0 else size - 1

        cal = s[i][j] * (s[i][jp] + s[i][jm] + s[ip][j] + s[im][j])
        den = cal * 2
        p_flip= np.exp(-1 * (den * jex) / te)

        p = p_flip / (1 + p_flip)

        s[i][j] = s[i][j] if np.random.rand(1) > p else s[i][j] * -1


    a = s 
    return a