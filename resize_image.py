from PIL import Image
import calculateSize
import os,verifyFile

if __name__ == '__main__':
    #image.show()
    folder_path = os.getcwd()
    for fileName in os.listdir(folder_path):
        if (fileName.endswith('.png') or fileName.endswith('.jpg') or fileName.endswith('.bmp')) and (not fileName.startswith('resized')):
                image = Image.open(fileName)
                width, height = image.size
                new_width, new_height =calculateSize.newSize(width, height)
                line =(f'File resized {fileName}: {width}, {height} to {new_width}, {new_height}')
                print(line)
                resized_image = image.resize((new_width, new_height))
                resized_image.save(f'resized_{fileName}')
                verifyFile.Verifier(line,width,height,new_width,new_height)
                    #save.saveFile(fileName,width,height,new_width,new_height)    
    print('Code finished and files generated.')
                #resized_image.show()
    #print(width,height)
    
    # resized_image = image.resize((new_width,new_height))
    # print(resized_image.size)
    # resized_image.save('resized_image.png')