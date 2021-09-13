# Домашнее задание Камашева Рафаэля 1.1.
## Упражнение 2.

>Напишите свою собственную упрощенную оболочку (shell). Он должен читать
пользовательский ввод и иметь возможность запускать команду без параметров, таких
как pwd, ls, top, pstree и т.д. Сохраните код в Робокод.
• Подсказка: используйте команду man

###
Простейшей программой, приходящей на ум является
`cat | sh` или `cat | bash`
cat принимает stdin построчно, sh или bash ее тут же выполняют, что в итоге дает
интерактивную консоль.

Можно сделать чуть сложнее:
```shell
#!/bin/bash

# считаем построчно stdin
while read line
do
    # выполним строку
    eval $line  
done < "${1:-/dev/stdin}"
```
Сохранил скрипт в shell.sh.
Затем 
```shell
сhmod +x shell.sh
./shell.sh
```

Теперь можно вводить команды и получать результат по каждой строке