# hackersuli_pwntools

The hmi_coolant binary was part of FIRST CTF 2021

prereqs:
	git
	docker
	optional: ghidra

git clone https://github.com/Z6543/hackersuli_pwntools

docker build --tag pwnv1 .

docker run -it -v `pwd`:/home/pwntools pwnv1 /bin/bash tmux

Inside docker: 


RET2WIN
pwn -h
pwn template -h




HMI_COOLANT
pwn template hmi_coolant --host 127.0.0.1 --port 5050 > exploit.py

start tmux
./exploit.py DEBUG GDB 


