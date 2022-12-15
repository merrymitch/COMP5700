import rubik.verify as verify

#Assign the cube mapping to each of the cube faces
F00, F01, F02, F10, F11, F12, F20, F21, F22 = 0, 1, 2, 3, 4, 5, 6, 7, 8
R00, R01, R02, R10, R11, R12, R20, R21, R22 = 9, 10, 11, 12, 13, 14, 15, 16, 17
B00, B01, B02, B10, B11, B12, B20, B21, B22 = 18, 19, 20, 21, 22, 23, 24, 25, 26
L00, L01, L02, L10, L11, L12, L20, L21, L22 = 27, 28, 29, 30, 31, 32, 33, 34, 35
U00, U01, U02, U10, U11, U12, U20, U21, U22 = 36, 37, 38, 39, 40, 41, 42, 43, 44
D00, D01, D02, D10, D11, D12, D20, D21, D22 = 45, 46, 47, 48, 49, 50, 51, 52, 53

def _rotate(parms):
    """Return rotated cube""" 
    result = {}
    
    # Call isDirValid to determine if the rotations are valid 
    if _isDirValid(parms):
        encodedDir = parms.get('dir', None)
        if encodedDir == None or encodedDir.strip() == "":
            encodedDir = 'F'     
    else: 
        result['status'] = 'error: invalid rotation'
        return result 
    
    # Call verify to determine if the passed cube is a valid rubik's cube
    isCubeValid = verify._verify(parms)
    if (isCubeValid['status'] == 'ok'):
        encodedCube = parms.get('cube')
    else: 
        result['status'] = 'error: invalid cube'
        return result   
    
    # If everything is valid, then call rotateCube to perform the operations       
    result['cube'] = _rotateCube(encodedDir, encodedCube).get('cube')             
    result['status'] = 'ok'                     
    return result

def _isDirValid(direction = None):
    """ Check if dir is valid """
    # Check that parameter is present (if not we will assume direction is going to be 'F')
    if direction == None:
        return True
    # Check for no dir values and if there are none then return true (we will assume direction is going to be 'F')
    if (not 'dir' in direction) or (direction['dir'] == None) or (direction['dir'].strip() == ""):
        return True
    
    directionValue = direction.get('dir')
    allowedDir = 'FfRrBbLlUuDd'
    
    # Check that only FfRrBbLlUuDd are present
    if all(ch in allowedDir for ch in directionValue):
        return True
    return False
    
def _rotateCube(direction, cube):
    """ Rotate the cube based on dir """
    rotatedCube = cube
    output = {}
    
    # Iterate through all the directions and call the appropriate rotation for that value
    for ch in direction:
        if ch == 'F':
            rotatedCube = _rotateFrontClockwise(rotatedCube).get('cube')
        elif ch == 'f':
            rotatedCube = _rotateFrontCounterClockwise(rotatedCube).get('cube')
        elif ch == 'R':
            rotatedCube = _rotateRightClockwise(rotatedCube).get('cube')
        elif ch == 'r':
            rotatedCube = _rotateRightCounterClockwise(rotatedCube).get('cube')
        elif ch == 'B':
            rotatedCube = _rotateBackClockwise(rotatedCube).get('cube')
        elif ch == 'b':
            rotatedCube = _rotateBackCounterClockwise(rotatedCube).get('cube')
        elif ch == 'L':
            rotatedCube = _rotateLeftClockwise(rotatedCube).get('cube')
        elif ch == 'l':
            rotatedCube = _rotateLeftCounterClockwise(rotatedCube).get('cube')
        elif ch == 'U':
            rotatedCube = _rotateUpClockwise(rotatedCube).get('cube')
        elif ch == 'u':
            rotatedCube = _rotateUpCounterClockwise(rotatedCube).get('cube')
        elif ch == 'D':
            rotatedCube = _rotateDownClockwise(rotatedCube).get('cube')
        else:
            rotatedCube = _rotateDownCounterClockwise(rotatedCube).get('cube')
    output['cube'] = rotatedCube
    return output
    
def _rotateFrontClockwise(cube):
    """ Rotate front clockwise """
    cubeList = list(cube)
    rotatedCube = cubeList[:]
    # Rotate front face
    rotatedCube[F00] = cube[F20]
    rotatedCube[F01] = cube[F10]
    rotatedCube[F02] = cube[F00]
    rotatedCube[F10] = cube[F21]
    rotatedCube[F11] = cube[F11]
    rotatedCube[F12] = cube[F01]
    rotatedCube[F20] = cube[F22]
    rotatedCube[F21] = cube[F12]
    rotatedCube[F22] = cube[F02]
    # Rotate right portion
    rotatedCube[R00] = cube[U20]
    rotatedCube[R10] = cube[U21]
    rotatedCube[R20] = cube[U22]
    # Rotate left portion
    rotatedCube[L02] = cube[D00]
    rotatedCube[L12] = cube[D01]
    rotatedCube[L22] = cube[D02]
    # Rotate top portion
    rotatedCube[U20] = cube[L22]
    rotatedCube[U21] = cube[L12]
    rotatedCube[U22] = cube[L02]
    # Rotate bottom portion
    rotatedCube[D00] = cube[R20]
    rotatedCube[D01] = cube[R10]
    rotatedCube[D02] = cube[R00]
    rotatedString = "".join(rotatedCube)
    output = {}
    output['cube'] = rotatedString
    return output
    
def _rotateFrontCounterClockwise(cube):
    """ Rotate front counterclockwise """
    cubeList = list(cube)
    rotatedCube = cubeList[:]
    # Rotate front face
    rotatedCube[F00] = cube[F02]
    rotatedCube[F01] = cube[F12]
    rotatedCube[F02] = cube[F22]
    rotatedCube[F10] = cube[F01]
    rotatedCube[F11] = cube[F11]
    rotatedCube[F12] = cube[F21]
    rotatedCube[F20] = cube[F00]
    rotatedCube[F21] = cube[F10]
    rotatedCube[F22] = cube[F20]
    # Rotate right portion
    rotatedCube[R00] = cube[D02]
    rotatedCube[R10] = cube[D01]
    rotatedCube[R20] = cube[D00]
    # Rotate left portion
    rotatedCube[L02] = cube[U22]
    rotatedCube[L12] = cube[U21]
    rotatedCube[L22] = cube[U20]
    # Rotate top portion
    rotatedCube[U20] = cube[R00]
    rotatedCube[U21] = cube[R10]
    rotatedCube[U22] = cube[R20]
    # Rotate bottom portion
    rotatedCube[D00] = cube[L02]
    rotatedCube[D01] = cube[L12]
    rotatedCube[D02] = cube[L22]
    rotatedString = "".join(rotatedCube)
    output = {}
    output['cube'] = rotatedString
    return output

def _rotateRightClockwise(cube):
    """ Rotate right clockwise """
    cubeList = list(cube)
    rotatedCube = cubeList[:]
    # Rotate front portion
    rotatedCube[F02] = cube[D02]
    rotatedCube[F12] = cube[D12]
    rotatedCube[F22] = cube[D22]
    # Rotate right face
    rotatedCube[R00] = cube[R20]
    rotatedCube[R01] = cube[R10]
    rotatedCube[R02] = cube[R00]
    rotatedCube[R10] = cube[R21]
    rotatedCube[R11] = cube[R11]
    rotatedCube[R12] = cube[R01]
    rotatedCube[R20] = cube[R22]
    rotatedCube[R21] = cube[R12]
    rotatedCube[R22] = cube[R02]
    # Rotate back portion
    rotatedCube[B00] = cube[U22]
    rotatedCube[B10] = cube[U12]
    rotatedCube[B20] = cube[U02]
    # Rotate top portion
    rotatedCube[U02] = cube[F02]
    rotatedCube[U12] = cube[F12]
    rotatedCube[U22] = cube[F22]
    # Rotate bottom portion
    rotatedCube[D02] = cube[B20]
    rotatedCube[D12] = cube[B10]
    rotatedCube[D22] = cube[B00]
    rotatedString = "".join(rotatedCube)
    output = {}
    output['cube'] = rotatedString
    return output
    
def _rotateRightCounterClockwise(cube):
    """ Rotate right counterclockwise """
    cubeList = list(cube)
    rotatedCube = cubeList[:]
    # Rotate front portion
    rotatedCube[F02] = cube[U02]
    rotatedCube[F12] = cube[U12]
    rotatedCube[F22] = cube[U22]
    # Rotate right face
    rotatedCube[R00] = cube[R02]
    rotatedCube[R01] = cube[R12]
    rotatedCube[R02] = cube[R22]
    rotatedCube[R10] = cube[R01]
    rotatedCube[R11] = cube[R11]
    rotatedCube[R12] = cube[R21]
    rotatedCube[R20] = cube[R00]
    rotatedCube[R21] = cube[R10]
    rotatedCube[R22] = cube[R20]
    # Rotate back portion
    rotatedCube[B00] = cube[D22]
    rotatedCube[B10] = cube[D12]
    rotatedCube[B20] = cube[D02]
    # Rotate top portion
    rotatedCube[U02] = cube[B20]
    rotatedCube[U12] = cube[B10]
    rotatedCube[U22] = cube[B00]
    # Rotate bottom portion
    rotatedCube[D02] = cube[F02]
    rotatedCube[D12] = cube[F12]
    rotatedCube[D22] = cube[F22]
    rotatedString = "".join(rotatedCube)
    output = {}
    output['cube'] = rotatedString
    return output

def _rotateBackClockwise(cube):
    """ Rotate back clockwise """
    cubeList = list(cube)
    rotatedCube = cubeList[:]
    # Rotate right portion
    rotatedCube[R02] = cube[D22]
    rotatedCube[R12] = cube[D21]
    rotatedCube[R22] = cube[D20]
    # Rotate back face
    rotatedCube[B00] = cube[B20]
    rotatedCube[B01] = cube[B10]
    rotatedCube[B02] = cube[B00]
    rotatedCube[B10] = cube[B21]
    rotatedCube[B11] = cube[B11]
    rotatedCube[B12] = cube[B01]
    rotatedCube[B20] = cube[B22]
    rotatedCube[B21] = cube[B12]
    rotatedCube[B22] = cube[B02]
    # Rotate left portion
    rotatedCube[L00] = cube[U02]
    rotatedCube[L10] = cube[U01]
    rotatedCube[L20] = cube[U00]
    # Rotate top portion
    rotatedCube[U00] = cube[R02]
    rotatedCube[U01] = cube[R12]
    rotatedCube[U02] = cube[R22]
    # Rotate bottom portion
    rotatedCube[D20] = cube[L00]
    rotatedCube[D21] = cube[L10]
    rotatedCube[D22] = cube[L20]
    rotatedString = "".join(rotatedCube)
    output = {}
    output['cube'] = rotatedString
    return output

def _rotateBackCounterClockwise(cube):
    """ Rotate back counterclockwise """
    cubeList = list(cube)
    rotatedCube = cubeList[:]
    # Rotate right portion 
    rotatedCube[R02] = cube[U00]
    rotatedCube[R12] = cube[U01]
    rotatedCube[R22] = cube[U02]
    # Rotate back face
    rotatedCube[B00] = cube[B02]
    rotatedCube[B01] = cube[B12]
    rotatedCube[B02] = cube[B22]
    rotatedCube[B10] = cube[B01]
    rotatedCube[B11] = cube[B11]
    rotatedCube[B12] = cube[B21]
    rotatedCube[B20] = cube[B00]
    rotatedCube[B21] = cube[B10]
    rotatedCube[B22] = cube[B20]
    # Rotate left portion
    rotatedCube[L00] = cube[D20]
    rotatedCube[L10] = cube[D21]
    rotatedCube[L20] = cube[D22]
    # Rotate top portion
    rotatedCube[U00] = cube[L20]
    rotatedCube[U01] = cube[L10]
    rotatedCube[U02] = cube[L00]
    # Rotate bottom portion
    rotatedCube[D20] = cube[R22]
    rotatedCube[D21] = cube[R12]
    rotatedCube[D22] = cube[R02]
    rotatedString = "".join(rotatedCube)
    output = {}
    output['cube'] = rotatedString
    return output

def _rotateLeftClockwise(cube):
    """ Rotate left clockwise """
    cubeList = list(cube)
    rotatedCube = cubeList[:]
    # Rotate front portion
    rotatedCube[F00] = cube[U00]
    rotatedCube[F10] = cube[U10]
    rotatedCube[F20] = cube[U20]
    # Rotate back portion
    rotatedCube[B02] = cube[D20]
    rotatedCube[B12] = cube[D10]
    rotatedCube[B22] = cube[D00]
    # Rotate left face
    rotatedCube[L00] = cube[L20]
    rotatedCube[L01] = cube[L10]
    rotatedCube[L02] = cube[L00]
    rotatedCube[L10] = cube[L21]
    rotatedCube[L11] = cube[L11]
    rotatedCube[L12] = cube[L01]
    rotatedCube[L20] = cube[L22]
    rotatedCube[L21] = cube[L12]
    rotatedCube[L22] = cube[L02]
    # Rotate top portion
    rotatedCube[U00] = cube[B22]
    rotatedCube[U10] = cube[B12]
    rotatedCube[U20] = cube[B02]
    # Rotate bottom portion
    rotatedCube[D00] = cube[F00]
    rotatedCube[D10] = cube[F10]
    rotatedCube[D20] = cube[F20]
    rotatedString = "".join(rotatedCube)
    output = {}
    output['cube'] = rotatedString
    return output

def _rotateLeftCounterClockwise(cube):
    """ Rotate left counterclockwise """
    cubeList = list(cube)
    rotatedCube = cubeList[:]
    # Rotate front portion
    rotatedCube[F00] = cube[D00]
    rotatedCube[F10] = cube[D10]
    rotatedCube[F20] = cube[D20]
    # Rotate back portion
    rotatedCube[B02] = cube[U20]
    rotatedCube[B12] = cube[U10]
    rotatedCube[B22] = cube[U00]
    # Rotate left face
    rotatedCube[L00] = cube[L02]
    rotatedCube[L01] = cube[L12]
    rotatedCube[L02] = cube[L22]
    rotatedCube[L10] = cube[L01]
    rotatedCube[L11] = cube[L11]
    rotatedCube[L12] = cube[L21]
    rotatedCube[L20] = cube[L00]
    rotatedCube[L21] = cube[L10]
    rotatedCube[L22] = cube[L20]
    # Rotate top portion
    rotatedCube[U00] = cube[F00]
    rotatedCube[U10] = cube[F10]
    rotatedCube[U20] = cube[F20]
    # Rotate bottom portion
    rotatedCube[D00] = cube[B22]
    rotatedCube[D10] = cube[B12]
    rotatedCube[D20] = cube[B02]
    rotatedString = "".join(rotatedCube)
    output = {}
    output['cube'] = rotatedString
    return output

def _rotateUpClockwise(cube):
    """ Rotate up clockwise """
    cubeList = list(cube)
    rotatedCube = cubeList[:]
    # Rotate front portion
    rotatedCube[F00] = cube[R00]
    rotatedCube[F01] = cube[R01]
    rotatedCube[F02] = cube[R02]
    # Rotate right portion
    rotatedCube[R00] = cube[B00]
    rotatedCube[R01] = cube[B01]
    rotatedCube[R02] = cube[B02]
    # Rotate back portion
    rotatedCube[B00] = cube[L00]
    rotatedCube[B01] = cube[L01]
    rotatedCube[B02] = cube[L02]
    # Rotate left portion
    rotatedCube[L00] = cube[F00]
    rotatedCube[L01] = cube[F01]
    rotatedCube[L02] = cube[F02]
    # Rotate top face
    rotatedCube[U00] = cube[U20]
    rotatedCube[U01] = cube[U10]
    rotatedCube[U02] = cube[U00]
    rotatedCube[U10] = cube[U21]
    rotatedCube[U11] = cube[U11]
    rotatedCube[U12] = cube[U01]
    rotatedCube[U20] = cube[U22]
    rotatedCube[U21] = cube[U12]
    rotatedCube[U22] = cube[U02]
    rotatedString = "".join(rotatedCube)
    output = {}
    output['cube'] = rotatedString
    return output
    
def _rotateUpCounterClockwise(cube):
    """ Rotate up counterclockwise """
    cubeList = list(cube)
    rotatedCube = cubeList[:]
    # Rotate front portion
    rotatedCube[F00] = cube[L00]
    rotatedCube[F01] = cube[L01]
    rotatedCube[F02] = cube[L02]
    # Rotate right portion
    rotatedCube[R00] = cube[F00]
    rotatedCube[R01] = cube[F01]
    rotatedCube[R02] = cube[F02]
    # Rotate back portion
    rotatedCube[B00] = cube[R00]
    rotatedCube[B01] = cube[R01]
    rotatedCube[B02] = cube[R02]
    # Rotate left portion
    rotatedCube[L00] = cube[B00]
    rotatedCube[L01] = cube[B01]
    rotatedCube[L02] = cube[B02]
    # Rotate top face
    rotatedCube[U00] = cube[U02]
    rotatedCube[U01] = cube[U12]
    rotatedCube[U02] = cube[U22]
    rotatedCube[U10] = cube[U01]
    rotatedCube[U11] = cube[U11]
    rotatedCube[U12] = cube[U21]
    rotatedCube[U20] = cube[U00]
    rotatedCube[U21] = cube[U10]
    rotatedCube[U22] = cube[U20]
    rotatedString = "".join(rotatedCube)
    output = {}
    output['cube'] = rotatedString
    return output

def _rotateDownClockwise(cube):
    """ Rotate down clockwise """
    cubeList = list(cube)
    rotatedCube = cubeList[:]
    # Rotate front portion
    rotatedCube[F20] = cube[L20]
    rotatedCube[F21] = cube[L21]
    rotatedCube[F22] = cube[L22]
    # Rotate right portion
    rotatedCube[R20] = cube[F20]
    rotatedCube[R21] = cube[F21]
    rotatedCube[R22] = cube[F22]
    # Rotate back portion
    rotatedCube[B20] = cube[R20]
    rotatedCube[B21] = cube[R21]
    rotatedCube[B22] = cube[R22]
    # Rotate left portion
    rotatedCube[L20] = cube[B20]
    rotatedCube[L21] = cube[B21]
    rotatedCube[L22] = cube[B22]
    # Rotate bottom face
    rotatedCube[D00] = cube[D20]
    rotatedCube[D01] = cube[D10]
    rotatedCube[D02] = cube[D00]
    rotatedCube[D10] = cube[D21]
    rotatedCube[D11] = cube[D11]
    rotatedCube[D12] = cube[D01]
    rotatedCube[D20] = cube[D22]
    rotatedCube[D21] = cube[D12]
    rotatedCube[D22] = cube[D02]
    rotatedString = "".join(rotatedCube)
    output = {}
    output['cube'] = rotatedString
    return output

def _rotateDownCounterClockwise(cube):
    """ Rotate down counterclockwise """
    cubeList = list(cube)
    rotatedCube = cubeList[:]
    # Rotate front portion
    rotatedCube[F20] = cube[R20]
    rotatedCube[F21] = cube[R21]
    rotatedCube[F22] = cube[R22]
    # Rotate right portion
    rotatedCube[R20] = cube[B20]
    rotatedCube[R21] = cube[B21]
    rotatedCube[R22] = cube[B22]
    # Rotate back portion
    rotatedCube[B20] = cube[L20]
    rotatedCube[B21] = cube[L21]
    rotatedCube[B22] = cube[L22]
    # Rotate left portion
    rotatedCube[L20] = cube[F20]
    rotatedCube[L21] = cube[F21]
    rotatedCube[L22] = cube[F22]
    # Rotate bottom face
    rotatedCube[D00] = cube[D02]
    rotatedCube[D01] = cube[D12]
    rotatedCube[D02] = cube[D22]
    rotatedCube[D10] = cube[D01]
    rotatedCube[D11] = cube[D11]
    rotatedCube[D12] = cube[D21]
    rotatedCube[D20] = cube[D00]
    rotatedCube[D21] = cube[D10]
    rotatedCube[D22] = cube[D20]
    rotatedString = "".join(rotatedCube)
    output = {}
    output['cube'] = rotatedString
    return output  