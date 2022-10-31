'''
Created on Sep 27, 2022

@author: marymitchell
'''
import unittest
import rubik.solve as solve


class Test(unittest.TestCase):

# 100 _solveDaisy
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
   
    def test100_010ValidCubeWithUnsolvedU21Daisy(self):
        inputDict = {}
        inputDict['cube'] = 'grwrrwobobbygggyogbryyogobwrowobyboygwrwywrgogybbwyrrw'
        expectedResult = {}
        expectedResult['rotations'] = 'uRU'
        expectedResult['cube'] = 'yggrryobwrbyogrggwbrygogobwrobobyboygwrwywowwgyobwyrrb'
        actualResult = solve._solveDaisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test100_020ValidCubeWithUnsolvedU21AndU12Daisy(self):
        inputDict = {}
        inputDict['cube'] = 'wryorwyowbyoogwbygbrogogwggwbgrbbrogbwywybobrogrywryyr'
        expectedResult = {}
        expectedResult['rotations'] = 'uRUruBU'
        expectedResult['cube'] = 'bororbyogwgoygyoyybrogorggywbrbbbrogbwywywwwgogwywrbrr'
        actualResult = solve._solveDaisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test100_030ValidCubeWithUnsolvedU21U12AndU10Daisy(self):
        inputDict = {}
        inputDict['cube'] = 'bgbboyrgryyoobbwwrgrbwroyoyrbwggyogwywwryroyogrbwwogbg'
        expectedResult = {}
        expectedResult['rotations'] = 'DFFrUBUrUU'
        expectedResult['cube'] = 'ygwyogbgwobrrbyoyybrbbrboorrogrgogoyywwwywrwgoybbwrwgg'
        actualResult = solve._solveDaisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
    
    def test100_040ValidCubeWithAllUnsolvedDaisy(self):
        inputDict = {}
        inputDict['cube'] = 'owobroobgbbbyggrogwwrrowyrgyybobwwygbgrryywrywoygwgrbo'
        expectedResult = {}
        expectedResult['rotations'] = 'FRLbUru'
        expectedResult['cube'] = 'bbbrrygowyrygggrogrgororyyrwoybbywowbwgwywrwooygbwgbbo'
        actualResult = solve._solveDaisy(inputDict)
        self.assertDictEqual(expectedResult, actualResult)    
        
# 200 _solveDownCross
#    inputs: 
#        parms:    dict; mandatory; arrives validated
#        parms['cube']:    string; len=54; [brgoyw]; 9 occurrences of each character, unique middle character; mandatory; arrives validated
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

    def test200_010ValidCubeWithSolvedDaisy(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'bbbrggrgwwggoogorwwroyboroyyooyryryggwowywywryrbbwbbbg'
        expectedResult = {}
        expectedResult['rotations'] = 'UUbbUUUFFuUURRUUuLLU'
        expectedResult['cube'] = 'wooygorgywggyoyroywyorbgobwbrrorgbrgybobyrgbbywbwwwrwg'
        actualResult = solve._solveDownCross(inputDict)
        self.assertDictEqual(expectedResult, actualResult)    

# 300 _solveDownCorners
#    inputs: 
#        parms:    dict; mandatory; arrives validated
#        parms['cube']:    string; len=54; [brgoyw]; 9 occurrences of each character, unique middle character; mandatory; arrives validated
#    outputs:
#        side-effects:    non state changes; no external effects
#        returns:    dict
#        nominal: 
#            dict['rotations']: string, valid rotations to solve down corners
#            dict['cube']: string, valid cube after rotations for down corners are performed
#        abnormal: 
#            no abnormal behavior since method is only called if down cross is solved and cube is already validated
#    confidence level: boundary value analysis
#
#    happy path:
#        test010: valid down cross with unsolved corners

    def test300_010ValidDownCrossWithUnsolvedCorners(self):
        inputDict = {}
        inputDict['cube'] = 'brrybobbgwbryryyrryboggyygbgorborwoywrbgyowggowowwwowg'
        expectedResult = {}
        expectedResult['rotations'] = 'LUllUULURurLUluLUluruuRUruR'
        expectedResult['cube'] = 'gyyrbybbborgrrbrrrobrogggggyyroobooobyygygyobwwwwwwwww'
        actualResult = solve._solveDownCorners(inputDict)
        self.assertDictEqual(expectedResult, actualResult)

# 400 _solveBottomDaisyPiece
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

    def test400_010PieceIsR10(self):
        inputDict = {}
        inputDict['cube'] = 'yywyrooyyrogwgwgworworoybbwbgrbbggryygwrygbobgrrbwboow'
        expectedResult = {}
        expectedResult['rotations'] = 'f'
        expectedResult['cube'] = 'woyyryyyorogrgwgworworoybbwbgbbbogrbygwrygrwgrgybwboow'
        actualResult = solve._solveBottomDaisyPiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)

    def test400_020PieceIsF01(self):
        inputDict = {}
        inputDict['cube'] = 'bwrobrggrbbybroyrogobbgybbwygygoyrrwowowywrrwooggwygyw'
        expectedResult = {}
        expectedResult['rotations'] = 'FuRU'
        expectedResult['cube'] = 'wrggbyrrwwbyrrooobgobygyybwygbgoorrgowowywrwoybbgwbgyr'
        actualResult = solve._solveBottomDaisyPiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test400_030PieceIsF10(self):
        inputDict = {}
        inputDict['cube'] = 'rrrwogwygwbyybrogrgobbroyobygwygrybbowowywbggorwyworbg'
        expectedResult = {}
        expectedResult['rotations'] = 'Ulu'
        expectedResult['cube'] = 'rrbyogrygobyybrogrgobbrgyobyggrgbryyowowywwwwbrwowowbg'
        actualResult = solve._solveBottomDaisyPiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test400_040PieceIsF12(self):
        inputDict = {}
        inputDict['cube'] = 'bggrgwrywwbyroyryrgobrbrbgrygwbrgyobowowywoyowogbwbgoy'
        expectedResult = {}
        expectedResult['rotations'] = 'uRU'
        expectedResult['cube'] = 'rrbrgbryyobyyogryggobybrogryggbrgyobowowywwwwwobbwrgow'
        actualResult = solve._solveBottomDaisyPiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test400_050PieceIsF21(self):
        inputDict = {}
        inputDict['cube'] = 'ybborbwwyobyygyrrrgoboogwygyggybboggowowywrrwrrbowgwrb'
        expectedResult = {}
        expectedResult['rotations'] = 'fuRU'
        expectedResult['cube'] = 'rrbbrgyobobyrgbryygobyogrygyggybrogrowowywwwwgbwowowrb'
        actualResult = solve._solveBottomDaisyPiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test400_060PieceIsR01(self):
        inputDict = {}
        inputDict['cube'] = 'rygoowwywowwrbgryoboborowbyygbbgygrrowowybybybrggwgrrg'
        expectedResult = {}
        expectedResult['rotations'] = 'rf'
        expectedResult['cube'] = 'obyyoyrowggorbybrrgobgrogbyygbbgbgryowwwyowwobyrgwwrrw'
        actualResult = solve._solveBottomDaisyPiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test400_070PieceIsR12(self):
        inputDict = {}
        inputDict['cube'] = 'bgybggyoyboroowbygbbgrbrrbwwgwbrorggowwwywoyroyorwrgyy'
        expectedResult = {}
        expectedResult['rotations'] = 'uuBUU'
        expectedResult['cube'] = 'rrbbggyoyoorooybygbbgbbgwrywgyyrorggowwwywgwwoyorwrbbr'
        actualResult = solve._solveBottomDaisyPiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test400_080PieceIsR21(self):
        inputDict = {}
        inputDict['cube'] = 'yybbgyrgbybgooowwwwgygbgrrbrroyrorrygwowywgbobrobwowyg'
        expectedResult = {}
        expectedResult['rotations'] = 'uruBUU'
        expectedResult['cube'] = 'oobbgbrggybgyoyyowwgyrbobgwrrbgrorrygwowywwwobrobwygyr'
        actualResult = solve._solveBottomDaisyPiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test400_090PieceIsB01(self):
        inputDict = {}
        inputDict['cube'] = 'ggrgobggwborybwoyoyworrbwbgbbwrgorooygbwywrywyrbywryog'
        expectedResult = {}
        expectedResult['rotations'] = 'burU'
        expectedResult['cube'] = 'rgbgoyggrroygbygyoobgrrbbrwybwogogoorrbwywbwyyrwywboww'
        actualResult = solve._solveBottomDaisyPiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)    
        
    def test400_1000PieceIsB10(self):   
        inputDict = {}
        inputDict['cube'] = 'brwoogoyrorwrbgbygbbrwrrygrgorbgygbbywowywwygygyowbwoo'
        expectedResult = {}
        expectedResult['rotations'] = 'urU'
        expectedResult['cube'] = 'wggooyoyworwrbybrbbbrbrrygrgogbgygbbywowywowyygrowgwor'
        actualResult = solve._solveBottomDaisyPiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)    
        
    def test400_2000PieceIsB12(self):
        inputDict = {}
        inputDict['cube'] = 'gywgbyyrbrrwbrrygrbbrbgwgbogoygoywooywowyworbbgrywogow'
        expectedResult = {}
        expectedResult['rotations'] = 'ULu'
        expectedResult['cube'] = 'wggrbybrborwbrrygrbbrbgygbbgogooyoywywowywowyrgrgwoyow'
        actualResult = solve._solveBottomDaisyPiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)      
        
    def test400_3000PieceIsB21(self):
        inputDict = {}
        inputDict['cube'] = 'bywbroygyrogbgrbyrwggboygwyorwgbygrbywowyworbroogworbw'
        expectedResult = {}
        expectedResult['rotations'] = 'uubuLu'
        expectedResult['cube'] = 'wbwgroggyrogbgrbyowggyogbbrorrrbybyyywowywgwbroobwoyrw'
        actualResult = solve._solveBottomDaisyPiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)  
        
    def test400_4000PieceIsL01(self):
        inputDict = {}
        inputDict['cube'] = 'rgbyowyoowgbbbrgybroobrgorowwgoggwbrbwyrywwrrgyyowbgyy'
        expectedResult = {}
        expectedResult['rotations'] = 'LF'
        expectedResult['cube'] = 'wrboogowbogbrbrrybrogbroorgworbgyrgyowygywgwwgbwywbyyy'
        actualResult = solve._solveBottomDaisyPiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)  
        
    def test400_5000PieceIsL10(self):
        inputDict = {}
        inputDict['cube'] = 'bggyggoyryggrobbyborrrbowyowbrwrgyoggwywywworwoybwrbbo'
        expectedResult = {}
        expectedResult['rotations'] = 'UUbuu'
        expectedResult['cube'] = 'gooyggoyrbggroobyworrgbybrwwbrbrgooggwywywywywoybwrbbr'
        actualResult = solve._solveBottomDaisyPiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)  
        
    def test400_6000PieceIsL12(self):
        inputDict = {}
        inputDict['cube'] = 'gowgoybrbrrrrbyyrwwbrbrgooggoyygwoyyywgwywogbogrowbwbb'
        expectedResult = {}
        expectedResult['rotations'] = 'F'
        expectedResult['cube'] = 'bggroobyworrgbybrwwbrbrgooggooyggoyrywgwywywyyrrowbwbb'
        actualResult = solve._solveBottomDaisyPiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)      
        
    def test400_7000PieceIsL21(self):
        inputDict = {}
        inputDict['cube'] = 'oggbggwyrwbrrobbybgoorbowywbgggrobwgywywywyyoroyrwrrbo'
        expectedResult = {}
        expectedResult['rotations'] = 'UluF'
        expectedResult['cube'] = 'rrgygorggwbrbobwybgoorbywyybgwgroogyywywywbwobrrowrgbo'
        actualResult = solve._solveBottomDaisyPiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)   
        
    def test400_8000PieceIsD01(self):
        inputDict = {}
        inputDict['cube'] = 'yrgbobgowygooborrwgrwgrooyrrbbygrbbobwwwywoyrywgywgygb'
        expectedResult = {}
        expectedResult['rotations'] = 'FF'
        expectedResult['cube'] = 'wogbobgryogorbobrwgrwgrooyrrbrygobbybwwwywgwyryoywgygb'
        actualResult = solve._solveBottomDaisyPiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult) 
    
    def test400_9000PieceIsD10(self):
        inputDict = {}
        inputDict['cube'] = 'yrgbobrrwygoobooyrgrwgrobborbbygrgowbwwwywoyrggbwwgyyy'
        expectedResult = {}
        expectedResult['rotations'] = 'DFF'
        expectedResult['cube'] = 'wogbobgryogorbobrwgrwgrooyrrbrygobbybwwwywgwyryoywgygb'
        actualResult = solve._solveBottomDaisyPiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)  
        
    def test400_9010PieceIsD12(self):
        inputDict = {}
        inputDict['cube'] = 'ryoorgbrrwbrogowrgwogbobobyogbrbygryywgwywygbogbywwryw'
        expectedResult = {}
        expectedResult['rotations'] = 'dFF'
        expectedResult['cube'] = 'grwgrooyrrbrygobbywogbobgryogorbobrwywgwywwwbbgygwyoyr'
        actualResult = solve._solveBottomDaisyPiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)  
        
    def test400_9020PieceIsD21(self):
        inputDict = {}
        inputDict['cube'] = 'ryoorggrywbrogobrrwogbobwrgogbrbyobyywgwywygbryoywgwwb'
        expectedResult = {}
        expectedResult['rotations'] = 'ddFF'
        expectedResult['cube'] = 'grwgrooyrrbrygobbywogbobgryogorbobrwywgwywwwbbgygwyoyr'
        actualResult = solve._solveBottomDaisyPiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)  
        
# 500 _solveRightDaisyPiece
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
#        test4000: piece is F10
#        test5000: piece is F12
#        test6000: piece is F21 
#        test7000: piece is D01
#        test8000: piece is D10
#        test9000: piece is D12
#        test9010: piece is D21       

    def test500_010PieceIsR01(self):
        inputDict = {}
        inputDict['cube'] = 'gbgyoygrwwwrrbbryybrbyrbrobyoyrgowoyowwwygoworgggwgobb'
        expectedResult = {}
        expectedResult['rotations'] = 'rUfu'
        expectedResult['cube'] = 'gbrborrygygogbyrrrgrbgrbgobyoyrgywobowwwywowbwoygwyobw'
        actualResult = solve._solveRightDaisyPiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult) 
    
    def test500_020PieceIsR10(self):   
        inputDict = {}
        inputDict['cube'] = 'groogobyywryworoygobrgbyrrrygogrggowbwbwybwwbrbgbwowyy'
        expectedResult = {}
        expectedResult['rotations'] = 'Ufu'
        expectedResult['cube'] = 'grbrgywobyoyborryggbrgbyrrrygogrbgobbwowywwwoogwbwowyy'
        actualResult = solve._solveRightDaisyPiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult) 
        
    def test500_030PieceIsR12(self):   
        inputDict = {}
        inputDict['cube'] = 'grogrbgobyrgrgwwooybrooyybrygoobywrrbwrwygwwgwboywgbyb'
        expectedResult = {}
        expectedResult['rotations'] = 'uBU'
        expectedResult['cube'] = 'grbgrbgobyoyrgywobgbrborrygygogbyrrrbwowywwwowboywgyow'
        actualResult = solve._solveRightDaisyPiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult) 
        
    def test500_040PieceIsR21(self):   
        inputDict = {}
        inputDict['cube'] = 'grwgbbrrbggyoryowbgbrbgorrwygogoroygbwowyywwryyyowobbw'
        expectedResult = {}
        expectedResult['rotations'] = 'ruBU'
        expectedResult['cube'] = 'grbgbyrrryoygrbgobgbrrgywobygoborrygbwowywwwoyywowbwgo'
        actualResult = solve._solveRightDaisyPiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult) 
        
    def test500_050PieceIsB01(self):   
        inputDict = {}
        inputDict['cube'] = 'obrworbygybwgbyrrrbwggrggowwggogrbyyooowyrywbooybwyrbw'
        expectedResult = {}
        expectedResult['rotations'] = 'br'
        expectedResult['cube'] = 'obwworbybooobbrygrwgwyroyggrggbgrwyybobwywywgoorbwrryg'
        actualResult = solve._solveRightDaisyPiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult) 
     
    def test500_060PieceIsB10(self):   
        inputDict = {}
        inputDict['cube'] = 'oooyroyggwgwbgrwyyrggworbybobwbbrygrywbwyogwbgyrrwbroo'
        expectedResult = {}
        expectedResult['rotations'] = 'r'
        expectedResult['cube'] = 'oobyroygbwryggywbwoggborrybobwbbrygrywbwywgwrgyorworog'
        actualResult = solve._solveRightDaisyPiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)  
    
    def test500_070PieceIsB12(self):   
        inputDict = {}
        inputDict['cube'] = 'ooyyroyggbybbgbwyryggrowwgwobwrbrogrywowyogwrgyrrwbbob'
        expectedResult = {}
        expectedResult['rotations'] = 'uuLuu'
        expectedResult['cube'] = 'ooborooggorbbgbwyrrggrorwggobwgbyrrbywywywgwwyyrywbyob'
        actualResult = solve._solveRightDaisyPiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)   
        
    def test500_080PieceIsB21(self):   
        inputDict = {}
        inputDict['cube'] = 'rgbbgoyggwrwgoywygoobobrywborbyroogrwwgwybywrgyrrwbybo'
        expectedResult = {}
        expectedResult['rotations'] = 'druBU'
        expectedResult['cube'] = 'rggbgbwyrobwrorwggoobgbyrrborborooggwwgwywywyrbbywoyyy'
        actualResult = solve._solveRightDaisyPiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)   
        
    def test500_090PieceIsL01(self):   
        inputDict = {}
        inputDict['cube'] = 'wgowgbyyrbrbrorwggobygbyyyrrwggrrgobgwwoyyowyrbbbwowoo'
        expectedResult = {}
        expectedResult['rotations'] = 'LUFu'
        expectedResult['cube'] = 'ggwygrrbboobyorwggybwgbbyyrggrorbbrbrwoyywywgwrowwoyoo'
        actualResult = solve._solveRightDaisyPiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)   
        
    def test500_1000PieceIsL10(self):   
        inputDict = {}
        inputDict['cube'] = 'ybbrrgybrwyyygrybbggwyorwgroobwbggobgwowyoowrrygbwrwoo'
        expectedResult = {}
        expectedResult['rotations'] = 'ubU'
        expectedResult['cube'] = 'yborrgybryrrygoybrwgwyogwywoobobgoobgwgwywowgrygbwrbrb'
        actualResult = solve._solveRightDaisyPiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)     
        
    def test500_2000PieceIsL12(self):   
        inputDict = {}
        inputDict['cube'] = 'ybgrgbyyyrorroggywbgwobgooboobrrwybggwwwyyowwogrywrrbb'
        expectedResult = {}
        expectedResult['rotations'] = 'UFu'
        expectedResult['cube'] = 'yboygoybryrryogwywwgwobgooboobrrgybrgwgwywowggrbywrrbb'
        actualResult = solve._solveRightDaisyPiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult) 
    
    def test500_3000PieceIsL21(self):   
        inputDict = {}
        inputDict['cube'] = 'oorobywyyyrobrogywyrrygboobwgwrogowrgwgwyggwbbgrbwrybb'
        expectedResult = {}
        expectedResult['rotations'] = 'UULUbU'
        expectedResult['cube'] = 'oorgbygyyybbbrbgybwrrrgooyowgwborbgogwrwywgwbygrowrwoy'
        actualResult = solve._solveRightDaisyPiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult) 
    
    def test500_4000PieceIsF10(self):   
        inputDict = {}
        inputDict['cube'] = 'ooywbgyybbygrroryoorrbgybrowgwoobygrgwywyggwrgbwowrbbw'
        expectedResult = {}
        expectedResult['rotations'] = 'uuluu'
        expectedResult['cube'] = 'ooyobgbybgbrrroryogrrbggbrrwgwyogboygwywywgwoobwywrybw'
        actualResult = solve._solveRightDaisyPiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test500_5000PieceIsF12(self):   
        inputDict = {}
        inputDict['cube'] = 'grgbgwbrgwgygoowybooyybgyybgbrrroryoowbwyoywowbrrwgwbr'
        expectedResult = {}
        expectedResult['rotations'] = 'R'
        expectedResult['cube'] = 'grrbggbrrwgwyogboyooyobgbybgbrrroryoowgwywywgwbyrwywbo'
        actualResult = solve._solveRightDaisyPiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
    
    def test500_6000PieceIsF21(self):
        inputDict = {}
        inputDict['cube'] = 'gbwobrywrrrryrgbbbwgwygrwoyooybogbyrgwgwygowbgrybwooyo'
        expectedResult = {}
        expectedResult['rotations'] = 'UfuR'
        expectedResult['cube'] = 'gbrrboroogrrbrrbgrwgwygrboyooybogbybgwgwywowywgwbwyoyy'
        actualResult = solve._solveRightDaisyPiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test500_7000PieceIsD01(self):
        inputDict = {}
        inputDict['cube'] = 'grggrbrbrybbogywryrogoobbrwogorbooywywywyywwrgwbgwybgo'
        expectedResult = {}
        expectedResult['rotations'] = 'DRR'
        expectedResult['cube'] = 'grwgrooyrrbrygobbywogbobgryogorbobrwywgwywwwbbgygwyoyr'
        actualResult = solve._solveRightDaisyPiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
    
    def test500_8000PieceIsD10(self):
        inputDict = {}
        inputDict['cube'] = 'grggrbwryybbogybrwrogooboywogorborbrywywyywwrbyowwgggb'
        expectedResult = {}
        expectedResult['rotations'] = 'DDRR'
        expectedResult['cube'] = 'grwgrooyrrbrygobbywogbobgryogorbobrwywgwywwwbbgygwyoyr'
        actualResult = solve._solveRightDaisyPiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
    
    def test500_9000PieceIsD12(self):
        inputDict = {}
        inputDict['cube'] = 'grggrboywybbogyrbrrogoobwryogorbobrwywywyywwrbgggwwoyb'
        expectedResult = {}
        expectedResult['rotations'] = 'RR'
        expectedResult['cube'] = 'grwgrooyrrbrygobbywogbobgryogorbobrwywgwywwwbbgygwyoyr'
        actualResult = solve._solveRightDaisyPiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test500_9010PieceIsD21(self):
        inputDict = {}
        inputDict['cube'] = 'grggrbbrwybbogyoywrogoobrbrogorbowryywywyywwrogbywgbwg'
        expectedResult = {}
        expectedResult['rotations'] = 'dRR'
        expectedResult['cube'] = 'grwgrooyrrbrygobbywogbobgryogorbobrwywgwywwwbbgygwyoyr'
        actualResult = solve._solveRightDaisyPiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
# 600 _solveLeftDaisyPiece
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
#        test050: piece is F10
#        test060: piece is F12
#        test070: piece is F21
#        test080: piece is R10
#        test090: piece is R12
#        test1000: piece is R21
#        test2000: piece is B01
#        test3000: piece is B10
#        test4000: piece is B12
#        test5000: piece is B21 
#        test6000: piece is D01
#        test7000: piece is D10
#        test8000: piece is D12
#        test9000: piece is D21        

    def test600_010PieceIsL01(self):
        inputDict = {}
        inputDict['cube'] = 'wrgoobwryrogrbgbrgogyyroobrrwoyggbbrgwybywbwwbyoywgyow'
        expectedResult = {}
        expectedResult['rotations'] = 'LuFU'
        expectedResult['cube'] = 'rrgroyybrrogobgyrgogwyryobbbbbbgyrgoowywywywwbrgowgwow'
        actualResult = solve._solveLeftDaisyPiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test600_020PieceIsL10(self):
        inputDict = {}
        inputDict['cube'] = 'wgwbgyrgobbbrogybwrrgrbogggyorwryybbrwyyywgwowobowroyo'
        expectedResult = {}
        expectedResult['rotations'] = 'Ubu'
        expectedResult['cube'] = 'ogwbgyrgobbbroyybrrrgobgyrgrogyryobbwwywywywowobowrwgg'
        actualResult = solve._solveLeftDaisyPiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test600_030PieceIsL12(self):
        inputDict = {}
        inputDict['cube'] = 'wgworbryobbbogywgorryroyybrgybobwyrwowybywrwoggggwogrb'
        expectedResult = {}
        expectedResult['rotations'] = 'uFU'
        expectedResult['cube'] = 'ogwyryobbbbbbgyrgorrgroyybrrogobgyrgwwywywywowowgwogrb'
        actualResult = solve._solveLeftDaisyPiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test600_040PieceIsL21(self):
        inputDict = {}
        inputDict['cube'] = 'bbbbrbryorrgogywgorogrogybgyowrbyywbrwwyywowywgggwoorb'
        expectedResult = {}
        expectedResult['rotations'] = 'LUbu'
        expectedResult['cube'] = 'rbbyrboyorrgoggwggrogrobyryygwrbobywrwwwywbwybggbwooyo'
        actualResult = solve._solveLeftDaisyPiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test600_050PieceIsF10(self):
        inputDict = {}
        inputDict['cube'] = 'yogwrbwywygoyggbgbbbgoorwryworybrorgowybywbwrrorbwyggo'
        expectedResult = {}
        expectedResult['rotations'] = 'l'
        expectedResult['cube'] = 'rogbrbgywygoyggbgbbbboobwrorrgobrwyoywywywwwryorrwyggo'
        actualResult = solve._solveLeftDaisyPiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test600_060PieceIsF12(self):
        inputDict = {}
        inputDict['cube'] = 'obbbrwgyrrrggggyybroyyobrroogbobrwyobwwoywwwyyogrwbggw'
        expectedResult = {}
        expectedResult['rotations'] = 'uuRuu'
        expectedResult['cube'] = 'bbbbrbgywrrgyggbgbrogoobwroygoobrwyorwwwywywyyorrwyggo'
        actualResult = solve._solveLeftDaisyPiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test600_070PieceIsF21(self):
        inputDict = {}
        inputDict['cube'] = 'rogoggywbygoyobwybbbyoborrogbgyrgwybowyrywwwrrrorwbggw'
        expectedResult = {}
        expectedResult['rotations'] = 'uFUl'
        expectedResult['cube'] = 'wogrgbgggygorobwybbbyobgrrbgrooryyywowywywbwroyrowbrgw'
        actualResult = solve._solveLeftDaisyPiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test600_080PieceIsR10(self):
        inputDict = {}
        inputDict['cube'] = 'borbbrrrgbgwwrorbwbbgggogrboyyboyoywywooywrwwggygwryyo'
        expectedResult = {}
        expectedResult['rotations'] = 'ufU'
        expectedResult['cube'] = 'yorybrobrbgwgrogbwbbrggogrbyrgboooyybwowywrwwgywgwryyo'
        actualResult = solve._solveLeftDaisyPiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)   
        
    def test600_090PieceIsR12(self):
        inputDict = {}
        inputDict['cube'] = 'ogwboooyybbrybwobryrworbyggrowrgowrbbwbgywgwoyggywyrrg'
        expectedResult = {}
        expectedResult['rotations'] = 'UBu'
        expectedResult['cube'] = 'bgwboooyybbrybrobryrggrogbwyorggogrbrwbwywwwoyggywyorw'
        actualResult = solve._solveLeftDaisyPiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)   
        
    def test600_1000PieceIsR21(self):
        inputDict = {}
        inputDict['cube'] = 'yrgybrobwyorbroowbbgwbgroggggryoooyyrwwrywbwrgybgwbwoy'
        expectedResult = {}
        expectedResult['rotations'] = 'uuruBu'
        expectedResult['cube'] = 'yrgybrobryorgrogbwbgwggogrbbbrboooyyowwwywbwrgywgwryyo'
        actualResult = solve._solveLeftDaisyPiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)  
        
    def test600_2000PieceIsB01(self):
        inputDict = {}
        inputDict['cube'] = 'gbrgbobgowrrbrrwgbgwybgroywbyyyowobwroygywowgrogywrboy'
        expectedResult = {}
        expectedResult['rotations'] = 'BL'
        expectedResult['cube'] = 'rbrgboogowrybrowgbobbygywrrroyboywwyyrbwywgwggoggwrbyo'
        actualResult = solve._solveLeftDaisyPiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult) 
        
    def test600_3000PieceIsB10(self):
        inputDict = {}
        inputDict['cube'] = 'wbwybbyyorgoyrrgyywowwgorgborrborobrgwbgywgwbgoyrwgyob'
        expectedResult = {}
        expectedResult['rotations'] = 'UUrUU'
        expectedResult['cube'] = 'bbwybgyygrgorryoygwogggoygbrryborobrwwbwywrwbgowrwbyoo'
        actualResult = solve._solveLeftDaisyPiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)  
    
    def test600_4000PieceIsB12(self):
        inputDict = {}
        inputDict['cube'] = 'ybwybbyyorgoyrbgywwooogwrrobgrrorwbrywboywbwbgoyrwgggg'
        expectedResult = {}
        expectedResult['rotations'] = 'L'
        expectedResult['cube'] = 'ybwobbbyorgoyrbgywwogogrrrgwrbbogrrrowbwywowbyoyywgygg'
        actualResult = solve._solveLeftDaisyPiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)  
        
    def test600_5000PieceIsB21(self):
        inputDict = {}
        inputDict['cube'] = 'ybwybbyyorgoyrggygwogrggowrroboorbbrwwbbywowbgoyrwgyrw'
        expectedResult = {}
        expectedResult['rotations'] = 'UBUrUU'
        expectedResult['cube'] = 'bbwybgyygrgorryoygwogggoygbrryborobrwwbwywrwbgowrwbyoo'
        actualResult = solve._solveLeftDaisyPiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)  
        
    def test600_6000PieceIsD01(self):
        inputDict = {}
        inputDict['cube'] = 'bbwobgyrrrgorrygygwoyggyoygrborobygbgwbrywywbrwwowoobw'
        expectedResult = {}
        expectedResult['rotations'] = 'dll'
        expectedResult['cube'] = 'bbwybgyygrgorryoygwogggoygbrryborobrwwbwywrwbgowrwbyoo'
        actualResult = solve._solveLeftDaisyPiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult) 
    
    def test600_7000PieceIsD10(self):
        inputDict = {}
        inputDict['cube'] = 'bbwobggygrgorryoygwoyggyygbrborobyrrgwbrywywbwowwwbroo'
        expectedResult = {}
        expectedResult['rotations'] = 'll'
        expectedResult['cube'] = 'bbwybgyygrgorryoygwogggoygbrryborobrwwbwywrwbgowrwbyoo'
        actualResult = solve._solveLeftDaisyPiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
    
    def test600_8000PieceIsD12(self):
        inputDict = {}
        inputDict['cube'] = 'bbwobgygbrgorryyrrwoyggygygrboroboyggwbrywywboorbwwwow'
        expectedResult = {}
        expectedResult['rotations'] = 'ddll'
        expectedResult['cube'] = 'bbwybgyygrgorryoygwogggoygbrryborobrwwbwywrwbgowrwbyoo'
        actualResult = solve._solveLeftDaisyPiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult) 
        
    def test600_9000PieceIsD21(self):
        inputDict = {}
        inputDict['cube'] = 'bbwobgoygrgorryygbwoyggyyrrrborobgyggwbrywywbwboowowwr'
        expectedResult = {}
        expectedResult['rotations'] = 'Dll'
        expectedResult['cube'] = 'bbwybgyygrgorryoygwogggoygbrryborobrwwbwywrwbgowrwbyoo'
        actualResult = solve._solveLeftDaisyPiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)      
        
# 700 _solveTopDaisyPiece
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
#        test050: piece is L10
#        test060: piece is L12
#        test070: piece is L21
#        test080: piece is F10
#        test090: piece is F12
#        test1000: piece is F21
#        test2000: piece is R10
#        test3000: piece is R12
#        test4000: piece is R21 
#        test5000: piece is D01
#        test6000: piece is D10
#        test7000: piece is D12
#        test8000: piece is D21        
    
    def test700_010PieceIsB01(self):
        inputDict = {}
        inputDict['cube'] = 'rbgooggyrwgwobybbgbwyoryyrbrowggbogrgrowywbwowbyrwryyo'
        expectedResult = {}
        expectedResult['rotations'] = 'bUru'
        expectedResult['cube'] = 'rbgooggyrwgoybbyobbrorrryoywowygbogrbwywywbwowbgrwggyr'
        actualResult = solve._solveTopDaisyPiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test700_020PieceIsB10(self):
        inputDict = {}
        inputDict['cube'] = 'wowooggyrrbgobgbboyywwrryoyoroygbogrggrwywbwbwbyrwrgyb'
        expectedResult = {}
        expectedResult['rotations'] = 'Uru'
        expectedResult['cube'] = 'wowooggyrrbgybbyobwgorrryoybroygbogrywowywbwbwbgrwggyr'
        actualResult = solve._solveTopDaisyPiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test700_030PieceIsB12(self):
        inputDict = {}
        inputDict['cube'] = 'wowygbrgrrbyooggyroryybwyoogrogrowryoybwywbwbbrwbwbggg'
        expectedResult = {}
        expectedResult['rotations'] = 'uLU'
        expectedResult['cube'] = 'wowygbogrrbgooggyrwgoybbyobbrorrryoyywowywbwbgrwywbrgg'
        actualResult = solve._solveTopDaisyPiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
    
    def test700_040PieceIsB21(self):
        inputDict = {}
        inputDict['cube'] = 'wowooggyrrbgobgbbrwryyroywygroygbbgroyowywbwbwbyrwrogg'
        expectedResult = {}
        expectedResult['rotations'] = 'BUru'
        expectedResult['cube'] = 'wowooggyrrbgybbyobwgorrryoybroygbogrywowywbwbwbgrwggyr'
        actualResult = solve._solveTopDaisyPiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test700_050PieceIsL10(self):
        inputDict = {}
        inputDict['cube'] = 'brwbbowyyrbogrrgoygbwygoogybgowoyrogorwwywywbrgrbwybrg'
        expectedResult = {}
        expectedResult['rotations'] = 'b'
        expectedResult['cube'] = 'brwbbowyyrbogrrgowwoybgggyobgoroygogrwbwywywbrgrbwyyro'
        actualResult = solve._solveTopDaisyPiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test700_060PieceIsL12(self):
        inputDict = {}
        inputDict['cube'] = 'woyrbybbwbgbgrrrowwoybgggyorborowgoyggrwywbwroygbwyyro'
        expectedResult = {}
        expectedResult['rotations'] = 'uuFuu'
        expectedResult['cube'] = 'woybbowyybgogrrgowbrwbgggyorboroygogbwywywbwrrgrbwyyro'
        actualResult = solve._solveTopDaisyPiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)  
        
    def test700_070PieceIsL21(self):
        inputDict = {}
        inputDict['cube'] = 'brwgbygbwrbygrrrowgrybgbgyobgoooobwyrgowywywbrygowywro'
        expectedResult = {}
        expectedResult['rotations'] = 'uLUb'
        expectedResult['cube'] = 'brwgbyrbwrbygrbroogorogybbgggororooyywowywywbbyggwywrw'
        actualResult = solve._solveTopDaisyPiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult) 
        
    def test700_080PieceIsF10(self):
        inputDict = {}
        inputDict['cube'] = 'gbwwooyogbrwbbbygrorbyrobgrworygggborygwywywobgorwrwyy'
        expectedResult = {}
        expectedResult['rotations'] = 'ulU'
        expectedResult['cube'] = 'gbwroowogbrrbbbygrbgoyrybggborrgboygywwwywyworgoowrwyy'
        actualResult = solve._solveTopDaisyPiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult) 
        
    def test700_090PieceIsF12(self):
        inputDict = {}
        inputDict['cube'] = 'bgorgwoyybooboogrwwoggbbrgrorryrybggybbwywwwyworywbyrg'
        expectedResult = {}
        expectedResult['rotations'] = 'URu'
        expectedResult['cube'] = 'bgorgboygborroowoggbwbbbygrbrryrybggowywywwwyworywgyro'
        actualResult = solve._solveTopDaisyPiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult) 
        
    def test700_1000PieceIsF21(self):
        inputDict = {}
        inputDict['cube'] = 'gbwrooowybrrgbbbgrbogyrobgroorygygbgybwwywywowgorwrwyy'
        expectedResult = {}
        expectedResult['rotations'] = 'UUfuRu'
        expectedResult['cube'] = 'gbwoorbrybrggborbywgggrobgroorygbgbwywowywyworybrwywyo'
        actualResult = solve._solveTopDaisyPiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult) 
        
    def test700_2000PieceIsR10(self):
        inputDict = {}
        inputDict['cube'] = 'borygggbwgbwwoobrgboggbbygrwroyrobgrobowywywywrrywyyro'
        expectedResult = {}
        expectedResult['rotations'] = 'UUfUU'
        expectedResult['cube'] = 'borogbbyggboroowrgggwgbbygrrroyrbbgobwwwywywyworywyyro'
        actualResult = solve._solveTopDaisyPiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)         
        
    def test700_3000PieceIsR12(self):
        inputDict = {}
        inputDict['cube'] = 'rroyrbbgobowogwbyyoogborgrwogwybbrgryggwywbwyyywrwogbr'
        expectedResult = {}
        expectedResult['rotations'] = 'B'
        expectedResult['cube'] = 'rroyrbbgoborogbbyggboroowrgggwgbbygrwwywywbwyyywrwooyr'
        actualResult = solve._solveTopDaisyPiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)    
        
    def test700_4000PieceIsR21(self):
        inputDict = {}
        inputDict['cube'] = 'ggwgbyygorrygrbywgbyrrgywobgboooowrgybrwywwwborbywoobr'
        expectedResult = {}
        expectedResult['rotations'] = 'UruB'
        expectedResult['cube'] = 'ggwgbbygrrroyrbbgoborogbbyggboroowrgywywywwwboryywyrow'
        actualResult = solve._solveTopDaisyPiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult) 
        
    def test700_5000PieceIsD01(self):
        inputDict = {}
        inputDict['cube'] = 'gborooorrggbgbowygogbbrywrgrorbgbygbyywwywywwywbrwooyr'
        expectedResult = {}
        expectedResult['rotations'] = 'DDBB'
        expectedResult['cube'] = 'gboroowrgggwgbbygrrroyrbbgoborogbbygywbwywywwryoowrwyy'
        actualResult = solve._solveTopDaisyPiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult) 
    
    def test700_6000PieceIsD10(self):
        inputDict = {}
        inputDict['cube'] = 'borogbogogbbroybygrgybbgwrrgroorbwggorywywywywywwwobyr'
        expectedResult = {}
        expectedResult['rotations'] = 'dBB'
        expectedResult['cube'] = 'borogbbyggboroowrgggwgbbygrrroyrbbgobwwwywywyworywyyro'
        actualResult = solve._solveTopDaisyPiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult) 
    
    def test700_7000PieceIsD12(self):
        inputDict = {}
        inputDict['cube'] = 'ggwyrrbggrrwbgorobgybbooorgobogbbygrworwywwwbyyyrwwoyy'
        expectedResult = {}
        expectedResult['rotations'] = 'DBB'
        expectedResult['cube'] = 'ggwyrrygrrrobggbgoboroobbyggboobbwrgywywywwwboryywyrow'
        actualResult = solve._solveTopDaisyPiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test700_8000PieceIsD21(self):
        inputDict = {}
        inputDict['cube'] = 'ggwyrrygrrrwbgobgggybboorobobogbborgworwywwwboryywyywy'
        expectedResult = {}
        expectedResult['rotations'] = 'BB'
        expectedResult['cube'] = 'ggwyrrygrrrobggbgoboroobbyggboobbwrgywywywwwboryywyrow'
        actualResult = solve._solveTopDaisyPiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)     
          
# 800 _putBottomDaisyInDownCross
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
        actualResult = solve._putBottomDaisyInDownCross(inputDict)
        self.assertDictEqual(expectedResult, actualResult) 
    
    def test800_020PlaceIsD10(self):    
        inputDict = {}
        inputDict['cube'] = 'broygogogwbryoyrrwygorbgbgwyooorgrywgwbwywywbobybwbgrr'
        expectedResult = {}
        expectedResult['rotations'] = 'ULLu'
        expectedResult['cube'] = 'wyrggooogwbryoyrrwygorbybgwyoggroorbgwbwywobgybywwbbrr'
        actualResult = solve._putBottomDaisyInDownCross(inputDict)
        self.assertDictEqual(expectedResult, actualResult)        
        
    def test800_030PlaceIsD12(self):    
        inputDict = {}
        inputDict['cube'] = 'yooygogogbroyoyrrwwbrrbgbgwygoorgrywbwbwywgwyobybwbgrr'
        expectedResult = {}
        expectedResult['rotations'] = 'urrU'
        expectedResult['cube'] = 'wrrygrgobgroyoyooywbrobgogwygborgrywbwbwywrbyobybwwgrg'
        actualResult = solve._putBottomDaisyInDownCross(inputDict)
        self.assertDictEqual(expectedResult, actualResult)   
    
    def test800_034PlaceIsD21(self):    
        inputDict = {}
        inputDict['cube'] = 'yooorygogbrorgyrrwwbrgoybgwygoobgrywbwbwywgwyobybwbgrr'
        expectedResult = {}
        expectedResult['rotations'] = 'UUbbUU'
        expectedResult['cube'] = 'wgborygogwrorgorrbwbryogooyygrybgoywbwbwywgrrobybwbgwy'
        actualResult = solve._putBottomDaisyInDownCross(inputDict)
        self.assertDictEqual(expectedResult, actualResult) 
        
# 900 _putRightDaisyInDownCross
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
        actualResult = solve._putRightDaisyInDownCross(inputDict)
        self.assertDictEqual(expectedResult, actualResult) 
        
    def test900_020PlaceIsD10(self):    
        inputDict = {}
        inputDict['cube'] = 'yggyggbgwwroooyorwyooobrrogbbryrgrywywgwywbworrbbwbybg'
        expectedResult = {}
        expectedResult['rotations'] = 'UULLUU'
        expectedResult['cube'] = 'ygbrggggwwyrooyorwgooobyroybbrgryorwywywybbwrorbwwbgbg'
        actualResult = solve._putRightDaisyInDownCross(inputDict)
        self.assertDictEqual(expectedResult, actualResult) 
        
    def test900_030PlaceIsD12(self):    
        inputDict = {}
        inputDict['cube'] = 'bbrgryorwyggrgorogwroyoorywyoogbybgwgwowywywbbbgrwbrby'
        expectedResult = {}
        expectedResult['rotations'] = 'RR'
        expectedResult['cube'] = 'bbrgryorwgorogrggywroyoorywyoogbybgwgwgwybywybborwwrbb'
        actualResult = solve._putRightDaisyInDownCross(inputDict)
        self.assertDictEqual(expectedResult, actualResult) 
        
    def test900_040PlaceIsD21(self):    
        inputDict = {}
        inputDict['cube'] = 'wgbybgrbbwggoryorwwrorgorogyooyogryygwowywbrrbwybwbybg'
        expectedResult = {}
        expectedResult['rotations'] = 'uBBU'
        expectedResult['cube'] = 'wgrybgrbbgororyorwwroogrggwyooyogbyygwgwybbrybwybwbrwo'
        actualResult = solve._putRightDaisyInDownCross(inputDict)
        self.assertDictEqual(expectedResult, actualResult) 

# 1000 _putLeftDaisyInDownCross
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
        actualResult = solve._putLeftDaisyInDownCross(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test1000_020PlaceIsD10(self):    
        inputDict = {}
        inputDict['cube'] = 'wroyoyorwyoorbgroybbborgrygwggygorgwrwywywowgbbgrwbybb'
        expectedResult = {}
        expectedResult['rotations'] = 'LL'
        expectedResult['cube'] = 'grogoybrwyoorbgroybbooryrywwgrogyggwbwyrywywgrbgwwbobb'
        actualResult = solve._putLeftDaisyInDownCross(inputDict)
        self.assertDictEqual(expectedResult, actualResult) 
        
    def test1000_030PlaceIsD12(self):    
        inputDict = {}
        inputDict['cube'] = 'wroorgrygyooygorgwbbbyoyorwwggrbgroyrwywywowgbbybwrgbb'
        expectedResult = {}
        expectedResult['rotations'] = 'UURRUU'
        expectedResult['cube'] = 'grooryrywyooogyggwbbogoybrwwgrrbgroybwyrywywgbbobwwgbr'
        actualResult = solve._putLeftDaisyInDownCross(inputDict)
        self.assertDictEqual(expectedResult, actualResult)  
        
    def test1000_040PlaceIsD21(self):    
        inputDict = {}
        inputDict['cube'] = 'yoogoorygbbbgbrrgwwggyryorwwroogyroyowrwywgwybbybwrgbb'
        expectedResult = {}
        expectedResult['rotations'] = 'UBBu'
        expectedResult['cube'] = 'woogoorygbbbgborgywgryryorwwrorgygoygwrbywbwybbybwrowg'
        actualResult = solve._putLeftDaisyInDownCross(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
# 2000 _putTopDaisyInDownCross
#    inputs: 
#        parms:    dict; mandatory; arrives validated
#        parms['cube']:    string; len=54; [brgoyw]; 9 occurrences of each character, unique middle character; mandatory; arrives validated
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
        actualResult = solve._putTopDaisyInDownCross(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test2000_020PlaceIsD10(self):    
        inputDict = {}
        inputDict['cube'] = 'wrooryroyyoorgyrygbbbgoyrgwwggobgorwrwywywowggbbbwbbry'
        expectedResult = {}
        expectedResult['rotations'] = 'uLLU'
        expectedResult['cube'] = 'wroyryooyyorrgyrygwrogoorgwwgggbobbbbbgwywowgybbwwbrry'
        actualResult = solve._putTopDaisyInDownCross(inputDict)
        self.assertDictEqual(expectedResult, actualResult)  
        
    def test2000_030PlaceIsD12(self):    
        inputDict = {}
        inputDict['cube'] = 'yooyryrygbbbrggrgwwggoogorwwroyboroyowrwywgwybbybwrgbb'
        expectedResult = {}
        expectedResult['rotations'] = 'URRu'
        expectedResult['cube'] = 'yooyrorywbboggrggwwgryogbrwgroyboroyyrbwywgwybbobwwgbr'
        actualResult = solve._putTopDaisyInDownCross(inputDict)
        self.assertDictEqual(expectedResult, actualResult) 
        
    def test2000_040PlaceIsD21(self):    
        inputDict = {}
        inputDict['cube'] = 'yooyboroybbbyryrygwggrggrgwwrooogorwowrwywgwygbbbwbbry'
        expectedResult = {}
        expectedResult['rotations'] = 'BB'
        expectedResult['cube'] = 'yooyboroybboyrorywwgrggrggwgroyogbrwyrbwywgwygbbbwbrwo'
        actualResult = solve._putTopDaisyInDownCross(inputDict)
        self.assertDictEqual(expectedResult, actualResult)      
        
# 3000 _solveFrontLeftDownCorner
#    inputs: 
#        parms:    dict; mandatory; arrives validated
#        parms['cube']:    string; len=54; [brgoyw]; 9 occurrences of each character, unique middle character; mandatory; arrives validated
#    outputs:
#        side-effects:    non state changes; no external effects
#        returns:    dict
#        nominal: 
#            dict['rotations']: string, valid rotations to get proper rotations for D00 corner
#            dict['cube']: string, valid cube after rotation for D00 corner is performed
#        abnormal: 
#            no abnormal behavior since method is only called after cube is validated and down cross is solved
#    confidence level: boundary value analysis
#
#    happy path:
#        test010: down face is U00
#        test020: down face is U02
#        test030: down face is U20
#        test040: down face is U22
#        test050: down face is F00
#        test060: down face is F02
#        test070: down face is F20
#        test080: down face is F22
#        test090: down face is R00
#        test1000: down face is R02
#        test2000: down face is R20
#        test3000: down face is R22
#        test4000: down face is B00
#        test5000: down face is B02
#        test6000: down face is B20
#        test7000: down face is B22
#        test8000: down face is L00
#        test9000: down face is L02
#        test9010: down face is L20
#        test9020: down face is L22
#        test9030: down face is D02
#        test9040: down face is D20
#        test9050: down face is D22

    def test3000_010DownFaceIsU00(self):
        inputDict = {}
        inputDict['cube'] = 'grgbrryrryobggggggybroooooobyybbybbbwrogyyoyrrwwwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'uluuLUluL'
        expectedResult['cube'] = 'orgrrrrrryybggggggrygooooooooybbbbbbygyyybbyrwwwwwwwww'
        actualResult = solve._solveFrontLeftDownCorner(inputDict)
        self.assertDictEqual(expectedResult, actualResult) 
        
    def test3000_020DownFaceIsU02(self):
        inputDict = {}
        inputDict['cube'] = 'bbybrryrrgorggggggbyyoooooobrobbybbrrgwyyyyrogwwwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'UUluuLUluL'
        expectedResult['cube'] = 'oroyrrrrrbyrgggggggyboooooorbgbbobbbygyrybyyywwwwwwwww'
        actualResult = solve._solveFrontLeftDownCorner(inputDict)
        self.assertDictEqual(expectedResult, actualResult) 
    
    def test3000_030DownFaceIsU20(self):
        inputDict = {}
        inputDict['cube'] = 'oggybbybbyoorrrrrrbrgggggggoobooboobyyyyybwyrrwwwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'luuLUluL'
        expectedResult['cube'] = 'yooybbbbbbbbrrrrrrrgyggggggrrooooooogyyyyygbywwwwwwwww'
        actualResult = solve._solveFrontLeftDownCorner(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test3000_040DownFaceIsU22(self):
        inputDict = {}
        inputDict['cube'] = 'yobybbybbogyrrrrrrobgggggggyorooroogrybbyybywowwwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'UluuLUluL'
        expectedResult['cube'] = 'bbgybbbbbyrgrrrrrrogoggggggboyooooooyyybyyryrwwwwwwwww'
        actualResult = solve._solveFrontLeftDownCorner(inputDict)
        self.assertDictEqual(expectedResult, actualResult) 
        
    def test3000_050DownFaceIsF00(self):
        inputDict = {}
        inputDict['cube'] = 'wbbybbbbbrrgrrrrrroogggggggyoooogooyryybyybyyowwwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'ulUL'
        expectedResult['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        actualResult = solve._solveFrontLeftDownCorner(inputDict)
        self.assertDictEqual(expectedResult, actualResult) 
    
    def test3000_060DownFaceIsF02(self):
        inputDict = {}
        inputDict['cube'] = 'oowybbybbbrrrrrrrrggyggggggoogooboobbyybyyyyorwwwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'UluL'
        expectedResult['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        actualResult = solve._solveFrontLeftDownCorner(inputDict)
        self.assertDictEqual(expectedResult, actualResult) 
    
    def test3000_070DownFaceIsF20(self):
        inputDict = {}
        inputDict['cube'] = 'obbybbwbbroyrrrrrrrrgggggggooyoogoobyygyybbyyowwwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'lULulUL'
        expectedResult['cube'] = 'yoyybbbbbrryrrrrrrgbbggggggygroooooooyoyyybbgwwwwwwwww'
        actualResult = solve._solveFrontLeftDownCorner(inputDict)
        self.assertDictEqual(expectedResult, actualResult) 
        
    def test3000_080DownFaceIsF22(self):
        inputDict = {}
        inputDict['cube'] = 'gyyygbbgwgbyyoorooorgbbybbbwgrgrorrrogboyryroywgwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'RUrluuLUluL'
        expectedResult['cube'] = 'ybyrggggyoorroooooyygbbybbbwgggryrrrobboyyrrbwwgwwwwww'
        actualResult = solve._solveFrontLeftDownCorner(inputDict)
        self.assertDictEqual(expectedResult, actualResult) 
        
    def test3000_090DownFaceIsR00(self):
        inputDict = {}
        inputDict['cube'] = 'yooybbbbbwbbrrrrrrrrgggggggoogoogooyyyyyyyrbbowwwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'lUL'
        expectedResult['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        actualResult = solve._solveFrontLeftDownCorner(inputDict)
        self.assertDictEqual(expectedResult, actualResult) 
    
    def test3000_1000DownFaceIsR02(self):
        inputDict = {}
        inputDict['cube'] = 'oogybbybboowrrrrrrbrrggggggggyooboobyyoyyybbyrwwwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'uuluL'
        expectedResult['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        actualResult = solve._solveFrontLeftDownCorner(inputDict)
        self.assertDictEqual(expectedResult, actualResult) 
    
    def test3000_2000DownFaceIsR20(self):
        inputDict = {}
        inputDict['cube'] = 'ryrrggoggyygroowoowogbbybbbogygrbrrbyyooybgrbywrwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'RUrulUL'
        expectedResult['cube'] = 'oryrgyggrgygooobooybgbbybbbwgygryrrrorroybbgowwywwwwww'
        actualResult = solve._solveFrontLeftDownCorner(inputDict)
        self.assertDictEqual(expectedResult, actualResult) 
        
    def test3000_3000DownFaceIsR22(self):
        inputDict = {}
        inputDict['cube'] = 'oyrooyroogyoobrbbwbryyrrgrrboggggggbrbybybygywwwwwwwwo'
        expectedResult = {}
        expectedResult['rotations'] = 'ruRuluL'
        expectedResult['cube'] = 'ygbboyooowryobybbyboogrrbrryrgggyggggbryybrorwwwwwwwwo'
        actualResult = solve._solveFrontLeftDownCorner(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test3000_4000DownFaceIsB00(self):
        inputDict = {}
        inputDict['cube'] = 'oogybbbbbyoorrrrrrwbbggggggrrgoogooyyybyybyyrowwwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'UlUL'
        expectedResult['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        actualResult = solve._solveFrontLeftDownCorner(inputDict)
        self.assertDictEqual(expectedResult, actualResult) 
        
    def test3000_5000DownFaceIsB02(self):
        inputDict = {}
        inputDict['cube'] = 'ggyybbybboogrrrrrroowggggggbrroobooboyyyybyybrwwwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'uluL'
        expectedResult['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        actualResult = solve._solveFrontLeftDownCorner(inputDict)
        self.assertDictEqual(expectedResult, actualResult) 
        
    def test3000_6000DownFaceIsB20(self):
        inputDict = {}
        inputDict['cube'] = 'ryoyggrggyryooooogoooybbwbbwybrrgrrgbbbbygyrgywwwwwwwr'
        expectedResult = {}
        expectedResult['rotations'] = 'rURUlUL'
        expectedResult['cube'] = 'rybggggggrygooooooogbbbbbbbyoyrrrrrroyyyyrgbywwwwwwwww'
        actualResult = solve._solveFrontLeftDownCorner(inputDict)
        self.assertDictEqual(expectedResult, actualResult) 
    
    def test3000_7000DownFaceIsB22(self):
        inputDict = {}
        inputDict['cube'] = 'gyyyboybboorbrbrrryrrrgbggwgroyoooogygbyygwgbowwwwwbww'
        expectedResult = {}
        expectedResult['rotations'] = 'LululuL'
        expectedResult['cube'] = 'roggbobbborobrbrrrgyyrggggbooyroyyoobbwgyygyywwwwwwrww'
        actualResult = solve._solveFrontLeftDownCorner(inputDict)
        self.assertDictEqual(expectedResult, actualResult) 
    
    def test3000_8000DownFaceIsL00(self):
        inputDict = {}
        inputDict['cube'] = 'rrgybbbbboogrrrrrryooggggggwbboogooybbryyyyyyowwwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'uulUL'
        expectedResult['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        actualResult = solve._solveFrontLeftDownCorner(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
    
    def test3000_9000DownFaceIsL02(self):
        inputDict = {}
        inputDict['cube'] = 'brrybbybbggyrrrrrroogggggggoowooboobybbyyyoyyrwwwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'luL'
        expectedResult['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        actualResult = solve._solveFrontLeftDownCorner(inputDict)
        self.assertDictEqual(expectedResult, actualResult) 
        
    def test3000_9010DownFaceIsL20(self):
        inputDict = {}
        inputDict['cube'] = 'wyryoobooggrgbobbbyrobryrroybrggowgygybryrgbyowwwwwgww'
        expectedResult = {}
        expectedResult['rotations'] = 'LUllUUL'
        expectedResult['cube'] = 'bggyoooooroygbobbbogybrbrrorbyygrggggrbryyrywwwwwwwyww'
        actualResult = solve._solveFrontLeftDownCorner(inputDict)
        self.assertDictEqual(expectedResult, actualResult) 
        
    def test3000_9020DownFaceIsL22(self):
        inputDict = {}
        inputDict['cube'] = 'oboygrrggboyyooooobgrgbobbbgbgbrgrrwyrrryyyyygwwwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'luLUluL'
        expectedResult['cube'] = 'ygyrgrggggboyooooobobgbobbbrggbrbrrryyyyyyrrowwwwwwwww'
        actualResult = solve._solveFrontLeftDownCorner(inputDict)
        self.assertDictEqual(expectedResult, actualResult) 
    
    def test3000_9030DownFaceIsD02(self):
        inputDict = {}
        inputDict['cube'] = 'rryybybbogbbrrrbrrrogggggggyowoogooyryybyybboowwwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'RUrluL'
        expectedResult['cube'] = 'ygybbybbyorrorrorrgbwggggggrrroooooobyybyybybwwgwwwwww'
        actualResult = solve._solveFrontLeftDownCorner(inputDict)
        self.assertDictEqual(expectedResult, actualResult) 
        
    def test3000_9040DownFaceIsD20(self):
        inputDict = {}
        inputDict['cube'] = 'wrrybbybbgggrrrrrroooggoggobggbobbobyyyoyyoyyrwwwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'LulUlUUL'
        expectedResult['cube'] = 'ygoybbbbbbbbrrrrrrrrgggyggywbgoogooooyyoyyroywwwwwwgww'
        actualResult = solve._solveFrontLeftDownCorner(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test3000_9050DownFaceIsD22(self):
        inputDict = {}
        inputDict['cube'] = 'bgybryyrrrgwrgyggborgooorooooogbybbbybgbyryygrwwwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'rUURulUL'
        expectedResult['cube'] = 'yryoryrrrrgorgoggogyobooyooygrgbybbbgbwyyrbbgwwwwwwwwb'
        actualResult = solve._solveFrontLeftDownCorner(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
# 4000 _solveFrontRightDownCorner
#    inputs: 
#        parms:    dict; mandatory; arrives validated
#        parms['cube']:    string; len=54; [brgoyw]; 9 occurrences of each character, unique middle character; mandatory; arrives validated
#    outputs:
#        side-effects:    non state changes; no external effects
#        returns:    dict
#        nominal: 
#            dict['rotations']: string, valid rotations to get proper rotations for D02 corner
#            dict['cube']: string, valid cube after rotation for D02 corner is performed
#        abnormal: 
#            no abnormal behavior since method is only called after cube is validated and down cross is solved
#    confidence level: boundary value analysis
#
#    happy path:
#        test010: down face is U00
#        test020: down face is U02
#        test030: down face is U20
#        test040: down face is U22
#        test050: down face is F00
#        test060: down face is F02
#        test070: down face is F22
#        test080: down face is R00
#        test090: down face is R02
#        test1000: down face is R20
#        test2000: down face is R22
#        test3000: down face is B00
#        test4000: down face is B02
#        test5000: down face is B20
#        test6000: down face is B22
#        test7000: down face is L00
#        test8000: down face is L02
#        test9000: down face is L20
#        test9010: down face is D20
#        test9020: down face is D22

    def test4000_010DownFaceIsU00(self):
        inputDict = {}
        inputDict['cube'] = 'gobbbybbyrrybrrbrrggrggggggbrroooooowyoyybyyywwowwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'RUrURur'
        expectedResult['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        actualResult = solve._solveFrontRightDownCorner(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test4000_020DownFaceIsU02(self):
        inputDict = {}
        inputDict['cube'] = 'rrybbybbyggrbrrbrrbrrgggggggobooooooyywyyyybowwowwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'uRUrURur'
        expectedResult['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        actualResult = solve._solveFrontRightDownCorner(inputDict)
        self.assertDictEqual(expectedResult, actualResult)

    def test4000_030DownFaceIsU20(self):
        inputDict = {}
        inputDict['cube'] = 'brybbybbyoryorrgrrgbrggggggygroooooobyoyybwybwwrwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'uRUUruRUr'
        expectedResult['cube'] = 'gbbbbybbbyrbrrrrrrrgrgggggggoyooooooyyyyyboyowwwwwwwww'
        actualResult = solve._solveFrontRightDownCorner(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test4000_040DownFaceIsU22(self):
        inputDict = {}
        inputDict['cube'] = 'ygrbbybbybryorrgrrorygggggggbrooooooobbyyybywwwrwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'RUUruRUr'
        expectedResult['cube'] = 'gbbbbybbbyrbrrrrrrrgrgggggggoyooooooyyyyyboyowwwwwwwww'
        actualResult = solve._solveFrontRightDownCorner(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test4000_050DownFaceIsF00(self):
        inputDict = {}
        inputDict['cube'] = 'wrrbbybbygrrbrrbrryggggggggoobooooooyybyybryywwowwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'uRUr'
        expectedResult['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        actualResult = solve._solveFrontRightDownCorner(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test4000_060DownFaceIsF02(self):
        inputDict = {}
        inputDict['cube'] = 'bbwbbybbbrrygrryrrgrrgggggggooooooooyyoyybyybwwrwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'URur'
        expectedResult['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        actualResult = solve._solveFrontRightDownCorner(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
    
    def test4000_070DownFaceIsF22(self):
        inputDict = {}
        inputDict['cube'] = 'ygybbybbwrryrrrbrrgooggggggbbrooooooyyoyybbygwwrwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'RurURur'
        expectedResult['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        actualResult = solve._solveFrontRightDownCorner(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
    
    def test4000_080DownFaceIsR00(self):
        inputDict = {}
        inputDict['cube'] = 'oobbbybbywrrbrrbrrgrrggggggyggoooooobbyyyyyyrwwowwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'RUr'
        expectedResult['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        actualResult = solve._solveFrontRightDownCorner(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test4000_090DownFaceIsR02(self):
        inputDict = {}
        inputDict['cube'] = 'goobbybbbbbwgrryrrrrygggggggrrooooooobbyyyyyywwrwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'UURur'
        expectedResult['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        actualResult = solve._solveFrontRightDownCorner(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test4000_1000DownFaceIsR20(self):
        inputDict = {}
        inputDict['cube'] = 'ooybbybbrorrrrrwrrybgggggggyggoooooorybyybyybwwbwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'RUruRUr'
        expectedResult['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        actualResult = solve._solveFrontRightDownCorner(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test4000_2000DownFaceIsR22(self):
        inputDict = {}
        inputDict['cube'] = 'rowroooogrbogbyybwbbgoryorrygbrgggggryyyyrybbwwowwwwwb'
        expectedResult = {}
        expectedResult['rotations'] = 'ruRRUUr'
        expectedResult['cube'] = 'byrroyooogbrbbobbyygobrybrrygrrggggggyboyrwoywwwwwwwwo'
        actualResult = solve._solveFrontRightDownCorner(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
    
    def test4000_3000DownFaceIsB00(self):
        inputDict = {}
        inputDict['cube'] = 'yggbbybbyoobbrrbrrwrrgggggggrrooooooyyrbyybyywwowwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'URUr'
        expectedResult['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        actualResult = solve._solveFrontRightDownCorner(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test4000_4000DownFaceIsB02(self):
        inputDict = {}
        inputDict['cube'] = 'ygybbybbyorrorrorrgbwggggggrrroooooobyybyybybwwgwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'RUUr'
        expectedResult['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        actualResult = solve._solveFrontRightDownCorner(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
    
    def test4000_5000DownFaceIsB20(self):
        inputDict = {}
        inputDict['cube'] = 'rbbroboobyooyboybbygbyrywrrwgyrgggggrogyybgrowwrwwwwwo'
        expectedResult = {}
        expectedResult['rotations'] = 'rURURUr'
        expectedResult['cube'] = 'yyyroroooggybbgbbbroboryrrryorrgggggoygbyybbowwwwwwwww'
        actualResult = solve._solveFrontRightDownCorner(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
    
    def test4000_6000DownFaceIsB22(self):
        inputDict = {}
        inputDict['cube'] = 'gorrgyggrgoygorbooorbbbybbwwyyorygrrrgbbybogywwywwwoww'
        expectedResult = {}
        expectedResult['rotations'] = 'LuluRur'
        expectedResult['cube'] = 'gorrgbgggyowyorooorggbbgbbboorrryorryybgyyybbwwwwwwyww'
        actualResult = solve._solveFrontRightDownCorner(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
    
    def test4000_7000DownFaceIsL00(self):
        inputDict = {}
        inputDict['cube'] = 'grrbbybbyyggbrrbrroobggggggwrrooooooryyyyyybbwwowwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'uuRUr'
        expectedResult['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        actualResult = solve._solveFrontRightDownCorner(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test4000_8000DownFaceIsL02(self):
        inputDict = {}
        inputDict['cube'] = 'rrybbybbbgrrgrryrrgooggggggbbwooooooyyyyyybbowwrwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'Rur'
        expectedResult['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        actualResult = solve._solveFrontRightDownCorner(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
    
    def test4000_9000DownFaceIsL20(self):
        inputDict = {}
        inputDict['cube'] = 'wyrogyggyyyggoroooygobbybbobobbrgwrryrrbyrrobwwgwwwgww'
        expectedResult = {}
        expectedResult['rotations'] = 'LUUlRUr'
        expectedResult['cube'] = 'ogyogogggrbbyoroooyobbbrbbbwggyrgyrrrboryyyygwwwwwwrww'
        actualResult = solve._solveFrontRightDownCorner(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
    
    def test4000_9010DownFaceIsD20(self):
        inputDict = {}
        inputDict['cube'] = 'yggyoyooyogwrbobbbgoybrrrrorbrbgobggggryyybrywwowwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'LuulURur'
        expectedResult['cube'] = 'yoyyoroooogrbbobbbwrgbryrryybrggooggrygyyrbgbwwwwwwgww'
        actualResult = solve._solveFrontRightDownCorner(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test4000_9020DownFaceIsD22(self):
        inputDict = {}
        inputDict['cube'] = 'brrbryrrgyoybgyygrroggorgoowrobbobbboyggygyybwwowwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'rURUURur'
        expectedResult['cube'] = 'yogbrgrrrorgrgogggybbyoroooyyrbbobbboyrgyybgywwwwwwwww'
        actualResult = solve._solveFrontRightDownCorner(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
# 5000 _solveBackLeftDownCorner
#    inputs: 
#        parms:    dict; mandatory; arrives validated
#        parms['cube']:    string; len=54; [brgoyw]; 9 occurrences of each character, unique middle character; mandatory; arrives validated
#    outputs:
#        side-effects:    non state changes; no external effects
#        returns:    dict
#        nominal: 
#            dict['rotations']: string, valid rotations to get proper rotations for D20 corner
#            dict['cube']: string, valid cube after rotation for D20 corner is performed
#        abnormal: 
#            no abnormal behavior since method is only called after cube is validated and down cross is solved
#    confidence level: boundary value analysis
#
#    happy path:
#        test010: down face is U00
#        test020: down face is U02
#        test030: down face is U20
#        test040: down face is U22
#        test050: down face is F00
#        test060: down face is F02
#        test070: down face is R00
#        test080: down face is R02
#        test090: down face is R22
#        test1000: down face is B00
#        test2000: down face is B02
#        test3000: down face is B20
#        test4000: down face is B22
#        test5000: down face is L00
#        test6000: down face is L02
#        test7000: down face is L20
#        test8000: down face is D22
    
    def test5000_010DownFaceIsU00(self):
        inputDict = {}
        inputDict['cube'] = 'gbrbbobbbyoybrgrrroyorgyggygyyoorgoowgbrygoybwwwwwwrww'
        expectedResult = {}
        expectedResult['rotations'] = 'LulUULUl'
        expectedResult['cube'] = 'yyybbobbbgoybrgrrroygrgggggybroorooorgbyyybrowwwwwwwww'
        actualResult = solve._solveBackLeftDownCorner(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test5000_020DownFaceIsU02(self):
        inputDict = {}
        inputDict['cube'] = 'oyybbobbbbyobrgrrrgoyrgyggorbyoorgooggwyyrbgrwwwwwwyww'
        expectedResult = {}
        expectedResult['rotations'] = 'uLulUULUl'
        expectedResult['cube'] = 'ooybbobbbroybrgrrrbygrgggggobyyoroooyrryyybggwwwwwwwww'
        actualResult = solve._solveBackLeftDownCorner(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
    
    def test5000_030DownFaceIsU20(self):
        inputDict = {}
        inputDict['cube'] = 'gyobbobbbboybrgrrrgbrrgyggygyooorrooyyogygwrywwwwwwbww'
        expectedResult = {}
        expectedResult['rotations'] = 'uLUlULul'
        expectedResult['cube'] = 'bygbbobbbyobbrgrrrroyrgyggggyoborooooyyrygygrwwwwwwwww'
        actualResult = solve._solveBackLeftDownCorner(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test5000_040DownFaceIsU22(self):
        inputDict = {}
        inputDict['cube'] = 'gyobbobbbgyobrgrrrboyrgyggygbroorrooogyyyrygwwwwwwwbww'
        expectedResult = {}
        expectedResult['rotations'] = 'LUlULul'
        expectedResult['cube'] = 'bygbbobbbyobbrgrrrroyrgyggggyoborooooyyrygygrwwwwwwwww'
        actualResult = solve._solveBackLeftDownCorner(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test5000_050DownFaceIsF00(self):
        inputDict = {}
        inputDict['cube'] = 'woobbbbbbboorrrrrrybbggyggyrrggoogooyygyygoyywwwwwwrww'
        expectedResult = {}
        expectedResult['rotations'] = 'ULUl'
        expectedResult['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        actualResult = solve._solveBackLeftDownCorner(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test5000_060DownFaceIsF02(self):
        inputDict = {}
        inputDict['cube'] = 'bgwbbbbbbooorrrrrrybyggyggyroorooroogygyygyygwwwwwwbww'
        expectedResult = {}
        expectedResult['rotations'] = 'uLul'
        expectedResult['cube'] = 'rrybbbbbbgoorrrrrrbgyggggggbbyooooooryyyyygyowwwwwwwww'
        actualResult = solve._solveBackLeftDownCorner(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test5000_070DownFaceIsR00(self):
        inputDict = {}
        inputDict['cube'] = 'rrgbbbbbbwoorrrrrrbooggyggyybbgoogooggyyyyyyowwwwwwrww'
        expectedResult = {}
        expectedResult['rotations'] = 'UULUl'
        expectedResult['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        actualResult = solve._solveBackLeftDownCorner(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test5000_080DownFaceIsR02(self):
        inputDict = {}
        inputDict['cube'] = 'brrbbbbbbggwrrrrrrooyggygggboobooyoorggyyyyyywwwwwwoww'
        expectedResult = {}
        expectedResult['rotations'] = 'Lul'
        expectedResult['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        actualResult = solve._solveBackLeftDownCorner(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test5000_090DownFaceIsR22(self):
        inputDict = {}
        inputDict['cube'] = 'brbbbbbbbrrwrrgrrwgogygygggyoobooyoorgryyyygywwwwwwowo'
        expectedResult = {}
        expectedResult['rotations'] = 'rLuRl'
        expectedResult['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        actualResult = solve._solveBackLeftDownCorner(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test5000_1000DownFaceIsB00(self):
        inputDict = {}
        inputDict['cube'] = 'ybbbbbbbbrrgrrrrrrwooggyggyboogoogooyyogyygyywwwwwwrww'
        expectedResult = {}
        expectedResult['rotations'] = 'uLUl'
        expectedResult['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        actualResult = solve._solveBackLeftDownCorner(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test5000_2000DownFaceIsB02(self):
        inputDict = {}
        inputDict['cube'] = 'boobbbbbbbrrrrrrrrggwggygggooybooyoogyygyyryywwwwwwoww'
        expectedResult = {}
        expectedResult['rotations'] = 'ULul'
        expectedResult['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        actualResult = solve._solveBackLeftDownCorner(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test5000_3000DownFaceIsB20(self):
        inputDict = {}
        inputDict['cube'] = 'bobbbbbbbrryrrbrrogrrygywgywoogoogooggoyyyygywwwwwwrwg'
        expectedResult = {}
        expectedResult['rotations'] = 'rURuLUl'
        expectedResult['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        actualResult = solve._solveBackLeftDownCorner(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test5000_4000DownFaceIsB22(self):
        inputDict = {}
        inputDict['cube'] = 'brrbbbbbbggorrrrrrybyggyggwooyooogoobyggyyryywwwwwwoww'
        expectedResult = {}
        expectedResult['rotations'] = 'LulULul'
        expectedResult['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        actualResult = solve._solveBackLeftDownCorner(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test5000_5000DownFaceIsL00(self):
        inputDict = {}
        inputDict['cube'] = 'boobbbbbbybbrrrrrrrrgggyggywoogoogoooyyyyyyggwwwwwwrww'
        expectedResult = {}
        expectedResult['rotations'] = 'LUl'
        expectedResult['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        actualResult = solve._solveBackLeftDownCorner(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test5000_6000DownFaceIsL02(self):
        inputDict = {}
        inputDict['cube'] = 'ooybbbbbbboorrrrrrbrrggygggggwbooyooyyyyyyggrwwwwwwoww'
        expectedResult = {}
        expectedResult['rotations'] = 'UULul'
        expectedResult['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        actualResult = solve._solveBackLeftDownCorner(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test5000_7000DownFaceIsL20(self):
        inputDict = {}
        inputDict['cube'] = 'ygbbbbbbbybbrrrrrrrryggyggorooooowoogyygyygyowwwwwwgww'
        expectedResult = {}
        expectedResult['rotations'] = 'LUluLUl'
        expectedResult['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        actualResult = solve._solveBackLeftDownCorner(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test5000_8000DownFaceIsD22(self):
        inputDict = {}
        inputDict['cube'] = 'brobbbbbbybwrrrrrggooygyogyboygoogooyyrgyyrggwwwwwwrww'
        expectedResult = {}
        expectedResult['rotations'] = 'ruRLUl'
        expectedResult['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        actualResult = solve._solveBackLeftDownCorner(inputDict)
        self.assertDictEqual(expectedResult, actualResult)

# 6000 _solveBackRightDownCorner
#    inputs: 
#        parms:    dict; mandatory; arrives validated
#        parms['cube']:    string; len=54; [brgoyw]; 9 occurrences of each character, unique middle character; mandatory; arrives validated
#    outputs:
#        side-effects:    non state changes; no external effects
#        returns:    dict
#        nominal: 
#            dict['rotations']: string, valid rotations to get proper rotations for D22 corner
#            dict['cube']: string, valid cube after rotation for D22 corner is performed
#        abnormal: 
#            no abnormal behavior since method is only called after cube is validated and down cross is solved
#    confidence level: boundary value analysis
#
#    happy path:
#        test010: down face is U00
#        test020: down face is U02
#        test030: down face is U20
#        test040: down face is U22
#        test050: down face is F00
#        test060: down face is F02
#        test070: down face is R00
#        test080: down face is R02
#        test090: down face is R22
#        test1000: down face is B00
#        test2000: down face is B02
#        test3000: down face is B20
#        test4000: down face is L00
#        test5000: down face is L02

    def test6000_010DownFaceIsU00(self):
        inputDict = {}
        inputDict['cube'] = 'oyyoooooogyybbrbbrrgrbrrbrrbyyggggggwygoyrbbowwwwwwwwy'
        expectedResult = {}
        expectedResult['rotations'] = 'UrURUUruR'
        expectedResult['cube'] = 'rgyoooooogybbbybbbryybrrrrroryggggggboybyrgyowwwwwwwww'
        actualResult = solve._solveBackRightDownCorner(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test6000_020DownFaceIsU02(self):
        inputDict = {}
        inputDict['cube'] = 'orybbbbbbrrgrrorrorbyyggyggbggoooooorywyygyygwwwwwwwwb'
        expectedResult = {}
        expectedResult['rotations'] = 'ruuRUruR'
        expectedResult['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        actualResult = solve._solveBackRightDownCorner(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test6000_030DownFaceIsU20(self):
        inputDict = {}
        inputDict['cube'] = 'rbybbbbbbbggrrorrooryyggyggrrgoooooogyygyywyrwwwwwwwwb'
        expectedResult = {}
        expectedResult['rotations'] = 'UUruuRUruR'
        expectedResult['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        actualResult = solve._solveBackRightDownCorner(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test6000_040DownFaceIsU22(self):
        inputDict = {}
        inputDict['cube'] = 'rrgbbbbbbrbyrrorrobggyggyggoryooooooyyryyyggwwwwwwwwwb'
        expectedResult = {}
        expectedResult['rotations'] = 'uruuRUruR'
        expectedResult['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        actualResult = solve._solveBackRightDownCorner(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test6000_050DownFaceIsF00(self):
        inputDict = {}
        inputDict['cube'] = 'wgbbbbbbbrrorrorroybyyggyggrrroooooogyggyygyywwwwwwwwb'
        expectedResult = {}
        expectedResult['rotations'] = 'ruuR'
        expectedResult['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        actualResult = solve._solveBackRightDownCorner(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test6000_060DownFaceIsF02(self):
        inputDict = {}
        inputDict['cube'] = 'rrwbbbbbbgoorrgrrgbbyyggyggrrboooooogyygyyyyrwwwwwwwwo'
        expectedResult = {}
        expectedResult['rotations'] = 'uruR'
        expectedResult['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        actualResult = solve._solveBackRightDownCorner(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
    
    def test6000_070DownFaceIsR00(self):
        inputDict = {}
        inputDict['cube'] = 'rrrbbbbbbwgbrrorrorroyggyggybyoooooogyyyyygggwwwwwwwwb'
        expectedResult = {}
        expectedResult['rotations'] = 'UruuR'
        expectedResult['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        actualResult = solve._solveBackRightDownCorner(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test6000_080DownFaceIsR02(self):
        inputDict = {}
        inputDict['cube'] = 'rrbbbbbbbrrwrrgrrggooyggyggbbyooooooyyryyyggywwwwwwwwo'
        expectedResult = {}
        expectedResult['rotations'] = 'ruR'
        expectedResult['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        actualResult = solve._solveBackRightDownCorner(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test6000_090DownFaceIsR22(self):
        inputDict = {}
        inputDict['cube'] = 'bgybbbbbbrrorrrrrwyooyggrggbbyooooooyygyygrygwwwwwwwwg'
        expectedResult = {}
        expectedResult['rotations'] = 'ruRUruR'
        expectedResult['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        actualResult = solve._solveBackRightDownCorner(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
    
    def test6000_1000DownFaceIsB00(self):
        inputDict = {}
        inputDict['cube'] = 'rrbbbbbbbyrrrrbrrywggygggggoobooooooyygyygyyowwwwwwwwr'
        expectedResult = {}
        expectedResult['rotations'] = 'urUR'
        expectedResult['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        actualResult = solve._solveBackRightDownCorner(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test6000_2000DownFaceIsB02(self):
        inputDict = {}
        inputDict['cube'] = 'bbybbbbbbrrbrrgrrgrrwyggygggooooooooryyyygyygwwwwwwwwo'
        expectedResult = {}
        expectedResult['rotations'] = 'UruR'
        expectedResult['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        actualResult = solve._solveBackRightDownCorner(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test6000_3000DownFaceIsB20(self):
        inputDict = {}
        inputDict['cube'] = 'byyggggggoorooboobgogybbwbboyyrrrrrryyygybrrbwwwwwwwwo'
        expectedResult = {}
        expectedResult['rotations'] = 'rURurUR'
        expectedResult['cube'] = 'yoyggggggrboooooooyyybbbbbbbybrrrrrrrggryyoygwwwwwwwww'
        actualResult = solve._solveBackRightDownCorner(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test6000_4000DownFaceIsL00(self):
        inputDict = {}
        inputDict['cube'] = 'oobbbbbbbrrbrrbrryyrrygggggwggooooooggoyyyyyywwwwwwwwr'
        expectedResult = {}
        expectedResult['rotations'] = 'rUR'
        expectedResult['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        actualResult = solve._solveBackRightDownCorner(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test6000_5000DownFaceIsL02(self):
        inputDict = {}
        inputDict['cube'] = 'goobbbbbbbbyrrgrrgrrbyggyggrrwooooooyggyyyryywwwwwwwwo'
        expectedResult = {}
        expectedResult['rotations'] = 'uuruR'
        expectedResult['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        actualResult = solve._solveBackRightDownCorner(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
# 7000 _findDownCorner
#    inputs: 
#        parms:    dict; mandatory; arrives validated
#        parms['cube']:    string; len=54; [brgoyw]; 9 occurrences of each character, unique middle character; mandatory; arrives validated
#        parms['colors']:    set; len=3; [brgoyw]; unique colors; mandatory; arrives validated
#    outputs:
#        side-effects:    non state changes; no external effects
#        returns:    int
#        nominal: 
#            location: int, location of the down colored piece that goes in D00
#        abnormal: 
#            no abnormal behavior since method is only called after cube is validated
#    confidence level: boundary value analysis  
#
#    happy path: 
#        test010: nominal cube and nominal corner colors

    def test7000_010NominalCubeAndNominalCornerColors(self):
        inputDict = {}
        inputDict['cube'] = 'grgggobggyyybooooobgggbobbbrbyyrrrrywyrryboyrowwwwwwww'
        inputDict['colors'] = {'w', 'r', 'g'}
        expectedResult = 36
        actualResult = solve._findDownCorner(inputDict)
        self.assertEqual(expectedResult, actualResult) 
        
# 8000 _rotatePiece
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

    def test8000_010NominalCubeAndRotation(self):
        rotation = 'f'
        cube = 'yywyrooyyrogwgwgworworoybbwbgrbbggryygwrygbobgrrbwboow'
        expectedResult = 'woyyryyyorogrgwgworworoybbwbgbbbogrbygwrygrwgrgybwboow'
        actualResult = solve._rotatePiece(rotation, cube)
        self.assertEqual(expectedResult, actualResult)

# 9000 _findMiddleLayerPiece
#    inputs: 
#        parms:    dict; mandatory; arrives validated
#        parms['cube']:    string; len=54; [brgoyw]; 9 occurrences of each character, unique middle character; mandatory; arrives validated
#        parms['colors']:    set; len=2; [brgoyw]; unique colors; mandatory; arrives validated
#    outputs:
#        side-effects:    non state changes; no external effects
#        returns:    int
#        nominal: 
#            location: int, location of the front or back color of the piece that corresponds with the input colors
#        abnormal: 
#            no abnormal behavior since method is only called after cube is validated
#    confidence level: boundary value analysis  
#
#    happy path: 
#        test010: nominal cube and nominal middle piece colors
    def test9000_010NominalCubeAndNominalMiddlePieceColors(self):
        inputDict = {}
        inputDict['cube'] = 'rgobryrrrygyrgggggbybroooooyoybbrbbbobryyogygwwwwwwwww'
        inputDict['colors'] = {'r', 'b'}
        expectedResult = 32
        actualResult = solve._findMiddleLayerPiece(inputDict)
        self.assertEqual(expectedResult, actualResult) 

# 1010 _solveFrontLeftMiddlePiece
#    inputs: 
#        parms:    dict; mandatory; arrives validated
#        parms['cube']:    string; len=54; [brgoyw]; 9 occurrences of each character, unique middle character; mandatory; arrives validated
#    outputs:
#        side-effects:    non state changes; no external effects
#        returns:    dict
#        nominal: 
#            dict['rotations']: string, valid rotations to get proper rotations for front left middle piece
#            dict['cube']: string, valid cube after rotation for front left middle piece is performed
#        abnormal: 
#            no abnormal behavior since method is only called after cube is validated and down layer is solved
#    confidence level: boundary value analysis
#
#    happy path:
#        test010: front color piece is F01
#        test020: front color piece is F12
#        test030: front color piece is R01
#        test040: front color piece is R10
#        test050: front color piece is R12
#        test060: front color piece is B01
#        test070: front color piece is B10
#        test080: front color piece is B12
#        test090: front color piece is L01
#        test1000: front color piece is L10
#        test2000: front color piece is L12
#        test3000: front color piece is U01
#        test4000: front color piece is U10
#        test5000: front color piece is U12
#        test6000: front color piece is U21

    def test1010_010FrontColorPieceIsF01(self):
        inputDict = {}
        inputDict['cube'] = 'yryyrrrrrbybggggggyyyooooooryobbgbbbgbooyrgbrwwwwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'ulULUFuf'
        expectedResult['cube'] = 'yygrrrrrryobggggggrgbooooooyyobbbbbboyybyygrrwwwwwwwww'
        actualResult = solve._solveFrontLeftMiddlePiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
    
    def test1010_020FrontColorPieceIsF12(self):
        inputDict = {}
        inputDict['cube'] = 'oybyrrrrrrygbgggggyggooooooooybbgbbbyrryyrbbywwwwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'RurufUFFufulUL'
        expectedResult['cube'] = 'ggyrrorrroyryggggggyyoooooobyybbbbbbrbyrygorbwwwwwwwww'
        actualResult = solve._solveFrontLeftMiddlePiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test1010_030FrontColorPieceIsR01(self):
        inputDict = {}
        inputDict['cube'] = 'gyrrrrrrryroggggggbyroooooogoybbybbbybyyybogbwwwwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'lULUFuf'
        expectedResult['cube'] = 'yyorrrrrrygbggggggyyroooooogorbbbbbbyroyyybbgwwwwwwwww'
        actualResult = solve._solveFrontLeftMiddlePiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test1010_040FrontColorPieceIsR10(self):
        inputDict = {}
        inputDict['cube'] = 'ggbyrbrrryobrgggggrbyoooooogyrbbgbbboyyryyyrowwwwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'RurufUFUlULUFuf'
        expectedResult['cube'] = 'rryrryrrrryyrgggggggyooooooobbbbbbbbbyoyyoyggwwwwwwwww'
        actualResult = solve._solveFrontLeftMiddlePiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
    
    def test1010_050FrontColorPieceIsR12(self):
        inputDict = {}
        inputDict['cube'] = 'ogryrrrrrygyggrggggygboooooyoybbbbbbrroyyybobwwwwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'BuburURUFufulUL'
        expectedResult['cube'] = 'yorrrrrrryyrggggggggoooooooyybbbbbbbgyyryboybwwwwwwwww'
        actualResult = solve._solveFrontLeftMiddlePiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test1010_060FrontColorPieceIsB01(self):
        inputDict = {}
        inputDict['cube'] = 'oybyrrrrrrybggggggyryyooooorogbbobbbgbogybyrywwwwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'UlULUFuf'
        expectedResult['cube'] = 'yoyrrrrrrbbrgggggggogyooooooybbbbbbbyyyryyogrwwwwwwwww'
        actualResult = solve._solveFrontLeftMiddlePiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test1010_070FrontColorPieceIsB10(self):
        inputDict = {}
        inputDict['cube'] = 'gyrgrrrrryybggbgggyooroooooyorbbybbbgyogyrybbwwwwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'BuburURuulULUFuf'
        expectedResult['cube'] = 'yrbrrrrrrryrggyggggyyboooooooobbbbbbbgygyogyywwwwwwwww'
        actualResult = solve._solveFrontLeftMiddlePiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test1010_080FrontColorPieceIsB12(self):
        inputDict = {}
        inputDict['cube'] = 'boogrrrrrbyygggggggyyoorooorrybbybbbgboyyorbywwwwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'LulubUBUUFufulUL'
        expectedResult['cube'] = 'ooyrrrrrrggrggggggyygooyoooyryobbbbbrbbyyybbowwwwwwwww'
        actualResult = solve._solveFrontLeftMiddlePiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test1010_090FrontColorPieceIsL01(self):
        inputDict = {}
        inputDict['cube'] = 'rygbrrrrroyyggggggoryoooooobrybbybbbrybbyoggywwwwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'uulULUFuf'
        expectedResult['cube'] = 'bybrrrrrryyrgggggggygoooooooyybbbbbbybyoyrrgowwwwwwwww'
        actualResult = solve._solveFrontLeftMiddlePiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
    
    def test1010_1000FrontColorPieceIsL10(self):
        inputDict = {}
        inputDict['cube'] = 'gbyrrrrrrbybggggggyygooboooogrrbybbbyboyyoyorwwwwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'LulubUBulULUFuf'
        expectedResult['cube'] = 'gborrrrrrbyyggggggbyoooyoooybrobbbbbgrroygyyywwwwwwwww'
        actualResult = solve._solveFrontLeftMiddlePiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
    
    def test1010_2000FrontColorPieceIsL12(self):
        inputDict = {}
        inputDict['cube'] = 'roybrrrrrgrgggggggyyooooooobgbbbrbbbybryyyyyowwwwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'lULUFufUlULUFuf'
        expectedResult['cube'] = 'rgrrrrrrryobggggggyyyoooooogyybbbbbborobyygybwwwwwwwww'
        actualResult = solve._solveFrontLeftMiddlePiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test1010_3000FrontColorPieceIsU01(self):
        inputDict = {}
        inputDict['cube'] = 'roogrrrrrybyggggggbbbooooooyyybbybbborrryygygwwwwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'FufulUL'
        expectedResult['cube'] = 'yoorrrrrrygrggggggyrroooooogbbbbbbbbyybyyyoygwwwwwwwww'
        actualResult = solve._solveFrontLeftMiddlePiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test1010_4000FrontColorPieceIsU10(self):
        inputDict = {}
        inputDict['cube'] = 'yyygrrrrrrooggggggybyoooooobbbbbybbbrygryyorgwwwwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'UFufulUL'
        expectedResult['cube'] = 'yoorrrrrrygrggggggyrroooooogbbbbbbbbyybyyyoygwwwwwwwww'
        actualResult = solve._solveFrontLeftMiddlePiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test1010_5000FrontColorPieceIsU12(self):
        inputDict = {}
        inputDict['cube'] = 'ybygrrrrrbbbggggggyyyooooooroobbybbbgroyyrgyrwwwwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'uFufulUL'
        expectedResult['cube'] = 'yoorrrrrrygrggggggyrroooooogbbbbbbbbyybyyyoygwwwwwwwww'
        actualResult = solve._solveFrontLeftMiddlePiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
    
    def test1010_6000FrontColorPieceIsU21(self):
        inputDict = {}
        inputDict['cube'] = 'bbbgrrrrryyyggggggrooooooooybybbybbbgygyyrrrowwwwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'uuFufulUL'
        expectedResult['cube'] = 'yoorrrrrrygrggggggyrroooooogbbbbbbbbyybyyyoygwwwwwwwww'
        actualResult = solve._solveFrontLeftMiddlePiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
# 1020 _solveFrontRightMiddlePiece
#    inputs: 
#        parms:    dict; mandatory; arrives validated
#        parms['cube']:    string; len=54; [brgoyw]; 9 occurrences of each character, unique middle character; mandatory; arrives validated
#    outputs:
#        side-effects:    non state changes; no external effects
#        returns:    dict
#        nominal: 
#            dict['rotations']: string, valid rotations to get proper rotations for front right middle piece
#            dict['cube']: string, valid cube after rotation for front right middle piece is performed
#        abnormal: 
#            no abnormal behavior since method is only called after cube is validated and down layer is solved
#    confidence level: boundary value analysis
#
#    happy path:
#        test010: front color piece is F01
#        test020: front color piece is R01
#        test030: front color piece is R10
#        test040: front color piece is R12
#        test050: front color piece is B01
#        test060: front color piece is B10
#        test070: front color piece is B12
#        test080: front color piece is L01
#        test090: front color piece is L10
#        test1000: front color piece is U01
#        test2000: front color piece is U10
#        test3000: front color piece is U12
#        test4000: front color piece is U21
    
    def test1020_010FrontColorPieceIsF01(self):
        inputDict = {}
        inputDict['cube'] = 'brrrrrrrrygoygggggyygooooooyyobbbbbbrbgoyyygbwwwwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'URurufUF'
        expectedResult['cube'] = 'gyrrrrrrryygggggggyyyoooooooyybbbbbbbrrgyboobwwwwwwwww'
        actualResult = solve._solveFrontRightMiddlePiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test1020_020FrontColorPieceIsR01(self):
        inputDict = {}
        inputDict['cube'] = 'yobrryrrryryrgggggrgyoooooobyobbbbbbrygbyggyowwwwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'UURurufUF'
        expectedResult['cube'] = 'royrrrrrrryoggggggyrooooooobybbbbbbbyyggybyygwwwwwwwww'
        actualResult = solve._solveFrontRightMiddlePiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
    
    def test1020_030FrontColorPieceIsR10(self):
        inputDict = {}
        inputDict['cube'] = 'oryrrgrrrbyyrgggggryyoooooooygbbbbbbbogbygyyrwwwwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'RurufUFuRurufUF'
        expectedResult['cube'] = 'yybrrrrrryygggggggobgooooooyrrbbbbbbryyyyobgowwwwwwwww'
        actualResult = solve._solveFrontRightMiddlePiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test1020_040FrontColorPieceIsR12(self):
        inputDict = {}
        inputDict['cube'] = 'ygorryrrryrgggrgggyoogooooobyrbbbbbbyyrbyybogwwwwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'BuburURUfUFURur'
        expectedResult['cube'] = 'ryorrrrrrbygggggggoyrooooooyyybbbbbbboygyrgbywwwwwwwww'
        actualResult = solve._solveFrontRightMiddlePiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test1020_050FrontColorPieceIsB01(self):
        inputDict = {}
        inputDict['cube'] = 'bgrrryrrryygrgggggyroooooooybobbbbbbggryyoyybwwwwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'uRurufUF'
        expectedResult['cube'] = 'yyorrrrrrygrggggggyrroooooogybbbbbbbyybbyyoogwwwwwwwww'
        actualResult = solve._solveFrontRightMiddlePiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test1020_060FrontColorPieceIsB10(self):
        inputDict = {}
        inputDict['cube'] = 'yrrrrbrrrgoyygggggggbrooooorobbbbbbbyyogyyoyywwwwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'BuburURRurufUF'
        expectedResult['cube'] = 'ygorrrrrrborggrggggyyyoooooboobbbbbbrbyyyggyywwwwwwwww'
        actualResult = solve._solveFrontRightMiddlePiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test1020_070FrontColorPieceIsB12(self):
        inputDict = {}
        inputDict['cube'] = 'yrrrryrrrgorggggggybbooroooyyogbbbbboyboybgyywwwwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'bUBULulUURurufUF'
        expectedResult['cube'] = 'gorrrrrrryooggggggbgrooyooogyyrbbbbbyyybyboybwwwwwwwww'
        actualResult = solve._solveFrontRightMiddlePiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test1020_080FrontColorPieceIsL01(self):
        inputDict = {}
        inputDict['cube'] = 'rryrrbrrroybygggggryyoooooogrybbbbbbooygyggybwwwwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'RurufUF'
        expectedResult['cube'] = 'byyrrrrrrrybggggggryoooooooyyobbbbbbgbyrygyogwwwwwwwww'
        actualResult = solve._solveFrontRightMiddlePiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test1020_090FrontColorPieceIsL10(self):
        inputDict = {}
        inputDict['cube'] = 'yyyrrgrrrgoyygggggryroogoooyybrbbbbbbbgrybooowwwwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'LulubUBURurufUF'
        expectedResult['cube'] = 'ryorrrrrryyyggggggryooooooobybbbbbbbyggbyoyrgwwwwwwwww'
        actualResult = solve._solveFrontRightMiddlePiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test1020_1000FrontColorPieceIsU01(self):
        inputDict = {}
        inputDict['cube'] = 'gobrrrrrrybyygggggrgrooooooyyybbbbbbbrggyyoyowwwwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'fUFURur'
        expectedResult['cube'] = 'goyrrrrrrryoggggggbyyoooooobrybbbbbbrbyyygoygwwwwwwwww'
        actualResult = solve._solveFrontRightMiddlePiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
    
    def test1020_2000FrontColorPieceIsU10(self):
        inputDict = {}
        inputDict['cube'] = 'yyyrrrrrrgobygggggybyoooooorgrbbbbbbgyoryybgowwwwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'UfUFURur'
        expectedResult['cube'] = 'goyrrrrrrryoggggggbyyoooooobrybbbbbbrbyyygoygwwwwwwwww'
        actualResult = solve._solveFrontRightMiddlePiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test1020_3000FrontColorPieceIsU12(self):
        inputDict = {}
        inputDict['cube'] = 'ybyrrrrrrrgrygggggyyyoooooogobbbbbbbogbyyroygwwwwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'ufUFURur'
        expectedResult['cube'] = 'goyrrrrrrryoggggggbyyoooooobrybbbbbbrbyyygoygwwwwwwwww'
        actualResult = solve._solveFrontRightMiddlePiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
    
    def test1020_4000FrontColorPieceIsU21(self):
        inputDict = {}
        inputDict['cube'] = 'rgrrrrrrryyyyggggggobooooooybybbbbbboyoyyggrbwwwwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'uufUFURur'
        expectedResult['cube'] = 'goyrrrrrrryoggggggbyyoooooobrybbbbbbrbyyygoygwwwwwwwww'
        actualResult = solve._solveFrontRightMiddlePiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
# 1030 _solveBackLeftMiddlePiece
#    inputs: 
#        parms:    dict; mandatory; arrives validated
#        parms['cube']:    string; len=54; [brgoyw]; 9 occurrences of each character, unique middle character; mandatory; arrives validated
#    outputs:
#        side-effects:    non state changes; no external effects
#        returns:    dict
#        nominal: 
#            dict['rotations']: string, valid rotations to get proper rotations for back left middle piece
#            dict['cube']: string, valid cube after rotation for back left middle piece is performed
#        abnormal: 
#            no abnormal behavior since method is only called after cube is validated and down layer is solved
#    confidence level: boundary value analysis
#
#    happy path:
#        test010: back color piece is F01
#        test020: back color piece is R01
#        test030: back color piece is R12
#        test040: back color piece is B01
#        test050: back color piece is B10
#        test060: back color piece is L01
#        test070: back color piece is L10
#        test080: back color piece is U01
#        test090: back color piece is U10
#        test1000: back color piece is U12
#        test2000: back color piece is U21
    
    def test1030_010BackColorPieceIsF01(self):
        inputDict = {}
        inputDict['cube'] = 'ooyrrrrrrryyggggggboyooyoooobgrbbbbbbyryygybgwwwwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'uLulubUB'
        expectedResult['cube'] = 'oryrrrrrrggbggggggrbyooooooroybbbbbbgyyyyybyowwwwwwwww'
        actualResult = solve._solveBackLeftMiddlePiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test1030_020BackColorPieceIsR01(self):
        inputDict = {}
        inputDict['cube'] = 'obgrrrrrrooyggggggryyooyoooboyrbbbbbrggyybbyywwwwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'LulubUB'
        expectedResult['cube'] = 'oryrrrrrrggbggggggrbyooooooroybbbbbbgyyyyybyowwwwwwwww'
        actualResult = solve._solveBackLeftMiddlePiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test1030_030BackColorPieceIsR12(self):
        inputDict = {}
        inputDict['cube'] = 'ggbrrrrrrryyggogggoyoboyoooyyrbbbbbbgrboygyoywwwwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'BuburURubUBULul'
        expectedResult['cube'] = 'brrrrrrrrgyoggggggbyoooooooygybbbbbbgoyyybryywwwwwwwww'
        actualResult = solve._solveBackLeftMiddlePiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test1030_040BackColorPieceIsB01(self):
        inputDict = {}
        inputDict['cube'] = 'boyrrrrrrobgggggggooyooyoooryyrbbbbbgbygyyrybwwwwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'ULulubUB'
        expectedResult['cube'] = 'oryrrrrrrggbggggggrbyooooooroybbbbbbgyyyyybyowwwwwwwww'
        actualResult = solve._solveBackLeftMiddlePiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test1030_050BackColorPieceIsB10(self):
        inputDict = {}
        inputDict['cube'] = 'ryyrrrrrrgryggbgggbooooyoooboygbbbbbyyrgyygbowwwwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'BuburURuuLulubUB'
        expectedResult['cube'] = 'ggyrrrrrrorrggygggyogboooooyoybbbbbbrybgyyoybwwwwwwwww'
        actualResult = solve._solveBackLeftMiddlePiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test1030_060BackColorPieceIsL01(self):
        inputDict = {}
        inputDict['cube'] = 'ryyrrrrrrboyggggggobgooyoooooyrbbbbbyybbyyggrwwwwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'uuLulubUB'
        expectedResult['cube'] = 'oryrrrrrrggbggggggrbyooooooroybbbbbbgyyyyybyowwwwwwwww'
        actualResult = solve._solveBackLeftMiddlePiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test1030_070BackColorPieceIsL10(self):
        inputDict = {}
        inputDict['cube'] = 'gborrrrrrbybggggggrggoobooooorobbbbbyyyyyryyywwwwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'LulubUBuLulubUB'
        expectedResult['cube'] = 'rryrrrrrrrgygggggggoyooooooobbbbbbbbbyoyyyyygwwwwwwwww'
        actualResult = solve._solveBackLeftMiddlePiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test1030_080BackColorPieceIsU01(self):
        inputDict = {}
        inputDict['cube'] = 'ygyrrrrrroryggggggrboooooooyyrybbbbbgogbyybybwwwwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'uubUBULul'
        expectedResult['cube'] = 'yyyrrrrrrgorggggggygyoooooorybbbbbbbgybbyyorowwwwwwwww'
        actualResult = solve._solveBackLeftMiddlePiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test1030_090BackColorPieceIsU10(self):
        inputDict = {}
        inputDict['cube'] = 'yyrrrrrrrygyggggggoryoooooorboybbbbbgyboyygbbwwwwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'ubUBULul'
        expectedResult['cube'] = 'yyyrrrrrrgorggggggygyoooooorybbbbbbbgybbyyorowwwwwwwww'
        actualResult = solve._solveBackLeftMiddlePiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test1030_1000BackColorPieceIsU12(self):
        inputDict = {}
        inputDict['cube'] = 'oryrrrrrrrboggggggyyrooooooygyybbbbbbbgyyobygwwwwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'UbUBULul'
        expectedResult['cube'] = 'yyyrrrrrrgorggggggygyoooooorybbbbbbbgybbyyorowwwwwwwww'
        actualResult = solve._solveBackLeftMiddlePiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test1030_2000BackColorPieceIsU21(self):
        inputDict = {}
        inputDict['cube'] = 'rborrrrrryyrggggggygyoooooooryybbbbbbybyybgogwwwwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'bUBULul'
        expectedResult['cube'] = 'yyyrrrrrrgorggggggygyoooooorybbbbbbbgybbyyorowwwwwwwww'
        actualResult = solve._solveBackLeftMiddlePiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
# 1040 _solveBackRightMiddlePiece
#    inputs: 
#        parms:    dict; mandatory; arrives validated
#        parms['cube']:    string; len=54; [brgoyw]; 9 occurrences of each character, unique middle character; mandatory; arrives validated
#    outputs:
#        side-effects:    non state changes; no external effects
#        returns:    dict
#        nominal: 
#            dict['rotations']: string, valid rotations to get proper rotations for back right middle piece
#            dict['cube']: string, valid cube after rotation for back right middle piece is performed
#        abnormal: 
#            no abnormal behavior since method is only called after cube is validated and down layer is solved
#    confidence level: boundary value analysis
#
#    happy path:
#        test010: back color piece is F01
#        test020: back color piece is R01
#        test030: back color piece is R12
#        test040: back color piece is B01
#        test050: back color piece is L01
#        test060: back color piece is U01
#        test070: back color piece is U10
#        test080: back color piece is U12
#        test090: back color piece is U21

    def test1040_010BackColorPieceIsF01(self):
        inputDict = {}
        inputDict['cube'] = 'yobrrrrrrrygggggggoryyoooooobgbbbbbbbyyyyorgywwwwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'UrURUBub'
        expectedResult['cube'] = 'yggrrrrrrorgggggggyybooooooyyrbbbbbboorbyybyywwwwwwwww'
        actualResult = solve._solveBackRightMiddlePiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
    
    def test1040_020BackColorPieceIsR01(self):
        inputDict = {}
        inputDict['cube'] = 'obgrrrrrryobggggggrygyoooooorybbbbbbyoyyygbyrwwwwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'uurURUBub'
        expectedResult['cube'] = 'yggrrrrrrorgggggggyybooooooyyrbbbbbboorbyybyywwwwwwwww'
        actualResult = solve._solveBackRightMiddlePiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test1040_030BackColorPieceIsR12(self):
        inputDict = {}
        inputDict['cube'] = 'ryrrrrrrryroggogggyyygooooooyybbbbbbbogbyyggbwwwwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'rURUBubUrURUBub'
        expectedResult['cube'] = 'bbyrrrrrroyrgggggggryoooooogyybbbbbboyyoygrybwwwwwwwww'
        actualResult = solve._solveBackRightMiddlePiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test1040_040BackColorPieceIsB01(self):
        inputDict = {}
        inputDict['cube'] = 'oryrrrrrrobgggggggyobyooooorygbbbbbbygroyyyybwwwwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'urURUBub'
        expectedResult['cube'] = 'yggrrrrrrorgggggggyybooooooyyrbbbbbboorbyybyywwwwwwwww'
        actualResult = solve._solveBackRightMiddlePiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test1040_050BackColorPieceIsL01(self):
        inputDict = {}
        inputDict['cube'] = 'rygrrrrrroryggggggobgyoooooyobbbbbbbrybgyyyoywwwwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'rURUBub'
        expectedResult['cube'] = 'yggrrrrrrorgggggggyybooooooyyrbbbbbboorbyybyywwwwwwwww'
        actualResult = solve._solveBackRightMiddlePiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test1040_060BackColorPieceIsU01(self):
        inputDict = {}
        inputDict['cube'] = 'gbyrrrrrrrybggogggrgyyooooooyybbbbbbboygyroygwwwwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'UUBuburUR'
        expectedResult['cube'] = 'bggrrrrrroyyggggggobyooooooryybbbbbbgyboyrryywwwwwwwww'
        actualResult = solve._solveBackRightMiddlePiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test1040_070BackColorPieceIsU10(self):
        inputDict = {}
        inputDict['cube'] = 'oyyrrrrrrgbyggogggrybyooooorgybbbbbbyrgoyybgowwwwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'uBuburUR'
        expectedResult['cube'] = 'bggrrrrrroyyggggggobyooooooryybbbbbbgyboyrryywwwwwwwww'
        actualResult = solve._solveBackRightMiddlePiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test1040_080BackColorPieceIsU12(self):
        inputDict = {}
        inputDict['cube'] = 'rybrrrrrrrgyggogggoyyyooooogbybbbbbbogbyyogrywwwwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'UBuburUR'
        expectedResult['cube'] = 'bggrrrrrroyyggggggobyooooooryybbbbbbgyboyrryywwwwwwwww'
        actualResult = solve._solveBackRightMiddlePiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test1040_090BackColorPieceIsU21(self):
        inputDict = {}
        inputDict['cube'] = 'rgyrrrrrroyyggoggggbyyooooorybbbbbbbgyorygyobwwwwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'BuburUR'
        expectedResult['cube'] = 'bggrrrrrroyyggggggobyooooooryybbbbbbgyboyrryywwwwwwwww'
        actualResult = solve._solveBackRightMiddlePiece(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
# 1050 _solveMiddleLayer
#    inputs: 
#        parms:    dict; mandatory; arrives validated
#        parms['cube']:    string; len=54; [brgoyw]; 9 occurrences of each character, unique middle character; mandatory; arrives validated
#    outputs:
#        side-effects:    non state changes; no external effects
#        returns:    dict
#        nominal: 
#            dict['rotations']: string, valid rotations to solve middle layer
#            dict['cube']: string, valid cube after rotations for middle layer are performed
#        abnormal: 
#            no abnormal behavior since method is only called if down layer is solved and cube is already validated
#    confidence level: boundary value analysis
#
#    happy path:
#        test010: valid cube with solved down layer
#        test020: valid cube with solved down and middle layer

    def test1050_010ValidCubeWithSolvedDownLayer(self):
        inputDict = {}
        inputDict['cube'] = 'bygbrbrrryyyrgoggggrbyogoooygyobobbbogoyyrrbrwwwwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'RurufUFUlULUFufRurufUFuLulubUBUrURUBub'
        expectedResult['cube'] = 'boyrrrrrroygggggggyyoooooooygybbbbbbgrryybrybwwwwwwwww'
        actualResult = solve._solveMiddleLayer(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test1050_020ValidCubeWithSolvedDownAndMiddleLayers(self):
        inputDict = {}
        inputDict['cube'] = 'rybrrrrrryyyggggggbooooooooybybbbbbbgyryyrggowwwwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = ''
        expectedResult['cube'] = 'rybrrrrrryyyggggggbooooooooybybbbbbbgyryyrggowwwwwwwww'
        actualResult = solve._solveMiddleLayer(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
# 1060 _solveUpCross
#    inputs: 
#        parms:    dict; mandatory; arrives validated
#        parms['cube']:    string; len=54; [brgoyw]; 9 occurrences of each character, unique middle character; mandatory; arrives validated
#    outputs:
#        side-effects:    non state changes; no external effects
#        returns:    dict
#        nominal: 
#            dict['rotations']: string, valid rotations to solve up surface cross
#            dict['cube']: string, valid cube after rotations for up surface cross are performed
#        abnormal: 
#            no abnormal behavior since method is only called if down layer and middle layer are solved and cube is already validated
#    confidence level: boundary value analysis
#
#    happy path:
#        test010: valid cube with no part of cross
#        test020: valid cube with L part of cross
#        test030: valid cube with line part of cross

    def test1060_010ValidCubeWithNoPartOfCross(self):
        inputDict = {}
        inputDict['cube'] = 'yygrrrrrryygggggggoybooooooyyrbbbbbbooybygbrrwwwwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'FRUrufuuFRUruRUruf'
        expectedResult['cube'] = 'yborrrrrryorggggggggrooooooyrbbbbbbbbyyyyyoygwwwwwwwww'
        actualResult = solve._solveUpCross(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test1060_020ValidCubeWithLPartOfCross(self):
        inputDict = {}
        inputDict['cube'] = 'yrybbbbbbobbrrrrrrryrgggggggyoooooooygyoyygybwwwwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'uuFRUruRUruf'
        expectedResult['cube'] = 'yogbbbbbbyrgrrrrrrogbggggggybroooooooyyyyybyrwwwwwwwww'
        actualResult = solve._solveUpCross(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test1060_030ValidCubeWithLinePartOfCross(self):
        inputDict = {}
        inputDict['cube'] = 'ybrrrrrrrgyrggggggygbooooooyyobbbbbboyboyrgyywwwwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'uFRUruf'
        expectedResult['cube'] = 'yryrrrrrroobggggggrbrooooooggobbbbbbyyyyyygybwwwwwwwww'
        actualResult = solve._solveUpCross(inputDict)
        self.assertDictEqual(expectedResult, actualResult)

# 1070 _solveUpFace
#    inputs: 
#        parms:    dict; mandatory; arrives validated
#        parms['cube']:    string; len=54; [brgoyw]; 9 occurrences of each character, unique middle character; mandatory; arrives validated
#    outputs:
#        side-effects:    non state changes; no external effects
#        returns:    dict
#        nominal: 
#            dict['rotations']: string, valid rotations to solve up face of cube
#            dict['cube']: string, valid cube after rotations for up face are performed
#        abnormal: 
#            no abnormal behavior since method is only called if down and middle layer are solved and top cross is solved; cube is already validated
#    confidence level: boundary value analysis
#
#    happy path:  
#        test010: Valid cube with no up corners solved (this also tests fish configuration)
#        test020: Valid cube with two adjacent corners solved
#        test030: Valid cube with two diagonal corners solved

    def test1070_010ValidCubeWithNoUpCornersSolved(self):
        inputDict = {}
        inputDict['cube'] = 'yryrrrrrrbgbggggggyoyoooooogbgbbbbbboyoyyyryrwwwwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'URUrURUUrRUrURUUr'
        expectedResult['cube'] = 'rgorrrrrrbbgggggggorroooooogobbbbbbbyyyyyyyyywwwwwwwww'
        actualResult = solve._solveUpFace(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test1070_020ValidCubeWithTwoAdjacentCornersSolved(self):
        inputDict = {}
        inputDict['cube'] = 'ooyrrrrrrrgrggggggyrooooooobbgbbbbbbyybyyyyygwwwwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'UURUrURUUrURUrURUUrUURUrURUUr'
        expectedResult['cube'] = 'bbgrrrrrrorrgggggggoboooooorgobbbbbbyyyyyyyyywwwwwwwww'
        actualResult = solve._solveUpFace(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
    
    def test1070_030ValidCubeWithTwoDiagonalCornersSolved(self):
        inputDict = {}
        inputDict['cube'] = 'yborrrrrrbgyggggggbrroooooogoobbbbbbyyryyygyywwwwwwwww'
        expectedResult = {}
        expectedResult['rotations'] = 'RUrURUUrRUrURUUrUURUrURUUr'
        expectedResult['cube'] = 'ooorrrrrrbrbggggggrgroooooogbgbbbbbbyyyyyyyyywwwwwwwww'
        actualResult = solve._solveUpFace(inputDict)
        self.assertDictEqual(expectedResult, actualResult)
     
        
        
        