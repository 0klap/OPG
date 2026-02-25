public class TreeSort {

    NodeT root;

    public TreeSort() {
        root = null;
    }

    @Override
    public String toString() {
        return "TreeSort [root=" + root + "]";
    }

    public void put(int value) {
        NodeT node = new NodeT(value);
        if (root == null) {
            root = node;
        } else {
            NodeT link = root;

            while (true) {
                if (value < link.getValue()) {
                    if (link.getRight() == null) {
                        link.setRight(node);
                        break;
                    } else {
                        link = link.getRight();
                    }
                } else {
                    if (link.getLeft() == null) {
                        link.setLeft(node);
                        break;
                    } else {
                        link = link.getRight();
                    }
                }
            }

            if (value < root.getValue()) {
                root.setLeft(node);
            } else {
                root.setRight(node);
            }
        }
    }
}
