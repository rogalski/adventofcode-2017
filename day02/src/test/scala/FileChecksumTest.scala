import org.scalatest.FunSuite

class FileChecksumTest extends FunSuite {
  test("FileChecksum.check") {
    assert(FileChecksum.check("tc.txt") == 18)
  }

  test("FileChecksum.check2") {
    assert(FileChecksum.check2("tc2.txt") == 9)
  }
}
