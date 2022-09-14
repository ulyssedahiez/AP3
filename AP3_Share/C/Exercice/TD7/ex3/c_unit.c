#include <stdio.h>
#include "c_unit.h"

#define RED "\x1B[31m"
#define GREEN "\x1B[32m"
#define NORMAL "\x1B[0m"

void print_error(char* message)
{
  printf("%s%s%s\n",RED,message,NORMAL);
}
void print_success(char* message)
{
  printf("%s%s%s\n", GREEN, message, NORMAL);
}

int test(char* str, Response (*test_method)(char*))
{
  Response res = (*test_method)(str);
  if(res.status) print_success(res.success_message);
  else print_error(res.error_message);
  return res.status;
}

int testAll(char* str, int nb_test, Response (**test_methods)(char*)){
  int i;
  int res = 0;
  for (i = 0; i < nb_test; i++)
  {
    res += test(str, test_methods[i]);
  }
  return res;
}