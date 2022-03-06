#include <iostream>
#include <string>
using namespace std;

class Stocks {
    public:
    string company;
    string industry;
    string sector;
    int year;
};

int main () {

    Stocks stocksObj1;
    stocksObj1.industry = "Beverages-Non Alcoholic";
    stocksObj1.sector = "Consumer Defensive";
    stocksObj1.company ="Coca Cola Co";
    stocksObj1.year = 1999;

    Stocks stocksObj2;
    stocksObj2.industry = "Beverages-Non Alcoholic";
    stocksObj2.sector = "Consumer Defensive";
    stocksObj2.company ="Pepsico Inc";
    stocksObj2.year = 1969;

    cout << stocksObj1.industry << " " << stocksObj1.sector << " " << stocksObj1.company << " " << stocksObj1.year << "\n";
    cout << stocksObj2.industry << " " << stocksObj2.sector << " " << stocksObj2.company << " " << stocksObj2.year << "\n";
    return 0;
}




