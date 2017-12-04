# File: spiral_memory_test.exs

# 1) Start ExUnit.
ExUnit.start

# 2) Create a new test module (test case) and use "ExUnit.Case".
defmodule PasphraseTest do
  # 3) Notice we pass "async: true", this runs the test case
  #    concurrently with other test cases. The individual tests
  #    within each test case are still run serially.
  use ExUnit.Case, async: true

  # 4) Use the "test" macro instead of "def" for clarity.
  test "t1_valid" do
    assert Passphrase.count_valid("test_content/t1_valid.txt") == 1
  end
  test "t1_invalid" do
    assert Passphrase.count_valid("test_content/t1_invalid.txt") == 0
  end
  test "t1_valid2" do
    assert Passphrase.count_valid("test_content/t1_valid2.txt") == 1
  end
  test "t2_valid1" do
    assert Passphrase.count_valid2("test_content/t2_valid1.txt") == 1
  end
  test "t2_valid2" do
    assert Passphrase.count_valid2("test_content/t2_valid2.txt") == 1
  end
  test "t2_valid3" do
    assert Passphrase.count_valid2("test_content/t2_valid3.txt") == 1
  end
  test "t2_invalid1" do
    assert Passphrase.count_valid2("test_content/t2_invalid1.txt") == 0
  end
  test "t2_invalid2" do
    assert Passphrase.count_valid2("test_content/t2_invalid2.txt") == 0
  end
end
