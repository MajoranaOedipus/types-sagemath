# types-sagemath

Typing stubs for SageMath (WIP).

I will start from MyPy-generated stubs, and try my best to fill all the holes.
The first goal is that all the symbols available under `sage.all` shall be 
well typed and docstringed.

Since SageMath contains a lot of Cython modules, and does a lot runtime magic,
the generated stubs shall be manually edited to be correct.

I will be mainly please Pylance standard mode just for now.