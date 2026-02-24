public class DFIFO {
    private Node head;
    private Node tail;


    public DFIFO() {
        head = null;
        tail = null;
    }

    @Override
    public String toString() {
        return "DynamickeFifo{" +
                "head=" + head +
                ", tail=" + tail +
                '}';
    }

    public void put(int value) {
        Node newNode = new Node(value);
        if (head == null) head = newNode;
        else tail.setNext(newNode);
        tail = newNode;
    }

    public int get() {
        if (head == null ) {
            System.out.println("Fifo je prazdne");
            return -1;
        }
        else {
            int value = head.getValue();
            head = head.getNext();
            if (head == null) tail = null;
            return value;
        }
    }
}
