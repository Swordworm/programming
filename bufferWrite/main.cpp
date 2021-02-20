#include <iostream>
#include <string>
#include <fstream>

using namespace std;

class Buffer {
public:
    Buffer( string enteredMessage ) {
        this->message = enteredMessage;
    };
    void writeToDocument() {
        ofstream write ("../bufferWrite/buffer.txt", ios::out | ios::app);
        if ( write.is_open() ) {
            write << message << endl;
            cout << "The message was written!" << endl;
            write.close();
        } else {
            cout << "An error has occupied!" << endl;
        }
    };
private:
    string message;
};

int main() {
    string message;
    cout << "Enter the message: ";
    getline(cin, message);
    Buffer buffer(message);
    buffer.writeToDocument();
    return 0;
}
