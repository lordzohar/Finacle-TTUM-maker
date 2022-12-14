import openpyxl
import pandas as pd
def createttum(input, sheetname, output):
	wb=openpyxl.load_workbook(input)
	ws= wb[sheetname]
	data = ws.values
	col=next(data)[0:]
	df =pd.DataFrame(data,columns=col)
	df = df[df['Transaction Amount'].notna()]

	ttum=df.iloc[:,0].apply(lambda x: str(x).ljust(16," "))+df.iloc[:,1].astype(str)+df.iloc[:,2].apply(lambda x: str(x).ljust(8," "))+df.iloc[:,3].astype(str)+df.iloc[:,4].apply(lambda x: "{0:.2f}".format(float(x)).rjust(17," "))+df.iloc[:,5].apply(lambda x: str(x[0:30]).ljust(30," ")) +df.iloc[:,6].apply(lambda x: " "*5 if str(x).lower() in ["nan","none"] else str(x).ljust(5, " "))+" "*78+ df.iloc[:,15].apply(lambda x: str(x).ljust(5," ")) +" "*15+df.iloc[:,17].apply(lambda x: str(x).ljust(10," "))+df.iloc[:,18].apply(lambda x: str(x).ljust(10," ")) + " "*755
	
	ttum.to_csv(output, index=False, header=False)
if __name__=='__main__':
    
	createttum('inputfile.xlsx','Sheet1','TTUM\\TTUM.txt')