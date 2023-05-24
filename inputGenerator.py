import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import glob as gl
import shortuuid
import pathlib
import time
import os


def fuzzer(low, high, input_type):

    if input_type == 'int':
        size = np.random.uniform(low=3, high=15, size=1).astype(int)
        a = np.random.randint(low,high,size).tolist()
        return a
    
    if input_type == 'float':
        size = np.random.uniform(low=2, high=15, size=2).astype(int)
        a = np.random.random(size).tolist()
        return a
    
    else:
        return 0

def save_json(df, output, savePath):
    
    df.to_json(savePath + '/' + output + '.json', indent= 4, orient="index")


def save_csv(df, output, savePath):
    df.to_csv(savePath + '/' + output + '.csv')


if __name__ == '__main__':

    import click 

    global mainDF
    mainDF = {}

    global auxList
    auxList = []

    @click.command()
    @click.option('-l', '--low', 'low')
    @click.option('-h', '--high', 'high')
    @click.option('-it', '--input_type', 'input_type')
    @click.option('-t', '--t_end', 't_end')
    @click.option('-o', '--output', 'output', help = 'Output file name')

    def main(low, high, input_type, t_end, output):
        
        mainPath = str(pathlib.Path().absolute()) + '/' + 'inputs'
        print(mainPath)

        try:
            os.mkdir(mainPath)
        except:
            pass

        t_end = time.time() + float(t_end)
        # index = 0
        while time.time() < t_end:
            newInput = fuzzer(int(low),int(high), input_type)
            if len(newInput) != 0:
                valute_type = type(newInput[0])
            else:
                valute_type = None
            mainDF = {
                'test_input_id':shortuuid.uuid(),
                'input': newInput,
                'input_type': str(type(newInput)),
                'values_type': str(valute_type),
                'size': len(newInput)}
            # index = index + 1
            
            auxList.append(mainDF)
        
        df = pd.DataFrame(auxList, index=None)
        df = df.set_index('test_input_id')

        save_csv(df, output, mainPath)
        save_json(df, output, mainPath)

main()
