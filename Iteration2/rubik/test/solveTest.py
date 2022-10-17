'''
Created on Sep 27, 2022

@author: marymitchell
'''
import unittest
import rubik.solve as solve


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
#        test010: input a valid solved down cross
#        test020: input a valid solved daisy
#        test030: input a valid cube with unsolved daisy
#
#    sad path:
#        test910: input an invalid cube (just check that output is good since _verify has been tested already)

    def test100_010ValidSolvedDownCross(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        expectedResult = {}
        expectedResult['rotations'] = ''
        expectedResult['status'] = 'ok'
        actualResult = solve._solve(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
    
    def test100_020ValidSolvedDaisy(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'bbbrggrgwwggoogorwwroyboroyyooyryryggwowywywryrbbwbbbg'
        expectedResult = {}
        expectedResult['rotations'] = 'UUbbUUUFFuUURRUUuLLU'
        expectedResult['status'] = 'ok'
        actualResult = solve._solve(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test100_030ValidUnsolvedDaisy(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'gggwbbgrbrgbrrbrwroobogrywrybogoobwooywyyywowyywgwbyrg'
        expectedResult = {}
        expectedResult['rotations'] = 'UluruBUuFUUruULLuUFFuUBBuURRu'
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
        
# 200 _U21Daisy
#    inputs: 
#        parms:    dict; mandatory; arrives validated
#        parms['op']:    string; 'solve'; mandatory; arrives validated
#        parms['cube']:    string; len=54; [brgoyw]; 9 occurrences of each character, unique middle character; mandatory; arrives unvalidated
#    outputs:
#        side-effects:    non state changes; no external effects
#        returns:    dict
#        nominal: 
#            dict['rotations']: string, valid rotations to get proper U21 value
#            dict['cube']: string, valid cube after rotation for U21 is performed
#        abnormal: 
#            no abnormal behavior since method is only called if U21 does not have correct piece and cube has already been validated
#    confidence level: boundary value analysis
#
#    happy path:
#        test010: piece is R10 
#        test020: piece is F01
#        test030: piece is F10
#        test040: piece is F12
#        test050: piece is F21
#        test060: piece is R01
#        test070: piece is R12
#        test080: piece is R21
#        test090: piece is B01
#        test1000: piece is B10
#        test2000: piece is B12
#        test3000: piece is B21
#        test4000: piece is L01
#        test5000: piece is L10
#        test6000: piece is L12
#        test7000: piece is L21
#        test8000: piece is D01
#        test9000: piece is D10
#        test9010: piece is D12
#        test9020: piece is D21

    def test200_010PieceIsR10(self):
        inputDict = {}
        inputDict['cube'] = 'yywyrooyyrogwgwgworworoybbwbgrbbggryygwrygbobgrrbwboow'
        expectedResult = {}
        expectedResult['rotations'] = 'f'
        expectedResult['cube'] = 'woyyryyyorogrgwgworworoybbwbgbbbogrbygwrygrwgrgybwboow'
        actualResult = solve._U21Daisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult)

    def test200_020PieceIsF01(self):
        inputDict = {}
        inputDict['cube'] = 'bwoyryyyyyowggorwgbwowoywbwbgrbbrgrrygorygwrggobbwboor'
        expectedResult = {}
        expectedResult['rotations'] = 'FuRU'
        expectedResult['cube'] = 'gryyrbyyrrowwgygobbworoyrbwbgybbogrbygorygowgrgwbwwoow'
        actualResult = solve._U21Daisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test200_030PieceIsF10(self):
        inputDict = {}
        inputDict['cube'] = 'roowgygobgworoorywywogboorbbgyyrbyyryggryrgbwwwwgwbrbb'
        expectedResult = {}
        expectedResult['rotations'] = 'Ulu'
        expectedResult['cube'] = 'obrggyrobwworoorywywogbborgbgworyryyyggryrgwgbwwowbybb'
        actualResult = solve._U21Daisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test200_040PieceIsF12(self):
        inputDict = {}
        inputDict['cube'] = 'rrwoowboogworbbgywbgworyorgobbggwrywgrywygyyrrgyowbybb'
        expectedResult = {}
        expectedResult['rotations'] = 'uRU'
        expectedResult['cube'] = 'grroobbobywoybrwbwbgwyryrrgobyggwrywgrywygowbrgoowoybg'
        actualResult = solve._U21Daisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test200_050PieceIsF21(self):
        inputDict = {}
        inputDict['cube'] = 'ybwbbyowybgybrorrrrgoygrwwwbooyowrrgyyggyrgoowgbwwbgob'
        expectedResult = {}
        expectedResult['rotations'] = 'fuRU'
        expectedResult['cube'] = 'wgwbbbybbbgyrryroyrgobgrrwwbogyoorrgyyggyrowoowwwwygob'
        actualResult = solve._U21Daisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test200_060PieceIsR01(self):
        inputDict = {}
        inputDict['cube'] = 'wbggbywbbowworgyyyrgorgrgwwbooyowrroyybgybbrygorwwbgor'
        expectedResult = {}
        expectedResult['rotations'] = 'rf'
        expectedResult['cube'] = 'bbybbbwgwggyorygoyrgobgrrwwboryorrrbyyggyrwwoowowwygob'
        actualResult = solve._U21Daisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test200_070PieceIsR12(self):
        inputDict = {}
        inputDict['cube'] = 'bgybggyoyboroowbygbbgrbrrbwwgwbrorggowwwywoyroyorwrgyy'
        expectedResult = {}
        expectedResult['rotations'] = 'uuBUU'
        expectedResult['cube'] = 'rrbbggyoyoorooybygbbgbbgwrywgyyrorggowwwywgwwoyorwrbbr'
        actualResult = solve._U21Daisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test200_080PieceIsR21(self):
        inputDict = {}
        inputDict['cube'] = 'yybbgyrgbybgooowwwwgygbgrrbrroyrorrygwowywgbobrobwowyg'
        expectedResult = {}
        expectedResult['rotations'] = 'uruBUU'
        expectedResult['cube'] = 'oobbgbrggybgyoyyowwgyrbobgwrrbgrorrygwowywwwobrobwygyr'
        actualResult = solve._U21Daisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test200_090PieceIsB01(self):
        inputDict = {}
        inputDict['cube'] = 'brbooboygoogybbwooywyrrwwrbgryggyrbbobrwywrgwygrowgwyg'
        expectedResult = {}
        expectedResult['rotations'] = 'burU'
        expectedResult['cube'] = 'bbroogoyrgoorbobywywbgrrrrwwrwygygbbrggwywowyygyowbobg'
        actualResult = solve._U21Daisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult)    
        
    def test200_1000PieceIsB10(self):   
        inputDict = {}
        inputDict['cube'] = 'brwoogoyrorwrbgbygbbrwrrygrgorbgygbbywowywwygygyowbwoo'
        expectedResult = {}
        expectedResult['rotations'] = 'urU'
        expectedResult['cube'] = 'wggooyoyworwrbybrbbbrbrrygrgogbgygbbywowywowyygrowgwor'
        actualResult = solve._U21Daisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult)    
        
    def test200_2000PieceIsB12(self):
        inputDict = {}
        inputDict['cube'] = 'gywgbyyrbrrwbrrygrbbrbgwgbogoygoywooywowyworbbgrywogow'
        expectedResult = {}
        expectedResult['rotations'] = 'ULu'
        expectedResult['cube'] = 'wggrbybrborwbrrygrbbrbgygbbgogooyoywywowywowyrgrgwoyow'
        actualResult = solve._U21Daisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult)      
        
    def test200_3000PieceIsB21(self):
        inputDict = {}
        inputDict['cube'] = 'bywbroygyrogbgrbyrwggboygwyorwgbygrbywowyworbroogworbw'
        expectedResult = {}
        expectedResult['rotations'] = 'uubuLu'
        expectedResult['cube'] = 'wbwgroggyrogbgrbyowggyogbbrorrrbybyyywowywgwbroobwoyrw'
        actualResult = solve._U21Daisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult)  
        
    def test200_4000PieceIsL01(self):
        inputDict = {}
        inputDict['cube'] = 'ggrogyrbbyrrooboybwborbywyyywogrwggbgwggywwrbwoyowrrbo'
        expectedResult = {}
        expectedResult['rotations'] = 'LF'
        expectedResult['cube'] = 'wggbggbyrorrrobbybwbrrbowywggggrobwyywgyywowyooyowrrbo'
        actualResult = solve._U21Daisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult)  
        
    def test200_5000PieceIsL10(self):
        inputDict = {}
        inputDict['cube'] = 'bggyggoyryggrobbyborrrbowyowbrwrgyoggwywywworwoybwrbbo'
        expectedResult = {}
        expectedResult['rotations'] = 'UUbuu'
        expectedResult['cube'] = 'gooyggoyrbggroobyworrgbybrwwbrbrgooggwywywywywoybwrbbr'
        actualResult = solve._U21Daisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult)  
        
    def test200_6000PieceIsL12(self):
        inputDict = {}
        inputDict['cube'] = 'gowgoybrbrrrrbyyrwwbrbrgooggoyygwoyyywgwywogbogrowbwbb'
        expectedResult = {}
        expectedResult['rotations'] = 'F'
        expectedResult['cube'] = 'bggroobyworrgbybrwwbrbrgooggooyggoyrywgwywywyyrrowbwbb'
        actualResult = solve._U21Daisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult)      
        
    def test200_7000PieceIsL21(self):
        inputDict = {}
        inputDict['cube'] = 'oggbggwyrwbrrobbybgoorbowywbgggrobwgywywywyyoroyrwrrbo'
        expectedResult = {}
        expectedResult['rotations'] = 'UluF'
        expectedResult['cube'] = 'rrgygorggwbrbobwybgoorbywyybgwgroogyywywywbwobrrowrgbo'
        actualResult = solve._U21Daisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult)   
        
    def test200_8000PieceIsD01(self):
        inputDict = {}
        inputDict['cube'] = 'yrgbobgowygooborrwgrwgrooyrrbbygrbbobwwwywoyrywgywgygb'
        expectedResult = {}
        expectedResult['rotations'] = 'FF'
        expectedResult['cube'] = 'wogbobgryogorbobrwgrwgrooyrrbrygobbybwwwywgwyryoywgygb'
        actualResult = solve._U21Daisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult) 
    
    def test200_9000PieceIsD10(self):
        inputDict = {}
        inputDict['cube'] = 'yrgbobrrwygoobooyrgrwgrobborbbygrgowbwwwywoyrggbwwgyyy'
        expectedResult = {}
        expectedResult['rotations'] = 'DFF'
        expectedResult['cube'] = 'wogbobgryogorbobrwgrwgrooyrrbrygobbybwwwywgwyryoywgygb'
        actualResult = solve._U21Daisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult)  
        
    def test200_9010PieceIsD12(self):
        inputDict = {}
        inputDict['cube'] = 'ryoorgbrrwbrogowrgwogbobobyogbrbygryywgwywygbogbywwryw'
        expectedResult = {}
        expectedResult['rotations'] = 'dFF'
        expectedResult['cube'] = 'grwgrooyrrbrygobbywogbobgryogorbobrwywgwywwwbbgygwyoyr'
        actualResult = solve._U21Daisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult)  
        
    def test200_9020PieceIsD21(self):
        inputDict = {}
        inputDict['cube'] = 'ryoorggrywbrogobrrwogbobwrgogbrbyobyywgwywygbryoywgwwb'
        expectedResult = {}
        expectedResult['rotations'] = 'ddFF'
        expectedResult['cube'] = 'grwgrooyrrbrygobbywogbobgryogorbobrwywgwywwwbbgygwyoyr'
        actualResult = solve._U21Daisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult)  

# 300 _rotateDaisyPiece
#    inputs: 
#        parms:    string; mandatory; arrives validated
#        rotations:    string; len .GE. 0; [FfRrBbLlUuDd]; mandatory; arrives validated
#        cube:    string; len=54; [brgoyw]; 9 occurrences of each character, unique middle character; mandatory; arrives validated
#    outputs:
#        side-effects:    non state changes; no external effects
#        returns:    string
#        nominal: 
#           cube:    tring; len=54; [brgoyw]; 9 occurrences of each character, unique middle character;
#        abnormal: 
#            no abnormal behavior since method is only called if U21 does not have correct piece and cube has already been validated
#    confidence level: boundary value analysis
#
#    happy path:
#        test010: nominal cube and rotation (just a short method that is used often and calls rotate which is already tested so only one test)

    def test300_010NominalCubeAndRotation(self):
        rotation = 'f'
        cube = 'yywyrooyyrogwgwgworworoybbwbgrbbggryygwrygbobgrrbwboow'
        expectedResult = 'woyyryyyorogrgwgworworoybbwbgbbbogrbygwrygrwgrgybwboow'
        actualResult = solve._rotateDaisyPiece(rotation, cube)
        self.assertEqual(expectedResult, actualResult)
        
# 400 _U12Daisy
#    inputs: 
#        parms:    dict; mandatory; arrives validated
#        parms['cube']:    string; len=54; [brgoyw]; 9 occurrences of each character, unique middle character; mandatory; arrives unvalidated
#    outputs:
#        side-effects:    non state changes; no external effects
#        returns:    dict
#        nominal: 
#            dict['rotations']: string, valid rotations to get proper U12 value
#            dict['cube']: string, valid cube after rotation for U12 is performed
#        abnormal: 
#            no abnormal behavior since method is only called if U12 does not have correct piece and cube has already been validated
#    confidence level: boundary value analysis
#
#    happy path:
#        test010: piece is R01
#        test020: piece is R10
#        test030: piece is R12
#        test040: piece is R21
#        test050: piece is B01
#        test060: piece is B10
#        test070: piece is B12
#        test080: piece is B21
#        test090: piece is L01
#        test1000: piece is L10
#        test2000: piece is L12
#        test3000: piece is L21
#        test4000: piece is F01
#        test5000: piece is F10
#        test6000: piece is F12
#        test7000: piece is F21 
#        test8000: piece is D01
#        test9000: piece is D10
#        test9010: piece is D12
#        test9020: piece is D21       

    def test400_010PieceIsR01(self):
        inputDict = {}
        inputDict['cube'] = 'gbgyoygrwwwrrbbryybrbyrbrobyoyrgowoyowwwygoworgggwgobb'
        expectedResult = {}
        expectedResult['rotations'] = 'rUfu'
        expectedResult['cube'] = 'gbrborrygygogbyrrrgrbgrbgobyoyrgywobowwwywowbwoygwyobw'
        actualResult = solve._U12Daisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult) 
    
    def test400_020PieceIsR10(self):   
        inputDict = {}
        inputDict['cube'] = 'groogobyywryworoygobrgbyrrrygogrggowbwbwybwwbrbgbwowyy'
        expectedResult = {}
        expectedResult['rotations'] = 'Ufu'
        expectedResult['cube'] = 'grbrgywobyoyborryggbrgbyrrrygogrbgobbwowywwwoogwbwowyy'
        actualResult = solve._U12Daisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult) 
        
    def test400_030PieceIsR12(self):   
        inputDict = {}
        inputDict['cube'] = 'grogrbgobyrgrgwwooybrooyybrygoobywrrbwrwygwwgwboywgbyb'
        expectedResult = {}
        expectedResult['rotations'] = 'uBU'
        expectedResult['cube'] = 'grbgrbgobyoyrgywobgbrborrygygogbyrrrbwowywwwowboywgyow'
        actualResult = solve._U12Daisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult) 
        
    def test400_040PieceIsR21(self):   
        inputDict = {}
        inputDict['cube'] = 'grwgbbrrbggyoryowbgbrbgorrwygogoroygbwowyywwryyyowobbw'
        expectedResult = {}
        expectedResult['rotations'] = 'ruBU'
        expectedResult['cube'] = 'grbgbyrrryoygrbgobgbrrgywobygoborrygbwowywwwoyywowbwgo'
        actualResult = solve._U12Daisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult) 
        
    def test400_050PieceIsB01(self):   
        inputDict = {}
        inputDict['cube'] = 'obrworbygybwgbyrrrbwggrggowwggogrbyyooowyrywbooybwyrbw'
        expectedResult = {}
        expectedResult['rotations'] = 'br'
        expectedResult['cube'] = 'obwworbybooobbrygrwgwyroyggrggbgrwyybobwywywgoorbwrryg'
        actualResult = solve._U12Daisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult) 
     
    def test400_060PieceIsB10(self):   
        inputDict = {}
        inputDict['cube'] = 'oooyroyggwgwbgrwyyrggworbybobwbbrygrywbwyogwbgyrrwbroo'
        expectedResult = {}
        expectedResult['rotations'] = 'r'
        expectedResult['cube'] = 'oobyroygbwryggywbwoggborrybobwbbrygrywbwywgwrgyorworog'
        actualResult = solve._U12Daisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult)  
    
    def test400_070PieceIsB12(self):   
        inputDict = {}
        inputDict['cube'] = 'ooyyroyggbybbgbwyryggrowwgwobwrbrogrywowyogwrgyrrwbbob'
        expectedResult = {}
        expectedResult['rotations'] = 'uuLuu'
        expectedResult['cube'] = 'ooborooggorbbgbwyrrggrorwggobwgbyrrbywywywgwwyyrywbyob'
        actualResult = solve._U12Daisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult)   
        
    def test400_080PieceIsB21(self):   
        inputDict = {}
        inputDict['cube'] = 'rgbbgoyggwrwgoywygoobobrywborbyroogrwwgwybywrgyrrwbybo'
        expectedResult = {}
        expectedResult['rotations'] = 'druBU'
        expectedResult['cube'] = 'rggbgbwyrobwrorwggoobgbyrrborborooggwwgwywywyrbbywoyyy'
        actualResult = solve._U12Daisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult)   
        
    def test400_090PieceIsL01(self):   
        inputDict = {}
        inputDict['cube'] = 'wgowgbyyrbrbrorwggobygbyyyrrwggrrgobgwwoyyowyrbbbwowoo'
        expectedResult = {}
        expectedResult['rotations'] = 'LUFu'
        expectedResult['cube'] = 'ggwygrrbboobyorwggybwgbbyyrggrorbbrbrwoyywywgwrowwoyoo'
        actualResult = solve._U12Daisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult)   
        
    def test400_1000PieceIsL10(self):   
        inputDict = {}
        inputDict['cube'] = 'ybbrrgybrwyyygrybbggwyorwgroobwbggobgwowyoowrrygbwrwoo'
        expectedResult = {}
        expectedResult['rotations'] = 'ubU'
        expectedResult['cube'] = 'yborrgybryrrygoybrwgwyogwywoobobgoobgwgwywowgrygbwrbrb'
        actualResult = solve._U12Daisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult)     
        
    def test400_2000PieceIsL12(self):   
        inputDict = {}
        inputDict['cube'] = 'ybgrgbyyyrorroggywbgwobgooboobrrwybggwwwyyowwogrywrrbb'
        expectedResult = {}
        expectedResult['rotations'] = 'UFu'
        expectedResult['cube'] = 'yboygoybryrryogwywwgwobgooboobrrgybrgwgwywowggrbywrrbb'
        actualResult = solve._U12Daisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult) 
    
    def test400_3000PieceIsL21(self):   
        inputDict = {}
        inputDict['cube'] = 'oorobywyyyrobrogywyrrygboobwgwrogowrgwgwyggwbbgrbwrybb'
        expectedResult = {}
        expectedResult['rotations'] = 'UULUbU'
        expectedResult['cube'] = 'oorgbygyyybbbrbgybwrrrgooyowgwborbgogwrwywgwbygrowrwoy'
        actualResult = solve._U12Daisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult) 
        
    def test400_4000PieceIsF01(self):   
        inputDict = {}
        inputDict['cube'] = 'gwrgbwgybboobryybgwgwrgyrrooowoorygogwbwybrrwygrowybby'
        expectedResult = {}
        expectedResult['rotations'] = 'FR'
        expectedResult['cube'] = 'ggbybybwywrrbrogyowgwbgybroooyoogygrgwgwyworrybrowrbbw'
        actualResult = solve._U12Daisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult)      
    
    def test400_5000PieceIsF10(self):   
        inputDict = {}
        inputDict['cube'] = 'ooywbgyybbygrroryoorrbgybrowgwoobygrgwywyggwrgbwowrbbw'
        expectedResult = {}
        expectedResult['rotations'] = 'uuluu'
        expectedResult['cube'] = 'ooyobgbybgbrrroryogrrbggbrrwgwyogboygwywywgwoobwywrybw'
        actualResult = solve._U12Daisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test400_6000PieceIsF12(self):   
        inputDict = {}
        inputDict['cube'] = 'grgbgwbrgwgygoowybooyybgyybgbrrroryoowbwyoywowbrrwgwbr'
        expectedResult = {}
        expectedResult['rotations'] = 'R'
        expectedResult['cube'] = 'grrbggbrrwgwyogboyooyobgbybgbrrroryoowgwywywgwbyrwywbo'
        actualResult = solve._U12Daisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
    
    def test400_7000PieceIsF21(self):
        inputDict = {}
        inputDict['cube'] = 'gbwobrywrrrryrgbbbwgwygrwoyooybogbyrgwgwygowbgrybwooyo'
        expectedResult = {}
        expectedResult['rotations'] = 'UfuR'
        expectedResult['cube'] = 'gbrrboroogrrbrrbgrwgwygrboyooybogbybgwgwywowywgwbwyoyy'
        actualResult = solve._U12Daisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test400_8000PieceIsD01(self):
        inputDict = {}
        inputDict['cube'] = 'grggrbrbrybbogywryrogoobbrwogorbooywywywyywwrgwbgwybgo'
        expectedResult = {}
        expectedResult['rotations'] = 'DRR'
        expectedResult['cube'] = 'grwgrooyrrbrygobbywogbobgryogorbobrwywgwywwwbbgygwyoyr'
        actualResult = solve._U12Daisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
    
    def test400_9000PieceIsD10(self):
        inputDict = {}
        inputDict['cube'] = 'grggrbwryybbogybrwrogooboywogorborbrywywyywwrbyowwgggb'
        expectedResult = {}
        expectedResult['rotations'] = 'DDRR'
        expectedResult['cube'] = 'grwgrooyrrbrygobbywogbobgryogorbobrwywgwywwwbbgygwyoyr'
        actualResult = solve._U12Daisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
    
    def test400_9010PieceIsD12(self):
        inputDict = {}
        inputDict['cube'] = 'grggrboywybbogyrbrrogoobwryogorbobrwywywyywwrbgggwwoyb'
        expectedResult = {}
        expectedResult['rotations'] = 'RR'
        expectedResult['cube'] = 'grwgrooyrrbrygobbywogbobgryogorbobrwywgwywwwbbgygwyoyr'
        actualResult = solve._U12Daisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test400_9020PieceIsD21(self):
        inputDict = {}
        inputDict['cube'] = 'grggrbbrwybbogyoywrogoobrbrogorbowryywywyywwrogbywgbwg'
        expectedResult = {}
        expectedResult['rotations'] = 'dRR'
        expectedResult['cube'] = 'grwgrooyrrbrygobbywogbobgryogorbobrwywgwywwwbbgygwyoyr'
        actualResult = solve._U12Daisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
# 500 _U10Daisy
#    inputs: 
#        parms:    dict; mandatory; arrives validated
#        parms['cube']:    string; len=54; [brgoyw]; 9 occurrences of each character, unique middle character; mandatory; arrives unvalidated
#    outputs:
#        side-effects:    non state changes; no external effects
#        returns:    dict
#        nominal: 
#            dict['rotations']: string, valid rotations to get proper U10 value
#            dict['cube']: string, valid cube after rotation for U10 is performed
#        abnormal: 
#            no abnormal behavior since method is only called if U10 does not have correct piece and cube has already been validated
#    confidence level: boundary value analysis
#
#    happy path:
#        test010: piece is L01
#        test020: piece is L10
#        test030: piece is L12
#        test040: piece is L21
#        test050: piece is F01
#        test060: piece is F10
#        test070: piece is F12
#        test080: piece is F21
#        test090: piece is R01
#        test1000: piece is R10
#        test2000: piece is R12
#        test3000: piece is R21
#        test4000: piece is B01
#        test5000: piece is B10
#        test6000: piece is B12
#        test7000: piece is B21 
#        test8000: piece is D01
#        test9000: piece is D10
#        test9010: piece is D12
#        test9020: piece is D21        

    def test500_010PieceIsL01(self):
        inputDict = {}
        inputDict['cube'] = 'wrgoobwryrogrbgbrgogyyroobrrwoyggbbrgwybywbwwbyoywgyow'
        expectedResult = {}
        expectedResult['rotations'] = 'LuFU'
        expectedResult['cube'] = 'rrgroyybrrogobgyrgogwyryobbbbbbgyrgoowywywywwbrgowgwow'
        actualResult = solve._U10Daisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test500_020PieceIsL10(self):
        inputDict = {}
        inputDict['cube'] = 'wgwbgyrgobbbrogybwrrgrbogggyorwryybbrwyyywgwowobowroyo'
        expectedResult = {}
        expectedResult['rotations'] = 'Ubu'
        expectedResult['cube'] = 'ogwbgyrgobbbroyybrrrgobgyrgrogyryobbwwywywywowobowrwgg'
        actualResult = solve._U10Daisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test500_030PieceIsL12(self):
        inputDict = {}
        inputDict['cube'] = 'wgworbryobbbogywgorryroyybrgybobwyrwowybywrwoggggwogrb'
        expectedResult = {}
        expectedResult['rotations'] = 'uFU'
        expectedResult['cube'] = 'ogwyryobbbbbbgyrgorrgroyybrrogobgyrgwwywywywowowgwogrb'
        actualResult = solve._U10Daisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test500_040PieceIsL21(self):
        inputDict = {}
        inputDict['cube'] = 'bbbbrbryorrgogywgorogrogybgyowrbyywbrwwyywowywgggwoorb'
        expectedResult = {}
        expectedResult['rotations'] = 'LUbu'
        expectedResult['cube'] = 'rbbyrboyorrgoggwggrogrobyryygwrbobywrwwwywbwybggbwooyo'
        actualResult = solve._U10Daisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test500_050PieceIsF01(self):
        inputDict = {}
        inputDict['cube'] = 'owyrooyrroogbbrbrgygrwrywyobywgggbggwwrbywgbboyyowbwor'
        expectedResult = {}
        expectedResult['rotations'] = 'fl'
        expectedResult['cube'] = 'woroorwryyogybrorgygowrbwywbbgyggbgbywrwywobboggywbror'
        actualResult = solve._U10Daisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test500_060PieceIsF10(self):
        inputDict = {}
        inputDict['cube'] = 'yogwrbwywygoyggbgbbbgoorwryworybrorgowybywbwrrorbwyggo'
        expectedResult = {}
        expectedResult['rotations'] = 'l'
        expectedResult['cube'] = 'rogbrbgywygoyggbgbbbboobwrorrgobrwyoywywywwwryorrwyggo'
        actualResult = solve._U10Daisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test500_070PieceIsF12(self):
        inputDict = {}
        inputDict['cube'] = 'obbbrwgyrrrggggyybroyyobrroogbobrwyobwwoywwwyyogrwbggw'
        expectedResult = {}
        expectedResult['rotations'] = 'uuRuu'
        expectedResult['cube'] = 'bbbbrbgywrrgyggbgbrogoobwroygoobrwyorwwwywywyyorrwyggo'
        actualResult = solve._U10Daisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test500_080PieceIsF21(self):
        inputDict = {}
        inputDict['cube'] = 'rogoggywbygoyobwybbbyoborrogbgyrgwybowyrywwwrrrorwbggw'
        expectedResult = {}
        expectedResult['rotations'] = 'uFUl'
        expectedResult['cube'] = 'wogrgbgggygorobwybbbyobgrrbgrooryyywowywywbwroyrowbrgw'
        actualResult = solve._U10Daisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test500_090PieceIsR01(self):
        inputDict = {}
        inputDict['cube'] = 'wbbyoyorwowrbbgrrbgoyorwyyoobbrgggrgbwyoygrwwwbgywgyor'
        expectedResult = {}
        expectedResult['rotations'] = 'rufU'
        expectedResult['cube'] = 'bbyboroyorgbbbrwbrrorgrwgyobgwrgogrbwwywyoowgyggywyyow'
        actualResult = solve._U10Daisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test500_1000PieceIsR10(self):
        inputDict = {}
        inputDict['cube'] = 'borbbrrrgbgwwrorbwbbgggogrboyyboyoywywooywrwwggygwryyo'
        expectedResult = {}
        expectedResult['rotations'] = 'ufU'
        expectedResult['cube'] = 'yorybrobrbgwgrogbwbbrggogrbyrgboooyybwowywrwwgywgwryyo'
        actualResult = solve._U10Daisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult)   
        
    def test500_2000PieceIsR12(self):
        inputDict = {}
        inputDict['cube'] = 'ogwboooyybbrybwobryrworbyggrowrgowrbbwbgywgwoyggywyrrg'
        expectedResult = {}
        expectedResult['rotations'] = 'UBu'
        expectedResult['cube'] = 'bgwboooyybbrybrobryrggrogbwyorggogrbrwbwywwwoyggywyorw'
        actualResult = solve._U10Daisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult)   
        
    def test500_3000PieceIsR21(self):
        inputDict = {}
        inputDict['cube'] = 'yrgybrobwyorbroowbbgwbgroggggryoooyyrwwrywbwrgybgwbwoy'
        expectedResult = {}
        expectedResult['rotations'] = 'uuruBu'
        expectedResult['cube'] = 'yrgybrobryorgrogbwbgwggogrbbbrboooyyowwwywbwrgywgwryyo'
        actualResult = solve._U10Daisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult)  
        
    def test500_4000PieceIsB01(self):
        inputDict = {}
        inputDict['cube'] = 'ggorbbyyoworyrbgywbwoogwrrobrrrobwobybwyywywbroygwgggg'
        expectedResult = {}
        expectedResult['rotations'] = 'BL'
        expectedResult['cube'] = 'rgoybbyyowogyrggygrobrggowrybwoorbbrobwwywbwbgoyrwgyrw'
        actualResult = solve._U10Daisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult) 
        
    def test500_5000PieceIsB10(self):
        inputDict = {}
        inputDict['cube'] = 'wbwybbyyorgoyrrgyywowwgorgborrborobrgwbgywgwbgoyrwgyob'
        expectedResult = {}
        expectedResult['rotations'] = 'UUrUU'
        expectedResult['cube'] = 'bbwybgyygrgorryoygwogggoygbrryborobrwwbwywrwbgowrwbyoo'
        actualResult = solve._U10Daisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult)  
    
    def test500_6000PieceIsB12(self):
        inputDict = {}
        inputDict['cube'] = 'ybwybbyyorgoyrbgywwooogwrrobgrrorwbrywboywbwbgoyrwgggg'
        expectedResult = {}
        expectedResult['rotations'] = 'L'
        expectedResult['cube'] = 'ybwobbbyorgoyrbgywwogogrrrgwrbbogrrrowbwywowbyoyywgygg'
        actualResult = solve._U10Daisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult)  
        
    def test500_7000PieceIsB21(self):
        inputDict = {}
        inputDict['cube'] = 'ybwybbyyorgoyrggygwogrggowrroboorbbrwwbbywowbgoyrwgyrw'
        expectedResult = {}
        expectedResult['rotations'] = 'UBUrUU'
        expectedResult['cube'] = 'bbwybgyygrgorryoygwogggoygbrryborobrwwbwywrwbgowrwbyoo'
        actualResult = solve._U10Daisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult)  
        
    def test500_8000PieceIsD01(self):
        inputDict = {}
        inputDict['cube'] = 'bbwobgyrrrgorrygygwoyggyoygrborobygbgwbrywywbrwwowoobw'
        expectedResult = {}
        expectedResult['rotations'] = 'dll'
        expectedResult['cube'] = 'bbwybgyygrgorryoygwogggoygbrryborobrwwbwywrwbgowrwbyoo'
        actualResult = solve._U10Daisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult) 
    
    def test500_9000PieceIsD10(self):
        inputDict = {}
        inputDict['cube'] = 'bbwobggygrgorryoygwoyggyygbrborobyrrgwbrywywbwowwwbroo'
        expectedResult = {}
        expectedResult['rotations'] = 'll'
        expectedResult['cube'] = 'bbwybgyygrgorryoygwogggoygbrryborobrwwbwywrwbgowrwbyoo'
        actualResult = solve._U10Daisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
    
    def test500_9010PieceIsD12(self):
        inputDict = {}
        inputDict['cube'] = 'bbwobgygbrgorryyrrwoyggygygrboroboyggwbrywywboorbwwwow'
        expectedResult = {}
        expectedResult['rotations'] = 'ddll'
        expectedResult['cube'] = 'bbwybgyygrgorryoygwogggoygbrryborobrwwbwywrwbgowrwbyoo'
        actualResult = solve._U10Daisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult) 
        
    def test500_9020PieceIsD21(self):
        inputDict = {}
        inputDict['cube'] = 'bbwobgoygrgorryygbwoyggyyrrrborobgyggwbrywywbwboowowwr'
        expectedResult = {}
        expectedResult['rotations'] = 'Dll'
        expectedResult['cube'] = 'bbwybgyygrgorryoygwogggoygbrryborobrwwbwywrwbgowrwbyoo'
        actualResult = solve._U10Daisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult)      
        
# 600 _U01Daisy
#    inputs: 
#        parms:    dict; mandatory; arrives validated
#        parms['cube']:    string; len=54; [brgoyw]; 9 occurrences of each character, unique middle character; mandatory; arrives unvalidated
#    outputs:
#        side-effects:    non state changes; no external effects
#        returns:    dict
#        nominal: 
#            dict['rotations']: string, valid rotations to get proper U10 value
#            dict['cube']: string, valid cube after rotation for U01 is performed
#        abnormal: 
#            no abnormal behavior since method is only called if U01 does not have correct piece and cube has already been validated
#    confidence level: boundary value analysis
#
#    happy path:
#        test010: piece is B01
#        test020: piece is B10
#        test030: piece is B12
#        test040: piece is B21
#        test050: piece is L01
#        test060: piece is L10
#        test070: piece is L12
#        test080: piece is L21
#        test090: piece is F01
#        test1000: piece is F10
#        test2000: piece is F12
#        test3000: piece is F21
#        test4000: piece is R01
#        test5000: piece is R10
#        test6000: piece is R12
#        test7000: piece is R21 
#        test8000: piece is D01
#        test9000: piece is D10
#        test9010: piece is D12
#        test9020: piece is D21        
    
    def test600_010PieceIsB01(self):
        inputDict = {}
        inputDict['cube'] = 'rbgooggyrwgwobybbgbwyoryyrbrowggbogrgrowywbwowbyrwryyo'
        expectedResult = {}
        expectedResult['rotations'] = 'bUru'
        expectedResult['cube'] = 'rbgooggyrwgoybbyobbrorrryoywowygbogrbwywywbwowbgrwggyr'
        actualResult = solve._U01Daisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test600_020PieceIsB10(self):
        inputDict = {}
        inputDict['cube'] = 'wowooggyrrbgobgbboyywwrryoyoroygbogrggrwywbwbwbyrwrgyb'
        expectedResult = {}
        expectedResult['rotations'] = 'Uru'
        expectedResult['cube'] = 'wowooggyrrbgybbyobwgorrryoybroygbogrywowywbwbwbgrwggyr'
        actualResult = solve._U01Daisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test600_030PieceIsB12(self):
        inputDict = {}
        inputDict['cube'] = 'wowygbrgrrbyooggyroryybwyoogrogrowryoybwywbwbbrwbwbggg'
        expectedResult = {}
        expectedResult['rotations'] = 'uLU'
        expectedResult['cube'] = 'wowygbogrrbgooggyrwgoybbyobbrorrryoyywowywbwbgrwywbrgg'
        actualResult = solve._U01Daisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
    
    def test600_040PieceIsB21(self):
        inputDict = {}
        inputDict['cube'] = 'wowooggyrrbgobgbbrwryyroywygroygbbgroyowywbwbwbyrwrogg'
        expectedResult = {}
        expectedResult['rotations'] = 'BUru'
        expectedResult['cube'] = 'wowooggyrrbgybbyobwgorrryoybroygbogrywowywbwbwbgrwggyr'
        actualResult = solve._U01Daisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test600_050PieceIsL01(self):
        inputDict = {}
        inputDict['cube'] = 'wgobbowyybrggrrgoooywggowrybwbwoyrogorybywrwyrgrbwybbg'
        expectedResult = {}
        expectedResult['rotations'] = 'lb'
        expectedResult['cube'] = 'rgobbobyybrwgrrgoyrboygrogwwygboogwrbwbbywwwyygrowyorg'
        actualResult = solve._U01Daisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test600_060PieceIsL10(self):
        inputDict = {}
        inputDict['cube'] = 'brwbbowyyrbogrrgoygbwygoogybgowoyrogorwwywywbrgrbwybrg'
        expectedResult = {}
        expectedResult['rotations'] = 'b'
        expectedResult['cube'] = 'brwbbowyyrbogrrgowwoybgggyobgoroygogrwbwywywbrgrbwyyro'
        actualResult = solve._U01Daisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test600_070PieceIsL12(self):
        inputDict = {}
        inputDict['cube'] = 'woyrbybbwbgbgrrrowwoybgggyorborowgoyggrwywbwroygbwyyro'
        expectedResult = {}
        expectedResult['rotations'] = 'uuFuu'
        expectedResult['cube'] = 'woybbowyybgogrrgowbrwbgggyorboroygogbwywywbwrrgrbwyyro'
        actualResult = solve._U01Daisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult)  
        
    def test600_080PieceIsL21(self):
        inputDict = {}
        inputDict['cube'] = 'brwgbygbwrbygrrrowgrybgbgyobgoooobwyrgowywywbrygowywro'
        expectedResult = {}
        expectedResult['rotations'] = 'uLUb'
        expectedResult['cube'] = 'brwgbyrbwrbygrbroogorogybbgggororooyywowywywbbyggwywrw'
        actualResult = solve._U01Daisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult) 
        
    def test600_1000PieceIsF01(self):
        inputDict = {}
        inputDict['cube'] = 'owbwooyogwowbbbygrgygyrrbgwyrbbgggyororwywwbrbgorwroyy'
        expectedResult = {}
        expectedResult['rotations'] = 'fulU'
        expectedResult['cube'] = 'bogrooowyoorgbbbgrgbwyrobgrbrrygygbgowywywwbywgorwrwyy'
        actualResult = solve._U01Daisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult) 
        
    def test600_2000PieceIsF10(self):
        inputDict = {}
        inputDict['cube'] = 'gbwwooyogbrwbbbygrorbyrobgrworygggborygwywywobgorwrwyy'
        expectedResult = {}
        expectedResult['rotations'] = 'ulU'
        expectedResult['cube'] = 'gbwroowogbrrbbbygrbgoyrybggborrgboygywwwywyworgoowrwyy'
        actualResult = solve._U01Daisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult) 
        
    def test600_3000PieceIsF12(self):
        inputDict = {}
        inputDict['cube'] = 'bgorgwoyybooboogrwwoggbbrgrorryrybggybbwywwwyworywbyrg'
        expectedResult = {}
        expectedResult['rotations'] = 'URu'
        expectedResult['cube'] = 'bgorgboygborroowoggbwbbbygrbrryrybggowywywwwyworywgyro'
        actualResult = solve._U01Daisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult) 
        
    def test600_4000PieceIsF21(self):
        inputDict = {}
        inputDict['cube'] = 'gbwrooowybrrgbbbgrbogyrobgroorygygbgybwwywywowgorwrwyy'
        expectedResult = {}
        expectedResult['rotations'] = 'UUfuRu'
        expectedResult['cube'] = 'gbwoorbrybrggborbywgggrobgroorygbgbwywowywyworybrwywyo'
        actualResult = solve._U01Daisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult) 
        
    def test600_5000PieceIsR01(self):
        inputDict = {}
        inputDict['cube'] = 'gbbygggbwywyoowgobgbrgbgwyryorrrowgrbyowyrywowroywbbro'
        expectedResult = {}
        expectedResult['rotations'] = 'RB'
        expectedResult['cube'] = 'gboygbgbogogoorbwboroybbrgrboryrobgrywywygywwwrwywgyrw'
        actualResult = solve._U01Daisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult)  
    
    def test600_6000PieceIsR10(self):
        inputDict = {}
        inputDict['cube'] = 'borygggbwgbwwoobrgboggbbygrwroyrobgrobowywywywrrywyyro'
        expectedResult = {}
        expectedResult['rotations'] = 'UUfUU'
        expectedResult['cube'] = 'borogbbyggboroowrgggwgbbygrrroyrbbgobwwwywywyworywyyro'
        actualResult = solve._U01Daisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult)         
        
    def test600_7000PieceIsR12(self):
        inputDict = {}
        inputDict['cube'] = 'rroyrbbgobowogwbyyoogborgrwogwybbrgryggwywbwyyywrwogbr'
        expectedResult = {}
        expectedResult['rotations'] = 'B'
        expectedResult['cube'] = 'rroyrbbgoborogbbyggboroowrgggwgbbygrwwywywbwyyywrwooyr'
        actualResult = solve._U01Daisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult)    
        
    def test600_8000PieceIsR21(self):
        inputDict = {}
        inputDict['cube'] = 'ggwgbyygorrygrbywgbyrrgywobgboooowrgybrwywwwborbywoobr'
        expectedResult = {}
        expectedResult['rotations'] = 'UruB'
        expectedResult['cube'] = 'ggwgbbygrrroyrbbgoborogbbyggboroowrgywywywwwboryywyrow'
        actualResult = solve._U01Daisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult) 
        
    def test600_9000PieceIsD01(self):
        inputDict = {}
        inputDict['cube'] = 'gborooorrggbgbowygogbbrywrgrorbgbygbyywwywywwywbrwooyr'
        expectedResult = {}
        expectedResult['rotations'] = 'DDBB'
        expectedResult['cube'] = 'gboroowrgggwgbbygrrroyrbbgoborogbbygywbwywywwryoowrwyy'
        actualResult = solve._U01Daisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult) 
    
    def test600_9010PieceIsD10(self):
        inputDict = {}
        inputDict['cube'] = 'borogbogogbbroybygrgybbgwrrgroorbwggorywywywywywwwobyr'
        expectedResult = {}
        expectedResult['rotations'] = 'dBB'
        expectedResult['cube'] = 'borogbbyggboroowrgggwgbbygrrroyrbbgobwwwywywyworywyyro'
        actualResult = solve._U01Daisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult) 
    
    def test600_9020PieceIsD12(self):
        inputDict = {}
        inputDict['cube'] = 'ggwyrrbggrrwbgorobgybbooorgobogbbygrworwywwwbyyyrwwoyy'
        expectedResult = {}
        expectedResult['rotations'] = 'DBB'
        expectedResult['cube'] = 'ggwyrrygrrrobggbgoboroobbyggboobbwrgywywywwwboryywyrow'
        actualResult = solve._U01Daisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test600_9030PieceIsD21(self):
        inputDict = {}
        inputDict['cube'] = 'ggwyrrygrrrwbgobgggybboorobobogbborgworwywwwboryywyywy'
        expectedResult = {}
        expectedResult['rotations'] = 'BB'
        expectedResult['cube'] = 'ggwyrrygrrrobggbgoboroobbyggboobbwrgywywywwwboryywyrow'
        actualResult = solve._U01Daisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult)     

# 700 _solveDaisy
#    inputs: 
#        parms:    dict; mandatory; arrives validated
#        parms['op']:    string; 'solve'; mandatory; arrives validated
#        parms['cube']:    string; len=54; [brgoyw]; 9 occurrences of each character, unique middle character; mandatory; arrives unvalidated
#    outputs:
#        side-effects:    non state changes; no external effects
#        returns:    dict
#        nominal: 
#            dict['rotations']: string, valid rotations to solve daisy
#            dict['cube']: string, valid cube after rotations for daisy is performed
#        abnormal: 
#            no abnormal behavior since method is only called if daisy is unsolved and cube is already validated
#    confidence level: boundary value analysis
#
#    happy path:
#        test010: valid cube with unsolved U21 Daisy
#        test020: valid cube with unsolved U21 and U12 Daisy
#        test030: valid cube with unsolved U21, U12, and U10 Daisy
#        test040: valid cube with all unsolved Daisy
   
    def test700_010ValidCubeWithUnsolvedU21Daisy(self):
        inputDict = {}
        inputDict['cube'] = 'grwrrwobobbygggyogbryyogobwrowobyboygwrwywrgogybbwyrrw'
        expectedResult = {}
        expectedResult['rotations'] = 'uRU'
        expectedResult['cube'] = 'yggrryobwrbyogrggwbrygogobwrobobyboygwrwywowwgyobwyrrb'
        actualResult = solve._solveDaisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test700_020ValidCubeWithUnsolvedU21AndU12Daisy(self):
        inputDict = {}
        inputDict['cube'] = 'gywgggywrorwyogbbwbryobyboyrowrrwobogwowygrogbbyywrgbr'
        expectedResult = {}
        expectedResult['rotations'] = 'fuRUDRR'
        expectedResult['cube'] = 'bbwygyobbrgggobwrorryrbywgrroorroboygwwwywywbgyobwgyog'
        actualResult = solve._solveDaisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test700_030ValidCubeWithUnsolvedU21U12AndU10Daisy(self):
        inputDict = {}
        inputDict['cube'] = 'owbbgbyyowboyorggwgrggbwoggrwyororrbwwwbyrbgrroyywyyob'
        expectedResult = {}
        expectedResult['rotations'] = 'FuRUuuLuuLuFU'
        expectedResult['cube'] = 'ggybgrbyrrobyobgrorrrobyyggbbyoryobowwywywowgwgwrwgwob'
        actualResult = solve._solveDaisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
    
    def test700_040ValidCubeWithAllUnsolvedDaisy(self):
        inputDict = {}
        inputDict['cube'] = 'ywgrgywbbybygowwyybwwrbgbgwrwoorbroobbrgyogorgyoywrgro'
        expectedResult = {}
        expectedResult['rotations'] = 'FuRUruBULuFUbUru'
        expectedResult['cube'] = 'yooygogogbroyoyrrwwbrrbgbgwygoorgrywbwbwywgwyobybwbgrr'
        actualResult = solve._solveDaisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult)        
          
# 800 _U21Down
#    inputs: 
#        parms:    dict; mandatory; arrives validated
#        parms['cube']:    string; len=54; [brgoyw]; 9 occurrences of each character, unique middle character; mandatory; arrives unvalidated
#    outputs:
#        side-effects:    non state changes; no external effects
#        returns:    dict
#        nominal: 
#            dict['rotations']: string, valid rotations to get proper U21 to its proper down facing place
#            dict['cube']: string, valid cube after rotation for U21 is performed
#        abnormal: 
#            no abnormal behavior since method is only called after cube is validated and daisy is solved
#    confidence level: boundary value analysis
#
#    happy path:
#        test010: place is D01
#        test020: place is D10
#        test030: place is D12
#        test040: place is D21


    def test800_010PlaceIsD01(self):    
        inputDict = {}
        inputDict['cube'] = 'yooyoyrrwbrorbgbgwwbrorgrywygoygogogbwbwywgwyybrbwrobg'
        expectedResult = {}
        expectedResult['rotations'] = 'FF'
        expectedResult['cube'] = 'wrryoyooygroobgogwwbrorgrywygbygrgobbwbwywrbyywgbwrobg'
        actualResult = solve._U21Down(inputDict)
        self.assertDictEqual(expectedResult, actualResult) 
    
    def test800_020PlaceIsD10(self):    
        inputDict = {}
        inputDict['cube'] = 'broygogogwbryoyrrwygorbgbgwyooorgrywgwbwywywbobybwbgrr'
        expectedResult = {}
        expectedResult['rotations'] = 'ULLu'
        expectedResult['cube'] = 'wyrggooogwbryoyrrwygorbybgwyoggroorbgwbwywobgybywwbbrr'
        actualResult = solve._U21Down(inputDict)
        self.assertDictEqual(expectedResult, actualResult)        
        
    def test800_030PlaceIsD12(self):    
        inputDict = {}
        inputDict['cube'] = 'yooygogogbroyoyrrwwbrrbgbgwygoorgrywbwbwywgwyobybwbgrr'
        expectedResult = {}
        expectedResult['rotations'] = 'urrU'
        expectedResult['cube'] = 'wrrygrgobgroyoyooywbrobgogwygborgrywbwbwywrbyobybwwgrg'
        actualResult = solve._U21Down(inputDict)
        self.assertDictEqual(expectedResult, actualResult)   
    
    def test800_034PlaceIsD21(self):    
        inputDict = {}
        inputDict['cube'] = 'yooorygogbrorgyrrwwbrgoybgwygoobgrywbwbwywgwyobybwbgrr'
        expectedResult = {}
        expectedResult['rotations'] = 'UUbbUU'
        expectedResult['cube'] = 'wgborygogwrorgorrbwbryogooyygrybgoywbwbwywgrrobybwbgwy'
        actualResult = solve._U21Down(inputDict)
        self.assertDictEqual(expectedResult, actualResult) 
        
# 900 _U12Down
#    inputs: 
#        parms:    dict; mandatory; arrives validated
#        parms['cube']:    string; len=54; [brgoyw]; 9 occurrences of each character, unique middle character; mandatory; arrives unvalidated
#    outputs:
#        side-effects:    non state changes; no external effects
#        returns:    dict
#        nominal: 
#            dict['rotations']: string, valid rotations to get proper U12 to its proper down facing place
#            dict['cube']: string, valid cube after rotation for U12 is performed
#        abnormal: 
#            no abnormal behavior since method is only called after cube is validated and daisy is solved
#    confidence level: boundary value analysis
#
#    happy path:
#        test010: place is D01
#        test020: place is D10     
#        test030: place is D12
#        test040: place is D21      

    def test900_010PlaceIsD01(self):    
        inputDict = {}
        inputDict['cube'] = 'gogyrobgwwroggyrybwbrgoyooyygrobrorwbwbwywyborrgbwbgwy'
        expectedResult = {}
        expectedResult['rotations'] = 'UFFu'
        expectedResult['cube'] = 'gororyorwwgbrgygybwbrgoyooyygrobgorwbwrwyrybgbwobwbgwy'
        actualResult = solve._U12Down(inputDict)
        self.assertDictEqual(expectedResult, actualResult) 
        
    def test900_020PlaceIsD10(self):    
        inputDict = {}
        inputDict['cube'] = 'yggyggbgwwroooyorwyooobrrogbbryrgrywywgwywbworrbbwbybg'
        expectedResult = {}
        expectedResult['rotations'] = 'UULLUU'
        expectedResult['cube'] = 'ygbrggggwwyrooyorwgooobyroybbrgryorwywywybbwrorbwwbgbg'
        actualResult = solve._U12Down(inputDict)
        self.assertDictEqual(expectedResult, actualResult) 
        
    def test900_030PlaceIsD12(self):    
        inputDict = {}
        inputDict['cube'] = 'bbrgryorwyggrgorogwroyoorywyoogbybgwgwowywywbbbgrwbrby'
        expectedResult = {}
        expectedResult['rotations'] = 'RR'
        expectedResult['cube'] = 'bbrgryorwgorogrggywroyoorywyoogbybgwgwgwybywybborwwrbb'
        actualResult = solve._U12Down(inputDict)
        self.assertDictEqual(expectedResult, actualResult) 
        
    def test900_040PlaceIsD21(self):    
        inputDict = {}
        inputDict['cube'] = 'wgbybgrbbwggoryorwwrorgorogyooyogryygwowywbrrbwybwbybg'
        expectedResult = {}
        expectedResult['rotations'] = 'uBBU'
        expectedResult['cube'] = 'wgrybgrbbgororyorwwroogrggwyooyogbyygwgwybbrybwybwbrwo'
        actualResult = solve._U12Down(inputDict)
        self.assertDictEqual(expectedResult, actualResult) 

# 1000 _U10Down
#    inputs: 
#        parms:    dict; mandatory; arrives validated
#        parms['cube']:    string; len=54; [brgoyw]; 9 occurrences of each character, unique middle character; mandatory; arrives unvalidated
#    outputs:
#        side-effects:    non state changes; no external effects
#        returns:    dict
#        nominal: 
#            dict['rotations']: string, valid rotations to get proper U10 to its proper down facing place
#            dict['cube']: string, valid cube after rotation for U10 is performed
#        abnormal: 
#            no abnormal behavior since method is only called after cube is validated and daisy is solved
#    confidence level: boundary value analysis
#
#    happy path:
#        test010: place is D01
#        test020: place is D10     
#        test030: place is D12
#        test040: place is D21     
    
    def test1000_010PlaceIsD01(self):    
        inputDict = {}
        inputDict['cube'] = 'wgggboorwwroyrgroyyooygrrygbbbyoorgwywgwywrwobbgrwbybb'
        expectedResult = {}
        expectedResult['rotations'] = 'uFFU'
        expectedResult['cube'] = 'wggobgbbbwroorgooyyorygrrygwroyoyrgwgwgbywbworwyrwbybb'
        actualResult = solve._U10Down(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test1000_020PlaceIsD10(self):    
        inputDict = {}
        inputDict['cube'] = 'wroyoyorwyoorbgroybbborgrygwggygorgwrwywywowgbbgrwbybb'
        expectedResult = {}
        expectedResult['rotations'] = 'LL'
        expectedResult['cube'] = 'grogoybrwyoorbgroybbooryrywwgrogyggwbwyrywywgrbgwwbobb'
        actualResult = solve._U10Down(inputDict)
        self.assertDictEqual(expectedResult, actualResult) 
        
    def test1000_030PlaceIsD12(self):    
        inputDict = {}
        inputDict['cube'] = 'wroorgrygyooygorgwbbbyoyorwwggrbgroyrwywywowgbbybwrgbb'
        expectedResult = {}
        expectedResult['rotations'] = 'UURRUU'
        expectedResult['cube'] = 'grooryrywyooogyggwbbogoybrwwgrrbgroybwyrywywgbbobwwgbr'
        actualResult = solve._U10Down(inputDict)
        self.assertDictEqual(expectedResult, actualResult)  
        
    def test1000_040PlaceIsD21(self):    
        inputDict = {}
        inputDict['cube'] = 'yoogoorygbbbgbrrgwwggyryorwwroogyroyowrwywgwybbybwrgbb'
        expectedResult = {}
        expectedResult['rotations'] = 'UBBu'
        expectedResult['cube'] = 'woogoorygbbbgborgywgryryorwwrorgygoygwrbywbwybbybwrowg'
        actualResult = solve._U10Down(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
# 2000 _U01Down
#    inputs: 
#        parms:    dict; mandatory; arrives validated
#        parms['cube']:    string; len=54; [brgoyw]; 9 occurrences of each character, unique middle character; mandatory; arrives unvalidated
#    outputs:
#        side-effects:    non state changes; no external effects
#        returns:    dict
#        nominal: 
#            dict['rotations']: string, valid rotations to get proper U01 to its proper down facing place
#            dict['cube']: string, valid cube after rotation for U01 is performed
#        abnormal: 
#            no abnormal behavior since method is only called after cube is validated and daisy is solved
#    confidence level: boundary value analysis
#
#    happy path:
#        test010: place is D01
#        test020: place is D10     
#        test030: place is D12
#        test040: place is D21       
        
    def test2000_010PlaceIsD01(self):    
        inputDict = {}
        inputDict['cube'] = 'wrogborygyooyrgrgwbbbygrorwwggyooroyrwywywowgbbybwrgbb'
        expectedResult = {}
        expectedResult['rotations'] = 'UUFFUU'
        expectedResult['cube'] = 'wroobgbbbyororgogwgyrygrorwyggyoyrowbbywywowgrwybwrgbb'
        actualResult = solve._U01Down(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test2000_020PlaceIsD10(self):    
        inputDict = {}
        inputDict['cube'] = 'wrooryroyyoorgyrygbbbgoyrgwwggobgorwrwywywowggbbbwbbry'
        expectedResult = {}
        expectedResult['rotations'] = 'uLLU'
        expectedResult['cube'] = 'wroyryooyyorrgyrygwrogoorgwwgggbobbbbbgwywowgybbwwbrry'
        actualResult = solve._U01Down(inputDict)
        self.assertDictEqual(expectedResult, actualResult)  
        
    def test2000_030PlaceIsD12(self):    
        inputDict = {}
        inputDict['cube'] = 'yooyryrygbbbrggrgwwggoogorwwroyboroyowrwywgwybbybwrgbb'
        expectedResult = {}
        expectedResult['rotations'] = 'URRu'
        expectedResult['cube'] = 'yooyrorywbboggrggwwgryogbrwgroyboroyyrbwywgwybbobwwgbr'
        actualResult = solve._U01Down(inputDict)
        self.assertDictEqual(expectedResult, actualResult) 
        
    def test2000_040PlaceIsD21(self):    
        inputDict = {}
        inputDict['cube'] = 'yooyboroybbbyryrygwggrggrgwwrooogorwowrwywgwygbbbwbbry'
        expectedResult = {}
        expectedResult['rotations'] = 'BB'
        expectedResult['cube'] = 'yooyboroybboyrorywwgrggrggwgroyogbrwyrbwywgwygbbbwbrwo'
        actualResult = solve._U01Down(inputDict)
        self.assertDictEqual(expectedResult, actualResult)      
        
# 3000 _solveDownCross
#    inputs: 
#        parms:    dict; mandatory; arrives validated
#        parms['op']:    string; 'solve'; mandatory; arrives validated
#        parms['cube']:    string; len=54; [brgoyw]; 9 occurrences of each character, unique middle character; mandatory; arrives unvalidated
#    outputs:
#        side-effects:    non state changes; no external effects
#        returns:    dict
#        nominal: 
#            dict['rotations']: string, valid rotations to solve down cross
#            dict['cube']: string, valid cube after rotations for down cross are performed
#        abnormal: 
#            no abnormal behavior since method is only called if daisy is solved and cube is already validated
#    confidence level: boundary value analysis
#
#    happy path:
#        test010: valid cube with solved daisy

    def test3000_010ValidCubeWithSolvedDaisy(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'bbbrggrgwwggoogorwwroyboroyyooyryryggwowywywryrbbwbbbg'
        expectedResult = {}
        expectedResult['rotations'] = 'UUbbUUUFFuUURRUUuLLU'
        expectedResult['cube'] = 'wooygorgywggyoyroywyorbgobwbrrorgbrgybobyrgbbywbwwwrwg'
        actualResult = solve._solveDownCross(inputDict)
        self.assertDictEqual(expectedResult, actualResult)