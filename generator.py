course = ['Python', 'Java', 'JavaScript', 'C', 'C++']

def list_items():
    for item in course:
        yield item

gen = list_items()

for item in gen:
    print(item)