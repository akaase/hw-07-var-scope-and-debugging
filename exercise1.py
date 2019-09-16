# EXPLANATION:
# When you forget to use the "global" keyword, you are inadvertently creating a new
# local variable within each function. These are separate unrelated variables just
# happen to share a name! That is why they had no effect on the values of the
# global variables the way that it was originally written.

offense = False
defense = False
rule_changes = False

def set_offense():
    global offense
    offense = True

def set_defense():
    global defense
    defense = True

def set_rule_changes():
    global rule_changes
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
