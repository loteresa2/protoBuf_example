from django.shortcuts import render
from django.http import HttpResponse
import person_pb2
import os
'''In linux use protoc -I=. --python_out=. person.proto to compile'''
# Create your views here.
def index():
	person = person_pb2.Person()
	script_dir = os.path.dirname(__file__)
	rel_path = "dummy"
	abs_file_path = os.path.join(script_dir, rel_path)	
	if not os.path.exists(abs_file_path):
		file(abs_file_path, 'w').close()
	writeFile(abs_file_path, person)
	readFile(abs_file_path, person)

# Write the new person book back to disk.
def writeFile(abs_file_path, person):
	promptForPerson(person)
	f = open(abs_file_path, "wb")
	f.write(person.SerializeToString())
	f.close()

#Read and print from person book
def readFile(abs_file_path, person):
	person_book = person_pb2.Person()
	try:
		f = open(abs_file_path, "rb")
	  	person_book.ParseFromString(f.read())
	  	f.close()
	except IOError:
		print abs_file_path + ": Could not open file" 

	print "Reading.."
	print "Name "+person_book.name
	print person_book.id

# This function fills in a Person message based on user input.
def promptForPerson(person):
  person.name = "MyName"
  person.id = 1

if __name__ == "__main__":
	index()
