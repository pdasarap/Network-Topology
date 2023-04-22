class ShortestPath:
    shrtst_pathlist = []

    def __init__(self):
        pass

    # shortest paths from all nodes to all nodes
    def shrtstpaths_forall(self, grph):
        shrtst_paths = []
        for src in range(len(grph[0])):
            gr_len = len(grph)
            c_lst = range(len(grph[0]))

            dst = [float("Inf")] * gr_len
            prnt = [-1] * gr_len
            dst[src] = 0

            dlist = range(len(dst))
            q_lst = []

            for i in range(gr_len):
                q_lst.append(i)

            while q_lst:
                minval = float("Inf")
                minindx = -1
                for i in dlist:
                    if minval >= dst[i]:
                        if i in q_lst:
                            minval = dst[i]
                            minindx = i
                x = minindx
                q_lst.remove(x)
                for i in c_lst:
                    if grph[x][i] and i in q_lst and (dst[x] + grph[x][i] < dst[i]):
                            dst[i] = dst[x] + grph[x][i]
                            prnt[i] = x

            all_shrtst_paths = [[]*len(dst) for _ in dlist]
            for i in dlist:
                self.shrtst_pathlist = []
                self.src_to_dstn(prnt, i)
                all_shrtst_paths[i] = self.shrtst_pathlist
                
            shrtst_paths.append(all_shrtst_paths)
#             shrtst_paths.append(self.algo_djkstr(i, grph))
        return shrtst_paths



    # shortest path from source to destination
    def src_to_dstn(self, prnt, i):
        if prnt[i] == -1:
            self.shrtst_pathlist.append(i)
            return
        self.src_to_dstn(prnt, prnt[i])
        self.shrtst_pathlist.append(i)

    
