defmodule Passphrase do
  def count_valid(filename) do
    # accept only lines where all words are unique
    File.stream!(filename) |> Stream.map(&String.split/1) |> Stream.filter(fn lst -> length(Enum.uniq(lst)) == length(lst) end) |> Enum.count
  end
  def count_valid2(filename) do
    # reject lines that contains anagrams
    File.stream!(filename) |> Stream.map(&String.split/1) |> Stream.reject(&contains_anagrams?/1) |> Enum.count
  end
  def contains_anagrams?(lst) do
    # list of words contains anarams when sorted list of charlists are not unique
    length(Enum.uniq(Enum.map(lst, &to_charlist/1) |> Enum.map(&Enum.sort/1))) < length(lst)
  end
end
