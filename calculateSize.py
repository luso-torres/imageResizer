
def newSize(width, height) -> int:
    ''' This function verifies if the image
        already has the proper size (i.e. 
        width greater than 400 pixels) '''
    if width > 400:
        new_width = width//(width//400)
        new_height = height//(width//400)
        #print(new_width,new_height)
        return new_width, new_height
    else:
        #print(width,height)
        return width, height