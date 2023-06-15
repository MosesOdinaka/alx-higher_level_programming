#include <Python.h>
#include <stdio.h>
#include <stdlib.h>

/**
 * print_python_list - prints info about a Python list
 * @p: pointer to the Python list object
 */
void print_python_list(PyObject *p)
{
	long int size = PyList_Size(p);
	int i;
	const char *type;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < size; i++)
	{
		type = (PyList_GetItem(p, i))->ob_type->tp_name;
		printf("Element %d: %s\n", i, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(PyList_GetItem(p, i));
	}
}

/**
 * print_python_bytes - prints info about a Python bytes object
 * @p: pointer to the Python bytes object
 */
void print_python_bytes(PyObject *p)
{
	long int size;
	int i;
	char *str;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = PyBytes_Size(p);
	str = PyBytes_AsString(p);
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);
	if (size > 10)
		size = 10;
	else
		size++;
	printf("  first %ld bytes:", size);
	for (i = 0; i < size; i++)
		printf(" %02x", str[i] & 0xff);
	putchar('\n');
}
