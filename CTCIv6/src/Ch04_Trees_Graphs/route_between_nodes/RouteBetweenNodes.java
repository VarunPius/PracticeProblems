package Ch04_Trees_Graphs.route_between_nodes;

import java.util.*;

public class RouteBetweenNodes {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Graph g = new Graph();
	    Node[] nodes = new Node[6];
	   
	    // This graph is taken from page 107
	    nodes[0] = new Node("0");
	    nodes[1] = new Node("1");
	    nodes[2] = new Node("2");
	    nodes[3] = new Node("3");
	    nodes[4] = new Node("4");
	    nodes[5] = new Node("5");

	    nodes[0].addNeighbor(nodes[1]);
	    nodes[0].addNeighbor(nodes[4]);
	    nodes[0].addNeighbor(nodes[5]);
	    nodes[1].addNeighbor(nodes[4]);
	    nodes[1].addNeighbor(nodes[3]);
	    nodes[2].addNeighbor(nodes[1]);
	    nodes[3].addNeighbor(nodes[2]);
	    nodes[3].addNeighbor(nodes[4]);

	    //g.vertices = nodes;
	    for (int i = 0; i < nodes.length; i++){
	    	g.vertices.add(nodes[i]);
	    }
	    g.count = 6;

	    System.out.println(verifyRoute(g, nodes[0], nodes[3]));
	    System.out.println(verifyRoute(g, nodes[3], nodes[5]));

	}

	public static boolean verifyRoute(Graph g, Node start, Node end){
		if(start == end)
			return true;

		Queue<Node> q = new ArrayDeque<Node>();

		for(Node n : g.vertices){
			n.state = Node.State.Unvisited;
		}
		start.state = Node.State.Visiting;

		q.add(start);

		while(!q.isEmpty()){
			Node tmp = q.remove();

			if(tmp != null){
				for(Node n : tmp.adj){
					if(n.state == Node.State.Unvisited){
						if(n == end)
							return true;
						else{
							n.state = Node.State.Visiting;
							q.add(n);
						}
					}
				}
			}
			tmp.state = Node.State.Visited;
		}

		return false;
	}

}

/*
public static boolean search(Graph g, Node start, Node end) {
    if (start == end) return true;

    Queue<Node> queue = new ArrayDeque<Node>();

    for (Node node : g.vertices) {
      node.state = Node.State.Unvisited;
    }

    start.state = Node.State.Visiting;
    queue.add(start);
    Node temp;
    while (!queue.isEmpty()) {
      temp = queue.remove();
      if (temp != null) {
        for (Node adjacent : temp.adjacent) {
          if (adjacent.state == Node.State.Unvisited) {
            if (adjacent == end) {
              return true;
            } else {
              adjacent.state = Node.State.Visiting;
              queue.add(adjacent);
            }
          }
        }
      }
      temp.state = Node.State.Visited;
    }

    return false;
  }
	*/
