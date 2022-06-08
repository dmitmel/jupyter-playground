import matplotlib.pyplot as plt

def plot(title, xs, ys, **kwargs):
    plt.figure(figsize=(15, 5))
    plt.suptitle(title, fontsize=24)

    plt.subplot(121, **kwargs)
    plt.title('linear')
    plt.plot(xs, ys, 'bo')

    plt.subplot(122, **kwargs)
    plt.title('logarithmic')
    plt.loglog(xs, ys, 'bo')

    plt.show()
