import binascii
from datetime import datetime,timedelta
import platform
import sys
import argparse

def parse_i(file_name):
	f=open(file_name,'rb')
	#print f
	l=[]
	for i in binascii.hexlify(f.read()):
		l.append(i)
	#print l
	zipped = zip(l[0::2],l[1::2])
	clear_list=[]
	for i in zipped:
		temp=''
		for j in i:
			temp=temp+str(j)
		clear_list.append(temp)
	#print clear_list
	#print clear_list
	offset_values={'Header':(0,7),
				'File_Size':(8,15),
				'Del_Time_Stamp':(16,23),
				'File_Name_Length':(24,27),
				'File_Name':28
				}
	offset_data ={'Header':'',
				'File_Size':'',
				'Del_Time_Stamp':'',
				'File_Name_Length':'',
				'File_Name':''
				}
	
	temp=clear_list[offset_values['File_Name_Length'][0]:offset_values['File_Name_Length'][1]+1]
	temp1=''
	for i in temp:
		temp1=temp1+i[::-1]
	temp1=temp1[::-1]
	
	if  int(temp1,16) > 500:
		offset_data.pop('File_Name_Length')
		offset_values.pop('File_Name_Length')
		offset_values['File_Name']=24
	for i in offset_values:
		if i != 'File_Name':
			#print offset_values[i][0] , offset_values[i][1]
			for k in clear_list[offset_values[i][0]:offset_values[i][1]+1]:
				offset_data[i]=offset_data[i]+k[::-1]
			offset_data[i]=offset_data[i][::-1]	
		else:
			#print i,offset_values[i]
			for k in clear_list[offset_values[i]:len(clear_list)-1]:
				if k != '00':
					offset_data[i]=str(offset_data[i])+str(k)
		
	print 'File_Size = ',int(offset_data['File_Size'],16) ,'Bytes'
	print 'Del_Time_Stamp = ',
	time_sec= int(offset_data['Del_Time_Stamp'],16)
	real_time = datetime(1601,1,1,0,0,0) + timedelta(seconds=time_sec/1e7)
	print real_time
	if 'File_Name_Length' in offset_data:
		print 'File_Name_Length = ', int(offset_data['File_Name_Length'],16)
	print 'File_Name  = ',offset_data['File_Name'].decode('hex')
	

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='$I parser , RecycleBin Forensics')
	parser.add_argument('-f','--file',help='Input File name and location')
	args = vars(parser.parse_args())
	print args
	if args:
		z=args['file'].split('\\')
		if z[len(z)-1].startswith('$I'):
			if 'Windows-10' in platform.platform():
				parse_i(args['file'])
		else:
			print 'Please select Appropriate File'
	else:
		print "Hello"