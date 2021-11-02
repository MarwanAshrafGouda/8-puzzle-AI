import heapq
from abc import abstractmethod, ABC
from collections import deque

from GameState import GameState
from Heuristics import Heuristic


# parent abstract class for all search algorithms
class SearchAlgorithm(ABC):
    def __init__(self):
        self.__expanded = set()  # a set of all expanded nodes
        self.__max_depth = 0

    @property
    def expanded(self):
        return self.__expanded

    @property
    def max_depth(self):
        return self.__max_depth

    @max_depth.setter
    def max_depth(self, max_depth):
        self.__max_depth = max_depth

    @abstractmethod
    def search(self, initial_state: GameState):
        pass

    @staticmethod
    # visualizes the given board configuration
    def _string_to_grid(config: str):
        print(config)


# a parent class for DFS and BFS
class UninformedSearch(SearchAlgorithm):
    def __init__(self):
        super().__init__()
        self._frontier = deque()

    @abstractmethod
    # popping the deque according to the type of search
    def remove_from_frontier(self):
        pass

    def __is_in_frontier(self, configuration: str):
        for node in self._frontier:
            if node.configuration == configuration:
                return True
        return False

    def search(self, initial_state: GameState):
        self._frontier.append(initial_state)
        while self._frontier:
            curr = self.remove_from_frontier()
            self._string_to_grid(curr.configuration)
            self.expanded.add(curr.configuration)
            self.max_depth = max(self.max_depth, curr.depth)
            if curr.is_goal():
                return curr, self.expanded, self.max_depth
            for child in curr.spawn_children():
                if child.configuration not in self.expanded and not self.__is_in_frontier(child.configuration):
                    self._frontier.append(child)
        return None, self.expanded, self.max_depth


class BFS(UninformedSearch):
    def remove_from_frontier(self):
        # treat frontier as a queue
        return self._frontier.popleft()


class DFS(UninformedSearch):
    def remove_from_frontier(self):
        # treat frontier as a stack
        return self._frontier.pop()


class AStar(SearchAlgorithm):
    def __init__(self, heuristic: Heuristic):
        self.__heuristic = heuristic
        super().__init__()

    def search(self, initial_state: GameState):
        frontier = []
        initial_state.heuristic_cost = self.__heuristic.calculate_cost(initial_state)
        heapq.heappush(frontier, initial_state)
        while frontier:
            curr = heapq.heappop(frontier)
            self._string_to_grid(curr.configuration)
            self.expanded.add(curr.configuration)
            self.max_depth = max(self.max_depth, curr.depth)
            if curr.is_goal():
                return curr, self.expanded, self.max_depth
            for child in curr.spawn_children():
                if child.configuration not in self.expanded:
                    child.heuristic_cost = self.__heuristic.calculate_cost(child)
                    heapq.heappush(frontier, child)
        return None, self.expanded, self.max_depth
