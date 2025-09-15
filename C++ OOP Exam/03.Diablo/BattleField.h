

#ifndef INC_03_DIABLO_BATTLEFIELD_H
#define INC_03_DIABLO_BATTLEFIELD_H
#include <vector>
#include <iostream>
#include <memory>
#include "Hero.h"

class BattleField{
private:
    std::vector<std::unique_ptr<Hero>> _heroes;
public:
    void createHeroes();

    void createSpells();

    void startBattle();

    void printWinner(const std::unique_ptr<Hero> &hero);
};

#endif //INC_03_DIABLO_BATTLEFIELD_H
