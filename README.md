# types-sagemath

Typing stubs for SageMath (WIP).

I will start from MyPy-generated stubs, and try my best to fill all the holes.
The first goal is that all the symbols available under `sage.all` shall be 
well typed and docstringed.

Since SageMath contains a lot of Cython modules, and does a lot runtime magic,
the generated stubs shall be manually edited to be correct.

I will be mainly please Pylance standard mode just for now.

## Notes
- The type stubs shall not work for the development of Sage, but for the user of Sage, since I will write a lot symbols that are not respecting the actual code structure. 
I will try my best to mimic the *behaviours* of the classes, though.
- Currently, I expose too much symbols than actuall just for typings. I will fix that in the future.
- I will rewrite the class decorator `richcmp_method` to a base class `RichCmpMixin`, 
since class decorator is not expressible by the current type system.
- Categories goes into the MRO of the parents, so I will write a lot classes corresponding to those categories so that the type checker finds the correct methods.
- As of elements, Basicall I make all `Element` classes generic in their parent type, so that e.g. `Integer <: Element[IntegerRing_class]`.
- On laziness, should I just remove the decorator?