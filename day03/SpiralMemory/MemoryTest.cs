using NUnit.Framework;
using System;
namespace SpiralMemory
{
	[TestFixture]
	public class MemoryTest
	{
		[Test]
		public void TestMD1()
		{
			Assert.AreEqual(0, Memory.ManhattanDistance(1));
		}
		[Test]
		public void TestMD12()
		{
			Assert.AreEqual(3, Memory.ManhattanDistance(12));
		}
		[Test]
		public void TestMD23()
		{
			Assert.AreEqual(2, Memory.ManhattanDistance(23));
		}
		[Test]
		public void TestMD1024()
		{
			Assert.AreEqual(31, Memory.ManhattanDistance(1024));
		}
	}
}
