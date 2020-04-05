all: venv/lib/python3.8/site-packages/cython.pyi stuff/module.c

venv/lib/python3.8/site-packages/cython.pyi: stubs/cython.pyi
	cp $< $@

%.c %.html %.cpython-38-x86_64-linux-gnu.so: %.py
	. venv/bin/activate;\
	cythonize -a -i $<
