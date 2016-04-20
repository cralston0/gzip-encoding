# Disclaimer: This is the worst Makefile ever.

CPR_SRC = $(wildcard cpr/cpr/*.cpp)
CPR_OBJ = $(patsubst cpr/cpr/%.cpp, obj/%.o, $(CPR_SRC))

all : client

GZipCodec.o : GZipCodec/GZipCodec.cpp
	g++ -c GZipCodec/GzipCodec.cpp -lz -std=c++11 -IGZipCodec

obj/%.o: cpr/cpr/%.cpp
	g++ -o $@ -c $< -std=c++11 -Icpr/include

client : GZipCodec.o $(CPR_OBJ) client.cpp
	g++ -o client client.cpp $(CPR_OBJ) GZipCodec.o -lz -lcurl -std=c++11 -I. -Icpr/include -Ijson/src

.PHONY : clean
clean :
	-rm client *.o obj/*.o
