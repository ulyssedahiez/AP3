FLAGS = -c -Wall -Werror -Wextra

c_unit: main.o c_unit.o
	gcc -o $@ $^

c_unit.o: c_unit.c c_unit.h
	gcc $(FLAGS) $<

main.o: main.c c_unit.h
	gcc $(FLAGS) $<

clean:
	rm -f *.o
