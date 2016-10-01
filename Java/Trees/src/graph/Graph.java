package graph;

import java.util.*;

public class Graph {

	private int v;
	private LinkedList<Integer>[] adj;

	public Graph(int v){
		this.v = v;
		adj = new LinkedList[v];
		for(int i = 0; i < v; i++){
			adj[i] = new LinkedList<Integer>();
		}
	}

	public void addEdge(int a, int b){
		adj[a].add(b);
	}

	public void bfs(int u){
		boolean[] visited = new boolean[v];

		visited[u] = true;

		LinkedList<Integer> queue = new LinkedList<Integer>();

		queue.add(u);

		while(queue.size() != 0){
			int s = queue.removeFirst();
			visited[s] = true;
			System.out.println(s + " ");

			Iterator<Integer> i = adj[s].listIterator();

			while(i.hasNext()){
				int r = i.next();
				if(!visited[r]){
					queue.add(r);
				}
			}

		}
	}

	public void dfs(int u){
		boolean visited[] = new boolean[v];

		dfsutil(u, visited);
	}

	public void dfsutil(int u, boolean[] visited){
		visited[u] = true;
		System.out.println(u+" ");

		Iterator<Integer> i = adj[u].listIterator();
		while(i.hasNext()){
			int n = i.next();

			if(!visited[n]){
				dfsutil(n, visited);
			}
		}
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Graph g = new Graph(4);

		g.addEdge(0, 1);
		g.addEdge(0, 2);
		g.addEdge(1, 2);
		g.addEdge(2, 0);
		g.addEdge(2, 3);
		g.addEdge(3, 3);

		System.out.println("Following is Breadth First Traversal "+
											 "(starting from vertex 2)");

		//g.bfs(2);
		g.dfs(2);
	}

}


/*
// Java program to print BFS traversal from a given source vertex.
// BFS(int s) traverses vertices reachable from s.
import java.io.*;
import java.util.*;

// This class represents a directed graph using adjacency list
// representation
class Graph
{
    private int V;   // No. of vertices
    private LinkedList<Integer> adj[]; //Adjacency Lists

    // Constructor
    Graph(int v)
    {
        V = v;
        adj = new LinkedList[v];
        for (int i=0; i<v; ++i)
            adj[i] = new LinkedList();
    }

    // Function to add an edge into the graph
    void addEdge(int v,int w)
    {
        adj[v].add(w);
    }

    // prints BFS traversal from a given source s
    void BFS(int s)
    {
        // Mark all the vertices as not visited(By default
        // set as false)
        boolean visited[] = new boolean[V];

        // Create a queue for BFS
        LinkedList<Integer> queue = new LinkedList<Integer>();

        // Mark the current node as visited and enqueue it
        visited[s]=true;
        queue.add(s);

        while (queue.size() != 0)
        {
            // Dequeue a vertex from queue and print it
            s = queue.poll();
            System.out.print(s+" ");

            // Get all adjacent vertices of the dequeued vertex s
            // If a adjacent has not been visited, then mark it
            // visited and enqueue it
            Iterator<Integer> i = adj[s].listIterator();
            while (i.hasNext())
            {
                int n = i.next();
                if (!visited[n])
                {
                    visited[n] = true;
                    queue.add(n);
                }
            }
        }
    }

		void DFSUtil(int v,boolean visited[])
    {
        // Mark the current node as visited and print it
        visited[v] = true;
        System.out.print(v+" ");

        // Recur for all the vertices adjacent to this vertex
        Iterator<Integer> i = adj[v].listIterator();
        while (i.hasNext())
        {
            int n = i.next();
            if (!visited[n])
                DFSUtil(n, visited);
        }
    }

    // The function to do DFS traversal. It uses recursive DFSUtil()
    void DFS(int v)
    {
        // Mark all the vertices as not visited(set as
        // false by default in java)
        boolean visited[] = new boolean[V];

        // Call the recursive helper function to print DFS traversal
        DFSUtil(v, visited);
    }



    // Driver method to
    public static void main(String args[])
    {
        Graph g = new Graph(4);

        g.addEdge(0, 1);
        g.addEdge(0, 2);
        g.addEdge(1, 2);
        g.addEdge(2, 0);
        g.addEdge(2, 3);
        g.addEdge(3, 3);

        System.out.println("Following is Breadth First Traversal "+
                           "(starting from vertex 2)");

        g.BFS(2);
    }
}
// This code is contributed by Aakash Hasija
*/