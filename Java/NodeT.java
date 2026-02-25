public class NodeT {

    private int value;
    private NodeT left;
    private NodeT right;

    public NodeT(int value) {
        this.value = value;
        left = null;
        right = null;
    }

    @Override
    public String toString() {
        return (
            "NodeT [value=" +
            value +
            ", left=" +
            left +
            ", right=" +
            right +
            "]"
        );
    }

    public int getValue() {
        return value;
    }

    public void setRight(NodeT right) {
        this.right = right;
    }

    public void setValue(int value) {
        this.value = value;
    }

    public void setLeft(NodeT left) {
        this.left = left;
    }

    public NodeT getRight() {
        return right;
    }

    public NodeT getLeft() {
        return left;
    }
}
