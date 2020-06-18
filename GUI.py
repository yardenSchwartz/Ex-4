from tkinter import *
from tkinter import filedialog
from tkinter import messagebox as mb
# import plotly.plotly as py
# from PIL import Image,ImageTk
from PIL import ImageTk,Image
import sys

import dataManagment
from dataManagment import *
from PlotsManagement import *

class GUI:

    data = ""
    validClusterParam = False
    validRunParam = False

    def __init__(self, master):
        try:
            py.sign_in('schyarde', 'QFqZeNqpcn2OaFftFKfY')

            self.master = master
            master.title("K Means Clustering")
            master.minsize(640, 400)

            vcmdRun = master.register(self.validateRun)
            vcmdCluster = master.register(self.validateCluster)

            self.labelPath = Label(master, text="DataSet Path: ")

            self.pathTxt = Entry(master)

            self.browseBtn = Button(master, text="Browse", command=lambda: self.browserBtn())
            self.fileName = ""
            self.preprocessingBtn = Button(master, text="Pre-process", command=lambda: self.pre(self.fileName))

            self.numOfClusterLbl = Label(master, text="Number of Clusters k")
            self.numOfClusterEntry = Entry(master,validate="key", validatecommand=(vcmdCluster, '%P'))
            self.numOfRunsLbl = Label(master, text="Number of runs")
            self.numOfRunsEntry = Entry(master,validate="key", validatecommand=(vcmdRun, '%P'))

            self.clusterBtn = Button(master, text="Cluster", state=DISABLED, command=lambda: self.sendToKMeans(self.numOfClusterEntry.get(), self.numOfRunsEntry.get()))

            #Layout
            self.labelPath.grid(row=1, column=1)
            self.pathTxt.grid(row=1, column=2)
            self.browseBtn.grid(row=1, column=5)
            self.preprocessingBtn.grid(row=2, column=2)
            self.numOfClusterLbl.grid(row=3, column=1)
            self.numOfClusterEntry.grid(row=3, column=2)
            self.numOfRunsLbl.grid(row=4, column=1)
            self.numOfRunsEntry.grid(row=4, column=2)
            self.clusterBtn.grid(row=5, column=1)

        except:
            mb.showerror("K Means Clustering", "Something wrong, try again!")

    def enableOrDisabledClusterBtn(self):
        if self.validClusterParam == True and self.validRunParam == True:
            self.clusterBtn.configure(state=NORMAL)
        else:
            self.clusterBtn.configure(state=DISABLED)

    def validateRun(self, new_text):
        if not new_text:  # the field is being cleared
            if len(self.numOfRunsEntry.children) == 0:
                self.validRunParam = False
                self.enableOrDisabledClusterBtn()

            self.entered_number = 0
            return True

        try:
            self.entered_number = int(new_text)
            if self.entered_number <= 0:
                mb.showerror("K Means Clustering", "Please enter just positive and valid integer numbers!")
                self.validRunParam = False
                self.enableOrDisabledClusterBtn()
                return False
            else:
                self.validRunParam = True
                self.enableOrDisabledClusterBtn()
                return True

        except ValueError:
            mb.showerror("K Means Clustering", "Please enter just positive and valid integer numbers!")
            self.validRunParam = False
            self.enableOrDisabledClusterBtn()
            return False

    def validateCluster(self, new_text):
        if not new_text:  # the field is being cleared
            if len(self.numOfClusterEntry.children) == 0:
                self.validClusterParam = False
                self.enableOrDisabledClusterBtn()

            self.entered_number = 0
            return True

        try:
            self.entered_number = int(new_text)
            if self.entered_number <= 0:
                mb.showerror("K Means Clustering", "Please enter just positive and valid integer numbers!")
                self.validClusterParam = False
                self.enableOrDisabledClusterBtn()
                return False
            else:
                self.validClusterParam = True
                self.enableOrDisabledClusterBtn()
                return True

        except ValueError:
            mb.showerror("K Means Clustering", "Please enter just positive and valid integer numbers!")
            self.validClusterParam = False
            self.enableOrDisabledClusterBtn()
            return False

    def browserBtn(self):
        try:
            self.fileName = filedialog.askopenfilename(initialdir ="/", title ="Select A File", filetypes=[("Excel files", "*.xlsx")])
            # self.pathTxt.configure(text = self.fileName)
            self.pathTxt.insert(0,self.fileName)
        except:
            mb.showerror("K Means Clustering", "Something wrong with the browser, try again!")

    def sendToKMeans(self, numOfCluster, numOfRuns):
        try:
            if numOfCluster == "" or numOfRuns == "":
                mb.showwarning("K Means Clustering", "Please fill all the fields before click on 'Cluster'!")
            else:
                try:
                    num1 = int(numOfCluster)
                    num2 = int(numOfRuns)
                    if num2 < 0 or num1 < 2 or num1 > 164 :
                        mb.showerror("K Means Clustering", "Please enter just positive and valid integer numbers!")
                    else:
                        # self.numOfRunsEntry = num1
                        # self.numOfClusterEntry = num2
                        ans = kmeansCalc(self.data, num1, num2)
                        if ans == "success":
                            box = mb.askokcancel("K Means Clustering",
                                                 "kmeans completed successfully! \n Do you want exit ?")
                            if box == TRUE:
                                root.destroy()
                                # sys.exit(-1)
                            elif box == FALSE:
                                # scatter Plot
                                scatterPlot(self.data)
                                self.img = ImageTk.PhotoImage(Image.open("scatterPlot.png"))
                                self.panel = Label(image=self.img)
                                self.panel.grid(row=7, column=2)

                                # horopleth plot
                                horoplethMap(self.data)
                                self.img2 = ImageTk.PhotoImage(Image.open("horoplethMap.png"))
                                self.panel2 = Label(image=self.img2)
                                self.panel2.grid(row=7, column=1)
                        else:
                            mb.showerror("K Means Clustering", "kmeans not completed successfully!")

                except ValueError:
                    mb.showerror("K Means Clustering", "Please enter just positive integer numbers!")
        except:
            mb.showerror("K Means Clustering", "Something wrong with the kMeans, try again!")

    def pre(self, file):
        try:
            ans = preprocessing(file)
            self.data = ans[0]
            if ans[1] == "success":
                mb.showinfo("K Means Clustering", "Preprocessing completed successfully!")
            else:
                mb.showerror("K Means Clustering", "Preprocessing not completed successfully!")
        except:
            mb.showerror("K Means Clustering", "Something wrong with the pre-processing. \n check your file and try again!")

root = Tk()
my_gui = GUI(root)
root.mainloop()