import os


def read_gt_for_id(filename):
    """Reads if genotype transcript file, all rules with # will not be read

    :param: filename - str
    :return: rsidlist, iidlist
    """

    rsidlist = []
    iidlist = []
    try:
        # open file
        with open(filename) as file:
            # read file per line
            for line in file:
                # checks if line does not start with #
                if line.startswith("rs"):
                    # add only the first word (rsid) to the list
                    rsidlist.append(line.split(None, 1)[0])
                elif line.startswith("i"):
                    # add only the first word (iid) to the list
                    iidlist.append(line.split(None, 1)[0])

        # return rs id and i id list
        return rsidlist, iidlist
    except FileNotFoundError:
        print("File could not be found")
    except IOError:
        print("File is not readable")
    except NameError:
        print("Name does not exist")

def read_gt(filename):
    """Reads if genotype transcript file, all rules with # will not be read

    :param: filename - str
    :return: gtlist
    """

    gtlist = dict()
    try:
        # open file
        with open(filename) as file:
            # read file per line
            for line in file:
                # checks if line does not start with #
                if line.startswith("rs"):
                    # add only the first word (rsid) to the list
                    rsid, chromosome, position, genotype = (line.split())
                    gtlist[rsid] = chromosome, position, genotype
        # returns gt file as dictionary
        return gtlist
    except FileNotFoundError:
        print("File could not be found")
    except IOError:
        print("File is not readable")
    except NameError:
        print("Name does not exist")


def main():
    # filename = ""
    # rsidlist, iidlist = read_gt(filename)

    path = "C:/Users/colin/PycharmProjects/cdt_2022/res/GT_files/Original_files"
    entries = os.listdir(path)
    for file in entries:
        print(file)
        gtlist = read_gt(os.path.join(path, file))
        # print(gtlist)
    return gtlist


print(main())
