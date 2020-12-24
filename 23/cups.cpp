#include <iostream>
#include <string>
#include <vector>

#define INPUT "614752839"

void play(const std::string labeling, const int moves)
{
    const bool million = moves > 10e5;

    std::vector<int> cups;
    if (million)
    {
        cups = std::vector<int>(10e5 + 1, 0);
    }
    else
    {
        cups = std::vector<int>(labeling.length() + 1, 0);
    }

    for (auto it = labeling.begin(); it != std::prev(labeling.end()); it = std::next(it))
    {
        const int cup = *it - '0';
        cups.at(cup) = *std::next(it) - '0';
    }

    int current = *labeling.begin() - '0';

    if (million)
    {
        int cup = labeling.length() + 1;
        cups.at(*std::prev(labeling.end()) - '0') = cup;
        while (cup < 10e5)
        {
            cups.at(cup) = cup + 1;
            cup++;
        }
        cups.at(cup) = current;
    }
    else
    {
        cups.at(*std::prev(labeling.end()) - '0') = current;
    }

    int move = 0;
    while (move++ < moves)
    {
        const int aside = cups.at(current);
        int last = current;
        int destination = current - 1;
        for (int i = 0; i < 3; i++)
        {
            if (destination == 0)
            {
                destination = cups.size() - 1;
            }
            last = cups.at(last);
            if (last == destination)
            {
                destination--;
                i = -1;
                last = current;
            }
        }

        cups.at(current) = cups.at(last);
        cups.at(last) = cups.at(destination);
        cups.at(destination) = aside;

        current = cups.at(current);
    }

    int next = cups.at(1);
    if (million)
    {
        std::cout << static_cast<long long>(next) * cups.at(next);
    }
    else
    {
        while (next != 1)
        {
            std::cout << next;
            next = cups.at(next);
        }
    }
}

int main()
{
    std::cout << "The labels on the cups are ";
    play(INPUT, 100);
    std::cout << std::endl;

    std::cout << "The stars' labels multiplied give ";
    play(INPUT, 10e6);
    std::cout << std::endl;

    return 0;
}
