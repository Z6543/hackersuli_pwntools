from pwntools/pwntools:latest


COPY .tmux.conf /home/pwntools/.tmux.conf
RUN sudo apt update
RUN sudo apt install -y gdb net-tools gdbserver tmux 
