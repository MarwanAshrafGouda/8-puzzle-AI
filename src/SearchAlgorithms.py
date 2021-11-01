import heapq
from abc import abstractmethod, ABC
from collections import deque

from GameState import GameState
from Heuristics import Heuristic


# parent abstract class for all search algorithms
class SearchAlgorithm(ABC):
    def __init__(self):
        self.__expanded = set()  # a set of all expanded nodes

    @property
    def expanded(self):
        return self.__expanded

    @abstractmethod
    def search(self, initial_state: GameState):
        pass


# a parent class to DFS and BFS
class UninformedSearch(SearchAlgorithm):
    def __init__(self):
        super().__init__()
        self._frontier = deque()

    @abstractmethod
    # popping the deque according to the type of search
    def remove_from_frontier(self):
        pass

    def search(self, initial_state: GameState):
        self._frontier.append(initial_state)
        while self._frontier:
            curr = self.remove_from_frontier()
            self.expanded.add(curr.configuration)
            if curr.is_goal():
                return curr, self.expanded
            for child in curr.spawn_children():
                if child.configuration not in self.expanded and child not in self._frontier:
                    self._frontier.append(child)
        return None, self.expanded


class BFS(UninformedSearch):
    def remove_from_frontier(self):
        return self._frontier.popleft()


class DFS(UninformedSearch):
    def remove_from_frontier(self):
        return self._frontier.pop()


class AStar(SearchAlgorithm):
    def __init__(self, heuristic: Heuristic):
        self.__heuristic = heuristic
        super().__init__()

    def search(self, initial_state: GameState):
        frontier = []
        heapq.heappush(frontier, initial_state)
        while frontier:
            curr = heapq.heappop(frontier)
            self.expanded.add(curr.configuration)
            if curr.is_goal():
                return curr, self.expanded
            for child in curr.spawn_children():
                if child.configuration not in self.expanded and child not in frontier:
                    child.heuristic = self.__heuristic.calculate_cost(child)
                    heapq.heappush(frontier, child)
        return None, self.expanded
