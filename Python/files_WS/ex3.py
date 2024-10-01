# Approved by:

import csv
import sys
from functools import reduce

def min_max_vaccinated_patients(file_name):
    """ Prints min and max age of vaccinated and unvaccinated patients """
    vaccinated_min = sys.maxsize
    vaccinated_max = -sys.maxsize - 1 
    unvaccinated_min = sys.maxsize
    unvaccinated_max = -sys.maxsize - 1
    
    with open(file_name, mode="r") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            age = int(row['Age'])
            if row['Is_vaccinated'] == 'Y':
                if age < vaccinated_min:
                    vaccinated_min = age
                if age > vaccinated_max:
                    vaccinated_max = age
            else:
                if age < unvaccinated_min:
                    unvaccinated_min = age
                if age > unvaccinated_max:
                    unvaccinated_max = age
    
    print(f"Youngest vaccinated patient: {vaccinated_min}")
    print(f"Oldest vaccinated patient: {vaccinated_max}")
    print(f"Youngest unvaccinated patient: {unvaccinated_min}")
    print(f"Oldest unvaccinated patient: {unvaccinated_max}")


def avg_length_of_hosp(file_name):
    """ Prints min and max age of vaccinated and unvaccinated patients """
    with open(file_name, mode="r") as file:
        csv_reader = csv.DictReader(file)

        hosp_len = [float(row['Length_of_hospitalization']) for row in csv_reader]
        sum_hosp_len= reduce(lambda x, y: x + y, hosp_len, 0)
        print(f"Average hospitalization length: {sum_hosp_len / len(hosp_len)}")


def filter(file_name):
    """ Create new filtered CSV file according to user's input in specified format: 
        Format example: field1=option field2>num field3<num field_n"""
    filters = input("Enter filters (Format: field1=option field2>num): ").split(' ')

    with open(file_name, 'r') as file:
        csv_reader = csv.DictReader(file)
        filtered_rows = []

        for row in csv_reader:
            match = True

            for criteria in filters:
                if '=' in criteria:
                    key, value = criteria.split('=')
                    if key in row and row[key].strip() != value.strip():
                        match = False
                        break
                elif '>' in criteria or '<' in criteria:
                    oper_index = criteria.find('>') if '>' in criteria else criteria.find('<')
                    key = criteria[:oper_index].strip()
                    operator = criteria[oper_index]
                    value = int(criteria[oper_index + 1:].strip()) 
                    if operator == '>':
                        if not (key in row and int(row[key].strip()) > value):
                            match = False
                            break
                    elif operator == '<':
                        if not (key in row and int(row[key].strip()) < value):
                            match = False
                            break
            if match:
                filtered_rows.append(row)
    
        if not filtered_rows:
            print("No matching data was found.")
        else:
            with open('corona_filter.csv', 'w') as filter_file:
                csv_writer = csv.DictWriter(filter_file, fieldnames=csv_reader.fieldnames)
                csv_writer.writeheader()
                csv_writer.writerows(filtered_rows)
        
            print("Filtered file 'corona_filter.csv' was successfully created.")


if __name__ == "__main__":
    print("Fields: Gender | Age | Ventilated | Length_of_hospitalization | Is_vaccinated", end=" | ")
    print("Time_between_positive_and_hospitalization | Time_between_positive_and_recovery")
    print("---------------------------------------")
    min_max_vaccinated_patients("corona.csv")
    avg_length_of_hosp("corona.csv")
    print("---------------------------------------")
    filter("corona.csv")