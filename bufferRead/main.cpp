#include <iostream>
#include <string>
#include <cstring>
#include <fstream>
using namespace std;

class Buffer {
public:
    void readFromDocument() {
        ifstream read ("../bufferWrite/buffer.txt", ios::in);
        int counter = 1;
        if ( read.is_open() ) {
            cout << "Result:" << endl;
            while ( getline ( read, message ) ) {
                cout << counter << ". " << message << endl;
                counter++;
            }
            read.close();
        } else {
            cout << "An error has occupied, the file was not opened!" << endl;
        }
    }
private:
    string message;
};

void ask();

int main() {

    ask();

    return 0;
}

void ask() {
    string response;
    cout << "Do you want to read the file? (yes/no) ";
    cin >> response;
    if (response == "yes" ) {
        Buffer buffer;
        buffer.readFromDocument();
    } else if (response == "no" ) {
        cout << "Good bye!" << endl;
    } else {
        cout << "Incorrect answer, try one more time!" << endl;
        ask();
    }
}
