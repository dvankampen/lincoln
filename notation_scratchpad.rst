#########################
# Notation Scratchpad
#########################

Lincoln logs follow a general cartesian coordinate system.  The intersection of blocks are the vertices, the length of blocks is teh edges.  Therefore, the blocks could be identified 2 ways - the # of verticies, or the # of edges.

### Identifying by # of edges
0. .
1. —
2. ——
3. ———

### Identifying by # of vertices:
1. .
2. —
3. ——
4. ———



## Notation

### Approach 1
Now, due to the intersecting layer of lincoln logs, one strategy for defining a "layer" could be pieces at exactly the same elevation.  I.e. if you are building on a floor, or table, the first layer could be defined as ONLY the pieces resting _directly_ on that surface, not on any other logs.  In the case of a 1x1 room, that first layer would be defined as follows:

.. code-block:: shell

    | |
    # or
    —

    —

However, in practice, this gets a bit too "whitespace-y", and generally, I think it is more intuitive to think of a single "layer" as that plus the first layer orthogonal to it, the first layer that intersects with it at right angles.


#### Identification of intersections
the plus sign (`+`) will be used to signify intersections.


### Approach 2

So if we again use our 1x1 room, that layer would look like this:

.. code-block:: shell

    +—+
    | |
    +—+


This shows the intersections as well.

However, you may have already seen an issue with that approach.  Thereares actually _2_ ways to achieve the above, and this notation does _not_ make clear which direction should be laid down first - vertical or horizontal.  So we need to add something to the notation for that, or go back to the single plane approach.

### Approach 3

What if we mix the minus sign (`-`) and the dash (`—`), where the minus can be used to denote the direction of the top layer at a corner?  And then vertically, use the apostrophe character, `'`? This would be a way to show what the intersection should look like, when viewed from above, once it is complete?


.. code-block:: shell

    # v1, where the vertical is put down first, horizontal second (i.e. on top)
    -—-
    | |
    -—-

    #v2, where the horizontal is put down first, vertical second (i.e. on top)
    '—'
    | |
    '—'


Well... that is _ok_, but... the aspect ratio is off (because characters aren't square), and it uses some non-intutive conventions (specifically the dash).  Also, while the multi-layer horizontal notation looks good, I don't like how the vertical notation os offset.


### Approach 4

Is it possible that we can _assume_ intersections?  Like if we have a corner... doesn't that imply intersection?  What if we reference ASCII art for chess boards.  Those tend to look pretty good.

.. code-block:: text

       _______________
    8 |_|#|_|#|_|#|_|#|
    7 |#|_|#|_|#|_|#|_|
    6 |_|#|_|#|_|#|_|#|
    5 |#|_|#|_|#|_|#|_|
    4 |_|#|_|#|_|_|_|#|
    3 |#|_|#|_|#|_|#|_|
    2 |_|#|_|#|_|#|_|#|
    1 |#|_|#|_|#|_|#|_|
    a b c d e f g h


So if we try to make a 1x1 that way:

.. code-block:: text

    _
    |_|

That looks ok. but it has the same probem as approach 2, where the ordering isn't clear.  Hmm...

Another interesting observation is the 2x piece is actually 3x as long as the 1x. piece.   Meaning putting 3 of the 1 length pieces end to end equals the length of the 2 length piece.  So maybe that defines our coordinate system - each "unit" is based on the length of a 1x piece.  So how could we do that.

Horizontally:

1. `_`
2. `___`
3. `_____`
4. `_______`

Vertically:
1. ``|``
2. ``
|
|
|
``
3. ``
|
|
|
|
|
``
4. ``
|
|
|
|
|
|
|
``

And then maybe it just doesn't matter if you choose to make a horizontal from a 3 1s, or a single 2?

No... this isn't any good either.  It doesn't help us with ordering, and a 2nd layer of 3 single pieces wouldnt "bridge the gap" - so we DO need a way to differentiate.

What if we go with the 1,3,5,7, and define each coordinate by one of 5 possible occupants:

1. empty
2. horizontal notch
3. vertical notch
4. horizontal solid
5. vertical solid

That seems to have some promise.

Notation:
1. empty: an actual space
2. horizontal notch: `<`
3. vertical notch: `V`
4. horizontal solid: `-`
5. vertical solid: `|`

Ok so in this case, our 1x1 room might be described like this:

.. code-block:: text

    #v1:
    V-V
    | |
    V-V
    # v2:
    <-<
    | |
    <-<


That seems to have some promise.  It makes clear the 2 possible orientations.   Ok, lets continue with that.  So a 2x2 house would look like this:

.. code-block:: text

    # v1:
    V-V-V
    |   |
    <   <
    |   |
    V-V-V
    # v2:
    <-<-<
    |   |
    V   V
    |   |
    <-<-<

Looking good.  I assume it works for 4 length (7x) as well.  So lets see how it would show a weird combo, like 1s and 2s in a line?

.. code-block:: text

    <<<<<-<


The above is 4 1's and a single 2, placed horizontally.

Great! I think thats our notation. It might not be perfect, but it seems good enough to move us forward for now.
