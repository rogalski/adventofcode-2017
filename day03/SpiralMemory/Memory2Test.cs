using NUnit.Framework;
using System;
namespace SpiralMemory
{
    [TestFixture]
    public class Memory2Test
    {
        [Test]
        public void TestM2()
        {
            var m2 = new Memory2();
            Assert.AreEqual(1, m2.GetAt(1));
            Assert.AreEqual(1, m2.GetAt(2));
            Assert.AreEqual(2, m2.GetAt(3));
            Assert.AreEqual(26, m2.GetAt(10));
            Assert.AreEqual(330, m2.GetAt(19));
            Assert.AreEqual(362, m2.GetAt(21));
        }
    }
}
