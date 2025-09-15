cmake_minimum_required(VERSION 3.20)
project(01_StringWrapper)

set(CMAKE_CXX_STANDARD 14)

add_executable(01_StringWrapper main.cpp InputParser.h StringWrapper.h InputParser.cpp)
