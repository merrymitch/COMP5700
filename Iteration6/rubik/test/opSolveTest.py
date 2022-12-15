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
#        test010: cube with solved down and middle layers and up face and up corners
#        test020: cube with solved down and middle layers and up face
#        test030: cube with solved down and middle layers and up cross
#        test040: cube with only solved down and middle layers
#        test050: cube with only a solved down layer
#        test060: cube completely unsolved
#        test070: cube completely solved
#
#    sad path:
#        test910: input an invalid cube (just check that output is good since _verify has been tested already)
    
    def test100_010CubeWithSolvedDownMiddleLayersAndUpFaceAndUpCorners(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'gogggggggobooooooobgbbbbbbbrrrrrrrrryyyyyyyyywwwwwwwww'
        expectedResult = 'gggggggggooooooooobbbbbbbbbrrrrrrrrryyyyyyyyywwwwwwwww'
        actualResult = solve._solve(inputDict)
        # Check that the rotations given result in a solved cube
        checkResult = {}
        checkResult['dir'] = actualResult.get('rotations')
        checkResult['cube'] = inputDict.get('cube')
        solvedCube = rotate._rotate(checkResult)
        self.assertEqual(expectedResult, solvedCube.get('cube'))
    
    def test100_020CubeWithSolvedDownMiddleLayersAndUpFace(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'rogrrrrrrorrgggggggbooooooobgbbbbbbbyyyyyyyyywwwwwwwww'
        expectedResult = 'rrrrrrrrrgggggggggooooooooobbbbbbbbbyyyyyyyyywwwwwwwww'
        actualResult = solve._solve(inputDict)
        # Check that the rotations given result in a solved cube
        checkResult = {}
        checkResult['dir'] = actualResult.get('rotations')
        checkResult['cube'] = inputDict.get('cube')
        solvedCube = rotate._rotate(checkResult)
        self.assertEqual(expectedResult, solvedCube.get('cube'))
        
    def test100_030CubeWithSolvedDownMiddleLayersAndUpCross(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'ooorrrrrrygyggggggrbrooooooyrybbbbbbbygyyybygwwwwwwwww'
        expectedResult = 'rrrrrrrrrgggggggggooooooooobbbbbbbbbyyyyyyyyywwwwwwwww'
        actualResult = solve._solve(inputDict)
        # Check that the rotations given result in a solved cube
        checkResult = {}
        checkResult['dir'] = actualResult.get('rotations')
        checkResult['cube'] = inputDict.get('cube')
        solvedCube = rotate._rotate(checkResult)
        self.assertEqual(expectedResult, solvedCube.get('cube'))
    
    def test100_040CubeWithOnlySolvedDownMiddleLayers(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'gyorrrrrrbybggggggrygooooooyyybbbbbbrgyryoobywwwwwwwww'
        expectedResult = 'rrrrrrrrrgggggggggooooooooobbbbbbbbbyyyyyyyyywwwwwwwww'
        actualResult = solve._solve(inputDict)
        # Check that the rotations given result in a solved cube
        checkResult = {}
        checkResult['dir'] = actualResult.get('rotations')
        checkResult['cube'] = inputDict.get('cube')
        solvedCube = rotate._rotate(checkResult)
        self.assertEqual(expectedResult, solvedCube.get('cube'))
    
    def test100_050CubeWithOnlySolvedDownLayer(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'gygyrrrrryoyygrgggbobbogoooygyrbbbbbogryyboorwwwwwwwww'
        expectedResult = 'rrrrrrrrrgggggggggooooooooobbbbbbbbbyyyyyyyyywwwwwwwww'
        actualResult = solve._solve(inputDict)
        # Check that the rotations given result in a solved cube
        checkResult = {}
        checkResult['dir'] = actualResult.get('rotations')
        checkResult['cube'] = inputDict.get('cube')
        solvedCube = rotate._rotate(checkResult)
        self.assertEqual(expectedResult, solvedCube.get('cube'))
    
    def test100_060CompletelyUnsolvedCube(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'ygyyrgrrbrwywgbrobogoworwywgrowbgroywrbbyogogbywywbgbo'
        expectedResult = 'rrrrrrrrrgggggggggooooooooobbbbbbbbbyyyyyyyyywwwwwwwww'
        actualResult = solve._solve(inputDict)
        # Check that the rotations given result in a solved cube
        checkResult = {}
        checkResult['dir'] = actualResult.get('rotations')
        checkResult['cube'] = inputDict.get('cube')
        solvedCube = rotate._rotate(checkResult)
        self.assertEqual(expectedResult, solvedCube.get('cube'))
        
    def test100_070ValidCompletelySolvedCube(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'rrrrrrrrrgggggggggooooooooobbbbbbbbbyyyyyyyyywwwwwwwww'
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