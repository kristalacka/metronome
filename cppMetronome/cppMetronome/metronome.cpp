#include <iostream>
#include <windows.h>
#include <mmsystem.h>
#include <conio.h>
#include "metronome.h"

Metronome::Metronome(int f): freq(f)
{
    period = 60000/freq;
    loop(period);
}

Metronome::~Metronome(){}

void Metronome::playUp()
{
    PlaySound(TEXT("MetronomeUp.wav"), NULL, SND_ASYNC);
}

void Metronome::playDown()
{
    PlaySound(TEXT("Metronome.wav"), NULL, SND_ASYNC);
}

void Metronome::loop(double period)
{
    while(!kbhit())
    {
        playUp();
        Sleep(period);
    }
}
