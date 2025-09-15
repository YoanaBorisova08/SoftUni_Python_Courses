
#ifndef INC_02_CONSOLEGAME_STORE_H
#define INC_02_CONSOLEGAME_STORE_H
#include "Defines.h"
#include <iostream>
#include <vector>
#include "PS.h"
#include "Xbox.h"

class Store {
protected:
    std::vector<PS> pss;
    std::vector<Xbox>xboxes;


public:
    Store(){}

    void addPs(int price, int quality, int generation);

    void addXbox(int price, int quality);

    void remove(ConsoleType consoleType);

    void sortByPrice(ConsoleType consoleType);

    void sortByQuality(ConsoleType consoleType);

    void print(ConsoleType consoleType);

};

#endif //INC_02_CONSOLEGAME_STORE_H
