from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
from numpy import get_include
import os


extensions = [
    Extension("py_inverted_multi_index", ["py_inverted_multi_index.pyx"],
              include_dirs=[r"c:\SourcePython\inverted_multi_index\src",
                            "c:\SourcePython\inverted_multi_index\OpenBLAS-v0.2.19-Win64-int32\include",
                            get_include()],
              libraries=[r'libopenblas.dll'],
              library_dirs=[r'c:\SourcePython\inverted_multi_index\OpenBLAS-v0.2.19-Win64-int32\lib']
              ),
    Extension("py_multi_index_util", ["py_multi_index_util.pyx"],
              include_dirs=[r"c:\SourcePython\inverted_multi_index\src",
                            get_include()]
              )
]

setup(
    name="build_inverted_multi_index",
    ext_modules=cythonize(extensions),
    extra_compile_args=["-Zi", "/Od"],
    extra_link_args=["-debug"],
)