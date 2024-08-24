# opening the file in read mode 
my_file = open("words.txt", "r") 
  
# reading the file 
data = my_file.read() 
  
# replacing end splitting the text  
# when newline ('\n') is seen. 
data_into_list = data.split("\n") 
print(data_into_list) 
my_file.close() 