'''
Created on Oct 16, 2022

@author: marymitchell
'''
import unittest
import rubik.solve as solve
import rubik.rotate as rotate

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
#        test030: input a valid completely solved cube
#        test040: input a valid cube with completely solved down and middle layer
#
#    sad path:
#        test910: input an invalid cube (just check that output is good since _verify has been tested already)

    def test100_010ValidSolvedDownLayer(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'yboyrbrrrbgbogrgggrbyyogooorgoybobbbgryryogyywwwwwwwww'
        expectedResult = 'yyyrrrrrrbygggggggyyyoooooogybbbbbbboorrygobrwwwwwwwww'
        actualResult = solve._solve(inputDict)
        # Check that the rotations given result in a solved cube
        checkResult = {}
        checkResult['dir'] = actualResult.get('rotations')
        checkResult['cube'] = inputDict.get('cube')
        solvedCube = rotate._rotate(checkResult)
        self.assertEqual(expectedResult, solvedCube.get('cube'))
    
    def test100_020ValidCubeWithUnsolvedDownLayer(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'bgybrowgwrrryggorgyywyowywrgwoobowborbbryyyoggrbwwbbgo'
        expectedResult = 'rybrrrrrryyyggggggbooooooooybybbbbbbgyryyrggowwwwwwwww'
        actualResult = solve._solve(inputDict)
        # Check that the rotations given result in a solved cube
        checkResult = {}
        checkResult['dir'] = actualResult.get('rotations')
        checkResult['cube'] = inputDict.get('cube')
        solvedCube = rotate._rotate(checkResult)
        self.assertEqual(expectedResult, solvedCube.get('cube'))
        
    def test100_030ValidCompletelySolvedCube(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'rrrrrrrrrgggggggggooooooooobbbbbbbbbyyyyyyyyywwwwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = ''
        expectedResult['status'] = 'ok'
        actualResult = solve._solve(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test100_040ValidCubeWithSolvedDownAndMiddleLayers(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'rybrrrrrryyyggggggbooooooooybybbbbbbgyryyrggowwwwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = ''
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
