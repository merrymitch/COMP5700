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
#        test010: cube with solved down and middle layers and up cross
#        test020: cube with only solved down and middle layers
#        test030: cube with only a solved down layer
#        test040: cube completely unsolved
#        test050: cube completely solved
#        test060: cube with solved down and middle layers and up face
#
#    sad path:
#        test910: input an invalid cube (just check that output is good since _verify has been tested already)

    def test100_010CubeWithSolvedDownMiddleLayersAndUpCross(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'ooorrrrrrygyggggggrbrooooooyrybbbbbbbygyyybygwwwwwwwww'
        expectedResult = 'bogrrrrrrobrgggggggrboooooorgobbbbbbyyyyyyyyywwwwwwwww'
        actualResult = solve._solve(inputDict)
        # Check that the rotations given result in a solved cube
        checkResult = {}
        checkResult['dir'] = actualResult.get('rotations')
        checkResult['cube'] = inputDict.get('cube')
        solvedCube = rotate._rotate(checkResult)
        self.assertEqual(expectedResult, solvedCube.get('cube'))
    
    def test100_020CubeWithOnlySolvedDownMiddleLayers(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'gyorrrrrrbybggggggrygooooooyyybbbbbbrgyryoobywwwwwwwww'
        expectedResult = 'gobrrrrrrrboggggggbrgooooooogrbbbbbbyyyyyyyyywwwwwwwww'
        actualResult = solve._solve(inputDict)
        # Check that the rotations given result in a solved cube
        checkResult = {}
        checkResult['dir'] = actualResult.get('rotations')
        checkResult['cube'] = inputDict.get('cube')
        solvedCube = rotate._rotate(checkResult)
        self.assertEqual(expectedResult, solvedCube.get('cube'))
    
    def test100_030CubeWithOnlySolvedDownLayer(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'gygyrrrrryoyygrgggbobbogoooygyrbbbbbogryyboorwwwwwwwww'
        expectedResult = 'rrrrrrrrrggoggggggbbgoooooooobbbbbbbyyyyyyyyywwwwwwwww'
        actualResult = solve._solve(inputDict)
        # Check that the rotations given result in a solved cube
        checkResult = {}
        checkResult['dir'] = actualResult.get('rotations')
        checkResult['cube'] = inputDict.get('cube')
        solvedCube = rotate._rotate(checkResult)
        self.assertEqual(expectedResult, solvedCube.get('cube'))
    
    def test100_040CompletelyUnsolvedCube(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'ygyyrgrrbrwywgbrobogoworwywgrowbgroywrbbyogogbywywbgbo'
        expectedResult = 'grbrrrrrrrbgggggggooooooooobgrbbbbbbyyyyyyyyywwwwwwwww'
        actualResult = solve._solve(inputDict)
        # Check that the rotations given result in a solved cube
        checkResult = {}
        checkResult['dir'] = actualResult.get('rotations')
        checkResult['cube'] = inputDict.get('cube')
        solvedCube = rotate._rotate(checkResult)
        self.assertEqual(expectedResult, solvedCube.get('cube'))
        
    def test100_050ValidCompletelySolvedCube(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'rrrrrrrrrgggggggggooooooooobbbbbbbbbyyyyyyyyywwwwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = ''
        expectedResult['status'] = 'ok'
        actualResult = solve._solve(inputDict)
        self.assertEqual(expectedResult.get('rotations'), actualResult.get('rotations'))
        
    def test100_060ValidCubeWithSolvedDownMiddleLayersAndUpFace(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'grbrrrrrrrbgggggggooooooooobgrbbbbbbyyyyyyyyywwwwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = ''
        expectedResult['status'] = 'ok'
        actualResult = solve._solve(inputDict)
        self.assertEqual(expectedResult.get('rotations'), actualResult.get('rotations'))
        
    def test100_910InvalidCube(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwww'
        expectedResult = {}
        expectedResult['status'] = 'error: invalid cube'
        actualResult = solve._solve(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
