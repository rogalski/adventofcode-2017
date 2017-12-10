package io.github.rogalski;

import org.junit.Test;

import static org.junit.Assert.assertArrayEquals;
import static org.junit.Assert.assertEquals;


public class KnotHash2Test {

    @Test
    public void toIntInput() {
        assertArrayEquals(new int[]{49, 44, 50, 44, 51}, KnotHash2.toIntInput("1,2,3"));
    }

    @Test
    public void test1() {
        assertEquals("a2582a3a0e66e6e86e3812dcb672a272", KnotHash2.getHash(""));
    }

    @Test
    public void test2() {
        assertEquals("33efeb34ea91902bb2f59c9920caa6cd", KnotHash2.getHash("AoC 2017"));
    }

    @Test
    public void test3() {
        assertEquals("3efbe78a8d82f29979031a4aa0b16a9d", KnotHash2.getHash("1,2,3"));
    }

    @Test
    public void test4() {
        assertEquals("63960835bcdc130f0b66d7ff4f6a5a8e", KnotHash2.getHash("1,2,4"));
    }
}