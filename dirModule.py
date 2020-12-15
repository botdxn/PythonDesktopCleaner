import os

STANDARD_DIRS = ["Obrazy", "Dokumenty", "Wideo", "Muzyka", "Inne", "Python", "Programy", "Archiwa"]

def checkDirs():
    for STANDARD_DIR in STANDARD_DIRS:
        if not os.path.exists(STANDARD_DIR):
            os.mkdir(STANDARD_DIR)
            print(f"Katalog {STANDARD_DIR} utworzony.")
        else:
            print(f"Katalog {STANDARD_DIR} już istnieje.")

checkDirs()
#os.mkdir("TestDir")
