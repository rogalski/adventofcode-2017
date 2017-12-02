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
