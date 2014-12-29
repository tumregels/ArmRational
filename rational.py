from math import copysign

def gcd(a,b):
    """Computes greatest common divisor of two values"""
    if b == 0:
        return a
    return gcd(b,a%b)

class Rational:
   """Representation of rational number
   >>> Rational(1,2)
   1/2
   >>> Rational(2,4)
   1/2
   >>> Rational(1,2) + Rational(3,4)
   5/4
   >>> Rational(-1,2)
   -1/2
   >>> Rational(5)
   5
   >>> float(Rational(3,4))
   0.75
   """

   def __init__( self, top = 1, bottom = 1 ):
      """Initializes Rational instance"""

      # do not allow 0 d
      if bottom == 0:
         raise ZeroDivisionError("Cannot have 0 d")

      # assign attribute values
      self.n = abs( top )
      self.d = abs( bottom )
      self.sign = copysign(1,top*bottom)

      self.simplify()  # Rational represented in reduced form

   # class interface method
   def simplify( self ):
      """Simplifies a Rational number"""

      common = gcd( self.n, self.d )
      self.n = int(self.n/common)
      self.d = int(self.d/common)

   # overloaded unary operator
   def __neg__( self ):
      """Overloaded negation operator"""

      return Rational( -self.sign * self.n,
                       self.d )

   # overloaded binary arithmetic operators
   def __add__( self, other ):
      """Overloaded addition operator"""
      if not isinstance(other, Rational):
          other = Rational(other)

      return Rational(
         self.sign * self.n * other.d +
         other.sign * other.n * self.d,
         self.d * other.d )

   def __sub__( self, other ):
      """Overloaded subtraction operator"""
      if not isinstance(other, Rational):
          other = Rational(other)

      return self + ( -other )

   def __mul__( self, other ):
      """Overloaded multiplication operator"""
      if not isinstance(other, Rational):
          other = Rational(other)

      return Rational( self.n * other.n,
                       self.sign * self.d *
                       other.sign * other.d )

   def __rmul__(self, other):

       return self.__mul__(other)

   def __div__( self, other ):
      """Overloaded / division operator."""
      if not isinstance(other, Rational):
          other = Rational(other)

      return Rational( self.n * other.d,
                       self.sign * self.d *
                       other.sign * other.n )

   def __truediv__( self, other ):
      """Overloaded / division operator"""
      #if not isinstance(other, Rational):
      #    other = Rational(other)

      return self.__div__( other )

   def __rtruediv__(self, other):
       if not isinstance(other, Rational):
           other = Rational(other)

       return other.__div__(self)

   # overloaded binary comparison operators
   def __eq__( self, other ):
      """Overloaded equality operator"""

      return ( self - other ).n == 0

   def __lt__( self, other ):
      """Overloaded less-than operator"""

      return ( self - other ).sign < 0

   def __gt__( self, other ):
      """Overloaded greater-than operator"""

      return ( self - other ).sign > 0

   def __le__( self, other ):
      """Overloaded less-than or equal-to operator"""

      return ( self < other ) or ( self == other )

   def __ge__( self, other ):
      """Overloaded greater-than or equal-to operator"""

      return ( self > other ) or ( self == other )

   def __ne__( self, other ):
      """Overloaded inequality operator"""

      return not ( self == other )

   # overloaded built-in functions
   def __abs__( self ):
      """Overloaded built-in function abs"""

      return Rational( self.n, self.d )

   def __str__( self ):
      """String representation"""

      # determine sign display
      if self.sign == -1:
         signString = "-"
      else:
         signString = ""

      if self.n == 0:
         return "0"
      elif self.d == 1:
         return "{}{:d}".format( signString, self.n)
      else:
         return "{}{:d}/{:d}".format(signString, self.n, self.d)

   __repr__ = __str__
   # overloaded coercion capability
   def __int__( self ):
      """Overloaded integer representation"""

      return int(self.sign * divmod( self.n,
         self.d )[ 0 ])

   def __float__( self ):
      """Overloaded floating-point representation"""

      return self.sign * float( self.n ) / self.d

      

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)