import re
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

epoch_pattern = re.compile("epoch (\d+), iter (\d+), cum. loss \d+.?\d+, cum. ppl (\d+.?\d+)")
validation_pattern = re.compile("validation: iter \d+, dev. ppl (\d+.?\d+)")

class Results:
    def __init__(self):
        self.epoch = 0
        self.train_ppl = 0
        self.dev_ppl = 0
        self.iter = 0

def read_results(infile: str):
    """
    read results
    """
    f = open(infile)
    exs = []
    for line in f:
        exs.append(line)
    f.close()
    return exs

def return_results(raw):
    results = []

    prev_epoch = 0
    epoch = 0

    prev_iter = 0
    current_iter = 0

    for l in raw:

        if re.match(validation_pattern, l):
            r = Results()
            r.dev_ppl = validation_pattern.findall(l)[0]
            r.epoch = epoch
            r.iter = current_iter
            results.append(r)


        if re.match(epoch_pattern, l):
            r = Results()
            r.epoch, r.iter, r.train_ppl = epoch_pattern.findall(l)[0]
            current_iter = r.iter
            epoch = r.epoch
            results.append(r)

        if prev_epoch != epoch:
            prev_epoch = epoch

        if prev_iter != current_iter:
            prev_iter = current_iter
    return results

def return_processed_results(results):
    train = []
    train_tuple = []
    dev = []
    dev_tuple = []
    for r in results:
        if float(r.train_ppl) != 0:
            train_tuple.append((float(r.epoch), float(r.train_ppl)))
            train.append(float(r.train_ppl))
        else:
            dev_tuple.append((float(r.epoch),float(r.dev_ppl)))
            dev.append(float(r.dev_ppl))


    epoch_list = list(range(1,50))
    train_list = []
    dev_list = []

    for e in epoch_list:
        ppl_train_sum = 0
        ppl_dev_sum = 0
        i=0
        j=0
        for e1,p in train_tuple:
            if e1 == e:
                ppl_train_sum += p
                i+=1
        for e2,p in dev_tuple:
            if e2 == e:
                ppl_dev_sum += p
                j+=1
        train_list.append(ppl_train_sum/i)
        dev_list.append(ppl_dev_sum/j)

    return epoch_list, train_list, dev_list
