//
// Created by User on 12-Sep-21.
//

#ifndef INC_02_CONSOLEGAME_XBOX_H
#define INC_02_CONSOLEGAME_XBOX_H

class Xbox{
private:
    int _price=0;
    int _quality=0;
public:
    Xbox()=default;
    Xbox(int price, int quality):_price(price), _quality(quality){}

    int getPrice()const{
        return _price;
    }

    int getQuality()const{
        return _quality;
    }

    std::string getInfo()const{
        std::string info;

        info.append("Xbox with price: ").append(std::to_string(_price)).
                append(", quality: ").append(std::to_string(_quality));

        return info;
    }



};


#endif //INC_02_CONSOLEGAME_XBOX_H
