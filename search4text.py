import glob
import os

def search4text(path, text):
    def read(file, text):
        try:
            with open(file) as f:
                next_line = f.readline()
                while next_line:
                    if text in next_line:
                        print(file)
                        break
                    next_line = f.readline()
        except:
            return
    
    def traverse(directories):
        while directories:
            for child in directories:
                if os.path.isdir(child) is False:
                    read(child, text)
                child_directories = glob.glob('%s/*' %(child))
                traverse(child_directories)
            return
        
    traverse(glob.glob('%s/*' %path))

search4text(path = '/home/user/wanted_folder', text = 'wanted_string')
