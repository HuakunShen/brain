#include <stdio.h>
#include <string.h>

int is_validated(char *serial) {
   if (strlen(serial) == 1) {
      return 1;
   } else {
      return 0;
   }
}

int main() {
   char serial[10] = "ab";
   if (is_validated(serial) == 1) {
      printf("activated\n");
   } else {
      printf("not activated\n");
   }
   return 0;
}
