from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
from numpy import get_include
import os


extensions = [
    Extension("py_inverted_multi_index", ["py_inverted_multi_index.pyx"],
              include_dirs=[r"c:\SourceOpen\inverted_multi_indexMy\src",
                            r"c:\SourceOpen\inverted_multi_indexMy\OpenBLAS-v0.2.19-Win64-int32\include",
                            get_include()],
              libraries=[r'libopenblas'],
              library_dirs=[r'c:\SourceOpen\inverted_multi_indexMy\OpenBLAS-VS\RelWithDebInfo'],
              extra_compile_args=["-Zi", "/Od"],
              extra_link_args=["-debug"],
              ),
    Extension("py_multi_index_util", ["py_multi_index_util.pyx"],
              include_dirs=[r"c:\SourceOpen\inverted_multi_indexMy\src",
                            get_include()],
              extra_compile_args=["-Zi", "/Od"],
              extra_link_args=["-debug"],
              )
]

setup(
    name="build_inverted_multi_index",
    ext_modules=cythonize(extensions),
)