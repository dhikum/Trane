from SubOperation import SubOperation
from TableMeta import TableMeta as tm

"""
Module functions that act as possible RowOperations.
There are two steps involved in adding a new method.
1. Create a new function.
2. Create a new mapping in the dictionary with the function inside the SubOperation class.
"""
def identity(val):
	return val
def equals(val, param):
	return val == param
def not_equals(val, param):
	return val != param
def less_than(val, param):
	return val < param
def greater_than(val, param):
	return val > param
def exponentiate(val, param):
	return val ** param

param_placeholder = 1 #TODO UPDATE WITH A FUNCTION TO PROGRAMATICALLY
	#SPECIFY WHAT THE PARAMS FOR EACH FUNCTION WILL BE

possible_operations = {
"identity" : SubOperation("identity", identity),
"equals" : SubOperation("equals", equals, param_placeholder),
"not equals" : SubOperation("not equals", not_equals, param_placeholder),
"less than" : SubOperation("less than", less_than, param_placeholder),
"greater than" : SubOperation("greater than", greater_than, param_placeholder),
"exponentiate" : SubOperation("exponentiate", exponentiate, param_placeholder)
}

operation_io_types = {
	"identity" : [(tm.TYPE_VALUE, tm.TYPE_VALUE), (tm.TYPE_BOOL, tm.TYPE_BOOL)],
	"equals": [(tm.TYPE_VALUE, tm.TYPE_BOOL)],
	"not equals": [(tm.TYPE_VALUE, tm.TYPE_BOOL)],
	"less than": [(tm.TYPE_VALUE, tm.TYPE_BOOL)],
	"greater than": [(tm.TYPE_VALUE, tm.TYPE_BOOL)],
	"exponentiate": [(tm.TYPE_VALUE, tm.TYPE_VALUE)]
}
