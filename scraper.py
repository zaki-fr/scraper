import codecs
import pandas as pd
import re
import os
import sys
from subprocess import check_output
import argparse
from pathlib import Path

parser = argparse.ArgumentParser(description='Scraping options of Medical Volume2')
parser.add_argument('--file', type=str,
                    help='Volume2 path that you need to extract')
parser.add_argument('--diag', type= str,
                    help='option to extract lists of diagnostics')

parser.add_argument('--act', type=str,
                    help='option to extract lists of acts')
parser.add_argument('--ghm', type=str,
                    help='option to extract lists of GHMs')
args = parser.parse_args()


def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    sys.stdout.flush()
    bar = fill * filledLength + '-' * (length - filledLength)
    _ = os.system('cls')
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r', flush = True)
    if iteration == total: 
        print()
def diagnotcis_extract():
    df2 = pd.DataFrame()
    j = 0
    i = 0
    t = None
    l = 0
    categ = ""
    categn = ""
    df = pd.read_csv(os.path.dirname(os.path.realpath(__file__))+"\\cmds.txt", sep="\n", header = None)
    while i < df.shape[0] -4:
        i += 1
        if re.match("CATÉGORIE MAJEURE", df.loc[i,0]):
            t = None
            printProgressBar(i + 1, df.shape[0], prefix = ' Diagnostic extraction:', suffix = 'Complete', length = 100)
            categ = df.loc[i,0]
            categn = df.loc[i+1,0]
            list = ""

        str1 = df.loc[i , 0]
        liste = re.match("Liste D-+[0-9]{3}",str1)
        if liste:
            t = True
            list = df.loc[i,0]
            listarray = list.split()
            listcode = listarray[1]

        if t == True:    
            m = re.match("[A-Z]{1,}[0-9]{2}", str1)
            d = df.loc[i+2 , 0]
            v = re.match("[A-Z]{1,}[0-9]{2}", d)
            cklist = re.match("Liste D-+[0-9]{3}", d)
            ckcat  = re.match("Catégorie majeure", d)
            ckman  = re.match("Manuel", d)
            if m:
                if v or cklist or ckcat or ckman:
                    df2.loc[j, 0] =  categ
                    df2.loc[j, 1] = categn
                    df2.loc[j, 3] = list
                    df2.loc[j, 2] =  listcode
                    df2.loc[j, 4] = df.loc[i,0]
                    df2.loc[j, 5] = df.loc[i+1,0]
                    j += 1
                else:
                    df2.loc[j, 0] =  categ
                    df2.loc[j, 1] = categn
                    df2.loc[j, 3] = list
                    df2.loc[j, 2] = listcode
                    df2.loc[j, 4] = df.loc[i,0]
                    df2.loc[j, 5] = df.loc[i+1,0]+ " "+ df.loc[i+2,0]
                    j += 1


    df2.to_excel("Diagnostics_list.xlsx")

def acts_extract():
    l_a = pd.DataFrame()
    df2 = pd.DataFrame()
    j = 0
    i = 0
    t = None
    l = 0
    categ = ""
    categn = ""
    df = pd.read_csv(os.path.dirname(os.path.realpath(__file__))+"\\cmds.txt", sep="\n", header = None)
    while i < df.shape[0] -4:
        i += 1
        
        if re.match("CATÉGORIE MAJEURE", df.loc[i,0]):
            t = None
            printProgressBar(i + 1, df.shape[0], prefix = ' Acts extraction:', suffix = 'Complete', length = 100)
            list = ""
            categ = df.loc[i,0]
            categn = df.loc[i+1,0]


        str1 = df.loc[i , 0]
        #liste = re.match("Liste +[A-Z]-+[0-9]{3}","Liste A-433")
        liste = re.match("Liste A-+[0-9]{3}",str1)
        if liste:
            t = True
            list = df.loc[i,0]
            listarray = list.split()
            listcode = listarray[1]

        if t == True:    
            m = re.match("[A-Z]{4,}[0-9]{3,}", str1)
            if i >= df.shape[0] - 3 :
                break
            d = df.loc[i+3 , 0]
            v1 = re.match("[A-Z]{4,}[0-9]{3,}", d)
            cklist = re.match("Liste A-+[0-9]{3}", d)
            ckcat  = re.match("Catégorie majeure", d)
            ckman  = re.match("Manuel", d)
            d2 = df.loc[i+2 , 0]
            v12 = re.match("[A-Z]{4,}[0-9]{3,}", d2)
            cklist2 = re.match("Liste A-+[0-9]{3}", d2)
            ckcat2  = re.match("Catégorie majeure", d2)
            ckman2  = re.match("Manuel", d2)
            if m:
                s = re.search("/0", str1)
                if s:                    
                    
                    if v12 or cklist2 or ckcat2 or ckman2:
                        l_a.loc[j, 0] =  categ
                        l_a.loc[j, 1] = categn
                        l_a.loc[j, 2] =  listcode
                        l_a.loc[j, 3] = list
                        code = df.loc[i,0]
                        l_a.loc[j, 4] = code[0:7] 
                        l_a.loc[j, 5] = df.loc[i+1,0]
                        j += 1
                    else:
                        l_a.loc[j, 0] =  categ
                        l_a.loc[j, 1] = categn
                        l_a.loc[j, 2] = listcode
                        l_a.loc[j, 3] = list
                        code = df.loc[i,0]
                        l_a.loc[j, 4] = code[0:7] 
                        l_a.loc[j, 5] = df.loc[i+1,0]+ " "+ df.loc[i+2,0]
                        j += 1
                else:       
                    
                    if v1 or cklist or ckcat or ckman:
                        l_a.loc[j, 0] =  categ
                        l_a.loc[j, 1] = categn
                        l_a.loc[j, 2] =  listcode
                        l_a.loc[j, 3] = list
                        l_a.loc[j, 4] = df.loc[i,0]
                        l_a.loc[j, 5] = df.loc[i+2,0]
                        j += 1
                    else:
                        l_a.loc[j, 0] =  categ
                        l_a.loc[j, 1] = categn
                        l_a.loc[j, 2] = listcode
                        l_a.loc[j, 3] = list
                        l_a.loc[j, 4] = df.loc[i,0]
                        l_a.loc[j, 5] = df.loc[i+2,0]+ " "+ df.loc[i+3,0]
                        j += 1


    l_a.to_excel("list_of_acts.xlsx")
def extract_ghm():
    l_ghm = pd.DataFrame()
    ghmdesc = ""
    ghmcode = ""
    j = 0
    i = 0
    df = pd.read_csv(os.path.dirname(os.path.realpath(__file__))+"\\cmds.txt", sep="\n", header = None) 
    while i < df.shape[0] -4:
        i += 1
        if re.match("CATÉGORIE MAJEURE", df.loc[i,0]):
            t = None
            printProgressBar(i + 1, df.shape[0], prefix = ' GHMs Extraction', suffix = 'Complete', length = 100)
            categ = df.loc[i,0]
            categn = df.loc[i+1,0]
        str1 = df.loc[i , 0]
        #liste = re.match("Liste +[A-Z]-+[0-9]{3}","Liste A-433")
        ghmlist = re.match("[0-9]{2,}[A-Z]{1,}[0-9]{2,} ",str1)
        ghmlower1 = re.match("[0-9]{2,}[A-Z]{1,}[0-9]{3,}",str1)
        ghmlower2 = re.match("[0-9]{2,}[A-Z]{1,}[0-9]{2,}[A-Z]{1,}",str1)
        if ghmlist and not ghmlower1 and not ghmlower2 :
            l_ghm.loc[j, 0] = str1[0:5]
            if not re.match("[0-9]{2,}[A-Z]{1,}[0-9]{3,}", str(df.loc[i +1 , 0])) and\
               not re.match("[0-9]{2,}[A-Z]{1,}[0-9]{2,}[A-Z]{1,}", str(df.loc[i + 1 , 0])) and\
               not re.match("[*]",str(df.loc[i + 1 , 0])) and\
               not re.match("Voir",str(df.loc[i + 1 , 0])):
                       l_ghm.loc[j, 1] = str1[5:] + " "+df.loc[i + 1, 0]
                       ghmdesc = str1[5:] + " "+df.loc[i + 1, 0] 

            else:
                l_ghm.loc[j, 1] = str1[5:]
                ghmdesc = str1[5:] 
            ghmcode = str1[0:5]             
        if ghmlower1 or ghmlower2 :
            l_ghm.loc[j, 2] = str1[0:6]
            if not re.match("[0-9]{2,}[A-Z]{1,}[0-9]{3,}", str(df.loc[i + 1 , 0])) and\
               not re.match("[0-9]{2,}[A-Z]{1,}[0-9]{2,}[A-Z]{1,}", str(df.loc[i + 1 , 0])) and\
               not re.match("Voir", str(df.loc[i + 1 , 0])) and\
               not re.match("[*]",str(df.loc[i + 1 , 0])):
                    l_ghm.loc[j, 3] = str1[7:]  + " " + df.loc[i + 1, 0] 
                    l_ghm.loc[j, 0] = ghmcode
                    l_ghm.loc[j, 1] = ghmdesc 
                    j+=1
            else:

                    l_ghm.loc[j, 3] = str1[7:]                 
                    l_ghm.loc[j, 0] = ghmcode
                    l_ghm.loc[j, 1] = ghmdesc 
                    j+=1 
    l_ghm.to_excel("list_GHMs.xlsx")
def java_line(str):
    check_output("java -jar extract_cmds.jar \""+str+"\"", shell=True)

def main():
    cmd = Path(os.path.dirname(os.path.realpath(__file__))+"\\cmds.txt")
    if args.file != "":
        if cmd.exists():
            if args.diag == "y" :
                diagnotcis_extract()
            if args.act == "y":
                acts_extract()
            if args.ghm == "y":
                extract_ghm()
        else:
            java_line(args.file)
            if args.diag == "y" :
                diagnotcis_extract()
            if args.act == "y":
                acts_extract()
            if args.ghm == "y":
                extract_ghm()

if __name__ == '__main__':
    main()