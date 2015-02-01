import os

PATH = 'Q:\\'

def fileScaner():
    files = [os.path.join(root, name)
                for root, dirs, files in os.walk(PATH)
                for name in files]
    
    for filePath in files:
        size = os.path.getsize(filePath)
        fileName, fileExtension = os.path.splitext(filePath)
        print(fileName + ',' + fileExtension + ',' + str(size))

def execute():
    fileScaner()

if __name__ == '__main__':
    execute()
