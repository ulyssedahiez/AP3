#include <stdio.h>
#include <string.h>
#include "c_unit.h"

Response create_response(char* success_message, char* error_message){
  return (Response){0, success_message, error_message};
}

Response must_not_contain_numbers(char* str)
{
  char success_message[1024];
  char error_message[1024];
  sprintf(error_message, "'%s' has numbers", str);
  sprintf(success_message, "'%s' doesn't have any numbers", str);
  Response res = create_response(success_message, error_message);

  int i = 0;
  while (str[i] != 0)
  {
    if (((int) str[i]) >= ((int)'0') && ((int)str[i]) <= ((int) '9')) {
      res.status = 0;
      return res;
    }
    i++;
  }
  return res;
}

Response must_contain_more_than_hundred_e(char* str)
{
  char success_message[1024];
  char error_message[1024];
  sprintf(success_message, "'%s' have more than one hundred 'e'", str);
  sprintf(error_message, "'%s' doesn't have more than one hundred 'e'", str);
  Response res = create_response(success_message, error_message);

  int i = 0;
  int cpt = 0;
  while (str[i] != 0)
  {
    if (str[i] == 'e') {
      cpt++;
    }
    if (cpt >= 100){
      res.status = 1;
      return res;
    }
    i++;
  }

  return res;
}

Response must_contain_a_following_n(char* str)
{
  char success_message[1024];
  char error_message[1024];
  sprintf(success_message, "'%s' have an 'a' followed by 'n'", str);
  sprintf(error_message, "'%s' doesn't have any 'a' followed by 'n'", str);
  Response res = create_response(success_message, error_message);

  int i = 0, flag = 0;
  while(str[i] != 0)
  {
    if(str[i] == 'a') flag = 1;
    else if (str[i] == 'n' && flag == 1){
      res.status = 1;
      return res;
    } else flag = 0;
    i++;
  }
  return res;
}

Response must_contain_capital_letter(char* str)
{
  char success_message[1024];
  char error_message[1024];
  sprintf(success_message, "'%s' contains capital letters", str);
  sprintf(error_message, "'%s' doesn't contain any capital letter", str);
  Response res = create_response(success_message, error_message);

  int i = 0;
  while (str[i] != 0)
  {
    if (((int) str[i]) >= ((int)'A') && ((int)str[i]) <= ((int) 'Z')) {
      res.status = 1;
      return res;
    }
    i++;
  }
  return res;
}

void display_args(int argc, char* argv[])
{
  printf("[\t");
  int i;
  for (i = 0; i < argc; i++)
  {
    printf("%s\t", argv[i]);
  }
  printf("]\n");
}

int main(int argc, char* argv[])
{
  display_args(argc, argv);
  char* str = "Hello worlda 1!";

  Response (*tests[4])(char* str) = {
    &must_not_contain_numbers,
    &must_contain_more_than_hundred_e,
    &must_contain_a_following_n,
    &must_contain_capital_letter};
  int res = testAll(str, 4, tests);

  return res;
}