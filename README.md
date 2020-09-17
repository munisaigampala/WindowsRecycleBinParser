# WindowsRecycleBinParser

I_Parser, A python command line script to parse $I File and prints the information

  - Read the information from $I file which belongs to Windows Recycle BIn
  
# Important points related Recycle Bin Forensics
  - Recyclebin or $Recycle.Bin is more like a directory in windows and can be found in every drive.(C:\\$Recycle.Bin\\SID\\$Ixxxxxx)
  - Each Deleted file will move to $Recycle.Bin and gets plit into two files $I and $R
  - $I file contains the metada of the deleted file and $R has the original content.
  
# $I File

  - $I file contains the metadata of the original file
  - Metadata includes
    - Name of the file along with original path, 
    - Size of the file,
    - Time and Date at which the file got deleted
   
# $R File

  - $R File has the original contents of the deleted file
 

![1](https://user-images.githubusercontent.com/61400637/93464936-ac5bb500-f907-11ea-8d30-64d9762835e9.png)


### Installation
Python2 is required to run the file
.
### Execution
```sh
python2 i_parser.py -f $IQ0Q8YU.jpg
```
![2](https://user-images.githubusercontent.com/61400637/93463615-a06ef380-f905-11ea-883f-764d939d4951.png)

