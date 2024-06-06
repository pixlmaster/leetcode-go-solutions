class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # essentially the problem is to figure out whether a cycle exists
        # we start of with constructing the adj list using a dict
        # we create a visited set, start with a random course
        # do dfs on it, if we come to visited node, return false
        # remove the visited nodes from the set, they don't need to be checked anymore,
        # else cycle would have been reported earleir
        
        adj = self.constructAdj(numCourses,prerequisites)
        
        for course in range(numCourses):
            if course in adj :
                if not self.dfs(adj,course,set()):
                    return False
        
        return True
        
    
    def dfs(self, adj : dict[int,set[int]], curr: int , visited : set[int]) ->bool:
        if curr in visited:
            return False
        visited.add(curr)
        
        children = adj[curr]
        if len(children) == 0:
            # deleting means course completed
            del adj[curr]
            return True
        

        for child in children:
            # children has been completed in a previous run
            if not child in adj:
                continue
            if not self.dfs(adj, child, visited):
                return False
        # deleting means course completed
        del adj[curr]
        return True
    
    def constructAdj(self, numCourses: int, prerequisites: List[List[int]]) -> dict[int, set[int]]:
        adjList = {}
        for course in range(numCourses):
            adjList[course] = set()
        
        for prereq in prerequisites:
            adjList[prereq[0]].add(prereq[1])
            
        
        return adjList
        
        