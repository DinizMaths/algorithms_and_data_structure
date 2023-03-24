from csv import reader



class DataSet(dict):
    def __init__(self, columns=None, data=None):
        super().__init__()
        if columns is not None and data is not None:
            self.__fill(columns, data)


    @property
    def columns(self):
        return list(self.keys())

    @property
    def shape(self):
        n_rows = len(next(iter(self.values()), []))
        n_columns = len(self)

        return (n_rows, n_columns)


    def __fill(self, columns, data):
        n_columns = len(columns)

        for idx, column in enumerate(columns):
            self[column] = [row[idx] for row in data if len(row) == n_columns]


    def get_row(self, row_index):
        return [self[column][row_index] for column in self.columns]

    def get_column(self, column):
        return self[column]

    def explore_data(self, start, stop):
        for column in self.columns:
            print(f"{column}: {self[column][start:stop]}")

    def head(self):
        self.explore_data(0, 5)

    def add_row(self, new_row):
        n_rows = len(next(iter(self.values()), []))

        if len(new_row) != len(self):
            raise ValueError(f"Expected {len(self)} columns, but got {len(new_row)}")

        for idx, column in enumerate(self.columns):
            self[column].append(new_row[idx])

    def delete_row(self, row_index):
        for column in self.columns:
            del self[column][row_index]



def read_csv(file_path):
    with open(file_path) as opened_file:
        read_file = reader(opened_file)
        list_file = list(read_file)

        columns = list_file[0]
        data    = list_file[1:]

        return DataSet(columns, data)
        
def generate_frequency_dict(dataset, column, sorted_dict=False):
    freq = {}

    for idx, value in enumerate(dataset[column]):
        if value not in freq.keys():
            freq[value] = 1
        else:
            freq[value] += 1

    if sorted_dict:
        return dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))
    
    return freq