# adventofcode-2017
See [adventofcode.com/2017](http://adventofcode.com/2017) for details.

Last year idea was to do everything in Python.
This year it'll be something different - I'd attempt to play around with multiple languages.
We'll see how it goes. Also, I'll try to keep a small journal with my observations (see below).

## Day 1
Yay, first code in Rust for me!

Part 1:
Honestly, not knowing language feels weird.

I believe that it may (and should) be solved in a much cleaner (e.g. by ziping two iterators). This code feels more like first programming classes ever taken. Well, at least we have tests.

Part 2:
Somewhat trivial after having first one implemented. Still, smart second iterator build according to as rules and ziping those iterators feels like more natural solution.

Remarks:
- `rustc` and `cargo` are really great with their suggestion and ease of running tests.
- After working for so long with high-level languages I kind of forgot about essentials that are emphasised in Rust (e.g. borrowing). I have to work a little bit on that.


## Day 2
Let's go with Scala. For some reason I feel like solution in functional paradigm should be somewhat concise. I started with [official tutorial](https://www.scala-lang.org/documentation/getting-started-sbt-track/getting-started-with-scala-and-sbt-on-the-command-line.html).

Part 1: Quite easy.

Part 2: Well, writing O(n^2) time and O(n) space solution hurts a little bit. I wonder whether it could be optimized.

Remarks:
- SBT is nice, but still it's quite a lot of overhead for such simple code.

## Day 3
Implementation in `C#`. Overall - I'm really not happy with outcome. It feels like there is some straightforward solution based purely on mathematical formula behind spiral layout. My implementation looks clumsy and not that great. Part 2 is essentially brute-forced (finding neighbors based in (x, y) coordinates).

Well, let's ship it and move on to the next one.

## Day 4
After reading first problem statement, I knew for sure that some functional language would be the best. Elixir was picked because it was high on list of languages to try (and, well, it's not my first attempt at writing it).

Some remarks:
- There seems like I wrongly have not used `mix` to generate app layout. Figuring out a simple stuff like "what is an entry point for my app" took me a lot of time. Also, without `mix` I have to compile and run tests and run main in multiple steps. Is there an easier way?
- Functional languages are cool, but currently I really need to focus in terms of thinking about functions and lists. It's not very easy, when daily job is done mostly in OOO / procedural style (but Python experience helps a lot).
- Arity notation is somewhat unexpected, I strongly prefer Python's notation of optional keyword arguments.
- File-based API was not a good decision. Function called `is_line_valid` and `is_line_valid2` would be better.

## Day 5
Swift - meh, nothing really exciting. Syntax is brief and concise, but I still cannot put my finger around Apple's IDE - I _think_ it just abstracts too much.

Problem was quite trivial and easily testable, both first and second version of it.

## Day 6
C++ - not a bad one, still really verbose language comparing to all previous ones (except C# of course). Implementation is quite straightforward, but it took me some time to complete it. As always - most of time was spent on Googling and Stack Overflowing for doing simple stuff is language I'm currently using.

- those non-const-time searching for vector in vectors still bothers me a little bit
- there are certainly better data types to do the job more efficiently,
- I know there should be some well-structures unit tests, but oh well... Quick test in main was good enough.

Compile with:
```
clang -std=c++14 -Wall -Werror -lstdc++ day06.cpp -o day06
```
