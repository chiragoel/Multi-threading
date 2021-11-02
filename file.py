import random as r
import os, sys, time, threading, multiprocessing


#numberOfCores=multiprocessing.cpu_count()
fw = open("time.csv","w")
co = "%s , %s \n"%("SNo." , "Time")
fw.write(co)
def task(cmd):
    fr = open(".\input\\"+cmd)
    fw = open(".\output\\"+cmd,"w+")
    for line in fr:
        fw.write(line.upper())
    fr.close()
    fw.close()
    
    return


def main():
    # Run Multiple Thread
    for i in range(1,101):
        start = time.time()
        print("New thread \n")
        files = os.listdir("./input")
        for f in files:
            cmd= f
            t1 = threading.Thread(target=task , args=(cmd,))
            t1.start()
            while True:
                if threading.activeCount()-1 <= i:
                    break
                time.sleep(1)

        # Waiting to finish the thread
        while True:
            if threading.activeCount() == 1:
                break
            time.sleep(1)
            print ("Thread Left ... ",threading.activeCount() - 2)
        end = time.time()
        t = end - start
        fw = open("time.csv","a")
        writing = "%s , % f\n"%(str(i) ,t)
        fw.write(writing)
        start = 0
        end = 0
        print("\n...All Thread ends....")
    fw.close()
main()
