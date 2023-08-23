SIZE_MEMORY=2**11
SIZE_PROGRAM=2**7

class pardazesh():

    def __init__(self):

        self.flagupload=0

        self.memory_asly_lable=[]
        self.program_asly_lable=[]

        self.memory_lable=["" for i in range(SIZE_MEMORY)]
        self.memory_instruction=["" for i in range(SIZE_MEMORY)]
        self.compile_code_asmbly=[0 for i in range(SIZE_MEMORY)]

        self.program_lable=["" for i in range(SIZE_PROGRAM)]
        self.program_instruction=["" for i in range(SIZE_PROGRAM)]
        self.compile_code_program=[0 for i in range(SIZE_PROGRAM)]
        self.program_code=[[0,0,0,0,0,0] for i in range(SIZE_PROGRAM)]

        self.AC=0;self.PC=0;self.DR=0;self.AR=0;self.CAR=64;self.SBR=0
        self.S=True

        self.ACcopy=0;self.PCcopy=0;self.DRcopy=0;self.ARcopy=0;self.CARcopy=64;self.SBRcopy=0

        self.memory_value=[]
        self.program_value=[]
        
    def valid_f1(self,f):
        f1=["NOP","ADD","CLRAC","INCAC","DRTAC","DRTAR","PCTAR","WRITE"]
        for i in range(8):
            if(f1[i]==f):
                return i
        return -1

    def valid_f2(self,f):
        f2=["NOP","SUB","OR","AND","READ","ACTDR","INCDR","PCTDR"]
        for i in range(8):
            if(f2[i]==f):
                return i
        return -1

    def valid_f3(self,f):
        f3=["NOP","XOR","COM","SHL","SHR","INCPC","ARTPC"]
        for i in range(7):
            if(f3[i]==f):
                return i
        return -1

    def valid_lable(self,lable,asly_lables):
        
        for lbl in asly_lables:
            if(lbl[0])==lable:
                return lbl[1]
                
        return -1
    
    def lbl(self,chr,codes,lables,asly_lables):

        address=-1
        for i in range(len(codes)):

            if(len(codes[i])==0):{}

            elif(codes[i][0]=="ORG"):
                if(len(codes[i])>2):return False
                try:    
                    address=int(codes[i][1])
                except:return False

            elif(codes[i][0]=="END"):
                if(len(codes[i])>1):return False
                break

            elif(address==-1):return False

            else:
                if (codes[i][0][-1]==chr):
                    lables[address]=codes[i][0][0:-1]

                    asly_lables.append((codes[i][0][0:-1],address))#ساخت جدول لیبل ها و ادرسشان
                    codes[i].pop(0)

                address+=1 

        return True

    def assembler(self,str_code):
        codes=str_code.split("\n")
        for i in range(len(codes)):
            codes[i]=codes[i].split()
        return codes

    def assembler_asembly(self,str_code):

        self.memory_asly_lable=[]

        self.memory_lable=["" for i in range(SIZE_MEMORY)]
        self.memory_instruction=["" for i in range(SIZE_MEMORY)]
        self.compile_code_asmbly=[0 for i in range(SIZE_MEMORY)]

        codes=self.assembler(str_code)
        if(self.lbl(',',codes,self.memory_lable,self.memory_asly_lable)==False):return False
        
        address=-1
        for i in range(len(codes)):

            self.compile_code_asmbly[address]=0

            if(len(codes[i])==0):{}

            elif(codes[i][0]=="ORG"):
                address=int(codes[i][1])
                
            elif(codes[i][0]=="END"):
                break

            elif(address==-1):return False

            elif(codes[i][0]=="DEC"):
                if(len(codes[i])==2):
                    self.compile_code_asmbly[address]=int(codes[i][1])
                    self.memory_instruction[address]=" ".join(codes[i])
                    address+=1
                else:return False

            elif(codes[i][0]=="HEX"):
                if(len(codes[i])==2):
                    self.compile_code_asmbly[address]=int(codes[i][1])
                    self.memory_instruction[address]=" ".join(codes[i])
                    address+=1
                else:return False

            else:
                if(codes[i][0]=="HLT" ):
                    address_microprogram=30
                else:
                    address_microprogram=self.valid_lable(codes[i][0],self.program_asly_lable)
                if (address_microprogram!=-1):

                    self.compile_code_asmbly[address]+=((address_microprogram%32)//2)*(2**11)
                    if(len(codes[i])>1):

                        try:
                            address_memory=int(codes[i][1])
                        except:
                            address_memory=self.valid_lable(codes[i][1],self.memory_asly_lable)

                        if(address_memory!=-1):
                            self.compile_code_asmbly[address]+=address_memory
                    
                            if(len(codes[i])==3 and codes[i][2]=='I'):
                                self.compile_code_asmbly[address]+=(2**15)

                            elif(len(codes[i])!=2):return False

                        else:return False
                    
                else:return False
                self.memory_instruction[address]=" ".join(codes[i])

                address+=1

        return True
        

    def assembler_program(self,str_code):

        self.program_asly_lable=[]

        self.program_lable=["" for i in range(SIZE_PROGRAM)]
        self.program_instruction=["" for i in range(SIZE_PROGRAM)]
        self.compile_code_program=[0 for i in range(SIZE_PROGRAM)]
        self.program_code=[[0,0,0,0,0,0] for i in range(SIZE_PROGRAM)]

        codes=self.assembler(str_code)
        if(self.lbl(':',codes,self.program_lable,self.program_asly_lable)==False):return  False

        address=-1
        for i in range(len(codes)):

            self.compile_code_program[address]=0

            if(len(codes[i])==0):{}

            elif(codes[i][0]=="ORG"):
                address=int(codes[i][1])
                
            elif(codes[i][0]=="END"):
                break

            elif(address==-1):return False

            else:
                if(len(codes[i])!=3 and len(codes[i])!=4):return False

                f_code=codes[i][0].split(',')
                f1=0
                f2=0
                f3=0
                for f in f_code:
                    flag=False
                    if(f1==0):
                        f1=self.valid_f1(f)
                        if(f1==-1):f1=0
                        else:flag=True
                    if(flag==False and f2==0):
                        f2=self.valid_f2(f)
                        if(f2==-1):f2=0
                        else:flag=True
                    if(flag==False and f3==0):
                        f3=self.valid_f3(f)
                        if(f3==-1):f3=0
                        else:flag=True
                    if(flag==False):
                        return False
                self.program_code[address][0]=f1
                self.program_code[address][1]=f2
                self.program_code[address][2]=f3
                self.compile_code_program[address]+=(2**17)*f1+(2**14)*f2+(2**11)*f3

                if(codes[i][1]=="U"):x=0  
                elif(codes[i][1]=="I"):x=1
                elif(codes[i][1]=="S"):x=2
                elif(codes[i][1]=="Z"):x=3
                else:return False

                self.program_code[address][3]=x
                self.compile_code_program[address]+=x*(10**9)

                if(codes[i][2]=="JMP"):x=0  
                elif(codes[i][2]=="CALL"):x=1
                elif(codes[i][2]=="RET"):x=2
                elif(codes[i][2]=="MAP"):x=3
                else:return False

                self.program_code[address][4]=x
                self.compile_code_program[address]+=x*(10**7)

                if(len(codes[i])==3):
                    self.program_code[address][5]=0
                    self.compile_code_program[address]+=0
                else:
                    if(codes[i][3]=="NEXT"): 
                        self.program_code[address][5]=address+1
                        self.compile_code_program[address]+=address+1
                    else:
                        address_microprogram=self.valid_lable(codes[i][3],self.program_asly_lable)
                        if(address_microprogram!=-1):
                            self.program_code[address][5]=address_microprogram
                            self.compile_code_program[address]+=address_microprogram
                        else:return False

                self.program_instruction[address]=" ".join(codes[i])
                address+=1 

              
        return True

    def upload_code(self):

        self.AC=0;self.PC=0;self.DR=0;self.AR=0;self.CAR=64;self.SBR=0
        self.S=True

        self.ACcopy=0;self.PCcopy=0;self.DRcopy=0;self.ARcopy=0;self.CARcopy=64;self.SBRcopy=0

        self.memory_value=self.compile_code_asmbly.copy()
        self.program_value=self.compile_code_program.copy()

    def run_f1(self,f1):
        
        if(f1==1):self.AC=self.ACcopy+self.DRcopy
        elif(f1==2):self.AC=0
        elif(f1==3):self.AC=self.ACcopy+1
        elif(f1==4):self.AC=self.DRcopy
        elif(f1==5):self.AR=(self.DRcopy)%(2**11)
        elif(f1==6):self.AR=self.PCcopy
        elif(f1==7):self.memory_value[self.ARcopy]=self.DRcopy

    def run_f2(self,f2):
        
        if(f2==1):self.AC=self.ACcopy-self.DRcopy
        elif(f2==2):self.AC=self.ACcopy | self.DRcopy
        elif(f2==3):self.AC=self.ACcopy & self.DRcopy
        elif(f2==4):self.DR=self.memory_value[self.ARcopy]
        elif(f2==5):self.DR=self.ACcopy
        elif(f2==6):self.DR=self.DRcopy+1
        elif(f2==7):self.DR=self.PCcopy

    def run_f3(self,f3):
        
        if(f3==1):self.AC=self.ACcopy ^ self.DRcopy
        elif(f3==2):self.AC=~self.ACcopy
        elif(f3==3):self.AC=self.ACcopy<<1
        elif(f3==4):self.AC=self.ACcopy>>1
        elif(f3==5):self.PC=self.PCcopy+1
        elif(f3==6):self.PC=self.ARcopy
        

    def run_BR(self,CD,BR,AD):

        if(CD==0 or (CD==1 and self.DR//(2**15)==1) or (CD==2 and self.AC//(2**15)==1) or (CD==3 and self.AC==0)):
            if(BR==0):self.CAR=AD
            elif(BR==1):
                self.SBR=self.CAR+1
                self.CAR=AD
            elif(BR==2):self.CAR=self.SBR
            elif(BR==3):self.CAR=((self.DR%(2**15))//(2**11))*2
        else:
            self.CAR+=1
    

    def step_run(self):
        
        if(self.S==False):return False

        self.ACcopy=self.AC;self.PCcopy=self.PC;self.DRcopy=self.DR;self.ARcopy=self.AR;self.CARcopy=self.CAR;self.SBRcopy=self.SBR
        if(self.CAR==30):
            self.S=False #HLT
        else:
            F1=self.program_code[self.CAR][0]
            F2=self.program_code[self.CAR][1]
            F3=self.program_code[self.CAR][2]
            self.run_f1(F1)
            self.run_f2(F2)
            self.run_f3(F3)

            CD=self.program_code[self.CAR][3]
            BR=self.program_code[self.CAR][4]
            AD=self.program_code[self.CAR][5]

            self.run_BR(CD,BR,AD)
        return True

    

    def run(self):
        while(True):
            if(self.step_run()==False):
                break
        


def main():
    str1="ORG 100\n LDA SUB \n CMA \n INC \n ADD  MIN \n STA DIF \nHLT \nMIN,  DEC 83 \n SUB,  DEC -23 \n DIF,  HEX 0  \nEND"
    str2="ORG 0\nADD: NOP I CALL INDRCT\nREAD U JMP NEXT\nADD U JMP FETCH\nORG 16\nINDRCT: READ U JMP NEXT\nDRTAR U RET\n ORG 64\nFETCH: PCTAR U JMP NEXT\n READ,INCPC U JMP NEXT\nDRTAR U MAP"
    comp= pardazesh()
    
    comp.assembler_program(str2)
    comp.assembler_asembly(str1)
    comp.step_run()
    


if __name__ == '__main__':
    main()

        