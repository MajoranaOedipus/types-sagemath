from _typeshed import Incomplete
from sage.categories.filtered_modules_with_basis import FilteredModulesWithBasis as FilteredModulesWithBasis
from sage.combinat.free_module import CombinatorialFreeModule as CombinatorialFreeModule
from sage.combinat.partition import Partitions as Partitions

class FilteredPartitionModule(CombinatorialFreeModule):
    """
    This class illustrates an implementation of a filtered module
    with basis: the free module on the set of all partitions.

    INPUT:

    - ``R`` -- base ring

    The implementation involves the following:

    - A choice of how to represent elements.  In this case, the basis
      elements are partitions. The algebra is constructed as a
      :class:`CombinatorialFreeModule
      <sage.combinat.free_module.CombinatorialFreeModule>` on the
      set of partitions, so it inherits all of the methods for such
      objects, and has operations like addition already defined.

      ::

          sage: A = ModulesWithBasis(QQ).Filtered().example()                           # needs sage.modules

    - If the algebra is called ``A``, then its basis function is
      stored as ``A.basis``.  Thus the function can be used to
      find a basis for the degree `d` piece: essentially, just call
      ``A.basis(d)``.  More precisely, call ``x`` for
      each ``x`` in ``A.basis(d)``.

      ::

          sage: [m for m in A.basis(4)]                                                 # needs sage.modules
          [P[4], P[3, 1], P[2, 2], P[2, 1, 1], P[1, 1, 1, 1]]

    - For dealing with basis elements: :meth:`degree_on_basis`, and
      :meth:`_repr_term`. The first of these defines the degree of any
      monomial, and then the :meth:`degree
      <FilteredModules.Element.degree>` method for elements --
      see the next item -- uses it to compute the degree for a linear
      combination of monomials.  The last of these determines the
      print representation for monomials, which automatically produces
      the print representation for general elements.

      ::

          sage: A.degree_on_basis(Partition([4,3]))                                     # needs sage.modules
          7
          sage: A._repr_term(Partition([4,3]))                                          # needs sage.modules
          'P[4, 3]'

    - There is a class for elements, which inherits from
      :class:`IndexedFreeModuleElement
      <sage.modules.with_basis.indexed_element.IndexedFreeModuleElement>`.
      An element is determined by a dictionary whose keys are partitions and
      whose corresponding values are the coefficients.  The class implements
      two things: an :meth:`is_homogeneous
      <FilteredModules.Element.is_homogeneous>` method and a
      :meth:`degree <FilteredModules.Element.degree>` method.

      ::

          sage: p = A.monomial(Partition([3,2,1])); p                                   # needs sage.modules
          P[3, 2, 1]
          sage: p.is_homogeneous()                                                      # needs sage.modules
          True
          sage: p.degree()                                                              # needs sage.modules
          6
    """
    def __init__(self, base_ring) -> None:
        """
        EXAMPLES::

            sage: A = ModulesWithBasis(QQ).Filtered().example(); A                      # needs sage.modules
            An example of a filtered module with basis: the free module on partitions over Rational Field
            sage: TestSuite(A).run()                                                    # needs sage.modules
        """
    basis: Incomplete
    def degree_on_basis(self, t):
        """
        The degree of the basis element indexed by the partition ``t``
        in this filtered module.

        INPUT:

        - ``t`` -- the index of an element of the basis of this module,
          i.e. a partition

        OUTPUT: integer; the degree of the corresponding basis element

        EXAMPLES::

            sage: # needs sage.modules
            sage: A = ModulesWithBasis(QQ).Filtered().example()
            sage: A.degree_on_basis(Partition((2,1)))
            3
            sage: A.degree_on_basis(Partition((4,2,1,1,1,1)))
            10
            sage: type(A.degree_on_basis(Partition((1,1))))
            <class 'sage.rings.integer.Integer'>
        """
Example = FilteredPartitionModule
