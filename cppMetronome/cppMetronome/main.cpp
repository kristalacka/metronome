#include "metronome.h"
#include <iostream>

int main()
{
    int bpm;
    while(std::cin>>bpm)
    {
        if (bpm < 30)
            std::cout << "enter a higher bpm\n";
        else
            Metronome metronome(bpm);;
    }
    return 0;
}
