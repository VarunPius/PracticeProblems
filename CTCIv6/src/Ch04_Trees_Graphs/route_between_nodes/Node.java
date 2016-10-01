package Ch04_Trees_Graphs.route_between_nodes;

import java.util.*;

public class Node {
  ArrayList<Node> adj;
  String vertex;
  public enum State {Unvisited, Visited, Visiting};
  public State state;

  public Node(String v){
    vertex = v;
    adj = new ArrayList<Node>();
  }

  public void addNeighbor(Node n){
    adj.add(n);
  }

  public int adjCount(){
    return adj.size();
  } 

}
