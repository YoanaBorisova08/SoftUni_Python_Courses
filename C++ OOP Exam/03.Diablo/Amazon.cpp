#include "Amazon.h"

Amazon::Amazon(const VitalData &vitalData) : Hero() {
    this->_vitalData = vitalData;
    this->_name = AMAZON_NAME;
}

Amazon::~Amazon() = default;

void Amazon::readSpellFromInput(SpellType spellType){
    if(spellType==SpellType::Weak){
        std::cin>>_spells[0].name>>_spells[0].damage;
    }else if(spellType==SpellType::Strong){
        std::cin>>_spells[1].name>>_spells[1].damage>>_spells[1].manaCost;
    }

}

//returns the produced damage
int Amazon::castSpell() {
    counter++;
    if(counter==2) {
        if (_vitalData.currMana >= _spells[1].manaCost) {
            counter=0;
            int damage = _spells[1].damage;
            damage+=(damage/4);
            std::cout << "Amazon casting " << _spells[1].name << " for " << _spells[1].manaCost << " mana"
                      << std::endl;
            _vitalData.currMana -= _spells[1].manaCost;
            if(_vitalData.currMana<0){
                _vitalData.currMana=0;
            }
            return damage;
        } else {
            counter=0;
            std::cout << "Amazon casting " << _spells[0].name << " for " << _spells[0].manaCost << " mana"
                      << std::endl;
            return  (_spells[0].damage+((_spells[0].damage)/4));
        }
    }else{
        if(_vitalData.currMana>=_spells[1].manaCost){
            std::cout<<"Amazon casting "<< _spells[1].name<< " for "<<_spells[1].manaCost<<" mana"<<std::endl;
            _vitalData.currMana-=_spells[1].manaCost;
            if(_vitalData.currMana<0){
                _vitalData.currMana=0;
            }
            return _spells[1].damage;
        }else{
            std::cout<<"Amazon casting "<< _spells[0].name<< " for "<<_spells[0].manaCost<<" mana"<<std::endl;
            return _spells[0].damage;
        }
    }
}

void Amazon::takeDamage(int damage) {
    _vitalData.health-=damage;
    std::cout<<_name<<" took "<<damage<<" damage and is left with "<<_vitalData.health<< " health "<<std::endl;
}

void Amazon::regenerate() {
    _vitalData.currMana+=_vitalData.manaRegenRate;
    if(_vitalData.currMana>_vitalData.maxMana){
        _vitalData.currMana=_vitalData.maxMana;
    }
    std::cout<<_name<<" regained "<<_vitalData.manaRegenRate<<" mana for up to "<<_vitalData.currMana<<std::endl;
}

bool Amazon::isDead() const {
    if(_vitalData.health<=0){
        return true;
    }
    return false;
}