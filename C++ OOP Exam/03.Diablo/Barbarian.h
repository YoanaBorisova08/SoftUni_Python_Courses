//
// Created by User on 12-Sep-21.
//

#ifndef INC_03_DIABLO_BARBARIAN_H
#define INC_03_DIABLO_BARBARIAN_H

#include "Hero.h"

class Barbarian : public Hero {
protected:
    int damageTurn=0;

public:
    Barbarian(const VitalData &vitalData);
    ~Barbarian();

    void readSpellFromInput(SpellType spellType) override;

    //returns the produced damage
    int castSpell() override;

    void takeDamage(int damage) override;

    void regenerate() override;

    bool isDead() const override;
};

#endif //INC_03_DIABLO_BARBARIAN_H
