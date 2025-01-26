def saveFile(fileName,width,height,new_width,new_height) -> None:

    with open("files-generated.txt", "a") as file:
        file.write(f'File resized {fileName}: {width}, {height} to {new_width} {new_height}' + '\n')