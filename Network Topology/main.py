from generate import Generate
from capacity import Capacity
from density import Density
from display import *

if __name__ == "__main__":
    d = [2,0,2,1,5,8,6,5,4,7,2,0,2,1,5,8,6,5,4,7,2]
    noOfNodes = 21
    capacity_graphs = []
    total_costs = []
    density_vals = []
    maxK =14

    for k in range(3, maxK+1):
        # aij graphs & demand values
        aij_graph = Generate().gen_aij_graphs(noOfNodes, range(0, noOfNodes), k)
        bij_graph = Generate().gen_demand_vals(d)

        capacity_graph = Capacity().min_capacity_graphs(noOfNodes, aij_graph, bij_graph)
        total_cost = Capacity().totalcost(noOfNodes, aij_graph, capacity_graph)
        density = Density().compute_densities(noOfNodes, capacity_graph)

        # capacities, total costs & densities
        capacity_graphs.append(capacity_graph)
        total_costs.append(total_cost)
        density_vals.append(density)

    Display.display(range(3, maxK+1), total_costs, "TOTAL COST", "k", "total cost")
    Display.display(range(3, maxK+1), density_vals, "DENSITIES", "k", "density")

    #Graphical network topolgies for k=3, k=8, k=14
    Display.display_network_graphs(noOfNodes, capacity_graphs[0], "k = 3")
    Display.display_network_graphs(noOfNodes, capacity_graphs[5], "k = 8")
    Display.display_network_graphs(noOfNodes, capacity_graphs[11], "k = 14")

