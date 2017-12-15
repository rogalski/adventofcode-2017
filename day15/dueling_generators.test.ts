import { DuelingGenerators } from './dueling_generators';

import * as mocha from 'mocha';
import * as chai from 'chai';

const expect = chai.expect;
describe('Dueling Generators spec', () => {

  it('should generate expected numbers for generator A' , () => {
    let g = DuelingGenerators.generator(16807, 65);
    for (let expected of [1092455, 1181022009, 245556042, 1744312007, 1352636452]) {
      expect(g.next().value).to.equal(expected);
    }
  });
  it('should generate expected numbers for generator B' , () => {
    let g = DuelingGenerators.generator(48271, 8921);
    for (let expected of [430625591, 1233683848, 1431495498, 137874439, 285222916]) {
      expect(g.next().value).to.equal(expected);
    }
  });
  it('should judge correctly' , () => {
    expect(DuelingGenerators.judge(1092455, 430625591)).to.equal(false);
    expect(DuelingGenerators.judge(1181022009, 1233683848)).to.equal(false);
    expect(DuelingGenerators.judge(245556042, 1431495498)).to.equal(true);
    expect(DuelingGenerators.judge(1744312007, 137874439)).to.equal(false);
    expect(DuelingGenerators.judge(1352636452, 285222916)).to.equal(false);
  });
  it('should aggregate judge scores correctly' , () => {
    expect(DuelingGenerators.duel(65, 8921, 40000000)).to.equal(588);
  }).timeout(0);
  it('should generate expected numbers for generator2 A' , () => {
    let g = DuelingGenerators.generator2(16807, 65, 4);
    for (let expected of [1352636452, 1992081072, 530830436, 1980017072, 740335192]) {
      expect(g.next().value).to.equal(expected);
    }
  });
  it('should generate expected numbers for generator2 B' , () => {
    let g = DuelingGenerators.generator2(48271, 8921, 8);
    for (let expected of [1233683848, 862516352, 1159784568, 1616057672, 412269392]) {
      expect(g.next().value).to.equal(expected);
    }
  });

});

