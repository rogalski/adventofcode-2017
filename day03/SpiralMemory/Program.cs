using System;

namespace SpiralMemory
{
	class MainClass
	{
		public static void Main(string[] args)
		{
            Console.WriteLine("Part 1 solution: ");
            Console.WriteLine(Memory.ManhattanDistance(312051));
            Console.WriteLine("Part 2 solution: ");
            Console.WriteLine(new Memory2().GetFirstBiggerThan(312051));
		}
	}
}
