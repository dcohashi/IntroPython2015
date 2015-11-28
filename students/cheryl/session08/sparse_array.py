class SparseArray:

    def __init__(self, values):
        self.length = len(values)
        self.data = {}
        for i, val in enumerate(values):
            if val:
                self.data[i] = val

    def __len__(self):
        return(self.length)

    def __getitem__(self, index):
        try:
            return(self.data[index])
        except KeyError:
            return(0)

    def __setitem__(self, index, value):
        if (index > self.length):
            raise(IndexError)
        if not value:
            try: 
                del self.data[index]
            except KeyError:
                pass
        else:
            self.data[index] = value

    def __delitem__(self, index):
        if (index > self.length):       # bad index
            raise(IndexError)
        try:
            del self.data[index]
        except KeyError:
            pass        # 0 already
        finally: 
            # move all the values past the index up in the array
            for i, val in self.data.items():
                if (i > index):
                    self.data[i-1] = val
                    del self.data[i]
            self.length -= 1

    def append(self, additional):
        try:
            for val in additional:
                if val:
                    self.data[self.length] = val
                self.length += 1
        except TypeError:
            self.data[self.length] = additional
            self.length += 1

