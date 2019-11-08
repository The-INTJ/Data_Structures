public class Driver {


    public static void main(String[] args) {

        Node<String> sNode = new Node("a string");

        SingularlyLinkedList sll = new SingularlyLinkedList(sNode);

        for(int i = 0; i < 10; i++) {
            if(i % 2 < 1) {
                sll.add(new Node(i));
            } else {
                sll.add(new Node((char)i));
            }
        }

        sll.printArray();

    }

}
