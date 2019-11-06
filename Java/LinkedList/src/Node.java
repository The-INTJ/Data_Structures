public class Node<T> {

    private T t;
    private Node next;

    public Node() {
        t = null;
        this.next = null;
    }

    public Node(T t) {
        this.t = t;
    }

    public void setData(T t) {
        this.t = t;
    }

    public void setNext(Node newNext) {
        this.next = newNext;
    }

}
