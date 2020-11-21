import json
import yaml
import sys


def report_text(date, device_type, num_devices, avg_price, min_price, max_price,
                median_ram, operating_systems_reverse):
    """ Generates a report in a text format """

    fh = open(sys.argv[3]+".txt", "w")

    fh.writelines(("Timestamp: %s" % date.strftime("%Y-%m-%d %H:%M") + "\n"))
    fh.writelines("Device: %s" % device_type + "\n")
    fh.writelines("Number: %d" % num_devices + "\n")
    fh.writelines("Average Price: $%.2f" % avg_price + "\n")
    fh.writelines("Minimum Price: $%.2f" % min_price + "\n")
    fh.writelines("Maximum Price: $%.2f" % max_price + "\n")
    fh.writelines("Median RAM: %.1f GB" % median_ram + "\n")
    fh.writelines("Operating Systems: %s" % ", ".join(operating_systems_reverse) + "\n")
    fh.close()

    print("Timestamp: %s" % date.strftime("%Y-%m-%d %H:%M"))
    print("Device: %s" % device_type)
    print("Number: %d" % num_devices)
    print("Average Price: $%.2f" % avg_price)
    print("Minimum Price: $%.2f" % min_price)
    print("Maximum Price: $%.2f" % max_price)
    print("Median RAM: %.1f" % median_ram, "GB")
    print("Operating Systems: %s" % ", ".join(operating_systems_reverse))


def report_csv(date, device_type, num_devices, avg_price, min_price,
               max_price, median_ram, operating_systems_reverse):
    """ Generates a report in a csv format """

    fh = open(sys.argv[3] + ".csv", "w")

    csv_line = "%s,%s,%d,%.2f,%.2f,%.2f,%.1f,%s" % (date.strftime("%Y-%m-%d %H:%M"), device_type,
                                                    num_devices, avg_price, min_price, max_price,
                                                    median_ram, "/".join(operating_systems_reverse))

    fh.write(csv_line)
    fh.close()
    print(csv_line)


def report_json(mydict):
    """ Generates a report in json format """
    fh = open(sys.argv[3] + ".json", "w")

    json_string = json.dumps(mydict, indent=4)
    fh.write(json_string)
    fh.close()
    print(json_string)


def report_yaml(mydict):
    """ Generates a report in yaml format """
    fh = open(sys.argv[3] + ".yaml", "w")

    yaml_string = yaml.dump(mydict)
    fh.write(yaml_string)
    fh.close()
    print(yaml_string)
