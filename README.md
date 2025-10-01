# dancingMiku
dancing miku gif runs from bash

nvim ~/.bashrc
(or nano or whatever)

at the bottom put:


alias miku="(nohup python3 PATH_TO_PYTHON_FILE >/dev/null 2>&1 & ) >/dev/null 2>&1"
alias mikoff="pkill -f 'PATH_TO_PYTHON_FILE' >/dev/null 2>&1 || true"

save it 
then reload the bashrc

source ~/.bashrc


type miku to run
mikoff to close 


