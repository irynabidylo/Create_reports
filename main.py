import data
import statistics
import datetime
import sys
import reports


def main():
    """ Main Function of the Program """

    if len(sys.argv) != 4:
        print("Name of file report cannot be empty. Enter report name")
        exit(0)

    if sys.argv[1] == "phone":
        data_list = data.get_phone_info_list()
    elif sys.argv[1] == "tablet":
        data_list = data.get_tablet_info_list()
    elif sys.argv[1] == "laptop":
        data_list = data.get_laptop_info_list()
    else:
        print("Invalid input type")
        exit(0)

    date = datetime.datetime.now()
    input_type = sys.argv[1].capitalize()
    device_type = ""
    num_devices = ""
    avg_price = ""
    min_price = ""
    max_price = ""
    median_ram = ""
    operating_systems = ""

    prices_list = []
    ram_list = []
    os_list = []
    index = 0

    while index < len(data_list):
        device_type = input_type
        num_devices = len(data_list)

        device_info = data_list[index].split(",")
        prices_list.append(float(device_info[6]))

        avg_price = round(statistics.mean(prices_list), 2)
        min_price = min(prices_list)
        max_price = max(prices_list)

        ram_list.append(int(device_info[3]))
        median_ram = statistics.median(ram_list)

        os = ("%s %s" % (device_info[4], (device_info[5])))
        os_list.append(os)
        operating_systems = os_list
        operating_systems_reverse = sorted(set(operating_systems), reverse=True)

        index += 1

    mydict = {"date_time": str(date.strftime("%Y-%m-%d %H:%M")),
              "device_type": input_type,
              "number": num_devices,
              "average_price": avg_price,
              "min_price": min_price,
              "max_price": max_price,
              "median_ram": median_ram,
              "operating_systems": operating_systems_reverse
              }

    if sys.argv[2] == "text":
        reports.report_text(date, device_type, num_devices, avg_price,
                            min_price, max_price, median_ram, operating_systems_reverse)
    elif sys.argv[2] == "csv":
        reports.report_csv(date, device_type, num_devices, avg_price,
                           min_price, max_price, median_ram, operating_systems_reverse)
    elif sys.argv[2] == "json":
        reports.report_json(mydict)
    elif sys.argv[2] == "yaml":
        reports.report_yaml(mydict)
    else:
        print("Invalid report type")
        exit(0)


if __name__ == '__main__':
    main()
