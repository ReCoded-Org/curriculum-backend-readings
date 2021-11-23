# Why is testing important?

You may think it is sufficient simply to manually test your code.

There are a few reasons testing is very important when it comes to a growing
codebase. You should not imagine the situation where you are working on a
project with one or two people, but a situation where you are working with a
larger team and with code that the company will use the code long after you leave. You
may not be at the company five years later, or you may forget what the code does
in six months.

## Correctness
Most obviously, a test is used to verify the correctness of the code. If you
have ever changed your code then had to test three or more cases manually, then
you are familiar with the fact that it is quite cumbersome to repeatedly check
manually. Not only that, it's very easy to forget to check some case when a
human is doing it by hand.

In contract, when you write a test, you simply need to run a command in order to
initiate the tests again, rather than repeating some steps to ensure that your
code is working.

If you work at a company with code review, consider the perspective of the
person reviewing your code: how do they know your code doesn't have bugs? How do
they know it works correctly? If your code is submitted along with tests, the
reviewer can be aware of exactly what you have or haven't verified about your
code.

## Ease of change
Have you ever
felt scared to change code, because you weren't sure if it would still work for
all the cases after you changed it? With a good test suite, this fear generally
doesn't exist. Even if the code is rewritten but the same tests pass, indicating
that the new code has the same behavior, one can feel a lot more secure about
rewriting the code.

Having good tests allows code to be changed in a more robust fashion. When the
same tests pass, a developer can be more sure (perhaps not completely sure,
depending on the tests) that changing the code did not break anything.
Additionally, it allows people who are not familiar with the code (say, your
teammates who work on related code, or someone who is responsible for your code
five years later) to more easily work with the code.

## Documentation
A well-written test suite serves as documentation. Again, imagine you have just
joined a company, and you don't know what a function or component does. In fact, if you want to
understand what a piece of code does, it's often more productive to go read the
tests first, rather than the code itself.

In the next section, we'll look an
example of a test, which will help illustrate how the tests themselves can be
used to document the code.

