#include <string.h>

#include <algorithm>
#include <iostream>
#include <list>
#include <queue>
#include <string>

#define INPUT "614752839" // "389125467"

void play(const std::string labeling, const int moves)
{
    std::list<int> cups;
    int maxCup = -1;
    for (char const &c : labeling)
    {
        const int cup = c - '0';
        cups.push_back(cup);
        if (cup > maxCup)
        {
            maxCup = cup;
        }
    }

    std::list<int>::iterator current = cups.begin();
    int move = 0;
    while (move++ < moves)
    {
        auto asideit = std::next(current, 1);
        std::queue<std::list<int>::iterator> aside;
        std::list<int> asidev;
        for (int i = 0; i < 3; i++)
        {
            if (asideit == cups.end())
            {
                asideit = cups.begin();
            }
            aside.push(asideit);
            asidev.push_back(*asideit);
            std::advance(asideit, 1);
        }

        int destLabel = *current - 1;
        int i = 0;
        while (i++ < 100)
        {
            if (destLabel == 0)
            {
                destLabel = maxCup;
            }
            if (std::find(asidev.begin(), asidev.end(), destLabel) != asidev.end())
            {
                destLabel--;
                continue;
            }
            auto destination = std::find(cups.begin(), cups.end(), destLabel);
            if (destination != cups.end())
            {
                std::advance(destination, 1);
                for (int i = 0; i < 3; i++)
                {
                    cups.splice(destination, cups, aside.front());
                    aside.pop();
                }
                break;
            }
            destLabel--;
        }

        std::advance(current, 1);
        if (current == cups.end())
        {
            current = cups.begin();
        }
    }

    auto one = std::find(cups.begin(), cups.end(), 1);
    auto it = std::next(one, 1);

    while (it != one)
    {
        if (it == cups.end())
        {
            it = cups.begin();
        }
        std::cout << *it;
        std::advance(it, 1);
    }
}

int main()
{
    std::cout << "The labels on the cups are ";
    play(INPUT, 100);
    std::cout << std::endl;

    return 0;
}
