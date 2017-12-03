using System;
using System.Collections.Generic;
using System.Linq;

namespace SpiralMemory
{
    public class Memory2 : Memory
    {
        private List<uint> mem;
        public Memory2()
        {
            mem = new List<uint>();
            mem.Add(0); // First index is unused
            mem.Add(1);
        }

        public uint GetFirstBiggerThan(uint n)
        {
            while(mem.Last() < n)
            {
                RunNext();
            }
            return mem.Last();
        }

        public uint GetAt(uint n)
        {
            while (ToBeFilled() <= n)
            {
                RunNext();
            }
            mem.ForEach(Console.WriteLine);
            return mem.ElementAt((int)n);
        }

        private void RunNext()
        {
            var neighbours = Neighbours(ToBeFilled());
            var sum = (uint)neighbours.Sum(nn => mem.ElementAt((int)nn));
            mem.Add(sum);
            mem.ForEach(Console.WriteLine);
        }

        private uint ToBeFilled()
        {
            return (uint) (mem.Count());
        }

        protected static List<uint> Neighbours(uint index)
        {
            var baseCoord = GetCoord(index);
            // TODO: full LINQ
            List<Coord> neighbours = new List<Coord>();
            foreach (int dy in new int[] { -1, 0, 1 })
            {
                foreach (int dx in new int[] { -1, 0, 1 })
                {
                    neighbours.Add(new Coord(baseCoord.x + dx, baseCoord.y + dy));
                }
            }

            return neighbours.Select(c => IndexFromCoord(c)).Where(u => u < index).ToList();
        }

        protected static uint IndexFromCoord(Coord c)
        {
            var ringNumber = Math.Max(Math.Abs(c.x), Math.Abs(c.y));
            if (ringNumber == 0)
            {
                return 1;
            }
            var squareSize = (2 * ringNumber + 1);
            var lowerBound = (squareSize - 2) * (squareSize - 2) + 1;
            var upperBound = squareSize * squareSize;
            // UGLY - brute-force solution while it should be done algorithmically
            foreach (int candidate in Enumerable.Range(lowerBound, upperBound))
            {
                if (GetCoord((uint)candidate).Equals(c))
                {
                    return (uint)candidate;
                }
            }
            throw new InvalidOperationException();
        }
    }
}
