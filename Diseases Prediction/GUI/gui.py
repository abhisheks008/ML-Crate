# GUI stuff..............................................................................
from tkinter import *
root = Tk()
root.configure(background='black')
Symptom1 = StringVar()
Symptom1.set("Select Here")
Symptom2 = StringVar()
Symptom2.set("Select Here")
Symptom3 = StringVar()
Symptom3.set("Select Here")
Symptom4 = StringVar()
Symptom4.set("Select Here")
Symptom5 = StringVar()
Symptom5.set("Select Here")
Name = StringVar()

w2 = Label(root, justify=CENTER, text="Disease Predictor using Machine Learning", fg="white", bg="black", )
w2.config(font=("Times", 30, "bold italic"))
w2.grid(row=1, column=0, columnspan=2, padx=100)

w2 = Label(root, justify=CENTER, text="A Project by Vikas Kumar", fg="white", bg="black")
w2.config(font=("Times", 30, "bold italic"))
w2.grid(row=2, column=0, columnspan=2, padx=100)

NameLb = Label(root, text="Name of the Patient", fg="white", bg="black")
NameLb.config(font=("", 15, "bold italic"))
NameLb.grid(row=6, column=0, pady=15, sticky=W)

S1Lb = Label(root, text="Symptom 1", fg="White", bg="black")
S1Lb.config(font=("Times", 15, "bold italic"))
S1Lb.grid(row=7, column=0, pady=10, sticky=W)

S2Lb = Label(root, text="Symptom 2", fg="White", bg="black")
S2Lb.config(font=("Times", 15, "bold italic"))
S2Lb.grid(row=8, column=0, pady=10, sticky=W)

S3Lb = Label(root, text="Symptom 3", fg="White", bg="black")
S3Lb.config(font=("Times", 15, "bold italic"))
S3Lb.grid(row=9, column=0, pady=10, sticky=W)

S4Lb = Label(root, text="Symptom 4", fg="White", bg="black")
S4Lb.config(font=("Times", 15, "bold italic"))
S4Lb.grid(row=10, column=0, pady=10, sticky=W)

S5Lb = Label(root, text="Symptom 5", fg="White", bg="black")
S5Lb.config(font=("Times", 15, "bold italic"))
S5Lb.grid(row=11, column=0, pady=10, sticky=W)

lrLb = Label(root, text="DecisionTree", fg="white", bg="black")
lrLb.config(font=("Times", 15, "bold italic"))
lrLb.grid(row=15, column=0, pady=10, sticky=W)

destreeLb = Label(root, text="RandomForest", fg="white", bg="black")
destreeLb.config(font=("Times", 15, "bold italic"))
destreeLb.grid(row=17, column=0, pady=10, sticky=W)

ranfLb = Label(root, text="NaiveBayes", fg="White", bg="black")
ranfLb.config(font=("Times", 15, "bold italic"))
ranfLb.grid(row=19, column=0, pady=10, sticky=W)

svLb = Label(root, text="Support Vector", fg="White", bg="black")
svLb.config(font=("Times", 15, "bold italic"))
svLb.grid(row=21, column=0, pady=10, sticky=W)

OPTIONS = sorted(l1)
NameEn = Entry(root, textvariable=Name)
NameEn.grid(row=6, column=1)

S1 = OptionMenu(root, Symptom1, *OPTIONS)
S1.grid(row=7, column=1)
S2 = OptionMenu(root, Symptom2, *OPTIONS)
S2.grid(row=8, column=1)
S3 = OptionMenu(root, Symptom3, *OPTIONS)
S3.grid(row=9, column=1)
S4 = OptionMenu(root, Symptom4, *OPTIONS)
S4.grid(row=10, column=1)
S5 = OptionMenu(root, Symptom5, *OPTIONS)
S5.grid(row=11, column=1)

lab = Label(root, justify=CENTER, text="Predictions", fg="white", bg="black", )
lab.config(font=("Times", 20, "bold italic"))
lab.grid(row=14, column=0, columnspan=2, padx=100)

dst = Button(root, text="Prediction 1", command=DecisionTree, bg="green", fg="white")
dst.config(font=("Times", 15, "bold italic"))
dst.grid(row=15, column=3, padx=15, pady=10)

t1 = Text(root, height=1, width=40, bg="green", fg="white")
t1.config(font=("Times", 15, "bold italic"))
t1.grid(row=15, column=1, padx=15, pady=10)

rnf = Button(root, text="Prediction 2", command=randomforest, bg="blue", fg="white")
rnf.config(font=("Times", 15, "bold italic"))
rnf.grid(row=17, column=3, padx=15, pady=10)

t2 = Text(root, height=1, width=40, bg="blue", fg="white")
t2.config(font=("Times", 15, "bold italic"))
t2.grid(row=17, column=1, padx=15, pady=10)

lr = Button(root, text="Prediction 3", command=NaiveBayes, bg="red", fg="white")
lr.config(font=("Times", 15, "bold italic"))
lr.grid(row=19, column=3, padx=15, pady=10)

t3 = Text(root, height=1, width=40, bg="red", fg="white")
t3.config(font=("Times", 15, "bold italic"))
t3.grid(row=19, column=1, padx=15, pady=10)

sv = Button(root, text="Prediction 4", command=SupportVector, bg="violet", fg="white")
sv.config(font=("Times", 15, "bold italic"))
sv.grid(row=21, column=3, padx=15, pady=10)

t4 = Text(root, height=1, width=40, bg="violet", fg="white")
t4.config(font=("Times", 15, "bold italic"))
t4.grid(row=21, column=1, padx=15, pady=10)

root.mainloop()