from tomcrypt._core cimport *

cdef class PRNG(object):
	
	cdef prng_desc *desc
	cdef readonly int idx
	cdef prng_state state

cdef get_prng_idx(input)