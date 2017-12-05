//
//  day05_tests.swift
//  day05_tests
//
//  Created by Łukasz Rogalski on 05.12.2017.
//  Copyright © 2017 Łukasz Rogalski. All rights reserved.
//

import XCTest

class day05_tests: XCTestCase {
    func test_jump() {
        let input : [Int] = [0, 3, 0, 1, -3]
        let expected : UInt = 5;
        let result = stepsNeededToJumpOut(jumpMap: input);
        XCTAssertEqual(expected, result)
    }
    func test_jump2() {
        let input : [Int] = [0, 3, 0, 1, -3]
        let expected : UInt = 10;
        let result = stepsNeededToJumpOut2(jumpMap: input);
        XCTAssertEqual(expected, result)
    }
}
