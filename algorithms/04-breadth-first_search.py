'''There is a graph scheme:

     Alice --- Peggy
    /         /
you ----- Bob ---Anuj
    \
     Claire --- Tom
           \
            Jonny

One of them could be a seller that you need. You only know your friend's names and know, that
seller's name end's on 'm'. 

'''
from collections import deque

graph = {}
graph['you'] = ['Alice', 'Bob', 'Claire']
graph['Alice'] = ['Peggy']
graph['Bob'] = ['Anuj', 'Peggy']
graph['Claire'] = ['Tom', 'Jonny']
graph['Anuj'] = []
graph['Peggy'] = []
graph['Tom'] = []
graph['Jonny'] = []


def is_seller(name):
    return name[-1] == 'm'

search_queue = deque()
search_queue += graph['you']
found = None
while search_queue:
    person = search_queue.popleft()
    if is_seller(person):
        print(f'{person} is a seller!')
        found = True
    else:
        search_queue += graph[person]

if not found:
    print('There are no sellers!')


