package io.github.rogalski;

import org.junit.Test;

import static org.junit.Assert.assertArrayEquals;
import static org.junit.Assert.assertEquals;

public class KnotHashTest {

    @Test
    public void testcase() {
        KnotHash knotHash = new KnotHash(5);

        knotHash.consume(3);
        assertArrayEquals(new int[]{2, 1, 0, 3, 4}, knotHash.getArray());
        assertEquals(3, knotHash.getPosition());

        knotHash.consume(4);
        assertArrayEquals(new int[]{4, 3, 0, 1, 2}, knotHash.getArray());
        assertEquals(3, knotHash.getPosition());

        knotHash.consume(1);
        assertArrayEquals(new int[]{4, 3, 0, 1, 2}, knotHash.getArray());
        assertEquals(1, knotHash.getPosition());

        knotHash.consume(5);
        assertArrayEquals(new int[]{3, 4, 2, 1, 0}, knotHash.getArray());
        assertEquals(4, knotHash.getPosition());
    }
}