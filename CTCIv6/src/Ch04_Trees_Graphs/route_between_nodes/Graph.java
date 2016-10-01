package Ch04_Trees_Graphs.route_between_nodes;

import java.util.*;

public class Graph {
  public ArrayList<Node> vertices;
  public int count;

  public Graph(){
    count = 0;
    vertices = new ArrayList<Node>();
  }

  public void addNode(Node n){
    vertices.add(n);
  }

}
