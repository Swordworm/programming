#include <iostream>
#include <string>
#include <cstdlib>
#include <ctime>

using namespace std;

int ask() {
    int size = 0;

    do {
        if ( size < 0 ) {
            cout << "Array's size must be greater than 0" << endl;
        }
        cout << "Enter the size of the array: ";
        cin >> size;
    } while ( size < 0 );

    return size;
}

int main() {
    srand( time(0));
    int size = ask();
    int array[size];

    for ( int i = 0; i < size; i++) {
        array[i] = rand() % 9;
    }

    // Метод вставки
    for ( int i = 1; i < size; i++ ) {
        for ( int j = i; j > 0 && array[j - 1] > array[j]; j-- ) {
            swap( array[j-1], array[j] );
        }
    }
    cout << "Метод вставки" << endl;
    for ( int i = 0; i < size; i ++ ) {
        cout << array[i] << " ";
    }
    cout << endl;

    for ( int i = 0; i < size; i++) {
        array[i] = rand() % 9;
    }
    
    // Метод пузырька
    for ( int i = 0; i < size - 1; i++ ) {
        for ( int j = 0; j < size - i - 1; j++ ) {
            if ( array[j] > array[j + 1]) {
                swap( array[j + 1], array[j] );
            }
        }
    }

    cout << "Метод пузырька" << endl;
    for ( int i = 0; i < size; i ++ ) {
        cout << array[i] << " ";
    }
    cout << endl;
    
    return 0;
}