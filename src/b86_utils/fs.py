import os
import time
import zipfile
import shutil

class fs:
    """ Class to contain the folder structure, with input, dl, tmp, db and out folders created from main
    """
    if os.name == "posix":
        input = os.getcwd()+"//input//"
        dl = os.getcwd()+"//dl//" 
        tmp = os.getcwd()+"//tmp//"
        db = os.getcwd()+"//db//"
        out = os.getcwd()+"//out//"

    else:
        input = os.getcwd()+"\\input\\"
        dl = os.getcwd()+"\\dl\\"
        tmp = os.getcwd()+"\\tmp\\"
        db = os.getcwd()+"\\db\\"
        out = os.getcwd()+"\\out\\"
    
    
    def init(self):
        folders = [x for x in dir(self) if "__" not in x]
        for folder in folders:
            path = getattr(self, folder)
            if type(path) == str and not os.path.isdir(path):
                print(f'#FS: Creating {path}')
                os.mkdir(path)
                
    def format(self):
        folders = [x for x in dir(self) if "__" not in x]
        for folder in folders:
            path = getattr(self, folder)
            if type(path) == str and os.path.isdir(path):
                print(f'#FS: removing {path}')
                shutil.rmtree(path)
        
        
    
    

def p_del(path):
    """Delete a single file

    Args:
        path (string): path to the file to be deleted
    """
    t0 = time.time()
    os.remove(path)
    return(path,time.time()-t0)

def p_unzip(args):
    """unzip a single file

    Args:
        args (list): args[0]: zip file path, args[1]:dir to extract
    """
    file = args[0]
    path = args[1]
    t0 = time.time()
    f = zipfile.ZipFile(file)
    f.extractall(path)
    return(path, time.time()-t0)