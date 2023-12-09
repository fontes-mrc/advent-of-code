/* 
================================================================================
Advent of Code 20xx
...
================================================================================
*/

#include <iostream>
#include <fstream>
#include <string>
#include <vector>

std::vector<std::string> getInput(){
    std::vector<std::string> input;
    std::ifstream file("input.txt");
    std::string line;
    while (std::getline(file, line)){
        input.push_back(line);
    }
    return input;
}

int part1(std::vector<std::string> input){
    return 0;
}

int part2(std::vector<std::string> input){
    return 0;
}

int main(){
    return 0;
}