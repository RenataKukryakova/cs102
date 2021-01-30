import pathlib

def load_tasks(taskfile: str = "tasks.txt"):
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
    print(f"unique: {unique}, len(graph): {len(graph)}")
    elements = {}
    broken = 0

    for link in graph:
        if link[0] == link[1]:
            broken += 1
        for element in link:
            if not element in elements.keys():
                elements[element] = 0
            elements[element] += 1

    print(elements)

    for i, count in enumerate(elements.values()):
        if i == 0:
            continue
        if count > 2:
            broken += 1

    return broken


def main():
    tasks = load_tasks()
    print(tasks)
    broken = find_broken(tasks[2])
    print(broken)

main()