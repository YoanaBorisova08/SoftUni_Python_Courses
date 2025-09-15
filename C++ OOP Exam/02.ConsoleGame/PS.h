//
// Created by User on 12-Sep-21.
//

#ifndef INC_02_CONSOLEGAME_PS_H
#define INC_02_CONSOLEGAME_PS_H

class PS{
private:
    int _price=0;
    int _quality=0;
    int _generation=0;
public:
    PS()=default;
    PS(int price, int quality, int generation):_price(price), _quality(quality), _generation(generation){}

    int getPrice()const{
        return _price;
    }

    int getQuality()const{
        return _quality;
    }

    std::string getInfo() const{
        std::string info;

        info.append("PS with generation ").append(std::to_string(_generation)).append(", price: ").append(std::to_string(_price)).
        append(", quality: ").append(std::to_string(_quality));

        return info;
    }



};

#endif //INC_02_CONSOLEGAME_PS_H
