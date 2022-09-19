'''
Created on Sep 3, 2022

@author: marymitchell
'''
import unittest
import rubik.rotate as rotate 

class RotateTest(unittest.TestCase):

# 100 _rotate 
#    inputs: 
#        parms:    dict; mandatory; arrives validated
#        parms['op']:    string; 'rotate'; mandatory; arrives validated
#        parms['cube']:    string; len=54; [brgoyw]; 9 occurrences of each character, unique middle character; mandatory; arrives unvalidated
#        parms['dir']:    string; len .GE. 0; [FfRrBbLlUuDd]; optional, defaulting to F if missing; arrives unvalidated
#    outputs:
#        side-effects:    non state changes; no external effects
#        returns:    dict
#        nominal: 
#            dict['cube']:    string, valid cube
#            dict['status']:    'ok'
#        abnormal: 
#            dict['status']:    'error: xxx', where xxx is a nonempty developer-selected diagnostic
#    confidence level: boundary value analysis
#    
#    (Many other test cases are found in other functions that check for validity)
#
#    happy path:
#        test 010: nominal valid cube with F rotation
#        test 020: nominal valid cube with f rotation
#        test 030: nominal valid cube with missing rotation
#        test 040: nominal valid cube with "" rotation
#        test 050: nominal valid cube with missing 'dir' key
#
#    sad path: 
#        test 910: missing cube with valid rotation
#        test 920: valid cube with invalid rotation 

    def test100_010NominalValidCubeWithFRotation(self):
        inputDict = {}
        inputDict['op'] = 'rotate'
        inputDict['dir'] = 'F'
        inputDict['cube'] = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        expectedResult = {}
        expectedResult['cube'] = 'gggggggggwrrwrrwrrbbbbbbbbbooyooyooywwwwwwooorrryyyyyy'
        expectedResult['status'] = 'ok'
        actualResult = rotate._rotate(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
    
    def test100_020NominalValidCubeWithFRotation(self):
        inputDict = {}
        inputDict['op'] = 'rotate'
        inputDict['dir'] = 'f'
        inputDict['cube'] = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        expectedResult = {}
        expectedResult['cube'] = 'gggggggggyrryrryrrbbbbbbbbboowoowoowwwwwwwrrroooyyyyyy'
        expectedResult['status'] = 'ok'
        actualResult = rotate._rotate(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test100_030NominalValidCubeWithMissingRotation(self):
        inputDict = {}
        inputDict['op'] = 'rotate'
        inputDict['dir'] = None
        inputDict['cube'] = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        expectedResult = {}
        expectedResult['cube'] = 'gggggggggwrrwrrwrrbbbbbbbbbooyooyooywwwwwwooorrryyyyyy'
        expectedResult['status'] = 'ok'
        actualResult = rotate._rotate(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test100_040NominalValidCubeWithEmptyRotation(self):
        inputDict = {}
        inputDict['op'] = 'rotate'
        inputDict['dir'] = ""
        inputDict['cube'] = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        expectedResult = {}
        expectedResult['cube'] = 'gggggggggwrrwrrwrrbbbbbbbbbooyooyooywwwwwwooorrryyyyyy'
        expectedResult['status'] = 'ok'
        actualResult = rotate._rotate(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test100_050NominalValidCubeWithMissingDirKey(self):
        inputDict = {}
        inputDict['op'] = 'rotate'
        inputDict['cube'] = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        expectedResult = {}
        expectedResult['cube'] = 'gggggggggwrrwrrwrrbbbbbbbbbooyooyooywwwwwwooorrryyyyyy'
        expectedResult['status'] = 'ok'
        actualResult = rotate._rotate(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test100_910MissingCubeWithValidRotation(self):
        inputDict = {}
        inputDict['op'] = 'rotate'
        inputDict['dir'] = 'uDrF'
        inputDict['cube'] = ""
        expectedResult = {}
        expectedResult['status'] = 'error: invalid cube'
        actualResult = rotate._rotate(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test100_920ValidCubeWithInvalidRotation(self):
        inputDict = {}
        inputDict['op'] = 'rotate'
        inputDict['dir'] = 'FfRa'
        inputDict['cube'] = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        expectedResult = {}
        expectedResult['status'] = 'error: invalid rotation'
        actualResult = rotate._rotate(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
# 200 isCubeValid
#    inputs:
#        parms:    dict; mandatory; arrives validated    
#        parms['cube']:    string; len=54; [brgoyw]; 9 occurrences of each character, unique middle character; mandatory; arrives unvalidated
#    outputs: 
#        side-effects:    non state changes; no external effects
#        returns:    boolean
#        nominal:    
#            boolean:    true
#        abnormal:
#            boolean:    false
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

    def test200_910MissingCubeKey(self):
        inputDict = {}
        expectedResult = False
        actualResult = rotate._isCubeValid(inputDict)
        self.assertEquals(expectedResult, actualResult)
    
    def test200_920MissingCube(self):
        inputDict = {}
        inputDict['cube'] = None
        expectedResult = False
        actualResult = rotate._isCubeValid(inputDict)
        self.assertEquals(expectedResult, actualResult)
    
    def test200_930CubeWithInvalidLength(self):
        inputDict = {}
        inputDict['cube'] = 'bbbbrrrrggggooooyyyywwww'
        expectedResult = False
        actualResult = rotate._isCubeValid(inputDict)
        self.assertEquals(expectedResult, actualResult)
        
    def test200_940CubeWithNonUniqueMiddlePieces(self):
        inputDict = {}
        inputDict['cube'] = 'bbbbbbbbbrrrrbrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        expectedResult = False
        actualResult = rotate._isCubeValid(inputDict)
        self.assertEquals(expectedResult, actualResult)
    
    def test200_950CubeWithColorsOtherThanBRGOYW(self):
        inputDict = {}
        inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyyaaaaaaaaa'
        expectedResult = False
        actualResult = rotate._isCubeValid(inputDict)
        self.assertEquals(expectedResult, actualResult)
    
    def test200_960CubeWithout9OccurrencesOfEachColor(self):
        inputDict = {}
        inputDict['cube'] = 'bbbbbbbbrrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        expectedResult = False
        actualResult = rotate._isCubeValid(inputDict)
        self.assertEquals(expectedResult, actualResult)
    
    def test200_970MissingParameters(self):
        expectedResult = False
        actualResult = rotate._isCubeValid()
        self.assertEquals(expectedResult, actualResult)


    def test200_010NominalValidCube(self):
        inputDict = {}
        inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        expectedResult = True
        actualResult = rotate._isCubeValid(inputDict)
        self.assertEquals(expectedResult, actualResult)
        
    
# 300 isDirValid
#    inputs:
#        parms:    dict; mandatory; arrives validated  
#        parms['dir']:    string; len .GE. 0; [FfRrBbLlUuDd]; optional, defaulting to F if missing; arrives unvalidated        
#    outputs: 
#        side-effects:    non state changes; no external effects
#        returns:    boolean
#        nominal:    
#            boolean:    true
#        abnormal:
#            boolean:    false
#    confidence level: boundary value analysis
#
#    happy path:
#        test010: missing 'dir' key
#        test020: nominal dir value with None value
#        test030: nominal dir value with empty value
#        test040: nominal dir value with len greater than 0
#
#    sad path:
#        test910: 'dir' value with invalid char(s)
#        test920: no parameters

    def test300_010MissingDirKey(self):
        inputDict = {}
        expectedResult = True
        actualResult = rotate._isDirValid(inputDict)
        self.assertEquals(expectedResult, actualResult)
        
    def test300_020NominalDirWithNoneValue(self):
        inputDict = {}
        inputDict['dir'] = None  
        expectedResult = True
        actualResult = rotate._isDirValid(inputDict)
        self.assertEquals(expectedResult, actualResult)
     
    def test300_030NominalDirWithEmptyValue(self):
        inputDict = {}
        inputDict['dir'] = "" 
        expectedResult = True
        actualResult = rotate._isDirValid(inputDict)
        self.assertEquals(expectedResult, actualResult)
        
    def test300_040NominalDirWithLenGreaterThan0(self): 
        inputDict = {}
        inputDict['dir'] = 'FuDl'
        expectedResult = True
        actualResult = rotate._isDirValid(inputDict)
        self.assertEquals(expectedResult, actualResult)
        
    def test300_910DirValueWithInvalidCharacters(self):
        inputDict = {}
        inputDict['dir'] = 'FuDAz'
        expectedResult = False
        actualResult = rotate._isDirValid(inputDict)
        self.assertEquals(expectedResult, actualResult)
        
    def test300_920MissingParameters(self):
        expectedResult = True
        actualResult = rotate._isDirValid()
        self.assertEquals(expectedResult, actualResult)
        
# 400 rotateCube
#    inputs:
#        parms:    strings; mandatory; arrives validated  
#        dir:    string; len .GE. 1; [FfRrBbLlUuDd]; mandatory; arrives validated
#        cube:    string; len=54; [brgoyw]; 9 occurrences of each character, unique middle character; mandatory; arrives validated
#    outputs: 
#        side-effects:    non state changes; no external effects
#        returns:    dict
#        nominal:    
#            dict['cube']
#    confidence level: boundary value analysis
#
#    (Only called by _rotate so everything is going to arrive validated bc of the two previous functions)
#
#    happy path:
#        test010: nominal valid dir and cube with clockwise rotation
#        test020: nominal valid dir and cube with counterclockwise rotation
#        test030: nominal valid dir and cube with multiple rotations

    def test400_010NominalDirAndCubeWithClockwiseRotation(self):
        inputDir = 'F'
        inputCube = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        expectedResult = {}
        expectedResult['cube'] = 'gggggggggwrrwrrwrrbbbbbbbbbooyooyooywwwwwwooorrryyyyyy'
        actualResult = rotate._rotateCube(inputDir, inputCube)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test400_020NominalDirAndCubeWithCounterClockwiseRotation(self):
        inputDir = 'f'
        inputCube = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        expectedResult = {}
        expectedResult['cube'] = 'gggggggggyrryrryrrbbbbbbbbboowoowoowwwwwwwrrroooyyyyyy'
        actualResult = rotate._rotateCube(inputDir, inputCube)
        self.assertDictEqual(expectedResult, actualResult)
    
    def test400_030NominalDirAndCubeWithMultipleRotations(self):
        inputDir = 'uLLULBBDDRRuRDfdLLBBLLuBBDDBBu'
        inputCube = 'ooyrbwbbwgyoororbowbrggwwrybwygoggorwwbrygbboyygywrryg'
        expectedResult = {}
        expectedResult['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        actualResult = rotate._rotateCube(inputDir, inputCube)
        self.assertDictEqual(expectedResult, actualResult)

# 500 rotateFrontClockwise
#    inputs:
#        parms:    strings; mandatory; arrives validated  
#        cube:    string; len=54; [brgoyw]; 9 occurrences of each character, unique middle character; mandatory; arrives validated
#    outputs: 
#        side-effects:    non state changes; no external effects
#        returns:    dict
#        nominal:    
#            dict['cube']
#    confidence level: boundary value analysis
#    
#    happy path:
#        test010: nominal valid dir and cube with front clockwise rotation    
#
#    (Only called by rotateCube so everything is going to arrive validated bc of the two validate functions)       

    def test500_010NominalParmsWithFrontClockwiseRotation(self):
        inputCube = 'yooygwwywworbybgybyyrrbgobgwwgrwgyrrgobgrgrwbbboworooy'
        expectedResult = {}
        expectedResult['cube'] = 'wyyygowwororwybbybyyrrbgobgwwbrwbyrogobgrgrgggbwworooy'
        actualResult = rotate._rotateFrontClockwise(inputCube)
        self.assertDictEqual(expectedResult, actualResult)
        
# 600 rotateFrontCounterClockwise
#    inputs:
#        parms:    strings; mandatory; arrives validated  
#        cube:    string; len=54; [brgoyw]; 9 occurrences of each character, unique middle character; mandatory; arrives validated
#    outputs: 
#        side-effects:    non state changes; no external effects
#        returns:    dict
#        nominal:    
#            dict['cube']
#    confidence level: boundary value analysis
#    
#    happy path:
#        test010: nominal valid dir and cube with front counterclockwise rotation    
#
#    (Only called by rotateCube so everything is going to arrive validated bc of the two validate functions)       

    def test600_010NominalParmsWithFrontCounterClockwiseRotation(self):
        inputCube = 'yooygwwywworbybgybyyrrbgobgwwgrwgyrrgobgrgrwbbboworooy'
        expectedResult = {}
        expectedResult['cube'] = 'owwogyyywoorbybbybyyrrbgobgwwbrwwyrrgobgrgwbgggrworooy'
        actualResult = rotate._rotateFrontCounterClockwise(inputCube)
        self.assertDictEqual(expectedResult, actualResult)      

# 700 rotateRightClockwise
#    inputs:
#        parms:    strings; mandatory; arrives validated  
#        cube:    string; len=54; [brgoyw]; 9 occurrences of each character, unique middle character; mandatory; arrives validated
#    outputs: 
#        side-effects:    non state changes; no external effects
#        returns:    dict
#        nominal:    
#            dict['cube']
#    confidence level: boundary value analysis
#    
#    happy path:
#        test010: nominal valid dir and cube with right clockwise rotation    
#
#    (Only called by rotateCube so everything is going to arrive validated bc of the two validate functions)       

    def test700_010NominalParmsWithRightClockwiseRotation(self):
        inputCube = 'yooygwwywworbybgybyyrrbgobgwwgrwgyrrgobgrgrwbbboworooy'
        expectedResult = {}
        expectedResult['cube'] = 'yooygrwyygbwyyobbrbyrgbgbbgwwgrwgyrrgoogrwrwwbboworooy'
        actualResult = rotate._rotateRightClockwise(inputCube)
        self.assertDictEqual(expectedResult, actualResult)      
        
# 800 rotateRightCounterClockwise
#    inputs:
#        parms:    strings; mandatory; arrives validated  
#        cube:    string; len=54; [brgoyw]; 9 occurrences of each character, unique middle character; mandatory; arrives validated
#    outputs: 
#        side-effects:    non state changes; no external effects
#        returns:    dict
#        nominal:    
#            dict['cube']
#    confidence level: boundary value analysis
#    
#    happy path:
#        test010: nominal valid dir and cube with right counterclockwise rotation    
#
#    (Only called by rotateCube so everything is going to arrive validated bc of the two validate functions)       

    def test800_010NominalParmsWithRightCounterClockwiseRotation(self):
        inputCube = 'yooygwwywworbybgybyyrrbgobgwwgrwgyrrgobgrgrwbbboworooy'
        expectedResult = {}
        expectedResult['cube'] = 'yobyggwybrbboyywbgyyrrbgobgwwgrwgyrrgoogrrrwybbowowoow'
        actualResult = rotate._rotateRightCounterClockwise(inputCube)
        self.assertDictEqual(expectedResult, actualResult)        
        
# 900 rotateBackClockwise
#    inputs:
#        parms:    strings; mandatory; arrives validated  
#        cube:    string; len=54; [brgoyw]; 9 occurrences of each character, unique middle character; mandatory; arrives validated
#    outputs: 
#        side-effects:    non state changes; no external effects
#        returns:    dict
#        nominal:    
#            dict['cube']
#    confidence level: boundary value analysis
#    
#    happy path:
#        test010: nominal valid dir and cube with back clockwise rotation    
#
#    (Only called by rotateCube so everything is going to arrive validated bc of the two validate functions)       

    def test900_010NominalParmsWithBackClockwiseRotation(self):
        inputCube = 'yooygwwywworbybgybyyrrbgobgwwgrwgyrrgobgrgrwbbboworooy'
        expectedResult = {}
        expectedResult['cube'] = 'yooygwwywwoybyogyoorybbyggrbwgowggrrrbbgrgrwbbboworwry'
        actualResult = rotate._rotateBackClockwise(inputCube)
        self.assertDictEqual(expectedResult, actualResult)        

# 1000 rotateBackCounterClockwise
#    inputs:
#        parms:    strings; mandatory; arrives validated  
#        cube:    string; len=54; [brgoyw]; 9 occurrences of each character, unique middle character; mandatory; arrives validated
#    outputs: 
#        side-effects:    non state changes; no external effects
#        returns:    dict
#        nominal:    
#            dict['cube']
#    confidence level: boundary value analysis
#    
#    happy path:
#        test010: nominal valid dir and cube with back counterclockwise rotation    
#
#    (Only called by rotateCube so everything is going to arrive validated bc of the two validate functions)       

    def test1000_010NominalParmsWithBackCounterClockwiseRotation(self):
        inputCube = 'yooygwwywworbybgybyyrrbgobgwwgrwgyrrgobgrgrwbbboworooy'
        expectedResult = {}
        expectedResult['cube'] = 'yooygwwywwogbyogybrggybbyroowgowgyrryrwgrgrwbbboworbbr'
        actualResult = rotate._rotateBackCounterClockwise(inputCube)
        self.assertDictEqual(expectedResult, actualResult)

# 2000 rotateLeftClockwise
#    inputs:
#        parms:    strings; mandatory; arrives validated  
#        cube:    string; len=54; [brgoyw]; 9 occurrences of each character, unique middle character; mandatory; arrives validated
#    outputs: 
#        side-effects:    non state changes; no external effects
#        returns:    dict
#        nominal:    
#            dict['cube']
#    confidence level: boundary value analysis
#    
#    happy path:
#        test010: nominal valid dir and cube with left clockwise rotation    
#
#    (Only called by rotateCube so everything is going to arrive validated bc of the two validate functions)       

    def test2000_010NominalParmsWithLeftClockwiseRotation(self):
        inputCube = 'yooygwwywworbybgybyyrrbgobgwwgrwgyrrgobgrgrwbbboworooy'
        expectedResult = {}
        expectedResult['cube'] = 'googgwrywworbybgybyyorbwobbyrwrwwrgggobgrgrwbyboyorwoy'
        actualResult = rotate._rotateLeftClockwise(inputCube)
        self.assertDictEqual(expectedResult, actualResult)

# 3000 rotateLeftCounterClockwise
#    inputs:
#        parms:    strings; mandatory; arrives validated  
#        cube:    string; len=54; [brgoyw]; 9 occurrences of each character, unique middle character; mandatory; arrives validated
#    outputs: 
#        side-effects:    non state changes; no external effects
#        returns:    dict
#        nominal:    
#            dict['cube']
#    confidence level: boundary value analysis
#    
#    happy path:
#        test010: nominal valid dir and cube with left counterclockwise rotation    
#
#    (Only called by rotateCube so everything is going to arrive validated bc of the two validate functions)       

    def test3000_010NominalParmsWithLeftCounterClockwiseRotation(self):
        inputCube = 'yooygwwywworbybgybyyrrbgobgwwgrwgyrrgobgrgrwbbboworooy'
        expectedResult = {}
        expectedResult['cube'] = 'boowgwoywworbybgybyyrrbgobgggrwwrwryyobyrgwwbgbogorroy'
        actualResult = rotate._rotateLeftCounterClockwise(inputCube)
        self.assertDictEqual(expectedResult, actualResult)
        
# 4000 rotateUpClockwise
#    inputs:
#        parms:    strings; mandatory; arrives validated  
#        cube:    string; len=54; [brgoyw]; 9 occurrences of each character, unique middle character; mandatory; arrives validated
#    outputs: 
#        side-effects:    non state changes; no external effects
#        returns:    dict
#        nominal:    
#            dict['cube']
#    confidence level: boundary value analysis
#    
#    happy path:
#        test010: nominal valid dir and cube with up clockwise rotation    
#
#    (Only called by rotateCube so everything is going to arrive validated bc of the two validate functions)       

    def test4000_010NominalParmsWithUpClockwiseRotation(self):
        inputCube = 'yooygwwywworbybgybyyrrbgobgwwgrwgyrrgobgrgrwbbboworooy'
        expectedResult = {}
        expectedResult['cube'] = 'worygwwywyyrbybgybwwgrbgobgyoorwgyrrrggwrobgbbboworooy'
        actualResult = rotate._rotateUpClockwise(inputCube)
        self.assertDictEqual(expectedResult, actualResult)

# 5000 rotateUpCounterClockwise
#    inputs:
#        parms:    strings; mandatory; arrives validated  
#        cube:    string; len=54; [brgoyw]; 9 occurrences of each character, unique middle character; mandatory; arrives validated
#    outputs: 
#        side-effects:    non state changes; no external effects
#        returns:    dict
#        nominal:    
#            dict['cube']
#    confidence level: boundary value analysis
#    
#    happy path:
#        test010: nominal valid dir and cube with up counterclockwise rotation    
#
#    (Only called by rotateCube so everything is going to arrive validated bc of the two validate functions)       

    def test5000_010NominalParmsWithUpCounterClockwiseRotation(self):
        inputCube = 'yooygwwywworbybgybyyrrbgobgwwgrwgyrrgobgrgrwbbboworooy'
        expectedResult = {}
        expectedResult['cube'] = 'wwgygwwywyoobybgybworrbgobgyyrrwgyrrbgborwggrbboworooy'
        actualResult = rotate._rotateUpCounterClockwise(inputCube)
        self.assertDictEqual(expectedResult, actualResult)

# 6000 rotateDownClockwise
#    inputs:
#        parms:    strings; mandatory; arrives validated  
#        cube:    string; len=54; [brgoyw]; 9 occurrences of each character, unique middle character; mandatory; arrives validated
#    outputs: 
#        side-effects:    non state changes; no external effects
#        returns:    dict
#        nominal:    
#            dict['cube']
#    confidence level: boundary value analysis
#    
#    happy path:
#        test010: nominal valid dir and cube with down clockwise rotation    
#
#    (Only called by rotateCube so everything is going to arrive validated bc of the two validate functions)       

    def test6000_010NominalParmsWithDownClockwiseRotation(self):
        inputCube = 'yooygwwywworbybgybyyrrbgobgwwgrwgyrrgobgrgrwbbboworooy'
        expectedResult = {}
        expectedResult['cube'] = 'yooygwyrrworbybwywyyrrbggybwwgrwgobggobgrgrwbowboobyro'
        actualResult = rotate._rotateDownClockwise(inputCube)
        self.assertDictEqual(expectedResult, actualResult)

# 7000 rotateDownCounterClockwise
#    inputs:
#        parms:    strings; mandatory; arrives validated  
#        cube:    string; len=54; [brgoyw]; 9 occurrences of each character, unique middle character; mandatory; arrives validated
#    outputs: 
#        side-effects:    non state changes; no external effects
#        returns:    dict
#        nominal:    
#            dict['cube']
#    confidence level: boundary value analysis
#    
#    happy path:
#        test010: nominal valid dir and cube with down counterclockwise rotation    
#
#    (Only called by rotateCube so everything is going to arrive validated bc of the two validate functions)       

    def test6000_010NominalParmsWithDownCounterClockwiseRotation(self):
        inputCube = 'yooygwwywworbybgybyyrrbgobgwwgrwgyrrgobgrgrwbbboworooy'
        expectedResult = {}
        expectedResult['cube'] = 'yooygwgybworbybobgyyrrbgyrrwwgrwgwywgobgrgrwboryboobwo'
        actualResult = rotate._rotateDownCounterClockwise(inputCube)
        self.assertDictEqual(expectedResult, actualResult)















