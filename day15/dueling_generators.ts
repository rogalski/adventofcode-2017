export namespace DuelingGenerators {
  let M = 2**31 - 1;
  let mask = 0x0000FFFF;
  export function* generator(factor, seed) {
    var val = seed;
    while (1){
      val = (val * factor) % M;
      yield val;      
    }
  }
  export function* generator2(factor, seed, multipliersOf) {
    var val = seed;
    while (1){
      val = (val * factor) % M;
      if (val % multipliersOf == 0)
        yield val;      
    }
  }
  export function judge(a, b) {
    return (a & mask) == (b & mask);
  }

  export function duel(seedA, seedB, N) {
    // I guess there is some "smart" solution and this is just a bruteforce
    // this should take generator objects on input
    let a = generator(16807, seedA);
    let b = generator(48271, seedB);
    var result = 0;
    for(var i=0; i<N; i++) {
      if (judge(a.next().value, b.next().value)) {
        result++;
      }
    }
    return result;
  }

  export function duel2(seedA, seedB, N) {
    let a = generator2(16807, seedA, 4);
    let b = generator2(48271, seedB, 8);
    var result = 0;
    for(var i=0; i<N; i++) {
      if (judge(a.next().value, b.next().value)) {
        result++;
      }
    }
    return result;
  }
}
