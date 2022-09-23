# dict-wrapper
A dict wrapper for python (deep option)
# What is the deep option?
A new way to reach from deep data
<br>
example
```py
{"hello": {"hi": "heyyy"}, "hey", "hi"}
```
To make the deeper data ({"hi": "heyyy"}) into the surface we will use the deep function or the deep algorithm
<br>
(most of our functions doesn't use the deep function, they use the deep algorithm)
<br>
# the functions
## deep
```py
(data: dict, *, still: bool = True) -> dict
```
### what's the point?
Not having to make an entire algorithm for one thing of the code
### data?
Data is the dict that you want to have the deeper dicts (in it) into the surface
### still?
The still kwargs is if the data is a dict doesn't it will multiplicate it?
<br>
for exemple
```py
# original
{"Hello": "fortnite", "hi": {"e": 'qwe'}}
# false
{'Hello': 'fortnite', 'e': 'qwe'}
# true
{'Hello': 'fortnite', 'e': 'qwe', 'hi': {'e': 'qwe'}}
```
## deeps
Same thing of deep but with more dicts
```py
(*dicts, still: bool = True) -> dict
```
### what's the point?
Not having to make a small algorithm for one thing of the code
### still?
The still kwargs is if the data is a dict doesn't it will multiplicate it?
