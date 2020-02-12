import random

class Ochko_session:
    def __init__(self):
        self.cards = {'Ah':1, 'Ad':1,'Ac':1,'As':1, 'Kh':4, 'Kd':4,'Kc':4,'Ks':4,
                      'Qh':3, 'Qd':3,'Qc':3,'Qs':3, 'Jh':2, 'Jd':2,'Jc':2,'Js':2,
                      'Th':10, 'Td':10,'Tc':10,'Ts':10, '9h':9, '9d':9,'9c':9,'9s':9,
                      '8h':8, '8d':8,'8c':8,'8s':8, '7h':7, '7d':7,'7c':7,'7s':7,
                      '6h':6, '6d':6,'6c':6,'6s':6}
        self.cards_in_game = []
        self.user_hand = [0]
        self.bot_hand = [0]
        self.in_game = 0
        
        
    def start_game(self):
        self.in_game = 1
        self.cards_in_game = ['Ah', 'Ad','Ac','As', 'Kh', 'Kd','Kc','Ks',
                      'Qh', 'Qd','Qc','Qs', 'Jh', 'Jd','Jc','Js',
                      'Th', 'Td','Tc','Ts', '9h', '9d','9c','9s',
                      '8h', '8d','8c','8s', '7h', '7d','7c','7s',
                      '6h', '6d','6c','6s']
        self.user_hand = [0]
        self.user_hand.append(self.cards_in_game.pop(random.randint(0,35)))
        self.user_hand.append(self.cards_in_game.pop(random.randint(0,34)))
        self.user_hand[0] = self.cards[self.user_hand[1]]+self.cards[self.user_hand[2]]
        return [('В вашей руке: ' + ', '.join(self.user_hand[1:]) + '. Всего: '+str(self.user_hand[0])+'. Доступные команды: еще, хватит, выход'),
                self.user_hand[1:]]
        
        
    def take_message(self, message):
        if message == 'выход':
            return message
        elif self.in_game == 0:
            if message == 'старт':
                return self.start_game()
            else:
                return ['Доступные команды: старт, выход', ['joker']]
        elif message == 'еще':
            self.user_hand.append(self.cards_in_game.pop(random.randint(0,(len(self.cards_in_game)-1))))
            self.user_hand[0] += self.cards[self.user_hand[-1]]
            if self.user_hand[0] > 21:
                self.in_game = 0
                return [('Перебор: ' + ', '.join(self.user_hand[1:]) + '. Чтобы играть снова напишите: старт; для выхода из игры: выход'),
                        self.user_hand[1:]]
            return [('В вашей руке: ' + ', '.join(self.user_hand[1:]) + '. Всего: '+str(self.user_hand[0])+'. Доступные команды: еще, хватит, выход'),
                    self.user_hand[1:]]
        elif message == 'хватит':
            return self.bot_game()
        else:
            return ['Доступные команды: еще, хватит, выход', ['joker']]

    def bot_game(self):
        self.in_game = 0
        self.bot_hand = [0]
        while self.bot_hand[0]<17:
            self.bot_hand.append(self.cards_in_game.pop(random.randint(0,(len(self.cards_in_game)-1))))
            self.bot_hand[0] += self.cards[self.bot_hand[-1]]
        if self.bot_hand[0] > 21:
            return [("У бота перебор) " + ', '.join(self.bot_hand[1:]) + '. Чтобы играть снова напишите: старт; для выхода из игры: выход'),
                    self.bot_hand[1:]]
        elif self.bot_hand[0] < self.user_hand[0]:
            return [("Вы выиграли! " + ', '.join(self.bot_hand[1:]) + '. Чтобы играть снова напишите: старт; для выхода из игры: выход'),
                    self.bot_hand[1:]]
        elif self.bot_hand[0] > self.user_hand[0]:
            return [("Вы проиграли( " + ', '.join(self.bot_hand[1:]) + '. Чтобы играть снова напишите: старт; для выхода из игры: выход'),
                    self.bot_hand[1:]]
        else:
            return [("Ничья! " + ', '.join(self.bot_hand[1:]) + '. Чтобы играть снова напишите: старт; для выхода из игры: выход'),
                    self.bot_hand[1:]]
    


            
