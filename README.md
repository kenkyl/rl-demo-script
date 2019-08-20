# rl-demo-script

## Description
This small python script inserts the values 1-100 into a redis db instance and then reads and prints the same values in reverse from a separate, replicated redis db instance. 

## Instructions
- Set the host and port values to those of the source and target redis db instances
- Use `pip` to install the `redis` python module 
- Run:
```
python rl-demo-script.py
```
Note that replication from the source to target database must be enabled first. 