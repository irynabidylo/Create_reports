# Data Module

def get_phone_info_list():
    """ Returns a list of phone data """
    # Format <id>,<manufacturer>,<model>,<memory in GB>,<operating system>,<os version>,<price>

    fh = open("phones.csv", "r")
    data = fh.readlines()
    fh.close()
    return data


def get_tablet_info_list():
    """ Returns a list of tablet data """
    # Format <id>,<manufacturer>,<model>,<memory in GB>,<operating system>,<os version>,<price>

    fh = open("tablets.csv", "r")
    data = fh.readlines()
    fh.close()
    return data


def get_laptop_info_list():
    """ Returns a list of laptop data """

    # Format <id>,<manufacturer>,<model>,<memory in GB>,<operating system>,<os version>,<price>

    fh = open("laptops.csv", "r")
    data = fh.readlines()
    fh.close()
    return data
