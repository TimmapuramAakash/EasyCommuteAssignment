import java.util.Scanner;

class Node{
	int data;
	Node left,right;
	Node(int item)  
    { 
        data = item; 
        left = right = null; 
    } 
}
public class pathSum {
	 Node root;
	 int path[] = new int[1000];
	 void pathFinder(Node node,int n,int sum, int s) {
		if (node ==null) {
			 return;
		 }
		path[n]=node.data;
		s=s+path[n];
		n=n+1;
		
		if (node.left == null && node.right == null && sum == s) 
           printPath(path,n);
        else 
        { pathFinder(node.left,  n,sum,s); 
        pathFinder(node.right,  n,sum,s); }
           
       

		
	}
private void printPath(int[] path2, int l) {
		// TODO Auto-generated method stub
	for(int i=0;i<l;i++) {
		System.out.print(path[i]+"  ");
	}
	System.out.println("\n");
	
		
	}
public static void main(String [] args) {
	 pathSum b = new pathSum();
	 b.root = new Node(10); 
     b.root.left = new Node(8); 
     b.root.right = new Node(2); 
     b.root.left.left = new Node(3); 
     b.root.left.right = new Node(5); 
     b.root.right.left = new Node(11);
     Scanner sc = new Scanner(System.in);
     System.out.println("enter the sum ");
     int sum = sc.nextInt();
     int s=0;
     /* Let us test the built tree by printing Inorder traversal */
     b.pathFinder(b.root,0,sum, s); 	     //prints paths if found else prints nothing
}

}

