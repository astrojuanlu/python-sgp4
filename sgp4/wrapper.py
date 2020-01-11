from .vallado_cpp import SatrecArray as _SatrecArray

class SatrecArray(_SatrecArray):
    """Wrapper around the high-speed SatrecArray to handle NumPy operations."""

    def sgp4(self, jd, fr):
        """Compute positions and velocities for the satellites in this array.

        Given NumPy scalars or arrays ``jd`` and ``fr`` supplying the
        whole part and the fractional part of one or more Julian dates,
        return a tuple ``(e, r, v)`` of three vectors that are each as
        long as ``jd`` and ``fr``:

        * ``e``: 1 for any dates that produced errors, 0 otherwise.
        * ``r``: (x,y,z) position vector in kilometers.
        * ``v``: (dx,dy,dz) velocity vector in kilometers per second.

        """
        jd = jd.astype('float64', copy=False)
        fr = fr.astype('float64', copy=False)

        ilength = len(self)
        jlength, = jd.shape
        eshape = ilength, jlength
        fshape = ilength, jlength, 3

        array = type(jd)
        e = array(eshape, 'uint8')
        r = array(fshape, 'float64')
        v = array(fshape, 'float64')
        self._sgp4(jd, fr, e, r, v)
        return e, r, v