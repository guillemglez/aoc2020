#include <stdio.h>
#include <string.h>

#define LINE_LENGTH 32

int main(void) {
  FILE* file;
  int i, c, x, count;
  char line[LINE_LENGTH];

  file = fopen("input", "r");
  count = 0;
  x = 0;

  while (!feof(file)) {
    i = 0;
    memset(line, '.', LINE_LENGTH);

    while (i < LINE_LENGTH) {
      c = getc(file);
      if (c == '\n') {
        break;
      }
      line[i] = c;
      i++;
    }

    if (line[x % i] == '#') {
      count++;
    }
    x += 3;
  }

  printf("There are %d trees on the way\n", count);

  return fclose(file);
}
