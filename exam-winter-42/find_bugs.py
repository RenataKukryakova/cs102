import pathlib


def load_tasks(taskfile: str = "C:\\Users\\Николай\\Downloads\\tasks.txt"):
    tasks = []
    path = pathlib.Path(taskfile)
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
        lines = (a for a in text.split('\n') if a)
        current = 0
        for line in lines:
            if 'task' in line:
                tasknum = int(line[4:]) - 1
                tasks.insert(tasknum, [])
                current = tasks[tasknum]
            else:
                node = line.split(' -> ')
                current.append(tuple(node))
    return tasks


def count_elements(graph):
    elements = [[el for el in node] for node in graph]
    unique = set([j for i in elements for j in i])
    return len(unique)


def find_broken(graph):
    unique = count_elements(graph)
    elements = {}
    broken = 0

    for link in graph:
        if link[0] == link[1]:
            broken += 1
        for element in link:
            if not element in elements.keys():
                elements[element] = 0
            elements[element] += 1

    for i, count in enumerate(elements.values()):
        if i == 0:
            continue
        if count > 2:
            broken += 1
    return broken


def fix(graph):
    i = -1
    self_ref = []
    for link in graph:
        i += 1
        if link[0] == link[1]:
            self_ref.append((link, i))

    if len(self_ref) != 0:
        return (self_ref[0][0][0], graph[self_ref[0][1] + 1][0])

    if graph[i][1] != graph[0][0]:
        graph[i] = (graph[i][0], graph[0][0])

    return graph[i]


def main():
    tasks = load_tasks()
    for task in tasks:
        broken = find_broken(task)
        if broken == 1:
            new = fix(task)
            if new:
                print(f'{new[0]} -> {new[1]}')
            else:
                print('V, V, V...')


main()