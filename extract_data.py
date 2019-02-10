import re
import csv

def process_data(filename):
    '''
    (str) --> list
    This function makes a list of lists from file with list format
    '''
    with open(filename) as f:
        lst = f.readlines()
    lst = lst[14:]
    main_lst = []
    pattern_year = r"[1-2][0-9][0-9][0-9]"
    pattern_title = r"\".*?\""
    additional_pattern = r"\(.*?\)"
    for line in lst:
        try:
            match_year = re.search(pattern_year, line)
            if re.match(pattern_title, line):
                match_title = re.search(pattern_title, line)
                title = match_title.group()
            else:
                title = line.split("(")[0]
            if ")}" in str(line):
                location = line.split(")}")[-1]
            else:
                location = line.split("\t")[-1]
            location = location.split("(")[0]
            title = title.replace("\"", "").replace("\#","")
            main_lst.append((title.strip(), match_year.group(), location.strip()))
        except:
            pass
    return main_lst


def make_csv(main_lst):
    '''
    (list) --> None
    Takes the list of lists and save the data to file with csv format
    '''
    with open("data.csv", 'w') as outcsv:
        writer = csv.writer(outcsv, delimiter=',', lineterminator='\n')
        writer.writerow(['title', 'year', 'location'])
        for item in main_lst:
            writer.writerow([item[0].replace("�",""), item[1], item[2]])


if __name__ == '__main__':
    main_lst = process_data("locations.list")
    make_csv(main_lst)
