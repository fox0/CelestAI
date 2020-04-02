"""
Игра "Пятнашки". Только 8 состояний.
"""
import logging

from aima.search import EightPuzzle, astar_search

log = logging.getLogger(__name__)


def main():  # pylint: disable=missing-docstring
    state = [0, 4, 5, 6, 2, 1, 7, 8, 3]
    assert len(set(state)) == 9
    puzzle = EightPuzzle(initial=tuple(state))
    solution = astar_search(puzzle, display=True).solution()
    print(solution)
    for move in solution:
        print_state(state)
        state = puzzle.result(state, move)
    print_state(state)


def print_state(state: list):
    """Распечатать игровое поле"""
    print(*state[0:3])
    print(*state[3:6])
    print(*state[6:9])
    print('-----')


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s [%(levelname)s] %(name)s %(funcName)s():%(lineno)d: %(message)s',
                        level=logging.DEBUG)
    main()
