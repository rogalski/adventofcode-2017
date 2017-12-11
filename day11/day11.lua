-- using "flat-topped axial coordinates", see link below for details
-- https://www.redblobgames.com/grids/hexagons/#coordinates-axial

function readInput(filename)
    local f = assert(io.open(filename, "rb"))
    local content = f:read("*all")
    f:close()
    return content
end

function finalCoord(input)
  local actions = {
    ["n"] = function (x, y) return x, y-1 end,
    ["ne"] = function (x, y) return x+1, y-1 end,
    ["se"] = function (x, y) return x+1, y end,
    ["s"] = function (x, y) return x, y+1 end,
    ["sw"] = function (x, y) return x-1, y+1 end,
    ["nw"] = function (x, y) return x-1, y end,
  }

  local x = 0;
  local y = 0;
  for adj in string.gmatch(input, "%a+") do
      local f = actions[adj];
      x, y = f(x, y);
  end
  return x, y;
end

function maxStepsFrom0(input)
  local actions = {
    ["n"] = function (x, y) return x, y-1 end,
    ["ne"] = function (x, y) return x+1, y-1 end,
    ["se"] = function (x, y) return x+1, y end,
    ["s"] = function (x, y) return x, y+1 end,
    ["sw"] = function (x, y) return x-1, y+1 end,
    ["nw"] = function (x, y) return x-1, y end,
  }

  local x = 0;
  local y = 0;
  local maxStepsFrom0 = 0;
  for adj in string.gmatch(input, "%a+") do
      local f = actions[adj];
      x, y = f(x, y);
      if stepsFrom0(x, y) > maxStepsFrom0 then
        maxStepsFrom0 = stepsFrom0(x, y);
      end
  end
  return maxStepsFrom0;
end

function stepsFrom0(x, y)
  -- our coordinate system guarantees that, it's preety cool
  return math.max(math.abs(x), math.abs(y))
end

-- tests
assert(stepsFrom0(finalCoord('ne,ne,ne')) == 3)
assert(stepsFrom0(finalCoord('ne,ne,sw,sw')) == 0)
assert(stepsFrom0(finalCoord('ne,ne,s,s')) == 2)
assert(stepsFrom0(finalCoord('se,sw,se,sw,sw')) == 3)

-- solution
print("Solution to part 1 is", stepsFrom0(finalCoord(readInput("data.txt"))))
print("Solution to part 2 is", maxStepsFrom0(readInput("data.txt")))
