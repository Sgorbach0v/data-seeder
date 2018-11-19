import os
import csv
import itertools

#TODO: all intents in one text file

cur_dir = os.getcwd()
csv_input = cur_dir + '/csv_input/input_data.csv'


#creating folder for output if doesn't exist
if not os.path.exists(cur_dir + '/csv_output'):
    os.makedirs(cur_dir + '/csv_output')

intent = 'check_balance'
path_to_write = cur_dir + '/csv_output/'+intent+'.csv'

input_data = []

with open (csv_input, 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        input_data.append(row)


#Creating a dict for each phrase element and all synonyms for each of those elements
def get_data():
    #number of elements, first element omitted - title of the row
    phrase_elements = input_data[1]
    dict_of_elements_and_synonyms = {}

    for item in phrase_elements[1:]:
        my_list = []

        #iterating over rows with synonyms only, excluding the first two rows with intent and element names
        for i in input_data[2:]:
            #skip empty entries
            if i[int(item)] == '':
                continue

            my_list.append(i[int(item)])
        dict_of_elements_and_synonyms[item] = my_list
    return dict_of_elements_and_synonyms


# create combos
def create_combinations(*args):
    list_of_final_queries = []

    for query in itertools.product(*args):
        #deleting 'optional' from the queries
        query_no_optional = [i for i in list(query) if i != 'optional']

        #TODO: identify such cases automatically. at the very beginning when getting data
        if query_no_optional.count('please') == 2:
            continue

        list_of_final_queries.append(' '.join(query_no_optional))

    print('Total number of queries is:',len(list_of_final_queries))
    return list_of_final_queries


# write
def write_file(queries_to_write):

    with open(path_to_write, 'w') as file:
        file.write("\n".join(queries_to_write))

    print('Done writing')


if __name__ == "__main__":
    dictionary_values = get_data().values()
    queries = create_combinations(*dictionary_values)
    write_file(queries)


