def lower_bound(order: int) -> int:
    """
    Return the best known lower bound on the number of MOLS of
    the given ``order``.

    The source of this information is Table 3.87 in the Handbook of
    Combinatorial Designs, 2nd edition, by Colbourn and Dinitz. A few
    updates have subsequently been provided on Jeff Dinitz's website.

    Parameters
    ----------

    order : int
      The order (also known as the side) for which you'd like a lower
      bound on the number of MOLS instances. In the language of the
      Handbook, this is ``n``, and it should be between 0 and 9999.

    Returns
    -------

    int
      A lower bound on the number of MOLS.

    Raises
    ------

    IndexError
      If you ask for an order that isn't contained in the table.

    Examples
    --------

    There are no MOLS of order zero::

        sage: from sage.combinat.designs import MOLS_handbook_data
        sage: MOLS_handbook_data.lower_bound(0)
        0
    """
