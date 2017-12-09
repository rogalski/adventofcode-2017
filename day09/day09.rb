def new_state(previous_state, character)
  case previous_state
  when :STATE_COLLECTING
    case character
    when "<"
      return :STATE_GARBAGE
    when "!"
      return :STATE_IGNORING_COLLECTING
    else
      return :STATE_COLLECTING
    end
  when :STATE_GARBAGE
    case character
    when ">"
      return :STATE_COLLECTING
    when "!"
      return :STATE_IGNORING_GARBAGE
    else
      return :STATE_GARBAGE
    end
  when :STATE_IGNORING_COLLECTING
    return :STATE_COLLECTING
  when :STATE_IGNORING_GARBAGE
    return :STATE_GARBAGE
  end
end

def should_accept_char?(old_state, new_state)
  return old_state == :STATE_COLLECTING && new_state == :STATE_COLLECTING
end

def should_count_garbage_char?(old_state, new_state)
  return old_state == :STATE_GARBAGE && new_state == :STATE_GARBAGE
end

def filtered_stream(stream)
  filtered = Array.new
  old_state = :STATE_COLLECTING
  stream.each_char do |char|
    state = new_state(old_state, char)
    if should_accept_char?(old_state, state)
      filtered << char
    end
    old_state = state
  end
  return filtered.join("")
end

def filter_stream_count_garbage(stream)
  counter = 0
  old_state = :STATE_COLLECTING
  stream.each_char do |char|
    state = new_state(old_state, char)
    if should_count_garbage_char?(old_state, state)
      counter += 1
    end
    old_state = state
  end
  return counter
end

def score(filtered_stream)
  nesting = 0
  total = 0
  filtered_stream.each_char do |char|
    if char == '{'
      nesting += 1
    end
    if char == '}'
      total += nesting
      nesting -= 1
    end
  end
  fail if nesting != 0
  return total
end

puts "Part 1 solution:", score(filtered_stream(File.read("data.txt")))
puts "Part 2 solution:", filter_stream_count_garbage(File.read("data.txt"))
