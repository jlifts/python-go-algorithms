from collections import deque

graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anju', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anju'] = ['jenny', 'fred']
graph['peggy'] = ['bob', 'daniel']
graph['thom'] = []
graph['jonny'] = []
graph['fred'] = ['peggy']
graph['daniel'] = ['thom']
graph['jenny'] = ['alice']


def person_is_seller(name):
    return name[-1] == 'l'


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


if __name__ == '__main__':
    search('anju')
