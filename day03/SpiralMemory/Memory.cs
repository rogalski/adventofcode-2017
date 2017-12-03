using System;
using System.Diagnostics;
namespace SpiralMemory
{

	public class Coord

	{
		public int x { get; set; }
		public int y { get; set; }
		public Coord(int x, int y)
		{
			this.x = x;
			this.y = y;
		}

        public override bool Equals(object obj)
        {
            return Equals(obj as Coord);
        }

        public bool Equals(Coord obj)
        {
            obj = obj as Coord;
            return obj.x == x && obj.y == y;
        }

  

    }

	public class Memory
	{
		public static Coord GetCoord(uint n)
		{
            // The idea is simple:
            // Given n, we find next "complete" square
            // Then we recalculate coordinates by going back
            // Since we know square size, it' trivial to know whether x or y is modified

            // Btw **certainly** can be computed in O(1) time, I just can't see it yet
			uint squareSize = 0;
            for (squareSize = 1; (squareSize * squareSize) < n; squareSize = squareSize + 2) {
            }
			var stepsToDecrease = (squareSize * squareSize) - n;

            var startingXY = ((int)squareSize - 1) / 2;
            var startingPoint = new Coord(startingXY, startingXY);

            // order of decreasing: Left, Up, Right, Down
			uint moveLeft = 0;
			uint moveUp = 0;
			uint moveRight = 0;
			uint moveDown = 0;

			moveLeft = Math.Min(stepsToDecrease, squareSize - 1);
			stepsToDecrease = stepsToDecrease - moveLeft;
            moveUp = Math.Min(stepsToDecrease, squareSize - 1);
			stepsToDecrease = stepsToDecrease - moveUp;
            moveRight = Math.Min(stepsToDecrease, squareSize - 1);
			stepsToDecrease = stepsToDecrease - moveRight;
            moveDown = Math.Min(stepsToDecrease, squareSize - 1);
			stepsToDecrease = stepsToDecrease - moveDown;

            Debug.Assert(stepsToDecrease == 0);

			var c = new Coord((int)(startingPoint.x - moveLeft + moveRight),
			                  (int)(startingPoint.y - moveUp + moveDown));
            return c;
		}

		public static uint ManhattanDistance(uint n)
		{
			var c = GetCoord(n);
			return (uint)(Math.Abs(c.x) + Math.Abs(c.y));
		}
	}
}
