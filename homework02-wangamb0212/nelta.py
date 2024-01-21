import csv


class LabeledList:
    def __init__(self, data=None, index=None):
        if index is None:
            index = list(range(len(data)))
        self.values = data
        self.index = index

    def __str__(self):
        s = ''
        max_len = max([len(str(label)) for label in self.index])
        vals_max_len = max([len(str(v)) for v in self.values])
        format_spec = f'>{max_len}'
        for index, data in zip(self.index, self.values):
            s += f'{index:{format_spec}} {str(data):>{vals_max_len}}\n'
        return s

    def __repr__(self):
        return self.__str__()

    def __getitem__(self, key_list):
        # try our best to make list of keys:

        # 1. first, if it's a labeled list, use the labeled list's 
        #    values property as the list of keys
        if isinstance(key_list, LabeledList):
            key_list = key_list.values

        # 2. at this point, if we still don't have a list, then assume we 
        #    have a non-sequence type, and wrap in a list
        if not isinstance(key_list, list):
            key_list = [key_list]

        # now that we definitely have a list... check if it's only
        # booleans; one way to do this is filter for only boolean values
        # and check the length against the original unfiltered list
        if len([v for v in key_list if type(v) is bool]) == len(key_list):
            # we have a bunch of booleans, keep only the values that
            # have the same label as the labels that have true
            return self.__filter(key_list) 
        else:
            # we have a bunch of keys... so get all values with a matching
            # label / key
            index = [] # labels for returned LabeledList
            data = []  # values for returned LabeledList
            for key in key_list: 
                # find key matches, and get back both the label and value
                for label, val in self.__find(key):
                    index.append(label)
                    data.append(val)
            return data[0] if len(data) == 1 else LabeledList(data, index)

    def __filter(self, filter_list):
        """ given a list of booleans, only give back the values
        that align with True as a LabeledList
        """
        index = []
        data = []
        if len(filter_list) != len(self.index):
            raise IndexError('Length of indexes does not match length of boolean list')
        for i, include in enumerate(filter_list):
            if include:
                index.append(self.index[i])
                data.append(self.values[i])
        return LabeledList(data, index)
    
    def __find(self, k):
        """give back all labels and values based on key
        """
        index, data = [], []
        matches = [(label, self.values[i]) for i, label in enumerate(self.index) if k == label]
        if len(matches) == 0:
            raise KeyError(f'Index label not found {k}')
        return matches
    
    def __iter__(self):
        return iter(self.values)
    
    def __eq__(self, scalar):
        ret_data = [i == scalar if i is not None else False for i in self.values]
        return LabeledList(ret_data, self.index)
    
    def __nq__(self, scalar):
        ret_data = [i != scalar if i is not None else False for i in self.values]
        return LabeledList(ret_data, self.index)     

    def __gt__(self, scalar):
        ret_data = [i > scalar if i is not None else False for i in self.values]
        return LabeledList(ret_data, self.index) 

    def __lt__(self, scalar):
        ret_data = [i < scalar if i is not None else False for i in self.values]
        return LabeledList(ret_data, self.index) 

    def map(self, f):
        ret_data = [f(i) for i in self.values]
        return LabeledList(ret_data, self.index)
    
class Table:
    def __init__(self, data, index=None, columns=None):
        if index == None:
            index = list(range(len(data)))
        if columns == None:
            columns = list(range(len(data[0])))
        self.values = data
        self.index = index
        self.columns = columns
        
    def __str__(self):
        rtn = ''
        length = []                            

        max_length = 0                          
        for i in self.index:
            if len(str(i)) > max_length:
                max_length = len(str(i))
        length.append(max_length)

        for i in range(len(self.columns)):      
            longest = len(str(self.columns[i]))
            for k in range(len(self.index)):
                if len(str(self.values[k][i])) > longest:
                    longest = len(str(self.values[k][i]))
            length.append(longest)
        
        title = ' ' * (length[0] + 3)           
        for i in range(len(self.columns)):
            format_spec = f'>{length[i+1]}'
            title += f'{str(self.columns[i]):{format_spec}}'
            title += ' ' * 3
        rtn += title
        rtn += '\n'

        for i in range(len(self.index)):       
            line = ''
            format_spec = f'>{length[0]}'
            line += f'{str(self.index[i]):{format_spec}}'
            line += ' ' * 3
            for k in range(len(self.columns)):
                format_spec = f'>{length[k+1]}'
                line += f'{str(self.values[i][k]):{format_spec}}'
                line += ' ' * 3
            rtn += line
            rtn += '\n'
        
        return rtn
        
    
    def __repr__(self):
        return str(self)
    
    def __getitem__(self, col_list):
        if isinstance(col_list, LabeledList):
            col_list = col_list.values
        
        if isinstance(col_list, list):
            data = []
            if all((isinstance(i, bool) for i in col_list)):
                new_index = []
                for k in range(len(col_list)):
                    if col_list[k] == True:
                        data.append(self.values[k])
                        new_index.append(self.index[k])
                return Table(data, new_index, self.columns)
            else:
                for i in range(len(self.index)):
                    line = []
                    for k in range(len(self.columns)):
                        for j in col_list:
                                if j == self.columns[k]:
                                    line.append(self.values[i][k])
                    data.append(line)
                return Table(data, self.index, col_list)
        
        else:
            single_index = []
            for i in range(len(self.columns)):
                if self.columns[i] == col_list:
                    single_index.append(i)

            data = []
            if len(single_index) == 1:
                for i in range(len(self.index)):
                    data.append(self.values[i][single_index[0]])
                return LabeledList(data, self.index)
            else:
                for i in range(len(self.index)):
                    line = []
                    for k in range(len(single_index)):
                        line.append(self.values[i][single_index[k]])
                    data.append(line)
                return Table(data, self.index, col_list * len(self.index))
        
        
    
    def head(self, n):
        data = self.values[:n]
        new_index = self.index[:n]
        return Table(data, new_index, self.columns)
    
    def tail(self, n):
        data = self.values[-n:]
        new_index = self.index[-n:]
        return Table(data, new_index, self.columns)

    def shape(self):
        col = len(self.columns)
        row = len(self.index)
        return (row, col)

      
def read_csv(fn):
    with open(fn, "r") as f:
        data = csv.reader(f, delimiter = ',') 
        new_data = []
        for i in data:
            line = []
            for k in i:
                try:
                    line.append(float(k))
                except ValueError:
                    line.append(k)
            new_data.append(line)
        col = new_data[0]
        return Table(new_data[1:], columns = col)



if __name__ == '__main__':
    t = Table([[1, 2], [3, 4], [5, 6], [7, 8]], columns=['x', 'y'])
    # print(t.shape())
    # gives back a new LabeledList composed of labels in original, along with boolean results of comparison
    pass

