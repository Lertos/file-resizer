# file-resizer
 A few useful tools for resizing and fixing file extensions

# How to use the tools

## imageDimensions.py : Get a list of all assets needed to be converted

Inside "imageDimensions.py", change the following variables to your needs:
1. ext_list - The list of extensions that you want to be converted
2. pixels_to_resize_to - The size of the images you want your assets to be converted to
3. paths_of_queued_assets - The output file that will hold all paths of assets to be converted
4. base_path - The path where you want this to run against to check RECURSIVELY for assets to be converted

Now use Python to run the "imageDimensions.py" file. 

The assets to be converted should now all be inside the file at the path given in the "paths_of_queued_assets" variable. NOTE: There will be two lists: one will have the file path as well as the current image width and height, and the second list will have just the file paths.

## filesToResize.txt : Get the paths of assets to be converted

Now you need to take the second list of paths and copy paste them inside "filesToResize.txt". We will use this list with the BlackMagic tool to resize all of them to the desired size.

## resizeImages.bat : Resize all the images at the supplied paths

Simply double click the "resizeImages.bat" file and it will read the "filesToResize.txt" file and sequentially resize each asset.

## OPTIONAL: fixFileExtensions.bat : Fix uppercase (or lowercase) file extensions

If you have any files that have an uppercase "PNG" for example, this will change it to "png". Might be easier in code if they are all using the same file extension - incase you want to use something such as: fileName + ".png".
