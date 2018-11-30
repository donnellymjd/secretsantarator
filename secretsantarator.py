## This secret santa generator code will give the same result every time if you enter the names in the same order. 
## If you'd like a new random order just adjust the number in line 4 (random.seed(1225)).
import random
random.seed(1225)

input_func = None
try:
    input_func = raw_input
except NameError:
    input_func = input

participants = []

n_parts_int = None

while (n_parts_int == None) | (n_parts_int<3):
	n_parts = (input_func("How many people are participating in your secret santa? "))

	try:
		n_parts_int = int(n_parts)
	except:
		print("Please enter a valid number.")

	if n_parts_int<3:
		print("Please enter a number greater than 2.")

for _ in range(n_parts_int):
	name = input_func("Please enter the name of a participant here: ")

	participants.append(name)
	print('Current participants are: {}'.format(participants))

random.shuffle(participants)
recipients = [x for x in participants]
remaining_givers = [x for x in participants]


print(r"""
                                         ,;7,
                                       _ ||:|,
                     _,---,_           )\'  '|
                   .'_.-.,_ '.         ',')  j
                  /,'   ___}  \        _/   /
      .,         ,1  .''  =\ _.''.   ,`';_ |
    .'  \        (.'T ~, (' ) ',.'  /     ';',
    \   .\(\O/)_. \ (    _Z-'`>--, .'',      ;
     \  |   I  _|._>;--'`,-j-'    ;    ',  .'
    __\_|   _.'.-7 ) `'-' "       (      ;'
  .'.'_.'|.' .'   \ ',_           .'\   /
  | |  |.'  /      \   \          l  \ /
  | _.-'   /        '. ('._   _ ,.'   \i
,--' ---' / k  _.-,.-|__L, '-' ' ()    ;
 '._     (   ';   (    _-}             |
  / '     \   ;    ',.__;         ()   /
 /         |   ;    ; ___._._____.: :-j
|           \,__',-' ____: :_____.: :-\
|               F :   .  ' '        ,  L
',             J  |   ;             j  |
  \            |  |    L            |  J
   ;         .-F  |    ;           J    L
    \___,---' J'--:    j,---,___   |_   |
              |   |'--' L       '--| '-'|
               '.,L     |----.__   j.__.'
                | '----'   |,   '-'  }
                j         / ('-----';
               { "---'--;'  }       |
               |        |   '.----,.'
               ',.__.__.'    |=, _/
                |     /      |    '.
                |'= -x       L___   '--,
          snd   L   __\          '-----'
                 '.____)
 	    __  __ ____ ____  ____  _  _
 	    |,\/,| |[_' |[_]) |[_]) \\//
 	    ||\/|| |[_, ||'\, ||'\,  ||

            ___ __ __ ____  __  __  ____  _  _    __    __
           // ' |[_]| |[_]) || ((_' '||' |,\/,|  //\\  ((_'
           \\_, |[']| ||'\, || ,_))  ||  ||\/|| //``\\ ,_))
           """)


print('Here is the drawing!')

for participant in participants:
    possible_recipients = [recipient for recipient in recipients if recipient != participant]
    remaining_givers.remove(participant)
    rand_idx = random.randint(0,len(possible_recipients)-1)
    if (len(remaining_givers) == 1):
        if (remaining_givers[0] in possible_recipients):
            recipient = remaining_givers[0]
        else:
            recipient = possible_recipients[rand_idx]
    else:
        recipient = possible_recipients[rand_idx]
    print('{0} is giving to {1}'.format(participant,recipient))
    recipients.remove(recipient)