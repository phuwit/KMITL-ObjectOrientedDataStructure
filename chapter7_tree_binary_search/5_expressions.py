'''
Chapter : 7 - item : 5 - Expression Tree

ให้น้องๆรับ input เป็น postfix จากนั้นให้แปลงเป็น Expression Tree , Infix และ Prefix  โดย Operator จะมีแค่ + - * /


Enter Postfix : ab+cde+**
Tree :
                e
           +
                d
      *
           c
 *
           b
      +
           a
--------------------------------------------------
Infix : ((a+b)*(c*(d+e)))
Prefix : *+ab*c+de


Enter Postfix : abc*+de*f+g*+
Tree :
           g
      *
                f
           +
                     e
                *
                     d
 +
                c
           *
                b
      +
           a
--------------------------------------------------
Infix : ((a+(b*c))+(((d*e)+f)*g))
Prefix : ++a*bc*+*defg


Enter Postfix : ab+c*de-fg+*-
Tree :
                g
           +
                f
      *
                e
           -
                d
 -
           c
      *
                b
           +
                a
--------------------------------------------------
Infix : (((a+b)*c)-((d-e)*(f+g)))
Prefix : -*+abc*-de+fg

'''