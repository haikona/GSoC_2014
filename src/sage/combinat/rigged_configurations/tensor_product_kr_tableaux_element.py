r"""
Tensor Product of Kirillov-Reshetikhin Tableaux Elements

A tensor product of
:class:`~sage.combinat.rigged_configurations.kr_tableaux.KirillovReshetikhinTableauxElement`.

AUTHORS:

- Travis Scrimshaw (2010-09-26): Initial version
"""

#*****************************************************************************
#       Copyright (C) 2010, 2011, 2012 Travis Scrimshaw <tscrim@ucdavis.edu>
#
#  Distributed under the terms of the GNU General Public License (GPL)
#
#    This code is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#    General Public License for more details.
#
#  The full text of the GPL is available at:
#
#                  http://www.gnu.org/licenses/
#*****************************************************************************

from sage.combinat.root_system.cartan_type import CartanType
from sage.combinat.crystals.tensor_product import TensorProductOfRegularCrystalsElement

class TensorProductOfKirillovReshetikhinTableauxElement(TensorProductOfRegularCrystalsElement):
    """
    An element in a tensor product of Kirillov-Reshetikhin tableaux.

    For more on tensor product of Kirillov-Reshetikhin tableaux, see
    :class:`~sage.combinat.rigged_configurations.tensor_product_kr_tableaux.TensorProductOfKirillovReshetikhinTableaux`.

    The most common way to construct an element is to specify the option
    ``pathlist`` which is a list of lists which will be used to generate
    the individual factors of
    :class:`~sage.combinat.rigged_configurations.kr_tableaux.KirillovReshetikhinTableauxElement`.

    EXAMPLES:

    Type `A_n^{(1)}` examples::

        sage: KRT = crystals.TensorProductOfKirillovReshetikhinTableaux(['A', 3, 1], [[1,1], [2,1], [1,1], [2,1], [2,1], [2,1]])
        sage: T = KRT(pathlist=[[2], [4,1], [3], [4,2], [3,1], [2,1]])
        sage: T
        [[2]] (X) [[1], [4]] (X) [[3]] (X) [[2], [4]] (X) [[1], [3]] (X) [[1], [2]]
        sage: T.to_rigged_configuration()
        <BLANKLINE>
        0[ ][ ]0
        1[ ]1
        <BLANKLINE>
        1[ ][ ]0
        1[ ]0
        1[ ]0
        <BLANKLINE>
        0[ ][ ]0
        <BLANKLINE>
        sage: T = KRT(pathlist=[[1], [2,1], [1], [4,1], [3,1], [2,1]])
        sage: T
        [[1]] (X) [[1], [2]] (X) [[1]] (X) [[1], [4]] (X) [[1], [3]] (X) [[1], [2]]
        sage: T.to_rigged_configuration()
        <BLANKLINE>
        (/)
        <BLANKLINE>
        1[ ]0
        1[ ]0
        <BLANKLINE>
        0[ ]0
        <BLANKLINE>

    Type `D_n^{(1)}` examples::

        sage: KRT = crystals.TensorProductOfKirillovReshetikhinTableaux(['D', 4, 1], [[1,1], [1,1], [1,1], [1,1]])
        sage: T = KRT(pathlist=[[-1], [-1], [1], [1]])
        sage: T
        [[-1]] (X) [[-1]] (X) [[1]] (X) [[1]]
        sage: T.to_rigged_configuration()
        <BLANKLINE>
        0[ ][ ]0
        0[ ][ ]0
        <BLANKLINE>
        0[ ][ ]0
        0[ ][ ]0
        <BLANKLINE>
        0[ ][ ]0
        <BLANKLINE>
        0[ ][ ]0
        <BLANKLINE>
        sage: KRT = crystals.TensorProductOfKirillovReshetikhinTableaux(['D', 4, 1], [[2,1], [1,1], [1,1], [1,1]])
        sage: T = KRT(pathlist=[[3,2], [1], [-1], [1]])
        sage: T
        [[2], [3]] (X) [[1]] (X) [[-1]] (X) [[1]]
        sage: T.to_rigged_configuration()
        <BLANKLINE>
        0[ ]0
        0[ ]0
        0[ ]0
        <BLANKLINE>
        0[ ]0
        0[ ]0
        0[ ]0
        <BLANKLINE>
        1[ ]0
        <BLANKLINE>
        1[ ]0
        <BLANKLINE>
        sage: T.to_rigged_configuration().to_tensor_product_of_kirillov_reshetikhin_tableaux()
        [[2], [3]] (X) [[1]] (X) [[-1]] (X) [[1]]
    """
    def __init__(self, parent, list=[[]], **options):
        r"""
        Construct a TensorProductOfKirillovReshetikhinTableauxElement.

        INPUT:

        - ``parent`` -- Parent for this element

        - ``list``   -- The list of KR tableaux elements

        EXAMPLES::

            sage: KRT = crystals.TensorProductOfKirillovReshetikhinTableaux(['A', 3, 1], [[1, 1], [2, 1], [1, 1], [2, 1], [2, 1], [2, 1]])
            sage: T = KRT(pathlist=[[2], [4, 1], [3], [4, 2], [3, 1], [2, 1]])
            sage: T
            [[2]] (X) [[1], [4]] (X) [[3]] (X) [[2], [4]] (X) [[1], [3]] (X) [[1], [2]]
            sage: KRT = crystals.TensorProductOfKirillovReshetikhinTableaux(['A', 3, 1], [[3,3], [2,1]])
            sage: T = KRT(pathlist=[[3, 2, 1, 4, 2, 1, 4, 3, 1], [2, 1]])
            sage: T
            [[1, 1, 1], [2, 2, 3], [3, 4, 4]] (X) [[1], [2]]
            sage: KRT = crystals.TensorProductOfKirillovReshetikhinTableaux(['D', 4, 1], [[2, 1], [1, 1], [1, 1], [1, 1]])
            sage: T = KRT(pathlist=[[3,2], [1], [-1], [1]])
            sage: T
            [[2], [3]] (X) [[1]] (X) [[-1]] (X) [[1]]
            sage: TestSuite(T).run()
        """
        if "pathlist" in options:
            pathlist = options["pathlist"]
            TensorProductOfRegularCrystalsElement.__init__(self, parent,
              [parent.crystals[i](*tab) for i, tab in enumerate(pathlist)])
        else:
            TensorProductOfRegularCrystalsElement.__init__(self, parent, list)

    def _repr_(self):
        """
        Return a string representation of ``self``.

        EXAMPLES::

            sage: KRT = crystals.TensorProductOfKirillovReshetikhinTableaux(['D', 4, 1], [[2, 1], [1, 1], [1, 1], [1, 1]])
            sage: T = KRT(pathlist=[[3,2], [1], [-1], [1]])
            sage: T # indirect doctest
            [[2], [3]] (X) [[1]] (X) [[-1]] (X) [[1]]
        """
        ret_str = repr(self[0])
        for i in range(1, len(self)):
            ret_str += " (X) " + repr(self[i])
        return(ret_str)

    def _repr_diagram(self):
        """
        Return a string representation of ``self`` as a diagram.

        EXAMPLES::

            sage: TPKRT = crystals.TensorProductOfKirillovReshetikhinTableaux(['A',4,1], [[2,2],[3,1],[3,3]])
            sage: print TPKRT.module_generators[0]._repr_diagram()
              1  1 (X)   1 (X)   1  1  1
              2  2       2       2  2  2
                         3       3  3  3
            sage: Partitions.global_options(convention='French')
            sage: print TPKRT.module_generators[0]._repr_diagram()
              2  2 (X)   3 (X)   3  3  3
              1  1       2       2  2  2
                         1       1  1  1
            sage: Partitions.global_options.reset()
        """
        comp = [crys._repr_diagram().splitlines() for crys in self]
        num_comp = len(comp) # number of components
        col_len = [len(t) > 0 and len(t[0]) or 1 for t in comp]  # columns per component
        num_rows = max(len(t) for t in comp)                     # number of rows

        # We take advantage of the fact the components are rectangular
        diag = ''
        diag += ' (X) '.join(c[0] for c in comp)
        for row in xrange(1, num_rows):
            diag += '\n'
            for c in range(num_comp):
                if c > 0:
                    diag += '     ' # For the tensor symbol
                if row < len(comp[c]):
                    diag += comp[c][row]
                else:
                    diag += ' '*col_len[c]
        return diag

    def pp(self):
        """
        Pretty print ``self``.

        EXAMPLES::

            sage: TPKRT = crystals.TensorProductOfKirillovReshetikhinTableaux(['A',4,1], [[2,2],[3,1],[3,3]])
            sage: TPKRT.module_generators[0].pp()
              1  1 (X)   1 (X)   1  1  1
              2  2       2       2  2  2
                         3       3  3  3
        """
        print(self._repr_diagram())

    def classical_weight(self):
        """
        Return the classical weight of ``self``.

        EXAMPLES::

            sage: KRT = crystals.TensorProductOfKirillovReshetikhinTableaux(['D',4,1], [[2,2]])
            sage: elt = KRT(pathlist=[[3,2,-1,1]]); elt            
            [[2, 1], [3, -1]]
            sage: elt.classical_weight()
            (0, 1, 1, 0)
            sage: KRT = crystals.TensorProductOfKirillovReshetikhinTableaux(['A',3,1], [[2,2],[1,3]])
            sage: elt = KRT(pathlist=[[2,1,3,2],[1,4,4]]); elt
            [[1, 2], [2, 3]] (X) [[1, 4, 4]]
            sage: elt.classical_weight()
            (2, 2, 1, 2)
        """
        return sum([x.classical_weight() for x in self])

    def to_rigged_configuration(self, display_steps=False):
        r"""
        Perform the bijection from ``self`` to a
        :class:`rigged configuration<sage.combinat.rigged_configurations.rigged_configuration_element.RiggedConfigurationElement>`
        which is described in [RigConBijection]_, [BijectionLRT]_, and
        [BijectionDn]_.

        .. NOTE::

            This is only proven to be a bijection in types `A_n^{(1)}`
            and `D_n^{(1)}`, as well as `\bigotimes_i B^{r_i,1}` and
            `\bigotimes_i B^{1,s_i}` for general affine types.

        INPUT:

        - ``display_steps`` -- (default: ``False``) Boolean which indicates
          if we want to output each step in the algorithm.

        OUTPUT:

        The rigged configuration corresponding to ``self``.

        EXAMPLES:

        Type `A_n^{(1)}` example::

            sage: KRT = crystals.TensorProductOfKirillovReshetikhinTableaux(['A', 3, 1], [[2,1], [2,1], [2,1]])
            sage: T = KRT(pathlist=[[4, 2], [3, 1], [2, 1]])
            sage: T
            [[2], [4]] (X) [[1], [3]] (X) [[1], [2]]
            sage: T.to_rigged_configuration()
            <BLANKLINE>
            0[ ]0
            <BLANKLINE>
            1[ ]1
            1[ ]0
            <BLANKLINE>
            0[ ]0
            <BLANKLINE>

        Type `D_n^{(1)}` example::

            sage: KRT = crystals.TensorProductOfKirillovReshetikhinTableaux(['D', 4, 1], [[2,2]])
            sage: T = KRT(pathlist=[[2,1,4,3]])
            sage: T
            [[1, 3], [2, 4]]
            sage: T.to_rigged_configuration()
            <BLANKLINE>
            0[ ]0
            <BLANKLINE>
            -1[ ]-1
            -1[ ]-1
            <BLANKLINE>
            0[ ]0
            <BLANKLINE>
            (/)

        Type `D_n^{(1)}` spinor example::

            sage: CP = crystals.TensorProductOfKirillovReshetikhinTableaux(['D', 5, 1], [[5,1],[2,1],[1,1],[1,1],[1,1]])
            sage: elt = CP(pathlist=[[-2,-5,4,3,1],[-1,2],[1],[1],[1]])
            sage: elt
            [[1], [3], [4], [-5], [-2]] (X) [[2], [-1]] (X) [[1]] (X) [[1]] (X) [[1]]
            sage: elt.to_rigged_configuration()
            <BLANKLINE>
            2[ ][ ]1
            <BLANKLINE>
            0[ ][ ]0
            0[ ]0
            <BLANKLINE>
            0[ ][ ]0
            0[ ]0
            <BLANKLINE>
            0[ ]0
            <BLANKLINE>
            0[ ][ ]0
            <BLANKLINE>

        This is invertible by calling
        :meth:`~sage.combinat.rigged_configurations.rigged_configuration_element.RiggedConfigurationElement.to_tensor_product_of_kirillov_reshetikhin_tableaux()`::

            sage: KRT = crystals.TensorProductOfKirillovReshetikhinTableaux(['D', 4, 1], [[2,2]])
            sage: T = KRT(pathlist=[[2,1,4,3]])
            sage: rc = T.to_rigged_configuration()
            sage: ret = rc.to_tensor_product_of_kirillov_reshetikhin_tableaux(); ret
            [[1, 3], [2, 4]]
            sage: ret == T
            True
        """
        from sage.combinat.rigged_configurations.bijection import KRTToRCBijection
        return KRTToRCBijection(self).run(display_steps)

    def to_tensor_product_of_kirillov_reshetikhin_crystals(self):
        """
        Return a tensor product of Kirillov-Reshetikhin crystals corresponding
        to ``self``.

        This works by performing the filling map on each individual factor.
        For more on the filling map, see
        :class:`~sage.combinat.rigged_configurations.kr_tableaux.KirillovReshetikhinTableaux`.

        EXAMPLES::

            sage: KRT = crystals.TensorProductOfKirillovReshetikhinTableaux(['D',4,1], [[1,1],[2,2]])
            sage: elt = KRT(pathlist=[[-1],[-1,2,-1,1]]); elt
            [[-1]] (X) [[2, 1], [-1, -1]]
            sage: tp_krc = elt.to_tensor_product_of_kirillov_reshetikhin_crystals(); tp_krc
            [[[-1]], [[2], [-1]]]

        We can recover the original tensor product of KR tableaux::

            sage: ret = KRT(tp_krc); ret
            [[-1]] (X) [[2, 1], [-1, -1]]
            sage: ret == elt
            True
        """
        TP = self.parent().tensor_product_of_kirillov_reshetikhin_crystals()
        return TP(*[x.to_kirillov_reshetikhin_crystal() for x in self])
