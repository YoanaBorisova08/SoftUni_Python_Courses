#include "Barbarian.h"
#include "Defines.h"

Barbarian::Barbarian(const VitalData &vitalData) : Hero() {
   this->_vitalData = vitalData;
   this->_name = BARBARIAN_NAME ;
}

Barbarian::~Barbarian() = default;

void Barbarian::readSpellFromInput(SpellType spellType){

    if(spellType==SpellType::Weak){
        std::cin>>_spells[0].name>>_spells[0].damage;
    }else if(spellType==SpellType::Strong){
        std::cin>>_spells[1].name>>_spells[1].damage>>_spells[1].manaCost;
    }

}

//returns the produced damage
int Barbarian::castSpell() {
 if(_vitalData.currMana>=_spells[1].manaCost){
     std::cout<<"Barbarian casting "<< _spells[1].name<< " for "<<_spells[1].manaCost<<" mana"<<std::endl;
     _vitalData.currMana-=_spells[1].manaCost;
     if(_vitalData.currMana<0){
         _vitalData.currMana=0;
     }
     return _spells[1].damage;
 }else{
     std::cout<<"Barbarian casting "<< _spells[0].name<< " for "<<_spells[0].manaCost<<" mana"<<std::endl;
     return _spells[0].damage;
 }
}

void Barbarian::takeDamage(int damage) {
    damageTurn++;
    if(damageTurn==BARBARIAN_PASSIVE_ABILITY_COUNTER){
        damage/=2;
        damageTurn=0;
    }
    _vitalData.health-=damage;
    std::cout<<"Barbarian took "<<damage<<" damage and is left with "<<_vitalData.health<< " health "<<std::endl;
}

void Barbarian::regenerate() {
    int regMana = _vitalData.manaRegenRate;
    _vitalData.currMana+=regMana;
    if(_vitalData.currMana>_vitalData.maxMana){
        regMana=_vitalData.currMana-_vitalData.maxMana;
        _vitalData.currMana=_vitalData.maxMana;

    }

    std::cout<<"Barbarian regained "<<regMana<<" mana for up to "<<_vitalData.currMana<<std::endl;
}

bool Barbarian::isDead() const {
  if(_vitalData.health<=0){
      return true;
  }
  return false;
}