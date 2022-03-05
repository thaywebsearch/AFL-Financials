#include <iostream>
#include <string>
using namespace std;

class Stocks {
    public:
    string industry;
    string sector;
    int ticker;
};

int main () {

    Stocks stocksObj1;
    stocksObj1.industry = "Beverages-Non Alcoholic";
    stocksObj1.sector = "Consumer Defensive";
    stocksObj1.ticker = PEP;

    Stocks stocksObj2;
    stocksObj2.industry = "Beverages-Non Alcoholic";
    stocksObj2.sector = "Consumer Defensive";
    stocksObj2.ticker = KO;

     cout << stocksObj1.industry << " " << stocksObj1.sector << " " << stocksObj1.ticker << "\n";
    cout << stocksObj2.industry << " " << stocksObj2.sector << " " << stocksObj2.ticker << "\n";
    return 0;
}




