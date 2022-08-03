def make_tuple(row):
    return (float(row[0]), float(row[1]), float(row[2]))

def make_dict(row):
    return {"x": float(row[0]), "y": float(row[1]), "z": float(row[2])}

class Points:
    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)


def read_data():
    records = [ ]
    with open("./data_files/points.txt", "r") as f:
        for line in f:
            parts = line.split()    # [-1.5796459414274868, 1.4362045785284654, -0.7896035854418733]
            p = Points(parts[0], parts[1], parts[2])
            records.append(p)
    return records

def average():
    data = read_data()
    # Calculate Average of x, y and z co-ordinates
    x_total = 0
    y_total = 0
    z_total = 0
    for item in data:
        x_total += item[0]
        y_total += item[1]
        z_total += item[2]
    # Average 
    average = (x_total/len(data), y_total/len(data), z_total/len(data))
    return average

def _min():
    data = read_data()
    x = [ item.x for item in data]
    y = [ item.y for item in data]
    z = [ item.z for item in data]
    # for item in data:
    #     x.append(item.x)
    #     y.append(item.y)
    #     z.append(item.z)
    return (min(x), min(y), min(z))

def _max():
    data = read_data()
    x = [ item.x for item in data]
    y = [ item.y for item in data]
    z = [ item.z for item in data]
    # for item in data:
    #     x.append(item.x)
    #     y.append(item.y)
    #     z.append(item.z)
    return (max(x), max(y), max(z))


from tracemalloc import start, stop, get_traced_memory

start()
data = read_data()
print(get_traced_memory())
stop()
