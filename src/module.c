// src/module.c
#include <Python.h>

// C function that corresponds to the Python function
static PyObject* py_add(PyObject* self, PyObject* args) {
    int a, b;
    if (!PyArg_ParseTuple(args, "ii", &a, &b))
        return NULL;
    return Py_BuildValue("i", a + b);
}

// Method definition object
static PyMethodDef ModuleMethods[] = {
    {"add", py_add, METH_VARARGS, "Add two numbers"},
    {NULL, NULL, 0, NULL}
};

// Module definition
static struct PyModuleDef moduledef = {
    PyModuleDef_HEAD_INIT,
    "module",   // Module name
    NULL,       // Module documentation
    -1,         // Size of per-interpreter state of the module
    ModuleMethods
};

// Module initialization function
PyMODINIT_FUNC PyInit_module(void) {
    return PyModule_Create(&moduledef);
}
