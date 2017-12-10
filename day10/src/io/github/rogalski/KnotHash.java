package io.github.rogalski;

import java.util.stream.IntStream;

public class KnotHash {
    private static int DEFAULT_SIZE = 256;
    private int size;
    private int position;
    private int skipSize;
    private int[] array;

    public KnotHash() {
        size = DEFAULT_SIZE;
        position = 0;
        skipSize = 0;
        initializeArray();
    }

    public KnotHash(int customSize) {
        size = customSize;
        position = 0;
        skipSize = 0;
        initializeArray();
    }

    public KnotHash(int customPosition, int customSkipSize, int[] inheritedArray) {
        size = DEFAULT_SIZE;
        position = customPosition;
        skipSize = customSkipSize;
        array = inheritedArray;
    }

    static private void reverseArray(int[] toReverse) {
        // from stack overflow
        // really, no built-in?
        for (int i = 0; i < toReverse.length / 2; i++) {
            int temp = toReverse[i];
            toReverse[i] = toReverse[toReverse.length - i - 1];
            toReverse[toReverse.length - i - 1] = temp;
        }
    }

    static private int[] copyOfRangeCircular(int[] arr, int from, int to) {
        int newLength = to - from;
        int[] copy = new int[newLength];
        for (int i = 0; i < newLength; i++) {
            copy[i] = arr[(from + i) % arr.length];
        }
        return copy;
    }

    private void initializeArray() {
        this.array = IntStream.range(0, size).toArray();
    }

    public void consume(int length) {
        assert length <= array.length;

        int[] toReverse = copyOfRangeCircular(array, position, position + length);

        reverseArray(toReverse);

        for (int i = 0; i < toReverse.length; i++) {
            array[(position + i) % array.length] = toReverse[i];
        }

        position = (position + length + skipSize) % array.length;
        skipSize += 1;
    }

    public void consume(int[] lengths) {
        for (int length : lengths) {
            consume(length);
        }
    }

    public int getPosition() {
        return position;
    }

    public int getSkipSize() {
        return skipSize;
    }

    public int[] getArray() {
        return array;
    }

}
