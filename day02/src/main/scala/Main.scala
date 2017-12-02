object Main extends App {
  println("Advent of code 2017, Day 2.")
  var part1Result = FileChecksum.check("data.txt")
  println(s"Part 1 solution: $part1Result")
  var part2Result = FileChecksum.check2("data.txt")
  println(s"Part 2 solution: $part2Result")
}
