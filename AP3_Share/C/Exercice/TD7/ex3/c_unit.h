
struct response{
  int status;
  char* success_message;
  char* error_message;
};
typedef struct response Response;

/**
 this method will apply a lot of tests on the string value and return the number of failed tests
 **/
int test(char* str, Response (*test_method)(char*));

int testAll(char* str, int nb_tests, Response (**test_method)(char*));