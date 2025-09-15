cmake_minimum_required(VERSION 3.20)
project(02_ConsoleGame)

set(CMAKE_CXX_STANDARD 11)

add_executable(02_ConsoleGame main.cpp Defines.h CommandExecutor.h CommandExecutor.cpp Store.h Store.cpp PS.h Xbox.h)
