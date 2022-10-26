'''
Created on Sep 27, 2022

@author: marymitchell
'''
import unittest
import rubik.verify as verify

class Test(unittest.TestCase):

# 100 _isCubeValid
#    inputs:
#        parms:    dict; mandatory; arrives validated    
#        parms['cube']:    string; len=54; [brgoyw]; 9 occurrences of each character, unique middle character; mandatory; arrives unvalidated
#    outputs: 
#        side-effects:    non state changes; no external effects
#        returns:    boolean
#        nominal:    
#            boolean:    True
#        abnormal:
#            boolean:    False
#    confidence level: boundary value analysis
#
#    sad path:
#        test 910: missing 'cube' key
#        test 920: missing cube 
#        test 930: cube with invalid length
#        test 940: cube with non unique middle pieces
#        test 950: cube with colors other than 'brgoyw'
#        test 960: cube without 9 occurrences of each color
#        test 070: missing parameters
#
#    happy path:
#        test 010: nominal valid cube

    def test100_910MissingCubeKey(self):
        inputDict = {}
        expectedResult = False
        actualResult = verify._isCubeValid(inputDict)
        self.assertEquals(expectedResult, actualResult)
    
    def test100_920MissingCube(self):
        inputDict = {}
        inputDict['cube'] = None
        expectedResult = False
        actualResult = verify._isCubeValid(inputDict)
        self.assertEquals(expectedResult, actualResult)
    
    def test100_930CubeWithInvalidLength(self):
        inputDict = {}
        inputDict['cube'] = 'bbbbrrrrggggooooyyyywwww'
        expectedResult = False
        actualResult = verify._isCubeValid(inputDict)
        self.assertEquals(expectedResult, actualResult)
        
    def test100_940CubeWithNonUniqueMiddlePieces(self):
        inputDict = {}
        inputDict['cube'] = 'bbbbbbbbbrrrrbrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        expectedResult = False
        actualResult = verify._isCubeValid(inputDict)
        self.assertEquals(expectedResult, actualResult)
    
    def test100_950CubeWithColorsOtherThanBRGOYW(self):
        inputDict = {}
        inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyyaaaaaaaaa'
        expectedResult = False
        actualResult = verify._isCubeValid(inputDict)
        self.assertEquals(expectedResult, actualResult)
    
    def test100_960CubeWithout9OccurrencesOfEachColor(self):
        inputDict = {}
        inputDict['cube'] = 'bbbbbbbbrrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        expectedResult = False
        actualResult = verify._isCubeValid(inputDict)
        self.assertEquals(expectedResult, actualResult)
    
    def test100_970MissingParameters(self):
        expectedResult = False
        actualResult = verify._isCubeValid()
        self.assertEquals(expectedResult, actualResult)


    def test100_010NominalValidCube(self):
        inputDict = {}
        inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        expectedResult = True
        actualResult = verify._isCubeValid(inputDict)
        self.assertEquals(expectedResult, actualResult)

# 200 _verify
#    inputs:
#        parms:    dict; mandatory; arrives validated    
#        parms['cube']:    string; len=54; [brgoyw]; 9 occurrences of each character, unique middle character; mandatory; arrives unvalidated
#    outputs: 
#        side-effects:    non state changes; no external effects
#        returns:    dict
#        nominal:    
#            boolean:    ['status']: 'ok'
#        abnormal:
#            boolean:    ['status']: 'error: invalid cube'
#    confidence level: boundary value analysis
#
#    Note: _isValidCube has already tested most sad paths so we just need to make sure the output is correct for sad and happy cases
#
#    sad path: 
#        test 910: cube with invalid length
#
#    happy path:
#        test 010: nominal valid cube  
        
        
    def test200_910CubeWithInvalidLength(self):
        inputDict = {}
        inputDict['cube'] = 'bbbbrrrrggggooooyyyywwww'
        expectedResult = {}
        expectedResult['status'] = 'error: invalid cube'
        actualResult = verify._verify(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
    
    def test200_010NominalValidCube(self):
        inputDict = {}
        inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        expectedResult = {}
        expectedResult['status'] = 'ok'
        actualResult = verify._verify(inputDict)
        self.assertDictEqual(expectedResult, actualResult)