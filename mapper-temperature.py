import sys
import io


def process_input_mapper_station_temperature(line):
    """
    Process a single line of text: split the line by comma and extract station id and temperature
    """
    val = line.strip()
    values = val.split(',')
    station_id = values[0].strip()
    temperature = values[3].strip()
    if '999.9' not in temperature:
        print("%s\t%s" % (station_id, temperature))


def process_input_mapper_year_temperature(line):
    """
    Process a single line of text: split the line by comma and extract station id and temperature
    """
    val = line.strip()
    values = val.split(',')
    year = values[2].strip()[0:4]
    temperature = values[3].strip()
    if '999.9' not in temperature:
        print("%s\t%s" % (year, temperature))

def process_input_station_032_temperature(line):
    val = line.strip()
    values = val.split(',')
    station_id = values[0].strip()
    temperature = values[3].strip()
    if station_id.startswith("032") and '999.9' not in temperature:
        print("%s\t%s" % (station_id, temperature))

def main():
    # Read from standard input with specified encoding
    input_stream = io.TextIOWrapper(sys.stdin.buffer, encoding='latin1')
    for line in input_stream:
        # map station and temperature data
        #process_input_mapper_station_temperature(line)
        # map year and temperature data
        process_input_mapper_year_temperature(line)


if __name__ == '__main__':
    main()
