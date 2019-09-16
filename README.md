# Assignment: Python Debugging and Intermediate Variables

In this homework, you're going to write code for a challenge problem and answer some reading comprehension questions.

You will practice these programming concepts we've covered in class:

* Type conversion
* Escape characters and string formatting
* Debugging techniques
* Variable scope

## Deliverables and Submitting

The usual!

---

# Part 1: Light Reading

Read through the examples in this article about [data types and type conversion](https://www.datacamp.com/community/tutorials/python-data-type-conversion). Then, answer the following questions.

1. **_Coercion_ is another term for which of the following concepts in Python?**

   * a) Encapsulation
   * b) Inheritance
   * c) Explicit type conversion
   * d) Implicit type conversion
   * e) Floor division

1. **_Type casting_ is another term for which of the following concepts in Python?**

   * a) Encapsulation
   * b) Inheritance
   * c) Explicit type conversion
   * d) Implicit type conversion
   * e) Floor division

1. **What function in Python can we use to check a variable's type?**

   * a) `type()`
   * b) `typeof()`
   * c) `typeof`, but it is an operator not a function
   * d) `get_type()`

1. **Which of the following is *not* a primitive data structure?**

   * a) Float
   * b) Integer
   * c) List
   * d) String
   * e) Both a and c are not primitives

1. **According to the article, what is the main reason to convert a tuple into a list?**

---

# Part 2: We're in a Good Place!

Jason is a huge Jacksonville Jaguars fan. The team isn't doing great now, but he has faith: "All we need is a defense, and an offense, and then some rule changes!"

He wrote some code to predict the future for the Jaguars according to whether we have all three of those factors.

## Starter Code

Unfortunately, Jason is just starting to learn how to program and there are some bugs in his code.

Here's what Jason wrote:

```python
offense = False
defense = False
rule_changes = False

def set_offense():
    offense = True

def set_defense():
    defense = True

    def set_rule_changes():
        rule_changes = True

    if offense and defense:
        set_rule_changes()

set_offense()
set_defense()

print("How are the Jags doing?\n")
print("We have offense:", offense)
print("We have defense:", defense)
print("We have some rule changes:", rule_changes)

if offense and defense and rule_changes:
    print("We're going to the Super Bowl!")
else:
    print("I can't predict the future, but no, the Jaguars will never win the Super Bowl.")
```

## Expected Output

Here's what Jason expected the program to output:

```
How are the Jags doing?

We have offense: True
We have defense: True
We have some rule changes: True
We're going to the Super Bowl!
```

## Actual Output

Here's what Jason actually saw instead:

```
How are the Jags doing?

We have offense: False
We have defense: False
We have some rule changes: False
I can't predict the future, but no, the Jaguars will never win the Super Bowl.
```

## Your Job

Jason heard that you're nearly halfway through the **Python Programming** course at GA, so he's asked you for help in fixing his code.

Your job is to fix the bugs in his code so that the expected output is produced.

Do this in a file called `part2.py`.

**Hint:** Include a bunch of `print` statements everywhere to print out the values of the variables at various times. For example, inside `set_offense()`, put a `print` statement like `print("offense is", offense)`.

---

# See Ya Later!

You're all done. Bye now!

![](https://media.giphy.com/media/fWgQH01z4rjwrZckyM/giphy.gif)