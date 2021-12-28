# hackersuli_pwntools

The ret2win binary is part of the Ropemporium project. 
The hmi_coolant binary was part of FIRST CTF 2021.

## prereqs
```
	git
	docker
	Recommended: 2 displays (one for the stream, 1 for the challenges), or one 4K
	optional: Ghidra 10.1.1 or later
```

## Note about binary CTF challenges
```
┌───────────────┐                  ┌───────────────┐
│ your computer │      TCP         │remote computer│
│         ──────┼────────────────► │               │
│pwntools       │                  │               │
│   ┌───────┐   │                  │  ┌───────┐    │
│ │ │binary │   │                  │  │binary │    │
│ │ │       │   │                  │  │       │    │
│ │ │       │   │                  │  │       │    │
│ │ └───────┘   │                  │  └───────┘    │
│ ▼             │                  │               │
│GDB            │                  │               │
└───────────────┘                  └───────────────┘	
```
```
git clone https://github.com/Z6543/hackersuli_pwntools

cd hackersuli_pwntools

docker build --tag pwnv1 .

docker run --rm -it -v `pwd`:/home/pwntools pwnv1 /usr/bin/tmux
```

Inside docker: 

## RET2WIN - chall_1

### Task: Analyze the ret2win binary, and get the flag!

Use strings, use ghidra.   
```
pwn -h
pwn template -h
pwn template ret2win > exploit.py
```

## HMI_COOLANT chall_2

### Tasks
Task1: Login as engineer.
Task2: Login as administrator.
Task3: Execute arbitrary commands.

```
pwn template hmi_coolant --host 127.0.0.1 --port 5050 > exploit.py

./exploit.py DEBUG GDB 
```