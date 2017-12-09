require_relative "day09"
require "test/unit"

class TestGarbage < Test::Unit::TestCase

  def test_empty_garbage
    assert_equal("", filtered_stream("<>") )
  end
  def test_garbage_with_random_characters
    assert_equal("", filtered_stream("<random characters>") )
  end
  def test_unbalanced_garbage
    assert_equal("", filtered_stream("<<<<>") )
  end
  def test_canceled_closing_garbage
    assert_equal("", filtered_stream("<{!>}>") )
  end
  def test_double_cancel
    assert_equal("", filtered_stream("<!!>") )
  end
  def test_double_double_cancel
    assert_equal("", filtered_stream("<!!!>>") )
  end
  def test_should_close_naturally
    assert_equal("", filtered_stream("<{o\"i!a,<{i<a>") )
  end
end

class TestScore < Test::Unit::TestCase

  def test_simple
    assert_equal(1, score("{}") )
  end
  def test_nested
    assert_equal(6, score("{{{}}}") )
  end
  def test_nested_collection
    assert_equal(5, score("{{},{}}") )
  end
  def test_nesting_varies
    assert_equal(16, score("{{{},{},{{}}}}") )
  end
end

class TestCountGarbage < Test::Unit::TestCase

  def test_empty_garbage
    assert_equal(0, filter_stream_count_garbage("<>") )
  end
  def test_garbage_with_random_characters
    assert_equal(17, filter_stream_count_garbage("<random characters>") )
  end
  def test_unbalanced_garbage
    assert_equal(3, filter_stream_count_garbage("<<<<>") )
  end
  def test_canceled_closing_garbage
    assert_equal(2, filter_stream_count_garbage("<{!>}>") )
  end
  def test_double_cancel
    assert_equal(0, filter_stream_count_garbage("<!!>") )
  end
  def test_double_double_cancel
    assert_equal(0, filter_stream_count_garbage("<!!!>>") )
  end
  def test_should_close_naturally
    assert_equal(10, filter_stream_count_garbage("<{o\"i!a,<{i<a>") )
  end
end
