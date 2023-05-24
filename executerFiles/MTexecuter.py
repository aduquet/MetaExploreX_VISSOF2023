import math
import struct


class MTexecuter:
    
    def __init__(self, inputA):
        self.inputA = inputA
    
    def mr_PER(self, inputB):
        try:
            if type(self.inputA) and type(inputB) != list:
            ## MR1 -> No violation when the output remain constant
                if type(self.inputA) and type(inputB) != str:
                    if math.isclose(self.inputA, inputB, rel_tol=1e-9, abs_tol=0):
                        return 'Not-violated'

                    if not math.isclose(self.inputA, inputB, rel_tol=1e-9):
                        return 'Violated'
                else:
                    return 'NA input type'
            
            else:
                self.inputA.sort()
                inputB.sort()
                if not self.inputA == inputB:
                    return 'Violated'

                else:
                    return 'Not-violated'
        
        except:
            return 'something happend'
    
    def mr_ADD(self, inputB):
        ## MR2 -> No violation when the output increace remain constant
        try:
            if type(self.inputA) and type(inputB) != str:
                if math.isclose(self.inputA, inputB, rel_tol=1e-9, abs_tol=0) or self.inputA < inputB:
                    return 'Not-violated'
                
                # if math.isclose(self.inputA,self.inputB, rel_tol=1e-9, abs_tol=0) and self.inputA < self.inputB:
                else:
                    return 'Violated'
            return 'NA input type'
        except:
            return 'something happend'

    def mr_ADD2(self, inputB):
        ## MR2 -> No violation when the output increace remain constant
        try:
            if type(self.inputA) and type(inputB) != str:
                if math.isclose(self.inputA, inputB, rel_tol=1e-9, abs_tol=0) or self.inputA > inputB:
                    return 'Not-violated'
                
                # if math.isclose(self.inputA,self.inputB, rel_tol=1e-9, abs_tol=0) and self.inputA < self.inputB:
                else:
                    return 'Violated'
            return 'NA input type'
        except:
            return 'something happend'

    def mr_MUL(self, inputB):
        ## MR3_MUL -> No violation when the output increace remain constant
        try: 
            if type(self.inputA) and type(inputB) != str:
                if math.isclose(self.inputA, inputB, rel_tol=1e-9, abs_tol=0) or self.inputA < inputB:
                    return 'Not-violated'
                
                # if math.isclose(self.inputA,self.inputB, rel_tol=1e-9, abs_tol=0) and self.inputA < self.inputB:
                else:
                    return 'Violated'
            else:
                'NA input type'
        except:
            return 'something happend'

    def mr_MUL2(self, inputB):
        ## MR3_MUL -> No violation when the output decrease
        try: 
            if type(self.inputA) and type(inputB) != str:
                if math.isclose(self.inputA, inputB, rel_tol=1e-9, abs_tol=0) or self.inputA > inputB:
                    return 'Not-violated'
                
                else:
                    return 'Violated'
            else:
                'NA input type'
        except:
            return 'something happend'

    def mr_INV(self, inputB):
        ## MR4 -> No violation when the output decrease or remain constant
        try:
            if type(self.inputA) and type(inputB) != str:

                if math.isclose(self.inputA, inputB, rel_tol=1e-9, abs_tol=0) or self.inputA > inputB:
                    return 'Not-violated'
                
                # if math.isclose(self.inputA,self.inputB, rel_tol=1e-9, abs_tol=0) and self.inputA < self.inputB:
                else:
                    return 'Violated'
            else:
                'NA input type'
        
        except:
            return 'something happend'
    
    def mr_INV2(self, inputB):
        ## MR4 -> No violation when the output increase
        try:
            if type(self.inputA) and type(inputB) != str:

                if math.isclose(self.inputA, inputB, rel_tol=1e-9, abs_tol=0) or self.inputA < inputB:
                    return 'Not-violated'
                
                # if math.isclose(self.inputA,self.inputB, rel_tol=1e-9, abs_tol=0) and self.inputA < self.inputB:
                else:
                    return 'Violated'
            else:
                'NA input type'
        
        except:
            return 'something happend'

    def mr_INC(self, inputB):
        ## MR5 -> No violation when the output increase or remain constant
        try:
            if type(self.inputA) and type(inputB) != str:

                if math.isclose(self.inputA, inputB, rel_tol=1e-9, abs_tol=0) or self.inputA < inputB:
                    return 'Not-violated'
                
                else:
                    return 'Violated'
            else:
                'NA input type'
        except:
            return 'something happend'
    
    def mr_INC2(self, inputB):
        ## MR5 -> No violation when the output decrease
        try:
            if type(self.inputA) and type(inputB) != str:

                if math.isclose(self.inputA, inputB, rel_tol=1e-9, abs_tol=0) or self.inputA > inputB:
                    return 'Not-violated'
                
                else:
                    return 'Violated'
            else:
                'NA input type'
        except:
            return 'something happend'

    def mr_EXC(self, inputB):
        ## MR6 -> No violation when the output decrease or remain constant
        try:
            if type(self.inputA) and type(inputB) != str:
                if math.isclose(self.inputA, inputB, rel_tol=1e-9, abs_tol=0) or self.inputA > inputB:
                    return 'Not-violated'
                
                else:
                    return 'Violated'
            else:
                'NA input type'

        except:
            return 'something happend'
    
    def mr_EXC2(self, inputB):
        ## MR6 -> No violation when the output increase
        try:
            if type(self.inputA) and type(inputB) != str:
                if math.isclose(self.inputA, inputB, rel_tol=1e-9, abs_tol=0) or self.inputA < inputB:
                    return 'Not-violated'
                
                else:
                    return 'Violated'
            else:
                'NA input type'

        except:
            return 'something happend'