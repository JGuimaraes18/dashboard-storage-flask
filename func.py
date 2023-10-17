
def format_bytes(size):
    # 2**10 = 1024
    power = 2**10
    n = 0
    power_labels = {-1 : 'B', 0: 'KB', 1: 'MB', 2: 'GB', 3: 'TB', 4: 'PB'}
    while size > power:
        size /= power
        n += 1
        # print(size, n)
    return size, power_labels[n]

def converter(c):
    t = 2
    d = int(c[0] * 10**t)/10**t
    return d

def percVol(volumeUsado, volumeTotal):
    percent = (volumeUsado/volumeTotal)*100
    percent="{0:.2f}".format(percent)
    return percent
