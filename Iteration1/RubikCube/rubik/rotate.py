import rubik.cube as rubik

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
    # Call isCubeValid to determine if the passed cube is a valid rubik's cube
    if _isCubeValid(parms):
        encodedCube = parms.get('cube')
    else: 
        result['status'] = 'error: invalid cube'
        return result   
    
    # If everything is valid, then call rotateCube to perform the operations       
    result['cube'] = _rotateCube(encodedDir, encodedCube).get('cube')             
    result['status'] = 'ok'                     
    return result

def _isCubeValid(cube = None):
    """ Check if the cube is valid """
    #Check that parameter is present
    if cube == None:
        return False
    
    # Make sure that cube key is present and that it has a value
    if (not 'cube' in cube) or (cube['cube'] == None):
        return False
    
    cubeValue = cube.get('cube')
    allowedColors = 'brgoyw'
    
    # Check the length colors of the cube
    if len(cubeValue) == 54:
        # Make sure all the middle pieces are unique
        middle_characters = {cubeValue[4], cubeValue[13], cubeValue[22], cubeValue[31], cubeValue[40], cubeValue[49]}
        if len(middle_characters) == 6:
            # Check that only brgoyw are used and there are nine occurrences of each
            if all(ch in allowedColors for ch in cubeValue):
                for ch in allowedColors:
                    if cubeValue.count(ch) != 9:
                        return False
                return True
    return False

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
    rotatedCube[0] = cube[6]
    rotatedCube[1] = cube[3]
    rotatedCube[2] = cube[0]
    rotatedCube[3] = cube[7]
    rotatedCube[4] = cube[4]
    rotatedCube[5] = cube[1]
    rotatedCube[6] = cube[8]
    rotatedCube[7] = cube[5]
    rotatedCube[8] = cube[2]
    # Rotate right portion
    rotatedCube[9] = cube[42]
    rotatedCube[12] = cube[43]
    rotatedCube[15] = cube[44]
    # Rotate left portion
    rotatedCube[29] = cube[45]
    rotatedCube[32] = cube[46]
    rotatedCube[35] = cube[47]
    # Rotate top portion
    rotatedCube[42] = cube[35]
    rotatedCube[43] = cube[32]
    rotatedCube[44] = cube[29]
    # Rotate bottom portion
    rotatedCube[45] = cube[15]
    rotatedCube[46] = cube[12]
    rotatedCube[47] = cube[9]
    rotatedString = "".join(rotatedCube)
    output = {}
    output['cube'] = rotatedString
    return output
    
def _rotateFrontCounterClockwise(cube):
    """ Rotate front counterclockwise """
    cubeList = list(cube)
    rotatedCube = cubeList[:]
    # Rotate front face
    rotatedCube[0] = cube[2]
    rotatedCube[1] = cube[5]
    rotatedCube[2] = cube[8]
    rotatedCube[3] = cube[1]
    rotatedCube[4] = cube[4]
    rotatedCube[5] = cube[7]
    rotatedCube[6] = cube[0]
    rotatedCube[7] = cube[3]
    rotatedCube[8] = cube[6]
    # Rotate right portion
    rotatedCube[9] = cube[47]
    rotatedCube[12] = cube[46]
    rotatedCube[15] = cube[45]
    # Rotate left portion
    rotatedCube[29] = cube[44]
    rotatedCube[32] = cube[43]
    rotatedCube[35] = cube[42]
    # Rotate top portion
    rotatedCube[42] = cube[9]
    rotatedCube[43] = cube[12]
    rotatedCube[44] = cube[15]
    # Rotate bottom portion
    rotatedCube[45] = cube[29]
    rotatedCube[46] = cube[32]
    rotatedCube[47] = cube[35]
    rotatedString = "".join(rotatedCube)
    output = {}
    output['cube'] = rotatedString
    return output

def _rotateRightClockwise(cube):
    """ Rotate right clockwise """
    cubeList = list(cube)
    rotatedCube = cubeList[:]
    # Rotate front portion
    rotatedCube[2] = cube[47]
    rotatedCube[5] = cube[50]
    rotatedCube[8] = cube[53]
    # Rotate right face
    rotatedCube[9] = cube[15]
    rotatedCube[10] = cube[12]
    rotatedCube[11] = cube[9]
    rotatedCube[12] = cube[16]
    rotatedCube[13] = cube[13]
    rotatedCube[14] = cube[10]
    rotatedCube[15] = cube[17]
    rotatedCube[16] = cube[14]
    rotatedCube[17] = cube[11]
    # Rotate back portion
    rotatedCube[18] = cube[44]
    rotatedCube[21] = cube[41]
    rotatedCube[24] = cube[38]
    # Rotate top portion
    rotatedCube[38] = cube[2]
    rotatedCube[41] = cube[5]
    rotatedCube[44] = cube[8]
    # Rotate bottom portion
    rotatedCube[47] = cube[24]
    rotatedCube[50] = cube[21]
    rotatedCube[53] = cube[18]
    rotatedString = "".join(rotatedCube)
    output = {}
    output['cube'] = rotatedString
    return output
    
def _rotateRightCounterClockwise(cube):
    """ Rotate right counterclockwise """
    cubeList = list(cube)
    rotatedCube = cubeList[:]
    # Rotate front portion
    rotatedCube[2] = cube[38]
    rotatedCube[5] = cube[41]
    rotatedCube[8] = cube[44]
    # Rotate right face
    rotatedCube[9] = cube[11]
    rotatedCube[10] = cube[14]
    rotatedCube[11] = cube[17]
    rotatedCube[12] = cube[10]
    rotatedCube[13] = cube[13]
    rotatedCube[14] = cube[16]
    rotatedCube[15] = cube[9]
    rotatedCube[16] = cube[12]
    rotatedCube[17] = cube[15]
    # Rotate back portion
    rotatedCube[18] = cube[53]
    rotatedCube[21] = cube[50]
    rotatedCube[24] = cube[47]
    # Rotate top portion
    rotatedCube[38] = cube[24]
    rotatedCube[41] = cube[21]
    rotatedCube[44] = cube[18]
    # Rotate bottom portion
    rotatedCube[47] = cube[2]
    rotatedCube[50] = cube[5]
    rotatedCube[53] = cube[8]
    rotatedString = "".join(rotatedCube)
    output = {}
    output['cube'] = rotatedString
    return output

def _rotateBackClockwise(cube):
    """ Rotate back clockwise """
    cubeList = list(cube)
    rotatedCube = cubeList[:]
    # Rotate right portion
    rotatedCube[11] = cube[53]
    rotatedCube[14] = cube[52]
    rotatedCube[17] = cube[51]
    # Rotate back face
    rotatedCube[18] = cube[24]
    rotatedCube[19] = cube[21]
    rotatedCube[20] = cube[18]
    rotatedCube[21] = cube[25]
    rotatedCube[22] = cube[22]
    rotatedCube[23] = cube[19]
    rotatedCube[24] = cube[26]
    rotatedCube[25] = cube[23]
    rotatedCube[26] = cube[20]
    # Rotate left portion
    rotatedCube[27] = cube[38]
    rotatedCube[30] = cube[37]
    rotatedCube[33] = cube[36]
    # Rotate top portion
    rotatedCube[36] = cube[11]
    rotatedCube[37] = cube[14]
    rotatedCube[38] = cube[17]
    # Rotate bottom portion
    rotatedCube[51] = cube[27]
    rotatedCube[52] = cube[30]
    rotatedCube[53] = cube[33]
    rotatedString = "".join(rotatedCube)
    output = {}
    output['cube'] = rotatedString
    return output

def _rotateBackCounterClockwise(cube):
    """ Rotate back counterclockwise """
    cubeList = list(cube)
    rotatedCube = cubeList[:]
    # Rotate right portion 
    rotatedCube[11] = cube[36]
    rotatedCube[14] = cube[37]
    rotatedCube[17] = cube[38]
    # Rotate back face
    rotatedCube[18] = cube[20]
    rotatedCube[19] = cube[23]
    rotatedCube[20] = cube[26]
    rotatedCube[21] = cube[19]
    rotatedCube[22] = cube[22]
    rotatedCube[23] = cube[25]
    rotatedCube[24] = cube[18]
    rotatedCube[25] = cube[21]
    rotatedCube[26] = cube[24]
    # Rotate left portion
    rotatedCube[27] = cube[51]
    rotatedCube[30] = cube[52]
    rotatedCube[33] = cube[53]
    # Rotate top portion
    rotatedCube[36] = cube[33]
    rotatedCube[37] = cube[30]
    rotatedCube[38] = cube[27]
    # Rotate bottom portion
    rotatedCube[51] = cube[17]
    rotatedCube[52] = cube[14]
    rotatedCube[53] = cube[11]
    rotatedString = "".join(rotatedCube)
    output = {}
    output['cube'] = rotatedString
    return output

def _rotateLeftClockwise(cube):
    """ Rotate left clockwise """
    cubeList = list(cube)
    rotatedCube = cubeList[:]
    # Rotate front portion
    rotatedCube[0] = cube[36]
    rotatedCube[3] = cube[39]
    rotatedCube[6] = cube[42]
    # Rotate back portion
    rotatedCube[20] = cube[51]
    rotatedCube[23] = cube[48]
    rotatedCube[26] = cube[45]
    # Rotate left face
    rotatedCube[27] = cube[33]
    rotatedCube[28] = cube[30]
    rotatedCube[29] = cube[27]
    rotatedCube[30] = cube[34]
    rotatedCube[31] = cube[31]
    rotatedCube[32] = cube[28]
    rotatedCube[33] = cube[35]
    rotatedCube[34] = cube[32]
    rotatedCube[35] = cube[29]
    # Rotate top portion
    rotatedCube[36] = cube[26]
    rotatedCube[39] = cube[23]
    rotatedCube[42] = cube[20]
    # Rotate bottom portion
    rotatedCube[45] = cube[0]
    rotatedCube[48] = cube[3]
    rotatedCube[51] = cube[6]
    rotatedString = "".join(rotatedCube)
    output = {}
    output['cube'] = rotatedString
    return output

def _rotateLeftCounterClockwise(cube):
    """ Rotate left counterclockwise """
    cubeList = list(cube)
    rotatedCube = cubeList[:]
    # Rotate front portion
    rotatedCube[0] = cube[45]
    rotatedCube[3] = cube[48]
    rotatedCube[6] = cube[51]
    # Rotate back portion
    rotatedCube[20] = cube[42]
    rotatedCube[23] = cube[39]
    rotatedCube[26] = cube[36]
    # Rotate left face
    rotatedCube[27] = cube[29]
    rotatedCube[28] = cube[32]
    rotatedCube[29] = cube[35]
    rotatedCube[30] = cube[28]
    rotatedCube[31] = cube[31]
    rotatedCube[32] = cube[34]
    rotatedCube[33] = cube[27]
    rotatedCube[34] = cube[30]
    rotatedCube[35] = cube[33]
    # Rotate top portion
    rotatedCube[36] = cube[0]
    rotatedCube[39] = cube[3]
    rotatedCube[42] = cube[6]
    # Rotate bottom portion
    rotatedCube[45] = cube[26]
    rotatedCube[48] = cube[23]
    rotatedCube[51] = cube[20]
    rotatedString = "".join(rotatedCube)
    output = {}
    output['cube'] = rotatedString
    return output

def _rotateUpClockwise(cube):
    """ Rotate up clockwise """
    cubeList = list(cube)
    rotatedCube = cubeList[:]
    # Rotate front portion
    rotatedCube[0] = cube[9]
    rotatedCube[1] = cube[10]
    rotatedCube[2] = cube[11]
    # Rotate right portion
    rotatedCube[9] = cube[18]
    rotatedCube[10] = cube[19]
    rotatedCube[11] = cube[20]
    # Rotate back portion
    rotatedCube[18] = cube[27]
    rotatedCube[19] = cube[28]
    rotatedCube[20] = cube[29]
    # Rotate left portion
    rotatedCube[27] = cube[0]
    rotatedCube[28] = cube[1]
    rotatedCube[29] = cube[2]
    # Rotate top face
    rotatedCube[36] = cube[42]
    rotatedCube[37] = cube[39]
    rotatedCube[38] = cube[36]
    rotatedCube[39] = cube[43]
    rotatedCube[40] = cube[40]
    rotatedCube[41] = cube[37]
    rotatedCube[42] = cube[44]
    rotatedCube[43] = cube[41]
    rotatedCube[44] = cube[38]
    rotatedString = "".join(rotatedCube)
    output = {}
    output['cube'] = rotatedString
    return output
    
def _rotateUpCounterClockwise(cube):
    """ Rotate up counterclockwise """
    cubeList = list(cube)
    rotatedCube = cubeList[:]
    # Rotate front portion
    rotatedCube[0] = cube[27]
    rotatedCube[1] = cube[28]
    rotatedCube[2] = cube[29]
    # Rotate right portion
    rotatedCube[9] = cube[0]
    rotatedCube[10] = cube[1]
    rotatedCube[11] = cube[2]
    # Rotate back portion
    rotatedCube[18] = cube[9]
    rotatedCube[19] = cube[10]
    rotatedCube[20] = cube[11]
    # Rotate left portion
    rotatedCube[27] = cube[18]
    rotatedCube[28] = cube[19]
    rotatedCube[29] = cube[20]
    # Rotate top face
    rotatedCube[36] = cube[38]
    rotatedCube[37] = cube[41]
    rotatedCube[38] = cube[44]
    rotatedCube[39] = cube[37]
    rotatedCube[40] = cube[40]
    rotatedCube[41] = cube[43]
    rotatedCube[42] = cube[36]
    rotatedCube[43] = cube[39]
    rotatedCube[44] = cube[42]
    rotatedString = "".join(rotatedCube)
    output = {}
    output['cube'] = rotatedString
    return output

def _rotateDownClockwise(cube):
    """ Rotate down clockwise """
    cubeList = list(cube)
    rotatedCube = cubeList[:]
    # Rotate front portion
    rotatedCube[6] = cube[33]
    rotatedCube[7] = cube[34]
    rotatedCube[8] = cube[35]
    # Rotate right portion
    rotatedCube[15] = cube[6]
    rotatedCube[16] = cube[7]
    rotatedCube[17] = cube[8]
    # Rotate back portion
    rotatedCube[24] = cube[15]
    rotatedCube[25] = cube[16]
    rotatedCube[26] = cube[17]
    # Rotate left portion
    rotatedCube[33] = cube[24]
    rotatedCube[34] = cube[25]
    rotatedCube[35] = cube[26]
    # Rotate bottom face
    rotatedCube[45] = cube[51]
    rotatedCube[46] = cube[48]
    rotatedCube[47] = cube[45]
    rotatedCube[48] = cube[52]
    rotatedCube[49] = cube[49]
    rotatedCube[50] = cube[46]
    rotatedCube[51] = cube[53]
    rotatedCube[52] = cube[50]
    rotatedCube[53] = cube[47]
    rotatedString = "".join(rotatedCube)
    output = {}
    output['cube'] = rotatedString
    return output

def _rotateDownCounterClockwise(cube):
    """ Rotate down counterclockwise """
    cubeList = list(cube)
    rotatedCube = cubeList[:]
    # Rotate front portion
    rotatedCube[6] = cube[15]
    rotatedCube[7] = cube[16]
    rotatedCube[8] = cube[17]
    # Rotate right portion
    rotatedCube[15] = cube[24]
    rotatedCube[16] = cube[25]
    rotatedCube[17] = cube[26]
    # Rotate back portion
    rotatedCube[24] = cube[33]
    rotatedCube[25] = cube[34]
    rotatedCube[26] = cube[35]
    # Rotate left portion
    rotatedCube[33] = cube[6]
    rotatedCube[34] = cube[7]
    rotatedCube[35] = cube[8]
    # Rotate bottom face
    rotatedCube[45] = cube[47]
    rotatedCube[46] = cube[50]
    rotatedCube[47] = cube[53]
    rotatedCube[48] = cube[46]
    rotatedCube[49] = cube[49]
    rotatedCube[50] = cube[52]
    rotatedCube[51] = cube[45]
    rotatedCube[52] = cube[48]
    rotatedCube[53] = cube[51]
    rotatedString = "".join(rotatedCube)
    output = {}
    output['cube'] = rotatedString
    return output
    
    
    
    
    
    
    