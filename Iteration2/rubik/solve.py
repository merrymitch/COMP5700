import rubik.cube as rubik
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
    """Return rotates needed to solve input cube"""
    result = {}
    
    # Call verify to determine if the passed cube is a valid rubik's cube
    isCubeValid = verify._verify(parms)
    if (isCubeValid['status'] != 'ok'):
        result['status'] = 'error: invalid cube'
        return result
    
    encodedCube = parms.get('cube')
    
    # Check if down face cross is already solved
    downCrossChars = {encodedCube[D01], encodedCube[D10], encodedCube[D11], encodedCube[D12], encodedCube[D21]}
    if len(downCrossChars) == 1:
        result['rotations'] = ''
        result['status'] = 'ok'                     
        return result
    
    # Initialize variables for the solve functions
    solveCube = {}
    solveCube['cube'] = parms.get('cube')
    rotations = ''
    
    # Call function to solve the daisy and get the rotations
    daisyCube = _solveDaisy(solveCube)
    solveCube['cube'] = daisyCube.get('cube')
    rotations += daisyCube.get('rotations')
    
    # Call function to solve the down cross and get the rotations
    downCrossCube = _solveDownCross(solveCube)
    solveCube['cube'] = downCrossCube.get('cube')
    rotations += downCrossCube.get('rotations')
    
    # Put the solution in the result and return it
    result['rotations'] = rotations
    result['status'] = 'ok' 
                    
    return result

def _solveDaisy(parms):
    """ Determines which of the daisy pieces need solving and calls function to solve them """
    result = {}
    solveCube = {}
    solveCube['cube'] = parms.get('cube')
    rotations = ''
     
    # If the daisy piece is not in correct place call the corresponding function to solve it
    if solveCube.get('cube')[U21] != solveCube.get('cube')[D11]:
        solveCube = _U21Daisy(solveCube)
        rotations += solveCube.get('rotations')
    if solveCube.get('cube')[U12] != solveCube.get('cube')[D11]:
        solveCube = _U12Daisy(solveCube)
        rotations += solveCube.get('rotations')
    if solveCube.get('cube')[U10] != solveCube.get('cube')[D11]:
        solveCube = _U10Daisy(solveCube)
        rotations += solveCube.get('rotations')
    if solveCube.get('cube')[U01] != solveCube.get('cube')[D11]:
        solveCube = _U01Daisy(solveCube)
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
    solveCube = _U21Down(solveCube)
    rotations += solveCube.get('rotations')
    solveCube = _U12Down(solveCube)
    rotations += solveCube.get('rotations')
    solveCube = _U10Down(solveCube)
    rotations += solveCube.get('rotations')
    solveCube = _U01Down(solveCube)
    rotations += solveCube.get('rotations')
    
    # Return the rotations to solve the down cross
    result['rotations'] = rotations
    result['cube'] = solveCube.get('cube')
    return result

def _U21Daisy(parms):
    """ Finds a down colored piece to put in U21 daisy spot """
    rotations = ''
    cubeValue = parms.get('cube')
    rotatedCube = ''
    output = {}
        
    # Find a down colored piece and put it in correct place in daisy
    if cubeValue[F01] == cubeValue[D11]:
        rotations = 'FuRU'
        rotatedCube = _rotateDaisyPiece(rotations, cubeValue)
    elif cubeValue[F10] == cubeValue[D11]:
        rotations = 'Ulu'
        rotatedCube = _rotateDaisyPiece(rotations, cubeValue) 
    elif cubeValue[F12] == cubeValue[D11]:
        rotations = 'uRU'
        rotatedCube = _rotateDaisyPiece(rotations, cubeValue)
    elif cubeValue[F21] == cubeValue[D11]:
        rotations = 'fuRU'
        rotatedCube = _rotateDaisyPiece(rotations, cubeValue)
    elif cubeValue[R01] == cubeValue[D11]:
        rotations = 'rf'
        rotatedCube = _rotateDaisyPiece(rotations, cubeValue)
    elif cubeValue[R10] == cubeValue[D11]:
        rotations = 'f'
        rotatedCube = _rotateDaisyPiece(rotations, cubeValue)
    elif cubeValue[R12] == cubeValue[D11]:
        rotations = 'uuBUU'
        rotatedCube = _rotateDaisyPiece(rotations, cubeValue)
    elif cubeValue[R21] == cubeValue[D11]:
        rotations = 'uruBUU'
        rotatedCube = _rotateDaisyPiece(rotations, cubeValue)
    elif cubeValue[B01] == cubeValue[D11]:
        rotations = 'burU'
        rotatedCube = _rotateDaisyPiece(rotations, cubeValue)
    elif cubeValue[B10] == cubeValue[D11]:
        rotations = 'urU'
        rotatedCube = _rotateDaisyPiece(rotations, cubeValue)
    elif cubeValue[B12] == cubeValue[D11]:
        rotations = 'ULu'
        rotatedCube = _rotateDaisyPiece(rotations, cubeValue)
    elif cubeValue[B21] == cubeValue[D11]:
        rotations = 'uubuLu'
        rotatedCube = _rotateDaisyPiece(rotations, cubeValue)
    elif cubeValue[L01] == cubeValue[D11]:
        rotations = 'LF'
        rotatedCube = _rotateDaisyPiece(rotations, cubeValue)
    elif cubeValue[L10] == cubeValue[D11]:
        rotations = 'UUbuu'
        rotatedCube = _rotateDaisyPiece(rotations, cubeValue)
    elif cubeValue[L12] == cubeValue[D11]:
        rotations = 'F'
        rotatedCube = _rotateDaisyPiece(rotations, cubeValue)
    elif cubeValue[L21] == cubeValue[D11]:
        rotations = 'UluF'
        rotatedCube = _rotateDaisyPiece(rotations, cubeValue)
    elif cubeValue[D01] == cubeValue[D11]:
        rotations = 'FF'
        rotatedCube = _rotateDaisyPiece(rotations, cubeValue)
    elif cubeValue[D10] == cubeValue[D11]:
        rotations = 'DFF'
        rotatedCube = _rotateDaisyPiece(rotations, cubeValue)
    elif cubeValue[D12] == cubeValue[D11]:
        rotations = 'dFF'
        rotatedCube = _rotateDaisyPiece(rotations, cubeValue)
    elif cubeValue[D21] == cubeValue[D11]:
        rotations = 'ddFF'
        rotatedCube = _rotateDaisyPiece(rotations, cubeValue)
        
    # Return the rotations to get correct U21 Daisy piece and the cube after rotations
    output['rotations'] = rotations
    output['cube'] = rotatedCube
    return output

def _U12Daisy(parms):
    """ Finds a down colored piece to put in U12 daisy spot """
    rotations = ''
    cubeValue = parms.get('cube')
    rotatedCube = ''
    output = {}
    
    # Find a down colored piece and put it in correct place in daisy
    if cubeValue[R01] == cubeValue[D11]:
        rotations = 'rUfu'
        rotatedCube = _rotateDaisyPiece(rotations, cubeValue)
    elif cubeValue[R10] == cubeValue[D11]:
        rotations = 'Ufu'
        rotatedCube = _rotateDaisyPiece(rotations, cubeValue)
    elif cubeValue[R12] == cubeValue[D11]:
        rotations = 'uBU'
        rotatedCube = _rotateDaisyPiece(rotations, cubeValue)
    elif cubeValue[R21] == cubeValue[D11]:
        rotations = 'ruBU'
        rotatedCube = _rotateDaisyPiece(rotations, cubeValue)
    elif cubeValue[B01] == cubeValue[D11]:
        rotations = 'br'
        rotatedCube = _rotateDaisyPiece(rotations, cubeValue)    
    elif cubeValue[B10] == cubeValue[D11]:
        rotations = 'r'
        rotatedCube = _rotateDaisyPiece(rotations, cubeValue) 
    elif cubeValue[B12] == cubeValue[D11]:
        rotations = 'uuLuu'
        rotatedCube = _rotateDaisyPiece(rotations, cubeValue)    
    elif cubeValue[B21] == cubeValue[D11]:
        rotations = 'druBU'
        rotatedCube = _rotateDaisyPiece(rotations, cubeValue)  
    elif cubeValue[L01] == cubeValue[D11]:
        rotations = 'LUFu'
        rotatedCube = _rotateDaisyPiece(rotations, cubeValue)  
    elif cubeValue[L10] == cubeValue[D11]:
        rotations = 'ubU'
        rotatedCube = _rotateDaisyPiece(rotations, cubeValue)  
    elif cubeValue[L12] == cubeValue[D11]:
        rotations = 'UFu'
        rotatedCube = _rotateDaisyPiece(rotations, cubeValue)
    elif cubeValue[L21] == cubeValue[D11]:
        rotations = 'UULUbU'
        rotatedCube = _rotateDaisyPiece(rotations, cubeValue)
    elif cubeValue[F01] == cubeValue[D11]:
        rotations = 'FR'
        rotatedCube = _rotateDaisyPiece(rotations, cubeValue)
    elif cubeValue[F10] == cubeValue[D11]:
        rotations = 'uuluu'
        rotatedCube = _rotateDaisyPiece(rotations, cubeValue)
    elif cubeValue[F12] == cubeValue[D11]:
        rotations = 'R'
        rotatedCube = _rotateDaisyPiece(rotations, cubeValue)
    elif cubeValue[F21] == cubeValue[D11]:
        rotations = 'UfuR'
        rotatedCube = _rotateDaisyPiece(rotations, cubeValue)
    elif cubeValue[D01] == cubeValue[D11]:
        rotations = 'DRR'
        rotatedCube = _rotateDaisyPiece(rotations, cubeValue)
    elif cubeValue[D10] == cubeValue[D11]:
        rotations = 'DDRR'
        rotatedCube = _rotateDaisyPiece(rotations, cubeValue)
    elif cubeValue[D12] == cubeValue[D11]:
        rotations = 'RR'
        rotatedCube = _rotateDaisyPiece(rotations, cubeValue)
    elif cubeValue[D21] == cubeValue[D11]:
        rotations = 'dRR'
        rotatedCube = _rotateDaisyPiece(rotations, cubeValue)
    
    # Return the rotations to get correct U12 Daisy piece and the cube after rotations
    output['rotations'] = rotations
    output['cube'] = rotatedCube
    return output

def _U10Daisy(parms):
    """ Finds a down colored piece to put in U10 daisy spot """
    rotations = ''
    cubeValue = parms.get('cube')
    rotatedCube = ''
    output = {}
    
    # Find a down colored piece and put it in correct place in daisy
    if cubeValue[L01] == cubeValue[D11]:
        rotations = 'LuFU'
        rotatedCube = _rotateDaisyPiece(rotations, cubeValue)
    elif cubeValue[L10] == cubeValue[D11]:
        rotations = 'Ubu'
        rotatedCube = _rotateDaisyPiece(rotations, cubeValue)
    elif cubeValue[L12] == cubeValue[D11]:
        rotations = 'uFU'
        rotatedCube = _rotateDaisyPiece(rotations, cubeValue)
    elif cubeValue[L21] == cubeValue[D11]:
        rotations = 'LUbu'
        rotatedCube = _rotateDaisyPiece(rotations, cubeValue)
    elif cubeValue[F01] == cubeValue[D11]:
        rotations = 'fl'
        rotatedCube = _rotateDaisyPiece(rotations, cubeValue)
    elif cubeValue[F10] == cubeValue[D11]:
        rotations = 'l'
        rotatedCube = _rotateDaisyPiece(rotations, cubeValue)
    elif cubeValue[F12] == cubeValue[D11]:
        rotations = 'uuRuu'
        rotatedCube = _rotateDaisyPiece(rotations, cubeValue)
    elif cubeValue[F21] == cubeValue[D11]:
        rotations = 'uFUl'
        rotatedCube = _rotateDaisyPiece(rotations, cubeValue)
    elif cubeValue[R01] == cubeValue[D11]:
        rotations = 'rufU'
        rotatedCube = _rotateDaisyPiece(rotations, cubeValue)
    elif cubeValue[R10] == cubeValue[D11]:
        rotations = 'ufU'
        rotatedCube = _rotateDaisyPiece(rotations, cubeValue)
    elif cubeValue[R12] == cubeValue[D11]:
        rotations = 'UBu'
        rotatedCube = _rotateDaisyPiece(rotations, cubeValue)
    elif cubeValue[R21] == cubeValue[D11]:
        rotations = 'uuruBu'
        rotatedCube = _rotateDaisyPiece(rotations, cubeValue)
    elif cubeValue[B01] == cubeValue[D11]:
        rotations = 'BL'
        rotatedCube = _rotateDaisyPiece(rotations, cubeValue)
    elif cubeValue[B10] == cubeValue[D11]:
        rotations = 'UUrUU'
        rotatedCube = _rotateDaisyPiece(rotations, cubeValue)
    elif cubeValue[B12] == cubeValue[D11]:
        rotations = 'L'
        rotatedCube = _rotateDaisyPiece(rotations, cubeValue)
    elif cubeValue[B21] == cubeValue[D11]:
        rotations = 'UBUrUU'
        rotatedCube = _rotateDaisyPiece(rotations, cubeValue)
    elif cubeValue[D01] == cubeValue[D11]:
        rotations = 'dll'
        rotatedCube = _rotateDaisyPiece(rotations, cubeValue)
    elif cubeValue[D10] == cubeValue[D11]:
        rotations = 'll'
        rotatedCube = _rotateDaisyPiece(rotations, cubeValue)
    elif cubeValue[D12] == cubeValue[D11]:
        rotations = 'ddll'
        rotatedCube = _rotateDaisyPiece(rotations, cubeValue)
    elif cubeValue[D21] == cubeValue[D11]:
        rotations = 'Dll'
        rotatedCube = _rotateDaisyPiece(rotations, cubeValue)
        
    # Return the rotations to get correct U10 Daisy piece and the cube after rotations
    output['rotations'] = rotations
    output['cube'] = rotatedCube
    return output

def _U01Daisy(parms):
    """ Finds a down colored piece to put in U01 daisy spot """
    rotations = ''
    cubeValue = parms.get('cube')
    rotatedCube = ''
    output = {}
    
    # Find a down colored piece and put it in correct place in daisy
    if cubeValue[B01] == cubeValue[D11]:
        rotations = 'bUru'
        rotatedCube = _rotateDaisyPiece(rotations, cubeValue)
    elif cubeValue[B10] == cubeValue[D11]:
        rotations = 'Uru'
        rotatedCube = _rotateDaisyPiece(rotations, cubeValue)
    elif cubeValue[B12] == cubeValue[D11]:
        rotations = 'uLU'
        rotatedCube = _rotateDaisyPiece(rotations, cubeValue)
    elif cubeValue[B21] == cubeValue[D11]:
        rotations = 'BUru'
        rotatedCube = _rotateDaisyPiece(rotations, cubeValue)
    elif cubeValue[L01] == cubeValue[D11]:
        rotations = 'lb'
        rotatedCube = _rotateDaisyPiece(rotations, cubeValue)
    elif cubeValue[L10] == cubeValue[D11]:
        rotations = 'b'
        rotatedCube = _rotateDaisyPiece(rotations, cubeValue)
    elif cubeValue[L12] == cubeValue[D11]:
        rotations = 'uuFuu'
        rotatedCube = _rotateDaisyPiece(rotations, cubeValue)
    elif cubeValue[L21] == cubeValue[D11]:
        rotations = 'uLUb'
        rotatedCube = _rotateDaisyPiece(rotations, cubeValue)
    elif cubeValue[F01] == cubeValue[D11]:
        rotations = 'fulU'
        rotatedCube = _rotateDaisyPiece(rotations, cubeValue)
    elif cubeValue[F10] == cubeValue[D11]:
        rotations = 'ulU'
        rotatedCube = _rotateDaisyPiece(rotations, cubeValue)
    elif cubeValue[F12] == cubeValue[D11]:
        rotations = 'URu'
        rotatedCube = _rotateDaisyPiece(rotations, cubeValue)
    elif cubeValue[F21] == cubeValue[D11]:
        rotations = 'UUfuRu'
        rotatedCube = _rotateDaisyPiece(rotations, cubeValue)
    elif cubeValue[R01] == cubeValue[D11]:
        rotations = 'RB'
        rotatedCube = _rotateDaisyPiece(rotations, cubeValue)
    elif cubeValue[R10] == cubeValue[D11]:
        rotations = 'UUfUU'
        rotatedCube = _rotateDaisyPiece(rotations, cubeValue)
    elif cubeValue[R12] == cubeValue[D11]:
        rotations = 'B'
        rotatedCube = _rotateDaisyPiece(rotations, cubeValue)
    elif cubeValue[R21] == cubeValue[D11]:
        rotations = 'UruB'
        rotatedCube = _rotateDaisyPiece(rotations, cubeValue)
    elif cubeValue[D01] == cubeValue[D11]:
        rotations = 'DDBB'
        rotatedCube = _rotateDaisyPiece(rotations, cubeValue)
    elif cubeValue[D10] == cubeValue[D11]:
        rotations = 'dBB'
        rotatedCube = _rotateDaisyPiece(rotations, cubeValue)
    elif cubeValue[D12] == cubeValue[D11]:
        rotations = 'DBB'
        rotatedCube = _rotateDaisyPiece(rotations, cubeValue)
    elif cubeValue[D21] == cubeValue[D11]:
        rotations = 'BB'
        rotatedCube = _rotateDaisyPiece(rotations, cubeValue)
        
    # Return the rotations to get correct U01 Daisy piece and the cube after rotations
    output['rotations'] = rotations
    output['cube'] = rotatedCube
    return output

def _U21Down(parms):
    """ Finds the correct down cross space and rotations for U21 daisy piece """
    rotations = ''
    inputCube = parms.get('cube')
    rotatedCube = ''
    output = {}
    
    # Find correct down cross space and rotations
    if inputCube[F01] == inputCube[F11]:
        rotations = 'FF'
        rotatedCube = _rotateDaisyPiece(rotations, inputCube)
    elif inputCube[F01] == inputCube[L11]:
        rotations = 'ULLu'
        rotatedCube = _rotateDaisyPiece(rotations, inputCube)
    elif inputCube[F01] == inputCube[R11]:
        rotations = 'urrU'
        rotatedCube = _rotateDaisyPiece(rotations, inputCube)
    elif inputCube[F01] == inputCube[B11]:
        rotations = 'UUbbUU'
        rotatedCube = _rotateDaisyPiece(rotations, inputCube)
        
    # Return the rotations to put U21 in correct down cross place and the rotated cube
    output['rotations'] = rotations
    output['cube'] = rotatedCube
    return output

def _U12Down(parms):
    """ Finds the correct down cross space and rotations for U12 daisy piece """
    rotations = ''
    inputCube = parms.get('cube')
    rotatedCube = ''
    output = {}
    
    # Find correct down cross space and rotations
    if inputCube[R01] == inputCube[F11]:
        rotations = 'UFFu'
        rotatedCube = _rotateDaisyPiece(rotations, inputCube)
    elif inputCube[R01] == inputCube[L11]:
        rotations = 'UULLUU'
        rotatedCube = _rotateDaisyPiece(rotations, inputCube)
    elif inputCube[R01] == inputCube[R11]:
        rotations = 'RR'
        rotatedCube = _rotateDaisyPiece(rotations, inputCube)
    elif inputCube[R01] == inputCube[B11]:
        rotations = 'uBBU'
        rotatedCube = _rotateDaisyPiece(rotations, inputCube)
     
    # Return the rotations to put U12 in correct down cross place and the rotated cube   
    output['rotations'] = rotations
    output['cube'] = rotatedCube
    return output

def _U10Down(parms):
    """ Finds the correct down cross space and rotations for U10 daisy piece """
    rotations = ''
    inputCube = parms.get('cube')
    rotatedCube = ''
    output = {}
    
    # Find correct down cross space and rotations
    if inputCube[L01] == inputCube[F11]:
        rotations = 'uFFU'
        rotatedCube = _rotateDaisyPiece(rotations, inputCube)
    elif inputCube[L01] == inputCube[L11]:
        rotations = 'LL'
        rotatedCube = _rotateDaisyPiece(rotations, inputCube)
    elif inputCube[L01] == inputCube[R11]:
        rotations = 'UURRUU'
        rotatedCube = _rotateDaisyPiece(rotations, inputCube)
    elif inputCube[L01] == inputCube[B11]:
        rotations = 'UBBu'
        rotatedCube = _rotateDaisyPiece(rotations, inputCube)
     
    # Return the rotations to put U10 in correct down cross place and the rotated cube   
    output['rotations'] = rotations
    output['cube'] = rotatedCube
    return output

def _U01Down(parms):
    """ Finds the correct down cross space and rotations for U01 daisy piece """
    rotations = ''
    inputCube = parms.get('cube')
    rotatedCube = ''
    output = {}
    
    # Find correct down cross space and rotations
    if inputCube[B01] == inputCube[F11]:
        rotations = 'UUFFUU'
        rotatedCube = _rotateDaisyPiece(rotations, inputCube)
    elif inputCube[B01] == inputCube[L11]:
        rotations = 'uLLU'
        rotatedCube = _rotateDaisyPiece(rotations, inputCube)
    elif inputCube[B01] == inputCube[R11]:
        rotations = 'URRu'
        rotatedCube = _rotateDaisyPiece(rotations, inputCube)
    elif inputCube[B01] == inputCube[B11]:
        rotations = 'BB'
        rotatedCube = _rotateDaisyPiece(rotations, inputCube)
    
    # Return the rotations to put U01 in correct down cross place and the rotated cube    
    output['rotations'] = rotations
    output['cube'] = rotatedCube
    return output


def _rotateDaisyPiece(rotations, cubeValue):
    """ Calls the rotate function and returns the rotated cube """
    rotateParms = {}
    rotateParms['dir'] = rotations
    rotateParms['cube'] = cubeValue
    rotatedCube = rotate._rotate(rotateParms)
    cubeValue = rotatedCube.get('cube')
    return cubeValue