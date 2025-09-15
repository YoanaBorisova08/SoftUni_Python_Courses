cmake_minimum_required(VERSION 3.20)
project(03_Diablo)

set(CMAKE_CXX_STANDARD 11)

add_executable(03_Diablo main.cpp Structs.h Hero.h Defines.h BattleField.cpp BattleField.h Barbarian.h Amazon.h Barbarian.cpp Amazon.cpp)
