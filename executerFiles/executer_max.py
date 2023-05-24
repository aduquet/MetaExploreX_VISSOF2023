from MTexecuter import MTexecuter
from Methods_one_input.max	import	max
import pandas as pd
import pathlib
import json
import os

def dataExecution(inputTestID, testData, outputData, outputchecker, pathdata, pathChecker):
    AUXtestInput = []
    AUX_MR1 = []
    AUX_MR2 = []
    AUX_MR3 = []
    AUX_MR4 = []
    AUX_MR5 = []
    AUX_MR6 = []
    
    AUX_testData = []
    AUX_MR1_tdt = []
    AUX_MR2_tdt = []
    AUX_MR3_tdt = []
    AUX_MR4_tdt = []
    AUX_MR5_tdt = []
    AUX_MR6_tdt = []
    id = []

    for i in range(0, len(testData)):
        testInput = testData[inputTestID[i]]['test_data'].copy()
        MR1 = testData[inputTestID[i]]['tdt_MR1_PER'].copy()
        MR2 = testData[inputTestID[i]]['tdt_MR2_ADD'].copy()
        MR3 = testData[inputTestID[i]]['tdt_MR3_MUL'].copy()
        MR4 = testData[inputTestID[i]]['tdt_MR4_INV'].copy()
        MR5 = testData[inputTestID[i]]['tdt_MR5_INC'].copy()
        MR6 = testData[inputTestID[i]]['tdt_MR6_EXC'].copy()

        output_testData = max(testInput)
        output_MR1 = max(MR1)
        output_MR2 = max(MR2)
        output_MR3 = max(MR3)
        output_MR5 = max(MR5)
        output_MR6 = max(MR6)

        if 'N/A' in MR4:
            output_MR4 = 'd/0'
        else:
            output_MR4 = max(MR4)

        AUXtestInput.append(output_testData)
        AUX_MR1.append(output_MR1)
        AUX_MR2.append(output_MR2)
        AUX_MR3.append(output_MR3)
        AUX_MR4.append(output_MR4)
        AUX_MR5.append(output_MR5)
        AUX_MR6.append(output_MR6)
        
        id.append(inputTestID[i])
        AUX_testData.append(testInput)
        AUX_MR1_tdt.append(testData[inputTestID[i]]['tdt_MR1_PER'])
        AUX_MR2_tdt.append(testData[inputTestID[i]]['tdt_MR2_ADD'])
        AUX_MR3_tdt.append(testData[inputTestID[i]]['tdt_MR3_MUL'])
        AUX_MR4_tdt.append(testData[inputTestID[i]]['tdt_MR4_INV'])
        AUX_MR5_tdt.append(testData[inputTestID[i]]['tdt_MR5_INC'])
        AUX_MR6_tdt.append(testData[inputTestID[i]]['tdt_MR6_EXC'])
        
    mainDF['test_input_id'] = id
    mainDF['test_data'] = AUX_testData
    mainDF['tdt_MR1_PER'] = AUX_MR1_tdt
    mainDF['tdt_MR2_ADD'] = AUX_MR2_tdt
    mainDF['tdt_MR3_MUL'] = AUX_MR3_tdt
    mainDF['tdt_MR4_INV'] = AUX_MR4_tdt
    mainDF['tdt_MR5_INC'] = AUX_MR5_tdt
    mainDF['tdt_MR6_EXC'] = AUX_MR6_tdt
    
    mainDF['output_testInput'] = AUXtestInput
    mainDF['output_MR1'] = AUX_MR1
    mainDF['output_MR2'] = AUX_MR2
    mainDF['output_MR3'] = AUX_MR3
    mainDF['output_MR4'] = AUX_MR4
    mainDF['output_MR5'] = AUX_MR5
    mainDF['output_MR6'] = AUX_MR6
    
    
    finalDF = mainDF.copy()
    # print(type(finalDF))
    finalDF = mainDF.set_index('test_input_id')

    save_csv(finalDF, outputData, pathdata)
    save_json(finalDF, outputData, pathdata)    
    
    for index, row in mainDF.iterrows():
        
        mr = MTexecuter(row['output_testInput'])
        
        #MR1
        finalDF.at[inputTestID[index],'MR1_checker'] = mr.mr_PER(row['output_MR1'])

        #MR2
        finalDF.at[inputTestID[index],'MR2_checker'] = mr.mr_ADD(row['output_MR2'])

        #MR3
        finalDF.at[inputTestID[index],'MR3_checker'] = mr.mr_MUL(row['output_MR3'])

        #MR4
        if row['output_MR4'] == 'd/0':
            finalDF.at[inputTestID[index],'MR4_checker'] ='NA -> d/0'
        else:
            finalDF.at[inputTestID[index],'MR4_checker'] = mr.mr_INV(row['output_MR4'])

        #MR5
        finalDF.at[inputTestID[index],'MR5_checker'] = mr.mr_INC(row['output_MR5'])

        #MR6
        finalDF.at[inputTestID[index],'MR6_checker'] = mr.mr_EXC(row['output_MR6'])


    # finalDF.to_csv('add_values_MRChecker.csv')
    save_csv(finalDF, outputchecker, pathChecker)
    save_json(finalDF, outputchecker, pathChecker)

def save_json(df, output, savePath):
    
    df.to_json(savePath + '/' + output + '.json', indent= 4, orient="index")


def save_csv(df, output, savePath):
    df.to_csv(savePath + '/' + output + '.csv')

if __name__ == '__main__':

    import click 

    global mainDF
    mainDF = pd.DataFrame()

    global auxListmainDF
    auxListmainDF = []

    @click.command()
    @click.option('-i', '--input_path', 'input_path')
    @click.option('-o', '--output', 'output')


    def main(input_path, output):
        
        mainPathOutputs = str(pathlib.Path().absolute()) + '/' + 'SUT_outputs'
        mainPathMRChecker = str(pathlib.Path().absolute()) + '/' + 'MR_Checker'
        try:
            os.mkdir(mainPathOutputs)
        except:
            pass
        try:
            os.mkdir(mainPathMRChecker)
        except:
            pass

        with open(input_path, "r") as readfile:
            testData = json.load(readfile)
            json.dumps(testData, indent = 4)

        inputTestID = list(testData.keys())
        dataExecution(inputTestID, testData, 'output_' + output, 'MrChecker_' + output, mainPathOutputs, mainPathMRChecker)

main()