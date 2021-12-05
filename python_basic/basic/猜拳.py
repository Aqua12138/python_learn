import random
user_choice=None
computer_choice=None
#电脑出拳
def computer_think():
    global computer_choice
    global hand_list
    hand_list=['石头','剪刀','布']
    computer_choice=random.choice(hand_list) 
#我出拳
def me_think():
    global user_choice
    user_choice=input('石头 剪刀 布\n请选择：')
#比较
def winner():
    if user_choice==hand_list[hand_list.index(computer_choice)-1]:#index【
        print('你赢了！')
    elif user_choice==hand_list[hand_list.index(computer_choice)-2]:
        print('你输了。')
    else:
        print('平局')
def main():
    me_think()
    computer_think()
    print('电脑出了{}'.format(computer_choice))
    winner()
main()


    