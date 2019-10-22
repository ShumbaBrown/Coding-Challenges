class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        flights = collections.defaultdict(list)

        for source, dest in sorted(tickets)[::-1]:
            flights[source].append(dest)

        route = []
        self.visit('JFK', flights, route)
        return route[::-1]


    def visit(self, airport, flights, route):
        while flights[airport]:
            next_city = flights[airport].pop()
            self.visit(next_city, flights, route)
        route.append(airport)
        
