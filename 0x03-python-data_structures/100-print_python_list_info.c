#include <Python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{
	long int s = PyList_Size(p);
	int x;
	PyListObject *o = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", s);
	printf("[*] Allocated = %li\n", o->allocated);
	for (x = 0; x < s; x++)
		printf("Element %i: %s\n", x, Py_TYPE(o->ob_item[x])->tp_name);
}
