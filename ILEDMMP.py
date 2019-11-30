import os
import sys
import tkinter as tk
import tkinter.ttk as ttk
import time
from collections import Counter
from tkinter.filedialog import askopenfilename, re

import numpy as np

import ILEDMMP_support


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel (root)
    ILEDMMP_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel (w)
    ILEDMMP_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel():
    global w
    w.destroy()
    w = None


class Toplevel:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("1366x685+1+30")
        top.title("Intelligent Logical Error Detection and Mitigation Model for Python")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        def newFile():
            if os.path.exists("sentencesword"):
                os.remove("sentencesword")
            self.file = None
            self.Entry1.delete(0, 'end')
            self.Text1.delete(1.0, tk.END)
            self.Text2.delete(1.0, tk.END)
            self.Text3.delete(1.0, tk.END)
            self.Text4.delete(1.0, tk.END)
            self.Text5.delete(1.0, tk.END)
            self.Text6.delete(1.0, tk.END)
            self.Text7.delete(1.0, tk.END)
            self.Text8.delete(1.0, tk.END)
            self.Text9.delete(1.0, tk.END)
            self.Text10.delete(1.0, tk.END)


        def openFile():
            if os.path.exists("sentencesword"):
                os.remove("sentencesword")
            self.Entry1.delete(0, 'end')
            self.Text1.delete(1.0, tk.END)
            self.Text2.delete(1.0, tk.END)
            self.Text3.delete(1.0, tk.END)
            self.Text4.delete(1.0, tk.END)
            self.Text5.delete(1.0, tk.END)
            self.Text6.delete(1.0, tk.END)
            self.Text7.delete(1.0, tk.END)
            self.Text8.delete(1.0, tk.END)
            self.Text9.delete(1.0, tk.END)
            self.Text10.delete(1.0, tk.END)
            self.file = askopenfilename(defaultextension=".py", filetypes=[("Python", "*.py")])
            if self.file == "":

                # no file to open
                self.file = None
            else:

                # Try to open the file
                # set the window title
                top.title("Intelligent Logical Error Detection and Mitigation Model for Python - " + os.path.basename(
                    self.file))
                self.Text1.delete(1.0, tk.END)
                file = open(self.file, "r")
                self.Text1.insert(1.0, file.read())
                file.close()
                with open("sentencesword", "w") as stword:
                    stword.write(self.Text1.get(1.0,tk.END))
                    stword.close()

        def popup(event):
            menu.post(event.x_root, event.y_root)

        def twdel():
            cleanfield()
            deltextfile()

        def cleanfield():
            self.Entry1.delete(0, 'end')
            self.Text1.delete(1.0, tk.END)
            self.Text2.delete(1.0, tk.END)
            self.Text3.delete(1.0, tk.END)
            self.Text4.delete(1.0, tk.END)
            self.Text5.delete(1.0, tk.END)
            self.Text6.delete(1.0, tk.END)
            self.Text7.delete(1.0, tk.END)
            self.Text8.delete(1.0, tk.END)
            self.Text9.delete(1.0, tk.END)
            self.Text10.delete(1.0, tk.END)

        def deltextfile():
            os.remove("sentencesword")

        def keyboardkeypressed(key):
            with open("sentencesword", "w") as stwrd:
                stwrd.write(self.Text1.get(1.0,tk.END))
                stwrd.close()
            x = key.char
            if ord(x) == 13:
                    with open("sentencesword", "a") as stword:
                        stword.write(self.Entry1.get())
                        stword.close()
                        self.Entry1.delete(0,'end')
                        corretext()
        totime =""
        def corretext():
            totime = time.time()
            with open("sentencesword") as infile, open("sentenceswor", 'w') as outfile:
                for line in infile:
                    if not line.strip(): continue  # skip the empty line
                    outfile.write(line)
            with open("sentenceswor", "r") as stwrd:
                self.Text1.delete(1.0, tk.END)
                stwrd = stwrd.read()
                self.Text1.insert(1.0,stwrd)
                x = self.Text1.get(1.0, tk.END)
                removeunvariable()
                variable()
                if len(self.Text2.get("1.0", tk.END)) == 1:
                    self.Text3.delete(1.0,tk.END)
                duplicate()
                if "[" and "]" and "(" and ")" and "print" and "while" in x:
                    self.Text6.delete(1.0,tk.END)
                if "/" in x:
                    findingsha()
                if len(self.Text2.get("1.0", tk.END)) == 1:
                    removingelement()
                for line in x:
                    if "[" and "]" in line:
                        indexarray()
                reassigning()
                if "+=" in x or "-=" in x:
                    infinityloop()
                    comparingword()
            print("Total Time Cycle = " + str(time.time() - totime))



        reeletime = ""
        def removingelement():
            reeletime = time.time()
            self.Text5.delete(1.0, tk.END)
            exlin = list()
            x = self.Text1.get(1.0, tk.END)
            with open("dupai", "w") as dupli:
                dupli.write(x)
                dupli.close()
            with open("dupai", "r") as dup:
                exline = set()
                for line in dup:
                    if line in exline:
                        self.Text5.insert(1.0, line)
                    else:
                        exline.add(line)
            exlin = exline
            #self.Text3.insert(1.0, exlin)
            with open("dupaires", "w") as fianlremove:
                fianlremove.write(str(exlin))
                fianlremove.close()
                self.Text5.delete(1.0, tk.END)

            with open("dupaires", "r") as fialremove:
                fialr = fialremove.read().replace("{", "").replace("}", "").replace("'", "").replace("\\n", "").replace(
                    ",", "\n")
                self.Text5.insert(1.0, fialr)
                filr = fialr.replace(" ", "")
            with open("duplicate_clean.py", "w") as clan:
                clan.write('')
                clan.close()
            with open("duplicate_clean.py", "a") as clan:
                clan.write(filr)
                clan.close()
                msg = "_____________________________________________\n"
                self.Text5.insert(1.0, msg)
                msg = "a clean file created named duplicate_clean.py"
                self.Text5.insert(1.0, msg)
            print("Removing Duplication Time = "+str(time.time()-reeletime))


        retime = ""
        def removeunvariable():
            retime = time.time()
            self.Text3.delete(1.0,tk.END)
            x = self.Text1.get(1.0, tk.END)
            with open("mnflex", "w") as maf:
                maf.write(x)
                maf.close()
            with open("mnflex", "r") as f:
                f = f.read().splitlines()
                for line in f:
                    if "while" not in line:
                        if "+=" not in line:
                            if "-=" not in line:
                                if "print" not in line:
                                    if "." not in line:
                                        if "," not in line:
                                            if "\\" not in line:
                                                if "/" not in line:
                                                    self.Text2.insert(1.0, line + " ")

            with open("vribleex", "w") as varia:
                varia.write(self.Text2.get(1.0, tk.END))
                varia.close()
                self.Text2.delete(1.0, tk.END)

            with open("vribleex", "r") as vria:
                vx = vria.read().replace("=", '').split()
                for word in vx:
                    if word.isdigit() == True:
                        print(" ")
                    else:
                        self.Text2.insert(1.0, "\n " + word + "\n")

            with open("lnevariable", "w") as aloneva:
                aloneva.write(self.Text2.get(1.0, tk.END))
                aloneva.close()
                self.Text2.delete(1.0, tk.END)

            exline = set()
            with open("lnevariable", "r") as alonea:
                alonea = alonea.read().replace("\n", "").split()
                for line in alonea:
                    if line in exline:
                        line
                    else:
                        exline.add(line)
                        self.Text2.insert(1.0, line + " \n")

            with open("inlvariles", "w") as finalvariles:
                finalvariles.write(self.Text2.get(1.0, tk.END))
                finalvariles.close()
                self.Text2.delete(1.0, tk.END)

            with open("inlvariles", "r") as fnalva:
                fnalva = fnalva.read().replace(' ', "").split()
            with open("mnflex", "r") as fna:
                fna = fna.read().splitlines()
                for word in fnalva:
                    for line in fna:
                        if word in line:
                            self.Text2.insert(1.0, line + "\n")

            with open("resulariable", "w") as resfvar:
                resfvar.write(self.Text2.get(1.0, tk.END))
                resfvar.close()

            with open("inlvariles", "r") as finalvaris:
                finalvaris = finalvaris.read().split()
                variables = np.asarray(finalvaris)

            with open("resulariable", "r") as resvar:
                self.Text2.delete(1.0, tk.END)
                resvar = resvar.read().splitlines()
                resultarr = np.asarray(resvar)
                for word in variables:
                    for line in resultarr:
                        if word in line:
                            self.Text2.insert(1.0, word + " ")

            with open("fresulariable", "w") as resar:
                resar.write(self.Text2.get(1.0, tk.END))
                resar.close()
                self.Text2.delete(1.0, tk.END)
            with open("fresulariable", "r") as file:
                wordcount = Counter(file.read().split())
                self.Text2.insert(1.0, wordcount)

            with open("sinevari", "w") as singlevar:
                singlevar.write(self.Text2.get(1.0, tk.END))
                singlevar.close()
                self.Text2.delete(1.0, tk.END)

            with open("sinevari", "r") as singleva:
                singleva = singleva.read().replace("Counter", "").replace("(", "").replace(")", "").replace("'",
                                                                                                            " ").replace(
                    "[", " ").replace("]", " ").replace("{", "").replace("}", "").replace(":", "").replace(",",
                                                                                                           "").split()
                self.Text2.insert(1.0, singleva)
            with open("slevari", "w") as sinlevar:
                sinlevar.write(self.Text2.get(1.0, tk.END))
                sinlevar.close()
                self.Text2.delete(1.0, tk.END)
            with open("slevari", "r") as sinle:
                single = np.asarray(singleva)
                for i in range(len(single)):
                    if single[i] == "1":
                        self.Text2.insert(1.0, single[i - 1] + " \n")
            with  open("getusedvari", "w") as getus:
                getus.write(self.Text2.get(1.0, tk.END))
                getus.close()
            with  open("getusedvari", "r") as getss:
                with  open("mnflex", "r") as getsws:
                    getsws = getsws.read().splitlines()
                getsss = getss.read().split()
                assd = np.asarray(getsss)
                asds = np.asarray(getsws)
                self.Text2.delete(1.0, tk.END)
                for i in range(len(assd)):
                    v = ""
                    v = assd[i]
                    for line in asds:
                        if v in line:
                            self.Text2.insert(1.0, line + "\n")
                        if v not in line:
                            self.Text3.insert(1.0, line + "\n")
                with open("sourcecode", "w") as sources:
                    sources.write(self.Text3.get(1.0, tk.END))
                    sources.close()
                    self.Text3.delete(1.0, tk.END)
                with open("sourcecode", "r") as surces:
                    surces = surces.read().splitlines()
                    ase = np.asarray(surces)
                    for line in surces:
                        self.Text3.insert(1.0, line + "\n")

                with open("MLogical_clean.py", "w") as clan:
                    clan.write(self.Text3.get(1.0, tk.END))
                clan.close()
                msg = "_____________________________________________"
                self.Text3.insert(1.0, msg)
                msg = "\na clean file created named MLogical_clean.py"
                self.Text3.insert(1.0, msg)
                self.Text3.insert(1.0, "\n")
            print("Removing Variable Time = "+str(time.time()-retime))

        looptime =""
        def comparingword():
            looptime = time.time()
            lineList = list()
            with open("mainfile", "w") as maf:
                maf.write(self.Text10.get(1.0, tk.END))
                maf.close()
            with open("mainfile", "r") as f:
                for line in f:
                    if "print" not in line:
                        lineList.append(line)

                self.Text8.insert(1.0, lineList)
                f.close()

                with open("loop1", "w") as file1:
                    file1.write(self.Text8.get(1.0, tk.END))
                    self.Text8.delete(1.0, tk.END)
                    file1.close()
                    print("1. Done")
            convert()

        def convert():
            print("2. Convert")
            with open('loop1', 'r') as f:
                data = f.read().replace('}', '')
                dats = data.replace('{', '')
                self.Text8.insert(1.0, dats)
                xc = dats.split()
                self.Text9.insert(1.0, xc)
                fxc = open("single", "w")
                fxc.write(self.Text3.get(1.0, tk.END))
                fxc.close()
                self.Text9.delete(1.0, tk.END)
                print("2. Done ")
                newtwo()

        def newtwo():
            print("3. New Two")
            with open("single", "r") as fg:
                a = fg.read().split()
                b = []
                for item in a:
                    if item not in b:
                        b.append(item)
                    else:
                        self.Text3.insert(1.0, item + " = ")
                        fxcx = open("equal", "w")
                        fxcx.write(self.Text3.get(1.0, tk.END))
                        fxcx.close()
                        break
                        print(item)
            self.Text3.delete(1.0, tk.END)
            with open('single', 'r') as f:
                data = f.read().split()
                self.Text8.insert(1.0, data)
                f.close()
                print("3. Done")
                matchvari()

        def matchvari():
            print("4. Match Variable")
            digitalnum = open("single", "r")
            dig = digitalnum.read()
            x = [int(s) for s in dig.split() if s.isdigit()]
            self.Text8.insert(1.0, x)
            fxcx = open("digi", "w")
            fxcx.write(self.Text8.get(1.0, tk.END))
            fxcx.close()
            self.Text8.delete(1.0, tk.END)
            print("4. Done")
            merging()

        def merging():
            print("5. Merging")
            with open("digi", "r") as digi:
                with open("equal", "r") as eqal:
                    x = digi.read().split()
                    y = eqal.read().splitlines()
                    print(x)
                    print(y)
                    xarr = np.asanyarray(x)
                    yarr = np.asanyarray(y)
                    for line in yarr:
                        for i in range(len(xarr)):
                            x = " " + line + xarr[i]
                            self.Text9.insert(1.0, x)
                with open("vari", "w") as f:
                    f.write(self.Text9.get(1.0, tk.END))
                    f.close()
                    self.Text9.delete(1.0, tk.END)
                print("5. Done")
            matchingvari()

        def matchingvari():
            print("6. Matching Varible")
            with open('vari', 'r') as f:
                data = f.read().replace('}', '')
                dats = data.replace('{', ' ')
                xc = dats.split()
                self.Text8.insert(1.0, xc)
                print(xc)
                f.close()
                with open('lineloop', 'w') as f:
                    f.write(self.Text8.get(1.0, tk.END))
                    f.close()
                    self.Text8.delete(1.0, tk.END)
                    print("6. Done")
                    lineloop()

        def lineloop():
            print("7. line loop ")
            with open("lineloop", "r") as f:
                data = f.read().split()
                arraynew = np.asanyarray(data)
                x = len(data)
                y = len(arraynew) - 1
            c = 0
            while c < y:
                v = ""
                v = arraynew[c]
                c += 1
                v = v + " " + arraynew[c]
                c += 1
                v = v + " " + arraynew[c]
                c += 1
                self.Text8.insert(1.0, v + "\n")

            with open("seq", "w") as f:
                f.write(self.Text8.get(1.0, tk.END))
                self.Text8.delete(1.0, tk.END)
                f.close()
                print("7. Done")
                matcingstring()

        def matcingstring():
            print("8. Matching String")
            f1x = list()
            f2x = list()
            with open("loop1", "r") as f1:
                with open("seq", "r") as f2:
                    with open('match', 'w+') as outfile:
                        data = f1.read().replace('}', '')
                        dats = data.replace('{', '')
                        dats = dats.splitlines()
                        seqa = f2.read().splitlines()
                        f1.close()
                        f2.close()
                        for line in dats:
                            f1x.append(line)
                        for line in seqa:
                            f2x.append(line)
                        for element in f2x:
                            for element2 in f1x:
                                if element == element2:
                                    outfile.write(element + "\n")

                    outfile.close()
                    print("8. Done")
                    loopmeaning()

        def corecttest():
            with open("match", "r") as maith:
                d = maith.read().replace('"', "")
                d = d.replace('[', '')
                d = d.replace(']', '')
                d = d.replace('{', '')
                d = d.replace('}', '')
                d = d.replace("'", '')
                print("corrt")
                print(d)
                maith.close()
            with open("match", "w") as mct:
                mct.write(d)
                mct.close()
                loopmeaning()

        def loopmeaning():
            print("9. Loop Meaning")
            with open("loop_find", "w") as lowrite:
                with open("loop1", 'r') as f1:
                    data = f1.read().replace('}', '')
                    dats = data.replace('{', '')
                    dats = dats.splitlines()
                    for line in dats:
                        print(line)
                        if "while" in line:
                            x = line + "\n"
                            print(x)
                            lowrite.write(x)
                            lowrite.close()
                            f1.close()
                            print("9. Done")
            loopinde()

        def comparingloop():
            print("10. Comparing Loop")
            wr = ""
            with open("loop_find", "r") as lowrite:
                x = lowrite.read().split()
                with open("match", "r") as matches:
                    matche = matches.read().replace("[", "").split()
                    arraynew = np.asanyarray(matche)
                    print(x)
                    print(matche)
                    for word in x:
                        for words in matche:
                            if word in words:
                                wr = word
                                j = np.where(arraynew == wr)
                                print(j)
                                h = j[0]
                                print(j[0])
                                print(h)
                                h += 2
                                u = arraynew[h]
                                lowrite.close()
                                matches.close()
                                arrayfianlreplace = np.asanyarray(x)
                                for word in arrayfianlreplace:
                                    if wr == word:
                                        d = np.where(arrayfianlreplace == word)
                                        h = d[0]
                                        arrayfianlreplace[h] = u
                                with open("replacedlooop", "w") as fe:
                                    self.Text8.insert(1.0, arrayfianlreplace)
                                    fe.write(self.Text8.get(1.0, tk.END))
                                    fe.close()
                print("10. Done")

        def loopinde():
            print("11. Loopinde")
            condi = ""
            with open("loop1", "r") as linde:
                x = linde.read().split()
                arrayy = np.asanyarray(x)
                for i in range(len(x)):
                    if "+=" == arrayy[i]:
                        condi = "+"
                for i in range(len(x)):
                    if condi == "":
                        if "-=" == arrayy[i]:
                            condi = "-"
                with open("condie", "w") as  coni:
                    coni.write(condi)
                    coni.close()
                    print("11. Done")
                    loopcondition()

        def loopcondition():
            print("12. Loop Condition")
            with open("loop1", "r") as linde:
                with open("condie", "r") as repl:
                    data = linde.read().replace('}', '')
                    dats = data.replace('{', '')
                    x = dats.split()
                    y = repl.readline()
                    y = y + "="
                    arrayay = np.asanyarray(x)
                    ce = np.where(arrayay == y)
                    h = ce[0]
                    h += 1
                    varie = arrayay[h]
                    with open("match", "r") as matt:
                        daa = matt.read().replace('}', '')
                        daas = daa.replace('{', '')
                        va = daas.split()
                        arvaria4 = np.asanyarray(va)
                    with open("equal", "r") as mat:
                        da = mat.read().replace('}', '')
                        das = da.replace('{', '')
                        v = das.split()
                        arvari6 = np.asanyarray(v)
                        x = set(arvaria4).difference(arvari6)
                        print(x)
                        self.Text8.delete(1.0, tk.END)
                        self.Text8.insert(1.0, x)
                        with open("variea", "w") as var:
                            var.write(self.Text8.get(1.0, tk.END))
                            self.Text8.delete(1.0, tk.END)
                            var.close()
                            print("12. Done")
                            loopst()

        def loopst():
            print("13. Loop ST")
            with open("variea", "r") as vari:
                x = vari.read()
                x = x.replace("{", "")
                x = x.replace("}", "")
                x = x.replace("'", "")
                y = x.replace(",", "")
                y = y.split()
                arew = np.asanyarray(y)
                d = len(arew)

                with open("match", "r") as matt:
                    daa = matt.read().replace('}', '')
                    daas = daa.replace('{', '')
                    va = daas.split()
                    arv = np.asanyarray(va)
                    i = 0
                    vao = ""
                    va = ""
                    v = ""
                    while i < d:
                        s = arew[i]
                        xx = np.where(arv == s)
                        xi = xx[0]
                        vao = arv[xi]
                        print(vao)
                        xi -= 1
                        va = arv[xi]
                        print(va)
                        xi -= 1
                        v = arv[xi]
                        print(v)
                        i += 1

                with open("start", "w") as ini:
                    reser = np.asarray(vao)
                    self.Text8.insert(1.0, reser[0])
                    ini.write(self.Text8.get(1.0, tk.END))
                    ini.close()
                    self.Text8.delete(1.0, tk.END)
                    incvalue()

        def incvalue():
            with open("condie", "r") as condi:
                inc = condi.read()
                with open("loop1", "r") as linde:
                    x = linde.read().split()
                    arrayy = np.asanyarray(x)
                    condi.close()
                    linde.close()
                    h = ""
                if inc == "+":
                    val = inc + "="
                    c = np.where(arrayy == val)
                    f = c[0]
                    f += 1
                    h = arrayy[f]
                    self.Text8.insert(1.0, h)
                    self.Text8.insert(1.0, val)

                if inc == "-":
                    vl = inc + "="
                    j = np.where(arrayy == vl)
                    k = j[0]
                    k += 1
                    h = arrayy[k]
                    self.Text8.insert(1.0, h)
                    self.Text8.insert(1.0, vl)

            with open("incval", "w") as ind:
                ind.write(self.Text8.get(1.0, tk.END))
                ind.close()
                self.Text8.delete(1.0, tk.END)
                matchwhiletest()

        def matchwhiletest():
            with open("loop_find", "r") as file:
                x = file.read()
                arr = np.asanyarray(re.findall(r'-?\d+', x))
                for i in range(len(arr)):
                    o = arr[i] + ":"
                    if o in x:
                        h = re.findall(r'-?\d+', o)
                        self.Text8.insert(1.0, h)
                        with open("true", "w") as tru:
                            tru.write(self.Text8.get(1.0, tk.END))
                            tru.close()
                            self.Text8.delete(1.0, tk.END)
            Loopcreation()

        def Loopcreation():
            print("Loop Creation")
            self.Text9.delete(1.0, tk.END)
            with open("start", "r") as ste:
                x = ste.read()
                x = x.replace("[", "").replace("]", "").replace("'", "")
                newx = np.asarray(x)
            with open("incval", "r") as invl:
                y = invl.read()
                y = y.replace("[", "").replace("]", "").replace("'", "").replace("=", " ")
                y = y.split()
                print(y)
                arr = np.asanyarray(y)
                a1 = int(x)
                a2 = int(arr[1])
                a3 = arr[0]
                a3 = a3 + arr[1]
                a3 = int(a3)
                print(a3)
                print(a1)
                print(a2)
                o = 0
                xo = 0

                if "+" in arr:
                    t = a1
                    while o < 12000:
                        self.Text9.insert(1.0, t)
                        self.Text9.insert(1.0, " ")
                        t = t + a2
                        print(o)
                        o += 1

                if "-" in arr:
                    t = a1
                    while o < 12000:
                        print(o)
                        self.Text9.insert(1.0, t)
                        self.Text9.insert(1.0, " ")
                        t = t + a3
                        o += 1

            with open("result", "w") as res:
                res.write(self.Text9.get(1.0, tk.END))
                self.Text9.delete(1.0, tk.END)
                res.close()
                findtheeqaution()

        def findtheeqaution():
            with open("loop_find", "r") as file:
                x = file.read().split()
                eql = np.asanyarray(x)
                vx = ""

                if "!=" in eql:
                    vx = "!="

                if "==" in eql:
                    vx = "=="

                if ">" in eql:
                    vx = ">"

                if "<" in eql:
                    vx = "<"

            self.Text9.insert(1.0, vx)
            with  open("eqlsign", "w") as eqlsi:
                eqlsi.write(self.Text9.get(1.0, tk.END))
                eqlsi.close()
                resultmatch()

        def resultmatch():
            with open("result", "r") as resu:
                x = resu.read().split()
                arrayresult = np.asanyarray(x)
                with open("true", "r") as tru:
                    y = tru.read().split()
                    arrayresult1 = np.asanyarray(y)
                    print(arrayresult1)
                    with open("eqlsign", "r") as condi:
                        z = condi.read()
            print(arrayresult)
            print(arrayresult1)
            print(z)
            print("_____________")

            if ">" in z:
                d = int(arrayresult1[0])
                h = 0
                print(d)
                for i in range(len(arrayresult)):
                    g = int(arrayresult[i])
                    if g > d:
                        h += 1
                        break
                if h == 1:
                    self.Text9.insert(1.0, "loop will terminate")
                if h == 0:
                    self.Text9.insert(1.0, "loop will not terminate")

            if '<' in z:
                d = int(arrayresult1[0])
                g = int(arrayresult[0])
                print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa d ", d)
                print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa d ", g)
                if g < d:
                    self.Text9.insert(1.0, "loop will not run")
                d = int(arrayresult1[0])
                h = 0
                for i in range(len(arrayresult)):
                    g = int(arrayresult[i])
                    if g < d:
                        h += 1
                        break
                if h == 1:
                        self.Text9.insert(1.0,"loop will terminate")
                if h == 0:
                    self.Text9.insert(1.0,"loop will not terminate")

            if "==" in z:
                d = arrayresult1[0]
                x = np.where(arrayresult == d)
                with open("plufinal", "w") as plu:
                    plu.write(str(arrayresult[x]))
                    plu.close()
                with open("plufial", "w") as plux:
                    plux.write(str(d))
                    plux.close()
                with open("plufinal", "r") as pu:
                    sd = pu.read().replace("[", "").replace("]", "").replace("'", "")
                    print("sd =", sd)
                with open("plufial", "r") as pux:
                    sdx = pux.read().replace("[", "").replace("]", "").replace("'", "")
                print("sdx ", sdx)
                if sdx == sd:
                    self.Text9.insert(1.0,"loop will terminate")
                else:
                    self.Text9.insert(1.0,"loop will not terminate")

            if "!=" in z:
                d = arrayresult1[0]
                x = np.where(arrayresult == d)
                with open("plufnal", "w") as plu:
                    plu.write(str(arrayresult[x]))
                    plu.close()
                with open("pluial", "w") as plux:
                    plux.write(str(d))
                    plux.close()
                with open("plufnal", "r") as pu:
                    sd = pu.read().replace("[", "").replace("]", "").replace("'", "")
                print("sd =", sd)
                with open("pluial", "r") as pux:
                    sdx = pux.read().replace("[", "").replace("]", "").replace("'", "")
                    if sdx == sd:
                        self.Text9.insert(1.0,"loop will terminate")
                    else:
                        self.Text9.insert(1.0,"loop will not terminate")

            print("Logical Loop Detecion Time = "+str(time.time()-looptime))

        vartime = ""
        def variable():
            vartime = time.time()
            x = self.Text1.get(1.0, tk.END)
            with open("mainflex", "w") as maf:
                maf.write(x)
                maf.close()
            with open("mainflex", "r") as f:
                f = f.read().splitlines()
                for line in f:
                    if "while" not in line:
                        if "+=" not in line:
                            if "-=" not in line:
                                if "print" not in line:
                                    if "." not in line:
                                        if "," not in line:
                                            if "\\" not in line:
                                                if "/" not in line:
                                                    self.Text2.insert(1.0,line+" ")

            with open("varibleex","w") as varia:
                varia.write(self.Text2.get(1.0,tk.END))
                varia.close()
                self.Text2.delete(1.0,tk.END)

            with open("varibleex","r") as vria:
                vx = vria.read().replace("=",'').split()
                for word in vx:
                    if word.isdigit()== True:
                        print(" ")
                    else:
                        self.Text2.insert(1.0,"\n "+word+"\n")


            with open ("lonevariable","w") as aloneva:
                aloneva.write(self.Text2.get(1.0,tk.END))
                aloneva.close()
                self.Text2.delete(1.0, tk.END)

            exline = set()
            with open ("lonevariable","r") as alonea:
                alonea = alonea.read().replace("\n","").split()
                for line in alonea:
                    if line in exline:
                        line
                    else:
                        exline.add(line)
                        self.Text2.insert(1.0,line+" \n")


            with open ("inalvariables","w") as finalvariles:
                finalvariles.write(self.Text2.get(1.0,tk.END))
                finalvariles.close()
                self.Text2.delete(1.0,tk.END)

            with open ("inalvariables","r") as fnalva:
                fnalva = fnalva.read().replace(' ',"").split()
            with open ("mainflex","r") as fna:
                fna = fna.read().splitlines()
                for word in fnalva:
                    for line in fna:
                        if word in line:
                            self.Text2.insert(1.0,line+"\n")

            with open("resultvariable","w") as resfvar:
                resfvar.write(self.Text2.get(1.0,tk.END))
                resfvar.close()

            with open("inalvariables","r") as finalvaris:
                finalvaris = finalvaris.read().split()
                variables = np.asarray(finalvaris)

            with open("resultvariable","r") as resvar:
                self.Text2.delete(1.0,tk.END)
                resvar = resvar.read().splitlines()
                resultarr = np.asarray(resvar)
                for word in variables:
                    for line in resultarr:
                        if word in line:
                            self.Text2.insert(1.0, word+" ")

            with open("fresultvariable","w") as resar:
                resar.write(self.Text2.get(1.0,tk.END))
                resar.close()
                self.Text2.delete(1.0,tk.END)
            with open("fresultvariable","r") as file:
                wordcount = Counter(file.read().split())
                self.Text2.insert(1.0,wordcount)

            with open ("singlevari","w") as singlevar:
                singlevar.write(self.Text2.get(1.0,tk.END))
                singlevar.close()
                self.Text2.delete(1.0,tk.END)

            with open ("singlevari","r") as singleva:
                singleva = singleva.read().replace("Counter","").replace("(","").replace(")","").replace("'"," ").replace("["," ").replace("]"," ").replace("{","").replace("}","").replace(":","").replace(",","").split()
                self.Text2.insert(1.0,singleva)
            with open ("sinlevari","w") as sinlevar:
                sinlevar.write(self.Text2.get(1.0,tk.END))
                sinlevar.close()
                self.Text2.delete(1.0,tk.END)
            with open ("sinlevari","r") as sinle:
                single = np.asarray(singleva)
                for i in range(len(single)):
                    if single[i] == "1":
                        self.Text2.insert(1.0, single[i-1]+" \n")
            print("Unused Varible Detection Time = "+str(time.time()-vartime))

        astime = 0
        def reassigning():
            x = self.Text1.get(1.0, tk.END)
            with open("mainfilex", "w") as maf:
                maf.write(x)
                maf.close()
            with open("mainfilex", "r") as f:
                f = f.read().splitlines()
                for line in f:
                    if "while" not in line:
                        if "+=" not in line:
                            if "-=" not in line:
                                if "print" not in line:
                                    if "." not in line:
                                        if "," not in line:
                                            if "\\" not in line:
                                                if "/" not in line:
                                                    self.Text8.insert(1.0, line + " ")

            with open("variableex", "w") as varia:
                varia.write(self.Text8.get(1.0, tk.END))
                varia.close()
                self.Text8.delete(1.0, tk.END)

            with open("variableex", "r") as vria:
                vx = vria.read().replace("=", '').split()
                for word in vx:
                    if word.isdigit() == True:
                        print(" ")
                    else:
                        self.Text8.insert(1.0, "\n " + word + "\n")

            with open("alonevariable", "w") as aloneva:
                aloneva.write(self.Text8.get(1.0, tk.END))
                aloneva.close()
                self.Text8.delete(1.0, tk.END)

            exline = set()
            with open("alonevariable", "r") as alonea:
                alonea = alonea.read().replace("\n", "").split()
                for line in alonea:
                    if line in exline:
                        line
                    else:
                        exline.add(line)
                        self.Text8.insert(1.0, line + " \n")

            with open("finalvariables", "w") as finalvariles:
                finalvariles.write(self.Text8.get(1.0, tk.END))
                finalvariles.close()
                self.Text8.delete(1.0, tk.END)

            with open("finalvariables", "r") as fnalva:
                fnalva = fnalva.read().replace(' ', "").split()
            with open("mainfilex", "r") as fna:
                fna = fna.read().splitlines()
                for word in fnalva:
                    for line in fna:
                        if word in line:
                            self.Text8.insert(1.0, line + "\n")

            with open("resultofvariable", "w") as resfvar:
                resfvar.write(self.Text8.get(1.0, tk.END))
                resfvar.close()
                self.Text8.delete(1.0, tk.END)


            with open("finalvariables", "r") as finalvaris:
                finalvaris = finalvaris.read().split()
                redf = np.asarray(finalvaris)

            with open("resultofvariable", "r") as resvar:
                resvar = resvar.read().splitlines()
                resultarr = np.asarray(resvar)
                resultarrlen = len(resultarr)
                onelessresult = resultarrlen - 1

                for i in range(len(redf)):
                    f = 0
                    while f < onelessresult:
                        o = redf[i]
                        u = redf[i] + " = "
                        x = resultarr[f]
                        y = resultarr[f + 1]
                        if o in x and o in y:
                            msg = ("Current Testing ( " + o + " ) variable on " + y + " and " + x + ".\n")
                            self.Text8.insert(1.0,msg)
                        if o in x and u in y:
                            mssg = ("Operation Verifying on " + o + " variable between " + y + " and " + x + " lines.\n")
                            self.Text8.insert(1.0,mssg)
                        if u in x and u in y:
                            msssg = ("Variable Value is Reassigned without Operation applying between " + x + " and " + y + ".\n")
                            self.Text8.insert(1.0, msssg)
                        f += 1
            print("Reassigning Value Time = "+str(time.time()-astime))

        duptime = ''

        def duplicate():
            duptime = time.time()
            self.Text4.delete(1.0, tk.END)
            x = self.Text1.get(1.0, tk.END)
            with open("dupi", "w") as dupli:
                dupli.write(x)
                dupli.close()
            with open("dupi", "r") as dup:
                exline = set()
                for line in dup:
                    linel = line.lower()
                    if linel in exline:
                        self.Text4.insert(1.0, linel)
                    else:
                        exline.add(linel)
            print("Duplication Detection Time = "+str(time.time()-duptime))

        arraytime = 0
        def indexarray():
            arraytime = time.time()
            self.Text7.delete(1.0,tk.END)
            b = 0
            x = self.Text1.get(1.0, tk.END)
            with open("indexin", "w") as indx:
                indx.write(x)
                indx.close()
            with open("indexin") as infile, open("indexing", 'w') as outfile:
                for line in infile:
                    if not line.strip(): continue  # skip the empty line
                    outfile.write(line)
            with open("indexing", "r") as ind:
                x = ind.read().splitlines()
                for line in x:
                    if "print" in line:
                        y = line

            y = ""
            with open("indexing", "r") as ind:
                x = ind.read().splitlines()
                for line in x:
                    if "=" in line:
                        y = line
            with open("digit", "w") as dig:
                dig.write(y)
                dig.close()

            with open("digit", "r") as digx:
                gd = digx.read().replace("[", ' ').replace(",", ' ').replace("]", ' ')
                result = [int(d) for d in re.findall(r'-?\d+', gd)]
                arrass = np.asarray(result)
                val = len(arrass) - 1

            with open("indexing", "r") as indxx:
                dd = indxx.read().splitlines()
            for line in dd:
                if "print" in line:
                    result = [int(d) for d in re.findall(r'-?\d+', line)]
                    vbn = str(result)
            with open("pridigit", "w") as pri:
                pri.write(vbn)
                pri.close()

            with open("pridigit", "r") as prii:
                vbnh = prii.read().replace("[", " ").replace("]", " ")
                res = int(vbnh)
                val2 = val+1
                res2 = -val2
                stringaper = str(res)
            if "-" in stringaper:
                if res < res2:
                    msg = ("Reverse index Higher appeared than Range. " + "\n")
                    self.Text7.insert(1.0, msg)
                    mssg = "Index value starts from 0 to " + str(val) +" and Reversed Index -1 to "+str(res2)+ "\n"
                    self.Text7.insert(1.0, mssg)
                    b += 1

            if res > val:
                msg = "Index value is invalid and greater than maximum index in array" + "\n"
                self.Text7.insert(1.0, msg)
                mssg = "Index value starts from 0 to " + str(val) + " and Reversed Index -1 to " + str(res2) + "\n"
                self.Text7.insert(1.0, mssg)
                b += 1


            if b == 0:
                mssg = "Array Index is logical Error Free" + "\n"
                self.Text7.insert(1.0, mssg)
                mssg = "Index value starts from 0 to " + str(val) + " and Reversed Index -1 to " + str(res2) + "\n"
                self.Text7.insert(1.0, mssg)
            print("Array Index calculation Time = "+str(time.time()-arraytime))

        def comparingword():
            lineList = list()
            with open("mainfile", "w") as maf:
                maf.write(self.Text1.get(1.0, tk.END))
                maf.close()
            with open("mainfile", "r") as f:
                for line in f:
                    if "print" not in line:
                        lineList.append(line)

                self.Text9.insert(1.0, lineList)
                f.close()

                with open("loop1", "w") as file1:
                    file1.write(self.Text9.get(1.0, tk.END))
                    self.Text9.delete(1.0, tk.END)
                    file1.close()
                    print("1. Done")
            convert()

        def convert():
            print("2. Convert")
            with open('loop1', 'r') as f:
                data = f.read().replace('}', '')
                dats = data.replace('{', '')
                self.Text9.insert(1.0, dats)
                xc = dats.split()
                self.Text9.insert(1.0, xc)
                fxc = open("single", "w")
                fxc.write(self.Text9.get(1.0, tk.END))
                fxc.close()
                self.Text9.delete(1.0, tk.END)
                print("2. Done ")
                newtwo()

        def newtwo():
            print("3. New Two")
            with open("single", "r") as fg:
                a = fg.read().split()
                b = []
                for item in a:
                    if item not in b:
                        b.append(item)
                    else:
                        self.Text9.insert(1.0, item + " = ")
                        fxcx = open("equal", "w")
                        fxcx.write(self.Text9.get(1.0, tk.END))
                        fxcx.close()
                        break
                        print(item)
            self.Text9.delete(1.0, tk.END)
            with open('single', 'r') as f:
                data = f.read().split()
                self.Text9.insert(1.0, data)
                f.close()
                print("3. Done")
                matchvari()

        def matchvari():
            print("4. Match Variable")
            digitalnum = open("single", "r")
            dig = digitalnum.read()
            x = [int(s) for s in dig.split() if s.isdigit()]
            self.Text9.insert(1.0, x)
            fxcx = open("digi", "w")
            fxcx.write(self.Text9.get(1.0, tk.END))
            fxcx.close()
            self.Text9.delete(1.0, tk.END)
            print("4. Done")
            merging()

        def merging():
            print("5. Merging")
            with open("digi", "r") as digi:
                with open("equal", "r") as eqal:
                    x = digi.read().split()
                    y = eqal.read().splitlines()
                    print(x)
                    print(y)
                    xarr = np.asanyarray(x)
                    yarr = np.asanyarray(y)
                    for line in yarr:
                        for i in range(len(xarr)):
                            x = " " + line + xarr[i]
                            self.Text9.insert(1.0, x)
                with open("vari", "w") as f:
                    f.write(self.Text9.get(1.0, tk.END))
                    f.close()
                    self.Text9.delete(1.0, tk.END)
                print("5. Done")
            matchingvari()

        def matchingvari():
            print("6. Matching Varible")
            with open('vari', 'r') as f:
                data = f.read().replace('}', '')
                dats = data.replace('{', ' ')
                xc = dats.split()
                self.Text9.insert(1.0, xc)
                print(xc)
                f.close()
                with open('lineloop', 'w') as f:
                    f.write(self.Text9.get(1.0, tk.END))
                    f.close()
                    self.Text9.delete(1.0, tk.END)
                    print("6. Done")
                    lineloop()

        def lineloop():
            print("7. line loop ")
            with open("lineloop", "r") as f:
                data = f.read().split()
                arraynew = np.asanyarray(data)
                x = len(data)
                y = len(arraynew) - 1
            c = 0
            while c < y:
                v = ""
                v = arraynew[c]
                c += 1
                v = v + " " + arraynew[c]
                c += 1
                v = v + " " + arraynew[c]
                c += 1
                self.Text9.insert(1.0, v + "\n")

            with open("seq", "w") as f:
                f.write(self.Text9.get(1.0, tk.END))
                self.Text9.delete(1.0, tk.END)
                f.close()
                print("7. Done")
                matcingstring()

        def matcingstring():
            print("8. Matching String")
            f1x = list()
            f2x = list()
            with open("loop1", "r") as f1:
                with open("seq", "r") as f2:
                    with open('match', 'w+') as outfile:
                        data = f1.read().replace('}', '')
                        dats = data.replace('{', '')
                        dats = dats.splitlines()
                        seqa = f2.read().splitlines()
                        f1.close()
                        f2.close()
                        for line in dats:
                            f1x.append(line)
                        for line in seqa:
                            f2x.append(line)
                        for element in f2x:
                            for element2 in f1x:
                                if element == element2:
                                    outfile.write(element + "\n")

                    outfile.close()
                    print("8. Done")
                    loopmeaning()

        def corecttest():
            with open("match", "r") as maith:
                d = maith.read().replace('"', "")
                d = d.replace('[', '')
                d = d.replace(']', '')
                d = d.replace('{', '')
                d = d.replace('}', '')
                d = d.replace("'", '')
                print("corrt")
                print(d)
                maith.close()
            with open("match", "w") as mct:
                mct.write(d)
                mct.close()
                loopmeaning()

        def loopmeaning():
            print("9. Loop Meaning")
            with open("loop_find", "w") as lowrite:
                with open("loop1", 'r') as f1:
                    data = f1.read().replace('}', '')
                    dats = data.replace('{', '')
                    dats = dats.splitlines()
                    for line in dats:
                        print(line)
                        if "while" in line:
                            x = line + "\n"
                            print(x)
                            lowrite.write(x)
                            lowrite.close()
                            f1.close()
                            print("9. Done")
            loopinde()

        itrtime = 0
        def comparingloop():
            itrtime = time.time()
            print("10. Comparing Loop")
            wr = ""
            with open("loop_find", "r") as lowrite:
                x = lowrite.read().split()
                with open("match", "r") as matches:
                    matche = matches.read().replace("[", "").split()
                    arraynew = np.asanyarray(matche)
                    print(x)
                    print(matche)
                    for word in x:
                        for words in matche:
                            if word in words:
                                wr = word
                                j = np.where(arraynew == wr)
                                print(j)
                                h = j[0]
                                print(j[0])
                                print(h)
                                h += 2
                                u = arraynew[h]
                                lowrite.close()
                                matches.close()
                                arrayfianlreplace = np.asanyarray(x)
                                for word in arrayfianlreplace:
                                    if wr == word:
                                        d = np.where(arrayfianlreplace == word)
                                        h = d[0]
                                        arrayfianlreplace[h] = u
                                with open("replacedlooop", "w") as fe:
                                    self.Text9.insert(1.0, arrayfianlreplace)
                                    fe.write(self.Text9.get(1.0, tk.END))
                                    fe.close()
                print("10. Done")

        def loopinde():
            print("11. Loopinde")
            condi = ""
            with open("loop1", "r") as linde:
                x = linde.read().split()
                arrayy = np.asanyarray(x)
                for i in range(len(x)):
                    if "+=" == arrayy[i]:
                        condi = "+"
                for i in range(len(x)):
                    if condi == "":
                        if "-=" == arrayy[i]:
                            condi = "-"
                with open("condie", "w") as  coni:
                    coni.write(condi)
                    coni.close()
                    print("11. Done")
                    loopcondition()

        def loopcondition():
            print("12. Loop Condition")
            with open("loop1", "r") as linde:
                with open("condie", "r") as repl:
                    data = linde.read().replace('}', '')
                    dats = data.replace('{', '')
                    x = dats.split()
                    y = repl.readline()
                    y = y + "="
                    arrayay = np.asanyarray(x)
                    ce = np.where(arrayay == y)
                    h = ce[0]
                    h += 1
                    varie = arrayay[h]
                    with open("match", "r") as matt:
                        daa = matt.read().replace('}', '')
                        daas = daa.replace('{', '')
                        va = daas.split()
                        arvaria4 = np.asanyarray(va)
                    with open("equal", "r") as mat:
                        da = mat.read().replace('}', '')
                        das = da.replace('{', '')
                        v = das.split()
                        arvari6 = np.asanyarray(v)
                        x = set(arvaria4).difference(arvari6)
                        print(x)
                        self.Text9.delete(1.0, tk.END)
                        self.Text9.insert(1.0, x)
                        with open("variea", "w") as var:
                            var.write(self.Text9.get(1.0, tk.END))
                            self.Text9.delete(1.0, tk.END)
                            var.close()
                            print("12. Done")
                            loopst()

        def loopst():
            print("13. Loop ST")
            with open("variea", "r") as vari:
                x = vari.read()
                x = x.replace("{", "")
                x = x.replace("}", "")
                x = x.replace("'", "")
                y = x.replace(",", "")
                y = y.split()
                arew = np.asanyarray(y)
                d = len(arew)

                with open("match", "r") as matt:
                    daa = matt.read().replace('}', '')
                    daas = daa.replace('{', '')
                    va = daas.split()
                    arv = np.asanyarray(va)
                    i = 0
                    vao = ""
                    va = ""
                    v = ""
                    while i < d:
                        s = arew[i]
                        xx = np.where(arv == s)
                        xi = xx[0]
                        vao = arv[xi]
                        print(vao)
                        xi -= 1
                        va = arv[xi]
                        print(va)
                        xi -= 1
                        v = arv[xi]
                        print(v)
                        i += 1

                with open("start", "w") as ini:
                    reser = np.asarray(vao)
                    self.Text9.insert(1.0, reser[0])
                    ini.write(self.Text9.get(1.0, tk.END))
                    ini.close()
                    self.Text9.delete(1.0, tk.END)
                    incvalue()

        def incvalue():
            with open("condie", "r") as condi:
                inc = condi.read()
                with open("loop1", "r") as linde:
                    x = linde.read().split()
                    arrayy = np.asanyarray(x)
                    condi.close()
                    linde.close()
                    h = ""
                if inc == "+":
                    val = inc + "="
                    c = np.where(arrayy == val)
                    f = c[0]
                    f += 1
                    h = arrayy[f]
                    self.Text9.insert(1.0, h)
                    self.Text9.insert(1.0, val)

                if inc == "-":
                    vl = inc + "="
                    j = np.where(arrayy == vl)
                    k = j[0]
                    k += 1
                    h = arrayy[k]
                    self.Text9.insert(1.0, h)
                    self.Text9.insert(1.0, vl)

            with open("incval", "w") as ind:
                ind.write(self.Text9.get(1.0, tk.END))
                ind.close()
                self.Text9.delete(1.0, tk.END)
                matchwhiletest()

        def matchwhiletest():
            with open("loop_find", "r") as file:
                x = file.read()
                arr = np.asanyarray(re.findall(r'-?\d+', x))
                for i in range(len(arr)):
                    o = arr[i] + ":"
                    if o in x:
                        h = re.findall(r'-?\d+', o)
                        self.Text9.insert(1.0, h)
                        with open("true", "w") as tru:
                            tru.write(self.Text9.get(1.0, tk.END))
                            tru.close()
                            self.Text9.delete(1.0, tk.END)
            Loopcreation()

        def Loopcreation():
            print("Loop Creation")
            self.Text9.delete(1.0, tk.END)
            with open("start", "r") as ste:
                x = ste.read()
                x = x.replace("[", "").replace("]", "").replace("'", "")
                newx = np.asarray(x)
            with open("incval", "r") as invl:
                y = invl.read()
                y = y.replace("[", "").replace("]", "").replace("'", "").replace("=", " ")
                y = y.split()
                print(y)
                arr = np.asanyarray(y)
                a1 = int(x)
                a2 = int(arr[1])
                a3 = arr[0]
                a3 = a3 + arr[1]
                a3 = int(a3)
                print(a3)
                print(a1)
                print(a2)
                o = 0
                xo = 0

                if "+" in arr:
                    t = a1
                    while o < 12000:
                        self.Text9.insert(1.0, t)
                        self.Text9.insert(1.0, " ")
                        t = t + a2
                        o += 1

                if "-" in arr:
                    t = a1
                    while o < 12000:
                        self.Text9.insert(1.0, t)
                        self.Text9.insert(1.0, " ")
                        t = t + a3
                        o += 1

            with open("result", "w") as res:
                res.write(self.Text9.get(1.0, tk.END))
                self.Text9.delete(1.0, tk.END)
                res.close()
                findtheeqaution()

        def findtheeqaution():
            with open("loop_find", "r") as file:
                x = file.read().split()
                eql = np.asanyarray(x)
                vx = ""

                if "!=" in eql:
                    vx = "!="

                if "==" in eql:
                    vx = "=="

                if ">" in eql:
                    vx = ">"

                if "<" in eql:
                    vx = "<"

            self.Text9.insert(1.0, vx)
            with  open("eqlsign", "w") as eqlsi:
                eqlsi.write(self.Text9.get(1.0, tk.END))
                eqlsi.close()
                resultmatch()


        def resultmatch():
            self.Text9.delete(1.0, tk.END)
            with open("result", "r") as resu:
                x = resu.read().split()
                arrayresult = np.asanyarray(x)
                with open("true", "r") as tru:
                    y = tru.read().split()
                    arrayresult1 = np.asanyarray(y)
                    print(arrayresult1)
                    with open("eqlsign", "r") as condi:
                        z = condi.read()


            if ">" in z:
                with open("start", "r") as ste:
                    xe = ste.read()
                    print(xe)
                    xe = int(xe)
                d = int(arrayresult1[0]) #testvalue
                print(d)
                g = int(arrayresult[0]) #inc value
                print(g)
                if xe > d:
                    self.Text9.insert(1.0, "loop will run \n")
                if xe == d:
                    self.Text9.insert(1.0, "loop will not run \n")
                elif g < d and g > 0:
                    self.Text9.insert(1.0, "loop will not run \n")
                elif g > d:
                    self.Text9.insert(1.0, "loop will terminate \n")
                elif g > 0 and 0 > d:
                    self.Text9.insert(1.0, "Loop will never terminated \n")
                else:
                    d = int(arrayresult1[0])
                    h = 0
                    for i in range(len(arrayresult)):
                        g = int(arrayresult[i])
                        if g > d:
                            h += 1
                            break
                    if h == 1:
                        self.Text9.insert(1.0, "loop will terminate \n")
                    if h == 0:
                        self.Text9.insert(1.0, "loop will not terminate \n")
                print(">_________________________________________________")

            if '<' in z:
                with open("start", "r") as ste:
                    xe = ste.read()
                    xe = int(xe)
                d = int(arrayresult1[0])
                g = int(arrayresult[11999])
                if xe < d:
                    self.Text9.insert(1.0, "loop will run \n")
                if xe == d:
                    self.Text9.insert(1.0, "loop will not run \n")
                if g > d:
                    self.Text9.insert(1.0, "loop will terminate \n")
                if g < d:
                    self.Text9.insert(1.0, "loop will not terminate \n")
                if g > 0 and 0 >  d:
                    self.Text9.insert(1.0, "Loop will never Run \n")
                else:
                    d = int(arrayresult1[0])
                    h = 0
                    for i in range(len(arrayresult)):
                        g = int(arrayresult[i])
                        if g < d:
                            h += 1
                            break
                    if h == 0:
                        self.Text9.insert(1.0,"loop will terminate \n")
                    if h == 1:
                        self.Text9.insert(1.0,"loop will not terminate \n")

            if "==" in z:
                with open("start", "r") as ste:
                    xe = ste.read()
                    xe = int(xe)
                with open("true", "r") as tru:
                    y = tru.read()
                    y = int(y)
                if y == xe:
                    self.Text9.insert(1.0, "Loop will run once.")
                else:
                    self.Text9.insert(1.0, "Loop will not run because its running value not match with test value.")

            if "!=" in z:
                with open("start", "r") as ste:
                    xe = ste.read()
                    xe = int(xe)
                with open("true", "r") as tru:
                    y = tru.read()
                    y = int(y)
                if y == xe:
                    self.Text9.insert(1.0, "Loop will not run.")

                d = arrayresult1[0]
                x = np.where(arrayresult == d)
                with open("plufnal", "w") as plu:
                    plu.write(str(arrayresult[x]))
                    plu.close()
                with open("pluial", "w") as plux:
                    plux.write(str(d))
                    plux.close()
                with open("plufnal", "r") as pu:
                    sd = pu.read().replace("[", "").replace("]", "").replace("'", "")
                print("sd =", sd)
                with open("pluial", "r") as pux:
                    sdx = pux.read().replace("[", "").replace("]", "").replace("'", "")
                    self.Text9.delete(1.0,tk.END)
                    if sdx == sd:
                        self.Text9.insert(1.0,"loop will terminate.")
                    else:
                        self.Text9.insert(1.0,"loop will not terminate.")
            print("12000  Iteration Loop Teermination Time = "+str(time.time()-itrtime))

        arrtime = 0
        def findingsha():
            arrtime = time.time()
            x = self.Text1.get(1.0, tk.END)
            with open("fingsha", "w") as findse:
                findse.write(x)
                findse.close()
            with open("fingsha", "r") as f:
                for line in f:
                    if "/" in line:
                        self.Text6.insert(1.0, line)
                f.close()

            with open("shalash", "w") as file1:
                file1.write(self.Text6.get(1.0, tk.END))
                file1.close()
                self.Text6.delete(1.0, tk.END)
                findedsha()

        def findedsha():
            with open("shalash", "r") as sha:
                sh = sha.read().replace(" ", '').replace("=", "=(").replace("/", ")/")
            with open("parent", "w") as par:
                par.write(sh)
                par.close()
            readingfile()

        def readingfile():
            with open("fullstate", "w") as fulst:
                fulst.write(self.Text1.get(1.0, tk.END))
                fulst.close()
            with open("fullstate", "r") as fsl:
                xx = fsl.read()
                for line in xx:
                    if "/" not in line:
                        xx = xx
            xy = [int(s) for s in xx.split() if s.isdigit()]
            arradd = np.asanyarray(xy)
            z = sum(arradd)
            l = len(arradd)
            x = z / len(arradd)
            self.Text6.insert(1.0, "Accurate Average is = " + str(x))
            self.Text6.insert(1.0, "Numbers Counts = " + str(l) + "\n")
            self.Text6.insert(1.0, "Total Sum is = " + str(z) + "\n")
            self.Text6.insert(1.0," Input Values = " + str(arradd)+"\n")
            print("Average Calculation Time = "+str(time.time()-arrtime))

        logtime = 0
        def infinityloop():
            logtime = time.time()
            x = self.Text1.get(1.0, tk.END)
            self.Text9.delete(1.0, tk.END)
            lineList = list()
            with open("mainfle", "w") as maf:
                maf.write(self.Text1.get(1.0, tk.END))
                maf.close()
                with open("mainfle", "r") as f:
                    for line in f:
                        if "print" not in line:
                            lineList.append(line)
                    self.Text10.insert(1.0, lineList)
                    f.close()
                with open("lop1", "w") as file1:
                    file1.write(self.Text10.get(1.0, tk.END))
                    self.Text10.delete(1.0, tk.END)
                    file1.close()
                    print("1. Done")
                    conver()


        def conver():
            print("2. Convert")
            with open('lop1', 'r') as f:
                data = f.read().replace('}', '')
                dats = data.replace('{', '')
                self.Text10.insert(1.0, dats)
                xc = dats.split()
                self.Text9.insert(1.0, xc)
                fxc = open("sigle", "w")
                fxc.write(self.Text9.get(1.0, tk.END))
                fxc.close()
                self.Text9.delete(1.0, tk.END)
                print("2. Done ")
                newtw()

        def newtw():
            print("3. New Two")
            with open("sigle", "r") as fg:
                a = fg.read().split()
                b = []
                for item in a:
                    if item not in b:
                        b.append(item)
                    else:
                        self.Text9.insert(1.0, item + " = ")
                        fxcx = open("equl", "w")
                        fxcx.write(self.Text9.get(1.0, tk.END))
                        fxcx.close()
                        break
                        print(item)
            self.Text9.delete(1.0, tk.END)
            with open('sigle', 'r') as f:
                data = f.read().split()
                self.Text9.insert(1.0, data)
                f.close()
                print("3. Done")
                mathvari()

        def mathvari():
            print("4. Match Variable")
            digitalnum = open("sigle", "r")
            dig = digitalnum.read()
            x = [int(s) for s in dig.split() if s.isdigit()]
            self.Text9.insert(1.0, x)
            fxcx = open("dii", "w")
            fxcx.write(self.Text9.get(1.0, tk.END))
            fxcx.close()
            self.Text9.delete(1.0, tk.END)
            print("4. Done")
            meging()

        def meging():
            print("5. Merging")
            with open("dii", "r") as digi:
                with open("equl", "r") as eqal:
                    x = digi.read().split()
                    y = eqal.read().splitlines()
                    print(x)
                    print(y)
                    xarr = np.asanyarray(x)
                    yarr = np.asanyarray(y)
                    for line in yarr:
                        for i in range(len(xarr)):
                            x = " " + line + xarr[i]
                            self.Text10.insert(1.0, x)
                with open("varri", "w") as f:
                    f.write(self.Text10.get(1.0, tk.END))
                    f.close()
                    self.Text10.delete(1.0, tk.END)
                print("5. Done")
            mtchingvari()

        def mtchingvari():
            print("6. Matching Varible")
            with open('varri', 'r') as f:
                data = f.read().replace('}', '')
                dats = data.replace('{', ' ')
                xc = dats.split()
                self.Text9.insert(1.0, xc)
                print(xc)
                f.close()
                with open('linloop', 'w') as f:
                    f.write(self.Text9.get(1.0, tk.END))
                    f.close()
                    self.Text9.delete(1.0, tk.END)
                    print("6. Done")
                    linelop()

        def linelop():
            with open("linloop", "r") as f:
                data = f.read().split()
                arraynew = np.asanyarray(data)
                x = len(data)
                y = len(arraynew) - 1
            c = 0
            while c < y:
                v = ""
                v = arraynew[c]
                c += 1
                v = v + " " + arraynew[c]
                c += 1
                v = v + " " + arraynew[c]
                c += 1
                self.Text9.insert(1.0, v + "\n")

            with open("seqa", "w") as f:
                f.write(self.Text9.get(1.0, tk.END))
                self.Text9.delete(1.0, tk.END)
                f.close()
                print("7. Done")
                matcingtring()

        def matcingtring():
            print("8. Matching String")
            f1x = list()
            f2x = list()
            with open("lop1", "r") as f1:
                with open("seqa", "r") as f2:
                    with open('matcha', 'w') as outfile:
                        data = f1.read().replace('}', '')
                        dats = data.replace('{', '')
                        dats = dats.splitlines()
                        seqa = f2.read().splitlines()
                        f1.close()
                        f2.close()
                        for line in dats:
                            f1x.append(line)
                        for line in seqa:
                            f2x.append(line)
                        for element in f2x:
                            for element2 in f1x:
                                if element == element2:
                                    outfile.write(element + "\n")

                    outfile.close()
                    print("8. Done")
                    oopmeaning()

        def oopmeaning():
            print("9. Loop Meaning")
            with open("loop_fin", "w") as lowrite:
                with open("lop1", 'r') as f1:
                    data = f1.read().replace('}', '')
                    dats = data.replace('{', '')
                    dats = dats.splitlines()
                    for line in dats:
                        print(line)
                        if "while" in line:
                            x = line + "\n"
                            print(x)
                            lowrite.write(x)
                            lowrite.close()
                            f1.close()
                            print("9. Done")
            loopnde()

        def loopnde():
            condi = ""
            with open("lop1", "r") as linde:
                x = linde.read().split()
                arrayy = np.asanyarray(x)
                for i in range(len(x)):
                    if "+=" == arrayy[i]:
                        condi = "+"
                for i in range(len(x)):
                    if condi == "":
                        if "-=" == arrayy[i]:
                            condi = "-"
                with open("conde", "w") as  coni:
                    coni.write(condi)
                    coni.close()
                    print("11. Done")
                    loopondition()

        def loopondition():
            print("12. Loop Condition")
            with open("lop1", "r") as linde:
                with open("conde", "r") as repl:
                    data = linde.read().replace('}', '')
                    dats = data.replace('{', '')
                    x = dats.split()
                    y = repl.readline()
                    y = y + "="
                    arrayay = np.asanyarray(x)
                    ce = np.where(arrayay == y)
                    h = ce[0]
                    h += 1
                    varie = arrayay[h]
                    with open("matcha", "r") as matt:
                        daa = matt.read().replace('}', '')
                        daas = daa.replace('{', '')
                        va = daas.split()
                        arvaria4 = np.asanyarray(va)
                    with open("equl", "r") as mat:
                        da = mat.read().replace('}', '')
                        das = da.replace('{', '')
                        v = das.split()
                        arvari6 = np.asanyarray(v)
                        x = set(arvaria4).difference(arvari6)
                        print(x)
                        self.Text9.delete(1.0, tk.END)
                        self.Text9.insert(1.0, x)
                        with open("varie", "w") as var:
                            var.write(self.Text9.get(1.0, tk.END))
                            self.Text9.delete(1.0, tk.END)
                            var.close()
                            print("12. Done")
                            loopt()

        def loopt():
            print("13. Loop ST")
            with open("varie", "r") as vari:
                x = vari.read()
                x = x.replace("{", "")
                x = x.replace("}", "")
                x = x.replace("'", "")
                y = x.replace(",", "")
                y = y.split()
                arew = np.asanyarray(y)
                d = len(arew)

                with open("matcha", "r") as matt:
                    daa = matt.read().replace('}', '')
                    daas = daa.replace('{', '')
                    va = daas.split()
                    arv = np.asanyarray(va)
                    i = 0
                    vao = ""
                    va = ""
                    v = ""
                    while i < d:
                        s = arew[i]
                        xx = np.where(arv == s)
                        xi = xx[0]
                        vao = arv[xi]
                        print(vao)
                        xi -= 1
                        va = arv[xi]
                        print(va)
                        xi -= 1
                        v = arv[xi]
                        print(v)
                        i += 1

                with open("starta", "w") as ini:
                    reser = np.asarray(vao)
                    self.Text9.insert(1.0, reser[0])
                    ini.write(self.Text9.get(1.0, tk.END))
                    ini.close()
                    self.Text9.delete(1.0, tk.END)
                    incalue()

        def incalue():
            with open("conde", "r") as condi:
                inc = condi.read()
                with open("lop1", "r") as linde:
                    x = linde.read().split()
                    arrayy = np.asanyarray(x)
                    condi.close()
                    linde.close()
                    h = ""
                if inc == "+":
                    val = inc + "="
                    c = np.where(arrayy == val)
                    f = c[0]
                    f += 1
                    h = arrayy[f]
                    self.Text9.insert(1.0, h)
                    self.Text9.insert(1.0, val)

                if inc == "-":
                    vl = inc + "="
                    j = np.where(arrayy == vl)
                    k = j[0]
                    k += 1
                    h = arrayy[k]
                    self.Text9.insert(1.0, h)
                    self.Text9.insert(1.0, vl)

            with open("incvl", "w") as ind:
                ind.write(self.Text9.get(1.0, tk.END))
                ind.close()
                self.Text9.delete(1.0, tk.END)
                matchhiletest()

        def matchhiletest():
            with open("loop_fin", "r") as file:
                x = file.read()
                arr = np.asanyarray(re.findall(r'-?\d+', x))
                for i in range(len(arr)):
                    o = arr[i] + ":"
                    if o in x:
                        h = re.findall(r'-?\d+', o)
                        self.Text9.insert(1.0, h)
                        print("true", h)
                        with open("tre", "w") as tru:
                            tru.write(self.Text9.get(1.0, tk.END))
                            tru.close()
                            self.Text9.delete(1.0, tk.END)
            fintheeqaution()

        def fintheeqaution():
            with open("loop_fin", "r") as file:
                x = file.read().split()
                eql = np.asanyarray(x)
                vx = ""

                if "!=" in eql:
                    vx = "!="

                if "==" in eql:
                    vx = "=="

                if ">" in eql:
                    vx = ">"

                if "<" in eql:
                    vx = "<"

            self.Text10.insert(1.0, vx)
            with  open("eqlign", "w") as eqlsi:
                eqlsi.write(self.Text10.get(1.0, tk.END))
                eqlsi.close()
                self.Text9.delete(1.0, tk.END)
            loopindection()

        def loopindection():
            with open("incvl", "r") as incra:
                incra = incra.read()
            with open("starta", "r") as start:
                start = start.read()
            with open("tre", "r") as true:
                true = true.read()
            with open("eqlign", "r") as eqlsign:
                eqlsign = eqlsign.read()
            self.Text10.delete(1.0, tk.END)
            incra = incra.replace("=", "").replace("'", "").replace("[", "").replace("]", "")
            incra = int(incra)
            start = int(start)
            true = int(true)
            xx = start + incra
            xxx = start + incra + incra

            if start == true:
                self.Text10.insert(1.0, "Starting Value Is Equal to Test Value \n")
                if start == true and "==" in eqlsign:
                    self.Text10.insert(1.0, "1) == Loop will run once but not goes to infinity\n")
                if start == true and "!=" in eqlsign:
                    self.Text10.insert(1.0, "2) != Loop will not run\n")
                if start == true and ">" in eqlsign:
                    self.Text10.insert(1.0, "3) > Loop will not run\n")
                if start == true and "<" in eqlsign:
                    self.Text10.insert(1.0, "4) < Loop will not run\n")
                if start > true and start == true:
                    self.Text10.insert(1.0, "5) > Loop will not goes to infinity\n")

            if xx == true:
                if xx == true and "==" in eqlsign:
                    self.Text10.insert(1.0, "7) == Loop will not run\n")
                if xx == true and "!=" in eqlsign:
                    self.Text10.insert(1.0, "8)!= Loop will run once\n")
                if xx > true and ">" in eqlsign:
                    self.Text10.insert(1.0, "9) > Loop will not run\n")
                if xx < true and "<" in eqlsign:
                    self.Text10.insert(1.0, "10) < Loop will run once\n")

            if xxx == true:
                if xxx == true and "==" in eqlsign:
                    self.Text10.insert(1.0, "7) == Loop will not run\n")
                if xxx == true and "!=" in eqlsign:
                    self.Text10.insert(1.0, "8)!= Loop will run once\n")
                if xxx > true and ">" in eqlsign:
                    self.Text10.insert(1.0, "9) > Loop will not run\n")
                if xxx < true and "<" in eqlsign:
                    self.Text10.insert(1.0, "10) < Loop will run once\n")

            if start == incra:
                s = start + incra
                if start != true and "==" in eqlsign:
                    self.Text10.insert(1.0, "11) == A Loop will not run\n")
                if start != true and "!=" in eqlsign:
                    self.Text10.insert(1.0, "11) != A Loop will not run\n")
                if (true % s) == 0 and  "!=" in eqlsign:
                    self.Text10.insert(1.0, "12) A != Loop will not goes to infinity\n")
                if (true % s) == 0 and "<" in eqlsign:
                    self.Text10.insert(1.0, "13) A Loop will not goes to infinity\n")
                if (true % s) == 0 and ">" in eqlsign:
                    self.Text10.insert(1.0, "14) A Loop will not goes to infinity\n")

                if (true % s) == 1 and "==" in eqlsign:
                    self.Text10.insert(1.0, "11)  B == A Loop will not goes to infinity\n")
                if (true % s) != 1 and "!=" in eqlsign:
                    self.Text10.insert(1.0, "12) B != Loop will goes to infinity\n")

                if (true % s) == 1 and "<" in eqlsign:
                    self.Text10.insert(1.0, "13) B Loop will not goes to infinity\n")
                if (true % s) == 1 and ">" in eqlsign:
                    self.Text10.insert(1.0, "14) B Loop will not run\n")

            if start and incra == 1:
                if start == true and "==" in eqlsign:
                    self.Text10.insert(1.0, "15) C == Loop will run once\n")
                if (true % 1) == 0 and "<" in eqlsign:
                    self.Text10.insert(1.0, "15) C  Loop will not goes to infinity\n")
                if (true % 1) == 0 and eqlsign == ">":
                    self.Text10.insert(1.0, "15) C  Loop will not goes to infinity\n")
                if (true % 1) == 0 and eqlsign == "!=":
                    self.Text10.insert(1.0, "16) C Loop will not goes to infinity\n")
            if start > 0 and incra < 0 and true < 0:
                    self.Text10.insert(1.0, "19) Loop will goes to infinity\n")
            if start > 0 and incra > 0 and true < 0:
                    self.Text10.insert(1.0, "20) Loop will goes to infinity\n")
            if start < 0 and incra > 0 and true < 0:
                    self.Text10.insert(1.0, "22) Loop will goes to infinity\n")
            if start > 0 and incra > 0 and true < 0:
                    self.Text10.insert(1.0, "23) Loop will goes to infinity\n")
            if start < 0 and incra < 0 and true > 0:
                    self.Text10.insert(1.0, "24) Loop will goes to infinity\n")
            print("Logical Infinity Detection Time = "+str(time.time()-logtime))

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.sub_menu = tk.Menu(top,tearoff=0)
        self.menubar.add_cascade(menu=self.sub_menu,
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                font="TkMenuFont",
                foreground="#000000",
                label="File")
        self.sub_menu.add_command(
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                font="TkMenuFont",
                foreground="#000000",
                label="New", command= newFile)
        self.sub_menu.add_command(
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                font="TkMenuFont",
                foreground="#000000",
                label="Open",command = openFile)
        self.sub_menu.add_command(
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                font="TkMenuFont",
                foreground="#000000",
                label="Save")
        self.sub_menu.add_command(
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                font="TkMenuFont",
                foreground="#000000",
                label="Exit",command= quit)

        self.Text2 = tk.Text(top)
        self.Text2.place(relx=0.366, rely=0.036, relheight=0.108, relwidth=0.318)
        self.Text2.configure(background="white")
        self.Text2.configure(font="TkTextFont")
        self.Text2.configure(foreground="black")
        self.Text2.configure(highlightbackground="#d9d9d9")
        self.Text2.configure(highlightcolor="black")
        self.Text2.configure(insertbackground="black")
        self.Text2.configure(selectbackground="#c4c4c4")
        self.Text2.configure(selectforeground="black")
        self.Text2.configure(width=434)
        self.Text2.configure(wrap="word")


        self.Text3 = tk.Text(top)
        self.Text3.place(relx=0.688, rely=0.036, relheight=0.108, relwidth=0.303)

        self.Text3.configure(background="white")
        self.Text3.configure(font="TkTextFont")
        self.Text3.configure(foreground="black")
        self.Text3.configure(highlightbackground="#d9d9d9")
        self.Text3.configure(highlightcolor="black")
        self.Text3.configure(insertbackground="black")
        self.Text3.configure(selectbackground="#c4c4c4")
        self.Text3.configure(selectforeground="black")
        self.Text3.configure(width=414)
        self.Text3.configure(wrap="word")

        self.Text4 = tk.Text(top)
        self.Text4.place(relx=0.366, rely=0.175, relheight=0.123, relwidth=0.318)

        self.Text4.configure(background="white")
        self.Text4.configure(font="TkTextFont")
        self.Text4.configure(foreground="black")
        self.Text4.configure(highlightbackground="#d9d9d9")
        self.Text4.configure(highlightcolor="black")
        self.Text4.configure(insertbackground="black")
        self.Text4.configure(selectbackground="#c4c4c4")
        self.Text4.configure(selectforeground="black")
        self.Text4.configure(width=434)
        self.Text4.configure(wrap="word")

        self.Text5 = tk.Text(top)
        self.Text5.place(relx=0.688, rely=0.175, relheight=0.123, relwidth=0.303)

        self.Text5.configure(background="white")
        self.Text5.configure(font="TkTextFont")
        self.Text5.configure(foreground="black")
        self.Text5.configure(highlightbackground="#d9d9d9")
        self.Text5.configure(highlightcolor="black")
        self.Text5.configure(insertbackground="black")
        self.Text5.configure(selectbackground="#c4c4c4")
        self.Text5.configure(selectforeground="black")
        self.Text5.configure(width=414)
        self.Text5.configure(wrap="word")

        self.Text6 = tk.Text(top)
        self.Text6.place(relx=0.366, rely=0.336, relheight=0.108, relwidth=0.318)

        self.Text6.configure(background="white")
        self.Text6.configure(font="TkTextFont")
        self.Text6.configure(foreground="black")
        self.Text6.configure(highlightbackground="#d9d9d9")
        self.Text6.configure(highlightcolor="black")
        self.Text6.configure(insertbackground="black")
        self.Text6.configure(selectbackground="#c4c4c4")
        self.Text6.configure(selectforeground="black")
        self.Text6.configure(width=434)
        self.Text6.configure(wrap="word")

        self.Text7 = tk.Text(top)
        self.Text7.place(relx=0.688, rely=0.336, relheight=0.108, relwidth=0.303)

        self.Text7.configure(background="white")
        self.Text7.configure(font="TkTextFont")
        self.Text7.configure(foreground="black")
        self.Text7.configure(highlightbackground="#d9d9d9")
        self.Text7.configure(highlightcolor="black")
        self.Text7.configure(insertbackground="black")
        self.Text7.configure(selectbackground="#c4c4c4")
        self.Text7.configure(selectforeground="black")
        self.Text7.configure(width=414)
        self.Text7.configure(wrap="word")

        self.Text8 = tk.Text(top)
        self.Text8.place(relx=0.366, rely=0.474, relheight=0.239, relwidth=0.625)

        self.Text8.configure(background="white")
        self.Text8.configure(font="TkTextFont")
        self.Text8.configure(foreground="black")
        self.Text8.configure(highlightbackground="#d9d9d9")
        self.Text8.configure(highlightcolor="black")
        self.Text8.configure(insertbackground="black")
        self.Text8.configure(selectbackground="#c4c4c4")
        self.Text8.configure(selectforeground="black")
        self.Text8.configure(width=854)
        self.Text8.configure(wrap="word")

        self.Text9 = tk.Text(top)
        self.Text9.place(relx=0.366, rely=0.737, relheight=0.21, relwidth=0.625)
        self.Text9.configure(background="white")
        self.Text9.configure(font="TkTextFont")
        self.Text9.configure(foreground="black")
        self.Text9.configure(highlightbackground="#d9d9d9")
        self.Text9.configure(highlightcolor="black")
        self.Text9.configure(insertbackground="black")
        self.Text9.configure(selectbackground="#c4c4c4")
        self.Text9.configure(selectforeground="black")
        self.Text9.configure(width=854)
        self.Text9.configure(wrap="word")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.366, rely=0.0, height=21, width=434)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Unused Garbage Variable(s) :''')

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.362, rely=0.146, height=21, width=434)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Duplicate \ Unbeneficial line(s) :''')

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.362, rely=0.299, height=21, width=434)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''Average Missing Parentheses :''')

        self.Label4 = tk.Label(top)
        self.Label4.place(relx=0.362, rely=0.445, height=21, width=854)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''Variable Value Reassigned :''')

        self.Label5 = tk.Label(top)
        self.Label5.place(relx=0.688, rely=0.0, height=21, width=414)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''Removed Variable(s) :''')

        self.Label6 = tk.Label(top)
        self.Label6.place(relx=0.688, rely=0.146, height=21, width=414)
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(activeforeground="black")
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(highlightbackground="#d9d9d9")
        self.Label6.configure(highlightcolor="black")
        self.Label6.configure(text='''Duplication Removed :''')

        self.Label7 = tk.Label(top)
        self.Label7.place(relx=0.684, rely=0.299, height=21, width=414)
        self.Label7.configure(activebackground="#f9f9f9")
        self.Label7.configure(activeforeground="black")
        self.Label7.configure(background="#d9d9d9")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(highlightbackground="#d9d9d9")
        self.Label7.configure(highlightcolor="black")
        self.Label7.configure(text='''Array Index(es) Evaluation :''')

        self.Label8 = tk.Label(top)
        self.Label8.place(relx=0.362, rely=0.708, height=21, width=854)
        self.Label8.configure(activebackground="#f9f9f9")
        self.Label8.configure(activeforeground="black")
        self.Label8.configure(background="#d9d9d9")
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(foreground="#000000")
        self.Label8.configure(highlightbackground="#d9d9d9")
        self.Label8.configure(highlightcolor="black")
        self.Label8.configure(text='''Loop Pre-Execution Results :''')

        self.TSeparator1 = ttk.Separator(top)
        self.TSeparator1.place(relx=0.359, rely=0.036, relheight=0.905)
        self.TSeparator1.configure(orient="vertical")

        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.004, rely=0.036,height=70, relwidth=0.347)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="#c4c4c4")
        self.Entry1.configure(selectforeground="black")
        self.Entry1.configure(width=474)
        self.Entry1.bind("<Key>",keyboardkeypressed)

        self.Label9 = tk.Label(top)
        self.Label9.place(relx=0.007, rely=0.0, height=21, width=474)
        self.Label9.configure(activebackground="#f9f9f9")
        self.Label9.configure(activeforeground="black")
        self.Label9.configure(background="#d9d9d9")
        self.Label9.configure(disabledforeground="#a3a3a3")
        self.Label9.configure(foreground="#000000")
        self.Label9.configure(highlightbackground="#d9d9d9")
        self.Label9.configure(highlightcolor="black")
        self.Label9.configure(text='''Live Development :''')

        self.Text1 = tk.Text(top)
        #self.Text1.place(relx=0.007, rely=0.182, relheight=0.765, relwidth=0.347)
        self.Text1.place(relx=0.007, rely=0.217, relheight=0.533, relwidth=0.347)

        self.Text1.configure(background="white")
        self.Text1.configure(font="TkTextFont")
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#d9d9d9")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="#c4c4c4")
        self.Text1.configure(selectforeground="black")
        self.Text1.configure(width=474)
        self.Text1.configure(wrap="word")

        self.Label10 = tk.Label(top)
        self.Label10.place(relx=0.007, rely=0.146, height=21, width=474)
        self.Label10.configure(background="#d9d9d9")
        self.Label10.configure(disabledforeground="#a3a3a3")
        self.Label10.configure(foreground="#000000")
        self.Label10.configure(text='''Working Sheet :''')
        self.Label10.configure(width=474)

        self.Label9 = tk.Label(top)
        self.Label9.place(relx=0.007, rely=0.737, height=21, width=474)
        self.Label9.configure(background="#d9d9d9")
        self.Label9.configure(disabledforeground="#a3a3a3")
        self.Label9.configure(foreground="#000000")
        self.Label9.configure(text='''Logical Pre-Execution Result :''')
        self.Label9.configure(width=474)

        self.Text10 = tk.Text(top)
        self.Text10.place(relx=0.007, rely=0.767, relheight=0.217, relwidth = 0.347)
        self.Text10.configure(background="white")
        self.Text10.configure(font="TkTextFont")
        self.Text10.configure(foreground="black")
        self.Text10.configure(highlightbackground="#d9d9d9")
        self.Text10.configure(highlightcolor="black")
        self.Text10.configure(insertbackground="black")
        self.Text10.configure(selectbackground="#c4c4c4")
        self.Text10.configure(selectforeground="black")
        self.Text10.configure(width=474) #474
        self.Text10.configure(wrap="word")

        menu = tk.Menu(root, tearoff=0)
        menu.add_command(label="Clean Results Field(s) ", command=cleanfield)
        menu.add_command(label="Delete Existing Code File", command=deltextfile)
        menu.add_command(label="Clean Results Field(s) and Delete Code File", command=twdel)
        menu.add_separator()
        menu.add_command(label="1.  While Scope Inspection", command=comparingword)
        menu.add_command(label="2.  Average Missing Parentheses", command=findingsha)
        menu.add_command(label="3.  Array Indexing", command=indexarray)
        menu.add_command(label="4.  Unused Variable", command=variable)
        menu.add_command(label="5.  Removing Unused Variable(s)", command = removeunvariable)
        menu.add_command(label="6.  Duplicate Line", command=duplicate)
        menu.add_command(label="7.  Variable Value Reassigned", command=reassigning)
        menu.add_command(label="8.  Removing Elements",command=removingelement)
        menu.add_command(label="9.  Infinity Loop Detection",command =infinityloop)

        top.bind("<Button-3>", popup)

if __name__ == '__main__':
    vp_start_gui()





