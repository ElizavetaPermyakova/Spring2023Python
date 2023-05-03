import pathlib
import typing as tp
import random

T = tp.TypeVar("T")


def read_sudoku(path: tp.Union[str, pathlib.Path]) -> tp.List[tp.List[str]]:
    """ Прочитать Судоку из указанного файла """
    path = pathlib.Path(path)
    with path.open() as f:
        puzzle = f.read()
    return create_grid(puzzle)


def create_grid(puzzle: str) -> tp.List[tp.List[str]]:
    digits = [c for c in puzzle if c in "123456789."]
    grid = group(digits, 9)
    return grid


def display(grid: tp.List[tp.List[str]]) -> None:
    """Вывод Судоку """
    width = 2
    line = "+".join(["-" * (width * 3)] * 3)
    for row in range(9):
        print(
            "".join(
                grid[row][col].center(width) + ("|" if str(col) in "25" else "") for col in range(9)
            )
        )
        if str(row) in "25":
            print(line)
    print()


def group(values: tp.List[T], n: int) -> tp.List[tp.List[T]]:
    """ Сгруппировать значения values в список, состоящий из списков по n элементов """
    return [values[i * n:(i + 1) * n] for i in range(n)]


def get_row(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения для номера строки, указанной в pos"""
    return grid[pos[0]]


def get_col(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения для номера столбца, указанного в pos"""
    c = []
    for i in range(len(grid)):
        c.append(grid[i][pos[1]])
    return c


def get_block(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения из квадрата, в который попадает позиция pos"""
    d = []
    for n in range(0, 9, 3):
        if (n <= pos[0] <= n+2):
            a = n

    for m in range(0, 9, 3):
        if (m <= pos[1] <= m+2):
            b = m

    for i in range(a, a + 3):
        for j in range(b, b + 3):
            d.append(grid[i][j])

    return d


def find_empty_positions(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.Tuple[int, int]]:
    """Найти первую свободную позицию в пазле"""
    a = [10, 10]
    for i in range(len(grid)):
        for j in range(len(grid)):
            if (grid[i][j] == '.'):
                a[0] = i
                a[1] = j
                break
    return tuple(a)


def find_possible_values(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.Set[str]:
    """Вернуть множество возможных значения для указанной позиции"""
    b = set('123456789') - set(get_row(grid, pos)) - set(get_col(grid, pos)) - set(get_block(grid, pos))
    return b


def solve(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.List[tp.List[str]]]:
    """ Решение пазла, заданного в grid """
    if find_empty_positions(grid) == (10, 10):
        return grid

    i = find_empty_positions(grid)[0]
    j = find_empty_positions(grid)[1]

    for a in find_possible_values(grid, find_empty_positions(grid)):
        grid[i][j] = a
        if solve(grid):
            return solve(grid)

    grid[i][j] = '.'



def check_solution(solution: tp.List[tp.List[str]]) -> bool:
    """ Если решение solution верно, то вернуть True, в противном случае False """
    for i in range(9):
        if (set(get_row(solution, (i, 0))) != set('123456789')) \
                or (set(get_col(solution, (0, i))) != set('123456789')) \
                or (set(get_block(solution, ((i // 3) * 3, (i % 3) * 3))) != set('123456789')):
            return False
    return True


def generate_sudoku(N: int) -> tp.List[tp.List[str]]:
    """Генерация судоку заполненного на N элементов"""
    a = [['.' for n in range(0, 9)] for m in range(0, 9)]
    b = solve(a)

    while (N < 81):
        i = random.randint(0, 8)
        j = random.randint(0, 8)
        if b[i][j] != '.':
            b[i][j] = '.'
            N += 1
    return b


if __name__ == "__main__":
    for fname in ["puzzle1.txt", "puzzle2.txt", "puzzle3.txt"]:
        grid = read_sudoku(fname)
        display(grid)
        solution = solve(grid)
        if not solution:
            print(f"Puzzle {fname} can't be solved")
        else:
            display(solution)
