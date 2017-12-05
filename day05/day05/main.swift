//
//  main.swift
//  day05
//
//  Created by Łukasz Rogalski on 05.12.2017.
//  Copyright © 2017 Łukasz Rogalski. All rights reserved.
//
import Foundation

public func stepsNeededToJumpOut(jumpMap: [Int]) -> UInt {
    let mapSize : Int = jumpMap.count;
    var jumpMap = jumpMap  // create a copy which is mutable in local scope
    var instructionPointer : Int = 0;
    var jumpCount : UInt = 0;
    while(-1 < instructionPointer && instructionPointer < mapSize)
    {
        let toJump = jumpMap[instructionPointer];
        jumpMap[instructionPointer] = jumpMap[instructionPointer] + 1;
        instructionPointer += toJump
        jumpCount += 1
    }
    return jumpCount;
}

public func stepsNeededToJumpOut2(jumpMap: [Int]) -> UInt {
    let mapSize : Int = jumpMap.count;
    var jumpMap = jumpMap  // create a copy which is mutable in local scope
    var instructionPointer : Int = 0;
    var jumpCount : UInt = 0;
    while(-1 < instructionPointer && instructionPointer < mapSize)
    {
        let toJump = jumpMap[instructionPointer];
        jumpMap[instructionPointer] = jumpMap[instructionPointer] + (toJump >= 3 ? -1 : 1);
        instructionPointer += toJump
        jumpCount += 1
    }
    return jumpCount;
}

public func jumpMapFromFile(resourceName: String) -> [Int] {
    if let filePath = Bundle.main.path(forResource: resourceName, ofType: "txt") {
        do {
            let contents = try String(contentsOfFile: filePath)
            let lines = contents.components(separatedBy: "\n")
            return lines.map{ Int($0) }.filter{ $0 != nil }.map { $0! }  // is there an easier way?
        } catch {
            print("Exception during parsing data")  // this could have been cleaner
            return []
        }
    } else {
        print("File no found") // this also could have been cleaner
        return []
    }
}

let myJumpMap = jumpMapFromFile(resourceName: "data")
print("Part 1 solution is", stepsNeededToJumpOut(jumpMap: myJumpMap));
print("Part 2 solution is", stepsNeededToJumpOut2(jumpMap: myJumpMap));
