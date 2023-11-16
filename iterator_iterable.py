### Iterators and Iterables

class Cities:

    def __init__(self):
        self._cities = ['Paris', 'Berlin', 'Rome', 'Madrid', 'London']
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._cities):
            raise StopIteration
        else:
            item = self._cities[self._index]
            self._index +=1
            return item


cities = Cities()
print(list(enumerate(cities)))



class Cities:

    def __init__(self):
        self._cities = ['Paris', 'Berlin', 'Rome', 'Madrid', 'London']
        self._index = 0

    def __len__(self):
        return len(self._cities)


cities = Cities()



class CityIterator:
    
    def __init__(self, city_obj):
        self._city_obj = city_obj
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        
        if self._index >= len(self._city_obj):
            raise StopIteration
        else:
            item = self._city_obj._cities[self._index]
            self._index +=1
            return item

city_iterator = CityIterator(cities)
for i in city_iterator:
    print(i)




class Cities:

    def __init__(self):

        self._cities = ['Paris', 'Berlin', 'Rome', 'Madrid', 'Kahalgaon']
        self._index = 0

    def __len__(self):
        return len(self._cities)

    def __iter__(self):
        return CityIterator(self)

cities = Cities()

for item in cities:
    print(item)

print([item for item in cities])
