Tokenizer
^^^^^^^^^

The tokenizer/lexer may be invoked directly be calling ``tokenizer.tokenize``,

.. code-block:: python

    >>> tokenizer.tokenize('System.out.println("Hello " + "world");')
    <generator object tokenize at 0x1ce5190>

This returns a generator which provides a stream of ``JavaToken`` objects. Each
token carries position (line, column) and value information,

.. code-block:: python

    >>> tokens = list(tokenizer.tokenize('System.out.println("Hello " + "world");'))
    >>> tokens[6].value
    u'"Hello "'
    >>> tokens[6].position
    (1, 19)

The tokens are not directly instances of ``JavaToken``, but are instead
instances of subclasses which identify their general type,

**NOTE:** The shift operators ``>>`` and ``>>>`` are represented by multiple
``>`` tokens. This is because multiple ``>`` may appear in a row when closing
nested generic parameter/arguments lists. This abiguity is instead resolved by
the parser.

