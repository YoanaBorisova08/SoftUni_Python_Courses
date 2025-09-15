

#ifndef INC_01_STRINGWRAPPER_STRINGWRAPPER_H
#define INC_01_STRINGWRAPPER_STRINGWRAPPER_H
#include <string>
#include <iostream>


class StringWrapper{
private:
    const std::string _line;
    const char _letter;
    const int _repetitions;
    int num=0;
    std::string contet;
public:
    StringWrapper():_line(" "), _letter(' '), _repetitions(0), num(2){}
    StringWrapper(const std::string& line):_line(line), _letter(' '), _repetitions(0), num(0){}
    StringWrapper(char letter, int repetitions) : _line(" "), _letter(letter), _repetitions(repetitions), num(1){}

    std::string getContent()const{
        std::string output;
        if(num==0){
            output+=_line;
        }
        else if(num==1){
            for(int i=0; i<_repetitions; i++){
                output=output+(_letter);
            }
        }
        return output;
    }

    StringWrapper& append(const std::string& str ){
        contet.append(str);
        return *this;
    }

    void printContent()const{
        std::cout<<contet<<std::endl;
    }



};

#endif //INC_01_STRINGWRAPPER_STRINGWRAPPER_H
