//
// Created by User on 12-Sep-21.
//

#ifndef INC_03_DIABLO_AMAZON_H
#define INC_03_DIABLO_AMAZON_H

#include "Hero.h"

class Amazon : public Hero {
protected:
    int counter=0;
public:
    Amazon(const VitalData &vitalData);
    ~Amazon();

    void readSpellFromInput(SpellType spellType) override;

    //returns the produced damage
    int castSpell() override;

    void takeDamage(int damage) override;

    void regenerate() override;

    bool isDead() const override;
};


#endif //INC_03_DIABLO_AMAZON_H
