Python the hard way, exercise 10: What was that?
How to make strings in multiple lines: `\n` these two characters put a `new line character` into the string at that point.
the `\` **(backslash)** character encodes difficult-to-type characters into a string.
Important escape sequence- **single quote** `'` or **double-quote** `"`

"I am 6'2\" tall". **escape double-quote**
'I am 6'\2" tall'. **escape single-quote**

The second way is by using **triple-quotes** `"""`, works like a string but can put as many lines of text you as you want until you type `"""`

**ESCAPE SEQUENCES**
This all of the escape sequences Python supports. You may not use many of these, but memorize their format and what they do anyway. Try them out in some strings to see if you can make them work.

```bash
`\\` **Backslash ()**
\'` **single-quote(')**
`\"` **Double-quote (")**
`\a` **ASCII bell(BEL)**
`\b` **backspace(BS)**
`\f` **ASCII formfeed(FF)**
`\n` **ASCII linefeed(LF)**
`\N{name}` **Character name in the Unicode database (Unicode only)**
`\r ASCII` **Carriage Return(CR)**
`\t ASCII` **Horizontal Tab(TAB)**
`\uxxxx` **Character with a 16-bit hex value xxxx(unicode only)**
`\Uxxxxxxxx` **Character code with a 32-bit hex value xxxxxxxx (Unicode)
`\v` **ASCII vertical tab(VT)**
`\ooo` **Character with octal value ooo**
`\xhh` **Character with hex value hh**
```
