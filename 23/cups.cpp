#include <string.h>

#include <iostream>
#include <string>
#include <vector>

#define INPUT "614752839"

void play(const std::string labeling, const int moves)
{
    std::vector<int> cups(labeling.length() + 1, 0);
    for (auto it = labeling.begin(); it != std::prev(labeling.end()); it = std::next(it))
    {
        const int cup = *it - '0';
        cups.at(cup) = *std::next(it) - '0';
    }

    int current = *labeling.begin() - '0';
    cups.at(*std::prev(labeling.end()) - '0') = current;

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
    while (next != 1)
    {
        std::cout << next;
        next = cups.at(next);
    }
}

int main()
{
    std::cout << "The labels on the cups are ";
    play(INPUT, 100);
    std::cout << std::endl;

    return 0;
}
