from tkinter import *
from tkinter import filedialog
from tkinter import messagebox as mb
# import plotly.plotly as py
# from PIL import Image,ImageTk
import dataManagment
from dataManagment import *
from PlotsManagement import *

class GUI:

    data = ""

    def __init__(self, master):
        py.sign_in('schyarde', 'QFqZeNqpcn2OaFftFKfY')

        self.master = master
        master.title("K Means Clustering")
        # self.minsize(640, 400)

        self.labelPath = Label(master, text="DataSet Path: ")

        self.pathTxt = Label(master)

        self.browseBtn = Button(master, text="Browse", command=lambda: self.browserBtn())

        self.preprocessingBtn = Button(master, text="Pre-process", command=lambda: self.pre(self.fileName))

        self.numOfClusterLbl = Label(master, text="Number of Clusters k")
        self.numOfClusterEntry = Entry(master)
        self.numOfRunsLbl = Label(master, text="Number of runs")
        self.numOfRunsEntry = Entry(master)
        self.clusterBtn = Button(master, text="Cluster", command=lambda: self.sendToKMeans(self.numOfClusterEntry.get(), self.numOfRunsEntry.get()))

        # self.img = ImageTk.PhotoImage(Image.open("scatterPlot.png"))
        # self.panel = Label(master, image=self.img)
        # self.panel.grid(row=3, column=3)
        #
        # self.img2 = ImageTk.PhotoImage(Image.open("horoplethMap.png"))
        # self.panel2 = Label(master, image=self.img2)
        # self.panel2.grid(row=3, column=4)


        #Layout
        self.labelPath.grid(row=1, column=1)
        self.pathTxt.grid(row=1, column=2)
        self.browseBtn.grid(row=1, column=3)
        self.preprocessingBtn.grid(row=2, column=2)
        self.numOfClusterLbl.grid(row=3, column=1)
        self.numOfClusterEntry.grid(row=3, column=2)
        self.numOfRunsLbl.grid(row=4, column=1)
        self.numOfRunsEntry.grid(row=4, column=2)
        self.clusterBtn.grid(row=5, column=1)

    def browserBtn(self):
        self.fileName = filedialog.askopenfilename(initialdir ="/", title ="Select A File") # file type - xlsx
        self.pathTxt.configure(text = self.fileName)

    def sendToKMeans(self, numOfCluster, numOfRuns):
        ans = kmeansCalc(self.data,int(numOfCluster),int(numOfRuns))
        if ans == "success":
            box = mb.askokcancel("K Means Clustering", "kmeans completed successfully!")
            if box == TRUE:
                root.destroy()
            # mb.showinfo("K Means Clustering", "kmeans completed successfully!")

            # scatter Plot
            # scatterPlot(self.data)

            # horopleth plot
            # horoplethMap(self.data)

        else:
            mb.showerror("K Means Clustering", "kmeans not completed successfully!")

    def pre(self, file):
        ans = preprocessing(file)
        self.data = ans[0]
        if ans[1] == "success":
            mb.showinfo("K Means Clustering", "Preprocessing completed successfully!")
        else:
            mb.showerror("K Means Clustering", "Preprocessing not completed successfully!")


root = Tk()
my_gui = GUI(root)
root.mainloop()