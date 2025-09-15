#include "InputParser.h"
#include <iostream>

Input readInput(){
    std::string line;
    char letter;
    int repetitions;
   std::cin>>line>> letter>>repetitions;
   Input input;
   input.line = line;
   input.letter=letter;
   input.repetitions=repetitions;
   return input;
}
