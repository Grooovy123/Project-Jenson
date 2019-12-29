import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

import os
import numpy
import tflearn
import tensorflow
import random
import json
import pickle
import time
from Functions import *

def main():
    func = Function()    
    data = read_JSON()    

    if os.path.exists("data.pickle"):
        words, labels, training, output = read_pickle()
        print(f"date.pickle exists")        
    else:       
        words, labels, training, output = intents_prep(data)

    model = DNN(training, output, False)
    chat(model, words, labels, data, func)

def read_JSON():
    with open("intents.json") as file:
        data = json.load(file)
    print("intents loaded")

    return data

def read_pickle():
    with open("data.pickle", "rb") as f:
        words, labels, training, output = pickle.load(f)
    print("data loaded")

    return words, labels, training, output

def intents_prep(data):
    words = []
    labels = []
    docs_x = []
    docs_y = []

    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            wrds = nltk.word_tokenize(pattern)
            words.extend(wrds)
            docs_x.append(wrds)
            docs_y.append(intent["tag"])

        if intent["tag"] not in labels:
            labels.append(intent["tag"])

    words = [stemmer.stem(w.lower()) for w in words if w != "?"]
    words = sorted(list(set(words)))

    labels = sorted(labels)

    training = []
    output = []

    out_empty = [0 for _ in range(len(labels))]

    for x, doc in enumerate(docs_x):
        bag = []

        wrds = [stemmer.stem(w.lower()) for w in doc]

        for w in words:
            if w in wrds:
                bag.append(1)
            else:
                bag.append(0)

        output_row = out_empty[:]
        output_row[labels.index(docs_y[x])] = 1

        training.append(bag)
        output.append(output_row)

    training = numpy.array(training) # number of patterns in intents
    output = numpy.array(output) # number of tags in intents

    with open("data.pickle", "wb") as f:
        pickle.dump((words, labels, training, output), f)

    return words, labels, training, output

def DNN(training, output, running):    
    tensorflow.reset_default_graph()        

    net = tflearn.input_data(shape=[None, len(training[0])])
    net = tflearn.fully_connected(net, 8)
    net = tflearn.fully_connected(net, 8)
    net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
    net = tflearn.regression(net)

    model = tflearn.DNN(net)

    if running == True:        
        return model
    else:
        if os.path.exists("model.tflearn.meta"):        
            model.load("model.tflearn")
        else:
            train(model, training, output)

        running = True
        return model

def train(model, training, output):
    model.fit(training, output, n_epoch=1000, batch_size=8, show_metric=True)    
    model.save("model.tflearn")    
    model.load("model.tflearn")    

def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1
            
    return numpy.array(bag)

def chat(model, words, labels, data, func):
    
    print("Start talking with the bot (type quit to stop)!")
    while True:
        inp = input("You: ")
        if inp.lower() == "quit":            
            quit()
        #start_time = time.time()
        results = model.predict([bag_of_words(inp, words)])[0]
        #print(f"prediction took: {time.time()-start_time}")
        results_index = numpy.argmax(results)
        tag = labels[results_index]        

        if results[results_index] > 0.8:
            for tg in data["intents"]:
                if tg['tag'] == tag:
                    responses = tg['responses']

                    if 'Function: ' in responses[0]:            
                        func_num = int(responses[0][10:])                      

                        print(case(func_num, inp, data, func))                    

                    else:
                        print(random.choice(responses))

        else:
            for tg in data["intents"]:
                if tg['tag'] == "unable_to_answer":
                    responses = tg['responses']
                    print(random.choice(responses))

def case(func_num, inp, data, func):

    switch = {
            0: func.get_time(func_num),
            1: func.get_day(func_num),
            2: func.retrain_jenson(func_num, func.remove_model(func_num), func),
            3: func.search_web(func_num, func.get_query_for_web(func_num, inp, data)),
            4: func.test(func_num),
            5: func.Wiki_search(func_num, inp),
            6: func.open_browsers(func_num, inp),
            7: func.play_music(func_num),
            8: func.stop_music(func_num)
            }

    return switch[func_num]
    
if __name__ == '__main__':
    main()

