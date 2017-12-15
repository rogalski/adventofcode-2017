#!/usr/bin/env node
import { DuelingGenerators } from './dueling_generators';
console.log('Part 1 solution', DuelingGenerators.duel(783, 325, 40000000))
console.log('Part 2 solution', DuelingGenerators.duel2(783, 325, 5000000))
