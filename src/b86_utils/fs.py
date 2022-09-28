import os
import time
import zipfile
import shutil
import pygsheets
import dtale
import pandas as pd

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
    
    
    def __init__(self):
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

class gdrive_fs:
    def __init__(self, account_file:str, filename:str):
        self.gc = pygsheets.authorize(service_account_file=account_file)
        self.sheet = self.gc.open(filename)
        
            
    def get_df(self, worksheet_name:str):
        worksheet = self.sheet.worksheet_by_title(worksheet_name)
        return worksheet.get_as_df()

    def write_df(self,df, worksheet_name:str, force_create=False):
        try:
            worksheet = self.sheet.worksheet('title',worksheet_name)
        except pygsheets.exceptions.WorksheetNotFound:
            if force_create:
                worksheet = self.sheet.add_worksheet(worksheet_name)
            else:
                raise pygsheets.exceptions.WorksheetNotFound()

        worksheet.set_dataframe(df,(1,1))

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

def edit_df(df:pd.DataFrame):
    d = dtale.show(df, open_browser=True)
    print(f'To edit the DF, open localhost:40000 on your browser... press any key to continue')
    a = input()
    df = d.data.copy() 
    d.kill()
    return df

def filter_df(df: pd.DataFrame, filters:dict):
    for col in filters.keys():
        df = df[df[col].isin(filters[col])].reset_index(drop=True)
    return df