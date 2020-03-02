#writing a file
print("writing a text file")
text_file = open("write_file.txt","w")
text_file.write("Akash")
#reading a file 
text_file = open("write_file.txt","rb")
print text_file.read()

text_file.close()
