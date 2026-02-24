public class MainLinkedList {

    public static void main(String[] args) {
        LinkedList list = new LinkedList();
        System.out.println(list.getList());

        for (int i = 0; i < 7; i++) {
            list.append(i * 3);
            System.out.println(list.getList());
            System.out.println(list.len());
        }

        System.out.println(list.getValueByIndexInak(-2));
    }
}
