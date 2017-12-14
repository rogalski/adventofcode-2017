import java.lang.Long.parseLong

const val N: Int = 128

fun defragMap(input: String): Array<String> {
    return (0 until N).map { n -> KnotHash2.getHash(input + "-" + n.toString()) }.toTypedArray()
}

fun countOnesInMap(defragMap: Array<String>): Int {
    return defragMap.map { hash -> countOnes(hash) }.sum()
}

fun countOnes(hash: String): Int {
    return hash.map { c -> countOnes(c) }.sum()
}

fun countOnes(char: Char): Int {
    // this really should'nt make final solution,
    // but key, it's const time look up table, quite fast
    when (char) {
        '0' -> return 0
        '1' -> return 1
        '2' -> return 1
        '3' -> return 2
        '4' -> return 1
        '5' -> return 2
        '6' -> return 2
        '7' -> return 3
        '8' -> return 1
        '9' -> return 2
        'a' -> return 2
        'b' -> return 3
        'c' -> return 2
        'd' -> return 3
        'e' -> return 3
        'f' -> return 4
        else -> {
            throw Error(char.toString())
        }
    }
}

fun toBoard(defragMap: Array<String>): Array<IntArray> {
    val board = Array(N, { IntArray(N) })
    for ((index, row) in defragMap.withIndex()) {
        for ((index2, char) in row.withIndex()) {
            val asInt = parseLong(char.toString(), 16).toInt()
            board[index][4 * index2 + 0] = (asInt and 0b1000) shr 3
            board[index][4 * index2 + 1] = (asInt and 0b0100) shr 2
            board[index][4 * index2 + 2] = (asInt and 0b0010) shr 1
            board[index][4 * index2 + 3] = (asInt and 0b0001) shr 0
        }
    }
    return board
}

fun countAreas(board: Array<IntArray>): Int {
    // 0's are borders, 1's ane not allocated tey
    // 2+ are allocated area

    var counter = 1
    for (r in 0 until N) {
        for (c in 0 until N) {
            if (board[r][c] == 1) {
                // new unflooded area found
                counter++
                floodFill(board, r, c, 1, counter)
            }
        }
    }
    return counter - 1;
}

fun floodFill(board: Array<IntArray>, r: Int, c: Int, from: Int, to: Int) {
    // it's just 128x128, let's not care about blowing up stack right now
    if (r !in 0 until N || c !in 0 until N) {
        return
    }
    if (board[r][c] != from) {
        return
    }
    board[r][c] = to
    floodFill(board, r - 1, c, from, to)
    floodFill(board, r + 1, c, from, to)
    floodFill(board, r, c - 1, from, to)
    floodFill(board, r, c + 1, from, to)
}

fun main(args: Array<String>) {
    val defragMap = defragMap("hwlqcszp")
    println("Part 1 solution: %d".format(countOnesInMap((defragMap))))
    println("Part 2 solution: %d".format(countAreas(toBoard(defragMap))))
}
