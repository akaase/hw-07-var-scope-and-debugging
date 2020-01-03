# Assignment: Variable Scope and Debugging

In this homework, you're going to answer some reading comprehension questions and write code for a challenge problem.

You will practice these programming concepts we've covered in class:

* Variable Scope
* Debugging

## Deliverables and Submitting

You know what you're doing by now! **Fork**/**Clone**/**Commit**/**Push**/**Submit** :grin:

---

# Exercise 1: We're in a Good Place!

Jason is a huge Jacksonville Jaguars fan. The team isn't doing great now, but he has faith: *"All we need is a defense, and an offense, and finally some rule changes!"*

He wrote some code to predict the future for the Jaguars according to whether we have all three of those factors.

## Starter Code

Unfortunately, Jason is just starting to learn how to program and his code isn't very well written.

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

set_offense()
set_defense()
if offense and defense:
    set_rule_changes()

print('How are the Jags doing?\n')
print('We have offense:', offense)
print('We have defense:', defense)
print('We have some rule changes:', rule_changes)

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

Jason heard that you're a third through the **Python Programming** course at GA, so he's asked you for help in fixing his code.

Your job is to fix the bugs in his code so that the expected output is produced.

Do this in a file called `exercise1.py`.

**Hint:** Include a bunch of `print` statements everywhere to print out the values of the variables at various times. For example, inside `set_offense()`, put a `print` statement like `print('offense is', offense)`.

---

# Exercise 2: 

Go through the **Introduction to Debugging** chapter of the **Foundations of Python Programming** ebook.

The chapter has a total of 8 pages, each of them containing a few interactive problems.

Start from [Page 1](https://runestone.academy/runestone/books/published/fopp/Debugging/intro-DebuggingGeneral.html) and use the arrows on the bottom to go to the next page, until you finish all 8 pages.

Focus in particular on Chapter 3.8: Know Your Error Messages!

Nothing to submit for this exercise -- just go through the problems, answer them, check your answer, and learn from the problems! 

---

# Debugging: It Could be a lot Worse!

At least it's not **real** bugs...

![](https://media.giphy.com/media/EvsgzxSJjRQWY/giphy.gif)
