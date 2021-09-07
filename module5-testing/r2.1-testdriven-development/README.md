# Test-driven Development

**Test-driven development** (TDD) is a process where developers write the tests first,
**before** writing the code. As we saw in the last section, the tests alone can
be sufficient for specifying the behavior of the function.

Even to modify existing code, a test would be written first under this
philosophy. For example, if you had an `if` statement in your code already, but
you wanted to add an `else` branch, under TDD, you would first write a test for
that `else` branch, and then write the actual code. As mentioned before, at the
highest levels of testing, a mistake in any line of code should be caught, and
TDD facilitates this.

## Why TDD?

First, TDD requires the developer to first think
about the behavior of the tested code and how it will be used, rather than
rushing head-first into writing the code. Perhaps you may have experienced
writing code and realizing later that the code you wrote was not quite what you
needed. When you think carefully first about the behavior of the code as in TDD,
this situation is often avoided.

Second, as developers must write tests with every code, TDD requires developers
to write tests and puts developers in the habit of writing tests, which is
generally healthy for the robustness of a codebase. If TDD was not present,
depending on the company, developers may be less strict about writing tests.

## Is TDD used in the real world?
Many companies do adopt TDD, although in practice, this is a minority of
companies. TDD is far from a perfect philosophy: it does not guarantee good test
coverage and it may even encourage developers to write sloppier tests so that
they can simply start coding faster.

However, as with all things
in life, understanding the perspective of TDD is still extremely useful.
But as all things in life, learning different perspectives is useful.
TDD is on the very rigorous end of the role of testing in
development. In reality, you will probably end up somewhere in between --
perhaps sometimes you will think about the tests first, or you will think in
your head about what will be tested, even though you may not be required to
actually write the tests as you would in TDD.

The reason that understanding or trying test-driven development is helpful is
because even if you do not work at a company that adopts test-driven
development, it will encourage you to think about success and failure cases
while you write your code. **This is a crucial part of the programmer's
mindset.** As you become a more experienced programmer, you will try to predict
issues; test-driven development aids greatly with this mindset, since it
encourages you to write the test and think about these scenarios before writing
the code.
