
import csv
import datetime
import requests


FILE_URL = "https://storage.googleapis.com/gwg-hol-assets/gic215/employees-with-date.csv"


def get_start_date():
    """Interactively get the start date to query for."""

    print()
    print('Getting the first start date to query for.')
    print()
    print('The date must be greater than Jan 1st, 2018')
    year = input('Enter a value for the year: ')
    month = input('Enter a value for the month: ')
    day = input('Enter a value for the day: ')
    print()
    return datetime.datetime(int(year), int(month), int(day))


def get_file_lines(url):
    """Returns the lines contained in the file at the given URL"""

    # Download the file over the internet
    response = requests.get(url, stream=True)

    lines = []

    for line in response.iter_lines():
        lines.append(line.decode("UTF-8"))
    return lines


def get_same_or_newer(start_date):
    """Returns the employees that started on the given date, or the closest one."""
    data = get_file_lines(FILE_URL)
    reader = csv.DictReader(data)
    dictionary = {}
    new_dictionary = {}
    for row in reader:
        dictionary["{} {}".format(
            row["Name"], row["Surname"])] = row["Start Date"]
    sort_dict = sorted(dictionary.items(), key=lambda x: x[1], reverse=False)
    for row in sort_dict:
        new_dictionary["{}".format(row[0])] = row[1]
    min_date_employees = []
    for row in new_dictionary.items():
        row_date = datetime.datetime.strptime(row[1], '%Y-%m-%d')
        if row_date >= start_date:
            min_date_employees.append("{} {}".format(row[0], row[1]))
        else:
            continue
    # print(min_date_employees)
    return min_date_employees


def list_newer(start_date):
    employees = get_same_or_newer(start_date)
    employee_dict = {}
    employee_list = []
    k = 1
    for j in range(len(employees) - 1):
        if (employees[j][-10:] == employees[k][-10:]):
            employee_dict["Date:"] = employees[j][-10:]
            employee_list.append(employees[j][:-11])
            employee_list += [employees[k][:-11]]
            employee_dict["Names:"] = employee_list
            k += 1
            j -= 1
        elif(len(employee_list) > 1):
                print(employee_dict["Names:"], "started on", employee_dict["Date:"])
                j = k
                k = j + 1
                employee_dict = {}
                employee_list = []
        else:
            employee_dict["Date:"] = employees[j][-10:]
            employee_list.append(employees[j][:-11])
            employee_dict["Names:"] = employee_list
            print(employee_dict["Names:"], "started on", employee_dict["Date:"])
            employee_dict = {}
            employee_list = []
            j = k
            k = j + 1
    employee_dict["Date:"] = employees[len(employees) - 1][-10:]
    employee_list.append(employees[len(employees) - 1][:-11])
    employee_dict["Names:"] = employee_list        
    print(employee_dict["Names:"], "started on", employee_dict["Date:"])
      
    # for i in range(len(employees) - 1):
    #     if (employees[i][-10:] == employees[i + 1][-10:]):
    #         employee_dict["Date:"] = employees[i][-10:]
    #         employee_list.append(employees[i][:-11])
    #         employee_list += [employees[i + 1][:-11]]
    #         employee_dict["Names:"] = employee_list
    #         k += 1
    #     elif (k > 1):
    #         print(employee_dict["Names:"], employee_dict["Date:"])
    #         # i += k
    #         k = 1
    #         employee_dict = {}
    #         employee_list = []
    #     else:
    #         employee_dict["Date:"] = employees[i][-10:]
    #         employee_list.append(employees[i][:-11])
    #         employee_dict["Names:"] = employee_list
    #         print(employee_dict["Names:"], employee_dict["Date:"])
    #         employee_dict = {}
    #         employee_list = []

    # if(employees[len(employees) -2][-10:] != employees[len(employees) -1][-10:]):
    #         employee_dict["Date:"] = employees[len(employees) -1][-10:]
    #         employee_list.append(employees[len(employees) -1][:-11])
    #         employee_dict["Names:"] = employee_list
    #         print(employee_dict["Names:"], employee_dict["Date:"])

        # elif(i + 1 < len(employees) and employees[i][-10:] != employees[i + 1][-10:]):
        #     print("['{}'] started on {}.".format(employees[i][:-11], employees[i][-10:]))
    return


# def main():
start_date = get_start_date()
list_newer(start_date)

# if __name__ == "__main__":
#     main()
