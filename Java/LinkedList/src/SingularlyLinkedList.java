public class SingularlyLinkedList<T> {

    private Node head;


    public SingularlyLinkedList() {
        this.head = null;
    }

    public SingularlyLinkedList(Node node) {
        this.head = node;
    }

    public void add(T data) {

        /* handles empty list */
        if(head == null) {
            Node node = new Node(data);
            this.head = node;
            return;
        }

        /* traversal of list until end to insert */
        Node curr = head;
        while(curr.getNext() != null) {
            curr = curr.getNext();
        }
        curr.setNext(new Node(data));


    }

    public void printArray() {
        Node curr = head;
        while(curr.getNext() != null) {
            System.out.print("" + curr.getData().toString() + ", ");
            curr = curr.getNext();
        }
        System.out.println(curr.getData().toString());
    }

    public String toString() {
        /* Will be used to construct string without creating new string each time */
        StringBuilder strBld = new StringBuilder();

        return "In development";
    }

    /* Recursive variations of methods above */

    public void recursiveAdd(T data) {
        if(head == null) {
            Node node = new Node(data);
            this.head = node;
            return;
        }
        wrapperRecAdd(data, this.head);
    }

    private void wrapperRecAdd(T data, Node curr) {
        if(curr.getNext() == null) {
            Node node = new Node(data);
            curr.setNext(node);
            return;
        }
        wrapperRecAdd(data, curr.getNext());
    }

}
