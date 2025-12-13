from sage.categories.category_with_axiom import CategoryWithAxiom as CategoryWithAxiom

class FacadeSets(CategoryWithAxiom):
    def example(self, choice: str = 'subset'):
        """
        Return an example of facade set, as per
        :meth:`Category.example()
        <sage.categories.category.Category.example>`.

        INPUT:

        - ``choice`` -- 'union' or 'subset' (default: ``'subset'``)

        EXAMPLES::

            sage: Sets().Facade().example()
            An example of facade set: the monoid of positive integers
            sage: Sets().Facade().example(choice='union')
            An example of a facade set: the integers completed by +-infinity
            sage: Sets().Facade().example(choice='subset')
            An example of facade set: the monoid of positive integers
        """
    class ParentMethods:
        def facade_for(self):
            """
            Return the parents this set is a facade for.

            This default implementation assumes that ``self`` has
            an attribute ``_facade_for``, typically initialized by
            :meth:`Parent.__init__`. If the attribute is not present, the method
            raises a :exc:`NotImplementedError`.

            EXAMPLES::

                sage: S = Sets().Facade().example(); S
                An example of facade set: the monoid of positive integers
                sage: S.facade_for()
                (Integer Ring,)

            Check that :issue:`13801` is corrected::

                sage: class A(Parent):
                ....:     def __init__(self):
                ....:         Parent.__init__(self, category=Sets(), facade=True)
                sage: a = A()
                sage: a.facade_for()
                Traceback (most recent call last):
                ...
                NotImplementedError: this parent did not specify which parents it is a facade for
            """
        def is_parent_of(self, element):
            """
            Return whether ``self`` is the parent of ``element``.

            INPUT:

            - ``element`` -- any object

            Since ``self`` is a facade domain, this actually tests
            whether the parent of ``element`` is any of the parent
            ``self`` is a facade for.

            EXAMPLES::

                sage: S = Sets().Facade().example(); S
                An example of facade set: the monoid of positive integers
                sage: S.is_parent_of(1)
                True
                sage: S.is_parent_of(1/2)
                False

            This method differs from :meth:`__contains__` in two
            ways.  First, this does not take into account the fact
            that ``self`` may be a strict subset of the parent(s)
            it is a facade for::

                sage: -1 in S, S.is_parent_of(-1)
                (False, True)

            Furthermore, there is no coercion attempted::

                sage: int(1) in S, S.is_parent_of(int(1))
                (True, False)

            .. warning::

               this implementation does not handle facade parents of facade
               parents. Is this a feature we want generically?
            """
        def __contains__(self, element) -> bool:
            '''
            Membership testing.

            Returns whether ``element`` is in one of the parents
            ``self`` is a facade for.

            .. warning::

                this default implementation is currently
                overridden by :meth:`Parent.__contains__`.

            EXAMPLES::

                sage: S = Sets().Facade().example("union"); S
                An example of a facade set: the integers completed by +-infinity
                sage: 1 in S, -5 in S, oo in S, -oo in S, int(1) in S, 2/1 in S
                (True, True, True, True, True, True)
                sage: 1/2 in S, "bla" in S
                (False, False)
            '''
