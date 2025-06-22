######################
Lincoln Log Notation
######################

Lincoln logs follow a general cartesian coordinate system.  The intersection of blocks are the vertices, the length of blocks is teh edges.  Therefore, the blocks could be identified 2 ways - the # of verticies, or the # of edges.


************************
Individual Characters
************************
There are just a small number of characters that can be used to represent the blocks, and the intersections between them.  The notation is designed to be simple, and easy to read, while still being able to represent the blocks in a way that is intuitive.

Vertical Notches:

``V ``

Horizontal Notches:
``<`` or ``>``

Vertical Lines:
``|``

Horizontal Lines:
``-`` or ``—`` (hyphen or em dash)


************************
Block Notation
************************

Therefore a 1 notch block would be represented as:

.. code-block:: text
    V
    # or
    <
    # or 
    >

a 2 notch block would be represented as:

.. code-block:: text
    V
    |
    V
    # or
    <-<
    <—<
    # or 
    >->
    >—>

a 3 notch block would be represented as:

.. code-block:: text
    V
    |
    V
    |
    V
    # or
    <-<-<
    <—<—<
    # or 
    >->->
    >—>—>

and a 4 notch block would be represented as:

.. code-block:: text
    V
    |
    V
    |
    V
    |
    V
    # or
    <-<-<-<
    <—<—<—<
    # or 
    >->->->
    >—>—>—>

.. note::
    Going forward, this document will use hyphens, not em dashes, to represent horizontal lines, but keep in mind that em dashes are also acceptable.  The same goes for the horizontal notches - you can use either < or >, and they are interchangeable in the notation.

************************
Layer Notation
************************

Now that we have the individual block notation, we can combine them to create layers. 
The terminology may be a bit confusing here, because a layer often typically consists of 2 logs on top of each other, which kind of seems like "2 layers", but we do it this way to keep the notation brief, and because laying down a single layer without the "orthogonal" structure makes it somewhat hard to construct properly.

Therefore, a single layer defined by 4 2 notch blocks would be represented as:

.. code-block:: text

    <-<
    | |
    <—<
    # or
    >->
    | |
    >—>
    # or
    V-V
    | |
    V-V

The first two are identical; both showing the top logs being horizontal, and the bottom logs being vertical.  The third shows the same layer, but with the top logs being vertical, and the bottom logs being horizontal.
The third could also be thought of as a 90 degree rotation of the first two.

A single layer defined by 4 3 notch blocks would be represented as:

.. code-block:: text
    V-V-V
    |   |
    <   <
    |   |
    V-V-V
    # or
    <-V-<
    |   |
    <   <
    |   |
    <-V-<

.. note::
    At this point I will also stop showing each < and > variation - as they are interchangeable.


*****************************
More Complex Examples
*****************************

Now that we have seen the language, the individual logs, and the layers, we can start to build more complex structures.


For example, a 2x2 layer with a 1 notch block in the center would be represented as:

.. code-block:: text

    <-<
    |V|
    <—<

I don't know why you would want to build a room like this, but it is a valid structure.


Here is a layer shouwing multiple "rooms" in a sense - we have a 4x3 layer with a 2 notch block in the top left corner:


.. code-block:: text

    <-<-V-<
    | |   |
    <—<   <
    |     |
    <-V-V-<


If its not obvious, on the above, the horizontal 4 length logs are on the bottom, and the vertical 3 length logs are on the top. 
There are 2 2 notch logs in the top left corner, the horizontal one is on the bottom, and the vertical one is on the top.

