#include "Store.h"
#include <algorithm>

void Store::addPs(int price, int quality, int generation) {
    PS ps(price, quality, generation);
    pss.push_back(ps);
    std::cout << "Adding: " << ps.getInfo() << std::endl;
}

void Store::addXbox(int price, int quality) {
    Xbox xbox(price, quality);
    xboxes.push_back(xbox);
    std::cout << "Adding: " << xbox.getInfo() << std::endl;
}

void Store::remove(ConsoleType consoleType) {
    if (consoleType == ConsoleType::PS) {
        PS last = pss.back();
        pss.pop_back();
        std::cout<<"Removing: "<<last.getInfo()<<std::endl;
    }else if(consoleType==ConsoleType::XBOX){
        Xbox last = xboxes.back();
        xboxes.pop_back();
        std::cout<<"Removing: "<<last.getInfo()<<std::endl;
    }
}

void Store::sortByPrice(ConsoleType consoleType) {
    if (consoleType == ConsoleType::PS){
        std::sort(pss.begin(), pss.end(), [](const PS& ps1, const PS& ps2){return ps1.getPrice()>ps2.getPrice();});
        std::cout<<"Sorting all PS by price"<<std::endl;
    } else if(consoleType==ConsoleType::XBOX){
        std::sort(xboxes.begin(), xboxes.end(), [](const Xbox& xbox1, const Xbox& xbox2){return xbox1.getPrice()>xbox2.getPrice();});
        std::cout<<"Sorting all Xbox by price"<<std::endl;
    }
}

void Store::sortByQuality(ConsoleType consoleType) {
    if (consoleType == ConsoleType::PS){
        std::sort(pss.begin(), pss.end(), [](const PS& ps1, const PS& ps2){return ps1.getQuality()>ps2.getQuality();});
        std::cout<<"Sorting all PS by quality"<<std::endl;
    } else if(consoleType==ConsoleType::XBOX){
        std::sort(xboxes.begin(), xboxes.end(), [](const Xbox& xbox1, const Xbox& xbox2){return xbox1.getQuality()>xbox2.getQuality();});
        std::cout<<"Sorting all Xbox by quality"<<std::endl;
    }

}

void Store::print(ConsoleType consoleType) {
    if (consoleType == ConsoleType::PS){
        std::cout<<"Printing all PS data"<<std::endl;
        for(const auto& ps:pss){
            std::cout<<ps.getInfo()<<std::endl;
        }
    }
    else if(consoleType==ConsoleType::XBOX){
        std::cout<<"Printing all Xbox data"<<std::endl;
        for(const auto& xbox:xboxes){
            std::cout<<xbox.getInfo()<<std::endl;
        }
    }

}
