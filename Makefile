#/usr/bin/sh
# Build Algerian Sign Language 3D avatar

default: all
# Clean build files
clean:
	
backup: 
	
#create all files 
all:
# Publish to github
publish:
	git push origin master 

server:
	# run server
	python3 -m http.server 
test:
	python -m unittest discover tests
test3:
	python3 -m unittest discover tests
docs:
	epydoc -v --config epydoc.conf
SOURCE=../source-data
OUTPUT=output
test_all:
	# test generate all files to output
	cd tests;python extract_data_word_list.py  -s $(SOURCE)  -o $(OUTPUT) -a all

test_json:
	# test generate json file to output
	cd tests;python extract_data_word_list.py  -s $(SOURCE)  -o $(OUTPUT) -a json

test_wordlist:
	# test generate wordlist file to output
	cd tests;python extract_data_word_list.py  -s $(SOURCE)  -o $(OUTPUT) -a wordlist

test_categories:
	# test generate categories file to output
	cd tests;python extract_data_word_list.py  -s $(SOURCE)  -o $(OUTPUT) -a categories

test_stat:
	# test generate statistics file to output
	cd tests;python extract_data_word_list.py  -s $(SOURCE)  -o $(OUTPUT) -a statistics
