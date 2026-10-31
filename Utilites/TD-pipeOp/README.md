# TD-pipeOp

TD-pipeOp provides a pair of palette .tox files that easily allow TouchDesigner users to quickly pack multiple operator connection cables into a single DAT link and then un-pack them back into separate connections at the other end.

## Why is this useful?

### Some Background: COMP Modules
As TouchDesigner projects become more complex, a common organizational strategy is to sort Operators that govern various operations into high level COMPs. 
![image](https://hackmd.io/_uploads/BJ-UAcmebl.png)
![image](https://hackmd.io/_uploads/BJOPkj7lWg.png)
This is also very helpful for externalized .tox workflows where projects are broken up into multiple parts for modular and collaborative development.

### The Problem: Wrangling Connections
Unfortunately it's quite easy to wind up with this:

![image](https://hackmd.io/_uploads/BJnNejQx-l.png)

Having to wrangle multiple connections at the top level gets a bit ugly and the process of managing the in and out pins is fairly cumbersome.

### The Fix: Trunking multiple connections into a single cable

Add the pipeIn Op to the COMP with outputs you'd like to route. Drop any number or type of operators onto the active Container.

![pipeIn example](https://hackmd.io/_uploads/rygag27gbx.gif)

https://hackmd.io/_uploads/rygag27gbx.gif

Any Operators dropped onto the pipeIn COMP are added to the list of sent OPs. The output can be routed to anywhere.

![pipeOut example](https://hackmd.io/_uploads/BJ1b-n7gZx.gif)

https://hackmd.io/_uploads/BJ1b-n7gZx.gif

At the other end, place a pipeOut Op and route the DAT cable from the pipeIn Op into it. Output pins for the referenced operators are automatically created for you. These can be used in place of multiple COMP inputs.

Pressing the "Show InPipe" button on the pipeOut Op's Parameter sheet quickly shows the source pipeIn in a floating window for editing.

![image](https://hackmd.io/_uploads/HJEpMhQeWl.png)

Extra sources can be dropped onto the pipeIn. Existing links can be deleted by pressing the 'X'.

![image](https://hackmd.io/_uploads/HkfeXhmxbx.png)

### All Operator types are supported =)
![image](https://hackmd.io/_uploads/SkHWN3XeZe.png)

Enjoy! -F
