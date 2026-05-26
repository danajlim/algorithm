public class Main {
    public static void main(String[] args) {
        int weight = 13;
        double gravity = 0.165;
        double total = weight * gravity;

        System.out.printf("%d * %.6f = %.6f",weight,gravity,total);
    }
}