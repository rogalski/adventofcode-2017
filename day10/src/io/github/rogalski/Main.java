package io.github.rogalski;

public class Main {

    public static void main(String[] args) {
        KnotHash part1 = new KnotHash();
        part1.consume(new int[]{183, 0, 31, 146, 254, 240, 223, 150, 2, 206, 161, 1, 255, 232, 199, 88});
        System.out.format("Part 1 solution is %d\n", multiplyFirstTwoValues(part1));
        System.out.format("Part 2 solution is %s\n", KnotHash2.getHash("183,0,31,146,254,240,223,150,2,206,161,1,255,232,199,88"));
    }

    static int multiplyFirstTwoValues(KnotHash h) {
        int[] arr = h.getArray();
        return arr[0] * arr[1];
    }
}
