import heapq
from abc import abstractmethod, ABC
from collections import deque

from GameState import GameState
# parent abstract class for all search algorithms
from Heuristics import Heuristic


class SearchAlgorithm(ABC):
    def __init__(self):
        self.__expanded = set()  # a set of all expanded nodes

    @property
    def expanded(self):
        return self.__expanded

    @abstractmethod
    def search(self, initial_state: GameState):
        pass


class UninformedSearch(SearchAlgorithm):
    @abstractmethod
    def remove_from_frontier(self):
        pass

    def search(self, initial_state: GameState):
        frontier = deque()
        frontier.append(initial_state)
        while frontier:
            curr = frontier.popleft()
            self.expanded.add(curr.configuration)
            if curr.is_goal():
                return curr, self.expanded
            for child in curr.spawn_children():
                if child.configuration not in self.expanded and child not in frontier:
                    frontier.append(child)
        return None, self.expanded


class BFS(SearchAlgorithm):
    def search(self, initial_state: GameState):
        frontier = deque()  # used as a queue
        frontier.append(initial_state)
        while frontier:
            curr = frontier.popleft()
            self.expanded.add(curr.configuration)
            if curr.is_goal():
                return curr, self.expanded
            for child in curr.spawn_children():
                if child.configuration not in self.expanded and child not in frontier:
                    frontier.append(child)
        return None, self.expanded


class DFS(SearchAlgorithm):
    def search(self, initial_state: GameState):
        frontier = deque()  # used as a stack
        frontier.append(initial_state)
        while frontier:
            curr = frontier.pop()
            self.expanded.add(curr.configuration)
            if curr.is_goal():
                return curr, self.expanded
            for child in curr.spawn_children():
                if child.configuration not in self.expanded and child not in frontier:
                    frontier.append(child)
        return None, self.expanded


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
