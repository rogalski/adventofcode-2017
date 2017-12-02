import scala.io.Source

object FileChecksum {
  def check(resourceName: String) : Int = {
    var file = Source.fromResource(resourceName)
    file.getLines.map(s => s.split("\\s+")).map(lst => lst.map(s => s.toInt)).map(lst => lst.max - lst.min).sum
  }

  def check2(resourceName: String) : Int = {
    var file = Source.fromResource(resourceName)
    // general solution may be
    file.getLines.map(s => s.split("\\s+")).map(lst => lst.map(s => s.toInt)).map(lst => findEvenlyDivisiblePair(lst)).map(t => t._1 / t._2).sum
  }

  def findEvenlyDivisiblePair(input: Array[Int]) : Tuple2[Int, Int] = {
    for(i <- 0 until input.length){
      for(j <- (i+1) until input.length) {
        var v1 = input(i);
        var v2 = input(j);
        if (v1 > v2 && v1 % v2 == 0)
          return (v1, v2)
        else if (v2 > v1 && v2 % v1 == 0)
          return (v2, v1)
      }
    }
    return (-1, -1)
  }
}
