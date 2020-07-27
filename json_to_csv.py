import sys, json, csv

def to_string(s):
    try:
        return str(s)
    except:
        return s.encode('utf-8')


def reduce_item(key, value):
    global reduced_item
    
    if type(value) is list:
        i=0
        for sub_item in value:
            reduce_item(key+to_string(i), sub_item)
            i=i+1

    elif type(value) is dict:
        sub_keys = value.keys()
        for sub_key in sub_keys:
            reduce_item(key+to_string(sub_key), value[sub_key])
    
    else:
        reduced_item[to_string(key)] = to_string(value)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print ("\nUsage: python json_to_csv.py <json_in_file_path> <csv_out_file_path>\n")
    else:
        node = ""
        json_file_path = sys.argv[1]
        csv_file_path = sys.argv[2]

        fp = open(json_file_path, 'r')
        json_value = fp.read().decode('utf-8')
        raw_data = json.loads(json_value)
        fp.close()
        
        try:
            data_to_be_processed = raw_data[node]
        except:
            data_to_be_processed = raw_data

        processed_data = []
        header = []
        for item in data_to_be_processed:
            reduced_item = {}
            reduce_item(node, item)

            header += reduced_item.keys()

            processed_data.append(reduced_item)

        header = list(set(header))
        header.sort()

        with open(csv_file_path, 'w+') as f:
            writer = csv.DictWriter(f, header, quoting=csv.QUOTE_ALL)
            writer.writeheader()
            for row in processed_data:
                writer.writerow(row)

        print ("Arquivo CSV criado com %d colunas" % len(header))