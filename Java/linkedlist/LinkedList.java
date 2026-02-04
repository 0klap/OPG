public class LinkedList {

    Node first;

    public LinkedList() {
        first = null;
    }

    @Override
    public String toString() {
        return "LinkedList{" + "first=" + first + "}";
    }

    public String getList() {
        if (first == null) return "[]";
        else {
            return "[" + first.getValues() + "]";
        }
    }

    public int len() {
        if (first == null) return 0;
        Node link = first;
        int count = 1;

        while (link.getNext() != null) {
            link = link.getNext();
            count++;
        }
        return count;
    }

    public int lenInak() {
        Node link = first;
        int count = 0;

        while (link != null) {
            link = link.getNext();
            count++;
        }
        return count;
    }

    public int getValueByIndexInak(int index) {
        Node link = first;
        while (link != null) {
            if (index == 0) return link.getValue();
            link = link.getNext();
            index--;
        }
        throw new IndexOutOfBoundsException("Index mimo rozsah");
    }

    public int getIndexByValue(int value) {
        Node link = first;
        int i = 0;
        while (link != null) {
            if (link.getValue() == value) return i;
            link = link.getNext();
            i++;
        }
        return -1;
    }

    public int getValueByIndex(int index) {
        Node link = first;
        int count = 0;

        if (
            this.len() < index || index < 0
        ) throw new IndexOutOfBoundsException("Index mimo rozsah");

        while (count != index) {
            link = link.getNext();
            count++;
        }
        return link.getValue();
    }

    public void append(int value) {
        Node newNode = new Node(value);

        if (first == null) first = newNode;
        else {
            Node link = first;

            while (link.getNext() != null) {
                link = link.getNext();
            }

            link.setNext(newNode);
        }
    }
}
