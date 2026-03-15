#This code calculate statistics of a dataset.

def calculate_statistics(**dataset: list) -> dict:
    statistics_dict = {}
    for dataset_name, dataset_numbers in dataset.items():
        if dataset_numbers:
            data_sum, data_avg, data_max, data_min = statistics_calculator(dataset_numbers)

            statistics_dict[dataset_name] = {
                'sum' : data_sum,
                'average' : data_avg,
                'min' : data_min,
                'max' : data_max
            }
        else:
            statistics_dict[dataset_name] = {
                'sum' : None,
                'average' : None,
                'min' : None,
                'max' : None
            }
    return statistics_dict

def statistics_calculator(data_list: list):
    if data_list:
        data_sum = sum(data_list)
        data_avg = data_sum / len(data_list) 
        data_max = max(data_list) 
        data_min = min(data_list) 
        return data_sum, data_avg, data_max, data_min


if __name__ == '__main__':
    print(calculate_statistics(math=[10, 20, 30], science=[30, 40, 50], programming=[]))