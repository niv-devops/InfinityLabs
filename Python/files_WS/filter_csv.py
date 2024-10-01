import csv

def filter(file_name):
    """ Create new CSV file out of gender, age range (include), is_vaccinated filters """
    filters = input("Enter filters (Format: field1=option field2>num): ").split(' ')
    headers = [criteria.split('=')[0] for criteria in filters]

    with open(file_name, 'r') as file:
        csv_reader = csv.DictReader(file)
        filtered_rows = []

        for row in csv_reader:
            match = True

            for criteria in filters:
                if '=' in criteria:
                    key, value = criteria.split('=')
                    if key in row and row[key] != value:
                        match = False
                        break
                elif '>' in criteria or '<' in criteria:
                    oper_index = criteria.find('>') if '>' in criteria else criteria.find('<')
                    key = criteria[:oper_index]
                    operator = criteria[oper_index]
                    value = criteria[oper_index + 1:]
                    if operator == '>':
                        if not (key in row and int(row[key]) > int(value)):
                            match = False
                            break
                    elif operator == '<':
                        if not (key in row and int(row[key]) < int(value)):
                            match = False
                            break

            if match:
                filtered_row = {}
                for header in headers:
                    filtered_row[header] = row.get(header)
                filtered_rows.append(filtered_row)
        
        if not filtered_rows:
            print("No matching data was found.")
            return
        
        with open('corona_filter.csv', 'w') as filter_file:
            csv_writer = csv.DictWriter(filter_file, fieldnames=headers)
            csv_writer.writeheader()
            csv_writer.writerows(filtered_rows)
    
    print("Filtered file 'corona_filter.csv' was successfully created.")


if __name__ == "__main__":
    print("Fields: Gender | Age | Ventilated | Length_of_hospitalization | Is_vaccinated", end=" | ")
    print("Time_between_positive_and_hospitalization | Time_between_positive_and_recovery")
    print("---------------------------------------")
    filter("corona.csv")