public class TestDFIFO {
    public static void main(String[] args){
        DFIFO fifo = new DFIFO();
        System.out.println(fifo);
        fifo.put(4);
        System.out.println(fifo);
        fifo.put(7);
        System.out.println(fifo);
        fifo.put(8);
        System.out.println(fifo);
    }
}
