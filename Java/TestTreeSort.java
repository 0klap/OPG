public class TestTreeSort {

    public static void main(String[] args) {
        TreeSort treeSort = new TreeSort();
        System.out.println(treeSort);
        treeSort.put(7);
        System.out.println(treeSort);
        treeSort.put(6);
        System.out.println(treeSort);
        treeSort.put(9);
        System.out.println(treeSort);
        treeSort.put(8);
        System.out.println(treeSort);
        treeSort.put(6);
        System.out.println(treeSort);
        treeSort.put(1);
        System.out.println(treeSort);
        treeSort.put(2);
        System.out.println(treeSort);

        System.out.println(treeSort.get());
    }
}
