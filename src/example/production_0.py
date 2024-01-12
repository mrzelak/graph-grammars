from graph import Graph, Node, NodeAttrs, EdgeAttrs, Edge
import basic_graph
import matplotlib.pyplot as plt
import itertools as it

def main():
    fig, plot = plt.subplots(nrows=1, ncols=1)

    graph = Graph()

    node_1 = Node(NodeAttrs('v', 0, 0, False), 0)
    node_2 = Node(NodeAttrs('v', 1, 0, False), 1)
    node_3 = Node(NodeAttrs('v', 1.3, 0.5, False), 2)
    node_4 = Node(NodeAttrs('v', 1, 1, False), 3)
    node_5 = Node(NodeAttrs('v', 0, 1, False), 4)

    pent_nodes = [node_1, node_2, node_3, node_4, node_5]
    graph.add_node_collection(pent_nodes)
    attr = EdgeAttrs('p', flag=False)
    graph.add_p_hyperedge(pent_nodes, attr)

    node_a = Node(NodeAttrs(label='v', x=-1, y=-1, flag=False))
    node_b = Node(NodeAttrs(label='v', x=2, y=-1, flag=False))
    node_c = Node(NodeAttrs(label='v', x=2, y=0.5, flag=True))
    node_d = Node(NodeAttrs(label='v', x=2, y=2, flag=False))
    node_e = Node(NodeAttrs(label='v', x=-1, y=2, flag=False))

    sqr_nodes = [node_a, node_b, node_c, node_d, node_e]
    graph.add_node_collection(sqr_nodes)
    for pent_a, pent_b in it.pairwise(pent_nodes + [pent_nodes[0]]):
        attr = EdgeAttrs('e', flag=False)
        edge = Edge(pent_a.handle, pent_b.handle, attr)
        graph.add_edge(edge)

    for sqr_a, sqr_b in it.pairwise(sqr_nodes + [sqr_nodes[0]]):
        attr=  EdgeAttrs('e', flag=True)
        edge = Edge(sqr_a.handle, sqr_b.handle, attr)
        graph.add_edge(edge)

    for (sqr_a, sqr_b), (pent_a, pent_b) in zip(it.pairwise(sqr_nodes + [sqr_nodes[0]]), it.pairwise(pent_nodes + [pent_nodes[0]])):
        qv = [pent_a, pent_b, sqr_a, sqr_b]
        attr = EdgeAttrs('q', False)
        graph.add_q_hyperedge(qv, attr)

        attr=  EdgeAttrs('e', flag=False)
        edge = Edge(pent_a.handle, sqr_a.handle, attr)
        graph.add_edge(edge)
        
        attr=  EdgeAttrs('e', flag=False)
        edge = Edge(pent_b.handle, sqr_b.handle, attr)
        graph.add_edge(edge)

    graph.display()
    plot.set(title='...')
    fig.suptitle("Applying production 17")
    fig.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
