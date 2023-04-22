import plotly.express as px
import pandas as pds
import networkx as ntx
import pylab as pl


class GenGraphs:
    def __init__(self):
        pass

    # to display the scatter plot
    def scatter_plot(x_val, y_val, ttl, xlbl, ylbl):
        vals = dict(x=x_val, y=y_val)
        lbls = {xlbl: ylbl}
        df_vals = pds.DataFrame(vals)
        fgr = px.scatter(df_vals, "x", "y", title=ttl, labels=lbls)
        fgr.show()

    # to display network topology graphs
    def topology_grphs(cap_grph, n, ttl):
        gr = ntx.DiGraph()

        nlen = list(range(n))
        for i in nlen:
            for j in nlen:
                cap = cap_grph[i][j]
                if cap != 0:
                    x = str(i)
                    y = str(j)
                    gr.add_edges_from([(x, y)], weight=cap)

        edgs = dict([((m, n,), dval['weight'])
                            for m, n, dval in gr.edges(data=True)])
        node_labels = {}
        
        for i in nlen:
            x = str(i)
            node_labels[x] = x

        layout = ntx.spring_layout(gr)
        ntx.draw_networkx_edge_labels(gr, layout, edgs)
        ntx.draw_networkx_labels(gr, layout, node_labels)
        ntx.draw(gr, layout, node_size=600)

        pl.title(ttl)
        pl.show()

