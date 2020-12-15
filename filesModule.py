import os, shutil, dirModule

#definition for paths and standard extensions
pathDesktop = "C:\\Users\\Marcin\\Desktop\\"
images = [".jpg", ".jpeg", ".png", ".tga", ".tiff", ".bmp", ".gif"]
documents = [".pdf", ".txt", ".doc", ".docx", ".mobi", ".epub", ".rtf", ".odt"]
video = [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm"]
python = [".py", ".pyc", ".pyw"]

#create list of files inside a given directory
filesList = []
for (pathDesktop, dirnames, filenames) in os.walk(pathDesktop):
    for filename in filenames:
            filesList.append(pathDesktop + filename)
    break

#check and return given file extension
def fileExtension(file):
    filename, file_ext = os.path.splitext(file)
    #print(file_ext)
    return filename, file_ext

#copy files from a given files list to directory based on their extensions
def moveFiles(filesList):

    for file in filesList:

        #OBRAZY
        if fileExtension(file)[1] in images:
            shutil.move(file, pathDesktop + "Obrazy\\" + os.path.basename(file))
            print(f"Przeniesiono {os.path.basename(file)} do katalogu \"Obrazy\"")

        #DOKUMENTY
        elif fileExtension(file)[1] in documents:
            shutil.move(file, pathDesktop + "Dokumenty\\" + os.path.basename(file))
            print(f"Przeniesiono {os.path.basename(file)} do katalogu \"Dokumenty\"")

        #WIDEO
        elif fileExtension(file)[1] in video:
            shutil.move(file, pathDesktop + "Wideo\\" + os.path.basename(file))
            print(f"Przeniesiono {os.path.basename(file)} do katalogu \"Wideo\"")

        elif fileExtension(file)[1] == ".exe":
            shutil.move(file, pathDesktop + "Programy\\" + os.path.basename(file))
            print(f"Przeniesiono {os.path.basename(file)} do katalogu \"Programy\"")

        elif fileExtension(file)[1] == ".rar" or fileExtension(file)[1] == ".zip" or fileExtension(file)[1] == ".7z":
            shutil.move(file, pathDesktop + "Archiwa\\" + os.path.basename(file))
            print(f"Przeniesiono {os.path.basename(file)} do katalogu \"Archiwa\"")

        #INNE
        else:
            try:
                shutil.move(file, pathDesktop + "Inne\\" + os.path.basename(file))
                print(f"Przeniesiono {os.path.basename(file)} do katalogu \"Inne\"")
            except:
                pass


        #PYTHON
        '''elif fileExtension(file)[1] in python:
            shutil.move(file, pathDesktop + "Python\\" + os.path.basename(file))
            print(f"Przeniesiono {os.path.basename(file)} do katalogu \"Python\"")'''


moveFiles(filesList)
