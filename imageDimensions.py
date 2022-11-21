from PIL import Image
import os, sys

#===Config setup

#Image file extensions to be included
ext_list = ['.png', '.jpg']
#Use this to not re-queue already converted assets (or those that are already the right size)
pixels_to_resize_to = 128
#File that holds all paths of assets to be converted; leave as is to be in the current working directory
paths_of_queued_assets = 'assetsToConvert.txt'
#The ABSOLUTE path of the folder you want to recursively convert assets in
base_path = r'C:\Users\User\Desktop\weapons'

#===MAIN

def main():
    file_output = ''
    path_output = ''

    #Create all the paths of files that need to be convertered
    #Also provide the current width and height of each file
    for folder, sub, files in os.walk(base_path):
        for f in files:
            #Check if file extension is in list specified above...
            if os.path.splitext(f)[1].lower() in ext_list:
                f_path = os.path.join(folder, f)
                width, height = Image.open(f_path).size
                
                #Check to make sure it's a valid asset to convert
                if(width > pixels_to_resize_to):
                    file_output += f_path + ' ' + str(width) + ' ' + str(height) + '\n'
                    path_output += f_path + '\n'

    #Output all asset paths that need to be converted to 
    output_file = open(paths_of_queued_assets, 'w')
    output_file.write(file_output)
    output_file.write('\n')
    output_file.write(path_output)
    output_file.close()

if __name__ == '__main__':
    main()