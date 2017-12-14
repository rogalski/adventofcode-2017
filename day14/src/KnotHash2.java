import java.util.Arrays;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class KnotHash2 {
    private static int[] ADDED_LENGTHS = new int[]{17, 31, 73, 47, 23};
    private static int NUM_ROUNDS = 64;

    public static String getHash(String input) {
        int[] lengths = IntStream.concat(Arrays.stream(toIntInput(input)), Arrays.stream(ADDED_LENGTHS)).toArray();
        return calcHash(lengths);
    }

    public static String getHash(int[] input) {
        int[] lengths = IntStream.concat(Arrays.stream(input), Arrays.stream(ADDED_LENGTHS)).toArray();
        return calcHash(lengths);
    }

    private static String calcHash(int[] lengths) {
        KnotHash roundHash = new KnotHash();
        for (int round = 0; round < NUM_ROUNDS; round++) {
            roundHash = new KnotHash(roundHash.getPosition(), roundHash.getSkipSize(), roundHash.getArray());
            roundHash.consume(lengths);
        }
        int[] sparseHash = roundHash.getArray();
        int[] denseHash = getDenseHash(sparseHash);
        return toHex(denseHash);
    }

    static public int[] toIntInput(String input) {
        return input.chars().toArray();
    }

    static public int[] getDenseHash(int[] sparseHash) {
        int[] denseHash = new int[16];
        for (int i = 0; i < 16; i++) {
            int[] block = Arrays.copyOfRange(sparseHash, 16 * i, 16 * (i + 1));
            denseHash[i] = IntStream.of(block).reduce(0, (a, b) -> a ^ b);
        }
        return denseHash;
    }

    static public String toHex(int[] hash) {
        return IntStream.of(hash).mapToObj(a -> String.format("%02x", a)).collect(Collectors.joining(""));
    }
}
