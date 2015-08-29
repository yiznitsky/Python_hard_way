#Python the Hard Way ex.12 Promping People
When you typed `raw_input()` you were typing `(` and `)` characters,
which are `parenthesis` characters. This is similar to when you used
them to do a format with extra variables, as in `"%s %s % (x, y).`
For `raw_input` you can also put a **prompt** to show to a person so
they know what to type. Put a **string** that you want for the prompt
inside th `()` so that it looks like this:
   `y = raw_input("name")`

This prompts the user with **"name?"** and puts the results into the
variable `y`.

This means that we can completely rewrite our previous exercise using
`raw_input` to do all the prompting.

#Pydoc
1. `pydoc raw_input`:
>raw_input(...)
    raw_input([prompt]) -> string

    Read a string from standard input.  The trailing newline is stripped.
    If the user hits EOF