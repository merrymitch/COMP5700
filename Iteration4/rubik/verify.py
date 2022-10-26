import rubik.cube as rubik


# Assign the cube mapping to the middle pieces
F11, R11, B11, L11, U11, D11 = 4, 13, 22, 31, 40, 49

def _verify(parms):
    """Determines if the provided cube is physically valid. Returns:
       {'status': 'ok'} if valid 
       {'status': 'error: xxx} if invalid"""
    result = {}
    
    # Call isCubeValid and return the proper dictionary
    if _isCubeValid(parms):
        result['status'] = 'ok'
    else: 
        result['status'] = 'error: invalid cube'
                            
    return result

def _isCubeValid(cube = None):
    """ Check if the cube is valid """
    # Check that parameter is present
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
        middleCharacters = {cubeValue[F11], cubeValue[R11], cubeValue[B11], cubeValue[L11], cubeValue[U11], cubeValue[D11]}
        if len(middleCharacters) == 6:
            # Check that only brgoyw are used and there are nine occurrences of each
            if all(ch in allowedColors for ch in cubeValue):
                for ch in allowedColors:
                    if cubeValue.count(ch) != 9:
                        return False
                return True
    return False