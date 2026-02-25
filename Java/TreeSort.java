public class TreeSort {

    NodeT root;

    public TreeSort() {
        root = null;
    }

    @Override
    public String toString() {
        return "TreeSort{" + "root=" + root + '}';
    }

    public void put(int value) {
        NodeT node = new NodeT(value);
        if (root == null) {
            root = node;
        } else {
            NodeT link = root;
            while (true) {
                if (value < link.getValue()) {
                    if (link.getLeft() == null) {
                        link.setLeft(node);
                        break;
                    } else {
                        link = link.getLeft();
                    }
                } else {
                    if (link.getRight() == null) {
                        link.setRight(node);
                        break;
                    } else {
                        link = link.getRight();
                    }
                }
            }
        }
    }

    private String getVetva(NodeT node) {
        if (node == null) {
            return "";
        }

        String vysledok = getVetva(node.getLeft());
        vysledok += node.getValue() + " ";
        vysledok += getVetva(node.getRight());

        return vysledok;
    }

    public String get() {
        return "[" + getVetva(root) + "]";
    }
}
