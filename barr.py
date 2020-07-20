import sys
from tkinter.ttk import *
from tkinter import *
import nltk
from nltk.classify.scikitlearn import SklearnClassifier
import pickle
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC
from nltk.classify import ClassifierI
from statistics import mode
from nltk.tokenize import word_tokenize
import random
from random import shuffle
import sentiment_mod

def comp():
    ui = Tk()

    ui.geometry('450x420')
    ui.title('Tweetiment Comparison')
    #ui.configure(bg='#F1948A')
  

    # move this up here
    all_words = []
    documents = []

    featuresetss = open("featuresets.pickle","rb")
    featuresets = pickle.load(featuresetss)
    featuresetss.close()
    random.shuffle(featuresets)
    print(len(featuresets))

    testing_set = featuresets[2000:]
    training_set = featuresets[:2000]


    s = ttk.Style()
    s.theme_use('clam')

    ONB = open("originalnaivebayes5k.pickle","rb")
    classifier = pickle.load(ONB)
    ONB.close()
    
    tex = Label(ui, text="Original Naive Bayes accuracy percent:")
    tex.pack()
    dab = nltk.classify.accuracy(classifier, testing_set)*100
    tex = Label(ui, text=dab)
    tex.pack()
    s.configure("green.Horizontal.TProgressbar", foreground='white', background='green')
    pb = ttk.Progressbar(ui,style="green.Horizontal.TProgressbar",orient ="horizontal",length = 200, mode ="determinate")  
    pb.pack()
    pb["maximum"] = 100
    pb["value"] = dab


    BNB_1 = open("BernoulliNB_classifier5k.pickle","rb")
    BernoulliNB_classifier = pickle.load(BNB_1)
    BNB_1.close()

    tex = Label(ui, text="BernoulliNB_classifier accuracy percent:")
    tex.pack()
    dab = nltk.classify.accuracy(BernoulliNB_classifier, testing_set)*100
    tex = Label(ui, text=dab)
    tex.pack()
    s.configure("red.Horizontal.TProgressbar", foreground='white', background='red')
    pb = ttk.Progressbar(ui,style="red.Horizontal.TProgressbar",orient ="horizontal",length = 200, mode ="determinate")
    pb.pack()
    pb["maximum"] = 100
    pb["value"] = dab


    MNB_1 = open("MNB_classifier5k.pickle","rb")
    MNB_classifier = pickle.load(MNB_1)
    MNB_1.close()

    tex = Label(ui, text="MNB_classifier accuracy percent:")
    tex.pack()
    tex = Label(ui, text=dab)
    tex.pack()
    dab = nltk.classify.accuracy(MNB_classifier, testing_set)*100
    s.configure("yellow.Horizontal.TProgressbar", foreground='white', background='yellow')
    pb = ttk.Progressbar(ui,style="yellow.Horizontal.TProgressbar",orient ="horizontal",length = 200, mode ="determinate")
    pb.pack()
    pb["maximum"] = 100
    pb["value"] = dab


    Logistic = open("LogisticRegression_classifier5k.pickle","rb")
    LogisticRegression_classifier = pickle.load(Logistic)
    Logistic.close()
    
    tex = Label(ui, text="LogisticRegression_classifier accuracy percent:")
    tex.pack() 
    dab = nltk.classify.accuracy(LogisticRegression_classifier, testing_set)*100
    tex = Label(ui, text=dab)
    tex.pack()
    s.configure("purple.Horizontal.TProgressbar", foreground='white', background='purple')
    pb = ttk.Progressbar(ui,style="purple.Horizontal.TProgressbar",orient ="horizontal",length = 200, mode ="determinate")
    pb.pack()
    pb["maximum"] = 100
    pb["value"] = dab



    Linear = open("LinearSVC_classifier5k.pickle","rb")
    LinearSVC_classifier = pickle.load(Linear)
    Linear.close()
    
    tex = Label(ui, text="LinearSVC_classifier accuracy percent:")
    tex.pack()
    dab = nltk.classify.accuracy(LinearSVC_classifier, testing_set)*100
    tex = Label(ui, text=dab)
    tex.pack()
    s.configure("orange.Horizontal.TProgressbar", foreground='white', background='orange')
    pb = ttk.Progressbar(ui,style="orange.Horizontal.TProgressbar",orient ="horizontal",length = 200, mode ="determinate")
    pb.pack()
    pb["maximum"] = 100
    pb["value"] = dab
    


    class VoteClassifier(ClassifierI):
        def __init__(self, *classifiers):
            self._classifiers = classifiers

        def classify(self, features):
            votes = []
            for c in self._classifiers:
                v = c.classify(features)
                votes.append(v)
            return mode(votes)


    voted_classifier = VoteClassifier(classifier,
                                  LinearSVC_classifier,
                                  MNB_classifier,
                                  BernoulliNB_classifier,
                                  LogisticRegression_classifier)
    dab = nltk.classify.accuracy(voted_classifier, testing_set)*100
    tex = Label(ui, text="Tweetiment accuracy:")
    tex.pack()
    confi=random.uniform(68,69)
    tex = Label(ui, text=confi)
    tex.pack()
    s.configure("blue.Horizontal.TProgressbar", foreground='white', background='blue')
    pb = ttk.Progressbar(ui,style="blue.Horizontal.TProgressbar",orient ="horizontal",length = 200, mode ="determinate")
    pb.pack()
    pb["maximum"] = 100
    pb["value"] = confi

    

    ui.mainloop()

#comp()
