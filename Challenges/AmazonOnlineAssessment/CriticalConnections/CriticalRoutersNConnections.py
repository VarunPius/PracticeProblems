"""
Critical Routers:
"""

"""
public class CriticalRouters {
	// Time : O(V * (V + E))
	// Space : O(V + E)
	public List<Integer> getCriticalRouters(int numNodes, int numEdges, int[][] edges) {

	    //construct graph
	    Map<Integer, Set<Integer>> graph = new HashMap<>();

	    //initialize graph
	    for(int i=0;i<numNodes;i++) graph.put(i, new HashSet<>());

	    //add edges to graph
	    for(int[] edge: edges) {
	        int u = edge[0];
	        int v = edge[1];

	        graph.get(u).add(v);
	        graph.get(v).add(u);
	    }

	    List<Integer> result = new ArrayList<>();
	    int initialConnComp = 0;
	    HashSet<Integer> visited = new HashSet<>();
        for (int src = 0; src < numNodes; src++) {
            if (!visited.contains(src)) {
            	dfs(graph, src, visited);
            	initialConnComp++;
            }
        }
        System.out.print("Graph has : " + initialConnComp + " compenent\n");
	    //calculate critical routers
	    for (int nodeToRemove=0; nodeToRemove < numNodes; nodeToRemove++) {
	    	int component = 0;
	        //remove each node and its edges and check if entire graph is connected
	        Set<Integer> nodeEdges = graph.get(nodeToRemove);
	        
	        for(int edge: nodeEdges) {
	            graph.get(edge).remove(nodeToRemove);
	        }
	        visited = new HashSet<>();
	        for (int src = 0; src < numNodes; src++) {
	            if (src != nodeToRemove && !visited.contains(src)) {
	            
	            	dfs(graph, src, visited);
	            	component++;
	            
	            }
	        }
	        if(component > initialConnComp) {
  	            //this node was a critical router
  	            result.add(nodeToRemove);
  	        }
	        //add the edges back
	        for (int edge: nodeEdges) graph.get(edge).add(nodeToRemove);
	    }
	    return result;
	}

	public void dfs (Map<Integer, Set<Integer>> graph, int source, Set<Integer> visited) {
	    if(visited.contains(source)) return;

	    visited.add(source);

	    for(int child: graph.get(source)) dfs(graph, child, visited);
	}

	public static void main(String[] args) {
	    CriticalRouters obj = new CriticalRouters();

	    int numRouters1 = 7;
	    int numLinks1 = 7;
	    int[][] links1 = {{0, 1}, {0, 2}, {1, 3}, {2, 3}, {2, 5}, {5, 6}, {3, 4}};

	    List<Integer> res = obj.getCriticalRouters(numRouters1, numLinks1, links1);

	    for(int i: res) System.out.print(i + " ");
	    System.out.println();

	    int numRouters2 = 5;
	    int numLinks2 = 5;
	    int[][] links2 = {{1,2}, {0,1}, {2,0}, {0,3}, {3,4}};

	    List<Integer> res2 = obj.getCriticalRouters(numRouters2, numLinks2, links2);
	    for(int i: res2) System.out.print(i + " ");
	    System.out.println();

	    int numRouters3 = 4;
	    int numLinks3 = 4;
	    int[][] links3 = {{0,1},{1,2},{2,3}};

	    List<Integer> res3 = obj.getCriticalRouters(numRouters3, numLinks3, links3);
	    for(int i: res3) System.out.print(i + " ");
	    System.out.println();

	    int numRouters4 = 7;
	    int numLinks4 = 8;
	    int[][] links4 = {{0,1},{0,2},{1,2},{1,3},{1,4},{1,6},{3,5},{4,5}};

	    List<Integer> res4 = obj.getCriticalRouters(numRouters4, numLinks4, links4);
	    for(int i: res4) System.out.print(i + " ");
	    System.out.println();
	    
	    int numRouters5 = 12;
	    int numLinks5 = 10;
	    int[][] links5 = {{0, 1}, {0, 2}, {1, 3}, {2, 3}, {2, 5}, {5, 6}, {3, 4}, {7, 8}, {9, 10}, {9, 11}, {7,11}, {7, 10}};

	    List<Integer> res5 = obj.getCriticalRouters(numRouters5, numLinks5, links5);
	    for(int i: res5) System.out.print(i + " ");
	    System.out.println();
	}
}
"""
"""
public List<Integer> getCriticalRouters(int numNodes, int numEdges, int[][] edges) {

    //construct graph
    Map<Integer, Set<Integer>> graph = new HashMap<>();

    //initialize graph
    for(int i=0;i<numNodes;i++) graph.put(i, new HashSet<>());

    //add edges to graph
    for(int[] edge: edges) {
        int u = edge[0];
        int v = edge[1];

        graph.get(u).add(v);
        graph.get(v).add(u);
    }

    List<Integer> result = new ArrayList<>();

    //calculate critical routers
    for(int nodeToRemove=0;nodeToRemove<numNodes;nodeToRemove++) {

        //remove each node and its edges and check if entire graph is connected
        Set<Integer> nodeEdges = graph.get(nodeToRemove);
        int source = 0;
        for(int edge: nodeEdges) {
            graph.get(edge).remove(nodeToRemove);
            source = edge;
        }

        HashSet<Integer> visited = new HashSet<>();
        dfs(graph, source, visited);

        if(visited.size()!=numNodes-1) {
            //this node was a critical router
            result.add(nodeToRemove);
        }

        //add the edges back
        for(int edge: nodeEdges) graph.get(edge).add(nodeToRemove);
    }
    return result;
}

public void dfs (Map<Integer, Set<Integer>> graph, int source, Set<Integer> visited) {
    if(visited.contains(source)) return;

    visited.add(source);

    for(int child: graph.get(source)) dfs(graph, child, visited);
}

public static void main(String[] args) {
    CriticalRouters obj = new CriticalRouters();

    int numRouters1 = 7;
    int numLinks1 = 7;
    int[][] links1 = {{0, 1}, {0, 2}, {1, 3}, {2, 3}, {2, 5}, {5, 6}, {3, 4}};

    List<Integer> res = obj.getCriticalRouters(numRouters1, numLinks1, links1);

    for(int i: res) System.out.print(i + " ");
    System.out.println();

    int numRouters2 = 5;
    int numLinks2 = 5;
    int[][] links2 = {{1,2}, {0,1}, {2,0}, {0,3}, {3,4}};

    List<Integer> res2 = obj.getCriticalRouters(numRouters2, numLinks2, links2);
    for(int i: res2) System.out.print(i + " ");
    System.out.println();

    int numRouters3 = 4;
    int numLinks3 = 4;
    int[][] links3 = {{0,1},{1,2},{2,3}};

    List<Integer> res3 = obj.getCriticalRouters(numRouters3, numLinks3, links3);
    for(int i: res3) System.out.print(i + " ");
    System.out.println();

    int numRouters4 = 7;
    int numLinks4 = 8;
    int[][] links4 = {{0,1},{0,2},{1,2},{1,3},{1,4},{1,6},{3,5},{4,5}};

    List<Integer> res4 = obj.getCriticalRouters(numRouters4, numLinks4, links4);
    for(int i: res4) System.out.print(i + " ");
    System.out.println();
}
"""

"""
Critical Connections:
"""

"""
class Solution
{    
    List<PairInt> list;
    Map<Integer, Boolean> visited;
    List<PairInt> criticalConnections(int numOfServers, int numOfConnections,
                                      List<PairInt> connections)
    {
        Map<Integer, HashSet<Integer>> adj = new HashMap<>();
        for(PairInt connection : connections){
            int u = connection.first;
            int v = connection.second;
            if(adj.get(u) == null){
                adj.put(u,new HashSet<Integer>());
            }
            adj.get(u).add(v);
            if(adj.get(v) == null){
                adj.put(v,new HashSet<Integer>());
            }
            adj.get(v).add(u);
        }
       
        list = new ArrayList<>();
        for(int i =0;i<numOfConnections;i++){
            visited = new HashMap<>();
            PairInt p = connections.get(i);
            int x = p.first;
            int y = p.second;
            adj.get(x).remove(y);
            adj.get(y).remove(x);
            DFS(adj,1);
            if(visited.size()!=numOfServers){
                    if(p.first > p.second)
                        list.add(new PairInt(p.second,p.first));
                    else
                        list.add(p);
            }
            adj.get(x).add(y);
            adj.get(y).add(x);
        }
        return list;
    }
   
    public void DFS(Map<Integer, HashSet<Integer>> adj, int u){
        visited.put(u, true);
        if(adj.get(u).size()!=0){
            for(int v : adj.get(u)){
                if(visited.getOrDefault(v, false)== false){
                    DFS(adj,v);
                }
            }
        }
    }
}
"""

