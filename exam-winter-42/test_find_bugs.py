import find_bugs

def test_load_tasks():
    print(find_bugs.load_tasks())
    assert [[('A', 'B'), ('B', 'C'), ('C', 'B')], [('A', 'A'), ('B', 'C'), ('C', 'A')], [('A', 'A'), ('B', 'B')]] == find_bugs.load_tasks()

def test_count_elements():
    graph = find_bugs.load_tasks()[0]
    assert ['A', 'B', 'B', 'C', 'C', 'B'] == find_bugs.count_elements(graph)

def test_fix():
    graph = find_bugs.load_tasks()[0]
    assert ('C', 'A') == find_bugs.fix(graph)

def test_find_broken():
    graph = find_bugs.load_tasks()[0]
    assert 1 == find_bugs.find_broken(graph)