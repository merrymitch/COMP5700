import rubik.cube as cube
import rubik.verify as verify
import rubik.rotate as rotate

#Assign the cube mapping to each of the cube faces
F00, F01, F02, F10, F11, F12, F20, F21, F22 = 0, 1, 2, 3, 4, 5, 6, 7, 8
R00, R01, R02, R10, R11, R12, R20, R21, R22 = 9, 10, 11, 12, 13, 14, 15, 16, 17
B00, B01, B02, B10, B11, B12, B20, B21, B22 = 18, 19, 20, 21, 22, 23, 24, 25, 26
L00, L01, L02, L10, L11, L12, L20, L21, L22 = 27, 28, 29, 30, 31, 32, 33, 34, 35
U00, U01, U02, U10, U11, U12, U20, U21, U22 = 36, 37, 38, 39, 40, 41, 42, 43, 44
D00, D01, D02, D10, D11, D12, D20, D21, D22 = 45, 46, 47, 48, 49, 50, 51, 52, 53

def _solve(parms):
    """ Return rotates needed to solve input cube """
    result = {}
    rotations = ''
    
    # Call verify to determine if the passed cube is a valid rubik's cube
    isCubeValid = verify._verify(parms)
    if (isCubeValid['status'] != 'ok'):
        result['status'] = 'error: invalid cube'
        return result
    
    # Call methods to solve each part of the cube
    solveCube = _solveDaisyAndDownCross(parms)
    rotations += solveCube.get('rotations')
    solveCube = _solveDownCorners(solveCube)
    rotations += solveCube.get('rotations')
    
    # Put the solution in result and return it
    result['rotations'] = rotations
    result['status'] = 'ok' 
                    
    return result

def _solveDaisyAndDownCross(parms):
    """ Refactored method to solve the daisy and down cross of the cube """
    encodedCube = parms.get('cube')
    result = {}
    
    # Check if down face cross is already solved
    downCrossChars = {encodedCube[D01], encodedCube[D10], encodedCube[D11], encodedCube[D12], encodedCube[D21]}
    if len(downCrossChars) == 1:
        result['rotations'] = ''
        result['cube'] = encodedCube
        return result
        
    # Initialize variables for the solve functions
    solveCube = {}
    solveCube['cube'] = encodedCube
    rotations = ''
    
    # Call function to solve the daisy and get the rotations
    daisyCube = _solveDaisy(solveCube)
    solveCube['cube'] = daisyCube.get('cube')
    rotations += daisyCube.get('rotations')
    
    # Call function to solve the down cross and get the rotations
    downCrossCube = _solveDownCross(solveCube)
    solveCube['cube'] = downCrossCube.get('cube')
    rotations += downCrossCube.get('rotations')
    
    result['cube'] = solveCube.get('cube')
    result['rotations'] = rotations
    return result

def _solveDownCorners(parms):
    """ Method to solve the down corners of the cube """
    solveCube = {}
    solveCube['cube'] = parms.get('cube')
    rotations = ''
    searchDict = {}
    result = {}
    
    # For each down corner check if it is already solved and if not solve it
    searchDict['cube'] = solveCube.get('cube')
    searchDict['colors'] = {solveCube.get('cube')[D11], solveCube.get('cube')[F11], solveCube.get('cube')[L11]}
    if _findDownCorner(searchDict) != D00:
        solveCube = _solveFrontLeftDownCorner(solveCube)
        rotations += solveCube.get('rotations')
        
    searchDict['cube'] = solveCube.get('cube')
    searchDict['colors'] = {solveCube.get('cube')[D11], solveCube.get('cube')[F11], solveCube.get('cube')[R11]}
    if _findDownCorner(searchDict) != D02:
        solveCube = _solveFrontRightDownCorner(solveCube)
        rotations += solveCube.get('rotations')
    
    searchDict['cube'] = solveCube.get('cube')
    searchDict['colors'] = {solveCube.get('cube')[D11], solveCube.get('cube')[L11], solveCube.get('cube')[B11]}
    if _findDownCorner(searchDict) != D20:
        solveCube = _solveBackLeftDownCorner(solveCube)
        rotations += solveCube.get('rotations')
    
    searchDict['cube'] = solveCube.get('cube')
    searchDict['colors'] = {solveCube.get('cube')[D11], solveCube.get('cube')[R11], solveCube.get('cube')[B11]}
    if _findDownCorner(searchDict) != D22:
        solveCube = _solveBackRightDownCorner(solveCube)
        rotations += solveCube.get('rotations')
    
    # Return the rotations to solve the down corners and the resulting cube
    result['cube'] = solveCube.get('cube')
    result['rotations'] = rotations
    return result
        
def _solveDaisy(parms):
    """ Determines which of the daisy pieces need solving and calls function to solve them """
    result = {}
    solveCube = {}
    solveCube['cube'] = parms.get('cube')
    rotations = ''
     
    # If the daisy piece is not in correct place call the corresponding function to solve it
    if solveCube.get('cube')[U21] != solveCube.get('cube')[D11]:
        solveCube = _solveBottomDaisyPiece(solveCube)
        rotations += solveCube.get('rotations')
    if solveCube.get('cube')[U12] != solveCube.get('cube')[D11]:
        solveCube = _solveRightDaisyPiece(solveCube)
        rotations += solveCube.get('rotations')
    if solveCube.get('cube')[U10] != solveCube.get('cube')[D11]:
        solveCube = _solveLeftDaisyPiece(solveCube)
        rotations += solveCube.get('rotations')
    if solveCube.get('cube')[U01] != solveCube.get('cube')[D11]:
        solveCube = _solveTopDaisyPiece(solveCube)
        rotations += solveCube.get('rotations')
    
    # Return the rotations to solve the daisy
    result['rotations'] = rotations
    result['cube'] = solveCube.get('cube')
    return result

def _solveDownCross(parms):
    """ Once daisy is solved call functions to put the daisy pieces in the corresponding down cross place """
    result = {}
    solveCube = {}
    solveCube['cube'] = parms.get('cube')
    rotations = ''
    
    # Put each daisy piece in its correct down cross place
    solveCube = _putBottomDaisyInDownCross(solveCube)
    rotations += solveCube.get('rotations')
    solveCube = _putRightDaisyInDownCross(solveCube)
    rotations += solveCube.get('rotations')
    solveCube = _putLeftDaisyInDownCross(solveCube)
    rotations += solveCube.get('rotations')
    solveCube = _putTopDaisyInDownCross(solveCube)
    rotations += solveCube.get('rotations')
    
    # Return the rotations to solve the down cross
    result['rotations'] = rotations
    result['cube'] = solveCube.get('cube')
    return result

def _solveBottomDaisyPiece(parms):
    """ Finds a down colored piece to put in U21 daisy spot """
    rotations = ''
    cubeValue = parms.get('cube')
    output = {}
        
    # Find a down colored piece and put it in correct place in daisy
    if cubeValue[L12] == cubeValue[D11]: rotations = 'F'
    elif cubeValue[R10] == cubeValue[D11]: rotations = 'f'
    elif cubeValue[D01] == cubeValue[D11]: rotations = 'FF'
    elif cubeValue[L01] == cubeValue[D11]: rotations = 'LF'
    elif cubeValue[R01] == cubeValue[D11]: rotations = 'rf'
    elif cubeValue[D10] == cubeValue[D11]: rotations = 'DFF'
    elif cubeValue[B12] == cubeValue[D11]: rotations = 'ULu'
    elif cubeValue[F12] == cubeValue[D11]: rotations = 'uRU'
    elif cubeValue[F10] == cubeValue[D11]: rotations = 'Ulu'
    elif cubeValue[B10] == cubeValue[D11]: rotations = 'urU'
    elif cubeValue[D12] == cubeValue[D11]: rotations = 'dFF'
    elif cubeValue[F01] == cubeValue[D11]: rotations = 'FuRU'
    elif cubeValue[L21] == cubeValue[D11]: rotations = 'UluF'
    elif cubeValue[F21] == cubeValue[D11]: rotations = 'fuRU'
    elif cubeValue[B01] == cubeValue[D11]: rotations = 'burU'
    elif cubeValue[D21] == cubeValue[D11]: rotations = 'ddFF'
    elif cubeValue[R12] == cubeValue[D11]: rotations = 'uuBUU'
    elif cubeValue[L10] == cubeValue[D11]: rotations = 'UUbuu'
    elif cubeValue[R21] == cubeValue[D11]: rotations = 'uruBUU'
    elif cubeValue[B21] == cubeValue[D11]: rotations = 'uubuLu'
    rotatedCube = _rotatePiece(rotations, cubeValue)
        
    # Return the rotations to get correct U21 Daisy piece and the cube after rotations
    output['rotations'] = rotations
    output['cube'] = rotatedCube
    return output

def _solveRightDaisyPiece(parms):
    """ Finds a down colored piece to put in U12 daisy spot """
    rotations = ''
    cubeValue = parms.get('cube')
    output = {}
    
    # Find a down colored piece and put it in correct place in daisy
    if cubeValue[F12] == cubeValue[D11]: rotations = 'R'
    elif cubeValue[B10] == cubeValue[D11]: rotations = 'r'
    elif cubeValue[D12] == cubeValue[D11]: rotations = 'RR'
    elif cubeValue[B01] == cubeValue[D11]: rotations = 'br'
    elif cubeValue[D01] == cubeValue[D11]: rotations = 'DRR'
    elif cubeValue[L12] == cubeValue[D11]: rotations = 'UFu' 
    elif cubeValue[R12] == cubeValue[D11]: rotations = 'uBU'
    elif cubeValue[D21] == cubeValue[D11]: rotations = 'dRR'
    elif cubeValue[R10] == cubeValue[D11]: rotations = 'Ufu'
    elif cubeValue[L10] == cubeValue[D11]: rotations = 'ubU' 
    elif cubeValue[D10] == cubeValue[D11]: rotations = 'DDRR'
    elif cubeValue[L01] == cubeValue[D11]: rotations = 'LUFu'
    elif cubeValue[F21] == cubeValue[D11]: rotations = 'UfuR'
    elif cubeValue[R01] == cubeValue[D11]: rotations = 'rUfu'
    elif cubeValue[R21] == cubeValue[D11]: rotations = 'ruBU'
    elif cubeValue[B21] == cubeValue[D11]: rotations = 'druBU'
    elif cubeValue[B12] == cubeValue[D11]: rotations = 'uuLuu'
    elif cubeValue[F10] == cubeValue[D11]: rotations = 'uuluu'
    elif cubeValue[L21] == cubeValue[D11]: rotations = 'UULUbU'
    rotatedCube = _rotatePiece(rotations, cubeValue)
    
    # Return the rotations to get correct U12 Daisy piece and the cube after rotations
    output['rotations'] = rotations
    output['cube'] = rotatedCube
    return output

def _solveLeftDaisyPiece(parms):
    """ Finds a down colored piece to put in U10 daisy spot """
    rotations = ''
    cubeValue = parms.get('cube')
    output = {}
    
    # Find a down colored piece and put it in correct place in daisy
    if cubeValue[B12] == cubeValue[D11]: rotations = 'L'
    elif cubeValue[F10] == cubeValue[D11]: rotations = 'l'
    elif cubeValue[B01] == cubeValue[D11]: rotations = 'BL'
    elif cubeValue[D10] == cubeValue[D11]: rotations = 'll'
    elif cubeValue[R12] == cubeValue[D11]: rotations = 'UBu'
    elif cubeValue[L12] == cubeValue[D11]: rotations = 'uFU'
    elif cubeValue[L10] == cubeValue[D11]: rotations = 'Ubu'
    elif cubeValue[D21] == cubeValue[D11]: rotations = 'Dll'
    elif cubeValue[R10] == cubeValue[D11]: rotations = 'ufU'
    elif cubeValue[D01] == cubeValue[D11]: rotations = 'dll'
    elif cubeValue[L01] == cubeValue[D11]: rotations = 'LuFU'
    elif cubeValue[L21] == cubeValue[D11]: rotations = 'LUbu'
    elif cubeValue[F21] == cubeValue[D11]: rotations = 'uFUl'
    elif cubeValue[D12] == cubeValue[D11]: rotations = 'ddll'
    elif cubeValue[B10] == cubeValue[D11]: rotations = 'UUrUU'
    elif cubeValue[F12] == cubeValue[D11]: rotations = 'uuRuu'
    elif cubeValue[B21] == cubeValue[D11]: rotations = 'UBUrUU'
    elif cubeValue[R21] == cubeValue[D11]: rotations = 'uuruBu'
    rotatedCube = _rotatePiece(rotations, cubeValue)
        
    # Return the rotations to get correct U10 Daisy piece and the cube after rotations
    output['rotations'] = rotations
    output['cube'] = rotatedCube
    return output

def _solveTopDaisyPiece(parms):
    """ Finds a down colored piece to put in U01 daisy spot """
    rotations = ''
    cubeValue = parms.get('cube')
    output = {}
    
    # Find a down colored piece and put it in correct place in daisy
    if cubeValue[R12] == cubeValue[D11]: rotations = 'B'
    elif cubeValue[L10] == cubeValue[D11]: rotations = 'b'
    elif cubeValue[D21] == cubeValue[D11]: rotations = 'BB'
    elif cubeValue[D12] == cubeValue[D11]: rotations = 'DBB'
    elif cubeValue[F12] == cubeValue[D11]: rotations = 'URu'
    elif cubeValue[D10] == cubeValue[D11]: rotations = 'dBB'
    elif cubeValue[B12] == cubeValue[D11]: rotations = 'uLU'
    elif cubeValue[B10] == cubeValue[D11]: rotations = 'Uru'
    elif cubeValue[F10] == cubeValue[D11]: rotations = 'ulU'
    elif cubeValue[D01] == cubeValue[D11]: rotations = 'DDBB'
    elif cubeValue[B21] == cubeValue[D11]: rotations = 'BUru'
    elif cubeValue[R21] == cubeValue[D11]: rotations = 'UruB'
    elif cubeValue[L21] == cubeValue[D11]: rotations = 'uLUb'
    elif cubeValue[B01] == cubeValue[D11]: rotations = 'bUru'
    elif cubeValue[R10] == cubeValue[D11]: rotations = 'UUfUU'
    elif cubeValue[L12] == cubeValue[D11]: rotations = 'uuFuu'
    elif cubeValue[F21] == cubeValue[D11]: rotations = 'UUfuRu'
    rotatedCube = _rotatePiece(rotations, cubeValue)
        
    # Return the rotations to get correct U01 Daisy piece and the cube after rotations
    output['rotations'] = rotations
    output['cube'] = rotatedCube
    return output

def _putBottomDaisyInDownCross(parms):
    """ Finds the correct down cross space and rotations for U21 daisy piece """
    rotations = ''
    inputCube = parms.get('cube')
    output = {}
    
    # Find correct down cross space and rotations
    if inputCube[F01] == inputCube[F11]: rotations = 'FF'
    elif inputCube[F01] == inputCube[L11]: rotations = 'ULLu'
    elif inputCube[F01] == inputCube[R11]: rotations = 'urrU'
    elif inputCube[F01] == inputCube[B11]: rotations = 'UUbbUU'
    rotatedCube = _rotatePiece(rotations, inputCube)
    
    # Return the rotations to put U21 in correct down cross place and the rotated cube
    output['rotations'] = rotations
    output['cube'] = rotatedCube
    return output

def _putRightDaisyInDownCross(parms):
    """ Finds the correct down cross space and rotations for U12 daisy piece """
    rotations = ''
    inputCube = parms.get('cube')
    output = {}
    
    # Find correct down cross space and rotations
    if inputCube[R01] == inputCube[F11]: rotations = 'UFFu'
    elif inputCube[R01] == inputCube[L11]: rotations = 'UULLUU'
    elif inputCube[R01] == inputCube[R11]: rotations = 'RR'
    elif inputCube[R01] == inputCube[B11]: rotations = 'uBBU'
    rotatedCube = _rotatePiece(rotations, inputCube)
    
    # Return the rotations to put U12 in correct down cross place and the rotated cube   
    output['rotations'] = rotations
    output['cube'] = rotatedCube
    return output

def _putLeftDaisyInDownCross(parms):
    """ Finds the correct down cross space and rotations for U10 daisy piece """
    rotations = ''
    inputCube = parms.get('cube')
    output = {}
    
    # Find correct down cross space and rotations
    if inputCube[L01] == inputCube[F11]: rotations = 'uFFU'
    elif inputCube[L01] == inputCube[L11]: rotations = 'LL'
    elif inputCube[L01] == inputCube[R11]: rotations = 'UURRUU'
    elif inputCube[L01] == inputCube[B11]: rotations = 'UBBu'
    rotatedCube = _rotatePiece(rotations, inputCube)
    
    # Return the rotations to put U10 in correct down cross place and the rotated cube   
    output['rotations'] = rotations
    output['cube'] = rotatedCube
    return output

def _putTopDaisyInDownCross(parms):
    """ Finds the correct down cross space and rotations for U01 daisy piece """
    rotations = ''
    inputCube = parms.get('cube')
    output = {}
    
    # Find correct down cross space and rotations
    if inputCube[B01] == inputCube[F11]: rotations = 'UUFFUU'
    elif inputCube[B01] == inputCube[L11]: rotations = 'uLLU'
    elif inputCube[B01] == inputCube[R11]: rotations = 'URRu'
    elif inputCube[B01] == inputCube[B11]: rotations = 'BB'
    rotatedCube = _rotatePiece(rotations, inputCube)
    
    # Return the rotations to put U01 in correct down cross place and the rotated cube    
    output['rotations'] = rotations
    output['cube'] = rotatedCube
    return output

def _solveFrontLeftDownCorner(parms):
    """ Finds the correct down corner piece for D00 and gets the rotations to put it in place """
    rotations = ''
    inputCube = parms.get('cube')
    output = {}
    searchDict = {}
    searchDict['cube'] = inputCube
    searchDict['colors'] = {inputCube[D11], inputCube[F11], inputCube[L11]}
    
    # Find correct corner and corresponding rotation for that location
    if _findDownCorner(searchDict) == U00: rotations = 'uluuLUluL'
    elif _findDownCorner(searchDict) == U02: rotations = 'UUluuLUluL'
    elif _findDownCorner(searchDict) == U20: rotations = 'luuLUluL'
    elif _findDownCorner(searchDict) == U22: rotations = 'UluuLUluL'
    elif _findDownCorner(searchDict) == F00: rotations = 'ulUL'
    elif _findDownCorner(searchDict) == F02: rotations = 'UluL'
    elif _findDownCorner(searchDict) == F20: rotations = 'lULulUL'
    elif _findDownCorner(searchDict) == F22: rotations = 'RUrluuLUluL'
    elif _findDownCorner(searchDict) == R00: rotations = 'lUL'
    elif _findDownCorner(searchDict) == R02: rotations = 'uuluL'
    elif _findDownCorner(searchDict) == R20: rotations = 'RUrulUL'
    elif _findDownCorner(searchDict) == R22: rotations = 'ruRuluL'
    elif _findDownCorner(searchDict) == B00: rotations = 'UlUL'
    elif _findDownCorner(searchDict) == B02: rotations = 'uluL'
    elif _findDownCorner(searchDict) == B20: rotations = 'rURUlUL'
    elif _findDownCorner(searchDict) == B22: rotations = 'LululuL'
    elif _findDownCorner(searchDict) == L00: rotations = 'uulUL'
    elif _findDownCorner(searchDict) == L02: rotations = 'luL'
    elif _findDownCorner(searchDict) == L20: rotations = 'LUllUUL'
    elif _findDownCorner(searchDict) == L22: rotations = 'luLUluL'
    elif _findDownCorner(searchDict) == D02: rotations = 'RUrluL'
    elif _findDownCorner(searchDict) == D20: rotations = 'LulUlUUL'
    elif _findDownCorner(searchDict) == D22: rotations = 'rUURulUL'
    rotatedCube = _rotatePiece(rotations, inputCube)
    
    # Return the rotations to get solve D00 and the resulting cube
    output['rotations'] = rotations
    output['cube'] = rotatedCube
    return output

def _solveFrontRightDownCorner(parms):
    """ Finds the correct down corner piece for D02 and gets the rotations to put it in place """
    rotations = ''
    inputCube = parms.get('cube')
    output = {}
    searchDict = {}
    searchDict['cube'] = inputCube
    searchDict['colors'] = {inputCube[D11], inputCube[F11], inputCube[R11]}
    
    # Find correct corner and corresponding rotation for that location
    if _findDownCorner(searchDict) == U00: rotations = 'RUrURur'
    elif _findDownCorner(searchDict) == U02: rotations = 'uRUrURur'
    elif _findDownCorner(searchDict) == U20: rotations = 'uRUUruRUr'
    elif _findDownCorner(searchDict) == U22: rotations = 'RUUruRUr'
    elif _findDownCorner(searchDict) == F00: rotations = 'uRUr'
    elif _findDownCorner(searchDict) == F02: rotations = 'URur'
    elif _findDownCorner(searchDict) == F22: rotations = 'RurURur'
    elif _findDownCorner(searchDict) == R00: rotations = 'RUr'
    elif _findDownCorner(searchDict) == R02: rotations = 'UURur'
    elif _findDownCorner(searchDict) == R20: rotations = 'RUruRUr'
    elif _findDownCorner(searchDict) == R22: rotations = 'ruRRUUr'
    elif _findDownCorner(searchDict) == B00: rotations = 'URUr'
    elif _findDownCorner(searchDict) == B02: rotations = 'RUUr'
    elif _findDownCorner(searchDict) == B20: rotations = 'rURURUr'
    elif _findDownCorner(searchDict) == B22: rotations = 'LuluRur'
    elif _findDownCorner(searchDict) == L00: rotations = 'uuRUr'
    elif _findDownCorner(searchDict) == L02: rotations = 'Rur'
    elif _findDownCorner(searchDict) == L20: rotations = 'LUUlRUr'
    elif _findDownCorner(searchDict) == D20: rotations = 'LuulURur'
    elif _findDownCorner(searchDict) == D22: rotations = 'rURUURur'
    rotatedCube = _rotatePiece(rotations, inputCube)
    
    # Return the rotations to get solve D00 and the resulting cube
    output['rotations'] = rotations
    output['cube'] = rotatedCube
    return output

def _solveBackLeftDownCorner(parms):
    """ Finds the correct down corner piece for D20 and gets the rotations to put it in place """
    rotations = ''
    inputCube = parms.get('cube')
    output = {}
    searchDict = {}
    searchDict['cube'] = inputCube
    searchDict['colors'] = {inputCube[D11], inputCube[L11], inputCube[B11]}
        
    # Find correct corner and corresponding rotation for that location
    if _findDownCorner(searchDict) == U00: rotations = 'LulUULUl'  
    elif _findDownCorner(searchDict) == U02: rotations = 'uLulUULUl'   
    elif _findDownCorner(searchDict) == U20: rotations = 'uLUlULul'   
    elif _findDownCorner(searchDict) == U22: rotations = 'LUlULul'    
    elif _findDownCorner(searchDict) == F00: rotations = 'ULUl'    
    elif _findDownCorner(searchDict) == F02: rotations = 'uLul'      
    elif _findDownCorner(searchDict) == R00: rotations = 'UULUl'    
    elif _findDownCorner(searchDict) == R02: rotations = 'Lul'        
    elif _findDownCorner(searchDict) == R22: rotations = 'rLuRl'    
    elif _findDownCorner(searchDict) == B00: rotations = 'uLUl'     
    elif _findDownCorner(searchDict) == B02: rotations = 'ULul'     
    elif _findDownCorner(searchDict) == B20: rotations = 'rURuLUl'     
    elif _findDownCorner(searchDict) == B22: rotations = 'LulULul'     
    elif _findDownCorner(searchDict) == L00: rotations = 'LUl'     
    elif _findDownCorner(searchDict) == L02: rotations = 'UULul'     
    elif _findDownCorner(searchDict) == L20: rotations = 'LUluLUl'      
    elif _findDownCorner(searchDict) == D22: rotations = 'ruRLUl'  
    rotatedCube = _rotatePiece(rotations, inputCube)    
    
    # Return the rotations to get solve D00 and the resulting cube
    output['rotations'] = rotations
    output['cube'] = rotatedCube
    return output

def _solveBackRightDownCorner(parms):
    """ Finds the correct down corner piece for D22 and gets the rotations to put it in place """
    rotations = ''
    inputCube = parms.get('cube')
    output = {}
    searchDict = {}
    searchDict['cube'] = inputCube
    searchDict['colors'] = {inputCube[D11], inputCube[R11], inputCube[B11]}
        
    # Find correct corner and corresponding rotation for that location
    if _findDownCorner(searchDict) == U00: rotations = 'UrURUUruR'      
    elif _findDownCorner(searchDict) == U02: rotations = 'ruuRUruR'  
    elif _findDownCorner(searchDict) == U20: rotations = 'UUruuRUruR'         
    elif _findDownCorner(searchDict) == U22: rotations = 'uruuRUruR'     
    elif _findDownCorner(searchDict) == F00: rotations = 'ruuR'     
    elif _findDownCorner(searchDict) == F02: rotations = 'uruR'      
    elif _findDownCorner(searchDict) == R00: rotations = 'UruuR'      
    elif _findDownCorner(searchDict) == R02: rotations = 'ruR'      
    elif _findDownCorner(searchDict) == R22: rotations = 'ruRUruR'     
    elif _findDownCorner(searchDict) == B00: rotations = 'urUR'    
    elif _findDownCorner(searchDict) == B02: rotations = 'UruR'    
    elif _findDownCorner(searchDict) == B20: rotations = 'rURurUR'     
    elif _findDownCorner(searchDict) == L00: rotations = 'rUR'     
    elif _findDownCorner(searchDict) == L02: rotations = 'uuruR'     
    rotatedCube = _rotatePiece(rotations, inputCube)    
    
    # Return the rotations to get solve D00 and the resulting cube
    output['rotations'] = rotations
    output['cube'] = rotatedCube
    return output
    
def _findDownCorner(parms):
    """ Method that finds a down corner of the cube and returns the location of the down face color of the corner """
    searchCube = parms.get('cube')
    searchColors = parms.get('colors')
    location = None
    
    # Set of all the corners of the cube
    corners = {frozenset([F00, L02, U20]), frozenset([F02, R00, U22]), frozenset([F20, L22, D00]), frozenset([F22, R20, D02]), 
               frozenset([R02, B00, U02]), frozenset([B02, L00, U00]), frozenset([R22, B20, D22]), frozenset([B22, L20, D20])}
    
    # Go through the set of corners and find one with the colors being searched for
    for corner in corners: 
        currentColors = set()
        for face in corner:
            currentColors.add(searchCube[face])
            if searchCube[face] == searchCube[D11]:
                location = face
        if searchColors == currentColors: 
            # Return the location of the down colored piece of the corner
            return location
                  
def _rotatePiece(rotations, cubeValue):
    """ Calls the rotate function and returns the rotated cube """
    rotateParms = {}
    rotateParms['dir'] = rotations
    rotateParms['cube'] = cubeValue
    rotatedCube = rotate._rotate(rotateParms)
    cubeValue = rotatedCube.get('cube')
    return cubeValue