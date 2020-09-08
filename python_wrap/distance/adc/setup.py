from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
from numpy import get_include
import os

extensions = [
    Extension("py_asymmetric_distance_computer", ["py_asymmetric_distance_computer.pyx"],
              include_dirs=[r"c:\SourcePython\inverted_multi_index\src",
                            "c:\SourcePython\inverted_multi_index\OpenBLAS-v0.2.19-Win64-int32\include",
                            get_include()],
              libraries=[r'libopenblas.dll'],
              library_dirs=[
                  r'c:\SourcePython\inverted_multi_index\OpenBLAS-v0.2.19-Win64-int32\lib']
              )
]

setup(
    name="py_asymmetric_distance_computer",
    ext_modules=cythonize(extensions),
)
