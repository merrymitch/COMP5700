'''
Created on Oct 16, 2022

@author: marymitchell
'''
import unittest
import rubik.solve as solve

#Assign the cube mapping to each of the cube faces
F00, F01, F02, F10, F11, F12, F20, F21, F22 = 0, 1, 2, 3, 4, 5, 6, 7, 8
R00, R01, R02, R10, R11, R12, R20, R21, R22 = 9, 10, 11, 12, 13, 14, 15, 16, 17
B00, B01, B02, B10, B11, B12, B20, B21, B22 = 18, 19, 20, 21, 22, 23, 24, 25, 26
L00, L01, L02, L10, L11, L12, L20, L21, L22 = 27, 28, 29, 30, 31, 32, 33, 34, 35
U00, U01, U02, U10, U11, U12, U20, U21, U22 = 36, 37, 38, 39, 40, 41, 42, 43, 44
D00, D01, D02, D10, D11, D12, D20, D21, D22 = 45, 46, 47, 48, 49, 50, 51, 52, 53

class Test(unittest.TestCase):
# 100 _solve 
#    inputs: 
#        parms:    dict; mandatory; arrives validated
#        parms['op']:    string; 'solve'; mandatory; arrives validated
#        parms['cube']:    string; len=54; [brgoyw]; 9 occurrences of each character, unique middle character; mandatory; arrives unvalidated
#    outputs:
#        side-effects:    non state changes; no external effects
#        returns:    dict
#        nominal: 
#            dict['rotations']:    string, valid rotations
#            dict['status']:    'ok'
#        abnormal: 
#            dict['status']:    'error: xxx', where xxx is a nonempty developer-selected diagnostic
#    confidence level: boundary value analysis
#
#    happy path:
#        test010: input a valid solved down layer
#        test020: input a valid cube with unsolved down layer
#
#    sad path:
#        test910: input an invalid cube (just check that output is good since _verify has been tested already)

    def test100_010ValidSolvedDownLayer(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'rygbbbbbboborrrrrrborgggggggybooooooyyyryyygywwwwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = ''
        expectedResult['status'] = 'ok'
        actualResult = solve._solve(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
    
    def test100_020ValidCubeWithUnsolvedDownLayer(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'brrybobbgwbryryyrryboggyygbgorborwoywrbgyowggowowwwowg'
        expectedResult = {}
        expectedResult['rotations'] = 'LUllUULURurLUluLUluruuRUruR'
        expectedResult['status'] = 'ok'
        actualResult = solve._solve(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test100_910InvalidCube(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwww'
        expectedResult = {}
        expectedResult['status'] = 'error: invalid cube'
        actualResult = solve._solve(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
