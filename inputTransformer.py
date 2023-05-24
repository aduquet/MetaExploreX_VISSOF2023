import pandas as pd
import numpy as np
import pathlib
import random
import json
import os

def MR1_PER(inputTestID, testData):

    # Permutative -> Randomly permute the elements

    for i in range(0, len(testData)):
        aux = testData[inputTestID[i]]['input'].copy()
        mainDF = {
            'test_input_id':inputTestID[i], 
            'test_data': testData[inputTestID[i]]['input'],
            'tdt_MR1_PER': random.sample(aux, len(aux))
        }
        auxListmainDF.append(mainDF)

def MR2_ADD(inputTestID, testData, constant):

    # Additive -> Add a positive constant

    auxListMR2 = []
    for i in range(0, len(testData)):
        aux = testData[inputTestID[i]]['input'].copy()
        auxList = []
        for i in aux:
            auxList.append(i + constant)    
        auxListMR2.append(auxList)

    return auxListMR2

def MR3_MUL(inputTestID, testData, constant):

    # Multiplicative -> Multiply by a positive constant
    
    auxListMR = []
    for i in range(0, len(testData)):
        aux = testData[inputTestID[i]]['input'].copy()
        auxList = []
        for i in aux:
            auxList.append(i * constant)    
        auxListMR.append(auxList)

    return auxListMR

def MR4_INV(inputTestID, testData):

    # Invertive -> Take the inverse of each element
    
    auxListMR = []
    for i in range(0, len(testData)):
        aux = testData[inputTestID[i]]['input'].copy()
        auxList = []
        for i in aux:
            if(i != 0):
                auxList.append(1/i) 
            else: 
                auxList.append('N/A') 
        auxListMR.append(auxList)

    return auxListMR

def MR5_INC(inputTestID, testData, constant):

    # Inclusive -> Add a new element
    
    auxListMR = []
    for i in range(0, len(testData)):
        aux = testData[inputTestID[i]]['input'].copy()
        aux.append(constant)
        auxListMR.append(aux)

    return auxListMR

def MR6_EXC(inputTestID, testData):

    # Exclusive -> Remove an elementt
    
    auxListMR = []
    for i in range(0, len(testData)):
        aux = testData[inputTestID[i]]['input'].copy()
        if len(aux) > 1 :
            aux.pop()
        auxListMR.append(aux)

    return auxListMR

def save_json(df, output, savePath):
    
    df.to_json(savePath + '/' + output + '.json', indent= 4, orient="index")


def save_csv(df, output, savePath):
    df.to_csv(savePath + '/' + output + '.csv')

if __name__ == '__main__':

    import click 

    global mainDF
    mainDF = {}

    global auxListmainDF
    auxListmainDF = []

    @click.command()
    @click.option('-i', '--input_path', 'input_path')
    @click.option('-o', '--output', 'output')

    def main(input_path, output):
        
        mainPath = str(pathlib.Path().absolute()) + '/' + 'MR_InputTransformations'

        try:
            os.mkdir(mainPath)
        except:
            pass

        with open(input_path, "r") as readfile:
            testData = json.load(readfile)
            json.dumps(testData,indent = 4)
        constant = 0
        while constant == 0 or constant == 1:
            constant = np.random.uniform(low=0, high=15, size=1).astype(int)[0]
        
        inputTestID = list(testData.keys())
        # print(testDataKeys)
        

        MR1_PER(inputTestID, testData)
        df = pd.DataFrame(auxListmainDF)

        df['tdt_MR2_ADD'] = MR2_ADD(inputTestID, testData, constant)
        df['tdt_MR3_MUL'] = MR3_MUL(inputTestID, testData, constant)
        df['tdt_MR4_INV'] = MR4_INV(inputTestID, testData)
        df['tdt_MR5_INC'] = MR5_INC(inputTestID, testData,constant)
        df['tdt_MR6_EXC'] = MR6_EXC(inputTestID, testData)
        
        df = df.set_index('test_input_id')

        save_csv(df, output, mainPath)
        save_json(df, output, mainPath)

main()