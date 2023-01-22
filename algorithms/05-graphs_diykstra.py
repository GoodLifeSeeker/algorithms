'''
We have this graph scheme:

 START---6--->A
     \       ^ \
      2     /   1
       \   3     \
        v /       v
         B---5-->END

We need to find the shortest way from start to end, which is obviously start->B->A->End.
'''
graph = {}
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2
graph['a'] = {}
graph['a']['end'] = 1
graph['b'] = {}
graph['b']['a'] = 3
graph['b']['end'] = 5
graph['end'] = {}

costs = {}
infinity = float('inf')
costs['a'] = 6
costs['b'] = 2
costs['end'] = infinity

parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['end'] = None

processed = []


def find_the_lowest(costs):
    '''Finds the node with the min weight and which is not processed yet.'''
    lowest_cost = float('inf')
    low_cost_host = None
    for host in costs:
        cost = costs[host]
        if cost < lowest_cost and host not in processed:
            lowest_cost = cost
            low_cost_host = host
    return low_cost_host

def show_line(parents):
    ''' Returns order of the shortest way.'''
    parents = {values: keys for keys, values in parents.items()}
    cur_key = 'start'
    line = ''
    while cur_key != 'end':
        line += cur_key + ' -> '
        cur_key = parents[cur_key]
    line += 'end'
    return line
        

node = find_the_lowest(costs)
while node is not None:
    cost = costs[node]
    neighbours = graph[node]
    for n in neighbours.keys():
        new_cost = cost + neighbours[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_the_lowest(costs)

print(f'Order of way is: {show_line(parents)}')
print(f'The weight of the shortest way is: {costs["end"]}')
print('END')
