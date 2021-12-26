from pwntools/pwntools:latest


COPY .tmux.conf /home/pwntools/.tmux.conf
RUN sudo apt update
RUN sudo apt install -y gdb net-tools gdbserver tmux 
RUN git clone https://github.com/hugsy/gef.git
RUN echo source `pwd`/gef/gef.py >> /home/pwntools/.gdbinit

#ENV TERM xterm-256color
#ENV LANG C.UTF-8
#ENV CHARSET UTF-8
#ENV LC_COLLATE C
