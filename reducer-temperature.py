import sys


def reducer_find_max_temperature():
    (last_key, max_val) = (None, -1000000)
    for line in sys.stdin:
        (key, val) = line.strip().split("\t")
        if last_key and last_key != key:
            print("%s\t%s" % (last_key, max_val))
            (last_key, max_val) = (key, float(val))
        else:
            (last_key, max_val) = (key, max(max_val, float(val)))

    if last_key:
        print("%s\t%s" % (last_key, max_val))

def reducer_find_min_temperature():
    (last_key, min_val) = (None, 1000000)
    for line in sys.stdin:
        (key, val) = line.strip().split("\t")
        if last_key and last_key != key:
            print("%s\t%s" % (last_key, min_val))
            (last_key, min_val) = (key, float(val))
        else:
            (last_key, min_val) = (key, min(min_val, float(val)))

    if last_key:
        print("%s\t%s" % (last_key, min_val))

def reducer_find_avg_temperature():
    year_temp_map = {}
    for line in sys.stdin:
        (key, val) = line.strip().split("\t")
        if key not in year_temp_map:
            year_temp_map[key] = [float(val)]
        else:
            year_temp_map[key].append(float(val))
    for key,temps in year_temp_map.items():
        print("%s\t%s" % (key,sum(temps)/len(temps)))

def main():
    reducer_find_max_temperature()


if __name__ == '__main__':
    main()
